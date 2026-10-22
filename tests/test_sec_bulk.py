"""Synthetic archives test identity, bounded recovery and zero-network ingestion."""
from datetime import timedelta
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
import zipfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from coverage_store import CoverageStore
import market_directory as directory
import sec_bulk as bulk
from test_market_directory import fixtures, NOW
from test_coverage_worker import financial_facts, submissions


def issuer(cik=123, ticker='T0', name='Company 0'):
    value = submissions(cik=str(cik).zfill(10))
    value.update(name=name, tickers=[ticker], exchanges=['Nasdaq'])
    return value


class BulkTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.store = CoverageStore(self.root / 'data.db', clock=lambda: NOW)
        directory.import_directories(self.store, fixtures())

    def archive(self, kind, values, *, stamp=NOW, filename=None):
        path = self.root / (filename or kind + '.zip')
        with zipfile.ZipFile(path, 'w', compression=zipfile.ZIP_DEFLATED) as output:
            for key, value in values.items():
                output.writestr(key, json.dumps(value))
        archive = bulk.SECArchive(path, kind, retrieved_at=stamp, sha256=bulk.digest_file(path), now=NOW)
        self.addCleanup(archive.archive.close)
        return archive

    def sources(self):
        return (self.archive('submissions', {'CIK0000000123.json': issuer()}),
                self.archive('companyfacts', {'CIK0000000123.json': financial_facts(cik=123)}))

    def test_resumable_registry_matches_explicit_identity_without_importing_private_filings(self):
        source = self.archive('submissions', {'CIK0000000123.json': issuer(),
            'CIK0000000124.json': issuer(124, 'T1', 'Company 1'),
            'CIK0000000125.json': issuer(125, 'PRIVATE', 'Private Company')})
        first = bulk.import_issuers(self.store, source, limit=1)
        self.assertFalse(first['complete'])
        self.assertEqual(first['cursor'], '0000000123')
        second = bulk.import_issuers(self.store, source, limit=2)
        self.assertTrue(second['complete'])
        self.assertEqual((second['scanned'], second['imported'], second['skipped']), (3, 2, 1))
        third = bulk.import_issuers(self.store, source, limit=2)
        self.assertEqual(third, second)
        self.assertIsNone(self.store.company('125'))
        security = directory.list_securities(self.store, query='T1')['items'][0]
        self.assertEqual(security['cik'], '0000000124')
        self.assertEqual(security['research_status'], 'not_reviewed')

    def test_array_position_does_not_establish_a_ticker_venue_mapping(self):
        data = issuer()
        data.update(tickers=['T0', 'ADR'], exchanges=['NYSE'])
        source = self.archive('submissions', {'CIK0000000123.json': data})
        bulk.import_issuers(self.store, source)
        self.assertIsNone(self.store.company('123'))

    def test_bad_issuer_is_quarantined_and_other_issuers_continue(self):
        source = self.archive('submissions', {'CIK0000000123.json': issuer(999),
            'CIK0000000124.json': issuer(124, 'T1', 'Company 1')})
        report = bulk.import_issuers(self.store, source)
        self.assertEqual((report['failed'], report['imported']), (1, 1))
        with self.store._connection() as db:
            self.assertEqual(db.execute('SELECT cik FROM sec_bulk_errors').fetchone()[0], '0000000123')
        self.assertIsNone(self.store.company('999'))

    def test_financial_collection_reuses_quality_gates_without_network_or_canonical_review(self):
        sub, facts = self.sources()
        bulk.import_issuers(self.store, sub)
        # A separate collector's job is never accidentally claimed by this run.
        queued = self.store.enqueue('123')
        with patch('urllib.request.urlopen', side_effect=AssertionError('network forbidden')):
            report = bulk.collect_financials(self.store, sub, facts, root=self.root)
        self.assertEqual((report['imported'], report['failed'], report['network_requests']), (1, 0, 0))
        history = self.store.get_payload('123', 'history')
        self.assertEqual(history['source']['archive']['sha256'], facts.sha256)
        self.assertIsNone(history['source']['raw_cache'])
        self.assertEqual(history['as_of'], NOW.date().isoformat())
        self.assertFalse(self.store.get_payload('123', 'automatic_changes')['canonical_reviewed'])
        security = directory.list_securities(self.store, query='T0')['items'][0]
        self.assertEqual(security['datasets']['profile']['scope'], 'issuer_identity_only')
        self.assertEqual(security['datasets']['filings']['scope'], 'recent_metadata_only')
        with self.store._connection() as db:
            self.assertEqual(db.execute('SELECT status FROM jobs WHERE id=?', (queued['job_id'],)).fetchone()[0], 'queued')
        version = self.store.get_payload_record('123', 'history')['metadata']['version']
        self.assertTrue(bulk.collect_financials(self.store, sub, facts, root=self.root)['complete'])
        self.assertEqual(self.store.get_payload_record('123', 'history')['metadata']['version'], version)

    def test_incomplete_registry_scan_blocks_financial_cursor_skips(self):
        sub, facts = self.sources()
        with self.assertRaisesRegex(ValueError, 'finish this archive issuer scan'):
            bulk.collect_financials(self.store, sub, facts, root=self.root)

    def test_complete_mode_drains_all_batches_with_one_archive_open(self):
        sub = self.archive('submissions', {f'CIK{123+i:010d}.json': issuer(123+i, f'T{i}', f'Company {i}') for i in range(3)})
        facts = self.archive('companyfacts', {f'CIK{123+i:010d}.json': financial_facts(cik=123+i) for i in range(3)})
        path = self.root / 'all.json'
        path.write_text(json.dumps({'format': 'stock-brain-sec-bulk-v1', **{a.kind: {
            'file': a.path.name, 'url': bulk.URLS[a.kind], 'retrieved_at': a.retrieved_at, 'sha256': a.sha256}
            for a in (sub, facts)}}))
        events = []
        with patch.object(bulk, 'open_manifest', wraps=bulk.open_manifest) as opened:
            report = bulk.ingest_manifest(self.store, path, root=self.root, issuer_limit=1,
                                         financial_limit=1, complete=True, on_progress=events.append)
        self.assertEqual(report['status'], 'completed')
        self.assertEqual(report['financials']['imported'], 3)
        self.assertEqual(len(events), 6)
        self.assertEqual(opened.call_count, 1)

    def test_unchanged_daily_bytes_retain_history_and_record_new_check(self):
        old_time = NOW - timedelta(hours=2)
        sub = self.archive('submissions', {'CIK0000000123.json': issuer()}, stamp=old_time)
        facts = self.archive('companyfacts', {'CIK0000000123.json': financial_facts(cik=123)}, stamp=old_time)
        bulk.import_issuers(self.store, sub)
        bulk.collect_financials(self.store, sub, facts, root=self.root)
        before = self.store.get_payload_record('123', 'history')
        before_sub = self.store.get_payload_record('123', 'submissions')
        new_sub = self.archive('submissions', {'CIK0000000123.json': issuer()}, filename='new-sub.zip')
        new_facts = self.archive('companyfacts', {'CIK0000000123.json': financial_facts(cik=123)}, filename='new-facts.zip')
        bulk.import_issuers(self.store, new_sub)
        self.assertEqual(bulk.collect_financials(self.store, new_sub, new_facts, root=self.root)['failed'], 0)
        self.assertEqual(self.store.get_payload_record('123', 'history'), before)
        self.assertEqual(self.store.get_payload_record('123', 'submissions'), before_sub)
        self.assertEqual(self.store.get_payload('123', 'collector_state')['facts_checked_at'], new_facts.retrieved_at)

    def test_new_archive_checks_same_accession_corrections_and_keeps_previous_version(self):
        sub, facts = self.sources()
        bulk.import_issuers(self.store, sub)
        bulk.collect_financials(self.store, sub, facts, root=self.root)
        corrected = financial_facts(cik=123)
        concept = next(iter(corrected['facts']['us-gaap'].values()))
        concept['units']['USD'][0]['val'] = 1100
        revised = self.archive('companyfacts', {'CIK0000000123.json': corrected}, filename='corrected.zip')
        report = bulk.collect_financials(self.store, sub, revised, root=self.root)
        self.assertEqual(report['failed'], 0)
        record = self.store.get_payload_record('123', 'history')
        self.assertEqual(record['metadata']['version'], 2)
        values = [cells['revenue']['value'] for cells in record['value']['financials'].values()]
        self.assertIn(1100, values)

    def test_older_archive_does_not_overwrite_newer_source(self):
        sub, facts = self.sources()
        bulk.import_issuers(self.store, sub)
        bulk.collect_financials(self.store, sub, facts, root=self.root)
        before = self.store.get_payload_record('123', 'history')
        old = self.archive('companyfacts', {'CIK0000000123.json': financial_facts(cik=123)},
                           stamp=NOW - timedelta(hours=1), filename='older.zip')
        result = bulk.collect_financials(self.store, sub, old, root=self.root)
        self.assertEqual(result['failed'], 1)
        self.assertEqual(self.store.get_payload_record('123', 'history'), before)

    def test_foreign_forms_do_not_become_invented_us_gaap_financials(self):
        data = issuer()
        data['filings']['recent']['form'] = ['20-F']
        sub = self.archive('submissions', {'CIK0000000123.json': data})
        facts = self.archive('companyfacts', {'CIK0000000123.json': {'cik': 123, 'facts': {}}})
        bulk.import_issuers(self.store, sub)
        report = bulk.collect_financials(self.store, sub, facts, root=self.root)
        self.assertEqual(report['failed'], 0)
        self.assertIsNone(self.store.get_payload('123', 'history'))
        self.assertEqual(self.store.get_payload('123', 'automatic_changes')['classification'], 'quality_review_required')
        self.assertEqual(self.store.get_payload('123', 'submissions')['recent_filing_inventory'][0]['form'], '20-F')

    def test_missing_facts_does_not_publish_partial_financial_refresh(self):
        sub = self.archive('submissions', {'CIK0000000123.json': issuer()})
        facts = self.archive('companyfacts', {'CIK0000000999.json': {'cik': 999, 'facts': {}}})
        bulk.import_issuers(self.store, sub)
        result = bulk.collect_financials(self.store, sub, facts, root=self.root)
        self.assertEqual(result['failed'], 1)
        self.assertIsNone(self.store.get_payload('123', 'history'))
        self.assertIsNone(self.store.get_payload('123', 'collector_state'))

    def test_paths_duplicates_hashes_size_and_identity_are_validated(self):
        sub, _ = self.sources()
        with self.assertRaisesRegex(ValueError, 'SHA-256 mismatch'):
            bulk.SECArchive(sub.path, 'submissions', retrieved_at=NOW, sha256='0' * 64, now=NOW)
        for bad in ('../CIK0000000123.json', 'CIK0000000000.json', '/CIK0000000123.json'):
            with self.subTest(member=bad), self.assertRaises(ValueError):
                self.archive('companyfacts', {bad: {'cik': 123}}, filename='bad.zip')
        with patch.object(bulk, 'MAX_MEMBER', 2), self.assertRaises(ValueError):
            bulk.SECArchive(sub.path, 'submissions', retrieved_at=NOW, sha256=sub.sha256, now=NOW)
        path = self.root / 'duplicates.zip'
        with zipfile.ZipFile(path, 'w') as output:
            with self.assertWarns(UserWarning):
                output.writestr('CIK0000000123.json', '{}')
                output.writestr('CIK0000000123.json', '{}')
        with self.assertRaisesRegex(ValueError, 'duplicate SEC ZIP member'):
            bulk.SECArchive(path, 'submissions', retrieved_at=NOW, sha256=bulk.digest_file(path), now=NOW)

    def test_stale_directory_blocks_bulk_association(self):
        sub, _ = self.sources()
        self.store.clock = lambda: NOW + timedelta(days=2)
        with self.assertRaisesRegex(ValueError, 'fresh listing directory'):
            bulk.import_issuers(self.store, sub)

    def test_acquisition_manifest_cycle_and_public_snapshot_recovery_keep_progress(self):
        sub, facts = self.sources()
        path = self.root / 'acquisition.json'
        path.write_text(json.dumps({'format': 'stock-brain-sec-bulk-v1', **{
            source.kind: {'file': source.path.name, 'url': bulk.URLS[source.kind],
                          'retrieved_at': source.retrieved_at, 'sha256': source.sha256}
            for source in (sub, facts)}}))
        result = bulk.ingest_manifest(self.store, path, root=self.root)
        self.assertEqual(result['status'], 'completed')
        self.assertEqual(result['financials']['imported'], 1)
        import coverage_release as release
        package = self.root / 'release'
        release.package(self.store, package, release_tag='coverage-20261022-123-1',
                        execution={'sec_bulk_collection': result})
        restored = self.root / 'restored.db'
        release.unpack(package / release.ASSET, package / release.MANIFEST, restored)
        recovered = CoverageStore(restored, clock=lambda: NOW)
        again = bulk.ingest_manifest(recovered, path, root=self.root)
        self.assertEqual(again, result)
        self.assertEqual(recovered.get_payload_record('123', 'history')['metadata']['version'], 1)


if __name__ == '__main__':
    unittest.main()
