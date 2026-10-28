---
schema_version: 1
document_type: company_facts
company_id: company-cik-0000069422
cik: 0000069422
company_name: INTERGROUP CORP
tickers:
- INTG
status: stub
canonical_reviewed: false
as_of: '2026-10-28'
updated_at: '2026-10-28T16:13:42.115634+00:00'
reviewed_at: null
coverage_release: coverage-20261028-40722802424-1
source_commit: 8a30d18f29f6ce6c61cbe955ca3f23f6f12ef180
financial_history_available: true
curated_research: null
financial_gap:
  reason: available
  next_action: Retain dated financial evidence and review blocked metrics before analytical
    use.
  observed_forms:
  - 10-K
  - 10-K/A
  - 10-Q
  - 10KSB
  - 10KSB/A
  - 10QSB
  - 10QSB/A
  - '25'
  - '3'
  - '4'
  - 4/A
  - '5'
  - 8-K
  - ARS
  - CORRESP
  - DEF 14A
  - DEF 14C
  - NT 10-K
  - NT 10-Q
  - PRE 14A
  - PRE 14C
  - S-8
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13D/A
  - UPLOAD
input_sources:
  history:
    url: https://data.sec.gov/api/xbrl/companyfacts/CIK0000069422.json
    sha256: 13bb3ebcbaa7f0b37deca80e4b994f5a144306db451d17c1802fe5df3e0684b5
    retrieved_at: '2026-10-22T17:53:02.398600+00:00'
    archive:
      member: CIK0000069422.json
      sha256: 7457a528288f1e3425cba6ffd7370c6c205845aba12761763aa5ae3683c0fdc2
      url: https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip
    acquisition: operator_supplied_sec_bulk_archive
  submissions:
    url: https://data.sec.gov/submissions/CIK0000069422.json
    sha256: d0b2f3f677054b3f74540ad4c3803c02b1da49036c5fcbce981849e30b575542
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0000069422.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
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
  url: https://data.sec.gov/submissions/CIK0000069422.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: d0b2f3f677054b3f74540ad4c3803c02b1da49036c5fcbce981849e30b575542
- id: S03
  title: SEC CompanyFacts source
  url: https://data.sec.gov/api/xbrl/companyfacts/CIK0000069422.json
  published_at: null
  retrieved_at: '2026-10-22T17:53:02.398600+00:00'
  sha256: 13bb3ebcbaa7f0b37deca80e4b994f5a144306db451d17c1802fe5df3e0684b5
- id: S04
  title: 10-K 0001493152-26-044490
  url: https://www.sec.gov/Archives/edgar/data/69422/000149315226044490/0001493152-26-044490-index.html
  published_at: '2026-09-28'
  retrieved_at: '2026-10-22T17:53:02.398600+00:00'
  sha256: null
- id: S09
  title: 10-Q 0001493152-26-022173
  url: https://www.sec.gov/Archives/edgar/data/69422/000149315226022173/0001493152-26-022173-index.html
  published_at: '2026-05-11'
  retrieved_at: '2026-10-22T17:53:02.398600+00:00'
  sha256: null
- id: S18
  title: 8-K 0001493152-26-044836
  url: https://www.sec.gov/Archives/edgar/data/69422/000149315226044836/0001493152-26-044836-index.html
  published_at: '2026-09-29'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S19
  title: 10-K 0001493152-26-044490
  url: https://www.sec.gov/Archives/edgar/data/69422/000149315226044490/0001493152-26-044490-index.html
  published_at: '2026-09-28'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S20
  title: 4 0001493152-26-027268
  url: https://www.sec.gov/Archives/edgar/data/69422/000149315226027268/0001493152-26-027268-index.html
  published_at: '2026-06-04'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S21
  title: 8-K 0001493152-26-025217
  url: https://www.sec.gov/Archives/edgar/data/69422/000149315226025217/0001493152-26-025217-index.html
  published_at: '2026-05-26'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S22
  title: 8-K 0001493152-26-022913
  url: https://www.sec.gov/Archives/edgar/data/69422/000149315226022913/0001493152-26-022913-index.html
  published_at: '2026-05-14'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0000069422
  classification_status: reported_sic
  entity_type: operating
  name: INTERGROUP CORP
  sic: '6513'
  sic_description: Operators of  Apartment Buildings
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: d0b2f3f677054b3f74540ad4c3803c02b1da49036c5fcbce981849e30b575542
  url: https://data.sec.gov/submissions/CIK0000069422.json
listings:
- ticker: INTG
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001493152-26-044490
  filed: '2026-09-28'
  form: 10-K
  period_end: '2026-06-30'
  url: https://www.sec.gov/Archives/edgar/data/69422/000149315226044490/0001493152-26-044490-index.html
- accession: 0001493152-26-022173
  filed: '2026-05-11'
  form: 10-Q
  period_end: '2026-03-31'
  url: https://www.sec.gov/Archives/edgar/data/69422/000149315226022173/0001493152-26-022173-index.html
- accession: 0001493152-26-015688
  filed: '2026-04-08'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/69422/000149315226015688/0001493152-26-015688-index.html
- accession: 0001493152-26-044836
  filed: '2026-09-29'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/69422/000149315226044836/0001493152-26-044836-index.html
research_progress:
  stage: pending
  input_sha256: dd19dda51387b535c45b0d015694c915608d809dda6a9f7d7116b20a7bd1c74f
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
  derived_observations: 9
  model_draft: false
  reviewed: false
sector_assignment:
  sector: real-estate
  method: project_sic_rule
  sic: '6513'
  sic_description: Operators of  Apartment Buildings
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0000069422.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/5da532c3abee5b40a5400c5864c6f3f4593276d7/brain/companies/INTG/README.md
full_history_commit: 5da532c3abee5b40a5400c5864c6f3f4593276d7
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# INTG — INTERGROUP CORP

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/5da532c3abee5b40a5400c5864c6f3f4593276d7/brain/companies/INTG/README.md)

## Business overview

Reported issuer name: **INTERGROUP CORP**. Stable SEC CIK: **0000069422**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| INTG | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **6513**: Operators of  Apartment Buildings. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **real-estate**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

## Financial performance

Derived observation: Operating margin was 16.05% for 2025-07-01 to 2026-06-30 (US GAAP inputs). [S19]
Formula: `operating_income / revenue * 100`. Inputs: operating_income=11866000 USD (OperatingIncomeLoss), revenue=73951000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Net margin was 2.22% for 2025-07-01 to 2026-06-30 (US GAAP inputs). [S19]
Formula: `net_income / revenue * 100`. Inputs: net_income=1643000 USD (NetIncomeLoss), revenue=73951000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Free cash flow margin was 1.69% for 2025-07-01 to 2026-06-30 (US GAAP inputs). [S19]
Formula: `free_cash_flow / revenue * 100`. Inputs: free_cash_flow=1252000 USD (NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment), revenue=73951000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Stock compensation / revenue was 0.06% for 2025-07-01 to 2026-06-30 (US GAAP inputs). [S19]
Formula: `stock_based_compensation / revenue * 100`. Inputs: stock_based_compensation=44000 USD (ShareBasedCompensation), revenue=73951000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Annual revenue changed +14.87% from the year ended 2025-06-30 to 2026-06-30. [S19]
Formula: `(current / prior - 1) * 100`. Inputs: revenue=73951000 USD (RevenueFromContractWithCustomerExcludingAssessedTax), revenue=64378000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Annual operating income changed +55.25% from the year ended 2025-06-30 to 2026-06-30. [S19]
Formula: `(current / prior - 1) * 100`. Inputs: operating_income=11866000 USD (OperatingIncomeLoss), operating_income=7643000 USD (OperatingIncomeLoss).

Derived observation: Annual operating cash flow changed -41.46% from the year ended 2025-06-30 to 2026-06-30. [S19]
Formula: `(current / prior - 1) * 100`. Inputs: operating_cash_flow=3450000 USD (NetCashProvidedByUsedInOperatingActivities), operating_cash_flow=5893000 USD (NetCashProvidedByUsedInOperatingActivities).

Derived observation: Annual free cash flow changed -65.61% from the year ended 2025-06-30 to 2026-06-30. [S19]
Formula: `(current / prior - 1) * 100`. Inputs: free_cash_flow=1252000 USD (NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment), free_cash_flow=3641000 USD (NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment).

Derived observation: Operating cash flow / net income was 2.10x for the year ended 2026-06-30. Working capital and non-cash adjustments require separate filing analysis. [S19]
Formula: `operating_cash_flow / net_income`. Inputs: operating_cash_flow=3450000 USD (NetCashProvidedByUsedInOperatingActivities), net_income=1643000 USD (NetIncomeLoss).

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:53:02.398600+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-07-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -2,198,000 | USD | US GAAP / reported | PaymentsToAcquirePropertyPlantAndEquipment; Cash outflow = negative of reported PaymentsToAcquirePropertyPlantAndEquipment; source value retained. | [S04] |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S04] |
| free_cash_flow | 1,252,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment | [S04] |
| gross_profit | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income | 1,643,000 | USD | US GAAP / reported | NetIncomeLoss | [S04] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income_including_noncontrolling_interests | 336,000 | USD | US GAAP / reported | ProfitLoss | [S04] |
| operating_cash_flow | 3,450,000 | USD | US GAAP / reported | NetCashProvidedByUsedInOperatingActivities | [S04] |
| operating_income | 11,866,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S04] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | 73,951,000 | USD | US GAAP / reported | RevenueFromContractWithCustomerExcludingAssessedTax | [S04] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S04] |
| stock_based_compensation | 44,000 | USD | US GAAP / reported | ShareBasedCompensation | [S04] |


### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -412,000 | USD | US GAAP / derived | PaymentsToAcquirePropertyPlantAndEquipment; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S09] |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| free_cash_flow | 368,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S09] |
| gross_profit | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income | 206,000 | USD | US GAAP / derived | NetIncomeLoss; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S09] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income_including_noncontrolling_interests | -62,000 | USD | US GAAP / derived | ProfitLoss; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S09] |
| operating_cash_flow | 780,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S09] |
| operating_income | 2,859,000 | USD | US GAAP / derived | OperatingIncomeLoss; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S09] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | 18,365,000 | USD | US GAAP / derived | RevenueFromContractWithCustomerExcludingAssessedTax; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S09] |
| shares_basic | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_diluted | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| stock_based_compensation | 8,000 | USD | US GAAP / derived | ShareBasedCompensation; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S09] |



## Balance sheet and capital allocation

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:53:02.398600+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-07-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 6,356,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S04] |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S04] |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |


### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 6,356,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S04] |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S04] |
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
- Collector status: quality_review_required; last action: new_financial_filing; last checked: 2026-10-24T13:27:51.777216+00:00.

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

Calculation gaps: net_income: annual growth withheld because periods, definitions or a positive prior denominator are not verified.

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest five available filing metadata records; document bodies have not been analyzed here.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-09-29 | 8-K | 0001493152-26-044836 | — | [S18] |
| 2026-09-28 | 10-K | 0001493152-26-044490 | — | [S19] |
| 2026-06-04 | 4 | 0001493152-26-027268 | — | [S20] |
| 2026-05-26 | 8-K | 0001493152-26-025217 | — | [S21] |
| 2026-05-14 | 8-K | 0001493152-26-022913 | — | [S22] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-28T16:09:01.738588+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0000069422.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [SEC CompanyFacts source](https://data.sec.gov/api/xbrl/companyfacts/CIK0000069422.json) — published not supplied; retrieved 2026-10-22T17:53:02.398600+00:00.

[S04] [10-K 0001493152-26-044490](https://www.sec.gov/Archives/edgar/data/69422/000149315226044490/0001493152-26-044490-index.html) — published 2026-09-28; retrieved 2026-10-22T17:53:02.398600+00:00.

[S09] [10-Q 0001493152-26-022173](https://www.sec.gov/Archives/edgar/data/69422/000149315226022173/0001493152-26-022173-index.html) — published 2026-05-11; retrieved 2026-10-22T17:53:02.398600+00:00.

[S18] [8-K 0001493152-26-044836](https://www.sec.gov/Archives/edgar/data/69422/000149315226044836/0001493152-26-044836-index.html) — published 2026-09-29; retrieved 2026-10-23T08:33:02.691743+00:00.

[S19] [10-K 0001493152-26-044490](https://www.sec.gov/Archives/edgar/data/69422/000149315226044490/0001493152-26-044490-index.html) — published 2026-09-28; retrieved 2026-10-23T08:33:02.691743+00:00.

[S20] [4 0001493152-26-027268](https://www.sec.gov/Archives/edgar/data/69422/000149315226027268/0001493152-26-027268-index.html) — published 2026-06-04; retrieved 2026-10-23T08:33:02.691743+00:00.

[S21] [8-K 0001493152-26-025217](https://www.sec.gov/Archives/edgar/data/69422/000149315226025217/0001493152-26-025217-index.html) — published 2026-05-26; retrieved 2026-10-23T08:33:02.691743+00:00.

[S22] [8-K 0001493152-26-022913](https://www.sec.gov/Archives/edgar/data/69422/000149315226022913/0001493152-26-022913-index.html) — published 2026-05-14; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261028-40722802424-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/5da532c3abee5b40a5400c5864c6f3f4593276d7/brain/companies/INTG/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
