---
schema_version: 1
document_type: company_facts
company_id: company-cik-0002115119
cik: 0002115119
company_name: Columbia Financial, Inc./MD/
tickers:
- CLBK
status: stub
canonical_reviewed: false
as_of: '2026-10-23'
updated_at: '2026-10-23T14:35:22.252685+00:00'
reviewed_at: null
coverage_release: coverage-20261023-39968262770-1
source_commit: 3f697433c3580d4ca83edbe44c66580ac926c8d7
financial_history_available: true
curated_research: null
financial_gap:
  reason: available
  next_action: Retain dated financial evidence and review blocked metrics before analytical
    use.
  observed_forms:
  - 10-Q
  - '3'
  - '4'
  - 424B3
  - 8-K
  - 8-K/A
  - 8-K12B
  - EFFECT
  - FWP
  - POS AM
  - S-1
  - S-1/A
  - S-4
  - S-4/A
  - S-8
input_sources:
  history:
    url: https://data.sec.gov/api/xbrl/companyfacts/CIK0002115119.json
    sha256: b33633bd73188bd237c0465b6a2f6e28b9fb7c9466d28df925fa0d0e79438d31
    retrieved_at: '2026-10-22T17:53:02.398600+00:00'
    archive:
      member: CIK0002115119.json
      sha256: 7457a528288f1e3425cba6ffd7370c6c205845aba12761763aa5ae3683c0fdc2
      url: https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip
    acquisition: operator_supplied_sec_bulk_archive
  submissions:
    url: https://data.sec.gov/submissions/CIK0002115119.json
    sha256: a97bb2f95cb536fe27b5b5c09c3281a93cf47d6ab80e5d54da611b36b0503aef
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0002115119.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: nasdaqlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt
  published_at: null
  retrieved_at: '2026-10-23T14:17:54.530395+00:00'
  sha256: a31379ea4791bd232005b22547c9cfa517e0cb9e9f14ff7091be845f143d5c71
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0002115119.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: a97bb2f95cb536fe27b5b5c09c3281a93cf47d6ab80e5d54da611b36b0503aef
- id: S03
  title: SEC CompanyFacts source
  url: https://data.sec.gov/api/xbrl/companyfacts/CIK0002115119.json
  published_at: null
  retrieved_at: '2026-10-22T17:53:02.398600+00:00'
  sha256: b33633bd73188bd237c0465b6a2f6e28b9fb7c9466d28df925fa0d0e79438d31
- id: S04
  title: 10-Q 0002115119-26-000030
  url: https://www.sec.gov/Archives/edgar/data/2115119/000211511926000030/0002115119-26-000030-index.html
  published_at: '2026-08-07'
  retrieved_at: '2026-10-22T17:53:02.398600+00:00'
  sha256: null
- id: S05
  title: 4 0001729897-26-000053
  url: https://www.sec.gov/Archives/edgar/data/2115119/000172989726000053/0001729897-26-000053-index.html
  published_at: '2026-10-20'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 4 0001729859-26-000055
  url: https://www.sec.gov/Archives/edgar/data/2115119/000172985926000055/0001729859-26-000055-index.html
  published_at: '2026-10-20'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 4 0001729897-26-000052
  url: https://www.sec.gov/Archives/edgar/data/2115119/000172989726000052/0001729897-26-000052-index.html
  published_at: '2026-10-06'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S08
  title: 4 0001729859-26-000054
  url: https://www.sec.gov/Archives/edgar/data/2115119/000172985926000054/0001729859-26-000054-index.html
  published_at: '2026-10-06'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S09
  title: 4 0001729840-26-000034
  url: https://www.sec.gov/Archives/edgar/data/2115119/000172984026000034/0001729840-26-000034-index.html
  published_at: '2026-10-06'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0002115119
  classification_status: reported_sic
  entity_type: operating
  name: Columbia Financial, Inc./MD/
  sic: '6035'
  sic_description: Savings Institution, Federally Chartered
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: a97bb2f95cb536fe27b5b5c09c3281a93cf47d6ab80e5d54da611b36b0503aef
  url: https://data.sec.gov/submissions/CIK0002115119.json
listings:
- ticker: CLBK
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0002115119-26-000030
  filed: '2026-08-07'
  form: 10-Q
  period_end: '2026-06-30'
  url: https://www.sec.gov/Archives/edgar/data/2115119/000211511926000030/0002115119-26-000030-index.html
- accession: 0002115119-26-000026
  filed: '2026-07-30'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/2115119/000211511926000026/0002115119-26-000026-index.html
- accession: 0002115119-26-000022
  filed: '2026-07-28'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/2115119/000211511926000022/0002115119-26-000022-index.html
research_progress:
  stage: pending
  input_sha256: 1e52743e31e23fc1685a46eeb614e87318a104fd21e376e7b77229cdf66553fa
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
  derived_observations: 0
  model_draft: false
  reviewed: false
sector_assignment:
  sector: financials
  method: project_sic_rule
  sic: '6035'
  sic_description: Savings Institution, Federally Chartered
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0002115119.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/d523cff21b18141b9a37cddd98ad6af6e1a30fa5/brain/companies/CLBK/README.md
full_history_commit: d523cff21b18141b9a37cddd98ad6af6e1a30fa5
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# CLBK — Columbia Financial, Inc./MD/

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/d523cff21b18141b9a37cddd98ad6af6e1a30fa5/brain/companies/CLBK/README.md)

## Business overview

Reported issuer name: **Columbia Financial, Inc./MD/**. Stable SEC CIK: **0002115119**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| CLBK | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **6035**: Savings Institution, Federally Chartered. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **financials**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

## Financial performance

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:53:02.398600+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; missing_annual_anchor, share_split_and_corporate_action_basis_unverified | [S04] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; missing_annual_anchor, share_split_and_corporate_action_basis_unverified | [S04] |
| free_cash_flow | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| gross_profit | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| net_income | Unavailable / blocked | USD | US GAAP / reported / not model usable | NetIncomeLoss; missing_annual_anchor | [S04] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| net_income_including_noncontrolling_interests | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| operating_cash_flow | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| operating_income | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| revenue | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; missing_annual_anchor, share_split_and_corporate_action_basis_unverified | [S04] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; missing_annual_anchor, share_split_and_corporate_action_basis_unverified | [S04] |
| stock_based_compensation | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |

## Balance sheet and capital allocation

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:53:02.398600+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | Unavailable / blocked | USD | US GAAP / reported / not model usable | CashAndCashEquivalentsAtCarryingValue; missing_annual_anchor | [S04] |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebt; debt_scope_requires_filing_review, missing_annual_anchor | [S04] |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; missing_annual_anchor, share_split_and_corporate_action_basis_unverified | [S04] |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |

Not available: reviewed debt maturity, acquisition, dividend and repurchase analysis.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- Collector status: quality_review_required; last action: new_financial_filing; last checked: 2026-10-23T14:34:46.170538+00:00.

### Research work queue

Collection stage: **pending**. Extracted evidence is not a reviewed conclusion. Daily collection resumes from durable state; unchanged accessions are reused.

- **Business overview** (evidence or analysis still needed): Explain what the company does, who pays it, and why the business exists. Cite primary sources.
- **Revenue model and segments** (evidence or analysis still needed): Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.
- **Products and services** (evidence or analysis still needed): Describe the main products, customer problems solved, distribution, and product dependencies.
- **Customers and end markets** (evidence or analysis still needed): Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.
- **Industry and value chain** (evidence or analysis still needed): Place the company among suppliers, distribution channels, customers, and substitutes. Explain cyclicality and supply constraints.
- **Competitive landscape** (evidence or analysis still needed): Identify direct competitors and alternatives. Compare specific products or business segments, with sources.
- **Moat and differentiation** (evidence or analysis still needed): Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.
- **Growth drivers** (evidence or analysis still needed): Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.
- **Financial performance** (evidence or analysis still needed): Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.
- **Balance sheet and capital allocation** (evidence or analysis still needed): Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.
- **Management and governance** (evidence or analysis still needed): Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.
- **Valuation context** (evidence or analysis still needed): Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.
- **Catalysts** (evidence or analysis still needed): List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.
- **Risks and thesis breakers** (evidence or analysis still needed): Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.
- **Scenarios and open questions** (evidence or analysis still needed): Separate bull, base, and bear assumptions from facts. Record missing data, disputed evidence, and research questions without inventing answers.
- **Relationships and themes** (evidence or analysis still needed): Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.
- **Recent developments** (evidence or analysis still needed): Keep a dated, source-backed log of material changes. Distinguish the event date from the article date and explain what changed in the profile.

Calculation gaps: No annual period is available for comparison.

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest five available filing metadata records; document bodies have not been analyzed here.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-10-20 | 4 | 0001729897-26-000053 | — | [S05] |
| 2026-10-20 | 4 | 0001729859-26-000055 | — | [S06] |
| 2026-10-06 | 4 | 0001729897-26-000052 | — | [S07] |
| 2026-10-06 | 4 | 0001729859-26-000054 | — | [S08] |
| 2026-10-06 | 4 | 0001729840-26-000034 | — | [S09] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-23T14:17:54.530395+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0002115119.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [SEC CompanyFacts source](https://data.sec.gov/api/xbrl/companyfacts/CIK0002115119.json) — published not supplied; retrieved 2026-10-22T17:53:02.398600+00:00.

[S04] [10-Q 0002115119-26-000030](https://www.sec.gov/Archives/edgar/data/2115119/000211511926000030/0002115119-26-000030-index.html) — published 2026-08-07; retrieved 2026-10-22T17:53:02.398600+00:00.

[S05] [4 0001729897-26-000053](https://www.sec.gov/Archives/edgar/data/2115119/000172989726000053/0001729897-26-000053-index.html) — published 2026-10-20; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [4 0001729859-26-000055](https://www.sec.gov/Archives/edgar/data/2115119/000172985926000055/0001729859-26-000055-index.html) — published 2026-10-20; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [4 0001729897-26-000052](https://www.sec.gov/Archives/edgar/data/2115119/000172989726000052/0001729897-26-000052-index.html) — published 2026-10-06; retrieved 2026-10-23T08:33:02.691743+00:00.

[S08] [4 0001729859-26-000054](https://www.sec.gov/Archives/edgar/data/2115119/000172985926000054/0001729859-26-000054-index.html) — published 2026-10-06; retrieved 2026-10-23T08:33:02.691743+00:00.

[S09] [4 0001729840-26-000034](https://www.sec.gov/Archives/edgar/data/2115119/000172984026000034/0001729840-26-000034-index.html) — published 2026-10-06; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261023-39968262770-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/d523cff21b18141b9a37cddd98ad6af6e1a30fa5/brain/companies/CLBK/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
