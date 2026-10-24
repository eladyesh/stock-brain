---
schema_version: 1
document_type: company_facts
company_id: company-cik-0000101829
cik: 0000101829
company_name: RTX Corp
tickers:
- RTX
status: stub
canonical_reviewed: false
as_of: '2026-10-24'
updated_at: '2026-10-24T13:37:20.730682+00:00'
reviewed_at: null
coverage_release: coverage-20261024-40097864335-1
source_commit: 88540b30f4be3c56b6c7fa8ba3dede59893b9834
financial_history_available: true
curated_research:
  url: https://github.com/eladyesh/stock-brain/blob/88540b30f4be3c56b6c7fa8ba3dede59893b9834/sectors/industrials/companies/RTX/README.md
  status: reviewed
  as_of: '2026-10-20'
  sector: industrials
financial_gap:
  reason: available
  next_action: Retain dated financial evidence and review blocked metrics before analytical
    use.
  observed_forms:
  - 10-K
  - 10-K/A
  - 10-Q
  - 11-K
  - '144'
  - 15-12G
  - 25-NSE
  - '3'
  - 3/A
  - '4'
  - 4/A
  - 424B2
  - 424B3
  - '425'
  - 8-A12B
  - 8-K
  - ARS
  - CERT
  - CERTNYS
  - CORRESP
  - DEF 14A
  - DEFA14A
  - EFFECT
  - FWP
  - IRANNOTICE
  - POS AM
  - PRE 14A
  - PX14A6G
  - S-3ASR
  - S-4
  - S-4/A
  - S-8
  - S-8 POS
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - SD
  - SD/A
  - UPLOAD
input_sources:
  history:
    url: https://data.sec.gov/api/xbrl/companyfacts/CIK0000101829.json
    sha256: 24494083f9c3c39826a9fe6ce29da4dcd4777701e72c59b507e8e2dd15d15ed5
    retrieved_at: '2026-10-24T05:30:51.165302+00:00'
  submissions:
    url: https://data.sec.gov/submissions/CIK0000101829.json
    sha256: 537f3ea8ccf7b51da5c42cbbc399859f3fa2740e5185735d0415160e2c6e581a
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0000101829.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: otherlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt
  published_at: null
  retrieved_at: '2026-10-24T13:23:33.193038+00:00'
  sha256: 94335ed3f4abc4bbd58a4415d105d453184f5484eaf6a2884d1bfb0120d850c9
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0000101829.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 537f3ea8ccf7b51da5c42cbbc399859f3fa2740e5185735d0415160e2c6e581a
- id: S03
  title: SEC CompanyFacts source
  url: https://data.sec.gov/api/xbrl/companyfacts/CIK0000101829.json
  published_at: null
  retrieved_at: '2026-10-24T05:30:51.165302+00:00'
  sha256: 24494083f9c3c39826a9fe6ce29da4dcd4777701e72c59b507e8e2dd15d15ed5
- id: S04
  title: 10-K 0000101829-26-000006
  url: https://www.sec.gov/Archives/edgar/data/101829/000010182926000006/0000101829-26-000006-index.html
  published_at: '2026-02-06'
  retrieved_at: '2026-10-24T05:30:51.165302+00:00'
  sha256: null
- id: S05
  title: 10-Q 0000101829-26-000031
  url: https://www.sec.gov/Archives/edgar/data/101829/000010182926000031/0000101829-26-000031-index.html
  published_at: '2026-10-20'
  retrieved_at: '2026-10-24T05:30:51.165302+00:00'
  sha256: null
- id: S09
  title: 10-Q 0000101829-26-000027
  url: https://www.sec.gov/Archives/edgar/data/101829/000010182926000027/0000101829-26-000027-index.html
  published_at: '2026-07-23'
  retrieved_at: '2026-10-24T05:30:51.165302+00:00'
  sha256: null
- id: S17
  title: 10-Q 0000101829-26-000031
  url: https://www.sec.gov/Archives/edgar/data/101829/000010182926000031/0000101829-26-000031-index.html
  published_at: '2026-10-20'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S18
  title: 8-K 0000101829-26-000030
  url: https://www.sec.gov/Archives/edgar/data/101829/000010182926000030/0000101829-26-000030-index.html
  published_at: '2026-10-20'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S19
  title: 4 0001225208-26-008208
  url: https://www.sec.gov/Archives/edgar/data/101829/000122520826008208/0001225208-26-008208-index.html
  published_at: '2026-10-05'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S20
  title: 4 0001225208-26-008207
  url: https://www.sec.gov/Archives/edgar/data/101829/000122520826008207/0001225208-26-008207-index.html
  published_at: '2026-10-05'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S21
  title: 8-K 0001140361-26-036662
  url: https://www.sec.gov/Archives/edgar/data/101829/000114036126036662/0001140361-26-036662-index.html
  published_at: '2026-09-15'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0000101829
  classification_status: reported_sic
  entity_type: operating
  name: RTX Corp
  sic: '3724'
  sic_description: Aircraft Engines & Engine Parts
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 537f3ea8ccf7b51da5c42cbbc399859f3fa2740e5185735d0415160e2c6e581a
  url: https://data.sec.gov/submissions/CIK0000101829.json
listings:
- ticker: RTX
  exchange: NYSE
  instrument_type: common_stock
research_filings:
- accession: 0000101829-26-000006
  filed: '2026-02-06'
  form: 10-K
  period_end: '2025-12-31'
  url: https://www.sec.gov/Archives/edgar/data/101829/000010182926000006/0000101829-26-000006-index.html
- accession: 0000101829-26-000031
  filed: '2026-10-20'
  form: 10-Q
  period_end: '2026-09-30'
  url: https://www.sec.gov/Archives/edgar/data/101829/000010182926000031/0000101829-26-000031-index.html
- accession: 0001308179-26-000036
  filed: '2026-03-09'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/101829/000130817926000036/0001308179-26-000036-index.html
- accession: 0000101829-26-000030
  filed: '2026-10-20'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/101829/000010182926000030/0000101829-26-000030-index.html
research_progress:
  stage: pending
  input_sha256: ed8f6e8b9795fac8bf4d195cb00594630c1e85e879ac1245fcd30429842e2cf1
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
  derived_observations: 10
  model_draft: false
  reviewed: false
sector_assignment:
  sector: industrials
  method: curated_profile
  sic: '3724'
  sic_description: Aircraft Engines & Engine Parts
  rule_version: 1
  reason: Uses the dated curated profile assignment; automatic data does not renew
    its review.
  source_url: https://github.com/eladyesh/stock-brain/blob/88540b30f4be3c56b6c7fa8ba3dede59893b9834/sectors/industrials/companies/RTX/README.md
full_history_url: https://github.com/eladyesh/stock-brain/blob/aad7b261e69b9f214b9c5e20228523ca644ed670/brain/companies/RTX/README.md
full_history_commit: aad7b261e69b9f214b9c5e20228523ca644ed670
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# RTX — RTX Corp

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/aad7b261e69b9f214b9c5e20228523ca644ed670/brain/companies/RTX/README.md)

## Business overview

Reported issuer name: **RTX Corp**. Stable SEC CIK: **0000101829**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| RTX | NYSE | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **3724**: Aircraft Engines & Engine Parts. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **industrials**. Method: `curated_profile`. Uses the dated curated profile assignment; automatic data does not renew its review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

## Financial performance

Derived observation: Operating margin was 10.50% for 2025-01-01 to 2025-12-31 (US GAAP inputs). [S04]
Formula: `operating_income / revenue * 100`. Inputs: operating_income=9300000000 USD (OperatingIncomeLoss), revenue=88603000000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Net margin was 7.60% for 2025-01-01 to 2025-12-31 (US GAAP inputs). [S04]
Formula: `net_income / revenue * 100`. Inputs: net_income=6732000000 USD (NetIncomeLoss), revenue=88603000000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Free cash flow margin was 8.96% for 2025-01-01 to 2025-12-31 (US GAAP inputs). [S04]
Formula: `free_cash_flow / revenue * 100`. Inputs: free_cash_flow=7940000000 USD (NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment), revenue=88603000000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Stock compensation / revenue was 0.59% for 2025-01-01 to 2025-12-31 (US GAAP inputs). [S04]
Formula: `stock_based_compensation / revenue * 100`. Inputs: stock_based_compensation=519000000 USD (ShareBasedCompensation), revenue=88603000000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Annual revenue changed +9.74% from the year ended 2024-12-31 to 2025-12-31. [S04]
Formula: `(current / prior - 1) * 100`. Inputs: revenue=88603000000 USD (RevenueFromContractWithCustomerExcludingAssessedTax), revenue=80738000000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Annual operating income changed +42.25% from the year ended 2024-12-31 to 2025-12-31. [S04]
Formula: `(current / prior - 1) * 100`. Inputs: operating_income=9300000000 USD (OperatingIncomeLoss), operating_income=6538000000 USD (OperatingIncomeLoss).

Derived observation: Annual net income changed +41.01% from the year ended 2024-12-31 to 2025-12-31. [S04]
Formula: `(current / prior - 1) * 100`. Inputs: net_income=6732000000 USD (NetIncomeLoss), net_income=4774000000 USD (NetIncomeLoss).

Derived observation: Annual operating cash flow changed +47.60% from the year ended 2024-12-31 to 2025-12-31. [S04]
Formula: `(current / prior - 1) * 100`. Inputs: operating_cash_flow=10567000000 USD (NetCashProvidedByUsedInOperatingActivities), operating_cash_flow=7159000000 USD (NetCashProvidedByUsedInOperatingActivities).

Derived observation: Annual free cash flow changed +75.12% from the year ended 2024-12-31 to 2025-12-31. [S04]
Formula: `(current / prior - 1) * 100`. Inputs: free_cash_flow=7940000000 USD (NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment), free_cash_flow=4534000000 USD (NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment).

Derived observation: Operating cash flow / net income was 1.57x for the year ended 2025-12-31. Working capital and non-cash adjustments require separate filing analysis. [S04]
Formula: `operating_cash_flow / net_income`. Inputs: operating_cash_flow=10567000000 USD (NetCashProvidedByUsedInOperatingActivities), net_income=6732000000 USD (NetIncomeLoss).

Evidence cutoff: 2026-10-24. Source retrieved: 2026-10-24T05:30:51.165302+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-01-01 to 2025-12-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -2,627,000,000 | USD | US GAAP / reported | PaymentsToAcquirePropertyPlantAndEquipment; Cash outflow = negative of reported PaymentsToAcquirePropertyPlantAndEquipment; source value retained. | [S04] |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S04] |
| free_cash_flow | 7,940,000,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment | [S04] |
| gross_profit | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income | 6,732,000,000 | USD | US GAAP / reported | NetIncomeLoss | [S04] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income_including_noncontrolling_interests | 7,069,000,000 | USD | US GAAP / reported | ProfitLoss | [S04] |
| operating_cash_flow | 10,567,000,000 | USD | US GAAP / reported | NetCashProvidedByUsedInOperatingActivities | [S04] |
| operating_income | 9,300,000,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S04] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | 88,603,000,000 | USD | US GAAP / reported | RevenueFromContractWithCustomerExcludingAssessedTax | [S04] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S04] |
| stock_based_compensation | 519,000,000 | USD | US GAAP / reported | ShareBasedCompensation | [S04] |


### quarterly: 2026-07-01 to 2026-09-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -749,000,000 | USD | US GAAP / derived | PaymentsToAcquirePropertyPlantAndEquipment; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S05] [S09] |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S05] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S05] |
| free_cash_flow | 2,119,000,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S05] [S09] |
| gross_profit | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income | 2,583,000,000 | USD | US GAAP / reported | NetIncomeLoss | [S05] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income_including_noncontrolling_interests | 2,708,000,000 | USD | US GAAP / reported | ProfitLoss | [S05] |
| operating_cash_flow | 2,868,000,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S05] [S09] |
| operating_income | 3,337,000,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S05] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | 24,965,000,000 | USD | US GAAP / reported | RevenueFromContractWithCustomerExcludingAssessedTax | [S05] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S05] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S05] |
| stock_based_compensation | 159,000,000 | USD | US GAAP / derived | ShareBasedCompensation; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S05] [S09] |



## Balance sheet and capital allocation

Evidence cutoff: 2026-10-24. Source retrieved: 2026-10-24T05:30:51.165302+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-01-01 to 2025-12-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 7,435,000,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S05] |
| debt_current | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtAndCapitalLeaseObligationsCurrent; debt_scope_requires_filing_review | [S05] |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtAndCapitalLeaseObligations; debt_scope_requires_filing_review | [S05] |
| debt_total | Unavailable / blocked | USD | US GAAP / derived / not model usable | LongTermDebtAndCapitalLeaseObligationsIncludingCurrentMaturities + ShortTermBorrowings; debt_scope_requires_filing_review, definition_changed_across_series, derived_input_requires_review | [S05] |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtAndCapitalLeaseObligationsIncludingCurrentMaturities; debt_scope_requires_filing_review, definition_changed_across_series | [S05] |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_borrowings | 204,000,000 | USD | US GAAP / reported | ShortTermBorrowings | [S05] |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |


### quarterly: 2026-07-01 to 2026-09-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 9,173,000,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S05] |
| debt_current | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtAndCapitalLeaseObligationsCurrent; debt_scope_requires_filing_review | [S05] |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtAndCapitalLeaseObligations; debt_scope_requires_filing_review | [S05] |
| debt_total | Unavailable / blocked | USD | US GAAP / derived / not model usable | LongTermDebtAndCapitalLeaseObligationsIncludingCurrentMaturities + ShortTermBorrowings; debt_scope_requires_filing_review, definition_changed_across_series, derived_input_requires_review | [S05] |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtAndCapitalLeaseObligationsIncludingCurrentMaturities; debt_scope_requires_filing_review, definition_changed_across_series | [S05] |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_borrowings | 210,000,000 | USD | US GAAP / reported | ShortTermBorrowings | [S05] |
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
- Collector status: quality_review_required; last action: new_financial_filing; last checked: 2026-10-24T13:28:14.744206+00:00.

Dated curated research is maintained separately: [profile at source commit](https://github.com/eladyesh/stock-brain/blob/88540b30f4be3c56b6c7fa8ba3dede59893b9834/sectors/industrials/companies/RTX/README.md) (status reviewed, as of 2026-10-20). Automatic facts never change its review date.

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

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest five available filing metadata records; document bodies have not been analyzed here.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-10-20 | 10-Q | 0000101829-26-000031 | — | [S17] |
| 2026-10-20 | 8-K | 0000101829-26-000030 | — | [S18] |
| 2026-10-05 | 4 | 0001225208-26-008208 | — | [S19] |
| 2026-10-05 | 4 | 0001225208-26-008207 | — | [S20] |
| 2026-09-15 | 8-K | 0001140361-26-036662 | — | [S21] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-24T13:23:33.193038+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0000101829.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [SEC CompanyFacts source](https://data.sec.gov/api/xbrl/companyfacts/CIK0000101829.json) — published not supplied; retrieved 2026-10-24T05:30:51.165302+00:00.

[S04] [10-K 0000101829-26-000006](https://www.sec.gov/Archives/edgar/data/101829/000010182926000006/0000101829-26-000006-index.html) — published 2026-02-06; retrieved 2026-10-24T05:30:51.165302+00:00.

[S05] [10-Q 0000101829-26-000031](https://www.sec.gov/Archives/edgar/data/101829/000010182926000031/0000101829-26-000031-index.html) — published 2026-10-20; retrieved 2026-10-24T05:30:51.165302+00:00.

[S09] [10-Q 0000101829-26-000027](https://www.sec.gov/Archives/edgar/data/101829/000010182926000027/0000101829-26-000027-index.html) — published 2026-07-23; retrieved 2026-10-24T05:30:51.165302+00:00.

[S17] [10-Q 0000101829-26-000031](https://www.sec.gov/Archives/edgar/data/101829/000010182926000031/0000101829-26-000031-index.html) — published 2026-10-20; retrieved 2026-10-23T08:33:02.691743+00:00.

[S18] [8-K 0000101829-26-000030](https://www.sec.gov/Archives/edgar/data/101829/000010182926000030/0000101829-26-000030-index.html) — published 2026-10-20; retrieved 2026-10-23T08:33:02.691743+00:00.

[S19] [4 0001225208-26-008208](https://www.sec.gov/Archives/edgar/data/101829/000122520826008208/0001225208-26-008208-index.html) — published 2026-10-05; retrieved 2026-10-23T08:33:02.691743+00:00.

[S20] [4 0001225208-26-008207](https://www.sec.gov/Archives/edgar/data/101829/000122520826008207/0001225208-26-008207-index.html) — published 2026-10-05; retrieved 2026-10-23T08:33:02.691743+00:00.

[S21] [8-K 0001140361-26-036662](https://www.sec.gov/Archives/edgar/data/101829/000114036126036662/0001140361-26-036662-index.html) — published 2026-09-15; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261024-40097864335-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/aad7b261e69b9f214b9c5e20228523ca644ed670/brain/companies/RTX/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
