// Pure company scenario calculations. The Python build owns historical source gates.
// Inputs and results are illustrative analyst assumptions, never issuer guidance.
const YEARS = [2027, 2028, 2029, 2030];
const OVERRIDES = {revenueGrowth: 'revenue_growth', netMargin: 'net_margin', fcfMargin: 'fcf_margin', shareChange: 'share_change'};
const number = value => typeof value === 'number' && Number.isFinite(value);
const clone = value => JSON.parse(JSON.stringify(value));
const dateValue = value => {
  const text = String(value ?? '').slice(0, 10);
  if (!/^\d{4}-\d{2}-\d{2}$/.test(text)) return null;
  const parsed = Date.parse(`${text}T00:00:00Z`);
  return Number.isFinite(parsed) && new Date(parsed).toISOString().slice(0, 10) === text ? parsed : null;
};
const range = values => {
  const finite = values.filter(number);
  return finite.length ? {low: Math.min(...finite), high: Math.max(...finite)} : null;
};
const blocked = reasons => ({status: 'blocked', reasons, scenarios: [], range: {price: null, annualized_return: null}, horizon_years: null, quote: null});

function validate(model) {
  const errors = [];
  if (model?.schema_version !== 1 || !model.ticker) errors.push('model_identity_mismatch');
  const cutoff = dateValue(model?.as_of), end = dateValue(model?.valuation_date);
  if (cutoff === null || end === null || dateValue(model?.base?.period?.end) === null) errors.push('invalid_model_dates');
  else {
    if (end <= cutoff) errors.push('valuation_date_not_after_assumption_date');
    if (dateValue(model.base.period.end) > cutoff) errors.push('base_after_cutoff');
  }
  if (model?.base?.period?.fiscal_year !== 2026) errors.push('base_must_be_fy2026');
  const base = model?.base ?? {};
  if (base.currency !== 'USD' || base.share_unit !== 'shares') errors.push('invalid_base_units');
  for (const key of ['revenue', 'net_income', 'shares_diluted', 'reported_eps']) {
    if (!number(base[key]) || (['revenue', 'shares_diluted'].includes(key) && base[key] <= 0)) errors.push(`invalid_base_${key}`);
  }
  if (base.free_cash_flow !== null && base.free_cash_flow !== undefined && !number(base.free_cash_flow)) errors.push('invalid_base_free_cash_flow');
  const scenarios = model?.scenarios ?? [];
  if (!Array.isArray(scenarios) || scenarios.map(s => s.id).sort().join(',') !== 'base,bear,bull') return [...errors, 'requires_bear_base_bull'];
  for (const scenario of scenarios) {
    if (scenario.assumption_type !== 'analyst_assumption' || !scenario.rationale) errors.push('unlabelled_scenario_assumption');
    if (!number(scenario.exit_pe) || scenario.exit_pe <= 0 || scenario.exit_pe > 100) errors.push('invalid_exit_pe');
    if (!Array.isArray(scenario.years) || scenario.years.map(y => y.fiscal_year).join(',') !== YEARS.join(',')) {
      errors.push('requires_contiguous_fy2027_fy2030');
      continue;
    }
    for (const year of scenario.years) {
      for (const [key, [low, high]] of Object.entries({revenue_growth: [-1, 3], net_margin: [-1, 1], fcf_margin: [-1, 1], share_change: [-0.5, 0.5]})) {
        const value = year[key];
        if (!number(value) || value < low || value > high || (key === 'revenue_growth' && value === -1)) errors.push(`invalid_assumption_${key}`);
      }
    }
  }
  return [...new Set(errors)].sort();
}

/**
 * Project all three cases. Optional camelCase overrides replace all four annual
 * assumptions ONLY in scenarioId (default 'base'); original model is never changed.
 * Blank fields must be omitted by callers. Rates are decimals, not percentage points.
 * EPS requires the build's verified diluted-share and EPS gates. Returns require
 * a dated USD quote and use actual days / 365.25, not four fiscal periods.
 */
export function projectCompanyModel(model, overrides = {}) {
  const readiness = model?.readiness ?? {};
  if (readiness.status === 'blocked') return blocked(readiness.reasons ?? []);
  const initialErrors = validate(model);
  if (initialErrors.length) return blocked(initialErrors);
  const working = clone(model), selected = overrides.scenarioId ?? 'base';
  if (!working.scenarios.some(s => s.id === selected)) return blocked(['unknown_scenario_override']);
  for (const scenario of working.scenarios) {
    if (scenario.id !== selected) continue;
    for (const [publicKey, key] of Object.entries(OVERRIDES)) {
      if (Object.hasOwn(overrides, publicKey)) for (const year of scenario.years) year[key] = overrides[publicKey];
    }
    if (Object.hasOwn(overrides, 'exitPe')) scenario.exit_pe = overrides.exitPe;
  }
  const errors = validate(working);
  if (errors.length) return blocked(errors);
  const quote = working.quote ?? null;
  if (Object.hasOwn(overrides, 'referencePrice')) {
    if (!number(overrides.referencePrice) || overrides.referencePrice <= 0) return blocked(['invalid_reference_price']);
    if (quote) {
      quote.price = overrides.referencePrice;
      quote.price_type = 'user_assumed_reference_price';
    }
  }
  const quoteDate = dateValue(quote?.trade_at), exitDate = dateValue(working.valuation_date);
  const elapsed = quoteDate !== null && exitDate !== null ? (exitDate - quoteDate) / (86400000 * 365.25) : null;
  const horizon = elapsed > 0 && number(quote?.price) && quote.price > 0 ? elapsed : null;
  const perShare = readiness.per_share_ready === true;
  const priceReady = readiness.price_ready === true && horizon !== null && quote?.currency === 'USD'
    && quote.ticker === model.ticker && quote.status === 'available' && Boolean(quote.source_url);
  const scenarios = working.scenarios.map(scenario => {
    let revenue = working.base.revenue, shares = working.base.shares_diluted;
    const rows = scenario.years.map(year => {
      revenue *= 1 + year.revenue_growth;
      shares *= 1 + year.share_change;
      const profit = revenue * year.net_margin;
      return {...year, revenue, net_income: profit, free_cash_flow: revenue * year.fcf_margin,
        shares_diluted: perShare ? shares : null, eps: perShare ? profit / shares : null,
        evidence_label: 'analyst_assumption_calculated'};
    });
    const last = rows.at(-1);
    const price = perShare && last.eps > 0 ? last.eps * scenario.exit_pe : null;
    const annualized = priceReady && price !== null ? (price / quote.price) ** (1 / horizon) - 1 : null;
    return {...scenario, rows, terminal: {...last, price, annualized_return: annualized,
      revenue_cagr: (revenue / working.base.revenue) ** (1 / rows.length) - 1,
      exit_pe: scenario.exit_pe, valuation_date: working.valuation_date},
      modified_by_user: scenario.id === selected && Object.keys(overrides).some(key => key !== 'scenarioId')};
  });
  return {status: readiness.status ?? 'illustrative', reasons: readiness.reasons ?? [], scenarios,
    range: {price: range(scenarios.map(s => s.terminal.price)), annualized_return: range(scenarios.map(s => s.terminal.annualized_return))},
    horizon_years: horizon, quote, return_basis: 'price_only_excludes_dividends_taxes_fees_fx', fiscal_projection_steps: 4};
}

/** The required constant fiscal revenue CAGR, holding terminal margin/shares/P/E fixed. */
export function requiredRevenueCagr(model, scenarioId = 'base', referencePrice = null, targetReturn = 0) {
  const projection = projectCompanyModel(model, referencePrice === null ? {} : {referencePrice});
  const scenario = projection.scenarios.find(s => s.id === scenarioId);
  const horizon = projection.horizon_years, quote = projection.quote;
  if (!scenario || !horizon || !quote || model?.readiness?.price_ready !== true
    || quote.currency !== 'USD' || quote.ticker !== model.ticker || quote.status !== 'available' || !quote.source_url
    || !number(targetReturn) || targetReturn <= -1) {
    return {status: 'unavailable', reason: 'requires_verified_shares_dated_quote_and_valid_return'};
  }
  const terminal = scenario.terminal;
  if (terminal.net_margin <= 0 || !terminal.shares_diluted) return {status: 'unavailable', reason: 'requires_positive_terminal_margin_and_shares'};
  const price = quote.price * (1 + targetReturn) ** horizon;
  const revenue = price / scenario.exit_pe * terminal.shares_diluted / terminal.net_margin;
  return {status: 'illustrative', required_revenue_cagr: (revenue / model.base.revenue) ** 0.25 - 1,
    required_terminal_revenue: revenue, required_terminal_price: price, target_annualized_return: targetReturn,
    horizon_years: horizon, fiscal_projection_steps: 4, scenario_id: scenarioId,
    interpretation: "Required constant fiscal revenue growth given this scenario's terminal margin, diluted shares and P/E; not market consensus."};
}
