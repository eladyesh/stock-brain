---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001037038
cik: 0001037038
company_name: RALPH LAUREN CORP
tickers:
- RL
status: stub
canonical_reviewed: false
as_of: '2026-10-25'
updated_at: '2026-10-25T13:50:29.910841+00:00'
reviewed_at: null
coverage_release: coverage-20261025-40199010718-1
source_commit: d4303e1efab53027fe4e6e90633e2c69b11c599c
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
  - 424B5
  - '5'
  - 8-K
  - ARS
  - CORRESP
  - DEF 14A
  - DEFA14A
  - FWP
  - S-3ASR
  - S-8
  - S-8 POS
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - SD
  - UPLOAD
input_sources:
  history:
    url: https://data.sec.gov/api/xbrl/companyfacts/CIK0001037038.json
    sha256: 9941afcadb20bb4ecf7958fe71a236ff4491ffe74a659b55b7c6737d81217e31
    retrieved_at: '2026-10-22T17:53:02.398600+00:00'
    archive:
      member: CIK0001037038.json
      sha256: 7457a528288f1e3425cba6ffd7370c6c205845aba12761763aa5ae3683c0fdc2
      url: https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip
    acquisition: operator_supplied_sec_bulk_archive
  submissions:
    url: https://data.sec.gov/submissions/CIK0001037038.json
    sha256: 7b3e79963e6ceaf0ce90411dc6555492e00ef91a2dfd32d9d085832d2ef913df
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001037038.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: otherlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt
  published_at: null
  retrieved_at: '2026-10-25T13:45:48.334682+00:00'
  sha256: 94335ed3f4abc4bbd58a4415d105d453184f5484eaf6a2884d1bfb0120d850c9
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001037038.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 7b3e79963e6ceaf0ce90411dc6555492e00ef91a2dfd32d9d085832d2ef913df
- id: S03
  title: SEC CompanyFacts source
  url: https://data.sec.gov/api/xbrl/companyfacts/CIK0001037038.json
  published_at: null
  retrieved_at: '2026-10-22T17:53:02.398600+00:00'
  sha256: 9941afcadb20bb4ecf7958fe71a236ff4491ffe74a659b55b7c6737d81217e31
- id: S04
  title: 10-K 0001628280-26-037074
  url: https://www.sec.gov/Archives/edgar/data/1037038/000162828026037074/0001628280-26-037074-index.html
  published_at: '2026-05-21'
  retrieved_at: '2026-10-22T17:53:02.398600+00:00'
  sha256: null
- id: S05
  title: 10-Q 0001628280-26-053992
  url: https://www.sec.gov/Archives/edgar/data/1037038/000162828026053992/0001628280-26-053992-index.html
  published_at: '2026-08-06'
  retrieved_at: '2026-10-22T17:53:02.398600+00:00'
  sha256: null
- id: S17
  title: 4 0000950142-26-002766
  url: https://www.sec.gov/Archives/edgar/data/1037038/000095014226002766/0000950142-26-002766-index.html
  published_at: '2026-10-14'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S18
  title: 4 0000950142-26-002765
  url: https://www.sec.gov/Archives/edgar/data/1037038/000095014226002765/0000950142-26-002765-index.html
  published_at: '2026-10-14'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S19
  title: 4 0000950142-26-002764
  url: https://www.sec.gov/Archives/edgar/data/1037038/000095014226002764/0000950142-26-002764-index.html
  published_at: '2026-10-14'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S20
  title: 4 0000950142-26-002763
  url: https://www.sec.gov/Archives/edgar/data/1037038/000095014226002763/0000950142-26-002763-index.html
  published_at: '2026-10-14'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S21
  title: 4 0000950142-26-002762
  url: https://www.sec.gov/Archives/edgar/data/1037038/000095014226002762/0000950142-26-002762-index.html
  published_at: '2026-10-14'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0001037038
  classification_status: reported_sic
  entity_type: operating
  name: RALPH LAUREN CORP
  sic: '2320'
  sic_description: Men's & Boys' Furnishgs, Work Clothg, & Allied Garments
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 7b3e79963e6ceaf0ce90411dc6555492e00ef91a2dfd32d9d085832d2ef913df
  url: https://data.sec.gov/submissions/CIK0001037038.json
listings:
- ticker: RL
  exchange: NYSE
  instrument_type: common_stock
research_filings:
- accession: 0001628280-26-037074
  filed: '2026-05-21'
  form: 10-K
  period_end: '2026-03-28'
  url: https://www.sec.gov/Archives/edgar/data/1037038/000162828026037074/0001628280-26-037074-index.html
- accession: 0001628280-26-053992
  filed: '2026-08-06'
  form: 10-Q
  period_end: '2026-06-27'
  url: https://www.sec.gov/Archives/edgar/data/1037038/000162828026053992/0001628280-26-053992-index.html
- accession: 0001140361-26-025788
  filed: '2026-06-18'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/1037038/000114036126025788/0001140361-26-025788-index.html
- accession: 0000950142-26-002493
  filed: '2026-09-03'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/1037038/000095014226002493/0000950142-26-002493-index.html
research_progress:
  stage: pending
  input_sha256: b88be81be1b1d5756b41191b37ae20ff3729fad28d659619ba0ddd4fee6f66a2
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
  derived_observations: 8
  model_draft: false
  reviewed: false
sector_assignment:
  sector: consumer-discretionary
  method: project_sic_rule
  sic: '2320'
  sic_description: Men's & Boys' Furnishgs, Work Clothg, & Allied Garments
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001037038.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/c6b3af0cefe967faceb0323aa590d422e87cbc29/brain/companies/RL/README.md
full_history_commit: c6b3af0cefe967faceb0323aa590d422e87cbc29
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# RL — RALPH LAUREN CORP

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/c6b3af0cefe967faceb0323aa590d422e87cbc29/brain/companies/RL/README.md)

## Business overview

Reported issuer name: **RALPH LAUREN CORP**. Stable SEC CIK: **0001037038**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| RL | NYSE | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **2320**: Men's & Boys' Furnishgs, Work Clothg, & Allied Garments. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **consumer-discretionary**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

## Financial performance

Derived observation: Operating margin was 14.53% for 2025-03-30 to 2026-03-28 (US GAAP inputs). [S04]
Formula: `operating_income / revenue * 100`. Inputs: operating_income=1179200000 USD (OperatingIncomeLoss), revenue=8114500000 USD (Revenues).

Derived observation: Net margin was 11.60% for 2025-03-30 to 2026-03-28 (US GAAP inputs). [S04]
Formula: `net_income / revenue * 100`. Inputs: net_income=941100000 USD (NetIncomeLoss), revenue=8114500000 USD (Revenues).

Derived observation: Stock compensation / revenue was 1.37% for 2025-03-30 to 2026-03-28 (US GAAP inputs). [S04]
Formula: `stock_based_compensation / revenue * 100`. Inputs: stock_based_compensation=111000000 USD (ShareBasedCompensation), revenue=8114500000 USD (Revenues).

Derived observation: Annual revenue changed +14.63% from the year ended 2025-03-29 to 2026-03-28. [S04]
Formula: `(current / prior - 1) * 100`. Inputs: revenue=8114500000 USD (Revenues), revenue=7079000000 USD (Revenues).

Derived observation: Annual operating income changed +26.51% from the year ended 2025-03-29 to 2026-03-28. [S04]
Formula: `(current / prior - 1) * 100`. Inputs: operating_income=1179200000 USD (OperatingIncomeLoss), operating_income=932100000 USD (OperatingIncomeLoss).

Derived observation: Annual net income changed +26.68% from the year ended 2025-03-29 to 2026-03-28. [S04]
Formula: `(current / prior - 1) * 100`. Inputs: net_income=941100000 USD (NetIncomeLoss), net_income=742900000 USD (NetIncomeLoss).

Derived observation: Annual operating cash flow changed -6.55% from the year ended 2025-03-29 to 2026-03-28. [S04]
Formula: `(current / prior - 1) * 100`. Inputs: operating_cash_flow=1154200000 USD (NetCashProvidedByUsedInOperatingActivities), operating_cash_flow=1235100000 USD (NetCashProvidedByUsedInOperatingActivities).

Derived observation: Operating cash flow / net income was 1.23x for the year ended 2026-03-28. Working capital and non-cash adjustments require separate filing analysis. [S04]
Formula: `operating_cash_flow / net_income`. Inputs: operating_cash_flow=1154200000 USD (NetCashProvidedByUsedInOperatingActivities), net_income=941100000 USD (NetIncomeLoss).

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:53:02.398600+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-03-30 to 2026-03-28

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| cost_of_revenue | 2,445,300,000 | USD | US GAAP / reported | CostOfRevenue | [S04] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S04] |
| free_cash_flow | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| gross_profit | 5,669,200,000 | USD | US GAAP / reported | GrossProfit | [S04] |
| net_income | 941,100,000 | USD | US GAAP / reported | NetIncomeLoss | [S04] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income_including_noncontrolling_interests | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| operating_cash_flow | 1,154,200,000 | USD | US GAAP / reported | NetCashProvidedByUsedInOperatingActivities | [S04] |
| operating_income | 1,179,200,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S04] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | 8,114,500,000 | USD | US GAAP / reported | Revenues | [S04] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S04] |
| stock_based_compensation | 111,000,000 | USD | US GAAP / reported | ShareBasedCompensation | [S04] |


### quarterly: 2026-03-29 to 2026-06-27

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| cost_of_revenue | 515,600,000 | USD | US GAAP / reported | CostOfRevenue | [S05] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S05] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S05] |
| free_cash_flow | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| gross_profit | 1,444,200,000 | USD | US GAAP / reported | GrossProfit | [S05] |
| net_income | 262,200,000 | USD | US GAAP / reported | NetIncomeLoss | [S05] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income_including_noncontrolling_interests | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| operating_cash_flow | 339,300,000 | USD | US GAAP / reported | NetCashProvidedByUsedInOperatingActivities | [S05] |
| operating_income | 342,400,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S05] |
| purchases_of_productive_assets | -53,400,000 | USD | US GAAP / reported | PaymentsToAcquireProductiveAssets; Cash outflow = negative of reported PaymentsToAcquireProductiveAssets; source value retained.; broader_than_property_plant_equipment_only | [S05] |
| revenue | 1,959,800,000 | USD | US GAAP / reported | Revenues | [S05] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S05] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S05] |
| stock_based_compensation | 26,000,000 | USD | US GAAP / reported | ShareBasedCompensation | [S05] |



## Balance sheet and capital allocation

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:53:02.398600+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-03-30 to 2026-03-28

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 1,988,000,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S05] |
| debt_current | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtCurrent; debt_scope_requires_filing_review | [S04] |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtNoncurrent; debt_scope_requires_filing_review | [S05] |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | 77,000,000 | USD | US GAAP / reported | ShortTermInvestments | [S05] |


### quarterly: 2026-03-29 to 2026-06-27

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 1,719,000,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S05] |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtNoncurrent; debt_scope_requires_filing_review | [S05] |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | 222,600,000 | USD | US GAAP / reported | ShortTermInvestments | [S05] |



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
- Collector status: quality_review_required; last action: new_financial_filing; last checked: 2026-10-24T13:31:02.098976+00:00.

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

Calculation gaps: Free cash flow margin: compatible positive revenue and usable inputs are required. free_cash_flow: annual growth withheld because periods, definitions or a positive prior denominator are not verified.

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest five available filing metadata records; document bodies have not been analyzed here.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-10-14 | 4 | 0000950142-26-002766 | — | [S17] |
| 2026-10-14 | 4 | 0000950142-26-002765 | — | [S18] |
| 2026-10-14 | 4 | 0000950142-26-002764 | — | [S19] |
| 2026-10-14 | 4 | 0000950142-26-002763 | — | [S20] |
| 2026-10-14 | 4 | 0000950142-26-002762 | — | [S21] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-25T13:45:48.334682+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001037038.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [SEC CompanyFacts source](https://data.sec.gov/api/xbrl/companyfacts/CIK0001037038.json) — published not supplied; retrieved 2026-10-22T17:53:02.398600+00:00.

[S04] [10-K 0001628280-26-037074](https://www.sec.gov/Archives/edgar/data/1037038/000162828026037074/0001628280-26-037074-index.html) — published 2026-05-21; retrieved 2026-10-22T17:53:02.398600+00:00.

[S05] [10-Q 0001628280-26-053992](https://www.sec.gov/Archives/edgar/data/1037038/000162828026053992/0001628280-26-053992-index.html) — published 2026-08-06; retrieved 2026-10-22T17:53:02.398600+00:00.

[S17] [4 0000950142-26-002766](https://www.sec.gov/Archives/edgar/data/1037038/000095014226002766/0000950142-26-002766-index.html) — published 2026-10-14; retrieved 2026-10-23T08:33:02.691743+00:00.

[S18] [4 0000950142-26-002765](https://www.sec.gov/Archives/edgar/data/1037038/000095014226002765/0000950142-26-002765-index.html) — published 2026-10-14; retrieved 2026-10-23T08:33:02.691743+00:00.

[S19] [4 0000950142-26-002764](https://www.sec.gov/Archives/edgar/data/1037038/000095014226002764/0000950142-26-002764-index.html) — published 2026-10-14; retrieved 2026-10-23T08:33:02.691743+00:00.

[S20] [4 0000950142-26-002763](https://www.sec.gov/Archives/edgar/data/1037038/000095014226002763/0000950142-26-002763-index.html) — published 2026-10-14; retrieved 2026-10-23T08:33:02.691743+00:00.

[S21] [4 0000950142-26-002762](https://www.sec.gov/Archives/edgar/data/1037038/000095014226002762/0000950142-26-002762-index.html) — published 2026-10-14; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261025-40199010718-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/c6b3af0cefe967faceb0323aa590d422e87cbc29/brain/companies/RL/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
