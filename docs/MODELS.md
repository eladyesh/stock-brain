# Company scenarios

MSFT, MU and NVDA have company-specific, illustrative FY2027–FY2030 paths in
`research/models/`. They start from a frozen FY2026 annual statement and use
explicit annual revenue growth, net margins, cash-flow margins and diluted-share
changes. These inputs are analyst assumptions, not consensus estimates, issuer
forecasts or recommendations. The three cases have no probability weights.

The source cutoff is October 22, 2026. A newer market quote can be used without
silently updating the financial assumptions. The displayed quote timestamp and
assumption cutoff must remain separate.

## Primary evidence and base definitions

| Company | Base period end | Revenue, USD bn | GAAP net income, USD bn | Strict FCF, USD bn | Weighted diluted shares, bn |
| --- | --- | ---: | ---: | ---: | ---: |
| MSFT | 2026-06-30 | 331.839 | 133.749 | 66.987 | 7.453 |
| MU | 2026-09-03 | 133.188 | 84.969 | 58.963 | 1.143 |
| NVDA | 2026-01-25 | 215.938 | 120.067 | unavailable | 24.514 |

Source review used the official [Microsoft FY2026 Q4 release](https://www.microsoft.com/en-us/investor/earnings/fy-2026-q4/press-release-webcast),
[Micron FY2026 release](https://investors.micron.com/news/press-release/2026/Micron-Technology-Inc--Reports-Record-Fiscal-Fourth-Quarter-and-Full-Year-2026-Results/default.aspx),
and [NVIDIA FY2026 release](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Fourth-Quarter-and-Fiscal-2026/default.aspx).
The loader reconciles these observations against the separately normalized SEC
history. A source URL and valid schema do not by themselves establish factual
validity. Every base item has a source ID and statement locator. Dates and review
type are explicit; no human review is claimed.

Strict historical FCF means operating cash flow less **gross cash PP&E purchases**.
MSFT is 182.935 minus 115.948 = 66.987 billion dollars. MU is 89.675 minus 30.712 =
58.963 billion dollars; government incentives and asset-sale proceeds do not reduce
gross capex in this definition. NVDA reports a broader asset-purchase line. Its
separate issuer FCF of 96.575 billion dollars subtracts PP&E **and intangibles** and
related principal payments. That figure is supplemental and does not fill the
missing strict historical FCF cell. NVDA's forward FCF margins are consequently
explicit assumptions without a comparable strict historical anchor.

Diluted shares are the **annual weighted-average EPS denominator**. They are not
quote-date shares outstanding and are never multiplied by the market quote to
claim current market capitalization. Future share changes describe future annual
diluted denominators, including an assumed net effect of repurchases and dilution.

## What each case tests

- **MSFT:** AI monetization versus cash capex and depreciation. The base path
  moderates growth and improves cash conversion; the bear path combines lower
  growth, margin pressure and dilution. Investment gains are not mechanically
  extrapolated from the historical GAAP earnings base.
- **MU:** Memory pricing and the capacity cycle. The base path includes a revenue
  decline in FY2029; the bear path has a deeper downcycle while committed factory
  spending consumes cash. The bull path requires demand and supply discipline to
  preserve unusually high economics. No case assumes Q4's gross margin is a
  permanent net margin.
- **NVDA:** The near-term AI ramp followed by alternative rates of deceleration.
  Customer spending concentration, export access, competing accelerators, pricing
  and product transitions affect later growth and margins. The base path does not
  require incremental China reopening.

The annual paths, share changes and exit P/E are deliberately visible and editable.
An exit multiple is a selected valuation assumption; it is not presented as a
historical average, a peer-derived fair value or a price target. Current issuer
quarterly guidance is labelled separately and never extended into a four-year
issuer forecast. Qualitative context also uses the official
[Microsoft Q3 release](https://www.microsoft.com/en-us/investor/earnings/fy-2026-q3/press-release-webcast)
and [NVIDIA Q2 FY2027 release](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Second-Quarter-Fiscal-2027/).

## Calculation contract

For each fiscal year, with rates stored as decimal fractions:

```text
revenue[t] = revenue[t-1] × (1 + revenue_growth[t])
net_income[t] = revenue[t] × net_margin[t]
free_cash_flow[t] = revenue[t] × fcf_margin[t]
diluted_shares[t] = diluted_shares[t-1] × (1 + share_change[t])
eps[t] = net_income[t] / diluted_shares[t]
terminal_price = FY2030 eps × exit_pe
price_only_annualized_return = (terminal_price / reference_quote)^(1 / market_years) − 1
market_years = days(quote trade date, assumed valuation date) / 365.25
```

There are four **fiscal growth steps**, but the market holding interval is shorter
because the quote is after the baseline's period end. The assumed valuation dates
are June 30, 2030 (MSFT), August 31, 2030 (MU), and January 31, 2030 (NVDA). They are
planning assumptions near FY2030 end, not confirmed issuer reporting or sale dates.
No P/E valuation is produced for zero or negative terminal earnings. Dividends,
taxes, fees and FX are excluded. There is no EV/debt bridge or DCF calculation.

Reverse valuation solves the constant fiscal revenue CAGR required to meet a chosen
price-only return while holding one scenario's terminal margin, shares and P/E
fixed. It uses four fiscal periods for revenue growth and the dated market interval
for investment return. It is a statement about these chosen assumptions, not the
market's actual expectations. Scenario min/max values are a range of three selected
outcomes, not a statistical confidence interval.

## Integration

`scripts/company_models.py` exports:

```python
load_company_model(root, ticker, history, quote)  # model dict, or None if absent
project_company_model(model, overrides=None)    # deterministic projection
required_revenue_cagr(model, scenario_id='base', reference_price=None, target_return=0)
```

The loader adds historical provenance, `base.model_usable`, `readiness`, the quote
and a projection. It requires the original fiscal identity and matching values; a
restatement cannot silently rebase the forecast. Missing/unusable core facts or a
changed baseline produce a visible `blocked` result with reasons, not an exception
that breaks the entire desk. Unverified share/EPS comparability withholds EPS,
terminal price and returns while retaining revenue/profit/cash scenarios. Missing
strict historical FCF remains null and visibly limits interpretation.

All current models retain `readiness.status = illustrative` even when the source and
math gates pass. `per_share_ready` and `price_ready` indicate technical gates, not
investment confidence. The generic EPS-growth sensitivity remains a separate tool.

`site/models.mjs` exports the matching pure browser functions:

```javascript
projectCompanyModel(model, {
  scenarioId: 'base', revenueGrowth: 0.15, netMargin: 0.4,
  fcfMargin: 0.25, shareChange: -0.005, exitPe: 28
});
requiredRevenueCagr(model, 'base', null, 0.1);
```

Omit blank overrides. An entered override replaces **all four years of the selected
case only**; the other two cases retain their stored paths. Inputs are not mutated.
`referencePrice` can replace the quote's amount as an explicit user assumption,
while keeping its dated horizon. No missing quote date is invented.

Projection output contains `scenarios[].rows`, `scenarios[].terminal`, `range.price`,
`range.annualized_return`, `quote`, `horizon_years`, and reasons. Monetary amounts are
unscaled USD; shares are unscaled share counts; rates are decimals. Optional values
are null, never coerced to zero. Reverse valuation returns an `illustrative` result
with required revenue CAGR, revenue and price, or `unavailable` with a reason.

## Thesis comparisons and maintenance

`research/thesis/` contains explicit before/after facts with both source bindings,
English/Hebrew text, labelled interpretation and measurable monitoring thresholds.
MSFT compares Q3 to Q4 FY2026; MU compares Q3 to Q4 FY2026; NVDA compares Q1 to Q2
FY2027. Prior-period columns in the latest release are valid comparative evidence
when their labels and locators are preserved. Thresholds are analyst assumptions
that trigger reassessment, never automatic trade instructions.

After a material report, review the annual base, earnings quality, fiscal identity,
split/share comparability, cash-flow definition, dated quote, scenario rationale
and measurable checkpoints. Record any rebase explicitly. Numerical checks cannot
replace this source review. Tests cover source/baseline gates, missing-data behavior,
cyclic paths, earnings/share math, dated annualization, selected-case overrides,
reverse-valuation round trips and Python/browser parity.
