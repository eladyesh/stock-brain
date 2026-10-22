#!/usr/bin/env python3
"""Explicit, bounded operations for the scalable coverage registry.

SEC source contract: https://www.sec.gov/search-filings/edgar-search-assistance/accessing-edgar-data
The ticker/exchange association file is not a guaranteed complete security master,
does not establish domicile/security type, and never establishes research review.
"""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import sqlite3
import sys

import research_pipeline as p
import stock_brain as kb
from review_gates import check_managed_reviews

ROOT = Path(__file__).resolve().parents[1]
SEC_LISTINGS_URL = "https://www.sec.gov/files/company_tickers_exchange.json"
MAX_BYTES = 30_000_000
MAX_BATCH = 500
SCOPE = (
    "Registry of SEC issuer/ticker/exchange associations for expanding U.S.-exchange listing coverage. "
    "Unassigned exchanges and OTC records are retained unless explicitly excluded. "
    "Registration does not establish U.S. domicile, common-stock security type, an active national-exchange listing, "
    "complete market coverage, or completed research. SEC does not guarantee this file's accuracy or scope."
)


def bounded_limit(value):
    try:
        parsed = int(value)
    except (ValueError, TypeError) as error:
        raise argparse.ArgumentTypeError("limit must be an integer") from error
    if not 1 <= parsed <= MAX_BATCH:
        raise argparse.ArgumentTypeError(f"limit must be between 1 and {MAX_BATCH}")
    return parsed


def timestamp(value):
    if not isinstance(value, str) or "T" not in value:
        raise ValueError("retrieved-at must be an ISO timestamp with a timezone")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as error:
        raise ValueError("retrieved-at must be an ISO timestamp with a timezone") from error
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ValueError("retrieved-at must include a timezone")
    parsed = parsed.astimezone(timezone.utc)
    if (parsed - datetime.now(timezone.utc)).total_seconds() > 300:
        raise ValueError("retrieved-at cannot be in the future")
    return parsed.isoformat()


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("Duplicate JSON object key: " + key)
        result[key] = value
    return result


def _reject_constant(value):
    raise ValueError("Non-finite JSON number: " + value)


def _plain_text(value, label, maximum):
    if not isinstance(value, str) or not value.strip() or len(value) > maximum:
        raise ValueError(f"Invalid listing {label}")
    if any(ord(char) < 32 or ord(char) == 127 for char in value):
        raise ValueError(f"Invalid control character in listing {label}")
    return value.strip()


def parse_listings(raw, *, exclude_unassigned=False, exclude_otc=False):
    """Validate the entire input before any import or absence-based retirement.

    The actual input bytes remain the provenance hash even if an explicitly
    requested partial import filters records. No security class is inferred.
    """
    if not isinstance(raw, bytes) or not raw or len(raw) > MAX_BYTES:
        raise ValueError("Listing source must contain between 1 byte and 30 MB")
    try:
        document = json.loads(raw.decode("utf-8-sig"), object_pairs_hook=_unique_object,
                              parse_constant=_reject_constant)
    except (UnicodeError, json.JSONDecodeError) as error:
        raise ValueError("Listing source must be valid UTF-8 JSON; HTML or partial downloads are not listings") from error
    if not isinstance(document, dict):
        raise ValueError("Expected SEC fields/data listing object")
    fields, rows = document.get("fields"), document.get("data")
    if (not isinstance(fields, list) or len(fields) != 4 or any(not isinstance(f, str) for f in fields)
            or set(fields) != {"cik", "name", "ticker", "exchange"}):
        raise ValueError("Expected exactly the SEC cik/name/ticker/exchange fields")
    if not isinstance(rows, list) or not rows:
        raise ValueError("Listing source data must be a nonempty array; empty snapshots cannot retire listings")
    output, seen, identities, excluded, exchanges = [], set(), {}, Counter(), Counter()
    for number, row in enumerate(rows, 1):
        if not isinstance(row, list) or len(row) != len(fields):
            raise ValueError(f"Listing row {number} does not match the fields array")
        item = dict(zip(fields, row))
        cik = item["cik"]
        if isinstance(cik, bool) or not isinstance(cik, (str, int)) or not re.fullmatch(r"\d{1,10}", str(cik), flags=re.ASCII) or int(cik) <= 0:
            raise ValueError(f"Invalid CIK in listing row {number}")
        cik = str(cik).zfill(10)
        name = _plain_text(item["name"], "name", 500)
        ticker = _plain_text(item["ticker"], "ticker", 32).upper()
        if not re.fullmatch(r"[A-Z0-9][A-Z0-9.\-/^+=]{0,31}", ticker):
            raise ValueError(f"Invalid ticker in listing row {number}")
        exchange = item["exchange"]
        if exchange is not None:
            exchange = _plain_text(exchange, "exchange", 80).upper()
            if not re.fullmatch(r"[A-Z0-9][A-Z0-9 ._/-]*", exchange):
                raise ValueError(f"Invalid exchange in listing row {number}")
        key = (cik, ticker, exchange)
        if key in seen:
            raise ValueError(f"Duplicate listing identity in row {number}")
        seen.add(key)
        security_key = (ticker, exchange)
        if security_key in identities and identities[security_key] != cik:
            raise ValueError(f"Conflicting ticker/exchange issuer identity in row {number}")
        identities[security_key] = cik
        exchanges[exchange or "UNASSIGNED"] += 1
        if exchange is None and exclude_unassigned:
            excluded["unassigned_exchange"] += 1
            continue
        if exchange is not None and exchange.startswith("OTC") and exclude_otc:
            excluded["otc"] += 1
            continue
        output.append([int(cik), name, ticker, exchange])
    if not output:
        raise ValueError("Explicit filters removed every listing; no snapshot was imported")
    return {"fields": ["cik", "name", "ticker", "exchange"], "data": output}, {
        "input_rows": len(rows), "included_rows": len(output), "excluded_rows": sum(excluded.values()),
        "excluded_by_reason": dict(excluded), "source_exchange_counts": dict(sorted(exchanges.items()))}


def load_import(args, store=None):
    """No network operation occurs unless --fetch was explicitly supplied."""
    if args.complete_snapshot and (args.exclude_otc or args.exclude_unassigned_exchange):
        raise ValueError("--complete-snapshot cannot be combined with exclusions; filtered imports are partial")
    if args.fetch:
        if args.retrieved_at:
            raise ValueError("--fetch records its actual retrieval timestamp; omit --retrieved-at")
        if args.source_url and args.source_url != SEC_LISTINGS_URL:
            raise ValueError("--fetch only supports the documented official SEC listings URL")
        if os.environ.get("STOCK_BRAIN_SEC_ENABLED", "1") != "1":
            raise ValueError("SEC collection paused by operator; existing registry retained")
        user_agent = os.environ.get("SEC_USER_AGENT", "")
        p.validate_sec_user_agent(user_agent)
        if store is None:
            raise ValueError("Explicit SEC fetch requires the shared coverage registry for global request pacing")
        from coverage_worker import SecFinancialProvider, sec_request_guard
        provider = SecFinancialProvider(args.root.resolve(), user_agent=user_agent, store=store)
        ready = provider.readiness()
        if not ready["ready"]:
            raise ValueError(ready["reason"])
        # Preserve raw bytes for independent parsing/hashing. The same shared
        # provider guard and failure policy protect every actual HTTP attempt.
        fetcher = p.Fetcher(args.root.resolve(), user_agent, before_request=sec_request_guard(store))
        provider.fetcher = fetcher
        try:
            raw, metadata = fetcher.fetch(SEC_LISTINGS_URL, refresh=True)
        except (ValueError, OSError) as error:
            provider.failure_policy(error)
            raise
        retrieved_at = timestamp(metadata["fetched_at"])
        acquisition = "explicit_sec_fetch"
    else:
        if args.source_url != SEC_LISTINGS_URL:
            raise ValueError("--file requires --source-url " + SEC_LISTINGS_URL)
        if not args.retrieved_at:
            raise ValueError("--file requires the source's --retrieved-at timestamp")
        retrieved_at = timestamp(args.retrieved_at)
        if args.file.stat().st_size > MAX_BYTES:
            raise ValueError("Listing source exceeds the 30 MB input limit")
        raw = args.file.read_bytes()
        acquisition = "operator_supplied_local_snapshot"
    payload, report = parse_listings(raw, exclude_unassigned=args.exclude_unassigned_exchange, exclude_otc=args.exclude_otc)
    source = {"url": SEC_LISTINGS_URL, "sha256": hashlib.sha256(raw).hexdigest(), "retrieved_at": retrieved_at,
              "acquisition": acquisition, "scope": SCOPE,
              "filters": {"exclude_unassigned_exchange": args.exclude_unassigned_exchange, "exclude_otc": args.exclude_otc},
              "input_rows": report["input_rows"], "included_rows": report["included_rows"]}
    return payload, source, report


def seed(store, root):
    """Register only configured issuers and preserve existing exact review bindings."""
    root = root.resolve()
    companies = p.universe(root)
    documents = {doc.metadata["ticker"]: doc for doc in kb.documents(root)}
    result = store.seed_companies(companies)
    reviewed, unreviewed = [], []
    for company in companies:
        ticker = company["ticker"]
        doc = documents.get(ticker)
        if not doc or doc.metadata.get("status") != "reviewed":
            unreviewed.append({"ticker": ticker, "reason": "no_reviewed_profile"})
            continue
        try:
            if check_managed_reviews(root, [doc]) != 1:
                raise ValueError("No evidence-bound managed review")
            packet_path = p.managed_packet_path(root, ticker)
            packet = p.read_json(packet_path)
            payload = {"ticker": ticker, "company_name": company["company_name"], "as_of": packet["as_of"],
                       "sections": packet["sections"], "sources": packet["sources"], "review_type": "ai",
                       "reviewed_at": doc.metadata["reviewed_at"],
                       "profile_sha256": p.digest(doc.path.read_bytes()), "packet_sha256": p.digest(packet_path.read_bytes())}
            store.put_payload(company["cik"], "reviewed_research", payload)
            reviewed.append(ticker)
        except (ValueError, OSError, KeyError) as error:
            unreviewed.append({"ticker": ticker, "reason": str(error)})
    return {"command": "seed", "registry": result, "configured_issuers": len(companies),
            "reviewed_payloads": len(reviewed), "reviewed_tickers": reviewed, "registered_without_review": unreviewed,
            "scope": "Configured repository companies only; no listing discovery, network fetch, or universe-file changes."}


def enqueue(store, *, ticker=None, limit=25):
    if not isinstance(limit, int) or isinstance(limit, bool) or not 1 <= limit <= MAX_BATCH:
        raise ValueError(f"limit must be between 1 and {MAX_BATCH}")
    if ticker:
        company = store.company(ticker)
        if not company:
            raise ValueError("Ticker is not registered: " + ticker)
        companies = [company]
    else:
        companies = store.eligible_for_job(kind="refresh_company", limit=limit)
    jobs = [store.enqueue(company["cik"], kind="refresh_company") for company in companies[:limit]]
    return {"command": "enqueue", "requested_limit": limit, "selected": len(jobs),
            "jobs": jobs, "selection": "Explicit ticker" if ticker else "Deterministic oldest eligible collection state, then historical payload age and CIK; active or blocked jobs skipped",
            "execution": "Queued only. This command does not download filings, invoke a model, or promote research to reviewed."}


def build_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", type=Path, help="SQLite registry path; otherwise CoverageStore's configured local default")
    commands = parser.add_subparsers(dest="command", required=True)
    seed_parser = commands.add_parser("seed", help="Register configured companies and copy only existing evidence-bound reviewed payloads")
    seed_parser.add_argument("--root", type=Path, default=ROOT)
    importer = commands.add_parser("import-listings", help="Import an explicit SEC listing snapshot; registration is not research")
    source = importer.add_mutually_exclusive_group(required=True)
    source.add_argument("--file", type=Path, help="Local SEC fields/data JSON; no network request")
    source.add_argument("--fetch", action="store_true", help="Explicitly retrieve the SEC file with your identifying SEC_USER_AGENT")
    importer.add_argument("--source-url", help="Official SEC URL required with --file")
    importer.add_argument("--retrieved-at", help="Source retrieval ISO timestamp with timezone, required with --file")
    importer.add_argument("--root", type=Path, default=ROOT, help="Cache root used only for explicit --fetch")
    importer.add_argument("--complete-snapshot", action="store_true", help="Explicitly allow retirement of absent listings in a validated, unfiltered complete snapshot")
    importer.add_argument("--exclude-unassigned-exchange", action="store_true", help="Explicit partial import excluding null exchange; cannot be complete")
    importer.add_argument("--exclude-otc", action="store_true", help="Explicit partial import excluding exchange labels beginning OTC; cannot be complete")
    queue = commands.add_parser("enqueue", help="Queue a bounded batch; does not run research")
    queue.add_argument("--limit", type=bounded_limit, default=25)
    queue.add_argument("--ticker", type=lambda s: _plain_text(s, "ticker", 32).upper())
    status = commands.add_parser("status", help="Print counts and a bounded company sample")
    status.add_argument("--limit", type=bounded_limit, default=10)
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    try:
        from coverage_store import CoverageStore
        if args.command == "import-listings" and args.fetch:
            # Network requests share persisted rate reservations/cooldowns with workers.
            store = CoverageStore(args.db)
            imported = load_import(args, store=store)
        else:
            # Validate local snapshots completely before opening or mutating the store.
            imported = load_import(args) if args.command == "import-listings" else None
            store = CoverageStore(args.db)
        if args.command == "seed":
            result = seed(store, args.root)
        elif args.command == "import-listings":
            payload, source, report = imported
            result = {"command": args.command, "source": source, "input": report,
                      "complete_snapshot": args.complete_snapshot,
                      "import": store.import_listings(payload, source, complete=args.complete_snapshot), "scope": SCOPE}
        elif args.command == "enqueue":
            result = enqueue(store, ticker=args.ticker, limit=args.limit)
        else:
            page = store.list_companies(limit=args.limit)
            sample = [{key: item.get(key) for key in ("cik", "ticker", "company_name", "exchange", "status")} for item in page["items"]]
            result = {"command": "status", "summary": store.stats(), "sample": sample,
                      "sample_limit": args.limit, "total_issuers": page["total"], "scope": SCOPE}
        print(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False))
        return 0
    except (ValueError, OSError, KeyError, sqlite3.Error) as error:
        print(json.dumps({"error": str(error), "command": args.command}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
