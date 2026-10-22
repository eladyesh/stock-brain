"""TTM checks protect exact periods, evidence availability and metric arithmetic."""
from copy import deepcopy
from datetime import date, timedelta
import json
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import ttm


def history_fixture():
    periods = [
        ("2025-07-01", "2025-09-30", 2025, 3),
        ("2025-10-01", "2025-12-31", 2025, 4),
        ("2026-01-01", "2026-03-31", 2026, 1),
        ("2026-04-01", "2026-06-30", 2026, 2),
    ]
    history = {"ticker": "TEST", "as_of": "2026-08-01", "periods": [], "financials": {}, "source_index": {}}
    for i, (start, end, year, quarter) in enumerate(periods, 1):
        p = {"id": "quarterly:" + end, "type": "quarterly", "start": start, "end": end,
             "fiscal_year": year, "fiscal_quarter": quarter, "label": f"Q{quarter} FY{year}", "flags": []}
        history["periods"].append(p)
        sid = "TEST-FILING-" + str(i)
        filed = (date.fromisoformat(end) + timedelta(days=20)).isoformat()
        url = "https://example.test/filings/" + str(i)
        history["source_index"][sid] = {"source_id": sid, "as_of_date": filed, "url": url}
        cells = {}
        amounts = {m: i * 10 for m in ttm.FLOW_METRICS}
        amounts.update(revenue=i * 100, gross_profit=i * 40, operating_income=i * 30,
                       net_income=i * 20, operating_cash_flow=i * 25, capex=-i * 5,
                       free_cash_flow=i * 20, stock_based_compensation=i * 2)
        for metric in ttm.FLOW_METRICS + ttm.BALANCE_METRICS + ("eps_diluted", "shares_diluted"):
            instant = metric in ttm.BALANCE_METRICS
            unit = "shares" if metric.startswith("shares_") else "USD/shares" if metric.startswith("eps_") else "USD"
            value = amounts.get(metric, i * 7)
            source = {"source_id": sid, "taxonomy": "us-gaap", "tag": metric, "unit": unit,
                      "start": None if instant else start, "end": end, "filed": filed,
                      "source_value": -value if metric == "capex" else value, "url": url}
            cells[metric] = {"status": "reported", "value": value, "unit": unit, "basis": "US GAAP",
                             "evidence_label": "fact_source_reported", "confidence": "high",
                             "model_usable": True, "comparison_status": "comparable",
                             "definition_tag": metric, "provenance": [source], "conflicts": [], "flags": []}
        history["financials"][p["id"]] = cells
    return history


class TTMTests(unittest.TestCase):
    def setUp(self):
        self.history = history_fixture()

    def cell(self, metric, n=-1):
        return self.history["financials"][self.history["periods"][n]["id"]][metric]

    def test_exact_four_quarters_cross_fiscal_year_and_provenance(self):
        original = deepcopy(self.history)
        result = ttm.build_ttm(self.history)
        self.assertEqual(result["status"], "available")
        self.assertEqual(result["period"]["start"], "2025-07-01")
        self.assertEqual(result["period"]["end"], "2026-06-30")
        self.assertEqual(result["financials"]["revenue"]["value"], 1000)
        self.assertEqual(len(result["financials"]["revenue"]["inputs"]), 4)
        self.assertEqual(len(result["financials"]["revenue"]["provenance"]), 4)
        self.assertEqual(len(result["source_ids"]), 4)
        self.assertEqual(self.history, original)

    def test_ratios_from_sums_not_average_of_quarterly_ratios(self):
        self.cell("net_income", 0)["value"] = -50
        self.cell("net_income", 0)["provenance"][0]["source_value"] = -50
        result = ttm.build_ttm(self.history)
        self.assertAlmostEqual(result["ratios"]["net_margin"]["value"], 0.13)
        self.assertEqual(result["ratios"]["net_margin"]["unit"], "ratio")
        self.assertEqual(result["financials"]["capex"]["value"], -50)

    def test_nonadditive_measures_never_summed_and_balance_separate(self):
        result = ttm.build_ttm(self.history)
        self.assertNotIn("eps_diluted", result["financials"])
        self.assertNotIn("shares_diluted", result["financials"])
        self.assertNotIn("cash_and_equivalents", result["financials"])
        self.assertEqual(result["balance_sheet"]["cash_and_equivalents"]["value"], 28)
        self.assertEqual(result["balance_sheet"]["cash_and_equivalents"]["date"], "2026-06-30")

    def test_missing_quarter_not_filled_with_zero_or_annual_fact(self):
        self.cell("revenue")["value"] = None
        self.cell("revenue")["status"] = "missing_required_source"
        result = ttm.build_ttm(self.history)
        self.assertEqual(result["period"]["end"], "2026-06-30")
        self.assertIsNone(result["financials"]["revenue"]["value"])
        self.assertFalse(result["ratios"]["net_margin"]["model_usable"])
        self.assertEqual(result["financials"]["net_income"]["value"], 200)

    def test_missing_latest_value_does_not_use_an_older_window(self):
        old = deepcopy(self.history["periods"][0])
        old.update(id="quarterly:2025-06-30", start="2025-04-01", end="2025-06-30", fiscal_quarter=2)
        self.history["periods"].insert(0, old)
        self.history["financials"][old["id"]] = deepcopy(self.history["financials"]["quarterly:2025-09-30"])
        self.cell("revenue")["model_usable"] = False
        result = ttm.build_ttm(self.history)
        self.assertEqual(result["period"]["quarter_ids"][0], "quarterly:2025-09-30")
        self.assertIsNone(result["financials"]["revenue"]["value"])

    def test_gap_overlap_duplicates_and_short_history_fail_window(self):
        cases = []
        gap = deepcopy(self.history); gap["periods"][1]["start"] = "2025-10-02"; cases.append(gap)
        overlap = deepcopy(self.history); overlap["periods"][1]["start"] = "2025-09-30"; cases.append(overlap)
        duplicate = deepcopy(self.history); duplicate["periods"].append(deepcopy(duplicate["periods"][-1])); cases.append(duplicate)
        short = deepcopy(self.history); short["periods"].pop(); cases.append(short)
        for history in cases:
            with self.subTest(issues=ttm.build_ttm(history)["issues"]):
                result = ttm.build_ttm(history)
                self.assertEqual(result["status"], "unavailable")
                self.assertIsNone(result["financials"]["revenue"]["value"])

    def test_fiscal_identity_and_ytd_are_not_quarters(self):
        for alteration in ({"fiscal_year": None}, {"fiscal_quarter": 3},
                           {"flags": ["conflicting_fiscal_year"]}, {"start": "2025-07-01"}):
            history = deepcopy(self.history)
            history["periods"][-1].update(alteration)
            self.assertEqual(ttm.build_ttm(history)["status"], "unavailable")

    def test_definition_basis_units_and_unreviewed_conflicts_block_only_affected_metric(self):
        for alteration in ({"definition_tag": "different_revenue_scope"}, {"unit": "EUR"},
                           {"basis": "non-GAAP"}, {"model_usable": False},
                           {"conflicts": [{"code": "revision"}]}, {"flags": ["revision_requires_review"]}):
            history = deepcopy(self.history)
            history["financials"][history["periods"][-1]["id"]]["revenue"].update(alteration)
            result = ttm.build_ttm(history)
            self.assertIsNone(result["financials"]["revenue"]["value"])
            self.assertEqual(result["financials"]["net_income"]["value"], 200)

    def test_future_source_or_period_cannot_leak_into_snapshot(self):
        self.cell("revenue")["provenance"][0]["filed"] = "2026-08-02"
        result = ttm.build_ttm(self.history)
        self.assertIn("source_after_cutoff", result["financials"]["revenue"]["flags"])
        self.history["as_of"] = "2026-06-29"
        self.assertIn("period_after_cutoff", ttm.build_ttm(self.history)["issues"])

    def test_future_indexed_source_and_missing_evidence_block(self):
        for field in ("future_index", "missing_provenance", "unindexed", "wrong_source_period"):
            history = deepcopy(self.history)
            cell = history["financials"][history["periods"][-1]["id"]]["revenue"]
            if field == "future_index": history["source_index"]["TEST-FILING-4"]["as_of_date"] = "2026-08-02"
            if field == "missing_provenance": cell["provenance"] = []
            if field == "unindexed": del history["source_index"]["TEST-FILING-4"]
            if field == "wrong_source_period": cell["provenance"][0]["start"] = "2026-01-01"
            self.assertIsNone(ttm.build_ttm(history)["financials"]["revenue"]["value"], field)

    def test_wrong_balance_date_is_not_a_latest_quarter_balance(self):
        self.cell("cash_and_equivalents")["provenance"][0]["end"] = "2026-03-31"
        result = ttm.build_ttm(self.history)
        self.assertIsNone(result["balance_sheet"]["cash_and_equivalents"]["value"])
        self.assertIn("balance_date_mismatch", result["balance_sheet"]["cash_and_equivalents"]["flags"])

    def test_nonfinite_and_boolean_values_never_calculated(self):
        for value in (float("nan"), float("inf"), True):
            history = deepcopy(self.history)
            history["financials"][history["periods"][-1]["id"]]["revenue"]["value"] = value
            self.assertIsNone(ttm.build_ttm(history)["financials"]["revenue"]["value"])
        for period in self.history["periods"]:
            self.history["financials"][period["id"]]["revenue"]["value"] = 1e308
        self.assertIn("nonfinite_ttm_sum", ttm.build_ttm(self.history)["financials"]["revenue"]["flags"])

    def test_zero_revenue_blocks_ratios_but_preserves_zero(self):
        for period in self.history["periods"]:
            self.history["financials"][period["id"]]["revenue"]["value"] = 0
            self.history["financials"][period["id"]]["revenue"]["provenance"][0]["source_value"] = 0
        result = ttm.build_ttm(self.history)
        self.assertEqual(result["financials"]["revenue"]["value"], 0)
        self.assertIsNone(result["ratios"]["net_margin"]["value"])

    def test_real_histories_reconcile_latest_year_and_cross_year_window(self):
        root = Path(__file__).resolve().parents[1]
        msft = json.loads((root / "research/financials/MSFT.json").read_text())
        result = ttm.build_ttm(msft)
        end = result["period"]["end"]
        self.assertEqual(result["financials"]["revenue"]["value"], msft["financials"]["annual:" + end]["revenue"]["value"])
        nvda = json.loads((root / "research/financials/NVDA.json").read_text())
        result = ttm.build_ttm(nvda)
        latest = sorted([p for p in nvda["periods"] if p["type"] == "quarterly"], key=lambda p: p["end"])[-4:]
        self.assertEqual(result["period"]["quarter_ids"], [p["id"] for p in latest])
        self.assertEqual(result["financials"]["revenue"]["value"], sum(nvda["financials"][p["id"]]["revenue"]["value"] for p in latest))

    def test_strict_comparison_requires_all_values_and_matching_windows(self):
        a = ttm.build_ttm(self.history)
        b = deepcopy(a); b["ticker"] = "OTHER"
        self.assertEqual(ttm.compare_ttm([a, b], "revenue")["status"], "available")
        b["period"]["end"] = "2026-07-31"
        result = ttm.compare_ttm([a, b], "revenue")
        self.assertEqual(result["ranking"], [])
        self.assertIn("different_ttm_windows", result["issues"])
        b = deepcopy(a); b["ticker"] = "OTHER"; b["financials"]["revenue"]["model_usable"] = False
        self.assertIn("incomplete_comparison", ttm.compare_ttm([a, b], "revenue")["issues"])
        self.assertIn("unsupported_ttm_metric", ttm.compare_ttm([a, b], "eps_diluted")["issues"])

    def test_strict_comparison_requires_reconciled_concepts(self):
        a = ttm.build_ttm(self.history)
        b = deepcopy(a); b["ticker"] = "OTHER"; b["financials"]["revenue"]["definition_tag"] = "other_scope"
        self.assertIn("unreconciled_comparison_definitions", ttm.compare_ttm([a, b], "revenue")["issues"])


if __name__ == "__main__":
    unittest.main()
