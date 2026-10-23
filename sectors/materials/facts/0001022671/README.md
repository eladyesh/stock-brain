---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001022671
cik: '0001022671'
company_name: STEEL DYNAMICS INC
tickers:
- STLD
status: stub
canonical_reviewed: false
as_of: '2026-10-23'
updated_at: '2026-10-23T14:35:22.252685+00:00'
reviewed_at: null
coverage_release: coverage-20261023-39968262770-1
source_commit: c5f247f1f77b31a20ec1a66533503255600926f7
financial_history_available: true
curated_research: null
financial_gap:
  reason: available
  next_action: Retain dated financial evidence and review blocked metrics before analytical
    use.
  observed_forms:
  - 10-K
  - 10-Q
  - 10-Q/A
  - '144'
  - '3'
  - 3/A
  - '4'
  - 4/A
  - 424B2
  - 424B5
  - 8-K
  - 8-K/A
  - ARS
  - CORRESP
  - DEF 14A
  - DEFA14A
  - FWP
  - S-3ASR
  - SC 13G/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - SD
  - UPLOAD
input_sources:
  history:
    url: https://data.sec.gov/api/xbrl/companyfacts/CIK0001022671.json
    sha256: 05faeb3700549a72e77fc8cdb107ba5bc36b73512de61c7a9a9c0e305a5d5943
    retrieved_at: '2026-10-22T17:39:41.848518+00:00'
    archive:
      member: CIK0001022671.json
      sha256: 7457a528288f1e3425cba6ffd7370c6c205845aba12761763aa5ae3683c0fdc2
      url: https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip
    acquisition: operator_supplied_sec_bulk_archive
  submissions:
    url: https://data.sec.gov/submissions/CIK0001022671.json
    sha256: e71e6a46e5a177584e300f102dd043bddc03c4f8514f4b8fceec1d1e12999746
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001022671.json
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
  url: https://data.sec.gov/submissions/CIK0001022671.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: e71e6a46e5a177584e300f102dd043bddc03c4f8514f4b8fceec1d1e12999746
- id: S03
  title: SEC CompanyFacts source
  url: https://data.sec.gov/api/xbrl/companyfacts/CIK0001022671.json
  published_at: null
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: 05faeb3700549a72e77fc8cdb107ba5bc36b73512de61c7a9a9c0e305a5d5943
- id: S04
  title: 10-K 0001104659-26-021395
  url: https://www.sec.gov/Archives/edgar/data/1022671/000110465926021395/0001104659-26-021395-index.html
  published_at: '2026-02-27'
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: null
- id: S05
  title: 10-Q 0001104659-26-087414
  url: https://www.sec.gov/Archives/edgar/data/1022671/000110465926087414/0001104659-26-087414-index.html
  published_at: '2026-07-28'
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: null
- id: S17
  title: 8-K 0001104659-26-117217
  url: https://www.sec.gov/Archives/edgar/data/1022671/000110465926117217/0001104659-26-117217-index.html
  published_at: '2026-10-20'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S18
  title: 8-K 0001104659-26-116898
  url: https://www.sec.gov/Archives/edgar/data/1022671/000110465926116898/0001104659-26-116898-index.html
  published_at: '2026-10-19'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S19
  title: 4 0001022671-26-000157
  url: https://www.sec.gov/Archives/edgar/data/1022671/000102267126000157/0001022671-26-000157-index.html
  published_at: '2026-10-09'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S20
  title: 4 0001022671-26-000156
  url: https://www.sec.gov/Archives/edgar/data/1022671/000102267126000156/0001022671-26-000156-index.html
  published_at: '2026-10-09'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S21
  title: 4 0001022671-26-000155
  url: https://www.sec.gov/Archives/edgar/data/1022671/000102267126000155/0001022671-26-000155-index.html
  published_at: '2026-10-09'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: '0001022671'
  classification_status: reported_sic
  entity_type: operating
  name: STEEL DYNAMICS INC
  sic: '3312'
  sic_description: Steel Works, Blast Furnaces & Rolling Mills (Coke Ovens)
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: e71e6a46e5a177584e300f102dd043bddc03c4f8514f4b8fceec1d1e12999746
  url: https://data.sec.gov/submissions/CIK0001022671.json
sector_assignment:
  sector: materials
  method: project_sic_rule
  sic: '3312'
  sic_description: Steel Works, Blast Furnaces & Rolling Mills (Coke Ovens)
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001022671.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/8929b40d1af134561afb621de3adca71dd9577ba/brain/companies/0001022671/README.md
full_history_commit: 8929b40d1af134561afb621de3adca71dd9577ba
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# STEEL DYNAMICS INC — STLD

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/8929b40d1af134561afb621de3adca71dd9577ba/brain/companies/0001022671/README.md)

## Business overview

Reported issuer name: **STEEL DYNAMICS INC**. Stable SEC CIK: **0001022671**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| STLD | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **3312**: Steel Works, Blast Furnaces & Rolling Mills (Coke Ovens). [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **materials**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

## Financial performance

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:39:41.848518+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-01-01 to 2025-12-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -948,025,000 | USD | US GAAP / reported | PaymentsToAcquirePropertyPlantAndEquipment; Cash outflow = negative of reported PaymentsToAcquirePropertyPlantAndEquipment; source value retained. | [S04] |
| cost_of_revenue | 15,784,398,000 | USD | US GAAP / reported | CostOfGoodsAndServicesSold | [S04] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S04] |
| free_cash_flow | 501,509,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment | [S04] |
| gross_profit | 2,392,183,000 | USD | US GAAP / reported | GrossProfit | [S04] |
| net_income | 1,185,595,000 | USD | US GAAP / reported | NetIncomeLoss | [S04] |
| net_income_common | 1,185,595,000 | USD | US GAAP / reported | NetIncomeLossAvailableToCommonStockholdersBasic | [S04] |
| net_income_including_noncontrolling_interests | 1,187,311,000 | USD | US GAAP / reported | ProfitLoss | [S04] |
| operating_cash_flow | 1,449,534,000 | USD | US GAAP / reported | NetCashProvidedByUsedInOperatingActivities | [S04] |
| operating_income | 1,475,986,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S04] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | 18,176,581,000 | USD | US GAAP / reported | RevenueFromContractWithCustomerExcludingAssessedTax | [S04] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S04] |
| stock_based_compensation | 68,983,000 | USD | US GAAP / reported | ShareBasedCompensation | [S04] |


### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -123,842,000 | USD | US GAAP / reported | PaymentsToAcquirePropertyPlantAndEquipment; Cash outflow = negative of reported PaymentsToAcquirePropertyPlantAndEquipment; source value retained. | [S05] |
| cost_of_revenue | 5,132,583,000 | USD | US GAAP / reported | CostOfGoodsAndServicesSold | [S05] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S05] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S05] |
| free_cash_flow | 304,094,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment | [S05] |
| gross_profit | 958,974,000 | USD | US GAAP / reported | GrossProfit | [S05] |
| net_income | 534,087,000 | USD | US GAAP / reported | NetIncomeLoss | [S05] |
| net_income_common | 534,087,000 | USD | US GAAP / reported | NetIncomeLossAvailableToCommonStockholdersBasic | [S05] |
| net_income_including_noncontrolling_interests | 530,785,000 | USD | US GAAP / reported | ProfitLoss | [S05] |
| operating_cash_flow | 427,936,000 | USD | US GAAP / reported | NetCashProvidedByUsedInOperatingActivities | [S05] |
| operating_income | 700,479,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S05] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | 6,091,557,000 | USD | US GAAP / reported | RevenueFromContractWithCustomerExcludingAssessedTax | [S05] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S05] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S05] |
| stock_based_compensation | 14,162,000 | USD | US GAAP / reported | ShareBasedCompensation | [S05] |



## Balance sheet and capital allocation

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:39:41.848518+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-01-01 to 2025-12-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 769,878,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S05] |
| debt_current | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtCurrent; debt_scope_requires_filing_review | [S05] |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtNoncurrent; debt_scope_requires_filing_review | [S05] |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebt; debt_scope_requires_filing_review, revision_requires_review | [S05] |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S05] |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | 0 | USD | US GAAP / reported | ShortTermInvestments | [S04] |


### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 567,708,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S05] |
| debt_current | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtCurrent; debt_scope_requires_filing_review | [S05] |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtNoncurrent; debt_scope_requires_filing_review | [S05] |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebt; debt_scope_requires_filing_review | [S05] |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S05] |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |



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
- Collector status: quality_review_required; last action: new_financial_filing; last checked: 2026-10-23T14:27:02.113926+00:00.

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest five available filing metadata records; document bodies have not been analyzed here.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-10-20 | 8-K | 0001104659-26-117217 | — | [S17] |
| 2026-10-19 | 8-K | 0001104659-26-116898 | — | [S18] |
| 2026-10-09 | 4 | 0001022671-26-000157 | — | [S19] |
| 2026-10-09 | 4 | 0001022671-26-000156 | — | [S20] |
| 2026-10-09 | 4 | 0001022671-26-000155 | — | [S21] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-23T14:17:54.530395+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001022671.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [SEC CompanyFacts source](https://data.sec.gov/api/xbrl/companyfacts/CIK0001022671.json) — published not supplied; retrieved 2026-10-22T17:39:41.848518+00:00.

[S04] [10-K 0001104659-26-021395](https://www.sec.gov/Archives/edgar/data/1022671/000110465926021395/0001104659-26-021395-index.html) — published 2026-02-27; retrieved 2026-10-22T17:39:41.848518+00:00.

[S05] [10-Q 0001104659-26-087414](https://www.sec.gov/Archives/edgar/data/1022671/000110465926087414/0001104659-26-087414-index.html) — published 2026-07-28; retrieved 2026-10-22T17:39:41.848518+00:00.

[S17] [8-K 0001104659-26-117217](https://www.sec.gov/Archives/edgar/data/1022671/000110465926117217/0001104659-26-117217-index.html) — published 2026-10-20; retrieved 2026-10-23T08:33:02.691743+00:00.

[S18] [8-K 0001104659-26-116898](https://www.sec.gov/Archives/edgar/data/1022671/000110465926116898/0001104659-26-116898-index.html) — published 2026-10-19; retrieved 2026-10-23T08:33:02.691743+00:00.

[S19] [4 0001022671-26-000157](https://www.sec.gov/Archives/edgar/data/1022671/000102267126000157/0001022671-26-000157-index.html) — published 2026-10-09; retrieved 2026-10-23T08:33:02.691743+00:00.

[S20] [4 0001022671-26-000156](https://www.sec.gov/Archives/edgar/data/1022671/000102267126000156/0001022671-26-000156-index.html) — published 2026-10-09; retrieved 2026-10-23T08:33:02.691743+00:00.

[S21] [4 0001022671-26-000155](https://www.sec.gov/Archives/edgar/data/1022671/000102267126000155/0001022671-26-000155-index.html) — published 2026-10-09; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261023-39968262770-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/8929b40d1af134561afb621de3adca71dd9577ba/brain/companies/0001022671/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
