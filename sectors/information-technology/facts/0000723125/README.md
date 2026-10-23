---
schema_version: 1
document_type: company_facts
company_id: company-cik-0000723125
cik: '0000723125'
company_name: MICRON TECHNOLOGY INC
tickers:
- MU
status: stub
canonical_reviewed: false
as_of: '2026-10-23'
updated_at: '2026-10-23T14:35:22.252685+00:00'
reviewed_at: null
coverage_release: coverage-20261023-39968262770-1
source_commit: c5f247f1f77b31a20ec1a66533503255600926f7
financial_history_available: true
curated_research:
  url: https://github.com/eladyesh/stock-brain/blob/c5f247f1f77b31a20ec1a66533503255600926f7/sectors/information-technology/companies/MU/README.md
  status: reviewed
  as_of: '2026-10-18'
  sector: information-technology
financial_gap:
  reason: available
  next_action: Retain dated financial evidence and review blocked metrics before analytical
    use.
  observed_forms:
  - 10-K
  - 10-Q
  - '144'
  - 144/A
  - 15-12G
  - '25'
  - '3'
  - 305B2
  - '4'
  - 4/A
  - 424B2
  - 424B5
  - '5'
  - 8-A12B/A
  - 8-K
  - 8-K/A
  - ARS
  - CORRESP
  - DEF 14A
  - DEFA14A
  - FWP
  - PRE 14A
  - S-3ASR
  - S-8
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - SD
  - UPLOAD
input_sources:
  history:
    url: https://data.sec.gov/api/xbrl/companyfacts/CIK0000723125.json
    sha256: 162439f31208eaf4cd1a33939d80fd40479a559735b9488d32ac43d5516ff7bf
    retrieved_at: '2026-10-23T08:48:00.843518+00:00'
  submissions:
    url: https://data.sec.gov/submissions/CIK0000723125.json
    sha256: 326d7461712f6da1214ff1c4b68bf11e17779260665a65bcc57a3bd955138876
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0000723125.json
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
  url: https://data.sec.gov/submissions/CIK0000723125.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 326d7461712f6da1214ff1c4b68bf11e17779260665a65bcc57a3bd955138876
- id: S03
  title: SEC CompanyFacts source
  url: https://data.sec.gov/api/xbrl/companyfacts/CIK0000723125.json
  published_at: null
  retrieved_at: '2026-10-23T08:48:00.843518+00:00'
  sha256: 162439f31208eaf4cd1a33939d80fd40479a559735b9488d32ac43d5516ff7bf
- id: S04
  title: 10-K 0000723125-26-000023
  url: https://www.sec.gov/Archives/edgar/data/723125/000072312526000023/0000723125-26-000023-index.html
  published_at: '2026-10-09'
  retrieved_at: '2026-10-23T08:48:00.843518+00:00'
  sha256: null
- id: S09
  title: 10-Q 0000723125-26-000015
  url: https://www.sec.gov/Archives/edgar/data/723125/000072312526000015/0000723125-26-000015-index.html
  published_at: '2026-06-25'
  retrieved_at: '2026-10-23T08:48:00.843518+00:00'
  sha256: null
- id: S18
  title: 4 0001568238-26-000003
  url: https://www.sec.gov/Archives/edgar/data/723125/000156823826000003/0001568238-26-000003-index.html
  published_at: '2026-10-20'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S19
  title: 4 0002058781-26-000003
  url: https://www.sec.gov/Archives/edgar/data/723125/000205878126000003/0002058781-26-000003-index.html
  published_at: '2026-10-15'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S20
  title: 4 0002058769-26-000006
  url: https://www.sec.gov/Archives/edgar/data/723125/000205876926000006/0002058769-26-000006-index.html
  published_at: '2026-10-15'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S21
  title: 144 0001965301-26-000160
  url: https://www.sec.gov/Archives/edgar/data/723125/000196530126000160/0001965301-26-000160-index.html
  published_at: '2026-10-15'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S22
  title: 4 0001798757-26-000009
  url: https://www.sec.gov/Archives/edgar/data/723125/000179875726000009/0001798757-26-000009-index.html
  published_at: '2026-10-15'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: '0000723125'
  classification_status: reported_sic
  entity_type: operating
  name: MICRON TECHNOLOGY INC
  sic: '3674'
  sic_description: Semiconductors & Related Devices
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 326d7461712f6da1214ff1c4b68bf11e17779260665a65bcc57a3bd955138876
  url: https://data.sec.gov/submissions/CIK0000723125.json
sector_assignment:
  sector: information-technology
  method: curated_profile
  sic: '3674'
  sic_description: Semiconductors & Related Devices
  rule_version: 1
  reason: Uses the dated curated profile assignment; automatic data does not renew
    its review.
  source_url: https://github.com/eladyesh/stock-brain/blob/c5f247f1f77b31a20ec1a66533503255600926f7/sectors/information-technology/companies/MU/README.md
full_history_url: https://github.com/eladyesh/stock-brain/blob/8929b40d1af134561afb621de3adca71dd9577ba/brain/companies/0000723125/README.md
full_history_commit: 8929b40d1af134561afb621de3adca71dd9577ba
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# MICRON TECHNOLOGY INC — MU

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/8929b40d1af134561afb621de3adca71dd9577ba/brain/companies/0000723125/README.md)

## Business overview

Reported issuer name: **MICRON TECHNOLOGY INC**. Stable SEC CIK: **0000723125**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| MU | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **3674**: Semiconductors & Related Devices. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **information-technology**. Method: `curated_profile`. Uses the dated curated profile assignment; automatic data does not renew its review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

## Financial performance

Evidence cutoff: 2026-10-23. Source retrieved: 2026-10-23T08:48:00.843518+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-08-29 to 2026-09-03

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -30,712,000,000 | USD | US GAAP / reported | PaymentsToAcquirePropertyPlantAndEquipment; Cash outflow = negative of reported PaymentsToAcquirePropertyPlantAndEquipment; source value retained. | [S04] |
| cost_of_revenue | 25,684,000,000 | USD | US GAAP / reported | CostOfGoodsAndServicesSold | [S04] |
| eps_basic | 75.38 | USD/shares | US GAAP / reported | EarningsPerShareBasic; filing_scope_verified | [S04] |
| eps_diluted | 74.33 | USD/shares | US GAAP / reported | EarningsPerShareDiluted; filing_scope_verified | [S04] |
| free_cash_flow | 58,963,000,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment | [S04] |
| gross_profit | 107,504,000,000 | USD | US GAAP / reported | GrossProfit | [S04] |
| net_income | 84,969,000,000 | USD | US GAAP / reported | NetIncomeLoss | [S04] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income_including_noncontrolling_interests | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| operating_cash_flow | 89,675,000,000 | USD | US GAAP / reported | NetCashProvidedByUsedInOperatingActivities | [S04] |
| operating_income | 99,340,000,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S04] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | 133,188,000,000 | USD | US GAAP / reported | RevenueFromContractWithCustomerExcludingAssessedTax | [S04] |
| shares_basic | 1,127,000,000 | shares | US GAAP / reported | WeightedAverageNumberOfSharesOutstandingBasic; filing_scope_verified | [S04] |
| shares_diluted | 1,143,000,000 | shares | US GAAP / reported | WeightedAverageNumberOfDilutedSharesOutstanding; filing_scope_verified | [S04] |
| stock_based_compensation | 1,333,000,000 | USD | US GAAP / reported | ShareBasedCompensation | [S04] |


### quarterly: 2026-05-29 to 2026-09-03

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -11,110,000,000 | USD | US GAAP / derived | PaymentsToAcquirePropertyPlantAndEquipment; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S09] |
| cost_of_revenue | 7,182,000,000 | USD | US GAAP / derived | CostOfGoodsAndServicesSold; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S09] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| free_cash_flow | 32,863,000,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S09] |
| gross_profit | 47,047,000,000 | USD | US GAAP / derived | GrossProfit; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S09] |
| net_income | 37,701,000,000 | USD | US GAAP / derived | NetIncomeLoss; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S09] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income_including_noncontrolling_interests | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| operating_cash_flow | 43,973,000,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S09] |
| operating_income | 43,751,000,000 | USD | US GAAP / derived | OperatingIncomeLoss; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S09] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | 54,229,000,000 | USD | US GAAP / derived | RevenueFromContractWithCustomerExcludingAssessedTax; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S09] |
| shares_basic | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_diluted | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| stock_based_compensation | 379,000,000 | USD | US GAAP / derived | ShareBasedCompensation; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S09] |



## Balance sheet and capital allocation

Evidence cutoff: 2026-10-23. Source retrieved: 2026-10-23T08:48:00.843518+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-08-29 to 2026-09-03

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 38,364,000,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S04] |
| debt_current | 491,000,000 | USD | US GAAP / reported | DebtCurrent; filing_scope_verified | [S04] |
| debt_noncurrent | 4,688,000,000 | USD | US GAAP / reported | LongTermDebtAndCapitalLeaseObligations; filing_scope_verified | [S04] |
| debt_total | 5,179,000,000 | USD | US GAAP / reported | DebtAndCapitalLeaseObligations; filing_scope_verified | [S04] |
| long_term_debt_total | 2,792,000,000 | USD | US GAAP / reported | LongTermDebt; filing_scope_verified | [S04] |
| shares_outstanding | 1,131,000,000 | shares | US GAAP / reported | CommonStockSharesOutstanding; filing_scope_verified | [S04] |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |


### quarterly: 2026-05-29 to 2026-09-03

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 38,364,000,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S04] |
| debt_current | 491,000,000 | USD | US GAAP / reported | DebtCurrent; filing_scope_verified | [S04] |
| debt_noncurrent | 4,688,000,000 | USD | US GAAP / reported | LongTermDebtAndCapitalLeaseObligations; filing_scope_verified | [S04] |
| debt_total | 5,179,000,000 | USD | US GAAP / reported | DebtAndCapitalLeaseObligations; filing_scope_verified | [S04] |
| long_term_debt_total | 2,792,000,000 | USD | US GAAP / reported | LongTermDebt; filing_scope_verified | [S04] |
| shares_outstanding | 1,131,000,000 | shares | US GAAP / reported | CommonStockSharesOutstanding; filing_scope_verified | [S04] |
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
- Collector status: quality_review_required; last action: new_financial_filing; last checked: 2026-10-23T14:24:35.100422+00:00.

Dated curated research is maintained separately: [profile at source commit](https://github.com/eladyesh/stock-brain/blob/c5f247f1f77b31a20ec1a66533503255600926f7/sectors/information-technology/companies/MU/README.md) (status reviewed, as of 2026-10-18). Automatic facts never change its review date.

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest five available filing metadata records; document bodies have not been analyzed here.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-10-20 | 4 | 0001568238-26-000003 | — | [S18] |
| 2026-10-15 | 4 | 0002058781-26-000003 | — | [S19] |
| 2026-10-15 | 4 | 0002058769-26-000006 | — | [S20] |
| 2026-10-15 | 144 | 0001965301-26-000160 | — | [S21] |
| 2026-10-15 | 4 | 0001798757-26-000009 | — | [S22] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-23T14:17:54.530395+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0000723125.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [SEC CompanyFacts source](https://data.sec.gov/api/xbrl/companyfacts/CIK0000723125.json) — published not supplied; retrieved 2026-10-23T08:48:00.843518+00:00.

[S04] [10-K 0000723125-26-000023](https://www.sec.gov/Archives/edgar/data/723125/000072312526000023/0000723125-26-000023-index.html) — published 2026-10-09; retrieved 2026-10-23T08:48:00.843518+00:00.

[S09] [10-Q 0000723125-26-000015](https://www.sec.gov/Archives/edgar/data/723125/000072312526000015/0000723125-26-000015-index.html) — published 2026-06-25; retrieved 2026-10-23T08:48:00.843518+00:00.

[S18] [4 0001568238-26-000003](https://www.sec.gov/Archives/edgar/data/723125/000156823826000003/0001568238-26-000003-index.html) — published 2026-10-20; retrieved 2026-10-23T08:33:02.691743+00:00.

[S19] [4 0002058781-26-000003](https://www.sec.gov/Archives/edgar/data/723125/000205878126000003/0002058781-26-000003-index.html) — published 2026-10-15; retrieved 2026-10-23T08:33:02.691743+00:00.

[S20] [4 0002058769-26-000006](https://www.sec.gov/Archives/edgar/data/723125/000205876926000006/0002058769-26-000006-index.html) — published 2026-10-15; retrieved 2026-10-23T08:33:02.691743+00:00.

[S21] [144 0001965301-26-000160](https://www.sec.gov/Archives/edgar/data/723125/000196530126000160/0001965301-26-000160-index.html) — published 2026-10-15; retrieved 2026-10-23T08:33:02.691743+00:00.

[S22] [4 0001798757-26-000009](https://www.sec.gov/Archives/edgar/data/723125/000179875726000009/0001798757-26-000009-index.html) — published 2026-10-15; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261023-39968262770-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/8929b40d1af134561afb621de3adca71dd9577ba/brain/companies/0000723125/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
