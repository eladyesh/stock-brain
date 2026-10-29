---
schema_version: 1
document_type: company_facts
company_id: company-cik-0000922621
cik: 0000922621
company_name: ERIE INDEMNITY CO
tickers:
- ERIE
status: stub
canonical_reviewed: false
as_of: '2026-10-29'
updated_at: '2026-10-29T16:18:46.634043+00:00'
reviewed_at: null
coverage_release: coverage-20261029-40909364006-1
source_commit: 066173dd7c0933a11c2085b144bbb14099b44560
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
  - CORRESP
  - DEF 14C
  - S-8
  - S-8 POS
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  history:
    url: https://data.sec.gov/api/xbrl/companyfacts/CIK0000922621.json
    sha256: 8dbc3ed84f9df02fb620289fade7db754c10c9d036bfceec1f1304b3753c977b
    retrieved_at: '2026-10-22T17:53:02.398600+00:00'
    archive:
      member: CIK0000922621.json
      sha256: 7457a528288f1e3425cba6ffd7370c6c205845aba12761763aa5ae3683c0fdc2
      url: https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip
    acquisition: operator_supplied_sec_bulk_archive
  submissions:
    url: https://data.sec.gov/submissions/CIK0000922621.json
    sha256: ae58639170be889339fc5741f19411dd97748a947aa5bc6c24650f433172cf94
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0000922621.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: nasdaqlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt
  published_at: null
  retrieved_at: '2026-10-29T16:14:13.115716+00:00'
  sha256: 0695ffec283534755d4efe90771a9cacee840d7affb7ba717f62899195a301c6
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0000922621.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: ae58639170be889339fc5741f19411dd97748a947aa5bc6c24650f433172cf94
- id: S03
  title: SEC CompanyFacts source
  url: https://data.sec.gov/api/xbrl/companyfacts/CIK0000922621.json
  published_at: null
  retrieved_at: '2026-10-22T17:53:02.398600+00:00'
  sha256: 8dbc3ed84f9df02fb620289fade7db754c10c9d036bfceec1f1304b3753c977b
- id: S04
  title: 10-K 0001628280-26-010666
  url: https://www.sec.gov/Archives/edgar/data/922621/000162828026010666/0001628280-26-010666-index.html
  published_at: '2026-02-23'
  retrieved_at: '2026-10-22T17:53:02.398600+00:00'
  sha256: null
- id: S09
  title: 10-Q 0001628280-26-051079
  url: https://www.sec.gov/Archives/edgar/data/922621/000162828026051079/0001628280-26-051079-index.html
  published_at: '2026-07-30'
  retrieved_at: '2026-10-22T17:53:02.398600+00:00'
  sha256: null
- id: S10
  title: 10-Q 0001628280-26-026866
  url: https://www.sec.gov/Archives/edgar/data/922621/000162828026026866/0001628280-26-026866-index.html
  published_at: '2026-04-23'
  retrieved_at: '2026-10-22T17:53:02.398600+00:00'
  sha256: null
- id: S16
  title: 4 0001628280-26-066810
  url: https://www.sec.gov/Archives/edgar/data/922621/000162828026066810/0001628280-26-066810-index.html
  published_at: '2026-10-22'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S17
  title: 4 0001628280-26-066809
  url: https://www.sec.gov/Archives/edgar/data/922621/000162828026066809/0001628280-26-066809-index.html
  published_at: '2026-10-22'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S18
  title: 4 0001628280-26-066808
  url: https://www.sec.gov/Archives/edgar/data/922621/000162828026066808/0001628280-26-066808-index.html
  published_at: '2026-10-22'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S19
  title: 4 0001628280-26-066806
  url: https://www.sec.gov/Archives/edgar/data/922621/000162828026066806/0001628280-26-066806-index.html
  published_at: '2026-10-22'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S20
  title: 4 0001628280-26-066805
  url: https://www.sec.gov/Archives/edgar/data/922621/000162828026066805/0001628280-26-066805-index.html
  published_at: '2026-10-22'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0000922621
  classification_status: reported_sic
  entity_type: operating
  name: ERIE INDEMNITY CO
  sic: '6411'
  sic_description: Insurance Agents, Brokers & Service
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: ae58639170be889339fc5741f19411dd97748a947aa5bc6c24650f433172cf94
  url: https://data.sec.gov/submissions/CIK0000922621.json
listings:
- ticker: ERIE
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001628280-26-010666
  filed: '2026-02-23'
  form: 10-K
  period_end: '2025-12-31'
  url: https://www.sec.gov/Archives/edgar/data/922621/000162828026010666/0001628280-26-010666-index.html
- accession: 0001628280-26-051079
  filed: '2026-07-30'
  form: 10-Q
  period_end: '2026-06-30'
  url: https://www.sec.gov/Archives/edgar/data/922621/000162828026051079/0001628280-26-051079-index.html
- accession: 0001628280-26-051071
  filed: '2026-07-30'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/922621/000162828026051071/0001628280-26-051071-index.html
- accession: 0000922621-24-000014
  filed: '2024-05-07'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/922621/000092262124000014/0000922621-24-000014-index.html
- accession: 0000922621-23-000015
  filed: '2023-07-27'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/922621/000092262123000015/0000922621-23-000015-index.html
research_progress:
  stage: pending
  input_sha256: cdada5d3c31cf6a94add5011f1228a714aebf69d6ca38c34d8fadd0b4dac4320
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
  sic: '6411'
  sic_description: Insurance Agents, Brokers & Service
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0000922621.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/52b6569b626a07b359d4a15742ebb633a0e48007/brain/companies/ERIE/README.md
full_history_commit: 52b6569b626a07b359d4a15742ebb633a0e48007
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# ERIE — ERIE INDEMNITY CO

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/52b6569b626a07b359d4a15742ebb633a0e48007/brain/companies/ERIE/README.md)

## Business overview

Reported issuer name: **ERIE INDEMNITY CO**. Stable SEC CIK: **0000922621**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| ERIE | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **6411**: Insurance Agents, Brokers & Service. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **financials**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

## Financial performance

Derived observation: Operating margin was 17.63% for 2025-01-01 to 2025-12-31 (US GAAP inputs). [S04]
Formula: `operating_income / revenue * 100`. Inputs: operating_income=717184000 USD (OperatingIncomeLoss), revenue=4067258000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Net margin was 13.75% for 2025-01-01 to 2025-12-31 (US GAAP inputs). [S04]
Formula: `net_income / revenue * 100`. Inputs: net_income=559335000 USD (NetIncomeLoss), revenue=4067258000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Annual revenue changed +7.17% from the year ended 2024-12-31 to 2025-12-31. [S04]
Formula: `(current / prior - 1) * 100`. Inputs: revenue=4067258000 USD (RevenueFromContractWithCustomerExcludingAssessedTax), revenue=3795115000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Annual operating income changed +6.02% from the year ended 2024-12-31 to 2025-12-31. [S04]
Formula: `(current / prior - 1) * 100`. Inputs: operating_income=717184000 USD (OperatingIncomeLoss), operating_income=676455000 USD (OperatingIncomeLoss).

Derived observation: Annual net income changed -6.83% from the year ended 2024-12-31 to 2025-12-31. [S04]
Formula: `(current / prior - 1) * 100`. Inputs: net_income=559335000 USD (NetIncomeLoss), net_income=600314000 USD (NetIncomeLoss).

Derived observation: Annual operating cash flow changed +12.34% from the year ended 2024-12-31 to 2025-12-31. [S04]
Formula: `(current / prior - 1) * 100`. Inputs: operating_cash_flow=686657000 USD (NetCashProvidedByUsedInOperatingActivities), operating_cash_flow=611249000 USD (NetCashProvidedByUsedInOperatingActivities).

Derived observation: Operating cash flow / net income was 1.23x for the year ended 2025-12-31. Working capital and non-cash adjustments require separate filing analysis. [S04]
Formula: `operating_cash_flow / net_income`. Inputs: operating_cash_flow=686657000 USD (NetCashProvidedByUsedInOperatingActivities), net_income=559335000 USD (NetIncomeLoss).

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:53:02.398600+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-01-01 to 2025-12-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| free_cash_flow | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| gross_profit | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income | 559,335,000 | USD | US GAAP / reported | NetIncomeLoss | [S04] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income_including_noncontrolling_interests | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| operating_cash_flow | 686,657,000 | USD | US GAAP / reported | NetCashProvidedByUsedInOperatingActivities | [S04] |
| operating_income | 717,184,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S04] |
| purchases_of_productive_assets | -115,692,000 | USD | US GAAP / reported | PaymentsToAcquireProductiveAssets; Cash outflow = negative of reported PaymentsToAcquireProductiveAssets; source value retained.; broader_than_property_plant_equipment_only | [S04] |
| revenue | 4,067,258,000 | USD | US GAAP / reported | RevenueFromContractWithCustomerExcludingAssessedTax | [S04] |
| shares_basic | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_diluted | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| stock_based_compensation | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |


### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| free_cash_flow | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| gross_profit | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income | 180,294,000 | USD | US GAAP / reported | NetIncomeLoss | [S09] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income_including_noncontrolling_interests | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| operating_cash_flow | 214,922,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S09] [S10] |
| operating_income | 204,123,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S09] |
| purchases_of_productive_assets | -41,519,000 | USD | US GAAP / derived | PaymentsToAcquireProductiveAssets; broader_than_property_plant_equipment_only, cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S09] [S10] |
| revenue | 1,089,796,000 | USD | US GAAP / reported | RevenueFromContractWithCustomerExcludingAssessedTax | [S09] |
| shares_basic | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_diluted | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| stock_based_compensation | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |



## Balance sheet and capital allocation

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:53:02.398600+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-01-01 to 2025-12-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |


### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
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
- Collector status: quality_review_required; last action: new_financial_filing; last checked: 2026-10-24T13:30:29.238557+00:00.

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

Calculation gaps: Free cash flow margin: compatible positive revenue and usable inputs are required. Stock compensation / revenue: compatible positive revenue and usable inputs are required. free_cash_flow: annual growth withheld because periods, definitions or a positive prior denominator are not verified.

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest five available filing metadata records; document bodies have not been analyzed here.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-10-22 | 4 | 0001628280-26-066810 | — | [S16] |
| 2026-10-22 | 4 | 0001628280-26-066809 | — | [S17] |
| 2026-10-22 | 4 | 0001628280-26-066808 | — | [S18] |
| 2026-10-22 | 4 | 0001628280-26-066806 | — | [S19] |
| 2026-10-22 | 4 | 0001628280-26-066805 | — | [S20] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-29T16:14:13.115716+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0000922621.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [SEC CompanyFacts source](https://data.sec.gov/api/xbrl/companyfacts/CIK0000922621.json) — published not supplied; retrieved 2026-10-22T17:53:02.398600+00:00.

[S04] [10-K 0001628280-26-010666](https://www.sec.gov/Archives/edgar/data/922621/000162828026010666/0001628280-26-010666-index.html) — published 2026-02-23; retrieved 2026-10-22T17:53:02.398600+00:00.

[S09] [10-Q 0001628280-26-051079](https://www.sec.gov/Archives/edgar/data/922621/000162828026051079/0001628280-26-051079-index.html) — published 2026-07-30; retrieved 2026-10-22T17:53:02.398600+00:00.

[S10] [10-Q 0001628280-26-026866](https://www.sec.gov/Archives/edgar/data/922621/000162828026026866/0001628280-26-026866-index.html) — published 2026-04-23; retrieved 2026-10-22T17:53:02.398600+00:00.

[S16] [4 0001628280-26-066810](https://www.sec.gov/Archives/edgar/data/922621/000162828026066810/0001628280-26-066810-index.html) — published 2026-10-22; retrieved 2026-10-23T08:33:02.691743+00:00.

[S17] [4 0001628280-26-066809](https://www.sec.gov/Archives/edgar/data/922621/000162828026066809/0001628280-26-066809-index.html) — published 2026-10-22; retrieved 2026-10-23T08:33:02.691743+00:00.

[S18] [4 0001628280-26-066808](https://www.sec.gov/Archives/edgar/data/922621/000162828026066808/0001628280-26-066808-index.html) — published 2026-10-22; retrieved 2026-10-23T08:33:02.691743+00:00.

[S19] [4 0001628280-26-066806](https://www.sec.gov/Archives/edgar/data/922621/000162828026066806/0001628280-26-066806-index.html) — published 2026-10-22; retrieved 2026-10-23T08:33:02.691743+00:00.

[S20] [4 0001628280-26-066805](https://www.sec.gov/Archives/edgar/data/922621/000162828026066805/0001628280-26-066805-index.html) — published 2026-10-22; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261029-40909364006-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/52b6569b626a07b359d4a15742ebb633a0e48007/brain/companies/ERIE/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
