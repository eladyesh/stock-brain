from copy import deepcopy
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import brain_markdown as brain
import brain_publication as publication
import stock_brain as kb
from coverage_store import CoverageStore
import market_directory as directory
from test_market_directory import fixtures, NOW


class MarkdownTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.store = CoverageStore(self.root / 'data.db', clock=lambda: NOW)
        self.store.seed_companies([{'cik': '0000789019', 'ticker': 'MSFT', 'company_name': 'Microsoft Corporation', 'exchange': 'NASDAQ'}])
        data = fixtures()
        data[0]['rows'][0].update(ticker='MSFT', security_name='Microsoft Corporation - Common Stock')
        directory.import_directories(self.store, data)
        self.history = json.loads((ROOT / 'research/financials/MSFT.json').read_text())
        self.store.put_payload('0000789019', 'history', self.history)
        self.release = {'release_tag': 'coverage-20261022-123-1', 'created_at': NOW.isoformat(),
                        'source_commit': 'a' * 40, 'database_sha256': 'b' * 64}
        self.output = self.root / 'export'

    def test_full_export_preserves_curated_files_and_publishes_exact_issuer_inventory(self):
        before = {d.path: d.path.read_bytes() for d in kb.documents(ROOT)}
        manifest = brain.export(self.store, self.output, self.release)
        self.assertEqual(manifest['company_profiles'], 1)
        self.assertEqual(manifest['financial_profiles'], 1)
        self.assertEqual(manifest['unresolved_listings'], 13)
        self.assertEqual(before, {p: p.read_bytes() for p in before})
        raw = (self.output / 'brain/companies/0000789019/README.md').read_text()
        meta, body = kb.split_document(raw)
        self.assertEqual(meta['status'], 'stub')
        self.assertFalse(meta['canonical_reviewed'])
        self.assertIsNone(meta['reviewed_at'])
        self.assertIn('/blob/' + 'a' * 40 + '/sectors/', meta['curated_research']['url'])
        kb.sections_from(body, kb.config(ROOT)[1])
        self.assertIn('US GAAP', body)
        self.assertIn('Cash outflow = negative of reported PaymentsToAcquirePropertyPlantAndEquipment; source value retained.', body)
        self.assertIn('Unavailable / blocked', body)
        self.assertNotIn('ETF1', (self.output / 'brain/INDEX.md').read_text())
        self.assertEqual(brain.verify(self.output), manifest)
        with self.assertRaisesRegex(ValueError, 'new directory'):
            brain.export(self.store, self.output, self.release)

    def test_changed_and_extra_files_prevent_republication(self):
        brain.export(self.store, self.output, self.release)
        path = self.output / 'brain/companies/0000789019/README.md'
        original = path.read_text()
        path.write_text(original + '\nManual research addition\n')
        with self.assertRaisesRegex(ValueError, 'preserve manual changes'):
            brain.verify(self.output)
        path.write_text(original)
        (self.output / 'brain/notes.md').write_text('Do not overwrite this note')
        with self.assertRaisesRegex(ValueError, 'preserve manual changes'):
            brain.verify(self.output)

    def test_fast_yaml_reader_rejects_ambiguous_metadata(self):
        with self.assertRaisesRegex(ValueError, 'duplicate YAML key'):
            brain.split_profile('---\nstatus: stub\nstatus: reviewed\n---\n# Ambiguous\n')

    def test_issuer_mismatch_and_invalid_financial_provenance_fail_closed(self):
        self.store.put_payload('0000789019', 'collector_state', {'cik': '0000000001'})
        with self.assertRaisesRegex(ValueError, 'issuer mismatch'):
            brain.export(self.store, self.output, self.release)
        self.store.put_payload('0000789019', 'collector_state', {'cik': '0000789019'})
        period = self.history['periods'][0]['id']
        self.history['financials'][period]['revenue']['value'] += 1
        self.store.put_payload('0000789019', 'history', self.history)
        with self.assertRaises(ValueError):
            brain.export(self.store, self.output, self.release)

    def test_missing_financials_are_not_zero_or_reviewed(self):
        with self.store._connection(write=True) as db:
            db.execute("DELETE FROM company_payloads WHERE kind='history'")
        manifest = brain.export(self.store, self.output, self.release)
        self.assertEqual(manifest['financial_profiles'], 0)
        raw = (self.output / 'brain/companies/0000789019/README.md').read_text()
        self.assertIn('not zero revenue', raw)
        self.assertNotIn('| revenue | 0', raw)
        self.assertEqual(manifest['financial_gap_counts']['not_collected'], 1)
        self.assertIn('Coverage gaps and next research tasks', (self.output / 'brain/GAPS.md').read_text())

    def test_gap_tasks_use_observed_forms_and_do_not_assume_all_foreign_forms_are_ifrs(self):
        def gap(forms, state=None):
            return brain.financial_gap(None, {'recent_filing_inventory': [{'form': f} for f in forms]}, state)
        self.assertEqual(gap(['20-F', '6-K'])['reason'], 'foreign_reporting_adapter')
        self.assertEqual(gap(['N-CSR', 'N-CSRS'])['reason'], 'fund_reporting_review')
        self.assertEqual(gap(['N-CSR', '10-K'])['reason'], 'unsupported_reporting_inventory')
        self.assertEqual(gap(['10-Q'], {'last_action': 'filings_only_financials_incomplete'})['reason'], 'latest_filing_incomplete')
        self.assertEqual(brain.financial_gap({'valid': True}, None, None)['reason'], 'available')
        self.assertNotIn('IFRS', gap(['20-F'])['next_action'])

    def test_frozen_reader_preserves_exact_snapshot_bytes_and_rejects_writes(self):
        import coverage_backup
        frozen = self.root / 'frozen.sqlite3'
        coverage_backup.backup(self.store.path, frozen)
        before = brain.file_digest(frozen)
        reader = brain.FrozenStore(frozen)
        brain.export(reader, self.output, self.release)
        self.assertEqual(brain.file_digest(frozen), before)
        self.assertFalse(Path(str(frozen) + '-wal').exists())
        with self.assertRaisesRegex(ValueError, 'read only'):
            reader.put_payload('0000789019', 'collector_state', {})
        Path(str(frozen) + '-wal').write_bytes(b'pending writer')
        with self.assertRaisesRegex(ValueError, 'without sidecars'):
            brain.FrozenStore(frozen)

    def test_real_git_publication_is_repeatable_and_preserves_manual_remote_changes(self):
        brain.export(self.store, self.output, self.release)
        remote = self.root / 'remote.git'
        subprocess.run(['git', 'init', '--bare', '-q', str(remote)], check=True)
        real_run = subprocess.run

        def local_remote(args, **kwargs):
            args = [str(remote) if x == 'https://github.com/' + brain.REPO + '.git' else x for x in args]
            return real_run(args, **kwargs)

        with patch.dict(os.environ, {'GH_TOKEN': 'synthetic-test-token'}), patch.object(brain.subprocess, 'run', side_effect=local_remote):
            first = brain.publish(self.output)
            second = brain.publish(self.output)
            self.assertEqual(first['commit'], second['commit'])
            clone = self.root / 'manual'
            real_run(['git', 'clone', '-q', '--branch', 'brain-data', str(remote), str(clone)], check=True)
            path = clone / 'brain/companies/0000789019/README.md'
            path.write_text(path.read_text() + '\nHand-edited research\n')
            real_run(['git', 'add', '.'], cwd=clone, check=True)
            real_run(['git', '-c', 'user.name=Test', '-c', 'user.email=test@example.test', 'commit', '-qm', 'Manual edit'], cwd=clone, check=True)
            real_run(['git', 'push', '-q'], cwd=clone, check=True)
            with self.assertRaisesRegex(ValueError, 'preserve manual changes'):
                brain.publish(self.output)
            self.assertIn('Hand-edited research', path.read_text())


class PublicationTests(unittest.TestCase):
    def setUp(self):
        self.ref = {'ref': 'refs/heads/brain-data', 'object': {'type': 'commit', 'sha': 'a' * 40}}
        self.manifest = {'format': brain.FORMAT, 'version': 1, 'release_tag': 'coverage-20261022-123-1',
                         'source_commit': 'b' * 40, 'created_at': '2026-10-22T00:00:00+00:00',
                         'company_ciks': ['0000789019'], 'company_profiles': 1,
                         'unresolved_listing_keys': ['c' * 32], 'unresolved_listings': 1,
                         'financial_profiles': 1, 'reviewed_generated_profiles': 0}
        self.reader = publication.BrainPublication()

    def refresh(self):
        with patch.object(publication, 'read_json', side_effect=[self.ref, self.manifest]):
            self.reader.refresh()

    def test_urls_pin_persisted_commit_and_reject_unknown_identities(self):
        self.refresh()
        result = self.reader.document(cik='0000789019', release_tag='coverage-20261022-123-1')
        self.assertTrue(result['available'])
        self.assertTrue(result['matches_current_data'])
        self.assertIn('/' + 'a' * 40 + '/brain/companies/0000789019/README.md', result['url'])
        self.assertFalse(self.reader.document(cik='9999999999')['available'])
        self.assertTrue(self.reader.document(listing_key='c' * 32)['available'])
        self.assertFalse(self.reader.document(cik='0000789019', release_tag='coverage-20261023-999-1')['matches_current_data'])
        self.assertNotIn('company_ciks', self.reader.summary())

    def test_failure_retains_last_known_published_files_and_no_provider_error(self):
        self.refresh()
        previous = self.reader.document(cik='0000789019')
        with patch.object(publication, 'read_json', side_effect=ValueError('private provider response')):
            self.reader.refresh()
        self.assertEqual(self.reader.status, 'degraded')
        self.assertEqual(self.reader.document(cik='0000789019'), previous)
        self.assertNotIn('private', json.dumps(self.reader.summary()))

    def test_invalid_counts_or_promoted_review_never_become_published_coverage(self):
        for field, value in [('company_profiles', 5000), ('reviewed_generated_profiles', 1),
                             ('source_commit', '../main'), ('company_ciks', ['0000789019', '0000789019'])]:
            changed = deepcopy(self.manifest)
            changed[field] = value
            with patch.object(publication, 'read_json', side_effect=[self.ref, changed]):
                self.reader.refresh()
            self.assertFalse(self.reader.summary()['available'])


if __name__ == '__main__':
    unittest.main()
