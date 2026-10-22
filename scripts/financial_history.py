#!/usr/bin/env python3
"""Collect conservative, source-linked annual and standalone-quarter SEC financials.

No calendar-frame inference, estimates, paid APIs, or missing-to-zero coercion.
The source cache is maintained by research_pipeline.Fetcher under ignored build/.
"""
from __future__ import annotations

import argparse
import copy
from collections import Counter, defaultdict
from datetime import date, timedelta
import json
import math
import os
from pathlib import Path
import re
import sys

import research_pipeline as rp
import stock_brain as kb

SCHEMA_VERSION = 1
FORMS = {"10-K", "10-K/A", "10-Q", "10-Q/A"}
DURATION = {
    "revenue": ("USD", ("RevenueFromContractWithCustomerExcludingAssessedTax", "Revenues", "SalesRevenueNet", "RevenueFromContractWithCustomerIncludingAssessedTax")),
    "net_income": ("USD", ("NetIncomeLoss",)),
    "net_income_common": ("USD", ("NetIncomeLossAvailableToCommonStockholdersBasic",)),
    "net_income_including_noncontrolling_interests": ("USD", ("ProfitLoss",)),
    "operating_income": ("USD", ("OperatingIncomeLoss",)),
    "gross_profit": ("USD", ("GrossProfit",)),
    "cost_of_revenue": ("USD", ("CostOfRevenue", "CostOfGoodsAndServicesSold")),
    "eps_basic": ("USD/shares", ("EarningsPerShareBasic",)),
    "eps_diluted": ("USD/shares", ("EarningsPerShareDiluted",)),
    "shares_basic": ("shares", ("WeightedAverageNumberOfSharesOutstandingBasic",)),
    "shares_diluted": ("shares", ("WeightedAverageNumberOfDilutedSharesOutstanding",)),
    "operating_cash_flow": ("USD", ("NetCashProvidedByUsedInOperatingActivities",)),
    "capex": ("USD", ("PaymentsToAcquirePropertyPlantAndEquipment",)),
    "purchases_of_productive_assets": ("USD", ("PaymentsToAcquireProductiveAssets",)),
    "stock_based_compensation": ("USD", ("ShareBasedCompensation",)),
}
INSTANT = {
    "cash_and_equivalents": ("USD", ("CashAndCashEquivalentsAtCarryingValue",)),
    "short_term_investments": ("USD", ("ShortTermInvestments",)),
    "debt_current": ("USD", ("DebtCurrent", "LongTermDebtCurrent", "LongTermDebtAndCapitalLeaseObligationsCurrent", "NotesPayableCurrent")),
    "debt_noncurrent": ("USD", ("LongTermDebtNoncurrent", "LongTermDebtAndCapitalLeaseObligations", "LongTermNotesPayable")),
    "long_term_debt_total": ("USD", ("LongTermDebt", "LongTermDebtAndCapitalLeaseObligationsIncludingCurrentMaturities")),
    "short_term_borrowings": ("USD", ("ShortTermBorrowings",)),
    "debt_total": ("USD", ("DebtAndCapitalLeaseObligations",)),
    "shares_outstanding": ("shares", ("CommonStockSharesOutstanding",)),
}
METRICS = {**DURATION, **INSTANT, "free_cash_flow": ("USD", ())}
NONADDITIVE = {"eps_basic", "eps_diluted", "shares_basic", "shares_diluted"}
SHARE_METRICS = NONADDITIVE | {"shares_outstanding"}
DEBT_METRICS = {"debt_current", "debt_noncurrent", "long_term_debt_total", "debt_total"}
SCOPE_BY_METRIC = {
    "eps_basic": "basic_common_eps", "eps_diluted": "diluted_common_eps",
    "shares_basic": "weighted_average_basic_common_shares",
    "shares_diluted": "weighted_average_diluted_common_shares",
    "shares_outstanding": "period_end_common_shares_outstanding",
}
CORE = tuple(tag for key in ("revenue", "net_income", "operating_income", "operating_cash_flow") for tag in DURATION[key][1])


def days(start, end):
    return (date.fromisoformat(end) - date.fromisoformat(start)).days + 1


def next_day(value):
    return (date.fromisoformat(value) + timedelta(days=1)).isoformat()


def filing_url(cik, accession):
    return f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{accession.replace('-', '')}/{accession}-index.html"


def _valid_row(row, cutoff):
    try:
        end, filed = row["end"], row["filed"]
        date.fromisoformat(end)
        date.fromisoformat(filed)
        if row.get("start"):
            if days(row["start"], end) < 1:
                return False
        return (end <= cutoff and filed <= cutoff and end <= filed and row.get("form") in FORMS
                and re.fullmatch(r"\d{10}-\d{2}-\d{6}", row.get("accn", "")) is not None
                and isinstance(row.get("val"), (float, int)) and not isinstance(row["val"], bool)
                and math.isfinite(row["val"]))
    except (KeyError, TypeError, ValueError):
        return False


def source_rows(data, tag, unit, cutoff, taxonomy="us-gaap"):
    return [r for r in data.get("facts", {}).get(taxonomy, {}).get(tag, {}).get("units", {}).get(unit, [])
            if _valid_row(r, cutoff)]


def discover_periods(data, cutoff, annual_limit=5, quarterly_limit=12):
    """Use the current period of each filing, never a comparative fact's fy/fp.

    Focus is anchored by the latest end among core statement durations in one
    accession. Annual start/end and current-quarter fp are source context. Q4
    boundaries require a sourced Q3 end and sourced full-year start/end.
    """
    by_accession = defaultdict(list)
    for tag in CORE:
        for row in source_rows(data, tag, "USD", cutoff):
            if row.get("start") and 60 <= days(row["start"], row["end"]) <= 400:
                by_accession[row["accn"]].append(row)
    periods, issues = {}, []
    for accession, rows in by_accession.items():
        focus_end = max(row["end"] for row in rows)
        current = [row for row in rows if row["end"] == focus_end]
        contexts = {(row.get("fy"), row.get("fp")) for row in current}
        if len(contexts) != 1:
            issues.append({"code": "conflicting_filing_focus", "accession": accession})
            continue
        fy, fp = contexts.pop()
        if not isinstance(fy, int) or isinstance(fy, bool):
            continue
        form = current[0]["form"]
        if fp == "FY" and form.startswith("10-K"):
            intervals = {(r["start"], r["end"]) for r in current if 330 <= days(r["start"], r["end"]) <= 400}
            kind, quarter = "annual", None
        elif fp in {"Q1", "Q2", "Q3"} and form.startswith("10-Q"):
            intervals = {(r["start"], r["end"]) for r in current if 60 <= days(r["start"], r["end"]) <= 110}
            kind, quarter = "quarterly", int(fp[1])
        else:
            continue
        if len(intervals) != 1:
            issues.append({"code": "ambiguous_primary_period", "accession": accession, "end": focus_end})
            continue
        start, end = intervals.pop()
        key = f"{kind}:{end}"
        period = {"id": key, "type": kind, "start": start, "end": end, "fiscal_year": fy,
                  "fiscal_quarter": quarter, "reported_fiscal_year": fy,
                  "fiscal_identity_basis": "current_core_duration_in_original_filing",
                  "identity_accessions": [accession], "flags": []}
        if key in periods:
            previous = periods[key]
            if any(previous[k] != period[k] for k in ("start", "fiscal_year", "fiscal_quarter")):
                previous["flags"].append("conflicting_fiscal_identity")
                previous["fiscal_year"] = None
            previous["identity_accessions"].append(accession)
        else:
            periods[key] = period
    annuals = sorted((p for p in periods.values() if p["type"] == "annual"), key=lambda p: p["end"])
    quarters = sorted((p for p in periods.values() if p["type"] == "quarterly"), key=lambda p: p["end"])
    for q in quarters:
        containing = [a for a in annuals if a["start"] <= q["start"] <= q["end"] <= a["end"]]
        preceding = [a for a in annuals if a["end"] < q["start"]]
        expected_year = None
        if len(containing) == 1:
            anchor = containing[0]
            q["fiscal_year_start"] = anchor["start"]
            expected_year = anchor["fiscal_year"]
            q["fiscal_year_anchor"] = anchor["id"]
        elif preceding:
            anchor = preceding[-1]
            if days(anchor["end"], q["end"]) <= 330 and anchor["fiscal_year"] is not None:
                q["fiscal_year_start"] = next_day(anchor["end"])
                expected_year = anchor["fiscal_year"] + 1
                q["fiscal_year_anchor"] = anchor["id"]
        if expected_year is not None and expected_year != q["reported_fiscal_year"]:
            q["fiscal_year"] = None
            q["fiscal_identity_basis"] = "reported_context_conflicts_with_annual_boundaries"
            q["flags"].append("conflicting_fiscal_year")
        # A Q1 must begin at the fiscal year's sourced beginning. Never alter it.
        if q["fiscal_quarter"] == 1 and q.get("fiscal_year_start") != q["start"]:
            q["flags"].append("fiscal_start_mismatch")
        if not q.get("fiscal_year_start"):
            q["flags"].append("missing_annual_anchor")
    for annual in annuals:
        matches = [q for q in quarters if q["fiscal_quarter"] == 3
                   and q.get("fiscal_year_start") == annual["start"]
                   and annual["start"] <= q["start"] < q["end"] < annual["end"]]
        if len(matches) == 1 and 60 <= days(next_day(matches[0]["end"]), annual["end"]) <= 110:
            q3 = matches[0]
            p = {"id": f"quarterly:{annual['end']}", "type": "quarterly", "start": next_day(q3["end"]),
                 "end": annual["end"], "fiscal_year": annual["fiscal_year"], "fiscal_quarter": 4,
                 "reported_fiscal_year": annual["reported_fiscal_year"], "fiscal_year_start": annual["start"],
                 "fiscal_year_anchor": annual["id"], "fiscal_identity_basis": "annual_end_and_sourced_q3_boundary",
                 "identity_accessions": sorted(set(annual["identity_accessions"] + q3["identity_accessions"])), "flags": []}
            periods[p["id"]] = p
    selected = sorted(annuals, key=lambda p: p["end"], reverse=True)[:annual_limit]
    selected += sorted((p for p in periods.values() if p["type"] == "quarterly"), key=lambda p: p["end"], reverse=True)[:quarterly_limit]
    for p in selected:
        fy = f"FY{p['fiscal_year']}" if p["fiscal_year"] is not None else "Fiscal year unverified"
        p["label"] = fy if p["type"] == "annual" else f"Q{p['fiscal_quarter']} {fy}"
    return selected, issues


def missing(metric, reason="No exact reported fact with an accepted tag, unit, period and filing available by cutoff."):
    return {"status": "missing_required_source", "value": None, "unit": METRICS[metric][0],
            "basis": "US GAAP", "evidence_label": "missing_required_source", "confidence": "low",
            "model_usable": False, "comparison_status": "missing_required_source", "provenance": [],
            "conflicts": [], "flags": [], "note": reason}


def _provenance(row, tag, unit, cik, taxonomy="us-gaap"):
    return {"source_id": f"SEC-{row['accn']}", "accession": row["accn"], "filed": row["filed"],
            "form": row["form"], "taxonomy": taxonomy, "tag": tag, "unit": unit,
            "start": row.get("start"), "end": row["end"], "source_value": row["val"],
            "filing_fiscal_year": row.get("fy"), "filing_fiscal_period": row.get("fp"),
            "calendar_frame": row.get("frame"), "url": filing_url(cik, row["accn"])}


def _observation_key(source):
    """Identify a reviewed fact, not merely an issuer or a plausible ratio."""
    return tuple(source.get(k) for k in ("accession", "filed", "taxonomy", "tag", "unit",
                                         "start", "end", "source_value"))


def eligible_normalization_reviews(reviews, cik, cutoff):
    """Keep only evidence available at the requested historical cutoff."""
    eligible, review_ids = [], set()
    for review in reviews or []:
        kb.need(review.get("type") in {"stock_split", "filing_scope"} and review.get("cik") == cik,
                "normalization review type or issuer mismatch")
        kb.iso_date(review["effective_date"], "review effective date", required=True)
        kb.need(review.get("review_id") and review["review_id"] not in review_ids, "missing or duplicate normalization review ID")
        review_ids.add(review["review_id"])
        if review["type"] == "stock_split":
            ratio = review.get("new_shares_per_old_share")
            kb.need(isinstance(ratio, (int, float)) and not isinstance(ratio, bool)
                    and math.isfinite(ratio) and ratio > 0, "invalid reviewed split ratio")
        kb.need(bool(review.get("evidence")), "normalization review requires filing evidence")
        for evidence in review["evidence"]:
            kb.iso_date(evidence["filed"], "review evidence filed", required=True)
            kb.need(bool(re.fullmatch(r"[0-9a-f]{64}", evidence.get("sha256", ""))), "review evidence requires document hash")
        if review["effective_date"] > cutoff or any(s["filed"] > cutoff for s in review["evidence"]):
            continue
        observations, keys = [], set()
        for observation in review["observations"]:
            if review["type"] == "stock_split":
                kb.need(observation.get("split_basis") in {"pre_split", "post_split"}, "invalid reviewed share basis")
            else:
                metric = observation.get("metric")
                kb.need(metric in SHARE_METRICS | DEBT_METRICS, "unsupported filing scope metric")
                expected_scope = SCOPE_BY_METRIC.get(metric)
                kb.need((expected_scope and observation.get("scope") == expected_scope) or
                        (metric in DEBT_METRICS and observation.get("scope") in {
                            "carrying_value_excluding_finance_leases", "carrying_value_including_finance_leases"}),
                        "invalid reviewed metric scope")
                kb.need(bool(observation.get("rationale")) and bool(observation.get("source_document", {}).get("locator")),
                        "filing scope requires a document locator and rationale")
                kb.need(any(e["url"] == observation["source_document"].get("url")
                            and e["sha256"] == observation["source_document"].get("sha256")
                            for e in review["evidence"]), "scope observation is not bound to its evidence document")
            kb.need(isinstance(observation.get("decimals"), int) and not isinstance(observation["decimals"], bool)
                    and -12 <= observation["decimals"] <= 12,
                    "invalid source rounding precision")
            kb.need(bool(re.fullmatch(r"[0-9a-f]{64}", observation.get("source_document", {}).get("sha256", ""))),
                    "reviewed observation requires document hash")
            kb.need(observation["end"] <= observation["filed"], "reviewed source end exceeds filing date")
            key = (observation.get("metric"), _observation_key(observation))
            kb.need(key not in keys, "duplicate reviewed observation")
            keys.add(key)
            if observation["filed"] <= cutoff:
                observations.append(observation)
        eligible.append({**review, "observations": observations})
    return eligible


def reconcile_share_split(cell, metric, cik, cutoff, reviews):
    """Apply a filing-verified split bridge to exact reviewed observations only.

    The persisted review contains the source document hash and inline-XBRL
    precision of every approved observation. New/changed facts, non-share
    revisions, same-day conflicts and facts outside that evidence stay gated.
    """
    if metric not in SHARE_METRICS or cell["status"] != "reported" or cell["value"] is None or cell.get("share_basis"):
        return cell
    selected = cell["provenance"][0]
    for review in reviews or []:
        if review.get("type") != "stock_split" or review.get("cik") != cik:
            continue
        evidence = review.get("evidence", [])
        if (not evidence or review["effective_date"] > cutoff
                or any(s["filed"] > cutoff for s in evidence)):
            continue
        ratio = review["new_shares_per_old_share"]
        kb.need(isinstance(ratio, (int, float)) and not isinstance(ratio, bool)
                and math.isfinite(ratio) and ratio > 0, "invalid reviewed split ratio")
        observations = {_observation_key(p): p for p in review["observations"]
                        if p["filed"] <= cutoff}
        chosen = observations.get(_observation_key(selected))
        if not chosen:
            continue

        def adjustment(observation):
            return (1 / ratio if metric.startswith("eps_") else ratio) if observation["split_basis"] == "pre_split" else 1

        def amount(observation):
            return observation["source_value"] * adjustment(observation)

        def half_precision(observation):
            return 0.5 * 10 ** (-observation["decimals"]) * adjustment(observation)

        resolved, unresolved = [], []
        for conflict in cell["conflicts"]:
            alternatives = [observations.get(_observation_key(p)) for p in conflict.get("alternatives", [])]
            # A stock split does not explain same-basis revisions. Rounding
            # tolerance comes from the filing's decimals, not an arbitrary %.
            supported = (conflict["type"] == "historical_value_revision_or_context_conflict"
                         and alternatives and all(p is not None and p["split_basis"] != chosen["split_basis"]
                             and abs(amount(p) - amount(chosen)) <= half_precision(p) + half_precision(chosen) + 1e-9
                             for p in alternatives))
            if supported:
                resolved.append({**conflict, "previous_resolution": conflict["resolution"],
                                 "resolution": "Verified stock split and overlapping source-rounding intervals; original values retained.",
                                 "review_id": review["review_id"]})
            else:
                unresolved.append(conflict)
        cell["conflicts"] = unresolved
        if resolved:
            cell["resolved_conflicts"] = resolved
        if not any(c["type"] == "historical_value_revision_or_context_conflict" for c in unresolved):
            cell["flags"] = [f for f in cell["flags"] if f != "revision_requires_review"]
        cell["flags"] = [f for f in cell["flags"] if f != "share_split_and_corporate_action_basis_unverified"]
        cell["flags"].append("share_split_basis_verified")
        cell["share_basis"] = {"review_id": review["review_id"], "effective_date": review["effective_date"],
                               "new_shares_per_old_share": ratio, "basis": "post_split",
                               "source_basis": chosen["split_basis"], "source_decimals": chosen["decimals"],
                               "evidence_source_ids": [s["source_id"] for s in evidence]}
        if chosen["split_basis"] == "pre_split":
            cell["value"] = amount(chosen)
            cell["status"] = "derived"
            cell["evidence_label"] = "derived_calculation"
            cell["confidence"] = "medium"
            cell["formula"] = f"Reported {metric} {'divided by' if metric.startswith('eps_') else 'multiplied by'} verified split ratio {ratio}; source rounding retained."
            cell["flags"].append("historical_fact_split_normalized")
        else:
            cell["confidence"] = "high" if not unresolved else "medium"
        cell["model_usable"] = not unresolved and set(cell["flags"]) <= {"share_split_basis_verified", "historical_fact_split_normalized"}
        cell["comparison_status"] = "comparable" if cell["model_usable"] else "not_comparable"
        return cell
    return cell


def reconcile_filing_scope(cell, metric, reviews):
    """Verify the definition of exact observations; never infer missing values.

    Scope approval does not resolve revisions, cross-series tag changes or any
    other gate. Weighted diluted shares and period-end outstanding shares retain
    distinct scopes; a reviewed borrowing balance is not a lease-inclusive EV.
    """
    if metric not in SHARE_METRICS | DEBT_METRICS or cell["value"] is None:
        return cell
    sources = {_observation_key(s) for s in cell["provenance"]}
    for review in reviews:
        if review["type"] != "filing_scope":
            continue
        observations = {_observation_key(o): o for o in review["observations"] if o["metric"] == metric}
        chosen = [observations.get(key) for key in sources]
        if not chosen or any(o is None for o in chosen) or len({o["scope"] for o in chosen}) != 1:
            continue
        gate = "share_split_and_corporate_action_basis_unverified" if metric in SHARE_METRICS else "debt_scope_requires_filing_review"
        cell["flags"] = sorted((set(cell["flags"]) - {gate}) | {"filing_scope_verified"})
        cell["scope_review"] = {"review_id": review["review_id"], "scope": chosen[0]["scope"],
                                "evidence_source_ids": [s["source_id"] for s in review["evidence"]]}
        if metric in DEBT_METRICS:
            cell["debt_scope"] = chosen[0]["scope"]
        safe = {"filing_scope_verified", "share_split_basis_verified", "historical_fact_split_normalized"}
        cell["model_usable"] = not cell["conflicts"] and set(cell["flags"]) <= safe
        cell["comparison_status"] = "comparable" if cell["model_usable"] else "not_comparable"
        return cell
    return cell


def apply_normalization_reviews(history, canonical_reviews):
    """Merge release evidence into a restored snapshot without replacing facts.

    Returns a validated deep copy. Review IDs are immutable; a different review
    with the same ID is rejected. New or changed facts receive no approval unless
    their full observation identity is explicitly present in the evidence.
    """
    validate_history(history)
    updated = copy.deepcopy(history)
    merged = {r["review_id"]: r for r in updated.get("normalization_reviews", [])}
    for review in canonical_reviews or []:
        old = merged.get(review["review_id"])
        kb.need(old is None or old == review, "normalization review ID has conflicting contents")
        merged[review["review_id"]] = copy.deepcopy(review)
    if list(merged.values()) == updated.get("normalization_reviews", []):
        return updated
    reviews = eligible_normalization_reviews(list(merged.values()), history["cik"], history["as_of"])
    if reviews:
        updated["normalization_reviews"] = reviews
    for review in reviews:
        for evidence in review["evidence"]:
            updated["source_index"][evidence["source_id"]] = {
                "source_id": evidence["source_id"], "source_name": evidence["title"], "source_type": "filing",
                "source_rank": 1, "owner_or_provider": "SEC EDGAR / issuer", "as_of_date": evidence["filed"],
                "retrieved_at": evidence.get("retrieved_at"), "url": evidence["url"],
                "sha256": evidence["sha256"], "freshness_status": "acceptable_for_period"}
    for cells in updated["financials"].values():
        for metric in sorted(cells, key=lambda m: m == "debt_total"):
            cell = cells[metric]
            reconcile_share_split(cell, metric, updated["cik"], updated["as_of"], reviews)
            reconcile_filing_scope(cell, metric, reviews)
    refresh_review_summary(updated)
    validate_history(updated)
    return updated


def refresh_review_summary(history):
    """Recount open evidence gates after exact reviews without erasing other QA."""
    for cells in history['financials'].values():
        propagate_derived_gates(cells)
    groups = {"share_basis_unverified": (SHARE_METRICS, "share_split_and_corporate_action_basis_unverified"),
              "debt_scope_unverified": (DEBT_METRICS, "debt_scope_requires_filing_review")}
    kept = []
    for flag in history["qa_flags"]:
        if flag["code"] in groups:
            metrics, gate = groups[flag["code"]]
            unresolved = {m for m in metrics for cells in history["financials"].values()
                          if cells[m]["value"] is not None and gate in cells[m]["flags"]}
            if unresolved:
                kept.append({**flag, "metrics": sorted(unresolved)})
        elif flag["code"] == "source_value_revision_or_conflict":
            cell = history["financials"][flag["period"]][flag["metric"]]
            if cell["conflicts"] or cell["status"] == "conflicted":
                kept.append(flag)
        else:
            kept.append(flag)
    history["qa_flags"] = kept
    cells = [c for period in history["financials"].values() for c in period.values()]
    history["coverage"].update(
        cell_status_counts=dict(Counter(c["status"] for c in cells)),
        model_usable_cells=sum(c["model_usable"] for c in cells),
        resolved_conflict_cells=sum(bool(c.get("resolved_conflicts")) for c in cells),
        split_normalized_cells=sum("historical_fact_split_normalized" in c["flags"] for c in cells),
        filing_scope_verified_cells=sum(bool(c.get("scope_review")) for c in cells),
        unverified_share_cells=sum("share_split_and_corporate_action_basis_unverified" in c["flags"] for c in cells),
        unverified_debt_cells=sum("debt_scope_requires_filing_review" in c["flags"] for c in cells))


def exact_metric(data, metric, start, end, cutoff, cik, tags=None):
    unit, default_tags = METRICS[metric]
    candidates = []
    for rank, tag in enumerate(default_tags if tags is None else tags):
        for row in source_rows(data, tag, unit, cutoff):
            if row.get("start") == start and row["end"] == end:
                candidates.append((rank, tag, row))
    if not candidates:
        return missing(metric)
    # First respect the latest exact-period source. Preference order resolves
    # overlapping accepted tags in that filing, never an obsolete tag forever.
    latest_filed = max(c[2]["filed"] for c in candidates)
    chosen_rank = min(c[0] for c in candidates if c[2]["filed"] == latest_filed)
    group = [c for c in candidates if c[0] == chosen_rank]
    latest = max(c[2]["filed"] for c in group)
    current = [c for c in group if c[2]["filed"] == latest]
    values = {c[2]["val"] for c in current}
    chosen = sorted(current, key=lambda c: (c[2]["accn"], c[1]))[-1]
    _, tag, row = chosen
    result = {"status": "reported", "value": -row["val"] if metric in {"capex", "purchases_of_productive_assets"} else row["val"],
              "unit": unit, "basis": "US GAAP", "evidence_label": "fact_source_reported", "confidence": "high",
              "model_usable": True, "comparison_status": "comparable", "definition_tag": tag,
              "provenance": [_provenance(row, tag, unit, cik)], "conflicts": [], "flags": []}
    distinct = {}
    for _, other_tag, other in candidates:
        if other_tag == tag and other["val"] != row["val"]:
            key = (other["val"], other["filed"], other["accn"])
            distinct[key] = _provenance(other, other_tag, unit, cik)
    if distinct:
        result["conflicts"] = [{"type": "historical_value_revision_or_context_conflict", "alternatives": list(distinct.values()),
                                "resolution": "Latest filed exact-period value shown; filing-level reconciliation remains required."}]
        result["flags"].append("revision_requires_review")
        result["confidence"] = "medium"
        result["model_usable"] = False
        result["comparison_status"] = "not_comparable"
    alternatives = {}
    for _, other_tag, other in candidates:
        if other_tag != tag and other["val"] != row["val"]:
            key = (other_tag, other["val"], other["filed"], other["accn"])
            alternatives[key] = _provenance(other, other_tag, unit, cik)
    if alternatives:
        result["conflicts"].append({"type": "alternative_tag_definition_conflict", "alternatives": list(alternatives.values()),
                                    "resolution": "Latest filed accepted tag shown; differing alternative definitions are not silently reconciled."})
        result["flags"].append("alternative_tag_scope_differs")
        result["model_usable"] = False
        result["confidence"] = "medium"
        result["comparison_status"] = "not_comparable"
    if len(values) != 1:
        result.update(status="conflicted", value=None, model_usable=False, confidence="low",
                      evidence_label="contradicted_source", comparison_status="not_comparable")
        result["flags"].append("same_date_value_conflict")
    if metric in {"capex", "purchases_of_productive_assets"}:
        result["normalization"] = f"Cash outflow = negative of reported {tag}; source value retained."
    if metric == "purchases_of_productive_assets":
        result["flags"].append("broader_than_property_plant_equipment_only")
        result["note"] = "Productive assets may include intangibles. Kept separate from strict PP&E capex and free_cash_flow."
    if metric in NONADDITIVE or metric == "shares_outstanding":
        result["flags"].append("share_split_and_corporate_action_basis_unverified")
        result["comparison_status"] = "not_comparable"
        result["model_usable"] = False
    if metric.startswith("debt_") or metric == "long_term_debt_total":
        if "CapitalLease" in tag:
            result["debt_scope"] = "includes_capital_or_finance_leases"
        elif tag == "DebtCurrent":
            result["debt_scope"] = "current_debt_as_tagged"
        elif "NotesPayable" in tag:
            result["debt_scope"] = "notes_payable_only"
        else:
            result["debt_scope"] = "long_term_debt_excludes_capital_leases"
        result["flags"].append("debt_scope_requires_filing_review")
        result["model_usable"] = False
    return result


def derived(metric, inputs, value, formula, flags=()):
    if any(x["value"] is None for x in inputs):
        return missing(metric, "A required source input is missing or conflicted; no value was calculated.")
    provenance = list({json.dumps(p, sort_keys=True): p for x in inputs for p in x["provenance"]}.values())
    conflicts = [c for x in inputs for c in x.get("conflicts", [])]
    all_flags = sorted(set(flags) | {f for x in inputs for f in x.get("flags", [])})
    usable = all(x["model_usable"] for x in inputs) and not conflicts
    return {"status": "derived", "value": value, "unit": METRICS[metric][0], "basis": "US GAAP",
            "evidence_label": "derived_calculation", "confidence": "medium", "model_usable": usable,
            "comparison_status": "comparable" if usable else "not_comparable", "provenance": provenance,
            "conflicts": conflicts, "flags": all_flags, "formula": formula,
            "definition_tag": " + ".join(sorted({x.get("definition_tag", "derived") for x in inputs}))}


def standalone_metric(data, metric, period, cutoff, cik):
    direct = exact_metric(data, metric, period["start"], period["end"], cutoff, cik)
    if direct["status"] != "missing_required_source" or period["type"] == "annual":
        return direct
    if metric in NONADDITIVE:
        return missing(metric, "No exact standalone-quarter fact. EPS and weighted-average shares are nonadditive and are never computed as annual/YTD differences.")
    fiscal_start = period.get("fiscal_year_start")
    if not fiscal_start or fiscal_start == period["start"] or "fiscal_start_mismatch" in period["flags"]:
        return direct
    previous_end = (date.fromisoformat(period["start"]) - timedelta(days=1)).isoformat()
    # Pick the same tag and unit for both cumulative inputs; never subtract
    # continuing operations from consolidated cash flow or incompatible tags.
    for tag in METRICS[metric][1]:
        cumulative = exact_metric(data, metric, fiscal_start, period["end"], cutoff, cik, tags=(tag,))
        previous = exact_metric(data, metric, fiscal_start, previous_end, cutoff, cik, tags=(tag,))
        if cumulative["value"] is None or previous["value"] is None:
            continue
        if cumulative["conflicts"] or previous["conflicts"]:
            result = missing(metric, "Quarter derivation blocked: cumulative inputs contain revisions or conflicting values requiring reconciliation.")
            result["provenance"] = cumulative["provenance"] + previous["provenance"]
            result["conflicts"] = cumulative["conflicts"] + previous["conflicts"]
            result["flags"] = ["unreconciled_cumulative_revision"]
            return result
        flags = ["standalone_quarter_from_cumulative_difference"]
        if cumulative["provenance"][0]["accession"] != previous["provenance"][0]["accession"]:
            flags.append("cross_filing_derivation")
        return derived(metric, [cumulative, previous], cumulative["value"] - previous["value"],
                       f"{fiscal_start}..{period['end']} minus {fiscal_start}..{previous_end}; same tag/unit, exact fiscal start.", flags)
    return direct


def fill_derived_metrics(cells):
    if cells["gross_profit"]["status"] == "missing_required_source":
        rev, cost = cells["revenue"], cells["cost_of_revenue"]
        if rev["value"] is not None and cost["value"] is not None:
            a = {p["accession"] for p in rev["provenance"]}
            b = {p["accession"] for p in cost["provenance"]}
            if a == b and "RevenueFromContractWithCustomerIncludingAssessedTax" not in rev.get("definition_tag", ""):
                cells["gross_profit"] = derived("gross_profit", [rev, cost], rev["value"] - cost["value"], "revenue minus cost_of_revenue")
    ocf, capex = cells["operating_cash_flow"], cells["capex"]
    cells["free_cash_flow"] = (derived("free_cash_flow", [ocf, capex], ocf["value"] + capex["value"],
                                      "operating_cash_flow + capex (capex is negative); excludes noncash capex and finance-lease additions")
                               if ocf["value"] is not None and capex["value"] is not None else missing("free_cash_flow"))
    if cells["debt_total"]["status"] != "missing_required_source":
        return
    cur, noncur = cells["debt_current"], cells["debt_noncurrent"]
    total, short = cells["long_term_debt_total"], cells["short_term_borrowings"]
    # DebtCurrent is broader than current maturities of long-term debt. A missing
    # short-term borrowing balance must never be assumed to be zero.
    pair = None
    if cur.get("definition_tag") == "DebtCurrent" and noncur.get("definition_tag") in {"LongTermDebtNoncurrent", "LongTermDebtAndCapitalLeaseObligations"}:
        pair = (cur, noncur, "current debt + noncurrent debt; lease scope requires source review")
    elif total["value"] is not None and short["value"] is not None:
        pair = (total, short, "reported total long-term debt + reported short-term borrowings; lease scope requires source review")
    if pair and all(x["value"] is not None for x in pair[:2]):
        a, b, formula = pair
        if {p["accession"] for p in a["provenance"]} == {p["accession"] for p in b["provenance"]}:
            cells["debt_total"] = derived("debt_total", [a, b], a["value"] + b["value"], formula, ("debt_scope_requires_filing_review",))
            cells["debt_total"]["model_usable"] = False
            cells["debt_total"]["comparison_status"] = "not_comparable"
    if cells["debt_total"]["value"] is None:
        cells["debt_total"]["note"] = "Complete, compatible debt coverage is not established by accepted tags. Missing short-term debt is not zero; long-term principal, carrying value and lease obligations must be reconciled."


def propagate_derived_gates(cells):
    """Later series/scope checks can only close a calculation's eligibility.

    Retain the reported inputs, calculated value and provenance. Never reopen
    an existing gate or reinterpret a standalone cumulative difference.
    """
    for metric, keys in (
        ('free_cash_flow', ('operating_cash_flow', 'capex')),
        ('gross_profit', ('revenue', 'cost_of_revenue')),
        ('debt_total', ('debt_current', 'debt_noncurrent')
            if cells['debt_total'].get('formula', '').startswith('current debt +')
            else ('long_term_debt_total', 'short_term_borrowings')),
    ):
        cell = cells[metric]
        if cell['status'] != 'derived' or cell.get('share_basis'):
            continue
        if metric == 'gross_profit' and cell.get('formula') != 'revenue minus cost_of_revenue':
            continue
        inputs = [cells[key] for key in keys]
        if any(not value['model_usable'] for value in inputs):
            cell['model_usable'] = False
            cell['comparison_status'] = 'not_comparable'
            cell['flags'] = sorted(set(cell['flags']) | {'derived_input_requires_review'} |
                                   {flag for value in inputs for flag in value['flags']})


def normalize_companyfacts(data, company, as_of, source_meta=None, annual_limit=5, quarterly_limit=12, normalization_reviews=None):
    kb.iso_date(as_of, "as_of", required=True)
    cik = str(company["cik"]).zfill(10)
    kb.need(str(data.get("cik", "")).zfill(10) == cik, "companyfacts CIK does not match the requested issuer")
    reviews = eligible_normalization_reviews(normalization_reviews, cik, as_of)
    periods, discovery_issues = discover_periods(data, as_of, annual_limit, quarterly_limit)
    history = {"schema_version": SCHEMA_VERSION, "company_id": "company-cik-" + cik, "ticker": company["ticker"],
               "company_name": data.get("entityName", company.get("company_name")), "cik": cik, "as_of": as_of,
               "source": {"provider": "SEC EDGAR Company Facts", "url": f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json",
                          "retrieved_at": (source_meta or {}).get("fetched_at"), "sha256": (source_meta or {}).get("sha256"),
                          "raw_cache": "build/research-cache/http/objects/" + (source_meta or {}).get("sha256", "unavailable")},
               "support_context": {"owning_workflow": "equity-model-update", "artifact_role": "embedded_support_artifact",
                                   "hidden_unless_requested": True, "readiness_effect": "needs_targeted_fixes",
                                   "decision_impact": "Exact reported historical metrics support research; open revisions, debt coverage and share-basis issues constrain valuation."},
               "units_policy": "Native SEC units: USD, shares, USD/shares; no scaling or FX conversion. Capex is negative cash outflow.",
               "accounting_basis": "US GAAP reported facts only; no adjusted results, forecasts or consensus.",
               "periods": periods, "financials": {}, "source_index": {}, "source_concepts": {}, "qa_flags": [], "validation_checks": [],
               "comparability_bridge": [], "readiness": "partial"}
    if reviews:
        history["normalization_reviews"] = reviews
        for review in reviews:
            for evidence in review["evidence"]:
                history["source_index"][evidence["source_id"]] = {
                    "source_id": evidence["source_id"], "source_name": evidence["title"], "source_type": "filing",
                    "source_rank": 1, "owner_or_provider": "SEC EDGAR / issuer", "as_of_date": evidence["filed"],
                    "retrieved_at": evidence.get("retrieved_at"), "url": evidence["url"],
                    "sha256": evidence["sha256"], "freshness_status": "acceptable_for_period"}
    for period in periods:
        cells = {metric: standalone_metric(data, metric, period, as_of, cik) for metric in DURATION}
        cells.update({metric: exact_metric(data, metric, None, period["end"], as_of, cik) for metric in INSTANT})
        for metric in SHARE_METRICS:
            reconcile_share_split(cells[metric], metric, cik, as_of, reviews)
        for metric in SHARE_METRICS | DEBT_METRICS:
            reconcile_filing_scope(cells[metric], metric, reviews)
        fill_derived_metrics(cells)
        reconcile_filing_scope(cells["debt_total"], "debt_total", reviews)
        history["financials"][period["id"]] = cells
        for metric, cell in cells.items():
            for provenance in cell["provenance"] + [p for c in cell["conflicts"] + cell.get("resolved_conflicts", []) for p in c.get("alternatives", [])]:
                concept_id = provenance["taxonomy"] + ":" + provenance["tag"]
                source_concept = data["facts"][provenance["taxonomy"]][provenance["tag"]]
                history["source_concepts"][concept_id] = {"label": source_concept.get("label"),
                                                          "description": source_concept.get("description"),
                                                          "available_units": sorted(source_concept["units"])}
                sid = provenance["source_id"]
                history["source_index"].setdefault(sid, {"source_id": sid, "source_name": f"{company['ticker']} {provenance['form']} {provenance['accession']}",
                                                "source_type": "filing", "source_rank": 1, "owner_or_provider": "SEC EDGAR / issuer",
                                                "as_of_date": provenance["filed"], "retrieved_at": (source_meta or {}).get("fetched_at"),
                                                "url": provenance["url"], "freshness_status": "acceptable_for_period"})
            if cell["conflicts"] or cell["status"] == "conflicted":
                history["qa_flags"].append({"severity": "high", "period": period["id"], "metric": metric,
                                            "code": "source_value_revision_or_conflict", "impact": "Historical comparison or derived quarter requires filing reconciliation.",
                                            "source_ids": sorted({p["source_id"] for p in cell["provenance"]}), "status": "open"})
        for flag in period["flags"]:
            history["qa_flags"].append({"severity": "high", "period": period["id"], "code": flag,
                                        "impact": "Use exact date boundaries; fiscal-year label is not verified.", "status": "open"})
        checks = history["validation_checks"]
        checks.append({"check": "period_duration", "period": period["id"], "observed_days": days(period["start"], period["end"]),
                       "result": "pass" if ((period["type"] == "annual" and 330 <= days(period["start"], period["end"]) <= 400)
                                            or (period["type"] == "quarterly" and 60 <= days(period["start"], period["end"]) <= 110)) else "fail"})
        rev, cost, gross = (cells[m] for m in ("revenue", "cost_of_revenue", "gross_profit"))
        if all(x["value"] is not None for x in (rev, cost, gross)):
            variance = rev["value"] - cost["value"] - gross["value"]
            ok = abs(variance) <= max(1, abs(rev["value"]) * 1e-9)
            checks.append({"check": "revenue_less_cost_equals_gross_profit", "period": period["id"], "variance": variance, "result": "pass" if ok else "fail"})
            if not ok:
                history["qa_flags"].append({"severity": "high", "period": period["id"], "code": "gross_profit_tieout_failed", "variance": variance, "status": "open"})
                for metric in ("revenue", "cost_of_revenue", "gross_profit"):
                    cells[metric]["flags"].append("gross_profit_tieout_failed")
                    cells[metric]["model_usable"] = False
                    cells[metric]["comparison_status"] = "not_comparable"
    for kind in ("annual", "quarterly"):
        for metric in METRICS:
            series = [(p, history["financials"][p["id"]][metric]) for p in periods if p["type"] == kind]
            tags = {c.get("definition_tag") for _, c in series if c["value"] is not None}
            # A derived difference of a single tag retains that tag. Mixed tags
            # need a manual disclosure bridge; no unsupported automatic recast.
            if len(tags) > 1:
                history["comparability_bridge"].append({"metric": metric, "period_type": kind, "source_definitions": sorted(t for t in tags if t),
                                                        "comparison_status": "not_comparable", "model_treatment": "Review tag and presentation changes before cross-period modeling."})
                for _, cell in series:
                    if cell["value"] is not None:
                        cell["flags"].append("definition_changed_across_series")
                        cell["comparison_status"] = "not_comparable"
                        cell["model_usable"] = False
                history["qa_flags"].append({"severity": "high", "metric": metric, "period_type": kind,
                                            "code": "definition_changed_across_series", "status": "open",
                                            "impact": "Use the comparability bridge; a source-tag change has not been reconciled."})
    for metric_group, code, impact in [
        (set(NONADDITIVE) | {"shares_outstanding"}, "share_basis_unverified", "Per-share and share-count histories require a corporate-action review before valuation or cross-period modeling."),
        ({"debt_total", "debt_current", "debt_noncurrent", "long_term_debt_total"}, "debt_scope_unverified", "Debt amounts must be reconciled for lease coverage, complete borrowing scope and carrying value before an enterprise-value bridge.")]:
        unresolved_metrics = {m for m in metric_group for cells in history["financials"].values()
                              if cells[m]["value"] is not None and
                              (code != "share_basis_unverified" or "share_split_and_corporate_action_basis_unverified" in cells[m]["flags"])}
        if unresolved_metrics:
            history["qa_flags"].append({"severity": "high", "code": code, "metrics": sorted(unresolved_metrics),
                                        "impact": impact, "status": "open"})
    counts = Counter(c["status"] for cells in history["financials"].values() for c in cells.values())
    history["coverage"] = {"annual_periods": sum(p["type"] == "annual" for p in periods),
                           "quarterly_periods": sum(p["type"] == "quarterly" for p in periods), "metric_count": len(METRICS),
                           "cell_status_counts": dict(counts), "latest_period_end": max((p["end"] for p in periods), default=None),
                           "latest_filed_date": max((s["as_of_date"] for s in history["source_index"].values()), default=None)}
    missing_by_metric = {m: sum(cells[m]["value"] is None for cells in history["financials"].values()) for m in METRICS}
    history["coverage"]["missing_by_metric"] = {m: count for m, count in missing_by_metric.items() if count}
    history["coverage"]["model_usable_cells"] = sum(c["model_usable"] for cells in history["financials"].values() for c in cells.values())
    history["coverage"]["resolved_conflict_cells"] = sum(bool(c.get("resolved_conflicts")) for cells in history["financials"].values() for c in cells.values())
    history["coverage"]["split_normalized_cells"] = sum("historical_fact_split_normalized" in c["flags"] for cells in history["financials"].values() for c in cells.values())
    history["qa_flags"].append({"severity": "medium", "code": "incomplete_selected_metric_coverage",
                                "missing_by_metric": history["coverage"]["missing_by_metric"], "status": "open",
                                "impact": "Missing cells are not zero; source the relevant filing and exact definition before modeling."})
    history["limitations"] = ["Company Facts excludes custom taxonomy and dimensional/segment facts; absent data is not zero.",
                              "Company Facts does not carry the full filing context. Revisions may reflect restatements, stock splits, scope changes or tagging differences; flagged revisions are not automatically reconciled.",
                              "Fiscal labels come from primary filing focus and annual boundaries; SEC calendar frames are retained only as provenance.",
                              "Standalone quarters derived from cumulative values use exact matching fiscal starts/tags/units; cross-filing inputs are disclosed. EPS and weighted-average shares are never subtracted.",
                              "Debt lease coverage, short-term borrowings, principal versus carrying value, and unverified share cells require filing-level review before valuation. Explicit split and scope reviews cover exact approved observations only. Weighted-average diluted shares and period-end outstanding shares are separate concepts, and neither is a current quote-date share count.",
                              "Cash excludes marketable securities unless independently presented as short_term_investments. Cash plus investments is not assumed to be unrestricted cash.",
                              "This is a selected historical metric schedule, not complete statements, a three-statement model, consensus, forecasts or a valuation.",
                              "Full balance-sheet and cash-flow reconciliations are outside the selected metric scope and have not been performed."]
    if discovery_issues:
        history["period_discovery_issues"] = discovery_issues
    refresh_review_summary(history)
    validate_history(history)
    history["validation_checks"].append({"check": "schema_provenance_units_cutoff_and_quarter_boundaries", "result": "pass"})
    return history


def validate_calculation(metric, cell, cells, period):
    """Recompute supported formulas without executing a persisted expression."""
    if cell['status'] != 'derived' or cell.get('share_basis'):
        return
    formula = cell.get('formula', '')
    inputs = []
    if metric == 'free_cash_flow':
        inputs = [cells['operating_cash_flow'], cells['capex']]
        value = sum(c['value'] for c in inputs if c['value'] is not None)
    elif metric == 'gross_profit' and formula == 'revenue minus cost_of_revenue':
        inputs = [cells['revenue'], cells['cost_of_revenue']]
        value = (inputs[0]['value'] or 0) - (inputs[1]['value'] or 0)
    elif metric == 'debt_total':
        keys = (['debt_current', 'debt_noncurrent'] if formula.startswith('current debt +') else
                ['long_term_debt_total', 'short_term_borrowings'] if formula.startswith('reported total long-term debt +') else [])
        kb.need(bool(keys), 'unknown debt calculation')
        inputs = [cells[k] for k in keys]
        value = sum(c['value'] for c in inputs if c['value'] is not None)
    else:
        sources = cell['provenance']
        kb.need('standalone_quarter_from_cumulative_difference' in cell['flags'] and len(sources) == 2,
                'unknown derived calculation')
        current, previous = sources
        kb.need(metric not in NONADDITIVE and period['type'] == 'quarterly'
                and current['tag'] == previous['tag'] and current['start'] == previous['start']
                and current['end'] == period['end'] and next_day(previous['end']) == period['start'],
                'invalid cumulative quarter inputs')
        value = current['source_value'] - previous['source_value']
        if metric in {'capex', 'purchases_of_productive_assets'}:
            value = -value
    if inputs:
        kb.need(all(c['value'] is not None for c in inputs), 'derived calculation has missing inputs')
        kb.need(not cell['model_usable'] or all(c['model_usable'] for c in inputs), 'derived eligibility exceeds inputs')
        expected = {json.dumps(s, sort_keys=True) for c in inputs for s in c['provenance']}
        kb.need({json.dumps(s, sort_keys=True) for s in cell['provenance']} == expected, 'derived provenance differs from inputs')
    kb.need(math.isclose(cell['value'], value, rel_tol=1e-12, abs_tol=1e-9), 'derived value differs from source calculation')


def validate_refresh(previous, candidate):
    """Fail closed on truncated/empty successful downloads, retaining the checkpoint."""
    validate_history(candidate)
    kb.need(bool(candidate['periods']), 'financial response contains no supported periods')
    if not previous:
        return
    kb.need((candidate['cik'], candidate['ticker']) == (previous['cik'], previous['ticker']), 'refresh issuer mismatch')
    for kind in ('annual', 'quarterly'):
        old = sorted((p for p in previous['periods'] if p['type'] == kind), key=lambda p: p['end'])
        new = sorted((p for p in candidate['periods'] if p['type'] == kind), key=lambda p: p['end'])
        kb.need(len(new) >= len(old) and (not old or new[-1]['end'] >= old[-1]['end']), 'financial response lost periods')
    new_ids = set(candidate['financials'])
    for period, cells in previous['financials'].items():
        if period in new_ids:
            for metric, cell in cells.items():
                replacement = candidate['financials'][period][metric]
                kb.need(cell['value'] is None or replacement['status'] != 'missing_required_source',
                        'financial response lost a previously available source: ' + period + ':' + metric)


def validate_history(history):
    kb.need(history.get("schema_version") == SCHEMA_VERSION, "unsupported financial history schema")
    kb.iso_date(history["as_of"], "as_of", required=True)
    kb.need(bool(re.fullmatch(r'\d{10}', history['cik'])) and history['company_id'] == 'company-cik-' + history['cik'],
            'financial history issuer identity mismatch')
    kb.need(set(history['financials']) == {p['id'] for p in history['periods']}, 'financial period maps differ')
    reviews = eligible_normalization_reviews(history.get("normalization_reviews", []), history["cik"], history["as_of"])
    kb.need(reviews == history.get("normalization_reviews", []), "financial history contains future normalization evidence")
    review_by_id = {r["review_id"]: r for r in reviews}
    for review in reviews:
        for evidence in review["evidence"]:
            indexed = history["source_index"].get(evidence["source_id"], {})
            kb.need(indexed.get("sha256") == evidence["sha256"] and indexed.get("url") == evidence["url"]
                    and indexed.get("as_of_date") == evidence["filed"], "normalization evidence binding mismatch")
    ids = set()
    for p in history["periods"]:
        kb.need(p["id"] not in ids, "duplicate normalized period")
        ids.add(p["id"])
        kb.need(p['type'] in {'annual', 'quarterly'} and p['id'] == p['type'] + ':' + p['end'], 'invalid period identity')
        kb.need(set(history['financials'][p['id']]) == set(METRICS), 'incomplete metric map')
        kb.need(p["end"] <= history["as_of"] and p["start"] <= p["end"], "invalid normalized period")
        if p["type"] == "quarterly":
            kb.need(60 <= days(p["start"], p["end"]) <= 110, "YTD must not be labeled quarterly")
        else:
            kb.need(330 <= days(p['start'], p['end']) <= 400, 'invalid annual duration')
        for metric, cell in history["financials"][p["id"]].items():
            kb.need(metric in METRICS and cell["unit"] == METRICS[metric][0], "metric unit mismatch")
            kb.need(cell["basis"] == "US GAAP", "adjusted and GAAP financials must remain separate")
            kb.need(cell['status'] in {'reported', 'derived', 'conflicted', 'missing_required_source'}, 'unknown cell status')
            kb.need((cell['value'] is not None) == (cell['status'] in {'reported', 'derived'}), 'status/value mismatch')
            blocked = {'share_split_and_corporate_action_basis_unverified', 'debt_scope_requires_filing_review',
                       'definition_changed_across_series', 'gross_profit_tieout_failed', 'unreconciled_cumulative_revision'}
            kb.need(type(cell['model_usable']) is bool and (not cell['model_usable'] or
                    (cell['value'] is not None and not cell['conflicts'] and not blocked.intersection(cell['flags'])
                     and cell['comparison_status'] == 'comparable')), 'unsafe model eligibility')
            if cell["value"] is not None:
                kb.need(isinstance(cell["value"], (int, float)) and not isinstance(cell['value'], bool)
                        and math.isfinite(cell["value"]), "nonfinite normalized value")
                kb.need(bool(cell["provenance"]), "normalized value has no provenance")
                validate_calculation(metric, cell, history['financials'][p['id']], p)
            if cell.get("share_basis"):
                basis = cell["share_basis"]
                kb.need(basis["review_id"] in review_by_id, "unindexed share normalization review")
                kb.need(all(s in history["source_index"] for s in cell["share_basis"]["evidence_source_ids"]), "unindexed split evidence")
                review = review_by_id[basis["review_id"]]
                kb.need(basis["evidence_source_ids"] == [s["source_id"] for s in review["evidence"]],
                        "split evidence identity mismatch")
                observations = {_observation_key(o): o for o in review["observations"]}
                observation = observations.get(_observation_key(cell["provenance"][0]))
                kb.need(observation is not None, "normalized share fact is outside its reviewed source observations")
                kb.need(review["type"] == "stock_split" and metric in SHARE_METRICS and basis["basis"] == "post_split"
                        and basis["new_shares_per_old_share"] == review["new_shares_per_old_share"]
                        and basis["source_basis"] == observation["split_basis"], "share normalization basis mismatch")
                factor = 1
                if observation["split_basis"] == "pre_split":
                    factor = 1 / review["new_shares_per_old_share"] if metric.startswith("eps_") else review["new_shares_per_old_share"]
                    kb.need(cell["status"] == "derived" and cell["evidence_label"] == "derived_calculation", "split adjustment must be labeled as derived")
                kb.need(math.isclose(cell["value"], observation["source_value"] * factor, rel_tol=1e-12, abs_tol=1e-12),
                        "normalized share value does not match its source and split factor")
                for conflict in cell.get("resolved_conflicts", []):
                    kb.need(conflict.get("review_id") == review["review_id"]
                            and conflict["type"] == "historical_value_revision_or_context_conflict",
                            "unsupported split conflict resolution")
                    for source in conflict.get("alternatives", []):
                        alternative = observations.get(_observation_key(source))
                        kb.need(alternative is not None and alternative["split_basis"] != observation["split_basis"],
                                "split resolution has unreviewed or same-basis alternative")
                        alt_factor = (1 / review["new_shares_per_old_share"] if metric.startswith("eps_")
                                      else review["new_shares_per_old_share"]) if alternative["split_basis"] == "pre_split" else 1
                        tolerance = 0.5 * (10 ** -observation["decimals"] * factor + 10 ** -alternative["decimals"] * alt_factor)
                        kb.need(abs(observation["source_value"] * factor - alternative["source_value"] * alt_factor) <= tolerance + 1e-9,
                                "split resolution does not reconcile source rounding intervals")
            if cell.get("scope_review"):
                scope = cell["scope_review"]
                review = review_by_id.get(scope.get("review_id"))
                kb.need(review is not None and review["type"] == "filing_scope", "unindexed filing scope review")
                observations = {_observation_key(o): o for o in review["observations"] if o["metric"] == metric}
                bound = [observations.get(_observation_key(s)) for s in cell["provenance"]]
                kb.need(bound and all(o is not None and o["scope"] == scope["scope"] for o in bound),
                        "fact is outside its reviewed scope observations")
                kb.need(scope["evidence_source_ids"] == [e["source_id"] for e in review["evidence"]],
                        "scope evidence identity mismatch")
                for evidence in review["evidence"]:
                    indexed = history["source_index"].get(evidence["source_id"], {})
                    kb.need(indexed.get("sha256") == evidence["sha256"] and indexed.get("url") == evidence["url"]
                            and indexed.get("as_of_date") == evidence["filed"], "unindexed filing scope evidence")
            if cell["model_usable"] and metric in SHARE_METRICS | DEBT_METRICS:
                kb.need(bool(cell.get("share_basis") or cell.get("scope_review")),
                        "share or debt eligibility requires exact bound review evidence")
            for source in cell["provenance"]:
                kb.need(isinstance(source['source_value'], (int, float)) and not isinstance(source['source_value'], bool)
                        and math.isfinite(source['source_value']), 'invalid source number')
                kb.need(source['source_id'] == 'SEC-' + source['accession']
                        and source['url'] == filing_url(history['cik'], source['accession']), 'source identity mismatch')
                kb.need(source["source_id"] in history["source_index"], "unindexed source")
                kb.need(source["filed"] <= history["as_of"] and source["unit"] == cell["unit"], "future source or wrong unit")
                if cell["status"] == "reported":
                    expected_start = p["start"] if metric in DURATION else None
                    kb.need(source["start"] == expected_start and source["end"] == p["end"], "reported fact does not match the exact period")
                    expected = -source['source_value'] if metric in {'capex', 'purchases_of_productive_assets'} else source['source_value']
                    kb.need(cell['value'] == expected, 'reported number differs from source')
            for conflict in cell["conflicts"] + cell.get("resolved_conflicts", []):
                for source in conflict.get("alternatives", []):
                    kb.need(source["source_id"] in history["source_index"], "unindexed alternative source")
                    kb.need(source["filed"] <= history["as_of"] and source["unit"] == cell["unit"], "future alternative source or wrong unit")
    return True


def load_history(root, ticker):
    """Load a persisted issuer schedule; missing file returns None, corrupt data raises."""
    ticker = ticker.upper()
    kb.need(bool(kb.TICKER.fullmatch(ticker)), "invalid ticker")
    path = Path(root) / "research" / "financials" / f"{ticker}.json"
    if not path.exists():
        return None
    history = rp.read_json(path)
    validate_history(history)
    kb.need(history["ticker"] == ticker, "financial history issuer mismatch")
    return history


def get_metric(history, metric, period_type="annual", period_end=None, *, period_start=None, fiscal_year=None, fiscal_quarter=None):
    """Return an exact metric cell plus period metadata; None for absent period.

    Omitting all date/fiscal filters explicitly selects the latest stored period
    of the requested type. Missing/conflicted values retain their null and status.
    No fuzzy fallback, latest-price lookup, annualization, or fiscal inference.
    """
    if history is None:
        return None
    if metric not in METRICS:
        raise ValueError(f"Unsupported financial metric: {metric}")
    if period_type not in {"annual", "quarterly"}:
        raise ValueError("period_type must be annual or quarterly")
    matches = [p for p in history["periods"] if p["type"] == period_type
               and (period_end is None or p["end"] == period_end)
               and (period_start is None or p["start"] == period_start)
               and (fiscal_year is None or p["fiscal_year"] == fiscal_year)
               and (fiscal_quarter is None or p["fiscal_quarter"] == fiscal_quarter)]
    if not matches:
        return None
    p = max(matches, key=lambda x: x["end"])
    return {**history["financials"][p["id"]][metric], "metric": metric, "period": p,
            "ticker": history["ticker"], "as_of": history["as_of"]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=kb.ROOT)
    parser.add_argument("--ticker", action="append", help="Repeat for selected tickers; default is the configured universe.")
    parser.add_argument("--as-of", required=True, help="Only use sources filed on or before this ISO date.")
    parser.add_argument("--refresh", action="store_true", help="Refresh SEC Company Facts rather than reuse the content-addressed cache.")
    parser.add_argument("--annual-periods", type=int, default=5)
    parser.add_argument("--quarterly-periods", type=int, default=12)
    args = parser.parse_args()
    try:
        kb.iso_date(args.as_of, "as_of", required=True)
        kb.need(1 <= args.annual_periods <= 10 and 1 <= args.quarterly_periods <= 40, "invalid history depth")
        companies = rp.universe(args.root)
        if args.ticker:
            wanted = {t.upper() for t in args.ticker}
            kb.need(wanted <= {c["ticker"] for c in companies}, "ticker is outside the configured universe")
            companies = [c for c in companies if c["ticker"] in wanted]
        fetcher = rp.Fetcher(args.root, os.environ.get("SEC_USER_AGENT", ""))
        failed = False
        for company in companies:
            try:
                raw, meta = fetcher.fetch(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{company['cik']}.json", refresh=args.refresh)
                previous = load_history(args.root, company["ticker"])
                history = normalize_companyfacts(json.loads(raw), company, args.as_of, meta, args.annual_periods, args.quarterly_periods,
                                                 normalization_reviews=(previous or {}).get("normalization_reviews", []))
                rp.write_json(args.root / "research/financials" / f"{company['ticker']}.json", history)
                print(json.dumps({"ticker": company["ticker"], "coverage": history["coverage"], "qa_flags": len(history["qa_flags"])}), flush=True)
            except (ValueError, OSError) as error:
                failed = True
                print(f"ERROR {company['ticker']}: {error}; existing schedule preserved", file=sys.stderr)
        return 1 if failed else 0
    except (ValueError, OSError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
