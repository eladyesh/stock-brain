"""Independent regressions for scale, scheduling and expired publication leases.

These expectations were selected from the ALL-US foundation requirements, not
from the existing module tests. All fixtures are synthetic and network-free.
"""
from contextlib import contextmanager
from copy import deepcopy
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import sqlite3
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from coverage_store import CoverageStore, LeaseLostError
import coverage_runtime


class Clock:
    def __init__(self):
        self.value = datetime(2026, 10, 22, tzinfo=timezone.utc)

    def __call__(self):
        return self.value


class IndependentCoverageStoreTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.clock = Clock()
        self.store = CoverageStore(Path(self.temporary.name) / "coverage.sqlite3", clock=self.clock)
        self.store.seed_companies([
            {"cik": 1, "ticker": "FIRST", "company_name": "First Issuer", "exchange": "NASDAQ"},
            {"cik": 2, "ticker": "SECOND", "company_name": "Second Issuer", "exchange": "NYSE"},
        ])

    def test_registry_and_queue_metadata_queries_do_not_read_payload_bodies(self):
        self.store.put_payload(1, "history", {"cik": "0000000001", "fixture": "opaque payload"})
        original_connection = self.store._connection

        @contextmanager
        def metadata_only_connection(write=False):
            with original_connection(write=write) as db:
                def authorize(action, table, column, _database, _trigger):
                    if action == sqlite3.SQLITE_READ and table == "company_payloads" and column == "value_json":
                        return sqlite3.SQLITE_DENY
                    return sqlite3.SQLITE_OK
                db.set_authorizer(authorize)
                yield db

        with patch.object(self.store, "_connection", metadata_only_connection):
            page = self.store.list_companies(limit=2)
            self.assertEqual(len(page["items"]), 2)
            self.assertIn("history", page["items"][0]["payloads"])
            self.assertEqual(len(self.store.eligible_for_job(limit=2)), 2)

    def test_successful_missing_history_check_yields_to_an_unchecked_issuer(self):
        first = self.store.eligible_for_job(limit=1)[0]
        self.assertEqual(first["cik"], "0000000001")
        job = self.store.enqueue(first["cik"])
        lease = self.store.claim("collector")
        self.clock.value += timedelta(seconds=1)
        self.store.commit_job(job["id"], "collector", lease["lease_token"], {
            "collector_state": {"value": {
                "cik": first["cik"], "last_checked_at": self.clock().isoformat(),
                "last_action": "no_supported_filing", "canonical_reviewed": False,
            }},
        }, result={"action": "no_supported_filing", "classification": "quality_review_required"})
        next_company = self.store.eligible_for_job(limit=1)[0]
        self.assertEqual(next_company["cik"], "0000000002",
                         "An issuer without supported forms must not monopolize each bounded batch.")

    def test_lease_expiring_during_write_lock_wait_cannot_publish_payloads(self):
        self.store.put_payload(1, "history", {"cik": "0000000001", "value": "last good"})
        job = self.store.enqueue(1)
        lease = self.store.claim("collector", lease_seconds=5)
        original_connection = self.store._connection

        @contextmanager
        def delayed_write_connection(write=False):
            # Deterministically model waiting for another SQLite writer. The
            # actual ownership check must use the time after acquiring the lock.
            if write:
                self.clock.value += timedelta(seconds=6)
            with original_connection(write=write) as db:
                yield db

        with patch.object(self.store, "_connection", delayed_write_connection):
            with self.assertRaises(LeaseLostError):
                self.store.commit_job(job["id"], "collector", lease["lease_token"], {
                    "history": {"value": {"cik": "0000000001", "value": "expired writer"}},
                })
        self.assertEqual(self.store.get_payload(1, "history")["value"], "last good")

    def test_startup_seed_cannot_overwrite_a_concurrently_collected_history(self):
        root = Path(__file__).resolve().parents[1]
        pilot = json.loads((root / "research/pilot/MSFT.json").read_text())
        old = json.loads((root / "research/financials/MSFT.json").read_text())
        newer = deepcopy(old)
        newer["as_of"] = "2026-10-21"
        newer["source"]["retrieved_at"] = "2026-10-21T12:00:00+00:00"
        newer["source"]["sha256"] = "9" * 64
        company = {"cik": old["cik"], "ticker": "MSFT", "company_name": "Microsoft Corporation", "exchange": "NASDAQ"}
        self.store.seed_companies([company])
        self.store.put_payload(old["cik"], "history", old, source=old["source"])
        snapshot = {"companies": [{"ticker": "MSFT", "as_of": pilot["as_of"], "history": old,
                                    "sections": pilot["sections"], "sources": pilot["sources"]}]}
        original_get = self.store.get_payload
        original_get_record = self.store.get_payload_record
        interleaved = False

        def concurrent_commit_after_read(cik, kind, reader):
            nonlocal interleaved
            observed = reader(cik, kind)
            if kind == "history" and not interleaved:
                interleaved = True
                # Model a leased worker completing between the startup read and
                # startup publication; its source snapshot must remain latest.
                self.store.put_payload(cik, "history", newer, source=newer["source"])
            return observed

        with patch.object(coverage_runtime, "CoverageStore", return_value=self.store), \
                patch.object(coverage_runtime.p, "universe", return_value=[company]), \
                patch.object(self.store, "get_payload", side_effect=lambda cik, kind:
                             concurrent_commit_after_read(cik, kind, original_get)), \
                patch.object(self.store, "get_payload_record", side_effect=lambda cik, kind:
                             concurrent_commit_after_read(cik, kind, original_get_record)):
            coverage_runtime.initialize_coverage(root, snapshot, self.store.path)
        self.assertTrue(interleaved)
        retained = original_get(old["cik"], "history")
        self.assertEqual(retained["source"]["sha256"], newer["source"]["sha256"],
                         "Startup seeding must not supersede a collection committed after its initial read.")


if __name__ == "__main__":
    unittest.main()
