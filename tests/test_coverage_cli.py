import contextlib
import hashlib
import io
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import coverage_cli as cli
from coverage_store import CoverageStore


def listings(count=3):
    return {'fields': ['cik', 'name', 'ticker', 'exchange'],
            'data': [[100000 + i, f'Fixture Issuer {i}', f'T{i:05d}', 'Nasdaq'] for i in range(count)]}


class CoverageCliTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.directory = Path(self.temporary.name)
        self.db = self.directory / 'coverage.sqlite3'

    def run_cli(self, *args):
        output, errors = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(output), contextlib.redirect_stderr(errors):
            result = cli.main(['--db', str(self.db), *map(str, args)])
        return result, json.loads(output.getvalue()) if output.getvalue().strip() else None, errors.getvalue()

    def import_file(self, payload, *flags, timestamp='2025-01-01T00:00:00Z'):
        path = self.directory / 'listings.json'
        raw = json.dumps(payload, ensure_ascii=False).encode() + b'\n'
        path.write_bytes(raw)
        result = self.run_cli('import-listings', '--file', path, '--source-url', cli.SEC_LISTINGS_URL,
                              '--retrieved-at', timestamp, *flags)
        return (*result, raw)

    def test_large_import_is_idempotent_and_hashes_actual_bytes(self):
        payload = listings(2500)
        with mock.patch.object(cli.p, 'Fetcher') as fetcher:
            code, report, errors, raw = self.import_file(payload)
            self.assertEqual((code, errors), (0, ''))
            self.assertEqual(report['source']['sha256'], hashlib.sha256(raw).hexdigest())
            self.assertEqual(report['input']['included_rows'], 2500)
            self.assertFalse(report['complete_snapshot'])
            self.assertEqual(self.import_file(payload)[0], 0)
            fetcher.assert_not_called()
        stats = CoverageStore(self.db).stats()
        self.assertEqual(stats['issuers'], 2500)
        self.assertEqual(stats['active_listings'], 2500)
        self.assertEqual(stats['payloads'], 0)

    def test_empty_malformed_and_invalid_rows_do_not_retire_existing_listings(self):
        self.assertEqual(self.import_file(listings())[0], 0)
        for payload in [ {'fields': ['cik', 'name', 'ticker', 'exchange'], 'data': []},
                         {'fields': ['cik', 'name', 'ticker'], 'data': [[1, 'Name', 'T']]},
                         {'fields': ['cik', 'name', 'ticker', 'exchange'], 'data': [[True, 'Name', 'T', 'NYSE']]},
                         {'fields': ['cik', 'name', 'ticker', 'exchange'], 'data': [[1, 'Name', 'T', 'NYSE'], [2, 'Broken']]},
                         {'fields': ['cik', 'name', 'ticker', 'exchange'], 'data': [[1, 'Name', 'T', 'NYSE'], [2, 'Other', 'T', 'NYSE']]},
                         {'fields': ['cik', 'name', 'ticker', 'exchange'], 'data': [[1, 'Name\nInjected', 'T', 'NYSE']]} ]:
            code, _, error, _ = self.import_file(payload, '--complete-snapshot')
            self.assertEqual(code, 2)
            self.assertTrue(error)
            self.assertEqual(CoverageStore(self.db).stats()['active_listings'], 3)
        with self.assertRaises(ValueError):
            cli.parse_listings(b'<html>Access denied</html>')
        with self.assertRaises(ValueError):
            cli.parse_listings(b'{"fields":[],"fields":[],"data":[]}')

    def test_retirement_requires_explicit_complete_snapshot(self):
        self.assertEqual(self.import_file(listings(3))[0], 0)
        self.assertEqual(self.import_file(listings(1), timestamp='2025-01-02T00:00:00Z')[0], 0)
        self.assertEqual(CoverageStore(self.db).stats()['active_listings'], 3)
        self.assertEqual(self.import_file(listings(1), '--complete-snapshot', timestamp='2025-01-03T00:00:00Z')[0], 0)
        stats = CoverageStore(self.db).stats()
        self.assertEqual(stats['active_listings'], 1)
        self.assertEqual(stats['inactive_listings'], 2)

    def test_exchange_exclusions_are_explicit_and_cannot_retire_a_filtered_snapshot(self):
        payload = {'fields': ['ticker', 'exchange', 'cik', 'name'],
                   'data': [['BRK-B', 'NYSE', 1067983, 'Berkshire fixture'], ['UNKN', None, 2, 'Unknown fixture'],
                            ['OTCX', 'OTC', 3, 'OTC fixture']]}
        parsed, report = cli.parse_listings(json.dumps(payload).encode())
        self.assertEqual(len(parsed['data']), 3)
        self.assertEqual(parsed['data'][0][2], 'BRK-B')
        self.assertEqual(report['excluded_rows'], 0)
        code, report, _, _ = self.import_file(payload, '--exclude-unassigned-exchange', '--exclude-otc')
        self.assertEqual(code, 0)
        self.assertEqual(report['input']['excluded_rows'], 2)
        self.assertEqual(CoverageStore(self.db).stats()['issuers'], 1)
        self.assertEqual(self.import_file(payload, '--exclude-otc', '--complete-snapshot')[0], 2)

    def test_queue_batches_are_bounded_deterministic_and_do_not_execute_work(self):
        self.import_file(listings(60))
        with mock.patch.object(cli.p, 'Fetcher') as fetcher:
            first = self.run_cli('enqueue')[1]
            second = self.run_cli('enqueue', '--limit', 5)[1]
            fetcher.assert_not_called()
        self.assertEqual(first['selected'], 25)
        self.assertEqual(second['selected'], 5)
        store = CoverageStore(self.db)
        self.assertEqual(store.stats()['jobs']['queued'], 30)
        self.assertEqual(store.stats()['payloads'], 0)
        self.assertEqual(first['jobs'][0]['cik'], '0000100000')
        self.assertEqual(second['jobs'][0]['cik'], '0000100025')
        self.assertEqual(self.run_cli('enqueue', '--ticker', 'T00000')[1]['selected'], 1)
        self.assertEqual(store.stats()['jobs']['queued'], 30)
        self.assertEqual(self.run_cli('enqueue', '--ticker', 'UNKNOWN')[0], 2)

    def test_bad_arguments_and_missing_provenance_fail_without_fetch(self):
        path = self.directory / 'input.json'
        path.write_text(json.dumps(listings()))
        with mock.patch.object(cli.p, 'Fetcher') as fetcher:
            self.assertEqual(self.run_cli('import-listings', '--file', path)[0], 2)
            self.assertEqual(self.run_cli('import-listings', '--file', path, '--source-url', 'https://example.test/listings',
                                          '--retrieved-at', '2025-01-01T00:00:00Z')[0], 2)
            self.assertEqual(self.run_cli('import-listings', '--file', path, '--source-url', cli.SEC_LISTINGS_URL,
                                          '--retrieved-at', '2025-01-01')[0], 2)
            for arguments in [('import-listings',), ('import-listings', '--fetch', '--file', path),
                              ('enqueue', '--limit', '0'), ('enqueue', '--limit', '501'), ('enqueue', '--limit', 'all')]:
                with self.assertRaises(SystemExit) as stopped:
                    self.run_cli(*arguments)
                self.assertEqual(stopped.exception.code, 2)
            fetcher.assert_not_called()

    def test_explicit_fetch_requires_real_contact_respects_pause_and_retains_prior_data_on_403(self):
        self.import_file(listings())
        with mock.patch.dict(os.environ, {'SEC_USER_AGENT': '', 'STOCK_BRAIN_SEC_ENABLED': '1'}), mock.patch.object(cli.p, 'Fetcher') as fetcher:
            self.assertEqual(self.run_cli('import-listings', '--fetch')[0], 2)
            fetcher.assert_not_called()
        with mock.patch.dict(os.environ, {'SEC_USER_AGENT': 'Fixture App operator@fixture-company.test', 'STOCK_BRAIN_SEC_ENABLED': '0'}), mock.patch.object(cli.p, 'Fetcher') as fetcher:
            self.assertEqual(self.run_cli('import-listings', '--fetch')[0], 2)
            fetcher.assert_not_called()
        with mock.patch.dict(os.environ, {'SEC_USER_AGENT': 'Fixture App operator@fixture-company.test', 'STOCK_BRAIN_SEC_ENABLED': '1'}), mock.patch.object(cli.p, 'Fetcher') as fetcher:
            fetcher.return_value.fetch.side_effect = ValueError('SEC access blocked (HTTP 403); remaining SEC requests skipped')
            code, _, error = self.run_cli('import-listings', '--fetch', '--complete-snapshot')
            self.assertEqual(code, 2)
            self.assertIn('403', error)
            fetcher.return_value.fetch.assert_called_once_with(cli.SEC_LISTINGS_URL, refresh=True)
            self.assertTrue(callable(fetcher.call_args.kwargs['before_request']))
        store = CoverageStore(self.db)
        self.assertEqual(store.stats()['active_listings'], 3)
        self.assertTrue(store.source_status('sec')['blocked'])
        with mock.patch.dict(os.environ, {'SEC_USER_AGENT': 'Fixture App operator@fixture-company.test', 'STOCK_BRAIN_SEC_ENABLED': '1'}), mock.patch.object(cli.p, 'Fetcher') as fetcher:
            code, _, error = self.run_cli('import-listings', '--fetch')
            self.assertEqual(code, 2)
            self.assertIn('cooldown', error)
            fetcher.assert_not_called()

    def test_seed_keeps_universe_unchanged_and_requires_exact_review_binding(self):
        original = (ROOT / 'config/universe.json').read_bytes()
        real_check = cli.check_managed_reviews
        def checked(root, documents):
            if documents[0].metadata['ticker'] == 'MSFT':
                raise ValueError('Fixture: profile changed after review')
            return real_check(root, documents)
        with mock.patch.object(cli, 'check_managed_reviews', side_effect=checked):
            code, report, error = self.run_cli('seed', '--root', ROOT)
        self.assertEqual((code, error), (0, ''))
        self.assertEqual(report['configured_issuers'], 10)
        self.assertEqual(report['reviewed_payloads'], 9)
        self.assertEqual(report['registered_without_review'][0]['ticker'], 'MSFT')
        self.assertEqual(CoverageStore(self.db).stats()['issuers'], 10)
        self.assertEqual(CoverageStore(self.db).stats()['payloads'], 9)
        self.assertEqual((ROOT / 'config/universe.json').read_bytes(), original)

    def test_status_is_bounded_and_does_not_label_registration_as_review(self):
        self.import_file(listings(50))
        code, report, errors = self.run_cli('status', '--limit', 4)
        self.assertEqual((code, errors), (0, ''))
        self.assertEqual(len(report['sample']), 4)
        self.assertEqual(report['total_issuers'], 50)
        self.assertEqual(report['summary']['payloads'], 0)
        self.assertIn('Registration does not establish', report['scope'])


if __name__ == '__main__':
    unittest.main()
