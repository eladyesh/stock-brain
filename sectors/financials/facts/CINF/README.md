---
schema_version: 1
document_type: company_facts
company_id: company-cik-0000020286
cik: 0000020286
company_name: CINCINNATI FINANCIAL CORP
tickers:
- CINF
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
  - 10-Q
  - 11-K
  - 13F-HR
  - '3'
  - '4'
  - 4/A
  - '5'
  - 8-K
  - 8-K/A
  - CORRESP
  - DEF 14A
  - DEFA14A
  - EFFECT
  - N-PX
  - PRE 14A
  - S-3
  - S-8
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  history:
    url: https://data.sec.gov/api/xbrl/companyfacts/CIK0000020286.json
    sha256: 9ff1ea6e63c2113938817e6f8c7f9840717f453a1653f5550271580cda58d648
    retrieved_at: '2026-10-22T17:53:02.398600+00:00'
    archive:
      member: CIK0000020286.json
      sha256: 7457a528288f1e3425cba6ffd7370c6c205845aba12761763aa5ae3683c0fdc2
      url: https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip
    acquisition: operator_supplied_sec_bulk_archive
  submissions:
    url: https://data.sec.gov/submissions/CIK0000020286.json
    sha256: acbaa6f02061e22330310977da3b9b9cbd4bae35b73fc8753b4ce5bebf258423
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0000020286.json
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
  url: https://data.sec.gov/submissions/CIK0000020286.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: acbaa6f02061e22330310977da3b9b9cbd4bae35b73fc8753b4ce5bebf258423
- id: S03
  title: SEC CompanyFacts source
  url: https://data.sec.gov/api/xbrl/companyfacts/CIK0000020286.json
  published_at: null
  retrieved_at: '2026-10-22T17:53:02.398600+00:00'
  sha256: 9ff1ea6e63c2113938817e6f8c7f9840717f453a1653f5550271580cda58d648
- id: S04
  title: 10-K 0000020286-26-000008
  url: https://www.sec.gov/Archives/edgar/data/20286/000002028626000008/0000020286-26-000008-index.html
  published_at: '2026-02-23'
  retrieved_at: '2026-10-22T17:53:02.398600+00:00'
  sha256: null
- id: S05
  title: 10-Q 0000020286-26-000045
  url: https://www.sec.gov/Archives/edgar/data/20286/000002028626000045/0000020286-26-000045-index.html
  published_at: '2026-07-27'
  retrieved_at: '2026-10-22T17:53:02.398600+00:00'
  sha256: null
- id: S14
  title: 10-Q 0000020286-26-000026
  url: https://www.sec.gov/Archives/edgar/data/20286/000002028626000026/0000020286-26-000026-index.html
  published_at: '2026-04-27'
  retrieved_at: '2026-10-22T17:53:02.398600+00:00'
  sha256: null
- id: S19
  title: 8-K 0000020286-26-000052
  url: https://www.sec.gov/Archives/edgar/data/20286/000002028626000052/0000020286-26-000052-index.html
  published_at: '2026-09-28'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S20
  title: 4 0001289454-26-000006
  url: https://www.sec.gov/Archives/edgar/data/20286/000128945426000006/0001289454-26-000006-index.html
  published_at: '2026-08-27'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S21
  title: N-PX 0001104659-26-101132
  url: https://www.sec.gov/Archives/edgar/data/20286/000110465926101132/0001104659-26-101132-index.html
  published_at: '2026-08-26'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S22
  title: 8-K 0000020286-26-000049
  url: https://www.sec.gov/Archives/edgar/data/20286/000002028626000049/0000020286-26-000049-index.html
  published_at: '2026-08-25'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S23
  title: 8-K 0000020286-26-000047
  url: https://www.sec.gov/Archives/edgar/data/20286/000002028626000047/0000020286-26-000047-index.html
  published_at: '2026-08-21'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0000020286
  classification_status: reported_sic
  entity_type: operating
  name: CINCINNATI FINANCIAL CORP
  sic: '6331'
  sic_description: Fire, Marine & Casualty Insurance
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: acbaa6f02061e22330310977da3b9b9cbd4bae35b73fc8753b4ce5bebf258423
  url: https://data.sec.gov/submissions/CIK0000020286.json
listings:
- ticker: CINF
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0000020286-26-000008
  filed: '2026-02-23'
  form: 10-K
  period_end: '2025-12-31'
  url: https://www.sec.gov/Archives/edgar/data/20286/000002028626000008/0000020286-26-000008-index.html
- accession: 0000020286-26-000045
  filed: '2026-07-27'
  form: 10-Q
  period_end: '2026-06-30'
  url: https://www.sec.gov/Archives/edgar/data/20286/000002028626000045/0000020286-26-000045-index.html
- accession: 0000020286-26-000015
  filed: '2026-03-18'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/20286/000002028626000015/0000020286-26-000015-index.html
- accession: 0000020286-26-000052
  filed: '2026-09-28'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/20286/000002028626000052/0000020286-26-000052-index.html
- accession: 0000020286-23-000065
  filed: '2023-08-25'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/20286/000002028623000065/0000020286-23-000065-index.html
- accession: 0000020286-19-000071
  filed: '2019-11-14'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/20286/000002028619000071/0000020286-19-000071-index.html
- accession: 0000020286-19-000050
  filed: '2019-08-05'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/20286/000002028619000050/0000020286-19-000050-index.html
research_progress:
  stage: pending
  input_sha256: c568823056c5f058907ad41651968da95c5c1faf47322c6f419e7278fd0c1dc7
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
  derived_observations: 7
  model_draft: false
  reviewed: false
sector_assignment:
  sector: financials
  method: project_sic_rule
  sic: '6331'
  sic_description: Fire, Marine & Casualty Insurance
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0000020286.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/71fcd4775048604503d616351f7f309068b23e1b/brain/companies/CINF/README.md
full_history_commit: 71fcd4775048604503d616351f7f309068b23e1b
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# CINF — CINCINNATI FINANCIAL CORP

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/71fcd4775048604503d616351f7f309068b23e1b/brain/companies/CINF/README.md)

## Business overview

Reported issuer name: **CINCINNATI FINANCIAL CORP**. Stable SEC CIK: **0000020286**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| CINF | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **6331**: Fire, Marine & Casualty Insurance. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **financials**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

## Financial performance

Derived observation: Net margin was 18.95% for 2025-01-01 to 2025-12-31 (US GAAP inputs). [S04]
Formula: `net_income / revenue * 100`. Inputs: net_income=2393000000 USD (NetIncomeLoss), revenue=12631000000 USD (Revenues).

Derived observation: Free cash flow margin was 24.48% for 2025-01-01 to 2025-12-31 (US GAAP inputs). [S04]
Formula: `free_cash_flow / revenue * 100`. Inputs: free_cash_flow=3092000000 USD (NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment), revenue=12631000000 USD (Revenues).

Derived observation: Annual revenue changed +11.41% from the year ended 2024-12-31 to 2025-12-31. [S04]
Formula: `(current / prior - 1) * 100`. Inputs: revenue=12631000000 USD (Revenues), revenue=11337000000 USD (Revenues).

Derived observation: Annual net income changed +4.41% from the year ended 2024-12-31 to 2025-12-31. [S04]
Formula: `(current / prior - 1) * 100`. Inputs: net_income=2393000000 USD (NetIncomeLoss), net_income=2292000000 USD (NetIncomeLoss).

Derived observation: Annual operating cash flow changed +17.48% from the year ended 2024-12-31 to 2025-12-31. [S04]
Formula: `(current / prior - 1) * 100`. Inputs: operating_cash_flow=3112000000 USD (NetCashProvidedByUsedInOperatingActivities), operating_cash_flow=2649000000 USD (NetCashProvidedByUsedInOperatingActivities).

Derived observation: Annual free cash flow changed +17.70% from the year ended 2024-12-31 to 2025-12-31. [S04]
Formula: `(current / prior - 1) * 100`. Inputs: free_cash_flow=3092000000 USD (NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment), free_cash_flow=2627000000 USD (NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment).

Derived observation: Operating cash flow / net income was 1.30x for the year ended 2025-12-31. Working capital and non-cash adjustments require separate filing analysis. [S04]
Formula: `operating_cash_flow / net_income`. Inputs: operating_cash_flow=3112000000 USD (NetCashProvidedByUsedInOperatingActivities), net_income=2393000000 USD (NetIncomeLoss).

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:53:02.398600+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-01-01 to 2025-12-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -20,000,000 | USD | US GAAP / reported | PaymentsToAcquirePropertyPlantAndEquipment; Cash outflow = negative of reported PaymentsToAcquirePropertyPlantAndEquipment; source value retained. | [S04] |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S04] |
| free_cash_flow | 3,092,000,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment | [S04] |
| gross_profit | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income | 2,393,000,000 | USD | US GAAP / reported | NetIncomeLoss | [S04] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income_including_noncontrolling_interests | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| operating_cash_flow | 3,112,000,000 | USD | US GAAP / reported | NetCashProvidedByUsedInOperatingActivities | [S04] |
| operating_income | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | 12,631,000,000 | USD | US GAAP / reported | Revenues | [S04] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S04] |
| stock_based_compensation | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |


### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -2,000,000 | USD | US GAAP / derived | PaymentsToAcquirePropertyPlantAndEquipment; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S05] [S14] |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S05] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S05] |
| free_cash_flow | 698,000,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S05] [S14] |
| gross_profit | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income | 1,255,000,000 | USD | US GAAP / reported | NetIncomeLoss | [S05] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income_including_noncontrolling_interests | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| operating_cash_flow | 700,000,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S05] [S14] |
| operating_income | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | 4,274,000,000 | USD | US GAAP / reported | Revenues | [S05] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S05] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S05] |
| stock_based_compensation | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |



## Balance sheet and capital allocation

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:53:02.398600+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-01-01 to 2025-12-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 1,431,000,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S05] |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtAndCapitalLeaseObligations; debt_scope_requires_filing_review | [S05] |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebt; debt_scope_requires_filing_review | [S05] |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | 148,000,000 | USD | US GAAP / reported | ShortTermInvestments | [S05] |


### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 1,750,000,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S05] |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtAndCapitalLeaseObligations; debt_scope_requires_filing_review | [S05] |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebt; debt_scope_requires_filing_review | [S05] |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | 142,000,000 | USD | US GAAP / reported | ShortTermInvestments | [S05] |



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
- Collector status: quality_review_required; last action: new_financial_filing; last checked: 2026-10-24T13:27:20.754938+00:00.

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

Calculation gaps: Operating margin: compatible positive revenue and usable inputs are required. Stock compensation / revenue: compatible positive revenue and usable inputs are required. operating_income: annual growth withheld because periods, definitions or a positive prior denominator are not verified.

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest five available filing metadata records; document bodies have not been analyzed here.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-09-28 | 8-K | 0000020286-26-000052 | — | [S19] |
| 2026-08-27 | 4 | 0001289454-26-000006 | — | [S20] |
| 2026-08-26 | N-PX | 0001104659-26-101132 | — | [S21] |
| 2026-08-25 | 8-K | 0000020286-26-000049 | — | [S22] |
| 2026-08-21 | 8-K | 0000020286-26-000047 | — | [S23] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-25T13:45:47.626200+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0000020286.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [SEC CompanyFacts source](https://data.sec.gov/api/xbrl/companyfacts/CIK0000020286.json) — published not supplied; retrieved 2026-10-22T17:53:02.398600+00:00.

[S04] [10-K 0000020286-26-000008](https://www.sec.gov/Archives/edgar/data/20286/000002028626000008/0000020286-26-000008-index.html) — published 2026-02-23; retrieved 2026-10-22T17:53:02.398600+00:00.

[S05] [10-Q 0000020286-26-000045](https://www.sec.gov/Archives/edgar/data/20286/000002028626000045/0000020286-26-000045-index.html) — published 2026-07-27; retrieved 2026-10-22T17:53:02.398600+00:00.

[S14] [10-Q 0000020286-26-000026](https://www.sec.gov/Archives/edgar/data/20286/000002028626000026/0000020286-26-000026-index.html) — published 2026-04-27; retrieved 2026-10-22T17:53:02.398600+00:00.

[S19] [8-K 0000020286-26-000052](https://www.sec.gov/Archives/edgar/data/20286/000002028626000052/0000020286-26-000052-index.html) — published 2026-09-28; retrieved 2026-10-23T08:33:02.691743+00:00.

[S20] [4 0001289454-26-000006](https://www.sec.gov/Archives/edgar/data/20286/000128945426000006/0001289454-26-000006-index.html) — published 2026-08-27; retrieved 2026-10-23T08:33:02.691743+00:00.

[S21] [N-PX 0001104659-26-101132](https://www.sec.gov/Archives/edgar/data/20286/000110465926101132/0001104659-26-101132-index.html) — published 2026-08-26; retrieved 2026-10-23T08:33:02.691743+00:00.

[S22] [8-K 0000020286-26-000049](https://www.sec.gov/Archives/edgar/data/20286/000002028626000049/0000020286-26-000049-index.html) — published 2026-08-25; retrieved 2026-10-23T08:33:02.691743+00:00.

[S23] [8-K 0000020286-26-000047](https://www.sec.gov/Archives/edgar/data/20286/000002028626000047/0000020286-26-000047-index.html) — published 2026-08-21; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261025-40199010718-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/71fcd4775048604503d616351f7f309068b23e1b/brain/companies/CINF/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
