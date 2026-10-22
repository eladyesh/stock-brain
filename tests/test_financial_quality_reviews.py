"""Exact filing evidence survives restoration without approving unseen facts."""
import copy
import unittest

from test_financial_history import CIK, COMPANY, REVENUE, facts, row, split_review, year
import financial_history as fh
import financial_answers


def scope_review(history, metric):
    cell = fh.get_metric(history, metric)
    evidence = {"source_id": "ISSUER-REPORT", "title": "Synthetic issuer report",
                "url": "https://issuer.example/annual.pdf", "filed": "2025-08-01", "sha256": "a" * 64}
    return {"review_id": "TEST-SCOPE-1", "type": "filing_scope", "cik": CIK,
            "effective_date": "2025-08-01", "evidence": [evidence],
            "observations": [{**source, "metric": metric, "decimals": -6,
                "scope": fh.SCOPE_BY_METRIC.get(metric, "carrying_value_excluding_finance_leases"),
                "rationale": "Synthetic table explicitly verifies this exact metric and scope.",
                "source_document": {"url": evidence["url"], "sha256": evidence["sha256"], "locator": "Note 2"}}
                for source in cell["provenance"]]}


def share_history(value=100, accession="0000000001-25-000001"):
    return fh.normalize_companyfacts(facts({REVENUE: [year()],
        "WeightedAverageNumberOfDilutedSharesOutstanding": {"shares": [year(value, accn=accession)]}}),
        COMPANY, "2025-09-01", {"fetched_at": "2025-09-01T00:00:00Z", "sha256": "b" * 64})


class FilingScopeReviewTests(unittest.TestCase):
    def test_restore_applies_exact_review_and_preserves_observations_and_fetch_metadata(self):
        saved = share_history()
        review = scope_review(saved, "shares_diluted")
        result = fh.apply_normalization_reviews(saved, [review])
        self.assertFalse(fh.get_metric(saved, "shares_diluted")["model_usable"])
        cell = fh.get_metric(result, "shares_diluted")
        self.assertTrue(cell["model_usable"])
        self.assertEqual(cell["provenance"], fh.get_metric(saved, "shares_diluted")["provenance"])
        self.assertEqual(result["source"], saved["source"])
        self.assertEqual(result, fh.apply_normalization_reviews(result, [review]))
        self.assertEqual(result["coverage"]["filing_scope_verified_cells"], 1)

    def test_numeric_or_accession_change_is_not_approved_by_old_review(self):
        review = scope_review(share_history(), "shares_diluted")
        for saved in [share_history(101), share_history(accession="0000000001-25-000002")]:
            result = fh.apply_normalization_reviews(saved, [review])
            self.assertFalse(fh.get_metric(result, "shares_diluted")["model_usable"])
            self.assertNotIn("scope_review", fh.get_metric(result, "shares_diluted"))

    def test_future_evidence_is_not_applied_and_ids_cannot_be_rewritten(self):
        saved = share_history()
        review = scope_review(saved, "shares_diluted")
        future = copy.deepcopy(review)
        future["evidence"][0]["filed"] = "2026-01-01"
        self.assertFalse(fh.get_metric(fh.apply_normalization_reviews(saved, [future]), "shares_diluted")["model_usable"])
        reviewed = fh.apply_normalization_reviews(saved, [review])
        changed = copy.deepcopy(review)
        changed["observations"][0]["rationale"] = "Different review"
        with self.assertRaisesRegex(ValueError, "conflicting contents"):
            fh.apply_normalization_reviews(reviewed, [changed])

    def test_share_scope_cannot_waive_other_conflicts(self):
        first = year(100)
        revised = year(101, filed="2025-08-15", accn="0000000001-25-000003")
        saved = fh.normalize_companyfacts(facts({REVENUE: [year()],
            "WeightedAverageNumberOfDilutedSharesOutstanding": {"shares": [first, revised]}}), COMPANY, "2025-09-01")
        result = fh.apply_normalization_reviews(saved, [scope_review(saved, "shares_diluted")])
        self.assertFalse(fh.get_metric(result, "shares_diluted")["model_usable"])
        self.assertTrue(fh.get_metric(result, "shares_diluted")["conflicts"])
        self.assertTrue(any(f["code"] == "source_value_revision_or_conflict" for f in result["qa_flags"]))

    def test_scope_review_tampering_and_bare_flag_removal_fail_validation(self):
        saved = share_history()
        reviewed = fh.apply_normalization_reviews(saved, [scope_review(saved, "shares_diluted")])
        for mutation in ["scope", "source", "binding"]:
            bad = copy.deepcopy(reviewed)
            cell = bad["financials"][bad["periods"][0]["id"]]["shares_diluted"]
            if mutation == "scope":
                cell["scope_review"]["scope"] = "period_end_common_shares_outstanding"
            elif mutation == "source":
                bad["source_index"]["ISSUER-REPORT"]["sha256"] = "b" * 64
            else:
                del cell["scope_review"]
            with self.assertRaises(ValueError):
                fh.validate_history(bad)

    def test_reviewed_long_term_debt_does_not_fill_missing_total_or_short_term(self):
        debt = year(300)
        debt.pop("start")
        saved = fh.normalize_companyfacts(facts({REVENUE: [year()], "LongTermDebt": [debt]}), COMPANY, "2025-09-01")
        result = fh.apply_normalization_reviews(saved, [scope_review(saved, "long_term_debt_total")])
        self.assertTrue(fh.get_metric(result, "long_term_debt_total")["model_usable"])
        self.assertIsNone(fh.get_metric(result, "debt_total")["value"])
        self.assertIsNone(fh.get_metric(result, "short_term_borrowings")["value"])

    def test_answer_includes_issuer_evidence_and_explicit_lease_scope(self):
        debt = year(300)
        debt.pop("start")
        saved = fh.normalize_companyfacts(facts({REVENUE: [year()], "DebtAndCapitalLeaseObligations": [debt]}),
                                         COMPANY, "2025-09-01", {"fetched_at": "2025-09-01T00:00:00Z"})
        review = scope_review(saved, "debt_total")
        review["observations"][0]["scope"] = "carrying_value_including_finance_leases"
        reviewed = fh.apply_normalization_reviews(saved, [review])
        result = next(r for r in financial_answers.index(reviewed) if r["metric"] == "debt_total")
        self.assertIn("including finance leases", result["text"])
        self.assertIn("כולל חכירות מימוניות", result["text_he"])
        self.assertIn("ISSUER-REPORT", {s["id"] for s in result["sources"]})
        self.assertEqual(result["reviewed_scope"], "carrying_value_including_finance_leases")

    def test_outstanding_share_split_requires_both_original_observations(self):
        old = year(2464_000_000)
        old.pop("start")
        later = dict(old, val=24643_000_000, filed="2026-02-01", accn="0000000001-26-000001")
        data = facts({REVENUE: [year()], "CommonStockSharesOutstanding": {"shares": [old, later]}})
        review = split_review("shares_outstanding", [old, later])
        result = fh.normalize_companyfacts(data, COMPANY, "2026-02-02", normalization_reviews=[review])
        cell = fh.get_metric(result, "shares_outstanding")
        self.assertEqual(cell["value"], 24643_000_000)
        self.assertTrue(cell["model_usable"])
        self.assertEqual(len(cell["resolved_conflicts"]), 1)
        review["observations"] = review["observations"][1:]
        result = fh.normalize_companyfacts(data, COMPANY, "2026-02-02", normalization_reviews=[review])
        self.assertFalse(fh.get_metric(result, "shares_outstanding")["model_usable"])


if __name__ == "__main__":
    unittest.main()
