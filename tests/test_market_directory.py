from copy import deepcopy
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from coverage_store import CoverageStore
import market_directory as directory
from market_api import serve_market


NOW = datetime(2026, 10, 22, 13, tzinfo=timezone.utc)


def raw_file(name, rows, stamp='1022202608:01'):
    header = ('Symbol|Security Name|Market Category|Test Issue|Financial Status|Round Lot Size|ETF|NextShares'
              if name == directory.FILES[0] else 'ACT Symbol|Security Name|Exchange|CQS Symbol|ETF|Round Lot Size|Test Issue|NASDAQ Symbol')
    return (header + '\n' + '\n'.join('|'.join(r) for r in rows) + '\nFile Creation Time: ' + stamp + '|||||||\n').encode()


def fixtures(count=12):
    nasdaq = [[f'T{i}', f'Company {i} - Common Stock', 'Q', 'N', 'N', '100', 'N', 'N'] for i in range(count)]
    other = [['ETF1', 'Broad Equity ETF', 'P', 'ETF1', 'Y', '100', 'N', 'ETF1'],
             ['TEST', 'Test Common Stock', 'N', 'TEST', 'N', '100', 'Y', 'TEST'],
             ['PREF', 'Company Preferred Stock', 'N', 'PREF', 'N', '100', 'N', 'PREF'],
             ['ADR', 'Example American Depositary Shares', 'N', 'ADR', 'N', '100', 'N', 'ADR']]
    return [directory.parse_directory(raw_file(name, rows), name, retrieved_at=NOW, now=NOW)
            for name, rows in zip(directory.FILES, [nasdaq, other])]


class DirectoryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.store = CoverageStore(Path(self.temp.name) / 'data.db', clock=lambda: NOW)
        self.store.seed_companies([{'cik': 123, 'ticker': 'T0', 'company_name': 'Company 0', 'exchange': 'NASDAQ'}])

    def test_flags_instrument_types_and_issuer_mapping_are_separate(self):
        directory.import_directories(self.store, fixtures())
        status = directory.directory_status(self.store)
        self.assertEqual(status['listed_securities'], 15)
        self.assertEqual(status['equity_candidates'], 14)
        self.assertEqual(status['linked_issuer_count'], 1)
        page = directory.list_securities(self.store)
        self.assertEqual(page['total'], 14)
        self.assertNotIn('ETF1', {x['ticker'] for x in page['items']})
        self.assertNotIn('TEST', {x['ticker'] for x in directory.list_securities(self.store, instrument='all')['items']})
        linked = directory.list_securities(self.store, query='T0')['items'][0]
        self.assertEqual(linked['cik'], '0000000123')
        self.assertEqual(linked['research_status'], 'not_reviewed')
        self.assertTrue(all(v['status'] == 'not_collected' for v in linked['datasets'].values()))
        unknown = directory.list_securities(self.store, query='T1')['items'][0]
        self.assertIsNone(unknown['cik'])

    def test_malformed_truncated_duplicate_flag_and_stale_files_are_rejected(self):
        name = directory.FILES[0]
        row = ['X', 'Example - Common Stock', 'Q', 'N', 'N', '100', 'N', 'N']
        good = raw_file(name, [row])
        invalid = [good.rsplit(b'File Creation Time:', 1)[0], raw_file(name, [row, row]),
                   raw_file(name, [[*row[:6], 'UNKNOWN', 'N']]), raw_file(name, [row], '1001202608:01'),
                   raw_file(name, [row], '1122202608:01'), b'<html>Unavailable</html>']
        for raw in invalid:
            with self.subTest(raw=raw[:60]), self.assertRaises(ValueError):
                directory.parse_directory(raw, name, retrieved_at=NOW, now=NOW)

    def test_packaged_unit_is_not_one_of_its_components_or_an_issuer_name(self):
        record = {'ETF': 'N', 'Security Name': 'Example Acquisition Units, each consisting of one ordinary share and one redeemable warrant'}
        self.assertEqual(directory.classify(record)[0], 'unit')
        record['Security Name'] = 'Unit Corporation - Common Stock'
        self.assertEqual(directory.classify(record)[0], 'common_stock')
        record['Security Name'] = 'Example Acquisition Redeemable warrants, each exercisable for one ordinary share'
        self.assertEqual(directory.classify(record)[0], 'warrant')

    def test_atomic_pair_and_shrink_guards_preserve_prior_registry(self):
        initial = fixtures()
        directory.import_directories(self.store, initial)
        before = directory.list_securities(self.store, instrument='all')
        for bad in ([initial[0]], [dict(initial[0], rows=initial[0]['rows'][:2]), initial[1]]):
            with self.assertRaises(ValueError): directory.import_directories(self.store, bad)
            self.assertEqual(directory.list_securities(self.store, instrument='all'), before)
        older = deepcopy(initial)
        older[1]['source']['file_created_at_local'] = '2026-10-21T08:01:00'
        with self.assertRaises(ValueError): directory.import_directories(self.store, older)

    def test_changed_name_does_not_reuse_issuer_or_dataset_identity(self):
        initial = fixtures()
        directory.import_directories(self.store, initial)
        key = initial[0]['rows'][0]['listing_key']
        with self.store._connection(write=True) as db:
            db.execute('INSERT INTO market_observations(listing_key,identity_revision,dataset,provider,retrieved_at,as_of,source_json,payload_json,sha256) VALUES (?,?,?,?,?,?,?,?,?)',
                       (key, 1, 'prices', 'synthetic', NOW.isoformat(), NOW.isoformat(), '{}', '{"price":1}', 'a' * 64))
        self.assertEqual(directory.security_detail(self.store, key)['datasets']['prices']['status'], 'available')
        changed = deepcopy(initial)
        changed[0]['rows'][0]['security_name'] = 'Unrelated Corp - Common Stock'
        directory.import_directories(self.store, changed)
        record = directory.security_detail(self.store, key)
        self.assertEqual(record['identity_revision'], 2)
        self.assertIsNone(record['cik'])
        self.assertEqual(record['datasets']['prices']['status'], 'not_collected')
        self.assertEqual(self.store.company('123')['company_name'], 'Company 0')

    def test_absence_retains_history_without_claiming_delisting(self):
        initial = fixtures()
        directory.import_directories(self.store, initial)
        key = initial[0]['rows'][-1]['listing_key']
        shortened = deepcopy(initial)
        shortened[0]['rows'] = shortened[0]['rows'][:-1]
        directory.import_directories(self.store, shortened)
        self.assertEqual(directory.security_detail(self.store, key)['directory_status'], 'not_in_latest_directory')
        self.assertEqual(directory.list_securities(self.store, status='all')['total'], 14)
        self.assertEqual(directory.list_securities(self.store)['total'], 13)
        directory.import_directories(self.store, initial)
        self.assertEqual(directory.security_detail(self.store, key)['directory_status'], 'present')
        self.assertEqual(directory.security_detail(self.store, key)['identity_revision'], 2)

    def test_lost_issuer_mapping_invalidates_old_observations_even_without_name_change(self):
        initial = fixtures()
        directory.import_directories(self.store, initial)
        key = initial[0]['rows'][0]['listing_key']
        with self.store._connection(write=True) as db:
            db.execute("UPDATE listings SET status='inactive' WHERE ticker='T0'")
        directory.import_directories(self.store, initial)
        record = directory.security_detail(self.store, key)
        self.assertIsNone(record['cik'])
        self.assertEqual(record['identity_revision'], 2)

    def test_bounded_search_filters_and_no_wildcard_expansion(self):
        directory.import_directories(self.store, fixtures())
        status, result = serve_market(self.store, '/api/securities', 'limit=2&offset=1')
        self.assertEqual(status, '200 OK')
        self.assertEqual(len(result['items']), 2)
        self.assertEqual(serve_market(self.store, '/api/securities', 'q=%25')[1]['total'], 0)
        self.assertEqual(serve_market(self.store, '/api/securities', 'instrument=etf')[1]['total'], 1)
        self.assertEqual(serve_market(self.store, '/api/securities', 'instrument=preferred')[1]['total'], 1)
        for query in ('limit=101', 'q=x&q=y', 'offset=-1', 'instrument=sql', 'q=%GG', 'exchange=x%27', 'unknown=x'):
            self.assertEqual(serve_market(self.store, '/api/securities', query)[0], '400 Bad Request')
        self.assertEqual(serve_market(self.store, '/api/securities/../../etc/passwd')[0], '404 Not Found')
        self.assertEqual(serve_market(None, '/api/securities')[0], '503 Service Unavailable')
        self.assertIsNone(serve_market(self.store, '/unrelated'))

    def test_retrieval_freshness_does_not_erase_source_file_date(self):
        directory.import_directories(self.store, fixtures())
        self.store.clock = lambda: NOW + timedelta(hours=40)
        status = directory.directory_status(self.store)
        self.assertEqual(status['status'], 'stale')
        self.assertEqual(status['sources'][directory.FILES[0]]['file_created_at_local'], '2026-10-22T08:01:00')

    def test_partnership_and_preferred_units_are_stocks_but_packaged_units_are_not(self):
        cases = {'Alliance Resource Partners L.P. Common Units Representing Limited Partnership Interests': 'partnership_unit',
                 'Brookfield Renewable Partners L.P. Limited Partnership Units': 'partnership_unit',
                 'Brookfield Property Partners L.P. Cumulative Redeemable Preferred Units': 'preferred',
                 'Example Units, each consisting of a preferred share and a warrant': 'unit',
                 'Example Redeemable Warrants to purchase Common Units': 'warrant'}
        for name, expected in cases.items():
            with self.subTest(name=name):
                self.assertEqual(directory.classify({'ETF': 'N', 'Security Name': name})[0], expected)
        directory.import_directories(self.store, fixtures())
        scope = directory.directory_status(self.store)['stock_scope']
        self.assertEqual(scope['otc'], 'not_collected')
        self.assertIn('preferred', scope['included_types'])


if __name__ == '__main__': unittest.main()
