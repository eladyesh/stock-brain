import copy
from datetime import datetime, timezone
import json
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import disclosure_monitor as monitor
import research_pipeline as pipeline
import verify_runtime as verifier


class SourceObservationTests(unittest.TestCase):
    def test_sec_retrieval_timestamp_comes_from_the_source_receipt(self):
        payload = {'cik': '0000789019', 'filings': {'recent': {
            'form': [], 'filingDate': [], 'accessionNumber': [], 'primaryDocument': []}}}
        fetched_at = '2020-10-21T22:00:00+00:00'
        fetcher = SimpleNamespace(fetch=lambda *args, **kwargs: (json.dumps(payload).encode(), {'fetched_at': fetched_at}))
        receipt = {}
        result = monitor.discover_sec({'ticker': 'MSFT', 'cik': '0000789019'},
            {'as_of': '2020-10-01', 'sources': []}, fetcher, '2020-10-22', receipt=receipt)
        self.assertEqual(result, [])
        self.assertEqual(receipt['retrieved_at'], fetched_at)

    def test_sec_failure_does_not_stop_or_conceal_successful_issuer_scan(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            packet_path = root / 'research/pilot/MSFT.json'
            pipeline.write_json(packet_path, {'as_of': '2020-10-01', 'sources': []})
            pipeline.write_json(root / 'config/discovery.json',
                                {'issuer_feeds': {'MSFT': ['https://issuer.example/feed']}})
            body = b'<rss><channel><item><title>Results</title><link>https://issuer.example/results</link><pubDate>2020-10-20</pubDate></item></channel></rss>'
            fetcher = SimpleNamespace(fetch=lambda *args, **kwargs: (body, {'fetched_at': '2020-10-22T01:01:00+00:00'}))
            with patch.object(pipeline, 'universe', return_value=[{'ticker': 'MSFT', 'cik': '0000789019'}]), \
                 patch.object(pipeline, 'managed_packet_path', return_value=packet_path), \
                 patch.object(monitor.kb, 'documents', return_value=[SimpleNamespace(metadata={'ticker': 'MSFT', 'status': 'stub'})]), \
                 patch('review_gates.check_managed_reviews'), patch('triage_disclosures.active_dispositions', return_value={}), \
                 patch.object(monitor, 'discover_sec', side_effect=OSError('SEC collection paused by operator')), \
                 patch.object(monitor, 'utc_now', return_value='2020-10-22T01:00:00+00:00'):
                result = monitor.run(root, 'test', '2020-10-22', fetcher=fetcher)
                first = result['companies']['MSFT']
                self.assertEqual(first['coverage_status'], 'error')
                self.assertEqual(first['sec_coverage_status'], 'error')
                self.assertEqual(first['issuer_coverage_status'], 'checked')
                self.assertIsNone(first['last_successful_scan_at'])
                self.assertEqual(result['queue'][0]['status'], 'pending_review')
                self.assertEqual(first['source_checks'][1]['last_successful_check_at'], first['checked_at'])
                self.assertEqual(first['source_checks'][1]['retrieved_at'], '2020-10-22T01:01:00+00:00')
                fetcher.fetch = lambda *args, **kwargs: (_ for _ in ()).throw(OSError('Issuer unavailable'))
                with patch.object(monitor, 'utc_now', return_value='2020-10-23T01:00:00+00:00'):
                    failed = monitor.run(root, 'test', '2020-10-22', previous=result, fetcher=fetcher)
            source = failed['companies']['MSFT']['source_checks'][1]
            self.assertEqual(source['attempted_at'], '2020-10-23T01:00:00+00:00')
            self.assertEqual(source['last_successful_check_at'], first['checked_at'])
            self.assertEqual(source['last_retrieved_at'], '2020-10-22T01:01:00+00:00')
            self.assertNotIn('retrieved_at', source)
            self.assertEqual(source['error'], 'Issuer unavailable')
            self.assertEqual(failed['queue'][0]['id'], result['queue'][0]['id'])

    def test_valid_empty_feed_does_not_renew_successful_coverage_timestamp(self):
        previous = {'checked_at': '2020-10-20T00:00:00+00:00', 'source_checks': [
            {'source': 'https://issuer.example/feed', 'kind': 'rss', 'status': 'checked'}]}
        checks = [{'source': 'https://issuer.example/feed', 'kind': 'rss', 'status': 'partial',
                   'retrieved_at': '2020-10-22T00:00:00+00:00'}]
        monitor.dated_checks(checks, previous, '2020-10-22T00:00:00+00:00')
        self.assertEqual(checks[0]['last_successful_check_at'], previous['checked_at'])
        self.assertEqual(checks[0]['last_retrieved_at'], checks[0]['retrieved_at'])
        self.assertEqual(monitor.source_coverage(checks), 'partial')
        self.assertEqual(monitor.source_coverage([]), 'unconfigured')


class OperationalEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.now = datetime(2026, 10, 22, 12, tzinfo=timezone.utc)
        self.files = {'run-status.json': {'status': 'partial', 'completed_at': '2026-10-22T11:00:00+00:00',
                      'financials': [{'ticker': 'MSFT', 'status': 'error', 'previous_data_retained': True}],
                      'market': [{'ticker': 'MSFT', 'status': 'available'}]},
                      'latest.json': {'companies': {'MSFT': {'coverage_status': 'error'}}},
                      'desk.json': {'companies': [{'ticker': 'MSFT',
                          'history': {'source': {'retrieved_at': '2026-10-19T11:00:00+00:00'},
                                      'periods': [{'end': '2026-06-30'}]},
                          'quote': {'retrieved_at': '2026-10-22T11:00:00+00:00',
                                    'trade_at': '2026-10-21T20:00:00+00:00'}}]}}

    def test_fresh_checkpoint_and_quote_do_not_renew_retained_financials(self):
        original = copy.deepcopy(self.files)
        health = verifier.source_health(self.files, self.now)
        financial = health['financials']['companies'][0]
        market = health['market']['companies'][0]
        self.assertEqual(health['financials']['fresh_count'], 0)
        self.assertEqual(financial['status'], 'retained')
        self.assertEqual(financial['retrieval_age_hours'], 73)
        self.assertEqual(financial['latest_period_end'], '2026-06-30')
        self.assertEqual(health['market']['fresh_count'], 1)
        self.assertEqual(market['retrieval_age_hours'], 1)
        self.assertEqual(market['trade_age_hours'], 16)
        self.assertEqual(health['discovery'][0]['coverage_status'], 'error')
        self.assertEqual(self.files, original)

    def test_recent_timestamp_alone_cannot_hide_failed_financial_collection(self):
        source = self.files['desk.json']['companies'][0]['history']['source']
        source['retrieved_at'] = '2026-10-22T11:00:00+00:00'
        self.assertEqual(verifier.source_health(self.files, self.now)['financials']['fresh_count'], 0)
        self.files['run-status.json']['financials'][0]['status'] = 'collected'
        self.assertEqual(verifier.source_health(self.files, self.now)['financials']['fresh_count'], 1)
        for stamp in ('2026-10-23T11:00:00+00:00', '2026-10-22T11:00:00', 'bad'):
            source['retrieved_at'] = stamp
            self.assertEqual(verifier.source_health(self.files, self.now)['financials']['fresh_count'], 0)

    def test_manual_backup_does_not_claim_scheduled_delivery(self):
        self.assertFalse(verifier.execution_context({'GITHUB_EVENT_NAME': 'workflow_dispatch'})['scheduled_execution_observed'])
        self.assertFalse(verifier.execution_context({})['scheduled_execution_observed'])
        context = verifier.execution_context({'GITHUB_EVENT_NAME': 'schedule', 'GITHUB_RUN_ID': '123', 'GITHUB_RUN_ATTEMPT': '1'})
        self.assertTrue(context['scheduled_execution_observed'])
        self.assertEqual(context['run_id'], '123')

    def test_failed_verification_retains_durable_failure_evidence(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            summary = root / 'summary.md'
            report = {'verification_status': 'failed', 'execution': verifier.execution_context({}),
                      'error': 'backup differs | no restore proof'}
            with patch.dict('os.environ', {'GITHUB_STEP_SUMMARY': str(summary)}):
                verifier.write_report(root, report)
            self.assertEqual(json.loads((root / 'build/runtime-verification.json').read_text()), report)
            text = summary.read_text()
            self.assertIn('not_proven', text)
            self.assertIn('backup differs \\| no restore proof', text)


if __name__ == '__main__':
    unittest.main()
