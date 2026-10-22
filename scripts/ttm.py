"""Source-linked trailing-twelve-month schedules from normalized quarter cells.

The caller should first validate the history with financial_history.validate_history.
This module adds a separate cross-quarter eligibility gate. It never substitutes an
older four-quarter window, annualizes a short period, or sums per-share quantities.
"""
from __future__ import annotations

from copy import deepcopy
from datetime import date, timedelta
import json
import math


FLOW_METRICS = (
    "revenue", "gross_profit", "cost_of_revenue", "operating_income", "net_income",
    "net_income_common", "net_income_including_noncontrolling_interests",
    "operating_cash_flow", "capex", "purchases_of_productive_assets",
    "stock_based_compensation", "free_cash_flow",
)
BALANCE_METRICS = (
    "cash_and_equivalents", "short_term_investments", "debt_current",
    "debt_noncurrent", "long_term_debt_total", "short_term_borrowings",
    "debt_total", "shares_outstanding",
)
RATIOS = {
    "gross_margin": "gross_profit", "operating_margin": "operating_income",
    "net_margin": "net_income", "fcf_margin": "free_cash_flow",
    "sbc_to_revenue": "stock_based_compensation",
}
BLOCKING_FLAGS = {
    "revision_requires_review", "unreconciled_cumulative_revision",
    "definition_changed_across_series", "alternative_tag_scope_differs",
    "gross_profit_tieout_failed", "debt_scope_requires_filing_review",
    "share_split_and_corporate_action_basis_unverified",
}


def _date(value):
    parsed = date.fromisoformat(value)
    if parsed.isoformat() != value:
        raise ValueError("Dates must use YYYY-MM-DD.")
    return parsed


def _finite(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def _confidence(cells):
    levels = ("low", "medium", "high")
    return levels[min(levels.index(c.get("confidence")) if c.get("confidence") in levels else 0 for c in cells)]


def _unique(rows):
    return list({json.dumps(row, sort_keys=True, ensure_ascii=False): deepcopy(row) for row in rows}.values())


def _missing(reasons, *, unit="USD", provenance=(), inputs=()):
    return {
        "status": "missing_required_source", "value": None, "unit": unit,
        "basis": "US GAAP", "evidence_label": "missing_required_source",
        "confidence": "low", "model_usable": False,
        "comparison_status": "not_comparable", "provenance": _unique(provenance),
        "conflicts": [], "flags": sorted(set(reasons)), "inputs": list(inputs),
        "source_urls": sorted({p["url"] for p in provenance if p.get("url")}),
        "note": "The exact selected period lacks complete, compatible, reviewed inputs.",
    }


def _window(history):
    """Select latest quarters before checking them; failure never shifts the window."""
    issues = []
    try:
        cutoff = _date(history["as_of"])
        quarters = [p for p in history.get("periods", []) if p.get("type") == "quarterly"]
        for p in quarters:
            _date(p["start"])
            _date(p["end"])
        quarters.sort(key=lambda p: (p["end"], p["start"], p.get("id", "")))
    except (KeyError, TypeError, ValueError):
        return [], ["invalid_period_metadata"]
    selected = quarters[-4:]
    if len(selected) != 4:
        issues.append("four_quarters_required")
    if len({p.get("id") for p in quarters}) != len(quarters) or len({(p["start"], p["end"]) for p in quarters}) != len(quarters):
        issues.append("duplicate_quarter")
    for p in selected:
        start, end = _date(p["start"]), _date(p["end"])
        if p.get("id") != "quarterly:" + p["end"] or not 60 <= (end - start).days + 1 <= 110:
            issues.append("not_a_standalone_quarter")
        if end > cutoff:
            issues.append("period_after_cutoff")
        fy, fq = p.get("fiscal_year"), p.get("fiscal_quarter")
        if type(fy) is not int or type(fq) is not int or fq not in (1, 2, 3, 4) or p.get("flags"):
            issues.append("quarter_identity_unverified")
    for prior, current in zip(selected, selected[1:]):
        if _date(prior["end"]) + timedelta(days=1) != _date(current["start"]):
            issues.append("nonconsecutive_quarters")
        if not any(type(p.get(k)) is not int for p in (prior, current) for k in ("fiscal_year", "fiscal_quarter")):
            expected_q = prior["fiscal_quarter"] % 4 + 1
            expected_y = prior["fiscal_year"] + (prior["fiscal_quarter"] == 4)
            if (current["fiscal_year"], current["fiscal_quarter"]) != (expected_y, expected_q):
                issues.append("inconsistent_fiscal_sequence")
    if len(selected) == 4 and not 330 <= (_date(selected[-1]["end"]) - _date(selected[0]["start"])).days + 1 <= 400:
        issues.append("invalid_ttm_duration")
    return selected, sorted(set(issues))


def _cell_reasons(history, period, metric, cell, *, instant=False):
    reasons = []
    unit = "shares" if metric == "shares_outstanding" else "USD"
    if not isinstance(cell, dict) or not _finite(cell.get("value")):
        return ["missing_quarter_value"]
    if cell.get("status") not in ("reported", "derived") or cell.get("model_usable") is not True or cell.get("comparison_status") != "comparable":
        reasons.append("quarter_not_model_usable")
    if cell.get("conflicts") or BLOCKING_FLAGS.intersection(cell.get("flags", [])):
        reasons.append("unresolved_source_or_definition_conflict")
    if cell.get("unit") != unit or cell.get("basis") != "US GAAP":
        reasons.append("incompatible_unit_or_basis")
    if not cell.get("definition_tag"):
        reasons.append("missing_metric_definition")
    sources = cell.get("provenance", [])
    if not sources:
        reasons.append("missing_source_provenance")
    for source in sources:
        try:
            end, filed, cutoff = _date(source["end"]), _date(source["filed"]), _date(history["as_of"])
            indexed = history.get("source_index", {}).get(source["source_id"])
            if not indexed:
                reasons.append("unindexed_source")
            elif indexed.get("as_of_date") and _date(indexed["as_of_date"]) > cutoff:
                reasons.append("source_after_cutoff")
            if filed > cutoff or end > filed:
                reasons.append("source_after_cutoff")
            if source.get("unit") != unit or not source.get("taxonomy") or not source.get("tag"):
                reasons.append("source_definition_mismatch")
            if not isinstance(source.get("url"), str) or not source["url"].startswith("https://"):
                reasons.append("missing_source_url")
            if instant:
                if source.get("start") is not None or source["end"] != period["end"]:
                    reasons.append("balance_date_mismatch")
            elif cell.get("status") == "reported":
                if source.get("start") != period["start"] or source["end"] != period["end"]:
                    reasons.append("source_period_mismatch")
            elif end > _date(period["end"]) or (source.get("start") and _date(source["start"]) > end):
                reasons.append("source_period_mismatch")
        except (KeyError, TypeError, ValueError):
            reasons.append("invalid_source_metadata")
    return sorted(set(reasons))


def _flow(history, periods, metric):
    cells = [history.get("financials", {}).get(p["id"], {}).get(metric) for p in periods]
    sources = [s for c in cells if isinstance(c, dict) for s in c.get("provenance", [])]
    reasons = [reason for p, c in zip(periods, cells) for reason in _cell_reasons(history, p, metric, c)]
    inputs = [{"period_id": p["id"], "start": p["start"], "end": p["end"],
               "value": c.get("value") if c else None, "status": c.get("status") if c else "missing_required_source",
               "source_ids": sorted({s["source_id"] for s in (c or {}).get("provenance", []) if s.get("source_id")})}
              for p, c in zip(periods, cells)]
    signatures = {(c.get("unit"), c.get("basis"), c.get("definition_tag"),
                   tuple(sorted({s.get("taxonomy", "") for s in c.get("provenance", [])})))
                  for c in cells if isinstance(c, dict) and c.get("value") is not None}
    if len(signatures) != 1:
        reasons.append("incompatible_quarter_definitions")
    if reasons:
        return _missing(reasons, provenance=sources, inputs=inputs)
    try:
        value = math.fsum(c["value"] for c in cells)
    except OverflowError:
        return _missing(["nonfinite_ttm_sum"], provenance=sources, inputs=inputs)
    if not math.isfinite(value):
        return _missing(["nonfinite_ttm_sum"], provenance=sources, inputs=inputs)
    return {
        "status": "derived", "value": value, "unit": "USD", "basis": cells[0]["basis"],
        "evidence_label": "derived_calculation", "confidence": _confidence(cells),
        "model_usable": True, "comparison_status": "comparable", "provenance": _unique(sources),
        "conflicts": [], "flags": sorted({f for c in cells for f in c.get("flags", [])}),
        "formula": " + ".join(p["id"] + ":" + metric for p in periods),
        "definition_tag": cells[0]["definition_tag"], "inputs": inputs,
        "source_urls": sorted({s["url"] for s in sources}),
        "note": "Sum of four consecutive standalone quarters; no annualization or earlier-period substitution.",
    }


def _ratio(financials, numerator):
    a, b = financials[numerator], financials["revenue"]
    sources = a.get("provenance", []) + b.get("provenance", [])
    if not a["model_usable"] or not b["model_usable"]:
        return _missing(["ratio_inputs_not_usable"], unit="ratio", provenance=sources)
    if b["value"] <= 0:
        return _missing(["nonpositive_revenue_denominator"], unit="ratio", provenance=sources)
    if a["unit"] != b["unit"] or a["basis"] != b["basis"]:
        return _missing(["ratio_inputs_incompatible"], unit="ratio", provenance=sources)
    value = a["value"] / b["value"]
    if not math.isfinite(value):
        return _missing(["nonfinite_ratio"], unit="ratio", provenance=sources)
    return {
        "status": "derived", "value": value, "unit": "ratio", "basis": a["basis"],
        "evidence_label": "derived_calculation", "confidence": _confidence((a, b)), "model_usable": True,
        "comparison_status": "comparable", "provenance": _unique(sources), "conflicts": [], "flags": [],
        "formula": "TTM " + numerator + " / TTM revenue",
        "definition_tag": a["definition_tag"] + " / " + b["definition_tag"],
        "inputs": [{"metric": numerator, "value": a["value"]}, {"metric": "revenue", "value": b["value"]}],
        "source_urls": sorted({s["url"] for s in sources if s.get("url")}),
    }


def build_ttm(history):
    """Return a JSON-ready TTM payload with fail-closed per-metric eligibility.

    ``financials`` contains additive flows only. ``balance_sheet`` is a separate
    date-specific snapshot, never a sum. ``ratios`` are fractions, not percents.
    Different issuers' valid TTM windows can still have different start/end dates.
    """
    if not isinstance(history, dict):
        history = {}
    periods, issues = _window(history)
    result = {
        "schema_version": 1, "ticker": history.get("ticker"), "as_of": history.get("as_of"),
        "status": "unavailable", "period": None, "financials": {}, "ratios": {}, "balance_sheet": {},
        "source_ids": [], "source_urls": [], "issues": issues,
        "limitations": [
            "TTM means the latest four stored standalone fiscal quarters, not verified current reporting.",
            "Each issuer's exact period dates must be checked before cross-company ranking.",
            "EPS and weighted-average shares are nonadditive and are not summed.",
            "Balance-sheet amounts refer only to the last quarter-end and remain separate from TTM flows.",
        ],
    }
    if periods:
        result["period"] = {
            "id": "ttm:" + periods[-1]["end"], "type": "ttm", "start": periods[0]["start"],
            "end": periods[-1]["end"], "label": "TTM · " + periods[0]["start"] + " – " + periods[-1]["end"],
            "quarter_ids": [p.get("id") for p in periods],
            "quarter_periods": deepcopy(periods),
        }
    if issues:
        result["financials"] = {m: _missing(issues) for m in FLOW_METRICS}
        result["ratios"] = {m: _missing(issues, unit="ratio") for m in RATIOS}
        return result
    result["financials"] = {m: _flow(history, periods, m) for m in FLOW_METRICS}
    result["ratios"] = {key: _ratio(result["financials"], metric) for key, metric in RATIOS.items()}
    last = periods[-1]
    for metric in BALANCE_METRICS:
        cell = history.get("financials", {}).get(last["id"], {}).get(metric)
        reasons = _cell_reasons(history, last, metric, cell, instant=True)
        value = (_missing(reasons, unit="shares" if metric == "shares_outstanding" else "USD",
                          provenance=(cell or {}).get("provenance", [])) if reasons else deepcopy(cell))
        value["date"] = last["end"]
        value["period"] = deepcopy(last)
        value["note"] = (value.get("note", "") + " Point-in-time balance; not summed across quarters.").strip()
        result["balance_sheet"][metric] = value
    count = sum(c["model_usable"] for c in result["financials"].values())
    result["status"] = "available" if count == len(FLOW_METRICS) else "partial" if count else "unavailable"
    for metric, cell in result["financials"].items():
        if not cell["model_usable"]:
            result["issues"].append({"metric": metric, "codes": cell["flags"]})
    sources = [s for group in ("financials", "balance_sheet") for c in result[group].values() for s in c.get("provenance", [])]
    result["source_ids"] = sorted({s["source_id"] for s in sources if s.get("source_id")})
    result["source_urls"] = sorted({s["url"] for s in sources if s.get("url")})
    return result


def compare_ttm(results, metric):
    """Rank only complete eligible values over identical dated TTM windows.

    The UI may display independently valid windows side by side with their dates.
    This stricter helper prevents that display from implying a matched-period rank.
    """
    answer = {"status": "unavailable", "metric": metric, "ranking": [], "issues": []}
    if metric not in FLOW_METRICS and metric not in RATIOS:
        answer["issues"].append("unsupported_ttm_metric")
        return answer
    if len(results) < 2 or len({r.get("ticker") for r in results}) != len(results):
        answer["issues"].append("distinct_issuers_required")
        return answer
    group = "financials" if metric in FLOW_METRICS else "ratios"
    cells = [r.get(group, {}).get(metric, {}) for r in results]
    if any(c.get("model_usable") is not True or not _finite(c.get("value")) for c in cells):
        answer["issues"].append("incomplete_comparison")
    periods = [r.get("period") or {} for r in results]
    if any(not p.get("start") or not p.get("end") for p in periods) or len({(p.get("start"), p.get("end")) for p in periods}) != 1:
        answer["issues"].append("different_ttm_windows")
    if len({(c.get("unit"), c.get("basis")) for c in cells}) != 1:
        answer["issues"].append("incompatible_comparison_basis")
    if len({c.get("definition_tag") for c in cells}) != 1 or any(not c.get("definition_tag") for c in cells):
        answer["issues"].append("unreconciled_comparison_definitions")
    if answer["issues"]:
        return answer
    answer["status"] = "available"
    answer["period"] = {"start": periods[0]["start"], "end": periods[0]["end"]}
    answer["ranking"] = sorted([
        {"ticker": r["ticker"], "value": c["value"], "unit": c["unit"], "basis": c["basis"],
         "source_urls": c.get("source_urls", [])}
        for r, c in zip(results, cells)
    ], key=lambda row: row["value"], reverse=True)
    return answer
