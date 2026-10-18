#!/usr/bin/env python3
"""Collect conservative, source-linked annual and standalone-quarter SEC financials.

No calendar-frame inference, estimates, paid APIs, or missing-to-zero coercion.
The source cache is maintained by research_pipeline.Fetcher under ignored build/.
"""
from __future__ import annotations

import argparse
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


def normalize_companyfacts(data, company, as_of, source_meta=None, annual_limit=5, quarterly_limit=12):
    kb.iso_date(as_of, "as_of", required=True)
    cik = str(company["cik"]).zfill(10)
    kb.need(str(data.get("cik", "")).zfill(10) == cik, "companyfacts CIK does not match the requested issuer")
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
    for period in periods:
        cells = {metric: standalone_metric(data, metric, period, as_of, cik) for metric in DURATION}
        cells.update({metric: exact_metric(data, metric, None, period["end"], as_of, cik) for metric in INSTANT})
        fill_derived_metrics(cells)
        history["financials"][period["id"]] = cells
        for metric, cell in cells.items():
            for provenance in cell["provenance"] + [p for c in cell["conflicts"] for p in c.get("alternatives", [])]:
                concept_id = provenance["taxonomy"] + ":" + provenance["tag"]
                source_concept = data["facts"][provenance["taxonomy"]][provenance["tag"]]
                history["source_concepts"][concept_id] = {"label": source_concept.get("label"),
                                                          "description": source_concept.get("description"),
                                                          "available_units": sorted(source_concept["units"])}
                sid = provenance["source_id"]
                history["source_index"][sid] = {"source_id": sid, "source_name": f"{company['ticker']} {provenance['form']} {provenance['accession']}",
                                                "source_type": "filing", "source_rank": 1, "owner_or_provider": "SEC EDGAR / issuer",
                                                "as_of_date": provenance["filed"], "retrieved_at": (source_meta or {}).get("fetched_at"),
                                                "url": provenance["url"], "freshness_status": "acceptable_for_period"}
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
        if any(cells[m]["value"] is not None for cells in history["financials"].values() for m in metric_group):
            history["qa_flags"].append({"severity": "high", "code": code, "metrics": sorted(metric_group),
                                        "impact": impact, "status": "open"})
    counts = Counter(c["status"] for cells in history["financials"].values() for c in cells.values())
    history["coverage"] = {"annual_periods": sum(p["type"] == "annual" for p in periods),
                           "quarterly_periods": sum(p["type"] == "quarterly" for p in periods), "metric_count": len(METRICS),
                           "cell_status_counts": dict(counts), "latest_period_end": max((p["end"] for p in periods), default=None),
                           "latest_filed_date": max((s["as_of_date"] for s in history["source_index"].values()), default=None)}
    missing_by_metric = {m: sum(cells[m]["value"] is None for cells in history["financials"].values()) for m in METRICS}
    history["coverage"]["missing_by_metric"] = {m: count for m, count in missing_by_metric.items() if count}
    history["qa_flags"].append({"severity": "medium", "code": "incomplete_selected_metric_coverage",
                                "missing_by_metric": history["coverage"]["missing_by_metric"], "status": "open",
                                "impact": "Missing cells are not zero; source the relevant filing and exact definition before modeling."})
    history["limitations"] = ["Company Facts excludes custom taxonomy and dimensional/segment facts; absent data is not zero.",
                              "Company Facts does not carry the full filing context. Revisions may reflect restatements, stock splits, scope changes or tagging differences; flagged revisions are not automatically reconciled.",
                              "Fiscal labels come from primary filing focus and annual boundaries; SEC calendar frames are retained only as provenance.",
                              "Standalone quarters derived from cumulative values use exact matching fiscal starts/tags/units; cross-filing inputs are disclosed. EPS and weighted-average shares are never subtracted.",
                              "Debt lease coverage, short-term borrowings, principal versus carrying value, and share split basis require filing-level review before valuation.",
                              "Cash excludes marketable securities unless independently presented as short_term_investments. Cash plus investments is not assumed to be unrestricted cash.",
                              "This is a selected historical metric schedule, not complete statements, a three-statement model, consensus, forecasts or a valuation.",
                              "Full balance-sheet and cash-flow reconciliations are outside the selected metric scope and have not been performed."]
    if discovery_issues:
        history["period_discovery_issues"] = discovery_issues
    validate_history(history)
    history["validation_checks"].append({"check": "schema_provenance_units_cutoff_and_quarter_boundaries", "result": "pass"})
    return history


def validate_history(history):
    kb.need(history.get("schema_version") == SCHEMA_VERSION, "unsupported financial history schema")
    kb.iso_date(history["as_of"], "as_of", required=True)
    ids = set()
    for p in history["periods"]:
        kb.need(p["id"] not in ids, "duplicate normalized period")
        ids.add(p["id"])
        kb.need(p["end"] <= history["as_of"] and p["start"] <= p["end"], "invalid normalized period")
        if p["type"] == "quarterly":
            kb.need(60 <= days(p["start"], p["end"]) <= 110, "YTD must not be labeled quarterly")
        for metric, cell in history["financials"][p["id"]].items():
            kb.need(metric in METRICS and cell["unit"] == METRICS[metric][0], "metric unit mismatch")
            kb.need(cell["basis"] == "US GAAP", "adjusted and GAAP financials must remain separate")
            if cell["value"] is not None:
                kb.need(isinstance(cell["value"], (int, float)) and math.isfinite(cell["value"]), "nonfinite normalized value")
                kb.need(bool(cell["provenance"]), "normalized value has no provenance")
            for source in cell["provenance"]:
                kb.need(source["source_id"] in history["source_index"], "unindexed source")
                kb.need(source["filed"] <= history["as_of"] and source["unit"] == cell["unit"], "future source or wrong unit")
                if cell["status"] == "reported":
                    expected_start = p["start"] if metric in DURATION else None
                    kb.need(source["start"] == expected_start and source["end"] == p["end"], "reported fact does not match the exact period")
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
                history = normalize_companyfacts(json.loads(raw), company, args.as_of, meta, args.annual_periods, args.quarterly_periods)
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
