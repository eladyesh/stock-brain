---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001117297
cik: 0001117297
company_name: QUINSTREET, INC
tickers:
- QNST
status: stub
canonical_reviewed: false
as_of: '2026-10-27'
updated_at: '2026-10-27T15:30:18.641431+00:00'
reviewed_at: null
coverage_release: coverage-20261027-40530587641-1
source_commit: 77264ce478c0c699392c0a049f464d4fda44c9f8
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
  - 10-Q/A
  - '144'
  - 144/A
  - '3'
  - 3/A
  - '4'
  - 4/A
  - '5'
  - 8-K
  - 8-K/A
  - ARS
  - CORRESP
  - CT ORDER
  - DEF 14A
  - DEFA14A
  - NT 10-Q
  - S-8
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  history:
    url: https://data.sec.gov/api/xbrl/companyfacts/CIK0001117297.json
    sha256: 992d910f4d9701cfa719bc2e62dae96ae46a31dbb9b7170d44a96972ee907c1a
    retrieved_at: '2026-10-22T17:39:41.848518+00:00'
    archive:
      member: CIK0001117297.json
      sha256: 7457a528288f1e3425cba6ffd7370c6c205845aba12761763aa5ae3683c0fdc2
      url: https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip
    acquisition: operator_supplied_sec_bulk_archive
  submissions:
    url: https://data.sec.gov/submissions/CIK0001117297.json
    sha256: e4a2efaebee0da4bf9d78bc0181233ce02e117e8087fec055ef7767baab90d30
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001117297.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: nasdaqlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt
  published_at: null
  retrieved_at: '2026-10-27T15:25:33.739265+00:00'
  sha256: 29c7cedde394d9fb806c731f8be32ec8c78cad2668852342db80ae28619465f0
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001117297.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: e4a2efaebee0da4bf9d78bc0181233ce02e117e8087fec055ef7767baab90d30
- id: S03
  title: SEC CompanyFacts source
  url: https://data.sec.gov/api/xbrl/companyfacts/CIK0001117297.json
  published_at: null
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: 992d910f4d9701cfa719bc2e62dae96ae46a31dbb9b7170d44a96972ee907c1a
- id: S04
  title: 10-K 0001193125-26-367160
  url: https://www.sec.gov/Archives/edgar/data/1117297/000119312526367160/0001193125-26-367160-index.html
  published_at: '2026-08-26'
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: null
- id: S09
  title: 10-Q 0001193125-26-213979
  url: https://www.sec.gov/Archives/edgar/data/1117297/000119312526213979/0001193125-26-213979-index.html
  published_at: '2026-05-08'
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: null
- id: S17
  title: DEF 14A 0002077096-26-000254
  url: https://www.sec.gov/Archives/edgar/data/1117297/000207709626000254/0002077096-26-000254-index.html
  published_at: '2026-09-16'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S18
  title: 10-K 0001193125-26-367160
  url: https://www.sec.gov/Archives/edgar/data/1117297/000119312526367160/0001193125-26-367160-index.html
  published_at: '2026-08-26'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S19
  title: 144 0001959173-26-006141
  url: https://www.sec.gov/Archives/edgar/data/1117297/000195917326006141/0001959173-26-006141-index.html
  published_at: '2026-08-18'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S20
  title: 4 0001858936-26-000004
  url: https://www.sec.gov/Archives/edgar/data/1117297/000185893626000004/0001858936-26-000004-index.html
  published_at: '2026-08-18'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S21
  title: 4 0001563458-26-000014
  url: https://www.sec.gov/Archives/edgar/data/1117297/000156345826000014/0001563458-26-000014-index.html
  published_at: '2026-08-18'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0001117297
  classification_status: reported_sic
  entity_type: operating
  name: QUINSTREET, INC
  sic: '7389'
  sic_description: Services-Business Services, NEC
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: e4a2efaebee0da4bf9d78bc0181233ce02e117e8087fec055ef7767baab90d30
  url: https://data.sec.gov/submissions/CIK0001117297.json
listings:
- ticker: QNST
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001193125-26-367160
  filed: '2026-08-26'
  form: 10-K
  period_end: '2026-06-30'
  url: https://www.sec.gov/Archives/edgar/data/1117297/000119312526367160/0001193125-26-367160-index.html
- accession: 0001193125-26-213979
  filed: '2026-05-08'
  form: 10-Q
  period_end: '2026-03-31'
  url: https://www.sec.gov/Archives/edgar/data/1117297/000119312526213979/0001193125-26-213979-index.html
- accession: 0002077096-26-000254
  filed: '2026-09-16'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/1117297/000207709626000254/0002077096-26-000254-index.html
- accession: 0001193125-26-338042
  filed: '2026-08-06'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/1117297/000119312526338042/0001193125-26-338042-index.html
- accession: 0001193125-26-105702
  filed: '2026-03-13'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1117297/000119312526105702/0001193125-26-105702-index.html
- accession: 0001564590-18-030993
  filed: '2018-12-17'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1117297/000156459018030993/0001564590-18-030993-index.html
research_progress:
  stage: pending
  input_sha256: cb68f81252f87b5037740c8625fee1363e8c966a90e6af896556e6ee402ab9b0
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
  derived_observations: 5
  model_draft: false
  reviewed: false
sector_assignment:
  sector: industrials
  method: project_sic_rule
  sic: '7389'
  sic_description: Services-Business Services, NEC
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001117297.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/f974cdc6ffee05a6e0489d88d3e13c8eebf0b613/brain/companies/QNST/README.md
full_history_commit: f974cdc6ffee05a6e0489d88d3e13c8eebf0b613
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# QNST — QUINSTREET, INC

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/f974cdc6ffee05a6e0489d88d3e13c8eebf0b613/brain/companies/QNST/README.md)

## Business overview

Reported issuer name: **QUINSTREET, INC**. Stable SEC CIK: **0001117297**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| QNST | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **7389**: Services-Business Services, NEC. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **industrials**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

## Financial performance

Derived observation: Operating margin was 2.74% for 2025-07-01 to 2026-06-30 (US GAAP inputs). [S18]
Formula: `operating_income / revenue * 100`. Inputs: operating_income=35426000 USD (OperatingIncomeLoss), revenue=1293712000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Net margin was 6.28% for 2025-07-01 to 2026-06-30 (US GAAP inputs). [S18]
Formula: `net_income / revenue * 100`. Inputs: net_income=81235000 USD (NetIncomeLoss), revenue=1293712000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Free cash flow margin was 9.89% for 2025-07-01 to 2026-06-30 (US GAAP inputs). [S18]
Formula: `free_cash_flow / revenue * 100`. Inputs: free_cash_flow=127906000 USD (NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment), revenue=1293712000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Stock compensation / revenue was 2.89% for 2025-07-01 to 2026-06-30 (US GAAP inputs). [S18]
Formula: `stock_based_compensation / revenue * 100`. Inputs: stock_based_compensation=37432000 USD (ShareBasedCompensation), revenue=1293712000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Operating cash flow / net income was 1.62x for the year ended 2026-06-30. Working capital and non-cash adjustments require separate filing analysis. [S18]
Formula: `operating_cash_flow / net_income`. Inputs: operating_cash_flow=131303000 USD (NetCashProvidedByUsedInOperatingActivities), net_income=81235000 USD (NetIncomeLoss).

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:39:41.848518+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-07-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -3,397,000 | USD | US GAAP / reported | PaymentsToAcquirePropertyPlantAndEquipment; Cash outflow = negative of reported PaymentsToAcquirePropertyPlantAndEquipment; source value retained. | [S04] |
| cost_of_revenue | 1,147,903,000 | USD | US GAAP / reported | CostOfRevenue | [S04] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S04] |
| free_cash_flow | 127,906,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment | [S04] |
| gross_profit | 145,809,000 | USD | US GAAP / reported | GrossProfit | [S04] |
| net_income | 81,235,000 | USD | US GAAP / reported | NetIncomeLoss | [S04] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income_including_noncontrolling_interests | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| operating_cash_flow | 131,303,000 | USD | US GAAP / reported | NetCashProvidedByUsedInOperatingActivities | [S04] |
| operating_income | 35,426,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S04] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | 1,293,712,000 | USD | US GAAP / reported | RevenueFromContractWithCustomerExcludingAssessedTax | [S04] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S04] |
| stock_based_compensation | 37,432,000 | USD | US GAAP / reported | ShareBasedCompensation | [S04] |


### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -797,000 | USD | US GAAP / derived | PaymentsToAcquirePropertyPlantAndEquipment; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S09] |
| cost_of_revenue | 324,066,000 | USD | US GAAP / derived | CostOfRevenue; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S09] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| free_cash_flow | 52,350,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S09] |
| gross_profit | 49,811,000 | USD | US GAAP / derived | GrossProfit; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S09] |
| net_income | 19,111,000 | USD | US GAAP / derived | NetIncomeLoss; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S09] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income_including_noncontrolling_interests | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| operating_cash_flow | 53,147,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S09] |
| operating_income | 19,123,000 | USD | US GAAP / derived | OperatingIncomeLoss; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S09] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | 373,877,000 | USD | US GAAP / derived | RevenueFromContractWithCustomerExcludingAssessedTax; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S09] |
| shares_basic | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_diluted | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| stock_based_compensation | 10,187,000 | USD | US GAAP / derived | ShareBasedCompensation; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S09] |



## Balance sheet and capital allocation

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:39:41.848518+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-07-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 128,315,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S04] |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtNoncurrent; debt_scope_requires_filing_review | [S04] |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S04] |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |


### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 128,315,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S04] |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtNoncurrent; debt_scope_requires_filing_review | [S04] |
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
- Collector status: quality_review_required; last action: new_financial_filing; last checked: 2026-10-24T13:31:46.635224+00:00.

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

Calculation gaps: revenue: annual growth withheld because periods, definitions or a positive prior denominator are not verified. operating_income: annual growth withheld because periods, definitions or a positive prior denominator are not verified. net_income: annual growth withheld because periods, definitions or a positive prior denominator are not verified. operating_cash_flow: annual growth withheld because periods, definitions or a positive prior denominator are not verified. free_cash_flow: annual growth withheld because periods, definitions or a positive prior denominator are not verified.

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest five available filing metadata records; document bodies have not been analyzed here.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-09-16 | DEF 14A | 0002077096-26-000254 | — | [S17] |
| 2026-08-26 | 10-K | 0001193125-26-367160 | — | [S18] |
| 2026-08-18 | 144 | 0001959173-26-006141 | — | [S19] |
| 2026-08-18 | 4 | 0001858936-26-000004 | — | [S20] |
| 2026-08-18 | 4 | 0001563458-26-000014 | — | [S21] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-27T15:25:33.739265+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001117297.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [SEC CompanyFacts source](https://data.sec.gov/api/xbrl/companyfacts/CIK0001117297.json) — published not supplied; retrieved 2026-10-22T17:39:41.848518+00:00.

[S04] [10-K 0001193125-26-367160](https://www.sec.gov/Archives/edgar/data/1117297/000119312526367160/0001193125-26-367160-index.html) — published 2026-08-26; retrieved 2026-10-22T17:39:41.848518+00:00.

[S09] [10-Q 0001193125-26-213979](https://www.sec.gov/Archives/edgar/data/1117297/000119312526213979/0001193125-26-213979-index.html) — published 2026-05-08; retrieved 2026-10-22T17:39:41.848518+00:00.

[S17] [DEF 14A 0002077096-26-000254](https://www.sec.gov/Archives/edgar/data/1117297/000207709626000254/0002077096-26-000254-index.html) — published 2026-09-16; retrieved 2026-10-23T08:33:02.691743+00:00.

[S18] [10-K 0001193125-26-367160](https://www.sec.gov/Archives/edgar/data/1117297/000119312526367160/0001193125-26-367160-index.html) — published 2026-08-26; retrieved 2026-10-23T08:33:02.691743+00:00.

[S19] [144 0001959173-26-006141](https://www.sec.gov/Archives/edgar/data/1117297/000195917326006141/0001959173-26-006141-index.html) — published 2026-08-18; retrieved 2026-10-23T08:33:02.691743+00:00.

[S20] [4 0001858936-26-000004](https://www.sec.gov/Archives/edgar/data/1117297/000185893626000004/0001858936-26-000004-index.html) — published 2026-08-18; retrieved 2026-10-23T08:33:02.691743+00:00.

[S21] [4 0001563458-26-000014](https://www.sec.gov/Archives/edgar/data/1117297/000156345826000014/0001563458-26-000014-index.html) — published 2026-08-18; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261027-40530587641-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/f974cdc6ffee05a6e0489d88d3e13c8eebf0b613/brain/companies/QNST/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
