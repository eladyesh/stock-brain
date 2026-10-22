"""Bounded, read-only registry routes, separate from the curated desk snapshot.

``serve_coverage(store, path, query_string)`` returns a WSGI status string and a
JSON-ready object, or ``None`` for an unrelated route. The HTTP application must
enforce GET/HEAD. Listing reads only registry rows and payload metadata. Detail
reads at most four payloads for one stable CIK and never writes research status.
"""
from __future__ import annotations

from copy import deepcopy
from datetime import date
import re
import sqlite3
from urllib.parse import parse_qs, unquote

import financial_history
import ttm


DEFAULT_LIMIT = 50
MAX_LIMIT = 100
MAX_OFFSET = 1_000_000
MAX_QUERY_LENGTH = 200
PAYLOAD_KINDS = ("history", "submissions", "automatic_changes", "reviewed_research")
COLLECTED_KINDS = frozenset(PAYLOAD_KINDS[:3])
REGISTRY_FIELDS = ("cik", "company_id", "ticker", "company_name", "exchange", "status")
LISTING_FIELDS = ("ticker", "exchange", "status", "first_seen_at", "last_seen_at", "inactivated_at")
PAYLOAD_FIELDS = ("version", "sha256", "stored_at", "source")
SCOPE_NOTE = (
    "Registry membership is separate from collected financial coverage and dated research review. "
    "Automatic collection does not review or update canonical research."
)


class _SnapshotChanged(Exception):
    """A writer committed between the bounded per-company payload reads."""


def _query(query_string, *, listing=False):
    if not isinstance(query_string, str) or len(query_string) > 4096:
        raise ValueError("invalid_query")
    if re.search(r"%(?![0-9A-Fa-f]{2})", query_string):
        raise ValueError("invalid_query")
    params = parse_qs(query_string, keep_blank_values=True, max_num_fields=8, errors="strict")
    allowed = {"q", "limit", "offset"} if listing else set()
    if set(params) - allowed or any(len(values) != 1 for values in params.values()):
        raise ValueError("invalid_query")
    query = params.get("q", [""])[0]
    if len(query) > MAX_QUERY_LENGTH or any(ord(c) < 32 or ord(c) == 127 for c in query):
        raise ValueError("invalid_query")
    query = query.strip()
    numbers = {}
    for name, default, lower, upper in (("limit", DEFAULT_LIMIT, 1, MAX_LIMIT), ("offset", 0, 0, MAX_OFFSET)):
        raw = params.get(name, [str(default)])[0]
        if not re.fullmatch(r"[0-9]{1,7}", raw):
            raise ValueError("invalid_pagination")
        number = int(raw)
        if not lower <= number <= upper:
            raise ValueError("invalid_pagination")
        numbers[name] = number
    return query, numbers["limit"], numbers["offset"]


def _identifier(value):
    if not isinstance(value, str) or len(value) > 96 or re.search(r"%(?![0-9A-Fa-f]{2})", value):
        return None
    try:
        value = unquote(value, errors="strict").upper()
    except UnicodeError:
        return None
    if re.fullmatch(r"[0-9]{1,10}", value):
        return value.zfill(10) if int(value) > 0 else None
    # Match registry listing symbols, including encoded preferred/unit suffixes.
    # The identifier is only passed to a parameterized lookup, never a file path.
    if re.fullmatch(r"[A-Z0-9][A-Z0-9.\-^/+=]{0,31}", value):
        return value
    return None


def _registry_record(record):
    """Whitelist metadata: a list item can never grow into a financial snapshot."""
    result = {key: deepcopy(record.get(key)) for key in REGISTRY_FIELDS}
    result["listings"] = [{key: deepcopy(listing.get(key)) for key in LISTING_FIELDS}
                          for listing in record.get("listings", [])]
    result["payloads"] = {
        kind: {key: deepcopy(meta.get(key)) for key in PAYLOAD_FIELDS}
        for kind, meta in record.get("payloads", {}).items() if kind in PAYLOAD_KINDS
    }
    result["collection_status"] = "data-collected" if COLLECTED_KINDS.intersection(result["payloads"]) else "registry-only"
    # Presence is all a registry-only read can establish; detail validates it.
    result["has_reviewed_research"] = "reviewed_research" in result["payloads"]
    return result


def _iso_date(value):
    if not isinstance(value, str):
        return False
    try:
        return date.fromisoformat(value).isoformat() == value
    except ValueError:
        return False


def _research(payload, company, issues):
    result = {"status": "not-available", "canonical_reviewed": False, "review_type": None,
              "as_of": None, "payload": None}
    if payload is None:
        return result
    tickers = {company.get("ticker"), *(listing.get("ticker") for listing in company.get("listings", []))}
    # This distinct payload is written only by the reviewed-corpus integration.
    # Neither automatic data nor a boolean on a registry row can attest review.
    valid = (isinstance(payload, dict) and payload.get("review_type") in {"ai", "human"}
             and payload.get("review_status", "reviewed") == "reviewed"
             and payload.get("canonical_reviewed", True) is True
             and payload.get("ticker") in tickers
             and payload.get("cik", company["cik"]) == company["cik"]
             and _iso_date(payload.get("as_of"))
             and isinstance(payload.get("sections"), dict) and bool(payload["sections"])
             and isinstance(payload.get("sources"), list) and bool(payload["sources"]))
    if not valid:
        issues.append("invalid_reviewed_research_record")
        result["status"] = "review-required"
        return result
    return {"status": "reviewed", "canonical_reviewed": True, "review_type": payload["review_type"],
            "as_of": payload["as_of"], "payload": deepcopy(payload)}


def _quality_requires_review(history, changes):
    if history:
        if any(flag.get("status", "open") == "open" for flag in history.get("qa_flags", [])):
            return True
        for period in history.get("periods", []):
            if period.get("flags"):
                return True
        for cells in history.get("financials", {}).values():
            if any(cell.get("conflicts") or cell.get("status") == "conflicted"
                   or ttm.BLOCKING_FLAGS.intersection(cell.get("flags", [])) for cell in cells.values()):
                return True
    if changes:
        return (changes.get("classification") == "quality_review_required"
                or bool(changes.get("qa", {}).get("open_flag_count"))
                or any(change.get("comparison") == "blocked" for change in changes.get("changes", [])))
    return False


def _company_detail(store, record):
    company = _registry_record(record)
    issues = []
    payloads = {kind: store.get_payload(company["cik"], kind) for kind in PAYLOAD_KINDS}
    current = store.company(company["cik"])
    if current is None or _registry_record(current)["payloads"] != company["payloads"]:
        # get_payload calls use independent reads. Never attach old metadata to
        # new values or mix history and change drafts across a worker commit.
        raise _SnapshotChanged()
    collected = {}
    for kind in PAYLOAD_KINDS[:3]:
        payload = payloads[kind]
        if payload is not None and (not isinstance(payload, dict) or payload.get("cik") != company["cik"]):
            issues.append(kind + "_issuer_mismatch")
            payload = None
        collected[kind] = deepcopy(payload)

    history = collected["history"]
    history_valid = False
    result_ttm = None
    if history is not None:
        try:
            financial_history.validate_history(history)
            result_ttm = ttm.build_ttm(history)
            history_valid = True
        except (ValueError, KeyError, TypeError, AttributeError, OverflowError):
            # Corrupt or partially written data must not become displayed facts.
            issues.append("invalid_financial_history")
            collected["history"] = None
    research = _research(payloads["reviewed_research"], company, issues)
    has_collected = any(payloads[kind] is not None for kind in PAYLOAD_KINDS[:3])
    status = "data-collected" if has_collected else "registry-only"
    try:
        review_required = _quality_requires_review(history if history_valid else None, collected["automatic_changes"])
    except (ValueError, KeyError, TypeError, AttributeError):
        issues.append("invalid_collection_quality_metadata")
        review_required = True
    if issues or review_required:
        status = "review-required"
    # These labels apply to the automatic collection only. They cannot overwrite
    # a separate, dated review or imply that later filings have been reviewed.
    return {"schema_version": 1, "company": company, "collection_status": status,
            "collection_review_status": "unreviewed",
            "research": research, "collected": collected,
            "financials_validated": history_valid, "ttm": result_ttm,
            "issues": sorted(set(issues)), "scope_note": SCOPE_NOTE}


def serve_coverage(store, path, query_string=""):
    """Handle coverage routes without reading the global snapshot or changing state."""
    if path not in {"/api/coverage", "/api/companies"} and not path.startswith("/api/companies/"):
        return None
    try:
        query, limit, offset = _query(query_string, listing=path == "/api/companies")
    except (ValueError, UnicodeError):
        return "400 Bad Request", {"error": "invalid_query", "limits": {
            "limit": {"min": 1, "max": MAX_LIMIT}, "offset": {"min": 0, "max": MAX_OFFSET},
            "q_max_length": MAX_QUERY_LENGTH}}
    if store is None:
        return "503 Service Unavailable", {"error": "coverage_unavailable"}
    try:
        if path == "/api/coverage":
            return "200 OK", {**store.stats(), "scope_note": SCOPE_NOTE}
        if path == "/api/companies":
            page = store.list_companies(query=query, limit=limit, offset=offset)
            return "200 OK", {"items": [_registry_record(record) for record in page["items"]],
                              "total": page["total"], "limit": limit, "offset": offset}
        identifier = _identifier(path.removeprefix("/api/companies/"))
        if identifier is None:
            return "404 Not Found", {"error": "company_not_found"}
        try:
            company = store.company(identifier)
        except ValueError:
            return "409 Conflict", {"error": "ambiguous_company_identifier", "hint": "Use the stable CIK."}
        if company is None:
            return "404 Not Found", {"error": "company_not_found"}
        return "200 OK", _company_detail(store, company)
    except _SnapshotChanged:
        return "503 Service Unavailable", {"error": "company_data_changed", "retryable": True}
    except (sqlite3.DatabaseError, OSError, ValueError, KeyError, TypeError, AttributeError):
        return "503 Service Unavailable", {"error": "coverage_unavailable"}
