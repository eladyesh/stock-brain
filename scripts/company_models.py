"""Source-bound, illustrative company scenarios; no consensus or trade recommendations.

The historical normalizer owns source/comparability gates. This module never
promotes an unusable historical cell merely because a model file has valid JSON.
"""
from __future__ import annotations

import copy
from datetime import date
import json
import math
from pathlib import Path
from urllib.parse import urlparse

FORECAST_YEARS = (2027, 2028, 2029, 2030)
ASSUMPTION_KEYS = ("revenue_growth", "net_margin", "fcf_margin", "share_change")
OVERRIDE_KEYS = {"revenueGrowth": "revenue_growth", "netMargin": "net_margin",
                 "fcfMargin": "fcf_margin", "shareChange": "share_change"}


def _number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def _date(value):
    text = str(value)[:10]
    parsed = date.fromisoformat(text)
    if parsed.isoformat() != text:
        raise ValueError("Expected ISO date")
    return parsed


def _range(values):
    values = [v for v in values if _number(v)]
    return {"low": min(values), "high": max(values)} if values else None


def _blocked(ticker, reasons, model=None):
    result = copy.deepcopy(model or {"schema_version": 1, "ticker": ticker})
    result["readiness"] = {"status": "blocked", "reasons": reasons,
                           "per_share_ready": False, "price_ready": False}
    result["projection"] = {"status": "blocked", "reasons": reasons, "scenarios": [],
                            "range": {"price": None, "annualized_return": None},
                            "horizon_years": None, "quote": result.get("quote")}
    return result


def _validate_model(model, ticker):
    """Return structural issues. Passing this check is not factual verification."""
    errors = []
    if model.get("schema_version") != 1 or model.get("ticker") != ticker:
        errors.append("model_identity_mismatch")
    try:
        cutoff = _date(model["as_of"])
        end = _date(model["valuation_date"])
        if end <= cutoff:
            errors.append("valuation_date_not_after_assumption_date")
        if model["base"]["period"]["fiscal_year"] != 2026:
            errors.append("base_must_be_fy2026")
        if _date(model["base"]["period"]["end"]) > cutoff:
            errors.append("base_after_cutoff")
    except (KeyError, ValueError, TypeError):
        errors.append("invalid_model_dates")
        cutoff = None
    sources = model.get("sources", [])
    source_ids = {s.get("id") for s in sources if isinstance(s, dict)}
    if not sources or None in source_ids or len(source_ids) != len(sources):
        errors.append("missing_or_duplicate_sources")
    for source in sources:
        if not isinstance(source, dict):
            errors.append("invalid_source")
            continue
        url = urlparse(source.get("url", ""))
        try:
            source_date = _date(source["date"])
            if cutoff and source_date > cutoff:
                errors.append("source_after_cutoff")
        except (KeyError, ValueError, TypeError):
            errors.append("invalid_source_date")
        if url.scheme != "https" or not url.netloc or not source.get("title"):
            errors.append("invalid_source")
    base = model.get("base", {})
    if base.get("currency") != "USD" or base.get("share_unit") != "shares":
        errors.append("invalid_base_units")
    for key in ("revenue", "net_income", "shares_diluted", "reported_eps"):
        if not _number(base.get(key)) or (key in {"revenue", "shares_diluted"} and base[key] <= 0):
            errors.append("invalid_base_" + key)
    for key in ("revenue", "net_income", "shares_diluted", "reported_eps", "free_cash_flow"):
        binding = base.get("provenance", {}).get(key, {})
        if base.get(key) is not None and (not binding.get("source_ids") or
                any(s not in source_ids for s in binding.get("source_ids", [])) or not binding.get("locator")):
            errors.append("unbound_base_" + key)
    if base.get("free_cash_flow") is not None and not _number(base["free_cash_flow"]):
        errors.append("invalid_base_free_cash_flow")
    scenarios = model.get("scenarios", [])
    if sorted(s.get("id", "") for s in scenarios) != ["base", "bear", "bull"]:
        errors.append("requires_bear_base_bull")
    for scenario in scenarios:
        if scenario.get("assumption_type") != "analyst_assumption" or not scenario.get("rationale"):
            errors.append("unlabelled_scenario_assumption")
        if not _number(scenario.get("exit_pe")) or not 0 < scenario["exit_pe"] <= 100:
            errors.append("invalid_exit_pe")
        years = scenario.get("years", [])
        if tuple(y.get("fiscal_year") for y in years) != FORECAST_YEARS:
            errors.append("requires_contiguous_fy2027_fy2030")
        for year in years:
            for key in ASSUMPTION_KEYS:
                value = year.get(key)
                low, high = {"revenue_growth": (-1, 3), "net_margin": (-1, 1),
                             "fcf_margin": (-1, 1), "share_change": (-0.5, 0.5)}[key]
                if not _number(value) or value < low or value > high or (key == "revenue_growth" and value == -1):
                    errors.append("invalid_assumption_" + key)
    return sorted(set(errors))


def load_company_model(root, ticker, history=None, quote=None):
    """Attach historical gates and a dated quote without silently rebasing forecasts.

    Missing files return None. Broken/stale model bindings return a visible blocked
    payload instead of breaking the whole desk build. Per-share results require
    usable diluted shares AND EPS on a verified corporate-action basis.
    """
    path = Path(root) / "research" / "models" / (ticker + ".json")
    if not path.exists():
        return None
    try:
        model = json.loads(path.read_text(encoding="utf-8"))
        errors = _validate_model(model, ticker)
    except (ValueError, TypeError, KeyError, AttributeError, OSError):
        return _blocked(ticker, ["unreadable_or_invalid_model"])
    if errors:
        return _blocked(ticker, errors, model)
    history = history or {}
    if history.get("ticker") != ticker:
        return _blocked(ticker, ["historical_identity_missing_or_mismatched"], model)
    base = model["base"]
    period = base["period"]
    actual = next((p for p in history.get("periods", []) if p.get("id") == period["id"]), None)
    if not actual or any(actual.get(k) != period.get(k) for k in ("start", "end", "fiscal_year", "type")):
        return _blocked(ticker, ["historical_base_period_mismatch"], model)
    cells = history.get("financials", {}).get(period["id"], {})
    reasons = ["illustrative_analyst_assumptions_not_consensus_or_issuer_guidance"]
    base["model_usable"] = {}
    base["historical_provenance"] = {}
    for key in ("revenue", "net_income", "free_cash_flow", "shares_diluted", "reported_eps"):
        cell = cells.get("eps_diluted" if key == "reported_eps" else key, {})
        value = base.get(key)
        same_value = _number(value) and _number(cell.get("value")) and math.isclose(value, cell["value"], rel_tol=1e-9, abs_tol=1e-6)
        expected_unit = "USD/shares" if key == "reported_eps" else "shares" if key == "shares_diluted" else "USD"
        usable = bool(same_value and cell.get("model_usable") is True and not cell.get("conflicts") and
                      cell.get("unit") == expected_unit and
                      cell.get("comparison_status") not in {"not_comparable", "conflicting"})
        base["model_usable"][key] = usable
        base["historical_provenance"][key] = copy.deepcopy(cell.get("provenance", []))
        if key in {"revenue", "net_income"} and not usable:
            errors.append("historical_base_not_usable_" + key)
        elif key in {"shares_diluted", "reported_eps"} and not usable:
            reasons.append("per_share_gate_not_verified_" + key)
        elif key == "free_cash_flow" and not usable:
            reasons.append("strict_historical_fcf_unavailable_forecast_is_assumed_margin")
        if value is not None and not same_value:
            errors.append("historical_base_value_mismatch_" + key)
    if errors:
        return _blocked(ticker, sorted(set(errors)), model)
    per_share_ready = all(base["model_usable"][k] for k in ("shares_diluted", "reported_eps"))
    # Reported statement rounding must reconcile; this does not certify split basis.
    calculated_eps = base["net_income"] / base["shares_diluted"]
    if abs(calculated_eps - base["reported_eps"]) > max(0.02, abs(base["reported_eps"]) * 0.001):
        per_share_ready = False
        reasons.append("reported_eps_does_not_reconcile_with_base_profit_and_shares")
    model["quote"] = copy.deepcopy(quote)
    quote_ready = False
    try:
        quote_ready = bool(quote and quote.get("ticker") == ticker and quote.get("status") == "available"
                           and quote.get("currency") == "USD" and _number(quote.get("price")) and quote["price"] > 0
                           and quote.get("source_url") and _date(quote["trade_at"]) < _date(model["valuation_date"]))
        if quote_ready:
            reasons.append("return_uses_dated_market_quote_" + str(quote["trade_at"])[:10])
    except (KeyError, ValueError, TypeError):
        quote_ready = False
    if not quote_ready:
        reasons.append("dated_usd_reference_quote_unavailable")
    model["readiness"] = {"status": "illustrative", "reasons": reasons,
                          "per_share_ready": per_share_ready, "price_ready": per_share_ready and quote_ready}
    model["projection"] = project_company_model(model)
    return model


def project_company_model(model, overrides=None):
    """Pure deterministic projection, mirrored in site/models.mjs.

    Optional overrides change one selected scenario's annual assumptions. They
    are user assumptions, never modifications to sourced historical facts.
    """
    overrides = overrides or {}
    readiness = model.get("readiness", {})
    if readiness.get("status") == "blocked":
        return _blocked(model.get("ticker"), readiness.get("reasons", []))["projection"]
    working = copy.deepcopy(model)
    selected = overrides.get("scenarioId", "base")
    if selected not in {s.get("id") for s in working.get("scenarios", [])}:
        return _blocked(model.get("ticker"), ["unknown_scenario_override"])["projection"]
    for scenario in working.get("scenarios", []):
        if scenario["id"] == selected:
            for public_key, key in OVERRIDE_KEYS.items():
                if public_key in overrides:
                    for year in scenario["years"]:
                        year[key] = overrides[public_key]
            if "exitPe" in overrides:
                scenario["exit_pe"] = overrides["exitPe"]
    errors = _validate_model(working, model.get("ticker"))
    if errors:
        return _blocked(model.get("ticker"), errors)["projection"]
    quote = copy.deepcopy(working.get("quote"))
    if "referencePrice" in overrides:
        if not _number(overrides["referencePrice"]) or overrides["referencePrice"] <= 0:
            return _blocked(model.get("ticker"), ["invalid_reference_price"])["projection"]
        if quote:
            quote["price"] = overrides["referencePrice"]
            quote["price_type"] = "user_assumed_reference_price"
    horizon = None
    try:
        if quote and _number(quote.get("price")) and quote["price"] > 0:
            horizon = (_date(working["valuation_date"]) - _date(quote["trade_at"])).days / 365.25
            if horizon <= 0:
                horizon = None
    except (KeyError, ValueError, TypeError):
        pass
    per_share = readiness.get("per_share_ready") is True
    price_ready = bool(readiness.get("price_ready") is True and horizon is not None and quote and
                       quote.get("currency") == "USD" and quote.get("ticker") == model.get("ticker") and
                       quote.get("status") == "available" and quote.get("source_url"))
    projections = []
    for scenario in working["scenarios"]:
        revenue, shares = working["base"]["revenue"], working["base"]["shares_diluted"]
        rows = []
        for year in scenario["years"]:
            revenue *= 1 + year["revenue_growth"]
            shares *= 1 + year["share_change"]
            profit = revenue * year["net_margin"]
            fcf = revenue * year["fcf_margin"]
            rows.append({**year, "revenue": revenue, "net_income": profit, "free_cash_flow": fcf,
                         "shares_diluted": shares if per_share else None,
                         "eps": profit / shares if per_share else None,
                         "evidence_label": "analyst_assumption_calculated"})
        last = rows[-1]
        # Non-positive EPS has no meaningful positive P/E valuation.
        price = last["eps"] * scenario["exit_pe"] if per_share and last["eps"] > 0 else None
        annualized = (price / quote["price"]) ** (1 / horizon) - 1 if price_ready and price is not None else None
        terminal = {**last, "price": price, "annualized_return": annualized,
                    "revenue_cagr": (revenue / working["base"]["revenue"]) ** (1 / len(rows)) - 1,
                    "exit_pe": scenario["exit_pe"], "valuation_date": working["valuation_date"]}
        projections.append({**scenario, "rows": rows, "terminal": terminal,
                            "modified_by_user": scenario["id"] == selected and bool(set(overrides) - {"scenarioId"})})
    return {"status": readiness.get("status", "illustrative"), "reasons": readiness.get("reasons", []),
            "scenarios": projections, "range": {"price": _range([s["terminal"]["price"] for s in projections]),
            "annualized_return": _range([s["terminal"]["annualized_return"] for s in projections])},
            "horizon_years": horizon, "quote": quote, "return_basis": "price_only_excludes_dividends_taxes_fees_fx",
            "fiscal_projection_steps": len(FORECAST_YEARS)}


def required_revenue_cagr(model, scenario_id="base", reference_price=None, target_return=0):
    """Constant fiscal revenue CAGR required at fixed terminal margin/shares/P/E.

    This is an implied assumption, not a claim about the market's actual forecast.
    """
    overrides = {"referencePrice": reference_price} if reference_price is not None else {}
    projection = project_company_model(model, overrides)
    scenario = next((s for s in projection["scenarios"] if s["id"] == scenario_id), None)
    horizon, quote = projection.get("horizon_years"), projection.get("quote")
    if (not scenario or not horizon or not quote or not model.get("readiness", {}).get("price_ready")
            or quote.get("currency") != "USD" or quote.get("ticker") != model.get("ticker")
            or quote.get("status") != "available" or not quote.get("source_url")
            or not _number(target_return) or target_return <= -1):
        return {"status": "unavailable", "reason": "requires_verified_shares_dated_quote_and_valid_return"}
    terminal = scenario["terminal"]
    if terminal["net_margin"] <= 0 or not terminal["shares_diluted"]:
        return {"status": "unavailable", "reason": "requires_positive_terminal_margin_and_shares"}
    price = quote["price"] * (1 + target_return) ** horizon
    revenue = price / scenario["exit_pe"] * terminal["shares_diluted"] / terminal["net_margin"]
    return {"status": "illustrative", "required_revenue_cagr": (revenue / model["base"]["revenue"]) ** 0.25 - 1,
            "required_terminal_revenue": revenue, "required_terminal_price": price,
            "target_annualized_return": target_return, "horizon_years": horizon,
            "fiscal_projection_steps": 4, "scenario_id": scenario_id,
            "interpretation": "Required constant fiscal revenue growth given this scenario's terminal margin, diluted shares and P/E; not market consensus."}
