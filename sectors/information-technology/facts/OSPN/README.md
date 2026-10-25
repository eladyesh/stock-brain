---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001044777
cik: '0001044777'
company_name: OneSpan Inc.
tickers:
- OSPN
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
  - 10-Q/A
  - '144'
  - '3'
  - 3/A
  - '4'
  - 4/A
  - '5'
  - 8-K
  - 8-K/A
  - ARS
  - CORRESP
  - DEF 14A
  - DEFA14A
  - DEFC14A
  - DEFR14A
  - DFAN14A
  - DFRN14A
  - EFFECT
  - NT 10-Q
  - PREC14A
  - PRRN14A
  - S-3
  - S-8
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SC TO-C
  - SC TO-I
  - SC TO-I/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - SD
  - SD/A
  - UPLOAD
input_sources:
  history:
    url: https://data.sec.gov/api/xbrl/companyfacts/CIK0001044777.json
    sha256: 32ae5cead11923f18383af7d37bf117c61daa6e2b1c7b512d1b66f2543cef06d
    retrieved_at: '2026-10-22T18:10:35.452616+00:00'
    archive:
      member: CIK0001044777.json
      sha256: 7457a528288f1e3425cba6ffd7370c6c205845aba12761763aa5ae3683c0fdc2
      url: https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip
    acquisition: operator_supplied_sec_bulk_archive
  submissions:
    url: https://data.sec.gov/submissions/CIK0001044777.json
    sha256: 9ca8775375eb54259681a207ff3c9df9eca5c0d9d87b9d55596c4368213815c8
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001044777.json
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
  url: https://data.sec.gov/submissions/CIK0001044777.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 9ca8775375eb54259681a207ff3c9df9eca5c0d9d87b9d55596c4368213815c8
- id: S03
  title: SEC CompanyFacts source
  url: https://data.sec.gov/api/xbrl/companyfacts/CIK0001044777.json
  published_at: null
  retrieved_at: '2026-10-22T18:10:35.452616+00:00'
  sha256: 32ae5cead11923f18383af7d37bf117c61daa6e2b1c7b512d1b66f2543cef06d
- id: S04
  title: 10-K 0001044777-26-000008
  url: https://www.sec.gov/Archives/edgar/data/1044777/000104477726000008/0001044777-26-000008-index.html
  published_at: '2026-02-26'
  retrieved_at: '2026-10-22T18:10:35.452616+00:00'
  sha256: null
- id: S05
  title: 10-Q 0001044777-26-000040
  url: https://www.sec.gov/Archives/edgar/data/1044777/000104477726000040/0001044777-26-000040-index.html
  published_at: '2026-08-04'
  retrieved_at: '2026-10-22T18:10:35.452616+00:00'
  sha256: null
- id: S09
  title: 10-Q 0001044777-26-000019
  url: https://www.sec.gov/Archives/edgar/data/1044777/000104477726000019/0001044777-26-000019-index.html
  published_at: '2026-04-30'
  retrieved_at: '2026-10-22T18:10:35.452616+00:00'
  sha256: null
- id: S17
  title: SCHEDULE 13G 0000354204-26-001075
  url: https://www.sec.gov/Archives/edgar/data/1044777/000035420426001075/0000354204-26-001075-index.html
  published_at: '2026-10-08'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S18
  title: 4 0001943565-26-000010
  url: https://www.sec.gov/Archives/edgar/data/1044777/000194356526000010/0001943565-26-000010-index.html
  published_at: '2026-09-08'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S19
  title: 4 0001935707-26-000007
  url: https://www.sec.gov/Archives/edgar/data/1044777/000193570726000007/0001935707-26-000007-index.html
  published_at: '2026-09-08'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S20
  title: 4 0001383360-26-000005
  url: https://www.sec.gov/Archives/edgar/data/1044777/000138336026000005/0001383360-26-000005-index.html
  published_at: '2026-09-08'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S21
  title: SCHEDULE 13G/A 0002012383-26-003228
  url: https://www.sec.gov/Archives/edgar/data/1044777/000201238326003228/0002012383-26-003228-index.html
  published_at: '2026-08-06'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S51
  title: 10-K 0001044777-26-000008
  url: https://www.sec.gov/Archives/edgar/data/1044777/000104477726000008/0001044777-26-000008-index.html
  published_at: '2026-02-26'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: '0001044777'
  classification_status: reported_sic
  entity_type: operating
  name: OneSpan Inc.
  sic: '7373'
  sic_description: Services-Computer Integrated Systems Design
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 9ca8775375eb54259681a207ff3c9df9eca5c0d9d87b9d55596c4368213815c8
  url: https://data.sec.gov/submissions/CIK0001044777.json
listings:
- ticker: OSPN
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001044777-26-000008
  filed: '2026-02-26'
  form: 10-K
  period_end: '2025-12-31'
  url: https://www.sec.gov/Archives/edgar/data/1044777/000104477726000008/0001044777-26-000008-index.html
- accession: 0001044777-26-000040
  filed: '2026-08-04'
  form: 10-Q
  period_end: '2026-06-30'
  url: https://www.sec.gov/Archives/edgar/data/1044777/000104477726000040/0001044777-26-000040-index.html
- accession: 0001044777-26-000011
  filed: '2026-04-23'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/1044777/000104477726000011/0001044777-26-000011-index.html
- accession: 0001044777-26-000038
  filed: '2026-08-04'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/1044777/000104477726000038/0001044777-26-000038-index.html
- accession: 0001628280-24-008570
  filed: '2024-03-04'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1044777/000162828024008570/0001628280-24-008570-index.html
- accession: 0001558370-21-012182
  filed: '2021-09-02'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1044777/000155837021012182/0001558370-21-012182-index.html
- accession: 0001387131-21-005236
  filed: '2021-05-03'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1044777/000138713121005236/0001387131-21-005236-index.html
- accession: 0001558370-18-006452
  filed: '2018-08-06'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1044777/000155837018006452/0001558370-18-006452-index.html
- accession: 0001558370-17-009371
  filed: '2017-12-18'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1044777/000155837017009371/0001558370-17-009371-index.html
- accession: 0001193125-16-452366
  filed: '2016-02-05'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1044777/000119312516452366/0001193125-16-452366-index.html
- accession: 0001193125-13-308932
  filed: '2013-07-30'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1044777/000119312513308932/0001193125-13-308932-index.html
- accession: 0001193125-11-263272
  filed: '2011-10-04'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1044777/000119312511263272/0001193125-11-263272-index.html
research_progress:
  stage: pending
  input_sha256: add1f2708c16915ea5c3d8bd9e1379958221a8fed0ddb4a004522e8d7f14d676
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
  derived_observations: 5
  model_draft: false
  reviewed: false
sector_assignment:
  sector: information-technology
  method: project_sic_rule
  sic: '7373'
  sic_description: Services-Computer Integrated Systems Design
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001044777.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/71fcd4775048604503d616351f7f309068b23e1b/brain/companies/OSPN/README.md
full_history_commit: 71fcd4775048604503d616351f7f309068b23e1b
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# OSPN — OneSpan Inc.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/71fcd4775048604503d616351f7f309068b23e1b/brain/companies/OSPN/README.md)

## Business overview

Reported issuer name: **OneSpan Inc.**. Stable SEC CIK: **0001044777**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| OSPN | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **7373**: Services-Computer Integrated Systems Design. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **information-technology**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

## Financial performance

Derived observation: Annual operating income changed +8.13% from the year ended 2024-12-31 to 2025-12-31. [S51]
Formula: `(current / prior - 1) * 100`. Inputs: operating_income=48446000 USD (OperatingIncomeLoss), operating_income=44805000 USD (OperatingIncomeLoss).

Derived observation: Annual net income changed +27.72% from the year ended 2024-12-31 to 2025-12-31. [S51]
Formula: `(current / prior - 1) * 100`. Inputs: net_income=72904000 USD (NetIncomeLoss), net_income=57082000 USD (NetIncomeLoss).

Derived observation: Annual operating cash flow changed +6.80% from the year ended 2024-12-31 to 2025-12-31. [S51]
Formula: `(current / prior - 1) * 100`. Inputs: operating_cash_flow=59454000 USD (NetCashProvidedByUsedInOperatingActivities), operating_cash_flow=55667000 USD (NetCashProvidedByUsedInOperatingActivities).

Derived observation: Annual free cash flow changed +8.77% from the year ended 2024-12-31 to 2025-12-31. [S51]
Formula: `(current / prior - 1) * 100`. Inputs: free_cash_flow=50495000 USD (NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment), free_cash_flow=46422000 USD (NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment).

Derived observation: Operating cash flow / net income was 0.82x for the year ended 2025-12-31. Working capital and non-cash adjustments require separate filing analysis. [S51]
Formula: `operating_cash_flow / net_income`. Inputs: operating_cash_flow=59454000 USD (NetCashProvidedByUsedInOperatingActivities), net_income=72904000 USD (NetIncomeLoss).

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T18:10:35.452616+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-01-01 to 2025-12-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -8,959,000 | USD | US GAAP / reported | PaymentsToAcquirePropertyPlantAndEquipment; Cash outflow = negative of reported PaymentsToAcquirePropertyPlantAndEquipment; source value retained. | [S04] |
| cost_of_revenue | 63,826,000 | USD | US GAAP / reported | CostOfGoodsAndServicesSold | [S04] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S04] |
| free_cash_flow | 50,495,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment | [S04] |
| gross_profit | 179,354,000 | USD | US GAAP / reported | GrossProfit | [S04] |
| net_income | 72,904,000 | USD | US GAAP / reported | NetIncomeLoss | [S04] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income_including_noncontrolling_interests | 72,904,000 | USD | US GAAP / reported | ProfitLoss | [S04] |
| operating_cash_flow | 59,454,000 | USD | US GAAP / reported | NetCashProvidedByUsedInOperatingActivities | [S04] |
| operating_income | 48,446,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S04] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | RevenueFromContractWithCustomerExcludingAssessedTax; definition_changed_across_series | [S04] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S04] |
| stock_based_compensation | 11,196,000 | USD | US GAAP / reported | ShareBasedCompensation | [S04] |


### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -3,177,000 | USD | US GAAP / derived | PaymentsToAcquirePropertyPlantAndEquipment; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S05] [S09] |
| cost_of_revenue | 15,983,000 | USD | US GAAP / reported | CostOfGoodsAndServicesSold | [S05] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S05] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S05] |
| free_cash_flow | -3,280,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S05] [S09] |
| gross_profit | 44,483,000 | USD | US GAAP / reported | GrossProfit | [S05] |
| net_income | 6,781,000 | USD | US GAAP / reported | NetIncomeLoss | [S05] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income_including_noncontrolling_interests | 6,781,000 | USD | US GAAP / derived | ProfitLoss; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S05] [S09] |
| operating_cash_flow | -103,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S05] [S09] |
| operating_income | 8,741,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S05] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | RevenueFromContractWithCustomerExcludingAssessedTax; definition_changed_across_series | [S05] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S05] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S05] |
| stock_based_compensation | 3,442,000 | USD | US GAAP / reported | ShareBasedCompensation | [S05] |



## Balance sheet and capital allocation

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T18:10:35.452616+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-01-01 to 2025-12-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 70,499,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S05] |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S05] |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |


### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 43,337,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S05] |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
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
- Collector status: quality_review_required; last action: new_financial_filing; last checked: 2026-10-24T13:31:09.010710+00:00.

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
| 2026-10-08 | SCHEDULE 13G | 0000354204-26-001075 | — | [S17] |
| 2026-09-08 | 4 | 0001943565-26-000010 | — | [S18] |
| 2026-09-08 | 4 | 0001935707-26-000007 | — | [S19] |
| 2026-09-08 | 4 | 0001383360-26-000005 | — | [S20] |
| 2026-08-06 | SCHEDULE 13G/A | 0002012383-26-003228 | — | [S21] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-25T13:45:47.626200+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001044777.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [SEC CompanyFacts source](https://data.sec.gov/api/xbrl/companyfacts/CIK0001044777.json) — published not supplied; retrieved 2026-10-22T18:10:35.452616+00:00.

[S04] [10-K 0001044777-26-000008](https://www.sec.gov/Archives/edgar/data/1044777/000104477726000008/0001044777-26-000008-index.html) — published 2026-02-26; retrieved 2026-10-22T18:10:35.452616+00:00.

[S05] [10-Q 0001044777-26-000040](https://www.sec.gov/Archives/edgar/data/1044777/000104477726000040/0001044777-26-000040-index.html) — published 2026-08-04; retrieved 2026-10-22T18:10:35.452616+00:00.

[S09] [10-Q 0001044777-26-000019](https://www.sec.gov/Archives/edgar/data/1044777/000104477726000019/0001044777-26-000019-index.html) — published 2026-04-30; retrieved 2026-10-22T18:10:35.452616+00:00.

[S17] [SCHEDULE 13G 0000354204-26-001075](https://www.sec.gov/Archives/edgar/data/1044777/000035420426001075/0000354204-26-001075-index.html) — published 2026-10-08; retrieved 2026-10-23T08:33:02.691743+00:00.

[S18] [4 0001943565-26-000010](https://www.sec.gov/Archives/edgar/data/1044777/000194356526000010/0001943565-26-000010-index.html) — published 2026-09-08; retrieved 2026-10-23T08:33:02.691743+00:00.

[S19] [4 0001935707-26-000007](https://www.sec.gov/Archives/edgar/data/1044777/000193570726000007/0001935707-26-000007-index.html) — published 2026-09-08; retrieved 2026-10-23T08:33:02.691743+00:00.

[S20] [4 0001383360-26-000005](https://www.sec.gov/Archives/edgar/data/1044777/000138336026000005/0001383360-26-000005-index.html) — published 2026-09-08; retrieved 2026-10-23T08:33:02.691743+00:00.

[S21] [SCHEDULE 13G/A 0002012383-26-003228](https://www.sec.gov/Archives/edgar/data/1044777/000201238326003228/0002012383-26-003228-index.html) — published 2026-08-06; retrieved 2026-10-23T08:33:02.691743+00:00.

[S51] [10-K 0001044777-26-000008](https://www.sec.gov/Archives/edgar/data/1044777/000104477726000008/0001044777-26-000008-index.html) — published 2026-02-26; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261025-40199010718-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/71fcd4775048604503d616351f7f309068b23e1b/brain/companies/OSPN/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
