---
schema_version: 1
document_type: company_facts
company_id: company-cik-0000104169
cik: 0000104169
company_name: Walmart Inc.
tickers:
- WMT
status: stub
canonical_reviewed: false
as_of: '2026-10-28'
updated_at: '2026-10-28T16:13:42.115634+00:00'
reviewed_at: null
coverage_release: coverage-20261028-40722802424-1
source_commit: 48056b79cf1dc5f5270bd576defc5c9bc49d62cf
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
  - 13F-HR
  - 13F-HR/A
  - '144'
  - 144/A
  - '25'
  - 25-NSE
  - '3'
  - '4'
  - 424B2
  - 424B5
  - 8-A12B
  - 8-K
  - 8-K/A
  - ARS
  - CERT
  - DEF 14A
  - DEFA14A
  - FWP
  - IRANNOTICE
  - N-PX
  - PRE 14A
  - PX14A6G
  - S-3ASR
  - S-8
  - S-8 POS
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13D
  - SCHEDULE 13D/A
  - SCHEDULE 13G/A
  - SD
input_sources:
  history:
    url: https://data.sec.gov/api/xbrl/companyfacts/CIK0000104169.json
    sha256: 49330f98609f70fcef4054edc90bc811398a58c4bf26dc0b218d607967a8dbe4
    retrieved_at: '2026-10-22T18:10:35.452616+00:00'
    archive:
      member: CIK0000104169.json
      sha256: 7457a528288f1e3425cba6ffd7370c6c205845aba12761763aa5ae3683c0fdc2
      url: https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip
    acquisition: operator_supplied_sec_bulk_archive
  submissions:
    url: https://data.sec.gov/submissions/CIK0000104169.json
    sha256: 4a201414e6dd0202fc0ca176b84bdcd62a98015db81fc965b2907a0ffc723e9a
    retrieved_at: '2026-10-24T13:22:51.759433+00:00'
    archive: &id001
      member: CIK0000104169.json
      sha256: 593fbbea6512ef5ec729a5e513c465fbedaac8a66602c0abe00d0ba5a4d18732
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: nasdaqlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt
  published_at: null
  retrieved_at: '2026-10-28T16:09:01.738588+00:00'
  sha256: b555e192b928396dc88877226e82c2c8e9470c389cf2def559495683c673510d
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0000104169.json
  published_at: null
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 4a201414e6dd0202fc0ca176b84bdcd62a98015db81fc965b2907a0ffc723e9a
- id: S03
  title: SEC CompanyFacts source
  url: https://data.sec.gov/api/xbrl/companyfacts/CIK0000104169.json
  published_at: null
  retrieved_at: '2026-10-22T18:10:35.452616+00:00'
  sha256: 49330f98609f70fcef4054edc90bc811398a58c4bf26dc0b218d607967a8dbe4
- id: S04
  title: 10-K 0000104169-26-000055
  url: https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.html
  published_at: '2026-03-13'
  retrieved_at: '2026-10-22T18:10:35.452616+00:00'
  sha256: null
- id: S05
  title: 10-Q 0000104169-26-000154
  url: https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.html
  published_at: '2026-08-28'
  retrieved_at: '2026-10-22T18:10:35.452616+00:00'
  sha256: null
- id: S09
  title: 10-Q 0000104169-26-000102
  url: https://www.sec.gov/Archives/edgar/data/104169/000010416926000102/0000104169-26-000102-index.html
  published_at: '2026-05-29'
  retrieved_at: '2026-10-22T18:10:35.452616+00:00'
  sha256: null
- id: S15
  title: 8-K 0001193125-26-429539
  url: https://www.sec.gov/Archives/edgar/data/104169/000119312526429539/0001193125-26-429539-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S16
  title: 424B5 0001193125-26-427928
  url: https://www.sec.gov/Archives/edgar/data/104169/000119312526427928/0001193125-26-427928-index.html
  published_at: '2026-10-21'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S17
  title: 424B5 0001193125-26-427921
  url: https://www.sec.gov/Archives/edgar/data/104169/000119312526427921/0001193125-26-427921-index.html
  published_at: '2026-10-21'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S18
  title: FWP 0001193125-26-425645
  url: https://www.sec.gov/Archives/edgar/data/104169/000119312526425645/0001193125-26-425645-index.html
  published_at: '2026-10-20'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S19
  title: FWP 0001193125-26-425644
  url: https://www.sec.gov/Archives/edgar/data/104169/000119312526425644/0001193125-26-425644-index.html
  published_at: '2026-10-20'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
issuer_classification:
  cik: 0000104169
  classification_status: reported_sic
  entity_type: operating
  name: Walmart Inc.
  sic: '5331'
  sic_description: Retail-Variety Stores
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 4a201414e6dd0202fc0ca176b84bdcd62a98015db81fc965b2907a0ffc723e9a
  url: https://data.sec.gov/submissions/CIK0000104169.json
listings:
- ticker: WMT
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0000104169-26-000055
  filed: '2026-03-13'
  form: 10-K
  period_end: '2026-01-31'
  url: https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.html
- accession: 0000104169-26-000154
  filed: '2026-08-28'
  form: 10-Q
  period_end: '2026-07-31'
  url: https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.html
- accession: 0001193125-26-173673
  filed: '2026-04-23'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/104169/000119312526173673/0001193125-26-173673-index.html
- accession: 0001193125-26-429539
  filed: '2026-10-23'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/104169/000119312526429539/0001193125-26-429539-index.html
- accession: 0000104169-26-000028
  filed: '2026-01-30'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/104169/000010416926000028/0000104169-26-000028-index.html
- accession: 0000104169-26-000024
  filed: '2026-01-16'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/104169/000010416926000024/0000104169-26-000024-index.html
research_progress:
  stage: pending
  input_sha256: ad61797ee859175e6fea4ef93fcfb8ef57b2b804a6256d1d42c32b8163858b34
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
  derived_observations: 5
  model_draft: false
  reviewed: false
sector_assignment:
  sector: consumer-discretionary
  method: project_sic_rule
  sic: '5331'
  sic_description: Retail-Variety Stores
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0000104169.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/d9e673c37aaa38580be4e36b4880e8ab015a9390/brain/companies/WMT/README.md
full_history_commit: d9e673c37aaa38580be4e36b4880e8ab015a9390
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# WMT — Walmart Inc.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/d9e673c37aaa38580be4e36b4880e8ab015a9390/brain/companies/WMT/README.md)

## Business overview

Reported issuer name: **Walmart Inc.**. Stable SEC CIK: **0000104169**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| WMT | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **5331**: Retail-Variety Stores. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **consumer-discretionary**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

## Financial performance

Derived observation: Annual operating income changed +1.63% from the year ended 2025-01-31 to 2026-01-31. [S04]
Formula: `(current / prior - 1) * 100`. Inputs: operating_income=29825000000 USD (OperatingIncomeLoss), operating_income=29348000000 USD (OperatingIncomeLoss).

Derived observation: Annual net income changed +12.64% from the year ended 2025-01-31 to 2026-01-31. [S04]
Formula: `(current / prior - 1) * 100`. Inputs: net_income=21893000000 USD (NetIncomeLoss), net_income=19436000000 USD (NetIncomeLoss).

Derived observation: Annual operating cash flow changed +14.05% from the year ended 2025-01-31 to 2026-01-31. [S04]
Formula: `(current / prior - 1) * 100`. Inputs: operating_cash_flow=41565000000 USD (NetCashProvidedByUsedInOperatingActivities), operating_cash_flow=36443000000 USD (NetCashProvidedByUsedInOperatingActivities).

Derived observation: Annual free cash flow changed +17.88% from the year ended 2025-01-31 to 2026-01-31. [S04]
Formula: `(current / prior - 1) * 100`. Inputs: free_cash_flow=14923000000 USD (NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment), free_cash_flow=12660000000 USD (NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment).

Derived observation: Operating cash flow / net income was 1.90x for the year ended 2026-01-31. Working capital and non-cash adjustments require separate filing analysis. [S04]
Formula: `operating_cash_flow / net_income`. Inputs: operating_cash_flow=41565000000 USD (NetCashProvidedByUsedInOperatingActivities), net_income=21893000000 USD (NetIncomeLoss).

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T18:10:35.452616+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-02-01 to 2026-01-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -26,642,000,000 | USD | US GAAP / reported | PaymentsToAcquirePropertyPlantAndEquipment; Cash outflow = negative of reported PaymentsToAcquirePropertyPlantAndEquipment; source value retained. | [S04] |
| cost_of_revenue | 535,395,000,000 | USD | US GAAP / reported | CostOfRevenue | [S04] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S04] |
| free_cash_flow | 14,923,000,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment | [S04] |
| gross_profit | Unavailable / blocked | USD | US GAAP / derived / not model usable | CostOfRevenue + RevenueFromContractWithCustomerExcludingAssessedTax; alternative_tag_scope_differs, derived_input_requires_review | [S04] |
| net_income | 21,893,000,000 | USD | US GAAP / reported | NetIncomeLoss | [S04] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income_including_noncontrolling_interests | 22,270,000,000 | USD | US GAAP / reported | ProfitLoss | [S04] |
| operating_cash_flow | 41,565,000,000 | USD | US GAAP / reported | NetCashProvidedByUsedInOperatingActivities | [S04] |
| operating_income | 29,825,000,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S04] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | RevenueFromContractWithCustomerExcludingAssessedTax; alternative_tag_scope_differs | [S04] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S04] |
| stock_based_compensation | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |


### quarterly: 2026-05-01 to 2026-07-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -7,497,000,000 | USD | US GAAP / derived | PaymentsToAcquirePropertyPlantAndEquipment; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S05] [S09] |
| cost_of_revenue | 138,804,000,000 | USD | US GAAP / reported | CostOfRevenue | [S05] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S05] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S05] |
| free_cash_flow | 7,475,000,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S05] [S09] |
| gross_profit | Unavailable / blocked | USD | US GAAP / derived / not model usable | CostOfRevenue + RevenueFromContractWithCustomerExcludingAssessedTax; alternative_tag_scope_differs, derived_input_requires_review | [S05] |
| net_income | 6,366,000,000 | USD | US GAAP / reported | NetIncomeLoss | [S05] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income_including_noncontrolling_interests | 6,529,000,000 | USD | US GAAP / reported | ProfitLoss | [S05] |
| operating_cash_flow | 14,972,000,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S05] [S09] |
| operating_income | 9,383,000,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S05] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | RevenueFromContractWithCustomerExcludingAssessedTax; alternative_tag_scope_differs | [S05] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S05] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S05] |
| stock_based_compensation | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |



## Balance sheet and capital allocation

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T18:10:35.452616+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-02-01 to 2026-01-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 10,727,000,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S05] |
| debt_current | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtCurrent; debt_scope_requires_filing_review | [S05] |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtNoncurrent; debt_scope_requires_filing_review | [S05] |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebt; debt_scope_requires_filing_review | [S04] |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_borrowings | 6,596,000,000 | USD | US GAAP / reported | ShortTermBorrowings | [S05] |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |


### quarterly: 2026-05-01 to 2026-07-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 11,529,000,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S05] |
| debt_current | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtCurrent; debt_scope_requires_filing_review | [S05] |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtNoncurrent; debt_scope_requires_filing_review | [S05] |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_borrowings | 10,479,000,000 | USD | US GAAP / reported | ShortTermBorrowings | [S05] |
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
- Collector status: quality_review_required; last action: new_financial_filing; last checked: 2026-10-24T13:28:16.711918+00:00.

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

Calculation gaps: Operating margin: compatible positive revenue and usable inputs are required. Net margin: compatible positive revenue and usable inputs are required. Free cash flow margin: compatible positive revenue and usable inputs are required. Stock compensation / revenue: compatible positive revenue and usable inputs are required. revenue: annual growth withheld because periods, definitions or a positive prior denominator are not verified.

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest five available filing metadata records; document bodies have not been analyzed here.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-10-23 | 8-K | 0001193125-26-429539 | — | [S15] |
| 2026-10-21 | 424B5 | 0001193125-26-427928 | — | [S16] |
| 2026-10-21 | 424B5 | 0001193125-26-427921 | — | [S17] |
| 2026-10-20 | FWP | 0001193125-26-425645 | — | [S18] |
| 2026-10-20 | FWP | 0001193125-26-425644 | — | [S19] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-28T16:09:01.738588+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0000104169.json) — published not supplied; retrieved 2026-10-24T13:22:51.759433+00:00.

[S03] [SEC CompanyFacts source](https://data.sec.gov/api/xbrl/companyfacts/CIK0000104169.json) — published not supplied; retrieved 2026-10-22T18:10:35.452616+00:00.

[S04] [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.html) — published 2026-03-13; retrieved 2026-10-22T18:10:35.452616+00:00.

[S05] [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.html) — published 2026-08-28; retrieved 2026-10-22T18:10:35.452616+00:00.

[S09] [10-Q 0000104169-26-000102](https://www.sec.gov/Archives/edgar/data/104169/000010416926000102/0000104169-26-000102-index.html) — published 2026-05-29; retrieved 2026-10-22T18:10:35.452616+00:00.

[S15] [8-K 0001193125-26-429539](https://www.sec.gov/Archives/edgar/data/104169/000119312526429539/0001193125-26-429539-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S16] [424B5 0001193125-26-427928](https://www.sec.gov/Archives/edgar/data/104169/000119312526427928/0001193125-26-427928-index.html) — published 2026-10-21; retrieved 2026-10-24T13:22:51.759433+00:00.

[S17] [424B5 0001193125-26-427921](https://www.sec.gov/Archives/edgar/data/104169/000119312526427921/0001193125-26-427921-index.html) — published 2026-10-21; retrieved 2026-10-24T13:22:51.759433+00:00.

[S18] [FWP 0001193125-26-425645](https://www.sec.gov/Archives/edgar/data/104169/000119312526425645/0001193125-26-425645-index.html) — published 2026-10-20; retrieved 2026-10-24T13:22:51.759433+00:00.

[S19] [FWP 0001193125-26-425644](https://www.sec.gov/Archives/edgar/data/104169/000119312526425644/0001193125-26-425644-index.html) — published 2026-10-20; retrieved 2026-10-24T13:22:51.759433+00:00.

Source release: `coverage-20261028-40722802424-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/d9e673c37aaa38580be4e36b4880e8ab015a9390/brain/companies/WMT/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
