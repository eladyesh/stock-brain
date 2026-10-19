# Exact periods and historical answers

The Python assistant and hosted browser use the same generated historical evidence
records and regression questions. A numeric answer must match every requested
metric, company, accounting basis and period. Neither engine substitutes a nearby
period or returns only one side of an incomplete comparison.

## Period contract

- `FY2024`, `fiscal 2024`, and `שנת הכספים 2024` request the issuer's sourced fiscal
  identity, including its fiscal quarter number when requested.
- `calendar 2024`, `CY2024`, and an unqualified `2024` require January 1 through
  December 31. A calendar quarter requires its exact first and last dates.
- Calendar and fiscal quarter numbers are independent. Microsoft calendar Q1 2026
  is January 1–March 31, even though the filing calls this Q3 FY2026.
- 52/53-week fiscal periods do not become calendar periods by rounding dates.
- A quarter without a year, contradictory calendar/fiscal modifiers, multiple
  periods, TTM/LTM, YTD and relative periods such as "last year" are unsupported.
  These require clarification or a future explicit calculation contract.
- Unsupported adjustments, segment breakdowns, non-GAAP substitutions and partial
  comparisons still fail closed. A source link alone does not establish that a
  number answers the requested period.

## Two evidence paths

Reviewed narrative lookup remains first. When a precisely dated metric is absent
from those selected claims, the assistant can use the separate SEC history.
Historical responses have `mode: financial_history`, an exact value/unit, start
and end dates, fiscal label, GAAP basis, source concept, accession, filing date,
snapshot date and original SEC URL. English and Hebrew text are deterministic
templates; they do not claim independent editorial review or human approval.

Only nonmissing, model-usable cells qualify for this additional path. A revision,
share-basis or debt-scope flag that blocks comparability remains a refusal, with
the history tab available for inspecting the source. Missing inputs are never
zero. This lookup does not add forecasts, consensus, rolling-period calculations
or currency conversions. Explicit "current/latest" wording retains the disclosure
freshness gate even when historical data is available.

Examples:

| Question | Behavior |
| --- | --- |
| What was MSFT revenue in FY2024? | Exact fiscal annual history with source |
| מה היו הכנסות מיקרוסופט ברבעון הראשון של 2026? | Exact January–March history, labelled Q3 FY2026 |
| What was AVGO revenue in calendar Q3 2026? | Refuse; the fiscal May–August quarter is not July–September |
| What was MSFT revenue over the last twelve months? | Refuse unsupported rolling period |

`tests/historical-answer-cases.json` is shared by Python and browser tests. Additional
tests mutate values, dates and citations and remove comparison evidence. The
original frozen acceptance questions remain unchanged; the former FY2024/Q1
history refusals in precision tests now require supported answers.

## Snapshot compatibility

Snapshots carry `answer_contract_version: 2` and a generated `historical_index`
for each issuer. The browser rejects incompatible remote snapshots, keeps its
usable bundled copy and labels the fallback date. This avoids mixing new answer
rules with an older data export. The number of companies is no longer hardcoded.

Daily maintenance uses the separate data branch described in CLOUD_UPDATES.md.
Source failures retain prior values and remain visible as partial updates; data
refreshes do not clear research review obligations.

## Derived percentages and semantic holdouts

Exact fiscal/quarterly questions can return gross, operating and parent-attributable
net margins, plus year-over-year revenue growth. Margins divide compatible,
model-usable income by revenue. Growth requires the same fiscal period one year
earlier, compatible revenue concepts and comparable period lengths. Every
calculation binds its formula, input records and source locators. Rates use `%`;
an absolute revenue amount is never substituted for growth or revenue per share.

Explicit FX requests, unsupported per-share ratios, CAGR and QoQ calculations are
refused. Sixteen independently added semantic cases run unchanged in both Python
and the browser. Verified NVDA/AVGO split-adjusted EPS additionally cites the
primary split disclosure; original reported inputs remain inspectable.
