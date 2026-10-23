---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001494259
cik: 0001494259
company_name: CarGurus, Inc.
tickers:
- CARG
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
  - 10-K
  - 10-Q
  - '144'
  - '3'
  - '4'
  - 4/A
  - 8-K
  - 8-K/A
  - ARS
  - CORRESP
  - DEF 14A
  - DEFA14A
  - PRE 14A
  - S-8
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  history:
    url: https://data.sec.gov/api/xbrl/companyfacts/CIK0001494259.json
    sha256: 78b67d6544657ffee49d7b40ab3bf4d5d0dfef4fadc67e46bb44953213e2dc0b
    retrieved_at: '2026-10-22T17:39:41.848518+00:00'
    archive:
      member: CIK0001494259.json
      sha256: 7457a528288f1e3425cba6ffd7370c6c205845aba12761763aa5ae3683c0fdc2
      url: https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip
    acquisition: operator_supplied_sec_bulk_archive
  submissions:
    url: https://data.sec.gov/submissions/CIK0001494259.json
    sha256: 724c781d7d4914c50c34694635247e4c60f558deba92274c6814cddb3c6feb32
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001494259.json
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
  url: https://data.sec.gov/submissions/CIK0001494259.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 724c781d7d4914c50c34694635247e4c60f558deba92274c6814cddb3c6feb32
- id: S03
  title: SEC CompanyFacts source
  url: https://data.sec.gov/api/xbrl/companyfacts/CIK0001494259.json
  published_at: null
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: 78b67d6544657ffee49d7b40ab3bf4d5d0dfef4fadc67e46bb44953213e2dc0b
- id: S04
  title: 10-K 0001193125-26-059435
  url: https://www.sec.gov/Archives/edgar/data/1494259/000119312526059435/0001193125-26-059435-index.html
  published_at: '2026-02-19'
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: null
- id: S05
  title: 10-Q 0001193125-26-338067
  url: https://www.sec.gov/Archives/edgar/data/1494259/000119312526338067/0001193125-26-338067-index.html
  published_at: '2026-08-06'
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: null
- id: S09
  title: 10-Q 0001193125-26-211983
  url: https://www.sec.gov/Archives/edgar/data/1494259/000119312526211983/0001193125-26-211983-index.html
  published_at: '2026-05-07'
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: null
- id: S17
  title: 4 0001494259-26-000085
  url: https://www.sec.gov/Archives/edgar/data/1494259/000149425926000085/0001494259-26-000085-index.html
  published_at: '2026-10-21'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S18
  title: 3 0001494259-26-000083
  url: https://www.sec.gov/Archives/edgar/data/1494259/000149425926000083/0001494259-26-000083-index.html
  published_at: '2026-10-21'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S19
  title: 4 0001494259-26-000080
  url: https://www.sec.gov/Archives/edgar/data/1494259/000149425926000080/0001494259-26-000080-index.html
  published_at: '2026-10-16'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S20
  title: 144 0001959173-26-007380
  url: https://www.sec.gov/Archives/edgar/data/1494259/000195917326007380/0001959173-26-007380-index.html
  published_at: '2026-10-15'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S21
  title: 4 0001494259-26-000078
  url: https://www.sec.gov/Archives/edgar/data/1494259/000149425926000078/0001494259-26-000078-index.html
  published_at: '2026-10-06'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0001494259
  classification_status: reported_sic
  entity_type: operating
  name: CarGurus, Inc.
  sic: '7374'
  sic_description: Services-Computer Processing & Data Preparation
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 724c781d7d4914c50c34694635247e4c60f558deba92274c6814cddb3c6feb32
  url: https://data.sec.gov/submissions/CIK0001494259.json
listings:
- ticker: CARG
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001193125-26-059435
  filed: '2026-02-19'
  form: 10-K
  period_end: '2025-12-31'
  url: https://www.sec.gov/Archives/edgar/data/1494259/000119312526059435/0001193125-26-059435-index.html
- accession: 0001193125-26-338067
  filed: '2026-08-06'
  form: 10-Q
  period_end: '2026-06-30'
  url: https://www.sec.gov/Archives/edgar/data/1494259/000119312526338067/0001193125-26-338067-index.html
- accession: 0001193125-26-170400
  filed: '2026-04-22'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/1494259/000119312526170400/0001193125-26-170400-index.html
- accession: 0001193125-26-381142
  filed: '2026-09-03'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/1494259/000119312526381142/0001193125-26-381142-index.html
- accession: 0001193125-21-041798
  filed: '2021-02-12'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1494259/000119312521041798/0001193125-21-041798-index.html
research_progress:
  stage: pending
  input_sha256: ad7e5a311119efb69e10463b90dcaef9600975e273fb73b5e647a172fb188c77
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
  derived_observations: 8
  model_draft: false
  reviewed: false
sector_assignment:
  sector: information-technology
  method: project_sic_rule
  sic: '7374'
  sic_description: Services-Computer Processing & Data Preparation
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001494259.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/d523cff21b18141b9a37cddd98ad6af6e1a30fa5/brain/companies/CARG/README.md
full_history_commit: d523cff21b18141b9a37cddd98ad6af6e1a30fa5
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# CARG — CarGurus, Inc.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/d523cff21b18141b9a37cddd98ad6af6e1a30fa5/brain/companies/CARG/README.md)

## Business overview

Reported issuer name: **CarGurus, Inc.**. Stable SEC CIK: **0001494259**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| CARG | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **7374**: Services-Computer Processing & Data Preparation. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **information-technology**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

## Financial performance

Derived observation: Operating margin was 26.95% for 2025-01-01 to 2025-12-31 (US GAAP inputs). [S04]
Formula: `operating_income / revenue * 100`. Inputs: operating_income=244445000 USD (OperatingIncomeLoss), revenue=906980000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Net margin was 17.19% for 2025-01-01 to 2025-12-31 (US GAAP inputs). [S04]
Formula: `net_income / revenue * 100`. Inputs: net_income=155903000 USD (NetIncomeLoss), revenue=906980000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Free cash flow margin was 31.85% for 2025-01-01 to 2025-12-31 (US GAAP inputs). [S04]
Formula: `free_cash_flow / revenue * 100`. Inputs: free_cash_flow=288897000 USD (NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment), revenue=906980000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Stock compensation / revenue was 5.56% for 2025-01-01 to 2025-12-31 (US GAAP inputs). [S04]
Formula: `stock_based_compensation / revenue * 100`. Inputs: stock_based_compensation=50439000 USD (ShareBasedCompensation), revenue=906980000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Annual net income changed +643.39% from the year ended 2024-12-31 to 2025-12-31. [S04]
Formula: `(current / prior - 1) * 100`. Inputs: net_income=155903000 USD (NetIncomeLoss), net_income=20972000 USD (NetIncomeLoss).

Derived observation: Annual operating cash flow changed +15.57% from the year ended 2024-12-31 to 2025-12-31. [S04]
Formula: `(current / prior - 1) * 100`. Inputs: operating_cash_flow=295280000 USD (NetCashProvidedByUsedInOperatingActivities), operating_cash_flow=255494000 USD (NetCashProvidedByUsedInOperatingActivities).

Derived observation: Annual free cash flow changed +60.21% from the year ended 2024-12-31 to 2025-12-31. [S04]
Formula: `(current / prior - 1) * 100`. Inputs: free_cash_flow=288897000 USD (NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment), free_cash_flow=180321000 USD (NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment).

Derived observation: Operating cash flow / net income was 1.89x for the year ended 2025-12-31. Working capital and non-cash adjustments require separate filing analysis. [S04]
Formula: `operating_cash_flow / net_income`. Inputs: operating_cash_flow=295280000 USD (NetCashProvidedByUsedInOperatingActivities), net_income=155903000 USD (NetIncomeLoss).

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:39:41.848518+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-01-01 to 2025-12-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -6,383,000 | USD | US GAAP / reported | PaymentsToAcquirePropertyPlantAndEquipment; Cash outflow = negative of reported PaymentsToAcquirePropertyPlantAndEquipment; source value retained. | [S04] |
| cost_of_revenue | 65,467,000 | USD | US GAAP / reported | CostOfGoodsAndServicesSold | [S04] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S04] |
| free_cash_flow | 288,897,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment | [S04] |
| gross_profit | 841,513,000 | USD | US GAAP / reported | GrossProfit | [S04] |
| net_income | 155,903,000 | USD | US GAAP / reported | NetIncomeLoss | [S04] |
| net_income_common | 155,903,000 | USD | US GAAP / reported | NetIncomeLossAvailableToCommonStockholdersBasic | [S04] |
| net_income_including_noncontrolling_interests | 155,903,000 | USD | US GAAP / reported | ProfitLoss | [S04] |
| operating_cash_flow | 295,280,000 | USD | US GAAP / reported | NetCashProvidedByUsedInOperatingActivities | [S04] |
| operating_income | 244,445,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S04] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | 906,980,000 | USD | US GAAP / reported | RevenueFromContractWithCustomerExcludingAssessedTax | [S04] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S04] |
| stock_based_compensation | 50,439,000 | USD | US GAAP / reported | ShareBasedCompensation | [S04] |


### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -562,000 | USD | US GAAP / derived | PaymentsToAcquirePropertyPlantAndEquipment; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S05] [S09] |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | CostOfGoodsAndServicesSold; definition_changed_across_series | [S05] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S05] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S05] |
| free_cash_flow | 94,029,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S05] [S09] |
| gross_profit | 231,098,000 | USD | US GAAP / reported | GrossProfit | [S05] |
| net_income | 49,193,000 | USD | US GAAP / reported | NetIncomeLoss | [S05] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income_including_noncontrolling_interests | 49,193,000 | USD | US GAAP / reported | ProfitLoss | [S05] |
| operating_cash_flow | 94,591,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S05] [S09] |
| operating_income | 62,982,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S05] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | 250,971,000 | USD | US GAAP / reported | RevenueFromContractWithCustomerExcludingAssessedTax | [S05] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S05] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S05] |
| stock_based_compensation | 13,358,000 | USD | US GAAP / derived | ShareBasedCompensation; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S05] [S09] |



## Balance sheet and capital allocation

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:39:41.848518+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-01-01 to 2025-12-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 190,518,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S05] |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebt; debt_scope_requires_filing_review | [S05] |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |


### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 122,136,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S05] |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebt; debt_scope_requires_filing_review | [S05] |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
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
- Collector status: quality_review_required; last action: new_financial_filing; last checked: 2026-10-23T14:30:28.161462+00:00.

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

Calculation gaps: revenue: annual growth withheld because periods, definitions or a positive prior denominator are not verified. operating_income: annual growth withheld because periods, definitions or a positive prior denominator are not verified.

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest five available filing metadata records; document bodies have not been analyzed here.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-10-21 | 4 | 0001494259-26-000085 | — | [S17] |
| 2026-10-21 | 3 | 0001494259-26-000083 | — | [S18] |
| 2026-10-16 | 4 | 0001494259-26-000080 | — | [S19] |
| 2026-10-15 | 144 | 0001959173-26-007380 | — | [S20] |
| 2026-10-06 | 4 | 0001494259-26-000078 | — | [S21] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-23T14:17:54.530395+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001494259.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [SEC CompanyFacts source](https://data.sec.gov/api/xbrl/companyfacts/CIK0001494259.json) — published not supplied; retrieved 2026-10-22T17:39:41.848518+00:00.

[S04] [10-K 0001193125-26-059435](https://www.sec.gov/Archives/edgar/data/1494259/000119312526059435/0001193125-26-059435-index.html) — published 2026-02-19; retrieved 2026-10-22T17:39:41.848518+00:00.

[S05] [10-Q 0001193125-26-338067](https://www.sec.gov/Archives/edgar/data/1494259/000119312526338067/0001193125-26-338067-index.html) — published 2026-08-06; retrieved 2026-10-22T17:39:41.848518+00:00.

[S09] [10-Q 0001193125-26-211983](https://www.sec.gov/Archives/edgar/data/1494259/000119312526211983/0001193125-26-211983-index.html) — published 2026-05-07; retrieved 2026-10-22T17:39:41.848518+00:00.

[S17] [4 0001494259-26-000085](https://www.sec.gov/Archives/edgar/data/1494259/000149425926000085/0001494259-26-000085-index.html) — published 2026-10-21; retrieved 2026-10-23T08:33:02.691743+00:00.

[S18] [3 0001494259-26-000083](https://www.sec.gov/Archives/edgar/data/1494259/000149425926000083/0001494259-26-000083-index.html) — published 2026-10-21; retrieved 2026-10-23T08:33:02.691743+00:00.

[S19] [4 0001494259-26-000080](https://www.sec.gov/Archives/edgar/data/1494259/000149425926000080/0001494259-26-000080-index.html) — published 2026-10-16; retrieved 2026-10-23T08:33:02.691743+00:00.

[S20] [144 0001959173-26-007380](https://www.sec.gov/Archives/edgar/data/1494259/000195917326007380/0001959173-26-007380-index.html) — published 2026-10-15; retrieved 2026-10-23T08:33:02.691743+00:00.

[S21] [4 0001494259-26-000078](https://www.sec.gov/Archives/edgar/data/1494259/000149425926000078/0001494259-26-000078-index.html) — published 2026-10-06; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261023-39968262770-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/d523cff21b18141b9a37cddd98ad6af6e1a30fa5/brain/companies/CARG/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
