"""Behavior and failure-mode tests; all financial examples are fictional fixtures."""
from copy import deepcopy
from datetime import date, timedelta
import io
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))
import stock_brain as kb
import research_pipeline as p
from financial_facts import select_fact
from openai_runner import parse_response
from sector_corpus import sector_records
from evaluate_retrieval import lexical_retrieve, evaluate, validate_cases


class PipelineTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / "repo"
        shutil.copytree(REPO, self.root, ignore=shutil.ignore_patterns(".git", "build", "__pycache__", ".venv", "research",
            "node_modules", "dist", "facts", "sector-facts.json", "unclassified"))
        for folder in (self.root / "sectors").glob("*/companies"):
            shutil.rmtree(folder)
        (self.root / "config/sector_research.json").unlink(missing_ok=True)
        self.today = date.today().isoformat()
        self.company = {"ticker": "SYNTH", "company_name": "Fictional Fixture", "cik": "0000000001", "exchange": "NASDAQ",
                        "sector": "information-technology", "industry": "Test fixture", "tags": [], "domicile_country": "US", "group": "test"}
        p.write_json(self.root / "config/universe.json", {"schema_version": 1, "companies": [self.company]})
        self.source = {"id": "S01", "title": "Fictional evidence", "publisher": "Test fixture", "url": "https://example.invalid/filing",
                       "published_at": self.today, "accessed_at": self.today}
        self.packet = {"schema_version": 1, "ticker": "SYNTH", "as_of": self.today, "sources": [self.source], "gaps": ["Fictional test data only."], "metrics": [], "sections": {}}
        for i, section in enumerate(kb.config(self.root)[1][:-1], 1):
            self.packet["sections"][section["id"]] = {"claims": [{"id": f"C{i:02d}", "kind": "reported", "text": "Fictional supported statement for testing.", "evidence": [{"source_id": "S01", "locator": "Test paragraph"}]}]}
        kb.build(self.root)

    def apply(self):
        return p.apply_packet(self.root, self.packet, apply=True)

    def attestation(self, path):
        packet_path = p.managed_packet_path(self.root, "SYNTH")
        record = {"ticker": "SYNTH", "packet_sha256": p.digest(packet_path.read_bytes()), "draft_sha256": p.digest(path.read_bytes()),
                  "reviewer": "Fictional fixture reviewer", "reviewed_at": self.today, "notes": "Fixture source assertions only; not real research.",
                  "claim_checks": [{"id": c["id"], "result": "supported", "note": "Matched fictional fixture."} for s in self.packet["sections"].values() for c in s.get("claims", [])],
                  "gaps_acknowledged": self.packet["gaps"]}
        review_path = self.root / "build/review.json"
        p.write_json(review_path, record)
        return packet_path, review_path

    def metric(self, name="M01", value=100, start="2025-01-01", end="2025-03-31", currency="USD"):
        return {"id": name, "claim_id": "C09", "name": "Fictional metric", "value": value, "unit": "million", "currency": currency,
                "period_start": start, "period_end": end, "basis": "GAAP", "source_id": "S01", "locator": "Test row"}

    def test_proposal_does_not_modify_canonical_profiles_and_apply_stays_draft(self):
        proposal = p.apply_packet(self.root, self.packet)
        self.assertTrue(proposal.exists())
        self.assertEqual(kb.documents(self.root), [])
        path = self.apply()
        self.assertEqual(kb.split_document(path.read_text())[0]["status"], "draft")
        self.assertTrue(p.managed_packet_path(self.root, "SYNTH").exists())
        self.assertEqual(kb.export_records(self.root), [])

    def test_packet_rejects_missing_sections_invented_sources_and_future_actuals(self):
        invalid = deepcopy(self.packet)
        del invalid["sections"]["business-overview"]
        with self.assertRaises(kb.Invalid):
            p.validate_packet(self.root, invalid)
        invalid = deepcopy(self.packet)
        invalid["sections"]["business-overview"]["claims"][0]["evidence"][0]["source_id"] = "S99"
        with self.assertRaises(kb.Invalid):
            p.validate_packet(self.root, invalid)
        self.packet["metrics"] = [self.metric(start=None, end=(date.today() + timedelta(days=10)).isoformat())]
        with self.assertRaisesRegex(kb.Invalid, "after evidence cutoff"):
            p.validate_packet(self.root, self.packet)
        self.packet["metrics"][0]["kind"] = "management_guidance"
        p.validate_packet(self.root, self.packet)

    def test_review_is_bound_to_exact_draft_packet_and_claim_checks(self):
        path = self.apply()
        packet_path, review_path = self.attestation(path)
        original = path.read_text()
        path.write_text(original + "\n")
        with self.assertRaisesRegex(kb.Invalid, "draft changed"):
            p.review_packet(self.root, packet_path, review_path)
        path.write_text(original)
        p.review_packet(self.root, packet_path, review_path)
        self.assertTrue(kb.export_records(self.root))
        packet_path.write_text(packet_path.read_text() + "\n")
        with self.assertRaisesRegex(kb.Invalid, "changed after review"):
            kb.export_records(self.root)

    def test_update_demotes_reviewed_profile_and_preserves_identity(self):
        path = self.apply()
        old_id = kb.split_document(path.read_text())[0]["company_id"]
        p.review_packet(self.root, *self.attestation(path))
        self.packet["sections"]["business-overview"]["claims"][0]["text"] = "Changed fictional evidence."
        self.apply()
        meta = kb.split_document(path.read_text())[0]
        self.assertEqual(meta["company_id"], old_id)
        self.assertEqual(meta["status"], "draft")
        self.assertEqual(kb.export_records(self.root), [])

    def test_calculations_reject_mixed_periods_currencies_and_zero_bases(self):
        current = self.metric(value=150)
        prior = self.metric("M02", 100, "2024-01-01", "2024-03-31")
        growth = {"id": "M03", "claim_id": "C09", "name": "Growth", "unit": "percent", "currency": None, "basis": "GAAP",
                  "period_start": current["period_start"], "period_end": current["period_end"],
                  "calculation": {"operation": "growth_pct", "inputs": ["M01", "M02"]}}
        self.packet["metrics"] = [current, prior, growth]
        self.assertEqual(p.computed_metrics(self.packet)[-1]["value"], 50)
        for field, value in (("currency", "EUR"), ("value", 0), ("period_end", "2024-12-31")):
            invalid = deepcopy(self.packet)
            invalid["metrics"][1][field] = value
            with self.assertRaises(kb.Invalid):
                p.computed_metrics(invalid)

    def test_exact_xbrl_period_revision_and_conflict_handling(self):
        facts = {"facts": {"us-gaap": {"Revenues": {"units": {"USD": [
            {"start": "2025-01-01", "end": "2025-03-31", "val": 100, "filed": "2025-04-20", "accn": "old", "form": "10-Q"},
            {"start": "2025-01-01", "end": "2025-03-31", "val": 90, "filed": "2025-05-01", "accn": "new", "form": "10-Q/A"},
            {"start": "2025-01-01", "end": "2025-06-30", "val": 250, "filed": "2025-07-20", "accn": "ytd", "form": "10-Q"}]}}}}}
        args = [facts, "us-gaap", "Revenues", "USD", "2025-01-01", "2025-03-31"]
        self.assertEqual(select_fact(*args, "2025-04-30")["value"], 100)
        self.assertEqual(select_fact(*args, self.today)["value"], 90)
        with self.assertRaises(kb.Invalid):
            select_fact(facts, "us-gaap", "Revenues", "USD", "2025-04-01", "2025-06-30", self.today)
        facts["facts"]["us-gaap"]["Revenues"]["units"]["USD"].append({"start": "2025-01-01", "end": "2025-03-31", "val": 95, "filed": "2025-05-01", "accn": "conflict", "form": "10-Q/A"})
        with self.assertRaisesRegex(kb.Invalid, "conflicting"):
            select_fact(*args, self.today)

    def test_filing_selection_retains_amendments_and_honors_cutoff(self):
        rows = [{"form": form, "filingDate": day, "accessionNumber": acc, "reportDate": "2025-12-31"} for form, day, acc in [
            ("10-K", "2026-02-01", "annual"), ("10-K/A", "2026-02-02", "amendment"),
            ("10-Q", "2026-05-01", "later"), ("8-K", "2026-02-03", "event")]]
        selected, gaps = p.select_filings(rows, "2026-02-10", 0)
        self.assertEqual({r["accessionNumber"] for r in selected}, {"annual", "amendment"})
        self.assertTrue(any("sampling limit" in gap for gap in gaps))

    def test_change_detection_noop_targeted_broad_and_failed_downloads(self):
        old = {"sources": [{"url": "https://example.invalid/a", "sha256": "1", "form": "10-K"}]}
        current = deepcopy(old)
        self.assertFalse(p.update_plan(old, current)["requires_review"])
        current["sources"].append({"url": "https://example.invalid/b", "sha256": "2", "form": "8-K", "items": "5.02"})
        self.assertIn("management-and-governance", p.update_plan(old, current)["affected_sections"])
        self.assertNotIn("financial-performance", p.update_plan(old, current)["affected_sections"])
        current["sources"][-1]["form"] = "10-K"
        self.assertEqual(p.update_plan(old, current)["affected_sections"], "all")
        self.assertTrue(p.update_plan(old, {**old, "errors": [{"url": "broken"}]})["requires_review"])

    def test_unapplied_collection_cannot_consume_pending_changes(self):
        source = {"url": self.source["url"], "sha256": "old", "form": "10-K"}
        manifest = {"requested_cutoff": self.today, "errors": [], "sources": [source]}
        location = self.root / "build/research/SYNTH/manifest.json"
        p.write_json(location, manifest)
        self.apply()
        self.assertFalse(p.update_plan(p.applied_source_state(self.root, "SYNTH"), manifest)["requires_review"])
        changed = deepcopy(manifest)
        changed["sources"][0]["sha256"] = "new"
        p.write_json(location, changed)
        for _ in range(2):
            self.assertTrue(p.update_plan(p.applied_source_state(self.root, "SYNTH"), changed)["requires_review"])
        self.apply()
        self.assertFalse(p.update_plan(p.applied_source_state(self.root, "SYNTH"), changed)["requires_review"])
        p.managed_packet_path(self.root, "SYNTH").write_text("{}")
        self.assertEqual(p.applied_source_state(self.root, "SYNTH")["sources"], [])

    def test_recollected_source_ids_preserve_existing_packet_citations(self):
        mapping = p.reconcile_source_ids({"https://example.invalid/extra": "S01", self.source["url"]: "S02"}, self.packet)
        self.assertEqual(mapping[self.source["url"]], "S01")
        self.assertNotEqual(mapping["https://example.invalid/extra"], "S01")

    def test_pdf_text_extraction_rejects_image_only_and_reads_text(self):
        from pypdf import PdfWriter
        from pypdf.generic import DecodedStreamObject, NameObject, DictionaryObject
        writer = PdfWriter()
        page = writer.add_blank_page(400, 400)
        empty = io.BytesIO()
        writer.write(empty)
        with self.assertRaisesRegex(kb.Invalid, "no readable text"):
            p.document_text(empty.getvalue(), "application/pdf")
        font = DictionaryObject({NameObject("/Type"): NameObject("/Font"), NameObject("/Subtype"): NameObject("/Type1"), NameObject("/BaseFont"): NameObject("/Helvetica")})
        page[NameObject("/Resources")] = DictionaryObject({NameObject("/Font"): DictionaryObject({NameObject("/F1"): font})})
        stream = DecodedStreamObject()
        stream.set_data(b"BT /F1 12 Tf 20 200 Td (Fictional source text for extraction test.) Tj ET")
        page[NameObject("/Contents")] = stream
        filled = io.BytesIO()
        writer.write(filled)
        self.assertIn("Fictional source text", p.document_text(filled.getvalue(), "application/pdf"))

    def test_retrieval_coverage_guards_allow_evidenced_relationships_and_acronyms(self):
        records = [{"id": "one", "document_type": "company", "ticker": "SYNTH", "text": "Fictional Fixture has a program acronym ABC and a supplier relationship with DRAFT."}]
        universe = [self.company, {"ticker": "DRAFT", "company_name": "Unreviewed Example"}]
        self.assertFalse(lexical_retrieve("What is SYNTH's ABC program?", records, universe)["abstain"])
        self.assertFalse(lexical_retrieve("What is SYNTH's relationship with DRAFT?", records, universe)["abstain"])
        for question in ("Compare SYNTH versus DRAFT revenue", "What is DRAFT revenue?", "What is UNKNOWN revenue?", "What is SYNTH's stock price today?"):
            self.assertTrue(lexical_retrieve(question, records, universe)["abstain"], question)

    def test_evaluation_rejects_missing_gold_and_invented_chunk_ids(self):
        records = [{"id": "one", "document_id": "fiction", "section_id": "business", "sources": [self.source]}]
        cases = [{"id": "Q1", "question": "Fiction?", "expected_answer": "Fixture", "expected_behavior": "answer", "evidence": [{"document_id": "fiction", "section_id": "business", "source_ids": ["S01"]}]}]
        validate_cases(cases, records)
        self.assertEqual(evaluate(cases, {"Q1": {"chunk_ids": ["one"]}}, records)["mean_evidence_recall"], 1)
        with self.assertRaisesRegex(kb.Invalid, "unknown"):
            evaluate(cases, {"Q1": {"chunk_ids": ["invented"]}}, records)
        cases[0]["evidence"][0]["source_ids"] = ["S99"]
        with self.assertRaisesRegex(kb.Invalid, "gold evidence"):
            validate_cases(cases, records)

    def test_cache_reuses_bytes_and_detects_corruption(self):
        class Response(io.BytesIO):
            url = "https://example.invalid/a"
            headers = {"Content-Type": "text/html"}
        fetcher = p.Fetcher(self.root, "Test fixture")
        with patch("urllib.request.urlopen", return_value=Response(b"<p>fixture</p>")) as opener:
            raw, info = fetcher.fetch("https://example.invalid/a")
            self.assertEqual(fetcher.fetch("https://example.invalid/a")[0], raw)
            self.assertEqual(opener.call_count, 1)
        (fetcher.cache / "objects" / info["sha256"]).write_bytes(b"corrupt")
        with self.assertRaisesRegex(kb.Invalid, "checksum"):
            fetcher.fetch("https://example.invalid/a")

    def test_html_parser_excludes_hidden_xbrl_but_preserves_table_boundaries(self):
        raw = b'<html><ix:header>secret metadata</ix:header><script>bad()</script><table><tr><td>Revenue</td><td>123</td></tr></table></html>'
        text = p.document_text(raw, "text/html")
        self.assertIn("Revenue | 123", text)
        self.assertNotIn("metadata", text)
        self.assertNotIn("bad()", text)

    def test_runner_validates_sources_and_preserves_draft(self):
        program = self.root / "build/runner.py"
        program.parent.mkdir(parents=True)
        program.write_text("import json,sys\nrequest=json.load(sys.stdin)\nprint(json.dumps(request['fixture_response']))\n")
        config = self.root / "build/runner.json"
        p.write_json(config, {"argv": [sys.executable, str(program)], "usd_per_million_tokens": {"input": 2, "output": 4}})
        request = {"company": self.company, "cutoff": self.today, "documents": [{"source": self.source}],
                   "fixture_response": {"packet": self.packet, "usage": {"input_tokens": 100, "output_tokens": 50}}}
        packet, metrics = p.run_model(self.root, request, config)
        self.assertAlmostEqual(metrics["estimated_cost_usd"], .0004)
        self.assertEqual(kb.documents(self.root), [])
        request["fixture_response"]["packet"] = deepcopy(self.packet)
        request["fixture_response"]["packet"]["sources"][0]["url"] = "https://example.invalid/invented"
        with self.assertRaisesRegex(kb.Invalid, "invented"):
            p.run_model(self.root, request, config)

    def test_api_runner_rejects_partial_or_refused_output(self):
        with self.assertRaises(ValueError):
            parse_response({"status": "incomplete", "output": []})
        with self.assertRaises(ValueError):
            parse_response({"status": "completed", "output": [{"content": [{"type": "refusal"}]}]})
        result = parse_response({"status": "completed", "output": [{"content": [{"type": "output_text", "text": "{}"}]}], "usage": {"input_tokens": 7, "output_tokens": 2}})
        self.assertEqual(result["usage"]["input_tokens"], 7)

    def test_sector_export_requires_review_and_exact_content_hash(self):
        guide = self.root / "sectors/information-technology/README.md"
        titles = __import__("re").findall(r"^## (.+)$", (self.root / "templates/sector/README.md").read_text(), flags=__import__("re").M)
        guide.write_text("# Information Technology\n\n" + "\n".join(f"## {title}\n\nFictional sector evidence. [S01]\n" for title in titles))
        entry = {"sector": "information-technology", "status": "draft", "as_of": self.today, "reviewed_at": self.today,
                 "updated_at": self.today, "sources": [self.source], "content_sha256": p.digest(guide.read_bytes())}
        registry = self.root / "config/sector_research.json"
        p.write_json(registry, {"schema_version": 1, "sectors": [entry]})
        self.assertEqual(sector_records(self.root), [])
        entry["status"] = "reviewed"
        p.write_json(registry, {"schema_version": 1, "sectors": [entry]})
        records = sector_records(self.root)
        self.assertEqual({r["document_type"] for r in records}, {"sector"})
        self.assertNotIn("company-index", {r["section_id"] for r in records})
        guide.write_text(guide.read_text() + "\nChanged")
        with self.assertRaisesRegex(kb.Invalid, "changed after review"):
            sector_records(self.root)


if __name__ == "__main__":
    unittest.main()
