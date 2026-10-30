---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001108524
cik: 0001108524
company_name: Salesforce, Inc.
tickers:
- CRM
status: stub
canonical_reviewed: false
as_of: '2026-10-30'
updated_at: '2026-10-30T16:05:25.650854+00:00'
reviewed_at: null
coverage_release: coverage-20261030-41085569265-1
source_commit: f9a34108789a82bf7c75f9d65a0e9552aa5552db
financial_history_available: true
curated_research: null
financial_gap:
  reason: available
  next_action: Retain dated financial evidence and review blocked metrics before analytical
    use.
  observed_forms:
  - 10-K
  - 10-Q
  - 13F-HR
  - '144'
  - '3'
  - '4'
  - 4/A
  - 424B2
  - 8-K
  - ARS
  - DEF 14A
  - DEFA14A
  - FWP
  - PRE 14A
  - PX14A6G
  - S-3ASR
  - S-8
  - S-8 POS
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
input_sources:
  history:
    url: https://data.sec.gov/api/xbrl/companyfacts/CIK0001108524.json
    sha256: c36bddafd22061dfe573fa22199074d882196f6667cf641eb30c8cec5a340ae5
    retrieved_at: '2026-10-22T17:39:41.848518+00:00'
    archive:
      member: CIK0001108524.json
      sha256: 7457a528288f1e3425cba6ffd7370c6c205845aba12761763aa5ae3683c0fdc2
      url: https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip
    acquisition: operator_supplied_sec_bulk_archive
  submissions:
    url: https://data.sec.gov/submissions/CIK0001108524.json
    sha256: 4eb15989367a723b1e17eeaaa8445afb30c63b44979b03f8bf7473c9c3bc693d
    retrieved_at: '2026-10-24T13:22:51.759433+00:00'
    archive: &id001
      member: CIK0001108524.json
      sha256: 593fbbea6512ef5ec729a5e513c465fbedaac8a66602c0abe00d0ba5a4d18732
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: otherlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt
  published_at: null
  retrieved_at: '2026-10-30T16:00:12.358089+00:00'
  sha256: a960a0bfc5439fac9e467fe07ef1f44afe893ba2afc3297648321a80ce09971e
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001108524.json
  published_at: null
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 4eb15989367a723b1e17eeaaa8445afb30c63b44979b03f8bf7473c9c3bc693d
- id: S03
  title: SEC CompanyFacts source
  url: https://data.sec.gov/api/xbrl/companyfacts/CIK0001108524.json
  published_at: null
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: c36bddafd22061dfe573fa22199074d882196f6667cf641eb30c8cec5a340ae5
- id: S04
  title: 10-K 0001108524-26-000060
  url: https://www.sec.gov/Archives/edgar/data/1108524/000110852426000060/0001108524-26-000060-index.html
  published_at: '2026-03-02'
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: null
- id: S05
  title: 10-Q 0001108524-26-000190
  url: https://www.sec.gov/Archives/edgar/data/1108524/000110852426000190/0001108524-26-000190-index.html
  published_at: '2026-08-27'
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: null
- id: S17
  title: 4 0001108524-26-000227
  url: https://www.sec.gov/Archives/edgar/data/1108524/000110852426000227/0001108524-26-000227-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S18
  title: 8-K 0001193125-26-425881
  url: https://www.sec.gov/Archives/edgar/data/1108524/000119312526425881/0001193125-26-425881-index.html
  published_at: '2026-10-20'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S19
  title: 4 0001108524-26-000225
  url: https://www.sec.gov/Archives/edgar/data/1108524/000110852426000225/0001108524-26-000225-index.html
  published_at: '2026-09-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S20
  title: 4 0001108524-26-000220
  url: https://www.sec.gov/Archives/edgar/data/1108524/000110852426000220/0001108524-26-000220-index.html
  published_at: '2026-09-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S21
  title: 4 0001108524-26-000217
  url: https://www.sec.gov/Archives/edgar/data/1108524/000110852426000217/0001108524-26-000217-index.html
  published_at: '2026-09-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
issuer_classification:
  cik: 0001108524
  classification_status: reported_sic
  entity_type: operating
  name: Salesforce, Inc.
  sic: '7372'
  sic_description: Services-Prepackaged Software
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 4eb15989367a723b1e17eeaaa8445afb30c63b44979b03f8bf7473c9c3bc693d
  url: https://data.sec.gov/submissions/CIK0001108524.json
listings:
- ticker: CRM
  exchange: NYSE
  instrument_type: common_stock
research_filings:
- accession: 0001108524-26-000060
  filed: '2026-03-02'
  form: 10-K
  period_end: '2026-01-31'
  url: https://www.sec.gov/Archives/edgar/data/1108524/000110852426000060/0001108524-26-000060-index.html
- accession: 0001108524-26-000190
  filed: '2026-08-27'
  form: 10-Q
  period_end: '2026-07-31'
  url: https://www.sec.gov/Archives/edgar/data/1108524/000110852426000190/0001108524-26-000190-index.html
- accession: 0001108524-26-000085
  filed: '2026-04-16'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/1108524/000110852426000085/0001108524-26-000085-index.html
- accession: 0001193125-26-425881
  filed: '2026-10-20'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/1108524/000119312526425881/0001193125-26-425881-index.html
research_progress:
  stage: pending
  input_sha256: 287a5d17ffe62e23d3b00bd5d4cd0a9d77d9999ababb48671e1417bd3f1f75ed
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
  derived_observations: 10
  model_draft: false
  reviewed: false
sector_assignment:
  sector: information-technology
  method: project_sic_rule
  sic: '7372'
  sic_description: Services-Prepackaged Software
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001108524.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/1b4771bc41dec553e210323f72d9bfc908288c04/brain/companies/CRM/README.md
full_history_commit: 1b4771bc41dec553e210323f72d9bfc908288c04
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# CRM — Salesforce, Inc.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/1b4771bc41dec553e210323f72d9bfc908288c04/brain/companies/CRM/README.md)

## Business overview

Reported issuer name: **Salesforce, Inc.**. Stable SEC CIK: **0001108524**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| CRM | NYSE | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **7372**: Services-Prepackaged Software. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **information-technology**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

## Financial performance

Derived observation: Operating margin was 20.06% for 2025-02-01 to 2026-01-31 (US GAAP inputs). [S04]
Formula: `operating_income / revenue * 100`. Inputs: operating_income=8331000000 USD (OperatingIncomeLoss), revenue=41525000000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Net margin was 17.96% for 2025-02-01 to 2026-01-31 (US GAAP inputs). [S04]
Formula: `net_income / revenue * 100`. Inputs: net_income=7457000000 USD (NetIncomeLoss), revenue=41525000000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Free cash flow margin was 34.68% for 2025-02-01 to 2026-01-31 (US GAAP inputs). [S04]
Formula: `free_cash_flow / revenue * 100`. Inputs: free_cash_flow=14402000000 USD (NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment), revenue=41525000000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Stock compensation / revenue was 8.45% for 2025-02-01 to 2026-01-31 (US GAAP inputs). [S04]
Formula: `stock_based_compensation / revenue * 100`. Inputs: stock_based_compensation=3509000000 USD (ShareBasedCompensation), revenue=41525000000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Annual revenue changed +9.58% from the year ended 2025-01-31 to 2026-01-31. [S04]
Formula: `(current / prior - 1) * 100`. Inputs: revenue=41525000000 USD (RevenueFromContractWithCustomerExcludingAssessedTax), revenue=37895000000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Annual operating income changed +15.63% from the year ended 2025-01-31 to 2026-01-31. [S04]
Formula: `(current / prior - 1) * 100`. Inputs: operating_income=8331000000 USD (OperatingIncomeLoss), operating_income=7205000000 USD (OperatingIncomeLoss).

Derived observation: Annual net income changed +20.33% from the year ended 2025-01-31 to 2026-01-31. [S04]
Formula: `(current / prior - 1) * 100`. Inputs: net_income=7457000000 USD (NetIncomeLoss), net_income=6197000000 USD (NetIncomeLoss).

Derived observation: Annual operating cash flow changed +14.54% from the year ended 2025-01-31 to 2026-01-31. [S04]
Formula: `(current / prior - 1) * 100`. Inputs: operating_cash_flow=14996000000 USD (NetCashProvidedByUsedInOperatingActivities), operating_cash_flow=13092000000 USD (NetCashProvidedByUsedInOperatingActivities).

Derived observation: Annual free cash flow changed +15.83% from the year ended 2025-01-31 to 2026-01-31. [S04]
Formula: `(current / prior - 1) * 100`. Inputs: free_cash_flow=14402000000 USD (NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment), free_cash_flow=12434000000 USD (NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment).

Derived observation: Operating cash flow / net income was 2.01x for the year ended 2026-01-31. Working capital and non-cash adjustments require separate filing analysis. [S04]
Formula: `operating_cash_flow / net_income`. Inputs: operating_cash_flow=14996000000 USD (NetCashProvidedByUsedInOperatingActivities), net_income=7457000000 USD (NetIncomeLoss).

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:39:41.848518+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-02-01 to 2026-01-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -594,000,000 | USD | US GAAP / reported | PaymentsToAcquirePropertyPlantAndEquipment; Cash outflow = negative of reported PaymentsToAcquirePropertyPlantAndEquipment; source value retained. | [S04] |
| cost_of_revenue | 9,270,000,000 | USD | US GAAP / reported | CostOfGoodsAndServicesSold | [S04] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S04] |
| free_cash_flow | 14,402,000,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment | [S04] |
| gross_profit | 32,255,000,000 | USD | US GAAP / reported | GrossProfit | [S04] |
| net_income | 7,457,000,000 | USD | US GAAP / reported | NetIncomeLoss | [S04] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income_including_noncontrolling_interests | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| operating_cash_flow | 14,996,000,000 | USD | US GAAP / reported | NetCashProvidedByUsedInOperatingActivities | [S04] |
| operating_income | 8,331,000,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S04] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | 41,525,000,000 | USD | US GAAP / reported | RevenueFromContractWithCustomerExcludingAssessedTax | [S04] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S04] |
| stock_based_compensation | 3,509,000,000 | USD | US GAAP / reported | ShareBasedCompensation | [S04] |


### quarterly: 2026-05-01 to 2026-07-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | Unavailable / blocked | USD | US GAAP / reported / not model usable | PaymentsToAcquirePropertyPlantAndEquipment; Cash outflow = negative of reported PaymentsToAcquirePropertyPlantAndEquipment; source value retained.; conflicting_fiscal_year | [S05] |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | CostOfGoodsAndServicesSold; conflicting_fiscal_year | [S05] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; conflicting_fiscal_year, share_split_and_corporate_action_basis_unverified | [S05] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; conflicting_fiscal_year, share_split_and_corporate_action_basis_unverified | [S05] |
| free_cash_flow | Unavailable / blocked | USD | US GAAP / derived / not model usable | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment; conflicting_fiscal_year | [S05] |
| gross_profit | Unavailable / blocked | USD | US GAAP / reported / not model usable | GrossProfit; conflicting_fiscal_year | [S05] |
| net_income | Unavailable / blocked | USD | US GAAP / reported / not model usable | NetIncomeLoss; conflicting_fiscal_year | [S05] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; conflicting_fiscal_year | No eligible evidence |
| net_income_including_noncontrolling_interests | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; conflicting_fiscal_year | No eligible evidence |
| operating_cash_flow | Unavailable / blocked | USD | US GAAP / reported / not model usable | NetCashProvidedByUsedInOperatingActivities; conflicting_fiscal_year | [S05] |
| operating_income | Unavailable / blocked | USD | US GAAP / reported / not model usable | OperatingIncomeLoss; conflicting_fiscal_year | [S05] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; conflicting_fiscal_year | No eligible evidence |
| revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | RevenueFromContractWithCustomerExcludingAssessedTax; conflicting_fiscal_year | [S05] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; conflicting_fiscal_year, share_split_and_corporate_action_basis_unverified | [S05] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; conflicting_fiscal_year, share_split_and_corporate_action_basis_unverified | [S05] |
| stock_based_compensation | Unavailable / blocked | USD | US GAAP / reported / not model usable | ShareBasedCompensation; conflicting_fiscal_year | [S05] |



## Balance sheet and capital allocation

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:39:41.848518+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-02-01 to 2026-01-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 7,327,000,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S05] |
| debt_current | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtCurrent; debt_scope_requires_filing_review | [S05] |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtNoncurrent; debt_scope_requires_filing_review | [S05] |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebt; debt_scope_requires_filing_review | [S05] |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S04] |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |


### quarterly: 2026-05-01 to 2026-07-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | Unavailable / blocked | USD | US GAAP / reported / not model usable | CashAndCashEquivalentsAtCarryingValue; conflicting_fiscal_year | [S05] |
| debt_current | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtCurrent; conflicting_fiscal_year, debt_scope_requires_filing_review | [S05] |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtNoncurrent; conflicting_fiscal_year, debt_scope_requires_filing_review | [S05] |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; conflicting_fiscal_year | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebt; conflicting_fiscal_year, debt_scope_requires_filing_review | [S05] |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable | ; conflicting_fiscal_year | No eligible evidence |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; conflicting_fiscal_year | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; conflicting_fiscal_year | No eligible evidence |



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
- Collector status: quality_review_required; last action: new_financial_filing; last checked: 2026-10-24T13:31:42.454416+00:00.

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
| 2026-10-23 | 4 | 0001108524-26-000227 | — | [S17] |
| 2026-10-20 | 8-K | 0001193125-26-425881 | — | [S18] |
| 2026-09-23 | 4 | 0001108524-26-000225 | — | [S19] |
| 2026-09-23 | 4 | 0001108524-26-000220 | — | [S20] |
| 2026-09-23 | 4 | 0001108524-26-000217 | — | [S21] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-30T16:00:12.358089+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001108524.json) — published not supplied; retrieved 2026-10-24T13:22:51.759433+00:00.

[S03] [SEC CompanyFacts source](https://data.sec.gov/api/xbrl/companyfacts/CIK0001108524.json) — published not supplied; retrieved 2026-10-22T17:39:41.848518+00:00.

[S04] [10-K 0001108524-26-000060](https://www.sec.gov/Archives/edgar/data/1108524/000110852426000060/0001108524-26-000060-index.html) — published 2026-03-02; retrieved 2026-10-22T17:39:41.848518+00:00.

[S05] [10-Q 0001108524-26-000190](https://www.sec.gov/Archives/edgar/data/1108524/000110852426000190/0001108524-26-000190-index.html) — published 2026-08-27; retrieved 2026-10-22T17:39:41.848518+00:00.

[S17] [4 0001108524-26-000227](https://www.sec.gov/Archives/edgar/data/1108524/000110852426000227/0001108524-26-000227-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S18] [8-K 0001193125-26-425881](https://www.sec.gov/Archives/edgar/data/1108524/000119312526425881/0001193125-26-425881-index.html) — published 2026-10-20; retrieved 2026-10-24T13:22:51.759433+00:00.

[S19] [4 0001108524-26-000225](https://www.sec.gov/Archives/edgar/data/1108524/000110852426000225/0001108524-26-000225-index.html) — published 2026-09-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S20] [4 0001108524-26-000220](https://www.sec.gov/Archives/edgar/data/1108524/000110852426000220/0001108524-26-000220-index.html) — published 2026-09-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S21] [4 0001108524-26-000217](https://www.sec.gov/Archives/edgar/data/1108524/000110852426000217/0001108524-26-000217-index.html) — published 2026-09-23; retrieved 2026-10-24T13:22:51.759433+00:00.

Source release: `coverage-20261030-41085569265-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/1b4771bc41dec553e210323f72d9bfc908288c04/brain/companies/CRM/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
