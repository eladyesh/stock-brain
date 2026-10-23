---
schema_version: 1
document_type: company_facts
company_id: company-cik-0000723531
cik: '0000723531'
company_name: PAYCHEX INC
tickers:
- PAYX
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
  - 11-K
  - '144'
  - 144/A
  - '3'
  - '4'
  - 4/A
  - 424B2
  - 424B7
  - '5'
  - 8-K
  - 8-K/A
  - ARS
  - CORRESP
  - DEF 14A
  - DEFA14A
  - FWP
  - S-3ASR
  - S-8
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  history:
    url: https://data.sec.gov/api/xbrl/companyfacts/CIK0000723531.json
    sha256: c14cf3666260c537a546e8e471039bf0b28c1cf9200eb2a1365668647b8c8328
    retrieved_at: '2026-10-22T18:10:35.452616+00:00'
    archive:
      member: CIK0000723531.json
      sha256: 7457a528288f1e3425cba6ffd7370c6c205845aba12761763aa5ae3683c0fdc2
      url: https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip
    acquisition: operator_supplied_sec_bulk_archive
  submissions:
    url: https://data.sec.gov/submissions/CIK0000723531.json
    sha256: 5e4f45d41ab4231466a32c27c7ec9bec2496c8fc892fcbc4339b138349c93619
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0000723531.json
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
  url: https://data.sec.gov/submissions/CIK0000723531.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 5e4f45d41ab4231466a32c27c7ec9bec2496c8fc892fcbc4339b138349c93619
- id: S03
  title: SEC CompanyFacts source
  url: https://data.sec.gov/api/xbrl/companyfacts/CIK0000723531.json
  published_at: null
  retrieved_at: '2026-10-22T18:10:35.452616+00:00'
  sha256: c14cf3666260c537a546e8e471039bf0b28c1cf9200eb2a1365668647b8c8328
- id: S04
  title: 10-K 0001193125-26-307785
  url: https://www.sec.gov/Archives/edgar/data/723531/000119312526307785/0001193125-26-307785-index.html
  published_at: '2026-07-17'
  retrieved_at: '2026-10-22T18:10:35.452616+00:00'
  sha256: null
- id: S05
  title: 10-Q 0000723531-26-000006
  url: https://www.sec.gov/Archives/edgar/data/723531/000072353126000006/0000723531-26-000006-index.html
  published_at: '2026-09-24'
  retrieved_at: '2026-10-22T18:10:35.452616+00:00'
  sha256: null
- id: S17
  title: 144 0001628280-26-066664
  url: https://www.sec.gov/Archives/edgar/data/723531/000162828026066664/0001628280-26-066664-index.html
  published_at: '2026-10-21'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S18
  title: 144 0001628280-26-066645
  url: https://www.sec.gov/Archives/edgar/data/723531/000162828026066645/0001628280-26-066645-index.html
  published_at: '2026-10-21'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S19
  title: 4 0001193125-26-427799
  url: https://www.sec.gov/Archives/edgar/data/723531/000119312526427799/0001193125-26-427799-index.html
  published_at: '2026-10-21'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S20
  title: 4 0001193125-26-424048
  url: https://www.sec.gov/Archives/edgar/data/723531/000119312526424048/0001193125-26-424048-index.html
  published_at: '2026-10-16'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S21
  title: 4 0001193125-26-424047
  url: https://www.sec.gov/Archives/edgar/data/723531/000119312526424047/0001193125-26-424047-index.html
  published_at: '2026-10-16'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: '0000723531'
  classification_status: reported_sic
  entity_type: operating
  name: PAYCHEX INC
  sic: '8700'
  sic_description: Services-Engineering, Accounting, Research, Management
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 5e4f45d41ab4231466a32c27c7ec9bec2496c8fc892fcbc4339b138349c93619
  url: https://data.sec.gov/submissions/CIK0000723531.json
sector_assignment:
  sector: industrials
  method: project_sic_rule
  sic: '8700'
  sic_description: Services-Engineering, Accounting, Research, Management
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0000723531.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/8929b40d1af134561afb621de3adca71dd9577ba/brain/companies/0000723531/README.md
full_history_commit: 8929b40d1af134561afb621de3adca71dd9577ba
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# PAYCHEX INC — PAYX

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/8929b40d1af134561afb621de3adca71dd9577ba/brain/companies/0000723531/README.md)

## Business overview

Reported issuer name: **PAYCHEX INC**. Stable SEC CIK: **0000723531**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| PAYX | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **8700**: Services-Engineering, Accounting, Research, Management. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **industrials**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

## Financial performance

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T18:10:35.452616+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-06-01 to 2026-05-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -234,900,000 | USD | US GAAP / reported | PaymentsToAcquirePropertyPlantAndEquipment; Cash outflow = negative of reported PaymentsToAcquirePropertyPlantAndEquipment; source value retained. | [S04] |
| cost_of_revenue | 1,674,500,000 | USD | US GAAP / reported | CostOfRevenue | [S04] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S04] |
| free_cash_flow | 2,321,800,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment | [S04] |
| gross_profit | Unavailable / blocked | USD | US GAAP / derived / not model usable | CostOfRevenue + RevenueFromContractWithCustomerExcludingAssessedTax; alternative_tag_scope_differs, derived_input_requires_review | [S04] |
| net_income | 1,760,100,000 | USD | US GAAP / reported | NetIncomeLoss | [S04] |
| net_income_common | 1,760,100,000 | USD | US GAAP / reported | NetIncomeLossAvailableToCommonStockholdersBasic | [S04] |
| net_income_including_noncontrolling_interests | 1,760,100,000 | USD | US GAAP / reported | ProfitLoss | [S04] |
| operating_cash_flow | 2,556,700,000 | USD | US GAAP / reported | NetCashProvidedByUsedInOperatingActivities | [S04] |
| operating_income | 2,510,500,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S04] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | RevenueFromContractWithCustomerExcludingAssessedTax; alternative_tag_scope_differs | [S04] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S04] |
| stock_based_compensation | 96,100,000 | USD | US GAAP / reported | ShareBasedCompensation | [S04] |


### quarterly: 2026-06-01 to 2026-08-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -56,100,000 | USD | US GAAP / reported | PaymentsToAcquirePropertyPlantAndEquipment; Cash outflow = negative of reported PaymentsToAcquirePropertyPlantAndEquipment; source value retained. | [S05] |
| cost_of_revenue | 430,100,000 | USD | US GAAP / reported | CostOfRevenue | [S05] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S05] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S05] |
| free_cash_flow | 357,400,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment | [S05] |
| gross_profit | Unavailable / blocked | USD | US GAAP / derived / not model usable | CostOfRevenue + RevenueFromContractWithCustomerExcludingAssessedTax; alternative_tag_scope_differs, derived_input_requires_review | [S05] |
| net_income | 429,700,000 | USD | US GAAP / reported | NetIncomeLoss | [S05] |
| net_income_common | 429,700,000 | USD | US GAAP / reported | NetIncomeLossAvailableToCommonStockholdersBasic | [S05] |
| net_income_including_noncontrolling_interests | 429,700,000 | USD | US GAAP / reported | ProfitLoss | [S05] |
| operating_cash_flow | 413,500,000 | USD | US GAAP / reported | NetCashProvidedByUsedInOperatingActivities | [S05] |
| operating_income | 619,200,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S05] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | RevenueFromContractWithCustomerExcludingAssessedTax; alternative_tag_scope_differs | [S05] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S05] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S05] |
| stock_based_compensation | 19,300,000 | USD | US GAAP / reported | ShareBasedCompensation | [S05] |



## Balance sheet and capital allocation

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T18:10:35.452616+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-06-01 to 2026-05-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 1,088,200,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S05] |
| debt_current | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtCurrent; debt_scope_requires_filing_review | [S04] |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtNoncurrent; debt_scope_requires_filing_review | [S05] |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebt; debt_scope_requires_filing_review | [S05] |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S05] |
| short_term_borrowings | 0 | USD | US GAAP / reported | ShortTermBorrowings | [S04] |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |


### quarterly: 2026-06-01 to 2026-08-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 600,900,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S05] |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
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
- Collector status: quality_review_required; last action: new_financial_filing; last checked: 2026-10-23T14:24:35.745870+00:00.

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest five available filing metadata records; document bodies have not been analyzed here.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-10-21 | 144 | 0001628280-26-066664 | — | [S17] |
| 2026-10-21 | 144 | 0001628280-26-066645 | — | [S18] |
| 2026-10-21 | 4 | 0001193125-26-427799 | — | [S19] |
| 2026-10-16 | 4 | 0001193125-26-424048 | — | [S20] |
| 2026-10-16 | 4 | 0001193125-26-424047 | — | [S21] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-23T14:17:54.530395+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0000723531.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [SEC CompanyFacts source](https://data.sec.gov/api/xbrl/companyfacts/CIK0000723531.json) — published not supplied; retrieved 2026-10-22T18:10:35.452616+00:00.

[S04] [10-K 0001193125-26-307785](https://www.sec.gov/Archives/edgar/data/723531/000119312526307785/0001193125-26-307785-index.html) — published 2026-07-17; retrieved 2026-10-22T18:10:35.452616+00:00.

[S05] [10-Q 0000723531-26-000006](https://www.sec.gov/Archives/edgar/data/723531/000072353126000006/0000723531-26-000006-index.html) — published 2026-09-24; retrieved 2026-10-22T18:10:35.452616+00:00.

[S17] [144 0001628280-26-066664](https://www.sec.gov/Archives/edgar/data/723531/000162828026066664/0001628280-26-066664-index.html) — published 2026-10-21; retrieved 2026-10-23T08:33:02.691743+00:00.

[S18] [144 0001628280-26-066645](https://www.sec.gov/Archives/edgar/data/723531/000162828026066645/0001628280-26-066645-index.html) — published 2026-10-21; retrieved 2026-10-23T08:33:02.691743+00:00.

[S19] [4 0001193125-26-427799](https://www.sec.gov/Archives/edgar/data/723531/000119312526427799/0001193125-26-427799-index.html) — published 2026-10-21; retrieved 2026-10-23T08:33:02.691743+00:00.

[S20] [4 0001193125-26-424048](https://www.sec.gov/Archives/edgar/data/723531/000119312526424048/0001193125-26-424048-index.html) — published 2026-10-16; retrieved 2026-10-23T08:33:02.691743+00:00.

[S21] [4 0001193125-26-424047](https://www.sec.gov/Archives/edgar/data/723531/000119312526424047/0001193125-26-424047-index.html) — published 2026-10-16; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261023-39968262770-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/8929b40d1af134561afb621de3adca71dd9577ba/brain/companies/0000723531/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
