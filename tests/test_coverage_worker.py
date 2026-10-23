"""Collection jobs retain checkpoints and never promote automated research drafts."""
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import sys
import tempfile
import urllib.error
import unittest
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import coverage_worker as worker
from coverage_store import CoverageStore


CIK = '0000000001'
COMPANY = {'cik': CIK, 'ticker': 'TEST', 'company_name': 'Test Issuer', 'exchange': 'NASDAQ', 'security_type': 'common_stock'}
ACC1 = '0000000001-25-000001'
ACC2 = '0000000001-26-000001'
TAG = 'RevenueFromContractWithCustomerExcludingAssessedTax'


def submissions(accession=ACC1, filed='2025-08-01', end='2025-06-30', cik=CIK):
    return {'cik': cik, 'name': 'Test Issuer', 'filings': {'recent': {
        'form': ['10-K'], 'accessionNumber': [accession], 'filingDate': [filed], 'reportDate': [end]}}}


def financial_facts(new=False, cik=1):
    rows = [{'val': 1000, 'start': '2024-07-01', 'end': '2025-06-30', 'filed': '2025-08-01',
             'form': '10-K', 'fy': 2025, 'fp': 'FY', 'accn': ACC1}]
    if new:
        rows.append({'val': 1200, 'start': '2025-07-01', 'end': '2026-06-30', 'filed': '2026-08-01',
                     'form': '10-K', 'fy': 2026, 'fp': 'FY', 'accn': ACC2})
    return {'cik': cik, 'entityName': 'Test Issuer', 'facts': {'us-gaap': {TAG: {'label': 'Revenue', 'units': {'USD': rows}}}}}


class Clock:
    def __init__(self):
        self.value = datetime(2025, 9, 1, tzinfo=timezone.utc)

    def __call__(self):
        return self.value


class FakeFetcher:
    def __init__(self, clock):
        self.clock = clock
        self.responses = {}
        self.calls = []
        self.sec_block = None

    def fetch(self, url, refresh=False):
        if getattr(self, 'before_request', None):
            self.before_request(url)
        self.calls.append(url)
        response = self.responses[url]
        if isinstance(response, Exception):
            if 'SEC access blocked' in str(response):
                self.sec_block = str(response)
            raise response
        raw = json.dumps(response).encode()
        return raw, {'sha256': worker.p.digest(raw), 'fetched_at': self.clock().isoformat()}


class CoverageWorkerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.clock = Clock()
        self.env = patch.dict('os.environ', {'STOCK_BRAIN_SEC_ENABLED': '1'})
        self.env.start()
        self.store = CoverageStore(self.root / 'coverage.sqlite3', clock=self.clock)
        self.store.seed_companies([COMPANY])
        self.fetcher = FakeFetcher(self.clock)
        # Fixture identity is used only with an injected fetcher, never a live request.
        self.provider = worker.SecFinancialProvider(self.root, user_agent='StockBrain fixture qa@fixture.test',
                                                    fetcher=self.fetcher, sleep=self.advance_clock)
        self.runner = worker.CoverageWorker(self.store, self.provider, root=self.root, clock=self.clock)
        self.sub_url = f'https://data.sec.gov/submissions/CIK{CIK}.json'
        self.fact_url = f'https://data.sec.gov/api/xbrl/companyfacts/CIK{CIK}.json'
        self.fetcher.responses[self.sub_url] = submissions()
        self.fetcher.responses[self.fact_url] = financial_facts()

    def advance_clock(self, seconds):
        self.clock.value += timedelta(seconds=seconds)

    def tearDown(self):
        self.env.stop()
        self.temp.cleanup()

    def run_job(self):
        self.store.enqueue(CIK)
        return self.runner.run('test-worker', limit=3)

    def test_online_runner_leaves_bulk_queue_untouched(self):
        bulk = self.store.enqueue(CIK, kind='refresh_company_bulk')
        result = self.run_job()
        self.assertEqual((result['processed'], result['succeeded']), (1, 1))
        with self.store._connection() as db:
            row = db.execute('SELECT status,attempts FROM jobs WHERE id=?', (bulk['job_id'],)).fetchone()
        self.assertEqual(tuple(row), ('queued', 0))

    def test_unchanged_filing_skips_facts_and_does_not_replace_draft(self):
        first = self.run_job()
        self.assertEqual(first['succeeded'], 1)
        previous = self.store.get_payload(CIK, 'history')
        draft = self.store.get_payload(CIK, 'automatic_changes')
        self.clock.value += timedelta(days=1)
        second = self.run_job()
        self.assertEqual(second['jobs'][0]['action'], 'filing_unchanged')
        self.assertEqual(self.fetcher.calls.count(self.fact_url), 1)
        self.assertEqual(previous, self.store.get_payload(CIK, 'history'))
        self.assertEqual(draft, self.store.get_payload(CIK, 'automatic_changes'))

    def test_reported_industry_is_retained_with_submission_source_not_inferred_sector(self):
        self.fetcher.responses[self.sub_url].update(sic='2834', sicDescription='Pharmaceutical preparations', entityType='operating')
        self.assertEqual(self.run_job()['succeeded'], 1)
        record = self.store.get_payload(CIK, 'submissions')
        self.assertEqual(record['issuer']['sic'], '2834')
        self.assertEqual(record['issuer']['sic_description'], 'Pharmaceutical preparations')
        self.assertEqual(record['source']['url'], self.sub_url)
        self.assertNotIn('sector', record['issuer'])
        for invalid in ('unknown', True, -1, 12345, None):
            result = worker.issuer_metadata({'cik': CIK, 'sic': invalid}, CIK)
            self.assertIsNone(result['sic'])
            self.assertEqual(result['classification_status'], 'missing_or_invalid_sic')
        self.assertEqual(worker.issuer_metadata({'cik': CIK, 'sic': 100}, CIK)['sic'], '0100')

    def test_changed_filing_produces_source_linked_unreviewed_neutral_draft(self):
        self.run_job()
        self.clock.value = datetime(2026, 9, 1, tzinfo=timezone.utc)
        self.fetcher.responses[self.sub_url] = submissions(ACC2, '2026-08-01', '2026-06-30')
        self.fetcher.responses[self.fact_url] = financial_facts(new=True)
        report = self.run_job()
        self.assertEqual(report['succeeded'], 1)
        draft = self.store.get_payload(CIK, 'automatic_changes')
        self.assertEqual(draft['status'], 'draft')
        self.assertEqual(draft['review_status'], 'unreviewed')
        self.assertFalse(draft['canonical_reviewed'])
        revenue = next(row for row in draft['changes'] if row['metric'] == 'revenue')
        self.assertEqual((revenue['period_start'], revenue['period_end']), ('2025-07-01', '2026-06-30'))
        self.assertEqual((revenue['previous_period_start'], revenue['previous_period_end']), ('2024-07-01', '2025-06-30'))
        self.assertEqual(revenue['delta'], 200)
        self.assertIn(worker.fh.filing_url(CIK, ACC2), revenue['source_urls'])
        self.assertEqual(draft['classification'], 'quality_review_required')
        self.assertFalse((self.root / 'research/reviews').exists())

    def test_failed_facts_preserves_all_prior_payloads_and_processed_accession(self):
        self.run_job()
        previous = {kind: self.store.get_payload(CIK, kind) for kind in ('history', 'submissions', 'automatic_changes', 'collector_state')}
        self.clock.value = datetime(2026, 9, 1, tzinfo=timezone.utc)
        self.fetcher.responses[self.sub_url] = submissions(ACC2, '2026-08-01', '2026-06-30')
        self.fetcher.responses[self.fact_url] = ValueError('bad source document')
        result = self.run_job()
        self.assertEqual(result['failed'], 1)
        for kind, value in previous.items():
            self.assertEqual(value, self.store.get_payload(CIK, kind))

    def test_not_yet_ingested_filing_retains_checkpoint_for_retry(self):
        self.run_job()
        previous = self.store.get_payload(CIK, 'history')
        self.clock.value = datetime(2026, 9, 1, tzinfo=timezone.utc)
        self.fetcher.responses[self.sub_url] = submissions(ACC2, '2026-08-01', '2026-06-30')
        result = self.run_job()
        self.assertEqual(result['failed'], 1)
        self.assertIn('not yet available', result['jobs'][0]['error'])
        self.assertEqual(previous, self.store.get_payload(CIK, 'history'))
        self.assertEqual(self.store.get_payload(CIK, 'collector_state')['latest_financial_accession'], ACC1)

    def test_irrelevant_new_accession_fact_does_not_advance_processed_filing(self):
        self.run_job()
        previous = self.store.get_payload(CIK, 'history')
        self.clock.value = datetime(2026, 9, 1, tzinfo=timezone.utc)
        self.fetcher.responses[self.sub_url] = submissions(ACC2, '2026-08-01', '2026-06-30')
        partial = financial_facts()
        partial['facts']['us-gaap']['UnrelatedConcept'] = {'units': {'USD': [{'accn': ACC2, 'val': 1}]}}
        self.fetcher.responses[self.fact_url] = partial
        result = self.run_job()
        self.assertEqual(result['failed'], 1)
        self.assertIn('not yet normalized', result['jobs'][0]['error'])
        self.assertEqual(previous, self.store.get_payload(CIK, 'history'))
        self.assertEqual(self.store.get_payload(CIK, 'collector_state')['latest_financial_accession'], ACC1)

    def test_stable_cik_ticker_rename_does_not_block_new_filing(self):
        self.run_job()
        self.clock.value = datetime(2026, 9, 1, tzinfo=timezone.utc)
        listings = {'fields': ['cik', 'name', 'ticker', 'exchange'], 'data': [[CIK, 'Test Issuer', 'RENAMED', 'NASDAQ']]}
        source = {'url': 'https://www.sec.gov/files/company_tickers_exchange.json',
                  'retrieved_at': self.clock().isoformat(), 'sha256': worker.encoded_digest(listings)}
        self.store.import_listings(listings, source, complete=True)
        self.fetcher.responses[self.sub_url] = submissions(ACC2, '2026-08-01', '2026-06-30')
        self.fetcher.responses[self.fact_url] = financial_facts(new=True)
        result = self.run_job()
        self.assertEqual(result['succeeded'], 1)
        self.assertEqual(self.store.get_payload(CIK, 'history')['ticker'], 'RENAMED')
        self.assertEqual(self.store.get_payload(CIK, 'automatic_changes')['identity_changes'][0]['previous'], 'TEST')

    def test_shared_sec_block_stops_batch_before_next_issuer(self):
        other = {**COMPANY, 'cik': '0000000002', 'ticker': 'OTHER'}
        self.store.seed_companies([other])
        self.store.enqueue(CIK)
        self.store.enqueue(other['cik'])
        self.fetcher.responses[self.sub_url] = ValueError('SEC access blocked (HTTP 403); remaining requests skipped')
        result = self.runner.run('test-worker', limit=100)
        self.assertEqual(result['processed'], 1)
        self.assertEqual(result['failed'], 1)
        self.assertIsNotNone(result['stopped_reason'])
        self.assertEqual(len(self.fetcher.calls), 1)
        remaining = self.store.claim('other-worker', now=self.clock().isoformat())
        self.assertEqual(remaining['cik'], other['cik'])
        self.assertIsNone(self.store.get_payload(CIK, 'history'))
        reopened = CoverageStore(self.root / 'coverage.sqlite3', clock=self.clock)
        fresh_provider = worker.SecFinancialProvider(self.root, user_agent='StockBrain fixture qa@fixture.test',
                                                    fetcher=FakeFetcher(self.clock), sleep=self.advance_clock)
        next_runner = worker.CoverageWorker(reopened, fresh_provider, root=self.root, clock=self.clock)
        second_run = next_runner.run('another-process', limit=100)
        self.assertEqual(second_run['processed'], 0)
        self.assertIn('persisted cooldown', second_run['stopped_reason'])
        self.assertEqual(fresh_provider.fetcher.calls, [])

    def test_paused_sec_and_dry_run_do_not_claim_jobs_or_fetch(self):
        self.store.enqueue(CIK)
        self.assertEqual(self.runner.run('test-worker', dry_run=True)['processed'], 0)
        with patch.dict('os.environ', {'STOCK_BRAIN_SEC_ENABLED': '0'}):
            result = self.runner.run('test-worker')
        self.assertEqual(result['processed'], 0)
        self.assertIn('paused', result['stopped_reason'])
        self.assertEqual(self.fetcher.calls, [])
        self.assertIsNotNone(self.store.claim('other-worker', now=self.clock().isoformat()))

    def test_company_identity_mismatch_cannot_write_another_issuers_data(self):
        self.fetcher.responses[self.fact_url] = financial_facts(cik=2)
        result = self.run_job()
        self.assertEqual(result['failed'], 1)
        self.assertIsNone(self.store.get_payload(CIK, 'history'))
        self.assertIsNone(self.store.get_payload(CIK, 'automatic_changes'))

    def test_malformed_company_facts_isolated_from_next_issuer(self):
        other = {**COMPANY, 'cik': '0000000002', 'ticker': 'OTHER'}
        self.store.seed_companies([other])
        self.store.enqueue(CIK)
        self.store.enqueue(other['cik'])
        self.fetcher.responses[self.fact_url] = {'cik': 1, 'facts': None}
        self.fetcher.responses[f'https://data.sec.gov/submissions/CIK{other["cik"]}.json'] = submissions(cik=other['cik'])
        self.fetcher.responses[f'https://data.sec.gov/api/xbrl/companyfacts/CIK{other["cik"]}.json'] = financial_facts(cik=2)
        result = self.runner.run('test-worker', limit=2)
        self.assertEqual((result['processed'], result['failed'], result['succeeded']), (2, 1, 1))
        self.assertIsNone(self.store.get_payload(CIK, 'history'))
        self.assertEqual(self.store.get_payload(other['cik'], 'history')['cik'], other['cik'])

    def test_missing_or_placeholder_contact_is_not_ready(self):
        for identity in ('unlabeledbot', 'StockBrain support@example.com', 'StockBrain contact@invalid.test'):
            self.provider.user_agent = identity
            self.assertFalse(self.provider.readiness()['ready'])

    def test_mid_job_shared_cooldown_defers_instead_of_terminally_blocking(self):
        original = self.fetcher.fetch
        def racing_fetch(url, refresh=False):
            result = original(url, refresh)
            if url == self.sub_url:
                self.store.pause_source('sec', seconds=60, reason='Another worker received HTTP429')
            return result
        self.fetcher.fetch = racing_fetch
        result = self.run_job()
        self.assertEqual(result['failed'], 1)
        self.assertFalse(result['jobs'][0]['blocked'])
        self.clock.value += timedelta(seconds=61)
        retried = self.store.claim('next-worker', now=self.clock().isoformat())
        self.assertIsNotNone(retried)
        self.assertEqual(retried['cik'], CIK)

    def test_mid_job_operator_pause_leaves_job_retryable(self):
        original = self.fetcher.fetch
        def racing_fetch(url, refresh=False):
            result = original(url, refresh)
            worker.os.environ['STOCK_BRAIN_SEC_ENABLED'] = '0'
            return result
        self.fetcher.fetch = racing_fetch
        result = self.run_job()
        self.assertEqual(result['failed'], 1)
        self.assertFalse(result['jobs'][0]['blocked'])
        self.assertFalse(self.store.source_status('sec')['blocked'])
        self.assertEqual(self.fetcher.calls, [self.sub_url])
        self.clock.value += timedelta(hours=2)
        self.assertIsNotNone(self.store.claim('next-worker', now=self.clock().isoformat()))

    def test_retry_after_is_persisted_across_worker_instances(self):
        error = urllib.error.HTTPError(self.sub_url, 429, 'slow down', {'Retry-After': '172800'}, None)
        policy = self.provider.failure_policy(error)
        self.assertFalse(policy['blocked'])
        self.assertTrue(policy['stop_batch'])
        self.assertEqual(self.store.source_status('sec')['wait_seconds'], 172800)

    def test_fetcher_calls_persistent_guard_for_every_retry(self):
        guard = Mock()
        fetcher = worker.p.Fetcher(self.root, 'StockBrain fixture qa@fixture.test', before_request=guard)
        response = Mock()
        response.url = self.sub_url
        response.headers = {'Content-Type': 'application/json'}
        response.read.return_value = b'{}'
        response.__enter__ = Mock(return_value=response)
        response.__exit__ = Mock(return_value=False)
        retry = urllib.error.HTTPError(self.sub_url, 503, 'temporary', {'Retry-After': '0'}, None)
        with patch('research_pipeline.urllib.request.urlopen', side_effect=[retry, response]), patch('research_pipeline.time.sleep'):
            fetcher.fetch(self.sub_url, refresh=True)
        self.assertEqual(guard.call_count, 2)


if __name__ == '__main__':
    unittest.main()
