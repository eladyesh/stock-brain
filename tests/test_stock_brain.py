"""Behavior tests use fictional companies in isolated temporary repositories."""

from datetime import date, timedelta
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

import yaml


REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))
spec = importlib.util.spec_from_file_location("stock_brain", REPO / "scripts/stock_brain.py")
brain = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = brain
spec.loader.exec_module(brain)


class KnowledgeBaseTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "brain"
        shutil.copytree(REPO, self.root, ignore=shutil.ignore_patterns(
            ".git", "build", "__pycache__", ".venv"))
        # Tests remain isolated if real profiles are added to the repository later.
        for folder in (self.root / "sectors").glob("*/companies"):
            shutil.rmtree(folder)
        (self.root / "config/sector_research.json").unlink(missing_ok=True)
        brain.build(self.root)

    def add(self, ticker="SYNTH", sector="information-technology"):
        return brain.add(self.root, ticker, "Synthetic Test Company", sector, "NASDAQ", "common_stock")

    def edit(self, path, change):
        metadata, body = brain.split_document(path.read_text())
        metadata, body = change(metadata, body)
        path.write_text("---\n" + yaml.safe_dump(metadata, sort_keys=False) + "---\n" + body)

    def reviewed(self, ticker="SYNTH"):
        path = self.add(ticker)

        def update(metadata, body):
            today = date.today().isoformat()
            metadata.update(status="reviewed", as_of=today, reviewed_at=today,
                            tags=["test-theme"], ticker_aliases=[ticker + ".A"])
            metadata["sources"] = [{
                "id": "S01", "title": "Synthetic test evidence; not real research",
                "publisher": "Test fixture", "url": "https://example.invalid/test-evidence",
                "published_at": today, "accessed_at": today,
            }]
            _, definitions = brain.config(self.root)
            body = body.split("## ", 1)[0]
            for entry in definitions:
                body += f"## {entry['title']}\n\nFictional test-only content for {entry['id']}. [S01]\n\n"
            return metadata, body

        self.edit(path, update)
        return path

    def test_empty_corpus_and_all_sector_indexes(self):
        self.assertEqual(brain.build(self.root, check=True), 0)
        self.assertEqual(len(list((self.root / "sectors").glob("*/INDEX.md"))), 11)
        self.assertEqual(brain.export_records(self.root), [])
        self.assertEqual(json.loads((self.root / "data/catalog.json").read_text())["companies"], [])

    def test_add_updates_all_indexes_and_remains_unresearched(self):
        path = self.add("synth")
        self.assertEqual(path.parent.name, "SYNTH")
        self.assertEqual(brain.build(self.root, check=True), 1)
        self.assertEqual(len(brain.documents(self.root)[0].sections), 18)
        for index in ("INDEX.md", "sectors/information-technology/INDEX.md"):
            self.assertIn("[SYNTH]", (self.root / index).read_text())
            self.assertIn("stub", (self.root / index).read_text())
        self.assertEqual(brain.export_records(self.root), [])

    def test_duplicate_symbol_or_alias_cannot_create_a_second_profile(self):
        self.reviewed()
        for ticker in ("SYNTH", "SYNTH.A"):
            with self.subTest(ticker=ticker), self.assertRaises(brain.Invalid):
                self.add(ticker, "energy")
        self.assertFalse((self.root / "sectors/energy/companies").exists())

    def test_path_traversal_is_rejected_before_writing(self):
        for ticker, sector in (("../../ESCAPE", "energy"), ("ESCAPE", "../../outside")):
            with self.subTest(ticker=ticker), self.assertRaises(brain.Invalid):
                self.add(ticker, sector)
        self.assertEqual(brain.documents(self.root), [])

    def test_duplicate_ids_and_ciks_fail(self):
        first, second = self.add("AAA"), self.add("BBB")
        original, _ = brain.split_document(first.read_text())
        self.edit(second, lambda m, b: ({**m, "company_id": original["company_id"]}, b))
        with self.assertRaisesRegex(brain.Invalid, "duplicate company_id"):
            brain.documents(self.root)
        self.edit(second, lambda m, b: ({**m, "company_id": "another-id", "cik": "0000000001"}, b))
        self.edit(first, lambda m, b: ({**m, "cik": "0000000001"}, b))
        with self.assertRaisesRegex(brain.Invalid, "duplicate CIK"):
            brain.documents(self.root)

    def test_yaml_duplicate_keys_and_unsafe_tags_fail(self):
        for text in ("---\nticker: AAA\nticker: BBB\n---\n", "---\nx: !!python/object:example {}\n---\n"):
            with self.subTest(text=text), self.assertRaises(brain.Invalid):
                brain.split_document(text)

    def test_bad_metadata_and_invalid_dates_fail(self):
        path = self.add()
        original = path.read_text()
        cases = {"ticker_aliases": "AAA", "tags": ["AI"], "cik": 123,
                 "status": ["reviewed"], "schema_version": True,
                 "updated_at": "2026-02-30", "as_of": (date.today() + timedelta(days=1)).isoformat()}
        for key, value in cases.items():
            with self.subTest(key=key):
                path.write_text(original)
                self.edit(path, lambda m, b: ({**m, key: value}, b))
                with self.assertRaises(brain.Invalid):
                    brain.documents(self.root)

    def test_unregistered_citations_fail_even_in_drafts(self):
        path = self.add()
        self.edit(path, lambda m, b: (m, b + "\nUnsupported statement. [S99]\n"))
        with self.assertRaisesRegex(brain.Invalid, "unregistered"):
            brain.documents(self.root)

    def test_reviewed_profile_requires_evidence_and_completed_sections(self):
        path = self.add()
        today = date.today().isoformat()
        self.edit(path, lambda m, b: ({**m, "status": "reviewed", "as_of": today, "reviewed_at": today}, b))
        with self.assertRaisesRegex(brain.Invalid, "require sources"):
            brain.documents(self.root)
        path.unlink()
        path = self.reviewed()
        self.edit(path, lambda m, b: (m, b + "\nTODO: Finish verification.\n"))
        with self.assertRaisesRegex(brain.Invalid, "placeholders"):
            brain.documents(self.root)

    def test_export_context_provenance_and_change_hash(self):
        path = self.reviewed()
        self.add("DRAFT")
        before = brain.export_records(self.root)
        self.assertEqual(len(before), 17)
        self.assertEqual(before, brain.export_records(self.root))
        for row in before:
            self.assertEqual(row["ticker"], "SYNTH")
            self.assertIn("Synthetic Test Company (SYNTH)", row["text"])
            self.assertEqual(row["sources"][0]["id"], "S01")
            self.assertTrue(row["source_path"].endswith("SYNTH/README.md"))
            self.assertEqual(len(row["content_sha256"]), 64)
        self.edit(path, lambda m, b: ({**m, "tags": ["changed-theme"]}, b))
        after = brain.export_records(self.root)
        self.assertEqual([r["id"] for r in before], [r["id"] for r in after])
        self.assertNotEqual(before[0]["content_sha256"], after[0]["content_sha256"])

    def test_archived_and_unavailable_content_are_removed_from_export(self):
        path = self.reviewed()
        self.edit(path, lambda m, b: (m, b.replace(
            "Fictional test-only content for competitive-landscape. [S01]",
            "Not available: No reliable competitor evidence was found.")))
        self.assertEqual(len(brain.export_records(self.root)), 16)
        self.edit(path, lambda m, b: ({**m, "status": "archived"}, b))
        self.assertEqual(brain.export_records(self.root), [])

    def test_stale_indexes_are_detected_and_rebuilt(self):
        path = self.add()
        self.edit(path, lambda m, b: ({**m, "tags": ["test-theme"]}, b))
        with self.assertRaisesRegex(brain.Invalid, "stale"):
            brain.build(self.root, check=True)
        brain.build(self.root)
        self.assertEqual(brain.build(self.root, check=True), 1)
        self.assertIn("**test-theme**", (self.root / "INDEX.md").read_text())

    def test_missing_sector_guide_is_not_silently_accepted(self):
        (self.root / "sectors/energy/README.md").unlink()
        with self.assertRaisesRegex(brain.Invalid, "missing sector guide"):
            brain.build(self.root)

    def test_heading_inside_code_fence_does_not_create_a_section(self):
        path = self.add()
        self.edit(path, lambda m, b: (m, b + "\n```text\n## Not a section\n```\n"))
        self.assertEqual(len(brain.documents(self.root)[0].sections), 18)

    def test_long_tables_keep_headers_rows_and_citation(self):
        header = "| Metric | Value |\n| --- | --- |"
        rows = [f"| Unique row {i:03d} | Synthetic value {i:03d} [S01] |" for i in range(60)]
        chunks = brain.chunk_body(header + "\n" + "\n".join(rows), 500)
        self.assertGreater(len(chunks), 1)
        self.assertTrue(all(chunk.startswith(header) for chunk in chunks))
        for row in rows:
            self.assertEqual(sum(row in chunk for chunk in chunks), 1)

    def test_cli_add_check_and_export_work_from_another_directory(self):
        script = self.root / "scripts/stock_brain.py"
        commands = [
            ["add", "--ticker", "SYNTH", "--name", "Synthetic Test Company", "--sector", "energy", "--exchange", "NYSE"],
            ["check"], ["export", "--output", "build/test.jsonl"],
        ]
        for command in commands:
            result = subprocess.run([sys.executable, str(script), "--root", str(self.root), *command],
                                    cwd=self.temp.name, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual((self.root / "build/test.jsonl").read_text(), "")


if __name__ == "__main__":
    unittest.main()
