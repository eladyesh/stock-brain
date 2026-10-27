---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001877184
cik: 0001877184
company_name: KESTRA MEDICAL TECHNOLOGIES, LTD.
tickers:
- KMTS
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
  - 10-Q
  - '144'
  - '3'
  - '4'
  - 4/A
  - 424B4
  - 8-A12B
  - 8-K
  - ARS
  - CERT
  - CORRESP
  - DEF 14A
  - DEFA14A
  - DRS
  - DRS/A
  - DRSLTR
  - EFFECT
  - S-1
  - S-1/A
  - S-1MEF
  - S-3ASR
  - S-8
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  history:
    url: https://data.sec.gov/api/xbrl/companyfacts/CIK0001877184.json
    sha256: 349255c9a0b63038a49963b03c273268a4ab92a4aa83703220500dec893270fb
    retrieved_at: '2026-10-22T17:39:41.848518+00:00'
    archive:
      member: CIK0001877184.json
      sha256: 7457a528288f1e3425cba6ffd7370c6c205845aba12761763aa5ae3683c0fdc2
      url: https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip
    acquisition: operator_supplied_sec_bulk_archive
  submissions:
    url: https://data.sec.gov/submissions/CIK0001877184.json
    sha256: db5d28bd0a11cb72be1a42541d7138995a7c9977490f98f3a81b2b810e183428
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001877184.json
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
  url: https://data.sec.gov/submissions/CIK0001877184.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: db5d28bd0a11cb72be1a42541d7138995a7c9977490f98f3a81b2b810e183428
- id: S03
  title: SEC CompanyFacts source
  url: https://data.sec.gov/api/xbrl/companyfacts/CIK0001877184.json
  published_at: null
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: 349255c9a0b63038a49963b03c273268a4ab92a4aa83703220500dec893270fb
- id: S04
  title: 10-K 0001193125-26-303397
  url: https://www.sec.gov/Archives/edgar/data/1877184/000119312526303397/0001193125-26-303397-index.html
  published_at: '2026-07-14'
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: null
- id: S05
  title: 10-Q 0001193125-26-390766
  url: https://www.sec.gov/Archives/edgar/data/1877184/000119312526390766/0001193125-26-390766-index.html
  published_at: '2026-09-14'
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: null
- id: S09
  title: 4 0001193125-26-428980
  url: https://www.sec.gov/Archives/edgar/data/1877184/000119312526428980/0001193125-26-428980-index.html
  published_at: '2026-10-22'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S10
  title: 4 0001193125-26-428976
  url: https://www.sec.gov/Archives/edgar/data/1877184/000119312526428976/0001193125-26-428976-index.html
  published_at: '2026-10-22'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S11
  title: 144 0001964306-26-000473
  url: https://www.sec.gov/Archives/edgar/data/1877184/000196430626000473/0001964306-26-000473-index.html
  published_at: '2026-10-21'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S12
  title: 144 0001964306-26-000472
  url: https://www.sec.gov/Archives/edgar/data/1877184/000196430626000472/0001964306-26-000472-index.html
  published_at: '2026-10-20'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S13
  title: 4 0001193125-26-410928
  url: https://www.sec.gov/Archives/edgar/data/1877184/000119312526410928/0001193125-26-410928-index.html
  published_at: '2026-10-01'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0001877184
  classification_status: reported_sic
  entity_type: operating
  name: KESTRA MEDICAL TECHNOLOGIES, LTD.
  sic: '3841'
  sic_description: Surgical & Medical Instruments & Apparatus
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: db5d28bd0a11cb72be1a42541d7138995a7c9977490f98f3a81b2b810e183428
  url: https://data.sec.gov/submissions/CIK0001877184.json
listings:
- ticker: KMTS
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001193125-26-303397
  filed: '2026-07-14'
  form: 10-K
  period_end: '2026-04-30'
  url: https://www.sec.gov/Archives/edgar/data/1877184/000119312526303397/0001193125-26-303397-index.html
- accession: 0001193125-26-390766
  filed: '2026-09-14'
  form: 10-Q
  period_end: '2026-07-31'
  url: https://www.sec.gov/Archives/edgar/data/1877184/000119312526390766/0001193125-26-390766-index.html
- accession: 0001193125-26-320956
  filed: '2026-07-28'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/1877184/000119312526320956/0001193125-26-320956-index.html
- accession: 0001193125-26-390535
  filed: '2026-09-14'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/1877184/000119312526390535/0001193125-26-390535-index.html
research_progress:
  stage: pending
  input_sha256: eba9e9b2d74b8d698e7cfeb67e9e79e52da1dbab1057009fcaccbfcb56f235af
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
  derived_observations: 5
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
  source_url: https://data.sec.gov/submissions/CIK0001877184.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/f974cdc6ffee05a6e0489d88d3e13c8eebf0b613/brain/companies/KMTS/README.md
full_history_commit: f974cdc6ffee05a6e0489d88d3e13c8eebf0b613
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# KMTS — KESTRA MEDICAL TECHNOLOGIES, LTD.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/f974cdc6ffee05a6e0489d88d3e13c8eebf0b613/brain/companies/KMTS/README.md)

## Business overview

Reported issuer name: **KESTRA MEDICAL TECHNOLOGIES, LTD.**. Stable SEC CIK: **0001877184**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| KMTS | NASDAQ | common_stock | 1 | [S01] |

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

Derived observation: Operating margin was -141.64% for 2025-05-01 to 2026-04-30 (US GAAP inputs). [S04]
Formula: `operating_income / revenue * 100`. Inputs: operating_income=-134741000 USD (OperatingIncomeLoss), revenue=95126000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Net margin was -138.36% for 2025-05-01 to 2026-04-30 (US GAAP inputs). [S04]
Formula: `net_income / revenue * 100`. Inputs: net_income=-131612000 USD (NetIncomeLoss), revenue=95126000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Free cash flow margin was -122.57% for 2025-05-01 to 2026-04-30 (US GAAP inputs). [S04]
Formula: `free_cash_flow / revenue * 100`. Inputs: free_cash_flow=-116595000 USD (NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment), revenue=95126000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Stock compensation / revenue was 35.37% for 2025-05-01 to 2026-04-30 (US GAAP inputs). [S04]
Formula: `stock_based_compensation / revenue * 100`. Inputs: stock_based_compensation=33644000 USD (ShareBasedCompensation), revenue=95126000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Annual revenue changed +59.03% from the year ended 2025-04-30 to 2026-04-30. [S04]
Formula: `(current / prior - 1) * 100`. Inputs: revenue=95126000 USD (RevenueFromContractWithCustomerExcludingAssessedTax), revenue=59815000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:39:41.848518+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-05-01 to 2026-04-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -34,892,000 | USD | US GAAP / reported | PaymentsToAcquirePropertyPlantAndEquipment; Cash outflow = negative of reported PaymentsToAcquirePropertyPlantAndEquipment; source value retained. | [S04] |
| cost_of_revenue | 46,263,000 | USD | US GAAP / reported | CostOfGoodsAndServicesSold | [S04] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S04] |
| free_cash_flow | -116,595,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment | [S04] |
| gross_profit | 48,863,000 | USD | US GAAP / reported | GrossProfit | [S04] |
| net_income | -131,612,000 | USD | US GAAP / reported | NetIncomeLoss | [S04] |
| net_income_common | -131,612,000 | USD | US GAAP / reported | NetIncomeLossAvailableToCommonStockholdersBasic | [S04] |
| net_income_including_noncontrolling_interests | -131,612,000 | USD | US GAAP / reported | ProfitLoss | [S04] |
| operating_cash_flow | -81,703,000 | USD | US GAAP / reported | NetCashProvidedByUsedInOperatingActivities | [S04] |
| operating_income | -134,741,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S04] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | 95,126,000 | USD | US GAAP / reported | RevenueFromContractWithCustomerExcludingAssessedTax | [S04] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S04] |
| stock_based_compensation | 33,644,000 | USD | US GAAP / reported | ShareBasedCompensation | [S04] |


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
| net_income_common | Unavailable / blocked | USD | US GAAP / reported / not model usable | NetIncomeLossAvailableToCommonStockholdersBasic; conflicting_fiscal_year | [S05] |
| net_income_including_noncontrolling_interests | Unavailable / blocked | USD | US GAAP / reported / not model usable | ProfitLoss; conflicting_fiscal_year | [S05] |
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

### annual: 2025-05-01 to 2026-04-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 99,710,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S05] |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtNoncurrent; debt_scope_requires_filing_review | [S05] |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S05] |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | 96,724,000 | USD | US GAAP / reported | ShortTermInvestments | [S05] |


### quarterly: 2026-05-01 to 2026-07-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | Unavailable / blocked | USD | US GAAP / reported / not model usable | CashAndCashEquivalentsAtCarryingValue; conflicting_fiscal_year | [S05] |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; conflicting_fiscal_year | No eligible evidence |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtNoncurrent; conflicting_fiscal_year, debt_scope_requires_filing_review | [S05] |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; conflicting_fiscal_year | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; conflicting_fiscal_year | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; conflicting_fiscal_year, share_split_and_corporate_action_basis_unverified | [S05] |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; conflicting_fiscal_year | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / reported / not model usable | ShortTermInvestments; conflicting_fiscal_year | [S05] |



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
- Collector status: quality_review_required; last action: new_financial_filing; last checked: 2026-10-24T13:36:16.727110+00:00.

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

Calculation gaps: operating_income: annual growth withheld because periods, definitions or a positive prior denominator are not verified. net_income: annual growth withheld because periods, definitions or a positive prior denominator are not verified. operating_cash_flow: annual growth withheld because periods, definitions or a positive prior denominator are not verified. free_cash_flow: annual growth withheld because periods, definitions or a positive prior denominator are not verified.

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest five available filing metadata records; document bodies have not been analyzed here.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-10-22 | 4 | 0001193125-26-428980 | — | [S09] |
| 2026-10-22 | 4 | 0001193125-26-428976 | — | [S10] |
| 2026-10-21 | 144 | 0001964306-26-000473 | — | [S11] |
| 2026-10-20 | 144 | 0001964306-26-000472 | — | [S12] |
| 2026-10-01 | 4 | 0001193125-26-410928 | — | [S13] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-27T15:25:33.739265+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001877184.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [SEC CompanyFacts source](https://data.sec.gov/api/xbrl/companyfacts/CIK0001877184.json) — published not supplied; retrieved 2026-10-22T17:39:41.848518+00:00.

[S04] [10-K 0001193125-26-303397](https://www.sec.gov/Archives/edgar/data/1877184/000119312526303397/0001193125-26-303397-index.html) — published 2026-07-14; retrieved 2026-10-22T17:39:41.848518+00:00.

[S05] [10-Q 0001193125-26-390766](https://www.sec.gov/Archives/edgar/data/1877184/000119312526390766/0001193125-26-390766-index.html) — published 2026-09-14; retrieved 2026-10-22T17:39:41.848518+00:00.

[S09] [4 0001193125-26-428980](https://www.sec.gov/Archives/edgar/data/1877184/000119312526428980/0001193125-26-428980-index.html) — published 2026-10-22; retrieved 2026-10-23T08:33:02.691743+00:00.

[S10] [4 0001193125-26-428976](https://www.sec.gov/Archives/edgar/data/1877184/000119312526428976/0001193125-26-428976-index.html) — published 2026-10-22; retrieved 2026-10-23T08:33:02.691743+00:00.

[S11] [144 0001964306-26-000473](https://www.sec.gov/Archives/edgar/data/1877184/000196430626000473/0001964306-26-000473-index.html) — published 2026-10-21; retrieved 2026-10-23T08:33:02.691743+00:00.

[S12] [144 0001964306-26-000472](https://www.sec.gov/Archives/edgar/data/1877184/000196430626000472/0001964306-26-000472-index.html) — published 2026-10-20; retrieved 2026-10-23T08:33:02.691743+00:00.

[S13] [4 0001193125-26-410928](https://www.sec.gov/Archives/edgar/data/1877184/000119312526410928/0001193125-26-410928-index.html) — published 2026-10-01; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261027-40530587641-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/f974cdc6ffee05a6e0489d88d3e13c8eebf0b613/brain/companies/KMTS/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
