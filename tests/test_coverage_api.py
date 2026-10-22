"""Coverage reads stay bounded and never turn collected data into a review."""
from copy import deepcopy
import json
from pathlib import Path
import sqlite3
import sys
import tempfile
import unittest
from unittest.mock import patch
from urllib.parse import urlencode

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import coverage_api as api


CIK = "0000789019"


def company_fixture():
    return {"cik": CIK, "company_id": "company-cik-" + CIK, "ticker": "MSFT",
            "company_name": "Microsoft Corporation", "exchange": "Nasdaq", "status": "listed",
            "listings": [{"ticker": "MSFT", "exchange": "Nasdaq", "status": "listed"}],
            "metadata": {"reviewed": True}, "payloads": {}}


class MemoryStore:
    def __init__(self, company=None, payloads=None):
        self.record = deepcopy(company or company_fixture())
        self.payloads = deepcopy(payloads or {})
        self.calls = []
        for kind in self.payloads:
            self.record["payloads"][kind] = {"version": 1, "sha256": "a" * 64,
                                             "stored_at": "2026-10-22T00:00:00+00:00", "source": None}

    def list_companies(self, query="", limit=50, offset=0):
        self.calls.append(("list", query, limit, offset))
        return {"items": [self.record] if offset == 0 else [], "total": 1, "limit": limit, "offset": offset}

    def company(self, identifier):
        self.calls.append(("company", identifier))
        tickers = {self.record["ticker"], *(listing["ticker"] for listing in self.record["listings"])}
        return self.record if identifier == self.record["cik"] or identifier in tickers else None

    def get_payload(self, cik, kind):
        self.calls.append(("payload", cik, kind))
        return self.payloads.get(kind)

    def stats(self):
        self.calls.append(("stats",))
        return {"schema_version": 1, "issuers": 1, "listings": 1, "payloads": len(self.payloads)}


class CoverageAPITests(unittest.TestCase):
    def setUp(self):
        self.store = MemoryStore()

    def detail(self, store=None, identifier="msft"):
        status, payload = api.serve_coverage(store or self.store, "/api/companies/" + identifier)
        self.assertEqual(status, "200 OK")
        return payload

    def history(self):
        return json.loads((ROOT / "research/financials/MSFT.json").read_text())

    def reviewed(self):
        return {"ticker": "MSFT", "as_of": "2026-01-01", "review_type": "ai",
                "sections": {"business": [{"text": "Existing dated research", "source_ids": ["SOURCE"]}]},
                "sources": [{"source_id": "SOURCE", "url": "https://example.test/source"}]}

    def test_unrelated_routes_do_not_access_store(self):
        for path in ("/", "/api/snapshot", "/api/state", "/api/companies-other", "/api/coverage/jobs"):
            self.assertIsNone(api.serve_coverage(self.store, path))
        self.assertEqual(self.store.calls, [])
        self.assertEqual(api.serve_coverage(None, "/api/coverage")[0], "503 Service Unavailable")

    def test_pagination_bounds_duplicates_and_query_decoding(self):
        invalid = ("limit=0", "limit=101", "limit=-1", "limit=1.0", "limit=", "limit=+1",
                   "limit=1000000000000000000", "offset=-1", "offset=1000001", "offset=1e2",
                   "limit=1&limit=2", "q=a&q=b", "unexpected=yes", "q=%FF", "q=%", "q=%00",
                   "q=%0A", "q=" + "a" * 201, "q=" + "a" * 4096)
        for query in invalid:
            with self.subTest(query=query[:80]):
                status, result = api.serve_coverage(self.store, "/api/companies", query)
                self.assertEqual(status, "400 Bad Request")
                self.assertEqual(result["error"], "invalid_query")
        self.assertEqual(self.store.calls, [])
        status, page = api.serve_coverage(self.store, "/api/companies", "q=Microsoft+Corporation&limit=100&offset=1000000")
        self.assertEqual(status, "200 OK")
        self.assertEqual((page["limit"], page["offset"]), (100, 1_000_000))
        self.assertEqual(self.store.calls, [("list", "Microsoft Corporation", 100, 1_000_000)])

    def test_list_only_returns_registry_and_payload_metadata(self):
        self.store.record.update(history={"huge": True}, canonical_reviewed=True)
        self.store.record["payloads"]["history"] = {"version": 1, "payload": {"financials": "not a list field"}}
        self.store.record["payloads"]["reviewed_research"] = {"version": 1}
        status, result = api.serve_coverage(self.store, "/api/companies")
        self.assertEqual(status, "200 OK")
        self.assertEqual(self.store.calls, [("list", "", 50, 0)])
        item = result["items"][0]
        self.assertEqual(item["collection_status"], "data-collected")
        self.assertTrue(item["has_reviewed_research"])
        for key in ("history", "metadata", "canonical_reviewed", "research"):
            self.assertNotIn(key, item)
        self.assertNotIn("payload", item["payloads"]["history"])

    def test_detail_uses_stable_padded_cik_after_case_insensitive_lookup(self):
        for identifier in ("msft", "MSFT", "789019", CIK):
            self.store.calls.clear()
            detail = self.detail(identifier=identifier)
            self.assertEqual(detail["company"]["cik"], CIK)
            self.assertEqual(self.store.calls[1:], [("payload", CIK, kind) for kind in api.PAYLOAD_KINDS]
                             + [("company", CIK)])
        self.store.record["listings"].append({"ticker": "MSFT.A", "exchange": "Nasdaq", "status": "listed"})
        self.assertEqual(self.detail(identifier="msft%2Ea")["company"]["cik"], CIK)
        self.store.record["listings"].append({"ticker": "MSFT/PR", "exchange": "Nasdaq", "status": "listed"})
        self.assertEqual(self.detail(identifier="msft%2Fpr")["company"]["cik"], CIK)

    def test_invalid_unknown_and_ambiguous_identifiers_do_not_guess(self):
        for identifier in ("", "0", "0000000000", "10000000000", "MSFT/extra", "../MSFT", "%2FMSFT",
                           "MSFT%00", "MSFT%FF", "%", "A" * 33, "' OR 1=1", "UNKNOWN"):
            status, result = api.serve_coverage(self.store, "/api/companies/" + identifier)
            self.assertEqual(status, "404 Not Found", identifier)
            self.assertEqual(result, {"error": "company_not_found"})
        with patch.object(self.store, "company", side_effect=ValueError("ambiguous")):
            self.assertEqual(api.serve_coverage(self.store, "/api/companies/MSFT")[0], "409 Conflict")

    def test_registry_and_collection_flags_cannot_create_a_research_review(self):
        detail = self.detail()
        self.assertEqual(detail["collection_status"], "registry-only")
        self.assertFalse(detail["research"]["canonical_reviewed"])
        self.assertEqual(detail["collected"], {kind: None for kind in api.PAYLOAD_KINDS[:3]})
        self.assertIsNone(detail["ttm"])
        changes = {"cik": CIK, "classification": "data_collected", "review_status": "reviewed",
                   "canonical_reviewed": True, "qa": {"open_flag_count": 0}, "changes": []}
        detail = self.detail(MemoryStore(payloads={"automatic_changes": changes}))
        self.assertEqual(detail["collection_status"], "data-collected")
        self.assertEqual(detail["research"]["status"], "not-available")
        self.assertFalse(detail["research"]["canonical_reviewed"])

    def test_one_validated_history_has_ttm_without_promoting_narrative(self):
        history = self.history()
        store = MemoryStore(payloads={"history": history})
        original = deepcopy(store.payloads)
        detail = self.detail(store)
        self.assertTrue(detail["financials_validated"])
        self.assertIsNotNone(detail["ttm"]["period"])
        self.assertGreater(detail["ttm"]["financials"]["revenue"]["value"], 0)
        self.assertFalse(detail["research"]["canonical_reviewed"])
        self.assertNotIn("eps_diluted", detail["ttm"]["financials"])
        self.assertEqual(store.payloads, original)
        detail["collected"]["history"]["as_of"] = "2000-01-01"
        self.assertEqual(store.payloads, original)

    def test_invalid_history_never_becomes_displayed_facts_or_ttm(self):
        for alteration in ("wrong_issuer", "duplicate_period", "invalid_value", "future_source"):
            history = self.history()
            latest = max((p for p in history["periods"] if p["type"] == "quarterly"), key=lambda p: p["end"])
            cell = history["financials"][latest["id"]]["revenue"]
            if alteration == "wrong_issuer": history["cik"] = "0000000001"
            if alteration == "duplicate_period": history["periods"].append(deepcopy(latest))
            if alteration == "invalid_value": cell["value"] += 1
            if alteration == "future_source": cell["provenance"][0]["filed"] = "9999-01-01"
            with self.subTest(alteration=alteration):
                detail = self.detail(MemoryStore(payloads={"history": history}))
                self.assertFalse(detail["financials_validated"])
                self.assertIsNone(detail["collected"]["history"])
                self.assertIsNone(detail["ttm"])
                self.assertEqual(detail["collection_status"], "review-required")
                self.assertFalse(detail["research"]["canonical_reviewed"])

    def test_blocked_metric_is_not_raised_to_usable_by_detail(self):
        history = self.history()
        latest = max((p for p in history["periods"] if p["type"] == "quarterly"), key=lambda p: p["end"])
        history["financials"][latest["id"]]["revenue"]["model_usable"] = False
        detail = self.detail(MemoryStore(payloads={"history": history}))
        self.assertTrue(detail["financials_validated"])
        self.assertFalse(detail["ttm"]["financials"]["revenue"]["model_usable"])
        self.assertIsNone(detail["ttm"]["financials"]["revenue"]["value"])

    def test_concurrent_payload_commit_never_mixes_versions_in_detail(self):
        store = MemoryStore(payloads={"history": self.history()})
        original_get = store.get_payload
        def changed(cik, kind):
            value = original_get(cik, kind)
            if kind == "submissions":
                store.record["payloads"]["history"]["version"] = 2
            return value
        with patch.object(store, "get_payload", side_effect=changed), \
                patch.object(api.ttm, "build_ttm", side_effect=AssertionError("mixed versions must not calculate")):
            self.assertEqual(api.serve_coverage(store, "/api/companies/msft"),
                             ("503 Service Unavailable", {"error": "company_data_changed", "retryable": True}))

    def test_review_record_stays_dated_and_separate_from_collection_quality(self):
        changes = {"cik": CIK, "classification": "quality_review_required", "qa": {"open_flag_count": 1}, "changes": []}
        detail = self.detail(MemoryStore(payloads={"reviewed_research": self.reviewed(), "automatic_changes": changes}))
        self.assertEqual(detail["collection_status"], "review-required")
        self.assertTrue(detail["research"]["canonical_reviewed"])
        self.assertEqual(detail["research"]["review_type"], "ai")
        self.assertEqual(detail["research"]["as_of"], "2026-01-01")
        self.assertIsNone(detail["ttm"])
        self.assertEqual(detail["collected"]["automatic_changes"], changes)

    def test_invalid_or_explicitly_unreviewed_research_is_not_promoted(self):
        for change in ({"ticker": "OTHER"}, {"cik": "0000000001"}, {"review_type": "automatic"},
                       {"review_status": "unreviewed"}, {"canonical_reviewed": False},
                       {"as_of": "2026-99-99"}, {"sources": []}, {"sections": {}}):
            detail = self.detail(MemoryStore(payloads={"reviewed_research": {**self.reviewed(), **change}}))
            self.assertFalse(detail["research"]["canonical_reviewed"])
            self.assertEqual(detail["research"]["status"], "review-required")
            self.assertIsNone(detail["research"]["payload"])

    def test_stats_are_metadata_only_and_store_errors_do_not_leak_sql(self):
        status, result = api.serve_coverage(self.store, "/api/coverage")
        self.assertEqual(status, "200 OK")
        self.assertEqual(result["issuers"], 1)
        self.assertEqual(self.store.calls, [("stats",)])
        self.assertEqual(api.serve_coverage(self.store, "/api/coverage", "q=MSFT")[0], "400 Bad Request")
        with patch.object(self.store, "list_companies", side_effect=sqlite3.DatabaseError("private SQL and path")):
            self.assertEqual(api.serve_coverage(self.store, "/api/companies"),
                             ("503 Service Unavailable", {"error": "coverage_unavailable"}))


class CoveragePaginationTests(unittest.TestCase):
    """A local scale fixture checks bounded work and output, not production load."""

    @classmethod
    def setUpClass(cls):
        from coverage_store import CoverageStore
        cls.temporary = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.temporary.cleanup)
        cls.store = CoverageStore(Path(cls.temporary.name) / "coverage.sqlite3")
        cls.store.seed_companies([
            {"cik": number, "ticker": "T" + str(number).zfill(5),
             "company_name": "Issuer " + str(number).zfill(5), "exchange": "Nasdaq"}
            for number in range(1, 50_001)
        ])
        # A large per-company payload makes an accidental list payload read
        # observable without requiring a network or a fragile wall-clock gate.
        cls.store.put_payload("1", "submissions", {"cik": "0000000001", "large": "x" * 500_000})

    def test_fifty_thousand_registry_rows_page_without_reading_payload_bodies(self):
        with patch.object(self.store, "get_payload", side_effect=AssertionError("list must not load payloads")), \
                patch.object(self.store, "list_companies", wraps=self.store.list_companies) as listing:
            for offset in (0, 100, 49_900, 50_000):
                status, page = api.serve_coverage(self.store, "/api/companies", f"limit=100&offset={offset}")
                self.assertEqual(status, "200 OK")
                self.assertEqual(page["total"], 50_000)
                self.assertEqual(len(page["items"]), 100 if offset < 50_000 else 0)
                self.assertLess(len(json.dumps(page)), 150_000)
                self.assertEqual([item["cik"] for item in page["items"]],
                                 [str(n).zfill(10) for n in range(offset + 1, min(offset + 101, 50_001))])
            self.assertEqual(listing.call_count, 4)
            self.assertTrue(all(call.kwargs["limit"] == 100 for call in listing.call_args_list))

    def test_parameterized_literal_search_and_case_insensitive_cik_lookup(self):
        for query in ("' OR 1=1 --", "%", "_", "T00001'; DROP TABLE issuers;--"):
            status, page = api.serve_coverage(self.store, "/api/companies", urlencode({"q": query}))
            self.assertEqual(status, "200 OK")
            self.assertEqual(page["total"], 0)
            self.assertEqual(page["items"], [])
        status, detail = api.serve_coverage(self.store, "/api/companies/t00001")
        self.assertEqual(status, "200 OK")
        self.assertEqual(detail["company"]["cik"], "0000000001")
        self.assertFalse(detail["research"]["canonical_reviewed"])
        status, detail = api.serve_coverage(self.store, "/api/companies/1")
        self.assertEqual(status, "200 OK")
        self.assertEqual(detail["company"]["company_id"], "company-cik-0000000001")
        self.assertEqual(api.serve_coverage(self.store, "/api/coverage")[1]["issuers"], 50_000)


if __name__ == "__main__":
    unittest.main()
