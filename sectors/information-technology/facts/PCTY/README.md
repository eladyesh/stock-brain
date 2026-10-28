---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001591698
cik: 0001591698
company_name: Paylocity Holding Corp
tickers:
- PCTY
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
  - 10-Q
  - '144'
  - '3'
  - 3/A
  - '4'
  - 4/A
  - 8-K
  - 8-K/A
  - ARS
  - DEF 14A
  - DEFA14A
  - PRE 14A
  - S-8
  - S-8 POS
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13G/A
input_sources:
  history:
    url: https://data.sec.gov/api/xbrl/companyfacts/CIK0001591698.json
    sha256: 3f8cf86b9e24f0cc83cb31b8ebde3959826aafacbdfabb9f35226d8bdb06f99e
    retrieved_at: '2026-10-23T08:33:18.308731+00:00'
    archive:
      member: CIK0001591698.json
      sha256: 75d1cc8bca6d990b787653521a352ab25164869485705a9fb49551e8e65a9650
      url: https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip
    acquisition: operator_supplied_sec_bulk_archive
  submissions:
    url: https://data.sec.gov/submissions/CIK0001591698.json
    sha256: b0e7e7299ebe7b2ed3032cb4a974a9cabd7d1e9bef5edd3d99da972b4d2df05b
    retrieved_at: '2026-10-24T13:22:51.759433+00:00'
    archive: &id001
      member: CIK0001591698.json
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
  url: https://data.sec.gov/submissions/CIK0001591698.json
  published_at: null
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: b0e7e7299ebe7b2ed3032cb4a974a9cabd7d1e9bef5edd3d99da972b4d2df05b
- id: S03
  title: SEC CompanyFacts source
  url: https://data.sec.gov/api/xbrl/companyfacts/CIK0001591698.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:18.308731+00:00'
  sha256: 3f8cf86b9e24f0cc83cb31b8ebde3959826aafacbdfabb9f35226d8bdb06f99e
- id: S04
  title: 10-K 0001591698-26-000069
  url: https://www.sec.gov/Archives/edgar/data/1591698/000159169826000069/0001591698-26-000069-index.html
  published_at: '2026-08-05'
  retrieved_at: '2026-10-23T08:33:18.308731+00:00'
  sha256: null
- id: S08
  title: 10-Q 0001591698-26-000037
  url: https://www.sec.gov/Archives/edgar/data/1591698/000159169826000037/0001591698-26-000037-index.html
  published_at: '2026-05-08'
  retrieved_at: '2026-10-23T08:33:18.308731+00:00'
  sha256: null
- id: S17
  title: 144 0001968582-26-001072
  url: https://www.sec.gov/Archives/edgar/data/1591698/000196858226001072/0001968582-26-001072-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S18
  title: 4 0001597870-26-000021
  url: https://www.sec.gov/Archives/edgar/data/1591698/000159787026000021/0001597870-26-000021-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S19
  title: 4 0001597870-26-000019
  url: https://www.sec.gov/Archives/edgar/data/1591698/000159787026000019/0001597870-26-000019-index.html
  published_at: '2026-10-22'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S20
  title: ARS 0001591698-26-000147
  url: https://www.sec.gov/Archives/edgar/data/1591698/000159169826000147/0001591698-26-000147-index.html
  published_at: '2026-10-22'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S21
  title: DEFA14A 0001591698-26-000146
  url: https://www.sec.gov/Archives/edgar/data/1591698/000159169826000146/0001591698-26-000146-index.html
  published_at: '2026-10-22'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
issuer_classification:
  cik: 0001591698
  classification_status: reported_sic
  entity_type: operating
  name: Paylocity Holding Corp
  sic: '7372'
  sic_description: Services-Prepackaged Software
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: b0e7e7299ebe7b2ed3032cb4a974a9cabd7d1e9bef5edd3d99da972b4d2df05b
  url: https://data.sec.gov/submissions/CIK0001591698.json
listings:
- ticker: PCTY
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001591698-26-000069
  filed: '2026-08-05'
  form: 10-K
  period_end: '2026-06-30'
  url: https://www.sec.gov/Archives/edgar/data/1591698/000159169826000069/0001591698-26-000069-index.html
- accession: 0001591698-26-000037
  filed: '2026-05-08'
  form: 10-Q
  period_end: '2026-03-31'
  url: https://www.sec.gov/Archives/edgar/data/1591698/000159169826000037/0001591698-26-000037-index.html
- accession: 0001591698-26-000144
  filed: '2026-10-22'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/1591698/000159169826000144/0001591698-26-000144-index.html
- accession: 0001591698-26-000131
  filed: '2026-09-17'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/1591698/000159169826000131/0001591698-26-000131-index.html
- accession: 0001591698-24-000181
  filed: '2024-08-19'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1591698/000159169824000181/0001591698-24-000181-index.html
- accession: 0001104659-20-070833
  filed: '2020-06-08'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1591698/000110465920070833/0001104659-20-070833-index.html
research_progress:
  stage: pending
  input_sha256: 314c73d2f97513f16c0d1c852b2a05813b504ad3ad9df05fc228df754f7f5f2b
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
  sic: '7372'
  sic_description: Services-Prepackaged Software
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001591698.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/5da532c3abee5b40a5400c5864c6f3f4593276d7/brain/companies/PCTY/README.md
full_history_commit: 5da532c3abee5b40a5400c5864c6f3f4593276d7
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# PCTY — Paylocity Holding Corp

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/5da532c3abee5b40a5400c5864c6f3f4593276d7/brain/companies/PCTY/README.md)

## Business overview

Reported issuer name: **Paylocity Holding Corp**. Stable SEC CIK: **0001591698**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| PCTY | NASDAQ | common_stock | 1 | [S01] |

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

Derived observation: Annual operating income changed +26.96% from the year ended 2025-06-30 to 2026-06-30. [S04]
Formula: `(current / prior - 1) * 100`. Inputs: operating_income=385993000 USD (OperatingIncomeLoss), operating_income=304024000 USD (OperatingIncomeLoss).

Derived observation: Annual net income changed +18.76% from the year ended 2025-06-30 to 2026-06-30. [S04]
Formula: `(current / prior - 1) * 100`. Inputs: net_income=269741000 USD (NetIncomeLoss), net_income=227127000 USD (NetIncomeLoss).

Derived observation: Annual operating cash flow changed +27.50% from the year ended 2025-06-30 to 2026-06-30. [S04]
Formula: `(current / prior - 1) * 100`. Inputs: operating_cash_flow=533252000 USD (NetCashProvidedByUsedInOperatingActivities), operating_cash_flow=418226000 USD (NetCashProvidedByUsedInOperatingActivities).

Derived observation: Annual free cash flow changed +22.69% from the year ended 2025-06-30 to 2026-06-30. [S04]
Formula: `(current / prior - 1) * 100`. Inputs: free_cash_flow=497100000 USD (NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment), free_cash_flow=405153000 USD (NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment).

Derived observation: Operating cash flow / net income was 1.98x for the year ended 2026-06-30. Working capital and non-cash adjustments require separate filing analysis. [S04]
Formula: `operating_cash_flow / net_income`. Inputs: operating_cash_flow=533252000 USD (NetCashProvidedByUsedInOperatingActivities), net_income=269741000 USD (NetIncomeLoss).

Evidence cutoff: 2026-10-23. Source retrieved: 2026-10-23T08:33:18.308731+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-07-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -36,152,000 | USD | US GAAP / reported | PaymentsToAcquirePropertyPlantAndEquipment; Cash outflow = negative of reported PaymentsToAcquirePropertyPlantAndEquipment; source value retained. | [S04] |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | CostOfGoodsAndServicesSold; gross_profit_tieout_failed | [S04] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S04] |
| free_cash_flow | 497,100,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment | [S04] |
| gross_profit | Unavailable / blocked | USD | US GAAP / reported / not model usable | GrossProfit; gross_profit_tieout_failed | [S04] |
| net_income | 269,741,000 | USD | US GAAP / reported | NetIncomeLoss | [S04] |
| net_income_common | 269,741,000 | USD | US GAAP / reported | NetIncomeLossAvailableToCommonStockholdersBasic | [S04] |
| net_income_including_noncontrolling_interests | 269,741,000 | USD | US GAAP / reported | ProfitLoss | [S04] |
| operating_cash_flow | 533,252,000 | USD | US GAAP / reported | NetCashProvidedByUsedInOperatingActivities | [S04] |
| operating_income | 385,993,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S04] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | RevenueFromContractWithCustomerExcludingAssessedTax; alternative_tag_scope_differs, gross_profit_tieout_failed | [S04] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S04] |
| stock_based_compensation | 138,657,000 | USD | US GAAP / reported | ShareBasedCompensation | [S04] |


### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -20,634,000 | USD | US GAAP / derived | PaymentsToAcquirePropertyPlantAndEquipment; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / derived / not model usable | CostOfGoodsAndServicesSold; cross_filing_derivation, gross_profit_tieout_failed, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| free_cash_flow | 91,259,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| gross_profit | Unavailable / blocked | USD | US GAAP / derived / not model usable | GrossProfit; cross_filing_derivation, gross_profit_tieout_failed, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| net_income | 60,303,000 | USD | US GAAP / derived | NetIncomeLoss; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| net_income_common | 60,303,000 | USD | US GAAP / derived | NetIncomeLossAvailableToCommonStockholdersBasic; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| net_income_including_noncontrolling_interests | 60,303,000 | USD | US GAAP / derived | ProfitLoss; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| operating_cash_flow | 111,893,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| operating_income | 84,422,000 | USD | US GAAP / derived | OperatingIncomeLoss; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | Unavailable / blocked | USD | US GAAP / derived / not model usable | RevenueFromContractWithCustomerExcludingAssessedTax; cross_filing_derivation, gross_profit_tieout_failed, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| shares_basic | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_diluted | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| stock_based_compensation | 27,154,000 | USD | US GAAP / derived | ShareBasedCompensation; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |



## Balance sheet and capital allocation

Evidence cutoff: 2026-10-23. Source retrieved: 2026-10-23T08:33:18.308731+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-07-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 271,917,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S04] |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebt; debt_scope_requires_filing_review | [S04] |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S04] |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |


### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 271,917,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S04] |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebt; debt_scope_requires_filing_review | [S04] |
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
- Collector status: quality_review_required; last action: new_financial_filing; last checked: 2026-10-24T13:34:23.533379+00:00.

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
| 2026-10-23 | 144 | 0001968582-26-001072 | — | [S17] |
| 2026-10-23 | 4 | 0001597870-26-000021 | — | [S18] |
| 2026-10-22 | 4 | 0001597870-26-000019 | — | [S19] |
| 2026-10-22 | ARS | 0001591698-26-000147 | — | [S20] |
| 2026-10-22 | DEFA14A | 0001591698-26-000146 | — | [S21] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-28T16:09:01.738588+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001591698.json) — published not supplied; retrieved 2026-10-24T13:22:51.759433+00:00.

[S03] [SEC CompanyFacts source](https://data.sec.gov/api/xbrl/companyfacts/CIK0001591698.json) — published not supplied; retrieved 2026-10-23T08:33:18.308731+00:00.

[S04] [10-K 0001591698-26-000069](https://www.sec.gov/Archives/edgar/data/1591698/000159169826000069/0001591698-26-000069-index.html) — published 2026-08-05; retrieved 2026-10-23T08:33:18.308731+00:00.

[S08] [10-Q 0001591698-26-000037](https://www.sec.gov/Archives/edgar/data/1591698/000159169826000037/0001591698-26-000037-index.html) — published 2026-05-08; retrieved 2026-10-23T08:33:18.308731+00:00.

[S17] [144 0001968582-26-001072](https://www.sec.gov/Archives/edgar/data/1591698/000196858226001072/0001968582-26-001072-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S18] [4 0001597870-26-000021](https://www.sec.gov/Archives/edgar/data/1591698/000159787026000021/0001597870-26-000021-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S19] [4 0001597870-26-000019](https://www.sec.gov/Archives/edgar/data/1591698/000159787026000019/0001597870-26-000019-index.html) — published 2026-10-22; retrieved 2026-10-24T13:22:51.759433+00:00.

[S20] [ARS 0001591698-26-000147](https://www.sec.gov/Archives/edgar/data/1591698/000159169826000147/0001591698-26-000147-index.html) — published 2026-10-22; retrieved 2026-10-24T13:22:51.759433+00:00.

[S21] [DEFA14A 0001591698-26-000146](https://www.sec.gov/Archives/edgar/data/1591698/000159169826000146/0001591698-26-000146-index.html) — published 2026-10-22; retrieved 2026-10-24T13:22:51.759433+00:00.

Source release: `coverage-20261028-40722802424-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/5da532c3abee5b40a5400c5864c6f3f4593276d7/brain/companies/PCTY/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
