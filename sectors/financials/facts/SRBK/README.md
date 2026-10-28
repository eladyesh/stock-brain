---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001951276
cik: 0001951276
company_name: SR Bancorp, Inc.
tickers:
- SRBK
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
  - 11-K
  - '3'
  - '4'
  - 4/A
  - 424B3
  - 8-A12B
  - 8-K
  - 8-K/A
  - ARS
  - CERT
  - CORRESP
  - DEF 14A
  - DRS
  - EFFECT
  - NT 10-K
  - NT 10-Q
  - NT 11-K
  - POS AM
  - S-1
  - S-1/A
  - S-8
  - SC 13G
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  history:
    url: https://data.sec.gov/api/xbrl/companyfacts/CIK0001951276.json
    sha256: 008bdbc55c4c9bd85aa726ea78949bc7f696e148ed7261219c414b58ab6524ea
    retrieved_at: '2026-10-22T18:10:35.452616+00:00'
    archive:
      member: CIK0001951276.json
      sha256: 7457a528288f1e3425cba6ffd7370c6c205845aba12761763aa5ae3683c0fdc2
      url: https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip
    acquisition: operator_supplied_sec_bulk_archive
  submissions:
    url: https://data.sec.gov/submissions/CIK0001951276.json
    sha256: 2f5c54f2af9d21ede728362540754d7641c83f443ce0933ae2d3f0d91d531ff0
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001951276.json
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
  url: https://data.sec.gov/submissions/CIK0001951276.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 2f5c54f2af9d21ede728362540754d7641c83f443ce0933ae2d3f0d91d531ff0
- id: S03
  title: SEC CompanyFacts source
  url: https://data.sec.gov/api/xbrl/companyfacts/CIK0001951276.json
  published_at: null
  retrieved_at: '2026-10-22T18:10:35.452616+00:00'
  sha256: 008bdbc55c4c9bd85aa726ea78949bc7f696e148ed7261219c414b58ab6524ea
- id: S04
  title: 10-K 0001437749-26-031222
  url: https://www.sec.gov/Archives/edgar/data/1951276/000143774926031222/0001437749-26-031222-index.html
  published_at: '2026-09-25'
  retrieved_at: '2026-10-22T18:10:35.452616+00:00'
  sha256: null
- id: S08
  title: 10-Q 0001437749-26-017364
  url: https://www.sec.gov/Archives/edgar/data/1951276/000143774926017364/0001437749-26-017364-index.html
  published_at: '2026-05-15'
  retrieved_at: '2026-10-22T18:10:35.452616+00:00'
  sha256: null
- id: S16
  title: ARS 0001193125-26-424759
  url: https://www.sec.gov/Archives/edgar/data/1951276/000119312526424759/0001193125-26-424759-index.html
  published_at: '2026-10-19'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S17
  title: DEF 14A 0001193125-26-424753
  url: https://www.sec.gov/Archives/edgar/data/1951276/000119312526424753/0001193125-26-424753-index.html
  published_at: '2026-10-19'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S18
  title: 10-K 0001437749-26-031222
  url: https://www.sec.gov/Archives/edgar/data/1951276/000143774926031222/0001437749-26-031222-index.html
  published_at: '2026-09-25'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S19
  title: 8-K 0000943374-26-000413
  url: https://www.sec.gov/Archives/edgar/data/1951276/000094337426000413/0000943374-26-000413-index.html
  published_at: '2026-09-17'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S20
  title: 4 0001437749-26-028128
  url: https://www.sec.gov/Archives/edgar/data/1951276/000143774926028128/0001437749-26-028128-index.html
  published_at: '2026-08-17'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0001951276
  classification_status: reported_sic
  entity_type: operating
  name: SR Bancorp, Inc.
  sic: '6036'
  sic_description: Savings Institutions, Not Federally Chartered
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 2f5c54f2af9d21ede728362540754d7641c83f443ce0933ae2d3f0d91d531ff0
  url: https://data.sec.gov/submissions/CIK0001951276.json
listings:
- ticker: SRBK
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001437749-26-031222
  filed: '2026-09-25'
  form: 10-K
  period_end: '2026-06-30'
  url: https://www.sec.gov/Archives/edgar/data/1951276/000143774926031222/0001437749-26-031222-index.html
- accession: 0001437749-26-017364
  filed: '2026-05-15'
  form: 10-Q
  period_end: '2026-03-31'
  url: https://www.sec.gov/Archives/edgar/data/1951276/000143774926017364/0001437749-26-017364-index.html
- accession: 0001193125-26-424753
  filed: '2026-10-19'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/1951276/000119312526424753/0001193125-26-424753-index.html
- accession: 0000943374-26-000413
  filed: '2026-09-17'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/1951276/000094337426000413/0000943374-26-000413-index.html
- accession: 0000950170-25-114518
  filed: '2025-09-12'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1951276/000095017025114518/0000950170-25-114518-index.html
research_progress:
  stage: pending
  input_sha256: 80669a0e0075bf65345aae9b84f87ccabc3a3ac9a8b18ce5f70ef55a26499c64
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
  derived_observations: 4
  model_draft: false
  reviewed: false
sector_assignment:
  sector: financials
  method: project_sic_rule
  sic: '6036'
  sic_description: Savings Institutions, Not Federally Chartered
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001951276.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/5da532c3abee5b40a5400c5864c6f3f4593276d7/brain/companies/SRBK/README.md
full_history_commit: 5da532c3abee5b40a5400c5864c6f3f4593276d7
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# SRBK — SR Bancorp, Inc.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/5da532c3abee5b40a5400c5864c6f3f4593276d7/brain/companies/SRBK/README.md)

## Business overview

Reported issuer name: **SR Bancorp, Inc.**. Stable SEC CIK: **0001951276**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| SRBK | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **6036**: Savings Institutions, Not Federally Chartered. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **financials**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

## Financial performance

Derived observation: Annual net income changed -34.72% from the year ended 2025-06-30 to 2026-06-30. [S18]
Formula: `(current / prior - 1) * 100`. Inputs: net_income=3353000 USD (NetIncomeLoss), net_income=5136000 USD (NetIncomeLoss).

Derived observation: Annual operating cash flow changed +129.43% from the year ended 2025-06-30 to 2026-06-30. [S18]
Formula: `(current / prior - 1) * 100`. Inputs: operating_cash_flow=10703000 USD (NetCashProvidedByUsedInOperatingActivities), operating_cash_flow=4665000 USD (NetCashProvidedByUsedInOperatingActivities).

Derived observation: Annual free cash flow changed +133.53% from the year ended 2025-06-30 to 2026-06-30. [S18]
Formula: `(current / prior - 1) * 100`. Inputs: free_cash_flow=9883000 USD (NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment), free_cash_flow=4232000 USD (NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment).

Derived observation: Operating cash flow / net income was 3.19x for the year ended 2026-06-30. Working capital and non-cash adjustments require separate filing analysis. [S18]
Formula: `operating_cash_flow / net_income`. Inputs: operating_cash_flow=10703000 USD (NetCashProvidedByUsedInOperatingActivities), net_income=3353000 USD (NetIncomeLoss).

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T18:10:35.452616+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-07-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -820,000 | USD | US GAAP / reported | PaymentsToAcquirePropertyPlantAndEquipment; Cash outflow = negative of reported PaymentsToAcquirePropertyPlantAndEquipment; source value retained. | [S04] |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S04] |
| free_cash_flow | 9,883,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment | [S04] |
| gross_profit | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income | 3,353,000 | USD | US GAAP / reported | NetIncomeLoss | [S04] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income_including_noncontrolling_interests | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| operating_cash_flow | 10,703,000 | USD | US GAAP / reported | NetCashProvidedByUsedInOperatingActivities | [S04] |
| operating_income | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S04] |
| stock_based_compensation | 2,139,000 | USD | US GAAP / reported | ShareBasedCompensation | [S04] |


### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -117,000 | USD | US GAAP / derived | PaymentsToAcquirePropertyPlantAndEquipment; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| free_cash_flow | 3,763,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| gross_profit | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income | 940,000 | USD | US GAAP / derived | NetIncomeLoss; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income_including_noncontrolling_interests | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| operating_cash_flow | 3,880,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| operating_income | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_basic | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_diluted | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| stock_based_compensation | 582,000 | USD | US GAAP / derived | ShareBasedCompensation; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |



## Balance sheet and capital allocation

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T18:10:35.452616+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-07-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 71,461,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S04] |
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
| cash_and_equivalents | 71,461,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S04] |
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
- Collector status: quality_review_required; last action: new_financial_filing; last checked: 2026-10-24T13:36:25.973666+00:00.

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

Calculation gaps: Operating margin: compatible positive revenue and usable inputs are required. Net margin: compatible positive revenue and usable inputs are required. Free cash flow margin: compatible positive revenue and usable inputs are required. Stock compensation / revenue: compatible positive revenue and usable inputs are required. revenue: annual growth withheld because periods, definitions or a positive prior denominator are not verified. operating_income: annual growth withheld because periods, definitions or a positive prior denominator are not verified.

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest five available filing metadata records; document bodies have not been analyzed here.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-10-19 | ARS | 0001193125-26-424759 | — | [S16] |
| 2026-10-19 | DEF 14A | 0001193125-26-424753 | — | [S17] |
| 2026-09-25 | 10-K | 0001437749-26-031222 | — | [S18] |
| 2026-09-17 | 8-K | 0000943374-26-000413 | — | [S19] |
| 2026-08-17 | 4 | 0001437749-26-028128 | — | [S20] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-28T16:09:01.738588+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001951276.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [SEC CompanyFacts source](https://data.sec.gov/api/xbrl/companyfacts/CIK0001951276.json) — published not supplied; retrieved 2026-10-22T18:10:35.452616+00:00.

[S04] [10-K 0001437749-26-031222](https://www.sec.gov/Archives/edgar/data/1951276/000143774926031222/0001437749-26-031222-index.html) — published 2026-09-25; retrieved 2026-10-22T18:10:35.452616+00:00.

[S08] [10-Q 0001437749-26-017364](https://www.sec.gov/Archives/edgar/data/1951276/000143774926017364/0001437749-26-017364-index.html) — published 2026-05-15; retrieved 2026-10-22T18:10:35.452616+00:00.

[S16] [ARS 0001193125-26-424759](https://www.sec.gov/Archives/edgar/data/1951276/000119312526424759/0001193125-26-424759-index.html) — published 2026-10-19; retrieved 2026-10-23T08:33:02.691743+00:00.

[S17] [DEF 14A 0001193125-26-424753](https://www.sec.gov/Archives/edgar/data/1951276/000119312526424753/0001193125-26-424753-index.html) — published 2026-10-19; retrieved 2026-10-23T08:33:02.691743+00:00.

[S18] [10-K 0001437749-26-031222](https://www.sec.gov/Archives/edgar/data/1951276/000143774926031222/0001437749-26-031222-index.html) — published 2026-09-25; retrieved 2026-10-23T08:33:02.691743+00:00.

[S19] [8-K 0000943374-26-000413](https://www.sec.gov/Archives/edgar/data/1951276/000094337426000413/0000943374-26-000413-index.html) — published 2026-09-17; retrieved 2026-10-23T08:33:02.691743+00:00.

[S20] [4 0001437749-26-028128](https://www.sec.gov/Archives/edgar/data/1951276/000143774926028128/0001437749-26-028128-index.html) — published 2026-08-17; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261028-40722802424-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/5da532c3abee5b40a5400c5864c6f3f4593276d7/brain/companies/SRBK/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
