from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone
import hashlib
import json
import os
from pathlib import Path
import sqlite3
import sys
import tempfile
import threading
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from coverage_store import CoverageStore, LeaseLostError, MIGRATIONS, SCHEMA_VERSION, normalize_cik


URL = 'https://www.sec.gov/files/company_tickers_exchange.json'


def listings(rows):
    return {'fields': ['cik', 'name', 'ticker', 'exchange'], 'data': rows}


def evidence(payload, retrieved_at='2026-10-20T10:00:00+00:00', url=URL):
    raw = json.dumps(payload).encode()
    return {'url': url, 'sha256': hashlib.sha256(raw).hexdigest(), 'retrieved_at': retrieved_at}


class CoverageStoreTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.path = Path(self.temp.name) / 'coverage.sqlite3'
        self.now = datetime(2026, 10, 22, 12, tzinfo=timezone.utc)
        self.store = CoverageStore(self.path, clock=lambda: self.now)

    def tearDown(self):
        self.temp.cleanup()

    def seed(self, count=1):
        return self.store.seed_companies([{'cik': i, 'company_name': f'Company {i:04}', 'ticker': f'T{i}', 'exchange': 'NASDAQ'}
                                          for i in range(1, count + 1)])

    def sql(self, query, params=()):
        with sqlite3.connect(self.path) as db:
            return db.execute(query, params).fetchall()

    def test_migration_upgrades_v1_and_environment_selects_persistent_path(self):
        old_path = Path(self.temp.name) / 'old.db'
        with sqlite3.connect(old_path) as db:
            for statement in MIGRATIONS[1]:
                db.execute(statement)
            db.execute('PRAGMA user_version=1')
            db.execute('INSERT INTO schema_migrations VALUES (1,?)', (self.now.isoformat(),))
        with patch.dict(os.environ, {'STOCK_BRAIN_COVERAGE_DB': str(old_path)}):
            reopened = CoverageStore(clock=lambda: self.now)
        self.assertEqual(reopened.path, old_path)
        self.assertEqual(reopened.stats()['schema_version'], SCHEMA_VERSION)
        self.assertFalse(reopened.source_status()['blocked'])
        with sqlite3.connect(old_path) as db:
            self.assertEqual(db.execute('PRAGMA user_version').fetchone()[0], SCHEMA_VERSION)
            self.assertEqual(db.execute('SELECT version FROM schema_migrations ORDER BY version').fetchall(),
                             [(version,) for version in range(1, SCHEMA_VERSION + 1)])

    def test_cik_identity_share_classes_and_all_source_venues_are_retained(self):
        payload = listings([[1, 'Example Holdings', 'ex-a', 'NYSE'], [1, 'Example Holdings', 'EX.B', 'NYSE'],
                            [2, 'Other Corp', 'OTH', 'Nasdaq'], [3, 'OTC Corp', 'OTCC', 'OTC'],
                            [4, 'Unknown Venue', 'UNK', None]])
        summary = self.store.import_listings(payload, evidence(payload), complete=True)
        self.assertEqual((summary['issuers'], summary['rows']), (4, 5))
        company = self.store.company('EX.B')
        self.assertEqual(company['cik'], '0000000001')
        self.assertEqual(company['ticker'], 'EX.B')
        self.assertEqual({x['ticker'] for x in company['listings']}, {'EX-A', 'EX.B'})
        self.assertEqual(self.store.company('OTH')['exchange'], 'NASDAQ')
        self.assertEqual(self.store.company('OTCC')['exchange'], 'OTC')
        self.assertIsNone(self.store.company('UNK')['exchange'])
        self.assertEqual(self.store.list_companies()['total'], 4)
        self.assertEqual(normalize_cik('0000000001'), normalize_cik(1))
        snapshot = self.sql('SELECT source_url,source_sha256,payload_json,row_count FROM listing_snapshots')[0]
        self.assertEqual(snapshot[0:2], (URL, evidence(payload)['sha256']))
        self.assertEqual(json.loads(snapshot[2]), payload)
        self.assertEqual(snapshot[3], 5)

    def test_partial_snapshots_never_retire_and_complete_retirement_keeps_history(self):
        both = listings([[1, 'Alpha', 'AAA', 'NYSE'], [2, 'Beta', 'BBB', 'Nasdaq']])
        only_alpha = listings(both['data'][:1])
        self.store.import_listings(both, evidence(both))
        self.store.put_payload(2, 'history', {'reported': {'revenue': 123}})
        source = evidence(only_alpha, '2026-10-21T10:00:00+00:00')
        partial = self.store.import_listings(only_alpha, source)
        self.assertEqual(partial['inactivated_listings'], 0)
        self.assertEqual(self.store.company(2)['status'], 'listed')
        # The same bytes may later be explicitly certified complete; this is not a duplicate.
        complete = self.store.import_listings(only_alpha, source, complete=True)
        self.assertFalse(complete['duplicate'])
        self.assertEqual(complete['inactivated_listings'], 1)
        self.assertEqual(self.store.company(2)['listings'][0]['status'], 'inactive')
        self.assertEqual(self.store.get_payload(2, 'history'), {'reported': {'revenue': 123}})
        self.assertEqual(self.store.stats()['issuers'], 2)
        self.assertEqual(self.sql("SELECT COUNT(*) FROM listing_events WHERE event='absent_from_complete_snapshot'")[0][0], 1)
        duplicate = self.store.import_listings(only_alpha, source, complete=True)
        self.assertTrue(duplicate['duplicate'])
        self.assertEqual(self.store.stats()['listing_snapshots'], 3)

    def test_stale_complete_snapshot_is_audited_without_rewinding_listings(self):
        current = listings([[1, 'Alpha', 'AAA', 'NYSE'], [2, 'Beta', 'BBB', 'Nasdaq']])
        self.store.import_listings(current, evidence(current, '2026-10-21T10:00:00+00:00'), complete=True)
        old = listings(current['data'][:1])
        result = self.store.import_listings(old, evidence(old), complete=True)
        self.assertFalse(result['applied'])
        self.assertEqual(self.store.stats()['active_listings'], 2)
        self.assertEqual(self.store.stats()['listing_snapshots'], 2)
        self.assertEqual(self.store.company(2)['company_name'], 'Beta')

    def test_complete_snapshot_cannot_remove_a_different_source_or_seed_scope(self):
        self.seed()
        imported = listings([[2, 'Imported', 'IMP', 'NYSE']])
        self.store.import_listings(imported, evidence(imported), complete=True)
        another = listings([[3, 'Another', 'ANO', 'Nasdaq']])
        self.store.import_listings(another, evidence(another, url='https://issuer.example/registry'), complete=True)
        self.assertEqual(self.store.stats()['active_listings'], 3)
        self.assertEqual(self.store.company(1)['listings'][0]['source_kind'], 'repository_seed')

    def test_bad_or_empty_complete_inputs_are_atomic_and_no_coverage_is_invented(self):
        self.seed()
        before = self.store.stats()
        invalid = [listings([[True, 'Bad', 'BAD', 'NYSE']]),
                   listings([[1, 'Bad', 'BAD', 'NYSE'], [2, 'Other', 'bad', 'NYSE']]),
                   listings([[1, 'Bad', 'BAD', 'NYSE'], [1, 'Conflicting name', 'BAD.A', 'NYSE']]),
                   {'fields': ['cik', 'name', 'ticker'], 'data': [[1, 'Bad', 'BAD']]},
                   listings([[1, 'Bad', 'BAD\n', 'NYSE']]), listings([])]
        for payload in invalid:
            with self.subTest(payload=payload), self.assertRaises(ValueError):
                self.store.import_listings(payload, evidence(payload), complete=True)
        valid = listings([[1, 'Company 0001', 'T1', 'Nasdaq']])
        for source in ({**evidence(valid), 'url': 'http://example.com/feed'},
                       {**evidence(valid), 'sha256': 'bad'},
                       {**evidence(valid), 'retrieved_at': '2026-10-20'},
                       {**evidence(valid), 'retrieved_at': '2026-10-23T00:00:00+00:00'}):
            with self.subTest(source=source), self.assertRaises(ValueError):
                self.store.import_listings(valid, source)
        self.assertEqual(self.store.stats(), before)
        self.assertIsNone(before['last_listing_import'])

    def test_offline_seed_is_idempotent_and_does_not_reactivate_delisted_share_class(self):
        companies = [{'cik': 1, 'company_name': 'Alpha', 'ticker': 'AAA', 'exchange': 'NYSE'}]
        first = self.store.seed_companies(companies)
        self.assertEqual(first['source_kind'], 'repository_seed')
        self.assertTrue(self.store.seed_companies(companies)['duplicate'])
        self.assertEqual(self.store.stats()['payloads'], 0)
        both = listings([[1, 'Alpha', 'AAA', 'NYSE'], [2, 'Beta', 'BBB', 'NYSE']])
        self.store.import_listings(both, evidence(both))
        subset = listings(both['data'][1:])
        self.store.import_listings(subset, evidence(subset, '2026-10-21T10:00:00+00:00'), complete=True)
        self.store.seed_companies([{**companies[0], 'sector': 'new local metadata'}])
        self.assertEqual(self.store.company(1)['status'], 'inactive')

    def test_search_paging_and_ambiguous_ticker_resolution(self):
        self.seed(5)
        self.store.seed_companies([{'cik': 6, 'company_name': '100% Widgets', 'ticker': 'PCNT', 'exchange': 'NYSE'},
                                   {'cik': 7, 'company_name': 'Under_score', 'ticker': 'UNDER', 'exchange': 'NYSE'}])
        pages = [self.store.list_companies(limit=2, offset=i) for i in range(0, 7, 2)]
        ids = [c['cik'] for page in pages for c in page['items']]
        self.assertEqual(len(set(ids)), 7)
        self.assertTrue(all(page['total'] == 7 for page in pages))
        self.assertEqual(self.store.list_companies(query='%')['total'], 1)
        self.assertEqual(self.store.list_companies(query='_')['total'], 1)
        self.assertEqual(self.store.list_companies(query="' OR 1=1 --")['total'], 0)
        self.assertEqual(self.store.list_companies(query='t3')['items'][0]['cik'], '0000000003')
        self.assertEqual(self.store.list_companies(offset=500)['items'], [])
        self.assertIsNone(self.store.company('MISSING'))
        other_venue = listings([[8, 'Another Issuer', 'T3', 'NYSE']])
        self.store.import_listings(other_venue, evidence(other_venue))
        with self.assertRaisesRegex(ValueError, 'ambiguous'):
            self.store.company('T3')
        self.assertEqual(self.store.company(3)['cik'], '0000000003')

    def test_payload_versions_keep_exact_source_evidence_and_return_raw_values(self):
        self.seed()
        first = {'reported': {'revenue': 100}, 'reviewed': False}
        source = evidence(first, url='https://issuer.example/report')
        sha = self.store.put_payload(1, 'history', first, source)
        self.assertEqual(len(sha), 64)
        self.assertEqual(self.store.get_payload(1, 'history'), first)
        self.assertEqual(self.store.put_payload(1, 'history', first, source), sha)
        self.assertEqual(self.store.stats()['payloads'], 1)
        updated_source = {**source, 'retrieved_at': '2026-10-21T10:00:00+00:00'}
        self.store.put_payload(1, 'history', first, updated_source)
        second = {'reported': {'revenue': 110}, 'reviewed': False}
        self.store.put_payload(1, 'history', second, updated_source)
        self.assertEqual(self.store.stats()['payloads'], 3)
        metadata = self.store.company(1)['payloads']['history']
        self.assertEqual(metadata['version'], 3)
        self.assertEqual(metadata['source']['sha256'], source['sha256'])
        self.assertEqual(self.store.get_payload(1, 'history'), second)
        self.assertEqual(json.loads(self.sql('SELECT value_json FROM company_payloads WHERE version=1')[0][0]), first)
        with self.assertRaises(ValueError):
            self.store.put_payload(99, 'history', first)
        with self.assertRaises(ValueError):
            self.store.put_payload(1, 'history', {'value': float('nan')})

    def test_duplicate_enqueue_and_concurrent_claims_are_atomic(self):
        self.seed(2)
        first = self.store.enqueue(1)
        self.assertEqual(first['id'], self.store.enqueue('0000000001')['id'])
        self.store.enqueue(2)
        second_store = CoverageStore(self.path, clock=lambda: self.now)
        barrier = threading.Barrier(2)
        def claim(store, worker):
            barrier.wait(timeout=5)
            return store.claim(worker)
        with ThreadPoolExecutor(max_workers=2) as pool:
            a = pool.submit(claim, self.store, 'worker-a')
            b = pool.submit(claim, second_store, 'worker-b')
            jobs = [a.result(timeout=10), b.result(timeout=10)]
        self.assertEqual({j['cik'] for j in jobs}, {'0000000001', '0000000002'})
        self.assertEqual(len({j['lease_token'] for j in jobs}), 2)
        self.assertIsNone(self.store.claim('worker-c'))
        self.assertEqual(self.store.enqueue(1)['id'], first['id'])

    def test_payload_cas_inserts_only_if_absent_and_preserves_concurrent_publication(self):
        self.seed()
        self.assertIsNone(self.store.get_payload_record(1, 'history'))
        first_sha = self.store.put_payload_if_current(1, 'history', {'version': 'seed'}, None)
        self.assertEqual(len(first_sha), 64)
        read = self.store.get_payload_record(1, 'history')
        self.assertEqual(read['value'], {'version': 'seed'})
        self.assertEqual(read['metadata']['sha256'], first_sha)
        self.assertEqual(read['metadata']['version'], 1)
        writer = CoverageStore(self.path, clock=lambda: self.now)
        writer.put_payload(1, 'history', {'version': 'newer collection'})
        self.assertIsNone(self.store.put_payload_if_current(1, 'history', {'version': 'stale startup merge'},
                          read['metadata']['sha256'], expected_version=read['metadata']['version']))
        self.assertIsNone(self.store.put_payload_if_current(1, 'history', {'version': 'another seed'}, None))
        self.assertEqual(self.store.get_payload(1, 'history'), {'version': 'newer collection'})
        self.assertEqual(self.store.stats()['payloads'], 2)

    def test_payload_cas_version_detects_new_evidence_with_unchanged_content_hash(self):
        self.seed()
        value = {'reported': 'unchanged'}
        source = evidence(value, url='https://issuer.example/report')
        self.store.put_payload(1, 'history', value, source)
        first = self.store.get_payload_record(1, 'history')
        newer_source = {**source, 'retrieved_at': '2026-10-21T10:00:00+00:00'}
        self.store.put_payload(1, 'history', value, newer_source)
        current = self.store.get_payload_record(1, 'history')
        self.assertEqual(first['metadata']['sha256'], current['metadata']['sha256'])
        self.assertEqual(current['metadata']['version'], 2)
        self.assertIsNone(self.store.put_payload_if_current(1, 'history', value, first['metadata']['sha256'],
                          source, expected_version=first['metadata']['version']))
        self.assertEqual(self.store.get_payload_record(1, 'history'), current)
        merged = {'reported': 'unchanged', 'review': 'new review bound to current data'}
        sha = self.store.put_payload_if_current(1, 'history', merged, current['metadata']['sha256'],
                                              newer_source, expected_version=current['metadata']['version'])
        self.assertEqual(self.store.get_payload_record(1, 'history')['metadata']['sha256'], sha)
        self.assertEqual(self.store.get_payload_record(1, 'history')['metadata']['version'], 3)

    def test_payload_cas_has_only_one_concurrent_winner(self):
        self.seed()
        original = self.store.put_payload(1, 'history', {'original': True})
        other = CoverageStore(self.path, clock=lambda: self.now)
        barrier = threading.Barrier(2)
        def publish(store, label):
            barrier.wait(timeout=5)
            return store.put_payload_if_current(1, 'history', {'winner': label}, original, expected_version=1)
        with ThreadPoolExecutor(max_workers=2) as pool:
            a = pool.submit(publish, self.store, 'one')
            b = pool.submit(publish, other, 'two')
            results = [a.result(timeout=10), b.result(timeout=10)]
        self.assertEqual(sum(result is not None for result in results), 1)
        self.assertEqual(self.store.stats()['payloads'], 2)
        self.assertEqual(self.store.get_payload_record(1, 'history')['metadata']['sha256'], next(r for r in results if r))

    def test_only_winning_unexpired_lease_can_publish_or_complete(self):
        self.seed()
        self.store.put_payload(1, 'history', {'old': True})
        self.store.enqueue(1)
        old = self.store.claim('same-worker', lease_seconds=5)
        self.now += timedelta(seconds=6)
        winner = self.store.claim('same-worker', lease_seconds=60)
        self.assertEqual(winner['attempts'], 2)
        self.assertNotEqual(winner['lease_token'], old['lease_token'])
        with self.assertRaises(LeaseLostError):
            self.store.commit_job(old['id'], 'same-worker', old['lease_token'], {'history': {'value': {'loser': True}}})
        with self.assertRaises(LeaseLostError):
            self.store.fail(old['id'], 'same-worker', old['lease_token'], 'old worker failure')
        self.assertEqual(self.store.get_payload(1, 'history'), {'old': True})
        completed = self.store.commit_job(winner['id'], 'same-worker', winner['lease_token'],
            {'history': {'value': {'new': True}}, 'collector_state': {'value': {'status': 'collected'}}}, {'status': 'collected'})
        self.assertEqual(completed['status'], 'completed')
        self.assertEqual(self.store.get_payload(1, 'history'), {'new': True})
        self.assertEqual(self.store.get_payload(1, 'collector_state'), {'status': 'collected'})
        with self.assertRaises(LeaseLostError):
            self.store.finish(winner['id'], 'same-worker', winner['lease_token'])

    def test_expired_lease_and_invalid_payload_batch_leave_existing_data_untouched(self):
        self.seed()
        self.store.enqueue(1)
        job = self.store.claim('worker', lease_seconds=5)
        with self.assertRaises(ValueError):
            self.store.commit_job(job['id'], 'worker', job['lease_token'],
                                 {'history': {'value': {'valid': True}}, 'submissions': {'value': {'bad': float('nan')}}})
        self.assertEqual(self.store.stats()['payloads'], 0)
        self.now += timedelta(seconds=5)
        with self.assertRaises(LeaseLostError):
            self.store.finish(job['id'], 'worker', job['lease_token'])
        self.assertEqual(self.store.stats()['jobs']['running'], 1)

    def test_exponential_retry_is_capped_and_terminal_failure_stops_claims(self):
        self.seed()
        self.store.enqueue(1)
        job = self.store.claim('worker')
        retry = self.store.fail(job['id'], 'worker', job['lease_token'], 'Temporary error', retry_after_seconds=50_000, max_attempts=3)
        self.assertEqual(datetime.fromisoformat(retry['available_at']) - self.now, timedelta(seconds=50_000))
        self.assertIsNone(self.store.claim('too-early'))
        self.now = datetime.fromisoformat(retry['available_at'])
        job = self.store.claim('worker')
        retry = self.store.fail(job['id'], 'worker', job['lease_token'], 'Still unavailable', retry_after_seconds=50_000, max_attempts=3)
        self.assertEqual(datetime.fromisoformat(retry['available_at']) - self.now, timedelta(days=1))
        self.now = datetime.fromisoformat(retry['available_at'])
        job = self.store.claim('worker')
        failed = self.store.fail(job['id'], 'worker', job['lease_token'], 'Unavailable', max_attempts=3)
        self.assertEqual(failed['status'], 'failed')
        self.assertIsNone(self.store.claim('worker'))
        self.assertGreater(self.store.enqueue(1)['id'], failed['id'])

    def test_blocked_jobs_are_visible_and_never_automatically_retried(self):
        self.seed()
        self.store.enqueue(1)
        job = self.store.claim('worker')
        self.store.fail(job['id'], 'worker', job['lease_token'], 'SEC operator pause', blocked=True)
        self.now += timedelta(days=2)
        self.assertIsNone(self.store.claim('another-worker'))
        self.assertEqual(self.store.eligible_for_job(), [])
        self.assertEqual(self.store.stats()['jobs']['blocked'], 1)
        self.assertIn('SEC operator pause', self.store.stats()['source_blocked'][0]['error'])
        self.assertEqual(self.store.enqueue(1)['status'], 'queued')

    def test_bounded_batches_progress_past_unchanged_or_unsupported_issuers(self):
        self.seed(3)
        self.assertEqual(self.store.eligible_for_job(limit=1)[0]['cik'], '0000000001')
        self.store.enqueue(1)
        job = self.store.claim('worker')
        self.store.commit_job(job['id'], 'worker', job['lease_token'],
                              {'collector_state': {'value': {'status': 'no_supported_filing'}}})
        self.assertEqual(self.store.eligible_for_job(limit=1)[0]['cik'], '0000000002')
        self.assertNotIn('0000000001', [r['cik'] for r in self.store.eligible_for_job()])
        self.now += timedelta(days=1)
        candidates = self.store.eligible_for_job()
        self.assertEqual([r['cik'] for r in candidates], ['0000000002', '0000000003', '0000000001'])

    def test_source_rate_reservations_are_global_and_pause_survives_restart(self):
        other = CoverageStore(self.path, clock=lambda: self.now)
        self.assertEqual(self.store.reserve_source(), 0)
        self.assertEqual(other.reserve_source(), 0.25)
        self.assertEqual(self.store.reserve_source(), 0.5)
        with self.assertRaises(ValueError):
            other.reserve_source(interval_seconds=0.01)
        blocked = self.store.pause_source('sec', seconds=86_400, error='403 access rejected')
        self.assertTrue(blocked['blocked'])
        reopened = CoverageStore(self.path, clock=lambda: self.now)
        self.assertTrue(reopened.source_status()['blocked'])
        self.assertEqual(reopened.reserve_source(), 86_400)
        next_request = reopened.source_status()['next_request_at']
        reopened.pause_source('sec', seconds=60, reason='Shorter pause cannot weaken existing cooldown')
        self.assertEqual(reopened.source_status()['blocked_until'], blocked['blocked_until'])
        self.assertEqual(reopened.source_status()['next_request_at'], next_request)
        self.assertEqual(self.store.stats()['sources']['sec']['reason'], '403 access rejected')
        self.now += timedelta(days=1, seconds=1)
        self.assertFalse(reopened.source_status()['blocked'])
        self.assertEqual(reopened.reserve_source(), 0)


if __name__ == '__main__':
    unittest.main()
