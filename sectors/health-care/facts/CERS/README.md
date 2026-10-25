---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001020214
cik: '0001020214'
company_name: CERUS CORP
tickers:
- CERS
status: stub
canonical_reviewed: false
as_of: '2026-10-25'
updated_at: '2026-10-25T13:50:29.910841+00:00'
reviewed_at: null
coverage_release: coverage-20261025-40199010718-1
source_commit: f5f88011907841550f3cf7652c3822295b45cb57
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
  - 15-12G
  - '3'
  - '4'
  - 4/A
  - 424B5
  - 8-A12G/A
  - 8-K
  - 8-K/A
  - ARS
  - CORRESP
  - CT ORDER
  - DEF 14A
  - DEFA14A
  - DEFR14A
  - EFFECT
  - POS AM
  - POSASR
  - PRE 14A
  - S-3
  - S-3/A
  - S-3ASR
  - S-8
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - SD
  - SEC STAFF LETTER
  - UPLOAD
input_sources:
  history:
    url: https://data.sec.gov/api/xbrl/companyfacts/CIK0001020214.json
    sha256: 48781e5ccd06b7d9984488c51a681c262823dcfe67ec6754bc10f19e45035240
    retrieved_at: '2026-10-22T17:53:02.398600+00:00'
    archive:
      member: CIK0001020214.json
      sha256: 7457a528288f1e3425cba6ffd7370c6c205845aba12761763aa5ae3683c0fdc2
      url: https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip
    acquisition: operator_supplied_sec_bulk_archive
  submissions:
    url: https://data.sec.gov/submissions/CIK0001020214.json
    sha256: 4a6e9a8d94033739be83b2d1e883792e4cdf8631ec4fb62d5372e0f38977c542
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001020214.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: nasdaqlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt
  published_at: null
  retrieved_at: '2026-10-25T13:45:47.626200+00:00'
  sha256: 59ac9b74ff663c6de40f5c93a54d5e12eb3fbef74f82e8a7cfc1456ad9f969ec
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001020214.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 4a6e9a8d94033739be83b2d1e883792e4cdf8631ec4fb62d5372e0f38977c542
- id: S03
  title: SEC CompanyFacts source
  url: https://data.sec.gov/api/xbrl/companyfacts/CIK0001020214.json
  published_at: null
  retrieved_at: '2026-10-22T17:53:02.398600+00:00'
  sha256: 48781e5ccd06b7d9984488c51a681c262823dcfe67ec6754bc10f19e45035240
- id: S04
  title: 10-K 0001193125-26-085678
  url: https://www.sec.gov/Archives/edgar/data/1020214/000119312526085678/0001193125-26-085678-index.html
  published_at: '2026-03-02'
  retrieved_at: '2026-10-22T17:53:02.398600+00:00'
  sha256: null
- id: S05
  title: 10-Q 0001193125-26-326295
  url: https://www.sec.gov/Archives/edgar/data/1020214/000119312526326295/0001193125-26-326295-index.html
  published_at: '2026-07-30'
  retrieved_at: '2026-10-22T17:53:02.398600+00:00'
  sha256: null
- id: S09
  title: 10-Q 0001193125-26-197777
  url: https://www.sec.gov/Archives/edgar/data/1020214/000119312526197777/0001193125-26-197777-index.html
  published_at: '2026-04-30'
  retrieved_at: '2026-10-22T17:53:02.398600+00:00'
  sha256: null
- id: S17
  title: 144 0001950047-26-008264
  url: https://www.sec.gov/Archives/edgar/data/1020214/000195004726008264/0001950047-26-008264-index.html
  published_at: '2026-08-17'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S18
  title: 4 0001193125-26-354496
  url: https://www.sec.gov/Archives/edgar/data/1020214/000119312526354496/0001193125-26-354496-index.html
  published_at: '2026-08-17'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S19
  title: SCHEDULE 13G/A 0001104659-26-097037
  url: https://www.sec.gov/Archives/edgar/data/1020214/000110465926097037/0001104659-26-097037-index.html
  published_at: '2026-08-14'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S20
  title: SCHEDULE 13G/A 0001104659-26-096930
  url: https://www.sec.gov/Archives/edgar/data/1020214/000110465926096930/0001104659-26-096930-index.html
  published_at: '2026-08-14'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S21
  title: SCHEDULE 13G/A 0001213900-26-088746
  url: https://www.sec.gov/Archives/edgar/data/1020214/000121390026088746/0001213900-26-088746-index.html
  published_at: '2026-08-13'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: '0001020214'
  classification_status: reported_sic
  entity_type: operating
  name: CERUS CORP
  sic: '3841'
  sic_description: Surgical & Medical Instruments & Apparatus
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 4a6e9a8d94033739be83b2d1e883792e4cdf8631ec4fb62d5372e0f38977c542
  url: https://data.sec.gov/submissions/CIK0001020214.json
listings:
- ticker: CERS
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001193125-26-085678
  filed: '2026-03-02'
  form: 10-K
  period_end: '2025-12-31'
  url: https://www.sec.gov/Archives/edgar/data/1020214/000119312526085678/0001193125-26-085678-index.html
- accession: 0001193125-26-326295
  filed: '2026-07-30'
  form: 10-Q
  period_end: '2026-06-30'
  url: https://www.sec.gov/Archives/edgar/data/1020214/000119312526326295/0001193125-26-326295-index.html
- accession: 0001020214-26-000011
  filed: '2026-04-22'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/1020214/000102021426000011/0001020214-26-000011-index.html
- accession: 0001193125-26-326093
  filed: '2026-07-30'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/1020214/000119312526326093/0001193125-26-326093-index.html
- accession: 0001193125-11-144246
  filed: '2011-05-18'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1020214/000119312511144246/0001193125-11-144246-index.html
research_progress:
  stage: pending
  input_sha256: 5435f82dd482a67a9433122faaf05141c90288e03ee4a96669e69e4a6977284d
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
  derived_observations: 7
  model_draft: false
  reviewed: false
sector_assignment:
  sector: health-care
  method: project_sic_rule
  sic: '3841'
  sic_description: Surgical & Medical Instruments & Apparatus
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001020214.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/71fcd4775048604503d616351f7f309068b23e1b/brain/companies/CERS/README.md
full_history_commit: 71fcd4775048604503d616351f7f309068b23e1b
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# CERS — CERUS CORP

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/71fcd4775048604503d616351f7f309068b23e1b/brain/companies/CERS/README.md)

## Business overview

Reported issuer name: **CERUS CORP**. Stable SEC CIK: **0001020214**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| CERS | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **3841**: Surgical & Medical Instruments & Apparatus. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **health-care**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

## Financial performance

Derived observation: Operating margin was -3.71% for 2025-01-01 to 2025-12-31 (US GAAP inputs). [S04]
Formula: `operating_income / revenue * 100`. Inputs: operating_income=-8681000 USD (OperatingIncomeLoss), revenue=233798000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Net margin was -6.68% for 2025-01-01 to 2025-12-31 (US GAAP inputs). [S04]
Formula: `net_income / revenue * 100`. Inputs: net_income=-15627000 USD (NetIncomeLoss), revenue=233798000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Free cash flow margin was 0.47% for 2025-01-01 to 2025-12-31 (US GAAP inputs). [S04]
Formula: `free_cash_flow / revenue * 100`. Inputs: free_cash_flow=1108000 USD (NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment), revenue=233798000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Stock compensation / revenue was 9.78% for 2025-01-01 to 2025-12-31 (US GAAP inputs). [S04]
Formula: `stock_based_compensation / revenue * 100`. Inputs: stock_based_compensation=22867000 USD (ShareBasedCompensation), revenue=233798000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Annual revenue changed +16.13% from the year ended 2024-12-31 to 2025-12-31. [S04]
Formula: `(current / prior - 1) * 100`. Inputs: revenue=233798000 USD (RevenueFromContractWithCustomerExcludingAssessedTax), revenue=201321000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Annual operating cash flow changed -57.42% from the year ended 2024-12-31 to 2025-12-31. [S04]
Formula: `(current / prior - 1) * 100`. Inputs: operating_cash_flow=4837000 USD (NetCashProvidedByUsedInOperatingActivities), operating_cash_flow=11359000 USD (NetCashProvidedByUsedInOperatingActivities).

Derived observation: Annual free cash flow changed -87.00% from the year ended 2024-12-31 to 2025-12-31. [S04]
Formula: `(current / prior - 1) * 100`. Inputs: free_cash_flow=1108000 USD (NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment), free_cash_flow=8522000 USD (NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment).

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:53:02.398600+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-01-01 to 2025-12-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -3,729,000 | USD | US GAAP / reported | PaymentsToAcquirePropertyPlantAndEquipment; Cash outflow = negative of reported PaymentsToAcquirePropertyPlantAndEquipment; source value retained. | [S04] |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S04] |
| free_cash_flow | 1,108,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment | [S04] |
| gross_profit | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income | -15,627,000 | USD | US GAAP / reported | NetIncomeLoss | [S04] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income_including_noncontrolling_interests | -15,637,000 | USD | US GAAP / reported | ProfitLoss | [S04] |
| operating_cash_flow | 4,837,000 | USD | US GAAP / reported | NetCashProvidedByUsedInOperatingActivities | [S04] |
| operating_income | -8,681,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S04] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | 233,798,000 | USD | US GAAP / reported | RevenueFromContractWithCustomerExcludingAssessedTax | [S04] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S04] |
| stock_based_compensation | 22,867,000 | USD | US GAAP / reported | ShareBasedCompensation | [S04] |


### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -873,000 | USD | US GAAP / derived | PaymentsToAcquirePropertyPlantAndEquipment; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S05] [S09] |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S05] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S05] |
| free_cash_flow | -3,534,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S05] [S09] |
| gross_profit | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income | -2,940,000 | USD | US GAAP / reported | NetIncomeLoss | [S05] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income_including_noncontrolling_interests | -2,982,000 | USD | US GAAP / reported | ProfitLoss | [S05] |
| operating_cash_flow | -2,661,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S05] [S09] |
| operating_income | -1,858,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S05] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | 57,441,000 | USD | US GAAP / reported | RevenueFromContractWithCustomerExcludingAssessedTax | [S05] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S05] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S05] |
| stock_based_compensation | 5,496,000 | USD | US GAAP / derived | ShareBasedCompensation; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S05] [S09] |



## Balance sheet and capital allocation

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:53:02.398600+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-01-01 to 2025-12-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 19,961,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S05] |
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
| cash_and_equivalents | 17,980,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S05] |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
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
- Collector status: quality_review_required; last action: new_financial_filing; last checked: 2026-10-24T13:30:53.119612+00:00.

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

Calculation gaps: operating_income: annual growth withheld because periods, definitions or a positive prior denominator are not verified. net_income: annual growth withheld because periods, definitions or a positive prior denominator are not verified.

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest five available filing metadata records; document bodies have not been analyzed here.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-08-17 | 144 | 0001950047-26-008264 | — | [S17] |
| 2026-08-17 | 4 | 0001193125-26-354496 | — | [S18] |
| 2026-08-14 | SCHEDULE 13G/A | 0001104659-26-097037 | — | [S19] |
| 2026-08-14 | SCHEDULE 13G/A | 0001104659-26-096930 | — | [S20] |
| 2026-08-13 | SCHEDULE 13G/A | 0001213900-26-088746 | — | [S21] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-25T13:45:47.626200+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001020214.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [SEC CompanyFacts source](https://data.sec.gov/api/xbrl/companyfacts/CIK0001020214.json) — published not supplied; retrieved 2026-10-22T17:53:02.398600+00:00.

[S04] [10-K 0001193125-26-085678](https://www.sec.gov/Archives/edgar/data/1020214/000119312526085678/0001193125-26-085678-index.html) — published 2026-03-02; retrieved 2026-10-22T17:53:02.398600+00:00.

[S05] [10-Q 0001193125-26-326295](https://www.sec.gov/Archives/edgar/data/1020214/000119312526326295/0001193125-26-326295-index.html) — published 2026-07-30; retrieved 2026-10-22T17:53:02.398600+00:00.

[S09] [10-Q 0001193125-26-197777](https://www.sec.gov/Archives/edgar/data/1020214/000119312526197777/0001193125-26-197777-index.html) — published 2026-04-30; retrieved 2026-10-22T17:53:02.398600+00:00.

[S17] [144 0001950047-26-008264](https://www.sec.gov/Archives/edgar/data/1020214/000195004726008264/0001950047-26-008264-index.html) — published 2026-08-17; retrieved 2026-10-23T08:33:02.691743+00:00.

[S18] [4 0001193125-26-354496](https://www.sec.gov/Archives/edgar/data/1020214/000119312526354496/0001193125-26-354496-index.html) — published 2026-08-17; retrieved 2026-10-23T08:33:02.691743+00:00.

[S19] [SCHEDULE 13G/A 0001104659-26-097037](https://www.sec.gov/Archives/edgar/data/1020214/000110465926097037/0001104659-26-097037-index.html) — published 2026-08-14; retrieved 2026-10-23T08:33:02.691743+00:00.

[S20] [SCHEDULE 13G/A 0001104659-26-096930](https://www.sec.gov/Archives/edgar/data/1020214/000110465926096930/0001104659-26-096930-index.html) — published 2026-08-14; retrieved 2026-10-23T08:33:02.691743+00:00.

[S21] [SCHEDULE 13G/A 0001213900-26-088746](https://www.sec.gov/Archives/edgar/data/1020214/000121390026088746/0001213900-26-088746-index.html) — published 2026-08-13; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261025-40199010718-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/71fcd4775048604503d616351f7f309068b23e1b/brain/companies/CERS/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
