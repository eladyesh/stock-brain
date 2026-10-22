"""Financial-history controls: dates, cumulative periods, restatements and scope."""
import copy
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import financial_history as fh
import research_pipeline as rp

CIK = '0000000001'
COMPANY = {'ticker': 'TEST', 'cik': CIK, 'company_name': 'Test Issuer'}
REVENUE = 'RevenueFromContractWithCustomerExcludingAssessedTax'


def row(value, start, end, filed, fy, fp, accn, form=None):
    out = {'val': value, 'end': end, 'filed': filed, 'fy': fy, 'fp': fp, 'accn': accn,
           'form': form or ('10-K' if fp == 'FY' else '10-Q')}
    if start is not None:
        out['start'] = start
    return out


def facts(mapping):
    return {'cik': 1, 'entityName': 'Test Issuer', 'facts': {'us-gaap': {
        tag: {'label': tag, 'units': value if isinstance(value, dict) else {'USD': value}}
        for tag, value in mapping.items()}}}


def year(value=1000, *, filed='2025-08-01', fy=2025, accn='0000000001-25-000001'):
    return row(value, '2024-07-01', '2025-06-30', filed, fy, 'FY', accn)


def q(value, n, start, end, accn, filed):
    return row(value, start, end, filed, 2026, f'Q{n}', accn)


def split_review(metric, source_rows, *, evidence_filed='2026-02-01', effective='2025-09-01'):
    """Synthetic filing review with explicit values, precision and document hashes."""
    tag = fh.METRICS[metric][1][0]
    return {'review_id': 'TEST-10-for-1', 'type': 'stock_split', 'cik': CIK,
            'effective_date': effective, 'new_shares_per_old_share': 10,
            'evidence': [{'source_id': 'SPLIT-TEST', 'filed': evidence_filed, 'sha256': 'a' * 64,
                          'title': 'Synthetic split disclosure', 'url': 'https://www.sec.gov/test'}],
            'observations': [{**fh._provenance(r, tag, fh.METRICS[metric][0], CIK),
                              'decimals': 2 if metric.startswith('eps_') else -6,
                              'split_basis': 'pre_split' if r['filed'] < effective else 'post_split',
                              'source_document': {'sha256': 'b' * 64, 'url': 'https://www.sec.gov/test'}} for r in source_rows]}


class FinancialHistoryTests(unittest.TestCase):
    def test_later_series_gate_reaches_derived_gross_profit(self):
        current = row(1200, '2025-07-01', '2026-06-30', '2026-08-01', 2026, 'FY', '0000000001-26-000004')
        data = facts({REVENUE: [year()], 'Revenues': [current],
                      'CostOfGoodsAndServicesSold': [dict(current, val=700)]})
        history = fh.normalize_companyfacts(data, COMPANY, '2026-10-18')
        gross = fh.get_metric(history, 'gross_profit')
        self.assertEqual(gross['value'], 500)
        self.assertFalse(gross['model_usable'])
        self.assertIn('definition_changed_across_series', gross['flags'])
        self.assertIn('derived_input_requires_review', gross['flags'])
        tampered = copy.deepcopy(history)
        tampered['financials']['annual:2026-06-30']['gross_profit'].update(
            flags=[], model_usable=True, comparison_status='comparable')
        with self.assertRaisesRegex(ValueError, 'derived eligibility exceeds inputs'):
            fh.validate_history(tampered)

    def test_comparative_filing_focus_does_not_change_fiscal_year(self):
        old = year()
        repeated = year(filed='2026-08-01', fy=2026, accn='0000000001-26-000004')
        current = row(1200, '2025-07-01', '2026-06-30', '2026-08-01', 2026, 'FY', '0000000001-26-000004')
        history = fh.normalize_companyfacts(facts({REVENUE: [old, repeated, current]}), COMPANY, '2026-10-18')
        metric = fh.get_metric(history, 'revenue', period_end='2025-06-30')
        self.assertEqual(metric['period']['fiscal_year'], 2025)
        self.assertEqual(metric['provenance'][0]['filing_fiscal_year'], 2026)
        self.assertIsNone(fh.get_metric(history, 'revenue', fiscal_year=2027))

    def test_calendar_frame_is_never_used_as_fiscal_quarter(self):
        quarter = q(300, 1, '2025-07-01', '2025-09-30', '0000000001-25-000002', '2025-10-20')
        quarter['frame'] = 'CY2025Q3'
        history = fh.normalize_companyfacts(facts({REVENUE: [year(), quarter]}), COMPANY, '2025-11-01')
        metric = fh.get_metric(history, 'revenue', 'quarterly')
        self.assertEqual(metric['period']['fiscal_quarter'], 1)
        self.assertEqual(metric['period']['fiscal_year'], 2026)
        self.assertEqual(metric['provenance'][0]['calendar_frame'], 'CY2025Q3')

    def test_conflicting_fiscal_year_is_unknown_not_silently_corrected(self):
        quarter = q(300, 1, '2025-07-01', '2025-09-30', '0000000001-25-000002', '2025-10-20')
        quarter['fy'] = 2025
        history = fh.normalize_companyfacts(facts({REVENUE: [year(), quarter]}), COMPANY, '2025-11-01')
        metric = fh.get_metric(history, 'revenue', 'quarterly')
        self.assertIsNone(metric['period']['fiscal_year'])
        self.assertIn('conflicting_fiscal_year', metric['period']['flags'])
        self.assertIsNone(fh.get_metric(history, 'revenue', 'quarterly', fiscal_year=2025))

    def test_ytd_cash_flow_becomes_standalone_only_by_exact_difference(self):
        q1 = q(300, 1, '2025-07-01', '2025-09-30', '0000000001-25-000002', '2025-10-20')
        q2 = q(350, 2, '2025-10-01', '2025-12-31', '0000000001-26-000001', '2026-01-20')
        cf1 = dict(q1, val=100)
        cf2 = dict(q2, start='2025-07-01', val=240)
        history = fh.normalize_companyfacts(facts({REVENUE: [year(), q1, q2], 'NetCashProvidedByUsedInOperatingActivities': [cf1, cf2]}), COMPANY, '2026-02-01')
        metric = fh.get_metric(history, 'operating_cash_flow', 'quarterly')
        self.assertEqual(metric['value'], 140)
        self.assertEqual(metric['status'], 'derived')
        self.assertIn('cross_filing_derivation', metric['flags'])
        self.assertEqual(metric['period']['start'], '2025-10-01')
        self.assertEqual(len(metric['provenance']), 2)

    def test_mismatched_ytd_start_cannot_be_used(self):
        q1 = q(300, 1, '2025-07-01', '2025-09-30', '0000000001-25-000002', '2025-10-20')
        q2 = q(350, 2, '2025-10-01', '2025-12-31', '0000000001-26-000001', '2026-01-20')
        cf1 = dict(q1, val=100)
        cf2 = dict(q2, start='2025-07-02', val=240)
        history = fh.normalize_companyfacts(facts({REVENUE: [year(), q1, q2], 'NetCashProvidedByUsedInOperatingActivities': [cf1, cf2]}), COMPANY, '2026-02-01')
        metric = fh.get_metric(history, 'operating_cash_flow', 'quarterly')
        self.assertIsNone(metric['value'])
        self.assertEqual(metric['status'], 'missing_required_source')

    def test_q4_nonadditive_eps_and_shares_are_not_subtracted(self):
        annual = row(1200, '2025-07-01', '2026-06-30', '2026-08-01', 2026, 'FY', '0000000001-26-000004')
        third = q(300, 3, '2026-01-01', '2026-03-31', '0000000001-26-000003', '2026-04-20')
        third_ytd = dict(third, start='2025-07-01', val=850)
        history = fh.normalize_companyfacts(facts({REVENUE: [year(), third, third_ytd, annual],
            'EarningsPerShareDiluted': {'USD/shares': [dict(annual, val=10), dict(third_ytd, val=7)]},
            'WeightedAverageNumberOfDilutedSharesOutstanding': {'shares': [dict(annual, val=100), dict(third_ytd, val=110)]}}), COMPANY, '2026-08-02')
        self.assertEqual(fh.get_metric(history, 'revenue', 'quarterly')['value'], 350)
        self.assertEqual(fh.get_metric(history, 'revenue', 'quarterly')['period']['start'], '2026-04-01')
        self.assertIsNone(fh.get_metric(history, 'eps_diluted', 'quarterly')['value'])
        self.assertIsNone(fh.get_metric(history, 'shares_diluted', 'quarterly')['value'])

    def test_latest_revision_is_retained_and_blocks_model_grade(self):
        revised = year(990, filed='2025-09-01', accn='0000000001-25-000003')
        revised['form'] = '10-K/A'
        data = facts({REVENUE: [year(), revised]})
        before = fh.exact_metric(data, 'revenue', '2024-07-01', '2025-06-30', '2025-08-10', CIK)
        after = fh.exact_metric(data, 'revenue', '2024-07-01', '2025-06-30', '2025-09-10', CIK)
        self.assertEqual(before['value'], 1000)
        self.assertEqual(after['value'], 990)
        self.assertEqual(after['conflicts'][0]['alternatives'][0]['source_value'], 1000)
        self.assertFalse(after['model_usable'])

    def test_same_day_conflict_fails_closed(self):
        other = year(999, accn='0000000001-25-000002')
        data = facts({REVENUE: [year(), other]})
        result = fh.exact_metric(data, 'revenue', '2024-07-01', '2025-06-30', '2025-08-10', CIK)
        self.assertEqual(result['status'], 'conflicted')
        self.assertIsNone(result['value'])
        self.assertEqual(result['evidence_label'], 'contradicted_source')

    def test_revised_cumulative_fact_blocks_quarter_difference(self):
        q1 = q(300, 1, '2025-07-01', '2025-09-30', '0000000001-25-000002', '2025-10-20')
        q2 = q(350, 2, '2025-10-01', '2025-12-31', '0000000001-26-000001', '2026-01-20')
        cf1 = dict(q1, val=100)
        cf1_revised = dict(cf1, val=110, filed='2026-01-20', accn=q2['accn'], fp='Q2')
        cf2 = dict(q2, start='2025-07-01', val=240)
        history = fh.normalize_companyfacts(facts({REVENUE: [year(), q1, q2], 'NetCashProvidedByUsedInOperatingActivities': [cf1, cf1_revised, cf2]}), COMPANY, '2026-02-01')
        metric = fh.get_metric(history, 'operating_cash_flow', 'quarterly')
        self.assertIsNone(metric['value'])
        self.assertIn('unreconciled_cumulative_revision', metric['flags'])
        self.assertTrue(metric['conflicts'])

    def test_units_adjusted_basis_and_instant_dates_are_not_mixed(self):
        data = facts({REVENUE: {'EUR': [year()]}, 'AdjustedNetIncome': [year(800)],
                      'CashAndCashEquivalentsAtCarryingValue': [row(200, None, '2025-07-15', '2025-08-01', 2025, 'FY', '0000000001-25-000001')]})
        self.assertIsNone(fh.exact_metric(data, 'revenue', '2024-07-01', '2025-06-30', '2025-09-01', CIK)['value'])
        self.assertIsNone(fh.exact_metric(data, 'net_income', '2024-07-01', '2025-06-30', '2025-09-01', CIK)['value'])
        self.assertIsNone(fh.exact_metric(data, 'cash_and_equivalents', None, '2025-06-30', '2025-09-01', CIK)['value'])

    def test_capex_sign_and_fcf_use_reported_cash_flows(self):
        data = facts({REVENUE: [year()], 'NetCashProvidedByUsedInOperatingActivities': [year(200)],
                      'PaymentsToAcquirePropertyPlantAndEquipment': [year(70)]})
        history = fh.normalize_companyfacts(data, COMPANY, '2025-08-10')
        self.assertEqual(fh.get_metric(history, 'capex')['value'], -70)
        self.assertEqual(fh.get_metric(history, 'capex')['provenance'][0]['source_value'], 70)
        self.assertEqual(fh.get_metric(history, 'free_cash_flow')['value'], 130)
        self.assertEqual(fh.get_metric(history, 'free_cash_flow')['evidence_label'], 'derived_calculation')

    def test_missing_short_term_debt_is_not_zero(self):
        debt = year(300)
        debt.pop('start')
        data = facts({REVENUE: [year()], 'LongTermDebt': [debt]})
        history = fh.normalize_companyfacts(data, COMPANY, '2025-08-10')
        self.assertEqual(fh.get_metric(history, 'long_term_debt_total')['value'], 300)
        self.assertIsNone(fh.get_metric(history, 'debt_total')['value'])

    def test_ticker_and_cik_provenance_integrity(self):
        data = facts({REVENUE: [year()]})
        with self.assertRaises(ValueError):
            fh.normalize_companyfacts(data, {**COMPANY, 'cik': '0000000002'}, '2025-08-10')
        history = fh.normalize_companyfacts(data, COMPANY, '2025-08-10')
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            rp.write_json(root / 'research/financials/TEST.json', history)
            loaded = fh.load_history(root, 'test')
            self.assertEqual(loaded['ticker'], 'TEST')
            self.assertIsNone(fh.load_history(root, 'MISSING'))
            bad = copy.deepcopy(history)
            bad['financials'][bad['periods'][0]['id']]['revenue']['provenance'][0]['filed'] = '2099-01-01'
            with self.assertRaises(ValueError):
                fh.validate_history(bad)
            with self.assertRaises(ValueError):
                fh.load_history(root, '../TEST')

    def test_53_week_fiscal_year_and_14_week_quarter(self):
        annual = row(1000, '2024-09-01', '2025-09-06', '2025-10-01', 2025, 'FY', '0000000001-25-000004')
        third = row(250, '2025-03-02', '2025-05-31', '2025-06-25', 2025, 'Q3', '0000000001-25-000003')
        ytd = dict(third, start='2024-09-01', val=700)
        history = fh.normalize_companyfacts(facts({REVENUE: [annual, third, ytd]}), COMPANY, '2025-10-02')
        metric = fh.get_metric(history, 'revenue', 'quarterly')
        self.assertEqual(metric['value'], 300)
        self.assertEqual(fh.days(metric['period']['start'], metric['period']['end']), 98)
        self.assertEqual(metric['period']['fiscal_quarter'], 4)

    def test_future_filings_cannot_enter_historical_snapshot(self):
        data = facts({REVENUE: [year(), year(1200, filed='2026-08-01', accn='0000000001-26-000004')]})
        result = fh.exact_metric(data, 'revenue', '2024-07-01', '2025-06-30', '2025-12-31', CIK)
        self.assertEqual(result['value'], 1000)
        self.assertFalse(result['conflicts'])

    def test_newer_tag_does_not_lose_to_obsolete_tag_preference(self):
        newer = year(1100, filed='2026-08-01', accn='0000000001-26-000004')
        result = fh.exact_metric(facts({REVENUE: [year()], 'Revenues': [newer]}), 'revenue',
                                '2024-07-01', '2025-06-30', '2026-08-02', CIK)
        self.assertEqual(result['value'], 1100)
        self.assertEqual(result['definition_tag'], 'Revenues')
        self.assertIn('alternative_tag_scope_differs', result['flags'])
        self.assertFalse(result['model_usable'])
        self.assertEqual(result['conflicts'][0]['alternatives'][0]['source_value'], 1000)

    def test_profit_attribution_and_productive_assets_are_separate(self):
        data = facts({REVENUE: [year()], 'ProfitLoss': [year(100)],
                      'NetIncomeLossAvailableToCommonStockholdersBasic': [year(90)],
                      'PaymentsToAcquireProductiveAssets': [year(80)],
                      'NetCashProvidedByUsedInOperatingActivities': [year(200)]})
        history = fh.normalize_companyfacts(data, COMPANY, '2025-08-10')
        self.assertIsNone(fh.get_metric(history, 'net_income')['value'])
        self.assertEqual(fh.get_metric(history, 'net_income_common')['value'], 90)
        self.assertEqual(fh.get_metric(history, 'net_income_including_noncontrolling_interests')['value'], 100)
        self.assertEqual(fh.get_metric(history, 'purchases_of_productive_assets')['value'], -80)
        self.assertIsNone(fh.get_metric(history, 'capex')['value'])
        self.assertIsNone(fh.get_metric(history, 'free_cash_flow')['value'])

    def test_failed_gross_profit_tieout_blocks_affected_model_inputs(self):
        data = facts({REVENUE: [year()], 'CostOfRevenue': [year(700)], 'GrossProfit': [year(320)]})
        history = fh.normalize_companyfacts(data, COMPANY, '2025-08-10')
        result = fh.get_metric(history, 'gross_profit')
        self.assertEqual(result['value'], 320)
        self.assertIn('gross_profit_tieout_failed', result['flags'])
        self.assertFalse(result['model_usable'])
        self.assertTrue(any(c['result'] == 'fail' for c in history['validation_checks']))

    def test_source_verified_split_reconciles_eps_and_retains_versions(self):
        old = year(32.98)
        new = year(3.30, filed='2026-02-01', accn='0000000001-26-000001')
        review = split_review('eps_diluted', [old, new])
        data = facts({REVENUE: [year()], 'EarningsPerShareDiluted': {'USD/shares': [old, new]}})
        h = fh.normalize_companyfacts(data, COMPANY, '2026-02-02', normalization_reviews=[review])
        c = fh.get_metric(h, 'eps_diluted')
        self.assertEqual(c['value'], 3.3)
        self.assertTrue(c['model_usable'])
        self.assertFalse(c['conflicts'])
        self.assertEqual(c['resolved_conflicts'][0]['alternatives'][0]['source_value'], 32.98)
        self.assertIn('SEC-' + old['accn'], h['source_index'])
        self.assertEqual(c['status'], 'reported')
        self.assertEqual(h['coverage']['resolved_conflict_cells'], 1)

    def test_source_rounding_intervals_reconcile_weighted_shares(self):
        old = year(427_000_000)
        new = year(4_272_000_000, filed='2026-02-01', accn='0000000001-26-000001')
        data = facts({'WeightedAverageNumberOfDilutedSharesOutstanding': {'shares': [old, new]}})
        cell = fh.exact_metric(data, 'shares_diluted', old['start'], old['end'], '2026-02-02', CIK)
        fh.reconcile_share_split(cell, 'shares_diluted', CIK, '2026-02-02', [split_review('shares_diluted', [old, new])])
        self.assertTrue(cell['model_usable'])
        self.assertEqual(cell['value'], 4_272_000_000)
        self.assertFalse(cell['conflicts'])

    def test_oldest_pre_split_fact_is_explicit_derived_value(self):
        old = year(3.85)
        data = facts({REVENUE: [year()], 'EarningsPerShareDiluted': {'USD/shares': [old]}})
        h = fh.normalize_companyfacts(data, COMPANY, '2026-02-02', normalization_reviews=[split_review('eps_diluted', [old])])
        c = fh.get_metric(h, 'eps_diluted')
        self.assertAlmostEqual(c['value'], 0.385)
        self.assertEqual(c['status'], 'derived')
        self.assertEqual(c['evidence_label'], 'derived_calculation')
        self.assertEqual(c['provenance'][0]['source_value'], 3.85)
        self.assertTrue(c['model_usable'])
        damaged = copy.deepcopy(h)
        damaged['financials'][c['period']['id']]['eps_diluted']['value'] = 3.85
        with self.assertRaises(ValueError):
            fh.validate_history(damaged)

    def test_split_does_not_waive_unexplained_revision_or_unreviewed_source(self):
        old = year(32.98)
        new = year(4.0, filed='2026-02-01', accn='0000000001-26-000001')
        data = facts({'EarningsPerShareDiluted': {'USD/shares': [old, new]}})
        review = split_review('eps_diluted', [old, new])
        c = fh.exact_metric(data, 'eps_diluted', old['start'], old['end'], '2026-02-02', CIK)
        fh.reconcile_share_split(c, 'eps_diluted', CIK, '2026-02-02', [review])
        self.assertFalse(c['model_usable'])
        self.assertTrue(c['conflicts'])
        self.assertIn('revision_requires_review', c['flags'])
        new['val'] = 3.3
        unreviewed = fh.exact_metric(data, 'eps_diluted', old['start'], old['end'], '2026-02-02', CIK)
        fh.reconcile_share_split(unreviewed, 'eps_diluted', CIK, '2026-02-02', [review])
        self.assertFalse(unreviewed['model_usable'])
        self.assertNotIn('share_basis', unreviewed)

    def test_split_review_cannot_leak_past_historical_cutoff(self):
        old = year(32.98)
        new = year(3.3, filed='2026-02-01', accn='0000000001-26-000001')
        review = split_review('eps_diluted', [old, new])
        data = facts({REVENUE: [year()], 'EarningsPerShareDiluted': {'USD/shares': [old, new]}})
        h = fh.normalize_companyfacts(data, COMPANY, '2025-12-01', normalization_reviews=[review])
        self.assertEqual(fh.get_metric(h, 'eps_diluted')['value'], 32.98)
        self.assertFalse(fh.get_metric(h, 'eps_diluted')['model_usable'])
        self.assertNotIn('normalization_reviews', h)
        self.assertNotIn('SPLIT-TEST', h['source_index'])

    def test_post_cutoff_observation_is_removed_even_when_action_is_known(self):
        old = year(32.98)
        later = year(3.3, filed='2026-02-01', accn='0000000001-26-000001')
        review = split_review('eps_diluted', [old, later], evidence_filed='2025-10-01')
        data = facts({REVENUE: [year()], 'EarningsPerShareDiluted': {'USD/shares': [old, later]}})
        h = fh.normalize_companyfacts(data, COMPANY, '2025-12-01', normalization_reviews=[review])
        self.assertEqual(len(h['normalization_reviews'][0]['observations']), 1)
        self.assertAlmostEqual(fh.get_metric(h, 'eps_diluted')['value'], 3.298)
        self.assertEqual(fh.get_metric(h, 'eps_diluted')['status'], 'derived')
        self.assertNotIn('SEC-' + later['accn'], h['source_index'])

    def test_split_review_rejects_wrong_issuer_or_missing_document_proof(self):
        data = facts({REVENUE: [year()]})
        review = split_review('eps_diluted', [year(3.3)])
        review['cik'] = '0000000002'
        with self.assertRaises(ValueError):
            fh.normalize_companyfacts(data, COMPANY, '2026-02-02', normalization_reviews=[review])
        review['cik'] = CIK
        review['observations'][0]['source_document']['sha256'] = ''
        with self.assertRaises(ValueError):
            fh.normalize_companyfacts(data, COMPANY, '2026-02-02', normalization_reviews=[review])

    def test_same_basis_and_same_day_conflicts_stay_gated_after_review(self):
        first = year(3.3, filed='2026-02-01', accn='0000000001-26-000001')
        second = year(3.31, filed='2026-02-02', accn='0000000001-26-000002')
        data = facts({'EarningsPerShareDiluted': {'USD/shares': [first, second]}})
        review = split_review('eps_diluted', [first, second])
        c = fh.exact_metric(data, 'eps_diluted', first['start'], first['end'], '2026-02-03', CIK)
        fh.reconcile_share_split(c, 'eps_diluted', CIK, '2026-02-03', [review])
        self.assertFalse(c['model_usable'])
        self.assertTrue(c['conflicts'])
        second['filed'] = first['filed']
        c = fh.exact_metric(data, 'eps_diluted', first['start'], first['end'], '2026-02-03', CIK)
        fh.reconcile_share_split(c, 'eps_diluted', CIK, '2026-02-03', [review])
        self.assertIsNone(c['value'])
        self.assertEqual(c['status'], 'conflicted')


if __name__ == '__main__':
    unittest.main()
