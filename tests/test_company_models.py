import copy
from datetime import date
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import company_models as cm
import research_insights


def load(ticker, history=None, quote=None):
    history = history if history is not None else json.loads((ROOT / 'research/financials' / f'{ticker}.json').read_text())
    quote = quote if quote is not None else json.loads((ROOT / 'research/market' / f'{ticker}.json').read_text())
    return cm.load_company_model(ROOT, ticker, history, quote)


class CompanyModelTests(unittest.TestCase):
    def test_all_company_baselines_and_thesis_comparisons_are_bound(self):
        for ticker in ('MSFT', 'MU', 'NVDA'):
            model = load(ticker)
            self.assertEqual(model['readiness']['status'], 'illustrative')
            self.assertTrue(model['readiness']['per_share_ready'])
            self.assertEqual([s['id'] for s in model['projection']['scenarios']], ['bear', 'base', 'bull'])
            for scenario in model['projection']['scenarios']:
                self.assertEqual([row['fiscal_year'] for row in scenario['rows']], list(cm.FORECAST_YEARS))
            thesis = research_insights.load_thesis(ROOT, ticker)
            self.assertEqual(thesis['comparison_count'], 3)
            self.assertTrue(all(f['threshold_basis'] == 'analyst_assumption' for f in thesis['falsifiers']))

    def test_profit_eps_fcf_and_dated_annualization(self):
        model = load('MSFT')
        result = model['projection']
        terminal = result['scenarios'][1]['terminal']
        self.assertAlmostEqual(terminal['revenue'], 579949657781.76, delta=.01)
        self.assertAlmostEqual(terminal['net_income'], 231979863112.704, delta=.01)
        self.assertAlmostEqual(terminal['free_cash_flow'], 162385904178.8928, delta=.01)
        expected_shares = 7453000000 * .995 ** 4
        expected_price = 231979863112.704 / expected_shares * 28
        self.assertAlmostEqual(terminal['price'], expected_price)
        interval = (date(2030, 6, 30) - date.fromisoformat(model['quote']['trade_at'][:10])).days / 365.25
        self.assertAlmostEqual(result['horizon_years'], interval)
        self.assertAlmostEqual(terminal['annualized_return'], (expected_price / model['quote']['price']) ** (1 / interval) - 1)
        self.assertNotEqual(interval, 4)

    def test_unverified_shares_withhold_per_share_outputs_without_losing_revenue_case(self):
        history = json.loads((ROOT / 'research/financials/MSFT.json').read_text())
        history['financials']['annual:2026-06-30']['shares_diluted']['model_usable'] = False
        model = load('MSFT', history=history)
        self.assertFalse(model['readiness']['per_share_ready'])
        self.assertIsNone(model['projection']['range']['price'])
        for scenario in model['projection']['scenarios']:
            self.assertGreater(scenario['terminal']['revenue'], 0)
            self.assertIsNone(scenario['terminal']['eps'])
            self.assertIsNone(scenario['terminal']['annualized_return'])
        self.assertEqual(cm.required_revenue_cagr(model)['status'], 'unavailable')

    def test_changed_or_unusable_annual_observation_blocks_frozen_model(self):
        history = json.loads((ROOT / 'research/financials/MU.json').read_text())
        history['financials']['annual:2026-09-03']['revenue']['value'] += 1000000
        model = load('MU', history=history)
        self.assertEqual(model['readiness']['status'], 'blocked')
        self.assertIn('historical_base_value_mismatch_revenue', model['readiness']['reasons'])
        self.assertEqual(model['projection']['scenarios'], [])

    def test_nvda_does_not_substitute_broader_issuer_fcf(self):
        model = load('NVDA')
        self.assertIsNone(model['base']['free_cash_flow'])
        self.assertFalse(model['base']['model_usable']['free_cash_flow'])
        self.assertEqual(model['base']['supplemental_issuer_fcf']['value'], 96575000000)
        self.assertFalse(model['base']['supplemental_issuer_fcf']['comparable_to_strict_fcf'])
        self.assertIn('strict_historical_fcf_unavailable_forecast_is_assumed_margin', model['readiness']['reasons'])

    def test_override_is_selected_scenario_only_and_input_is_immutable(self):
        model = load('MU')
        original = copy.deepcopy(model)
        result = cm.project_company_model(model, {'scenarioId': 'bear', 'revenueGrowth': .05, 'netMargin': .2, 'exitPe': 10})
        self.assertEqual(model, original)
        self.assertEqual(result['scenarios'][1], original['projection']['scenarios'][1])
        self.assertAlmostEqual(result['scenarios'][0]['terminal']['revenue'], 133188000000 * 1.05 ** 4, delta=.001)
        self.assertTrue(result['scenarios'][0]['modified_by_user'])
        self.assertEqual(cm.project_company_model(model, {'netMargin': '0.4'})['status'], 'blocked')
        self.assertEqual(cm.project_company_model(model, {'revenueGrowth': -1})['status'], 'blocked')
        self.assertEqual(cm.project_company_model(model, {'exitPe': 0})['status'], 'blocked')

    def test_reverse_valuation_round_trip_and_negative_earnings(self):
        model = load('NVDA')
        required = cm.required_revenue_cagr(model, 'base', target_return=.12)
        result = cm.project_company_model(model, {'revenueGrowth': required['required_revenue_cagr']})
        self.assertAlmostEqual(result['scenarios'][1]['terminal']['annualized_return'], .12)
        result = cm.project_company_model(model, {'netMargin': -.1})
        self.assertLess(result['scenarios'][1]['terminal']['eps'], 0)
        self.assertIsNone(result['scenarios'][1]['terminal']['price'])

    def test_bad_json_returns_visible_blocked_state(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'research/models'
            path.mkdir(parents=True)
            (path / 'MSFT.json').write_text('{')
            result = cm.load_company_model(directory, 'MSFT', {}, None)
            self.assertEqual(result['readiness']['status'], 'blocked')
            self.assertIsNone(cm.load_company_model(directory, 'UNKNOWN', {}, None))

    def test_browser_calculation_matches_python_at_each_fiscal_step(self):
        source = "import {projectCompanyModel} from './site/models.mjs'; let s=''; for await (const c of process.stdin) s+=c; process.stdout.write(JSON.stringify(projectCompanyModel(JSON.parse(s))));"
        for ticker in ('MSFT', 'MU', 'NVDA'):
            model = load(ticker)
            run = subprocess.run(['node', '--input-type=module', '-e', source], input=json.dumps(model), text=True, capture_output=True, check=True, cwd=ROOT)
            js = json.loads(run.stdout)
            py = model['projection']
            self.assertAlmostEqual(js['horizon_years'], py['horizon_years'])
            for left, right in zip(js['scenarios'], py['scenarios']):
                for lrow, rrow in zip(left['rows'], right['rows']):
                    for key in ('revenue', 'net_income', 'free_cash_flow', 'eps', 'shares_diluted'):
                        self.assertAlmostEqual(lrow[key], rrow[key], delta=max(abs(rrow[key]) * 1e-12, 1e-8))
                self.assertAlmostEqual(left['terminal']['annualized_return'], right['terminal']['annualized_return'])


if __name__ == '__main__':
    unittest.main()
