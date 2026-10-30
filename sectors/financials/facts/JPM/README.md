---
schema_version: 1
document_type: company_facts
company_id: company-cik-0000019617
cik: 0000019617
company_name: JPMORGAN CHASE & CO
tickers:
- JPM
- JPM$C
- JPM$D
- JPM$J
- JPM$K
- JPM$L
- JPM$M
status: stub
canonical_reviewed: false
as_of: '2026-10-30'
updated_at: '2026-10-30T16:05:25.650854+00:00'
reviewed_at: null
coverage_release: coverage-20261030-41085569265-1
source_commit: ef2ed016c2c344c23ee7fb991b25bf93660da77e
financial_history_available: true
curated_research: null
financial_gap:
  reason: available
  next_action: Retain dated financial evidence and review blocked metrics before analytical
    use.
  observed_forms:
  - '4'
  - 424B2
  - 424B3
  - 8-K
  - FWP
  - SCHEDULE 13G
  - SCHEDULE 13G/A
input_sources:
  history:
    url: https://data.sec.gov/api/xbrl/companyfacts/CIK0000019617.json
    sha256: c12d739195e280fb76969bb1d74e295cf2fa397cd40ff05ac0dc095b7c0d6d71
    retrieved_at: '2026-10-24T13:22:57.445127+00:00'
    archive:
      member: CIK0000019617.json
      sha256: 6a571557530102bb009e07bf4f2d86d9aa6021247bfde97f696dd22cb1a4a7e7
      url: https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip
    acquisition: operator_supplied_sec_bulk_archive
  submissions:
    url: https://data.sec.gov/submissions/CIK0000019617.json
    sha256: 8b1661213725b397a9af65e9690f69dd8970015871f8995d9089922e09d2379c
    retrieved_at: '2026-10-24T13:22:51.759433+00:00'
    archive: &id001
      member: CIK0000019617.json
      sha256: 593fbbea6512ef5ec729a5e513c465fbedaac8a66602c0abe00d0ba5a4d18732
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: otherlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt
  published_at: null
  retrieved_at: '2026-10-30T16:00:12.358089+00:00'
  sha256: a960a0bfc5439fac9e467fe07ef1f44afe893ba2afc3297648321a80ce09971e
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0000019617.json
  published_at: null
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 8b1661213725b397a9af65e9690f69dd8970015871f8995d9089922e09d2379c
- id: S03
  title: SEC CompanyFacts source
  url: https://data.sec.gov/api/xbrl/companyfacts/CIK0000019617.json
  published_at: null
  retrieved_at: '2026-10-24T13:22:57.445127+00:00'
  sha256: c12d739195e280fb76969bb1d74e295cf2fa397cd40ff05ac0dc095b7c0d6d71
- id: S04
  title: 10-K 0001628280-26-008131
  url: https://www.sec.gov/Archives/edgar/data/19617/000162828026008131/0001628280-26-008131-index.html
  published_at: '2026-02-13'
  retrieved_at: '2026-10-24T13:22:57.445127+00:00'
  sha256: null
- id: S05
  title: 10-Q 0001628280-26-054343
  url: https://www.sec.gov/Archives/edgar/data/19617/000162828026054343/0001628280-26-054343-index.html
  published_at: '2026-08-06'
  retrieved_at: '2026-10-24T13:22:57.445127+00:00'
  sha256: null
- id: S09
  title: 10-Q 0001628280-26-029344
  url: https://www.sec.gov/Archives/edgar/data/19617/000162828026029344/0001628280-26-029344-index.html
  published_at: '2026-05-01'
  retrieved_at: '2026-10-24T13:22:57.445127+00:00'
  sha256: null
- id: S17
  title: 424B2 0001918704-26-032504
  url: https://www.sec.gov/Archives/edgar/data/19617/000191870426032504/0001918704-26-032504-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S18
  title: 424B2 0001918704-26-032495
  url: https://www.sec.gov/Archives/edgar/data/19617/000191870426032495/0001918704-26-032495-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S19
  title: FWP 0001918704-26-032485
  url: https://www.sec.gov/Archives/edgar/data/19617/000191870426032485/0001918704-26-032485-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S20
  title: 424B2 0001918704-26-032470
  url: https://www.sec.gov/Archives/edgar/data/19617/000191870426032470/0001918704-26-032470-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S21
  title: 424B2 0001918704-26-032465
  url: https://www.sec.gov/Archives/edgar/data/19617/000191870426032465/0001918704-26-032465-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
issuer_classification:
  cik: 0000019617
  classification_status: reported_sic
  entity_type: operating
  name: JPMORGAN CHASE & CO
  sic: '6021'
  sic_description: National Commercial Banks
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 8b1661213725b397a9af65e9690f69dd8970015871f8995d9089922e09d2379c
  url: https://data.sec.gov/submissions/CIK0000019617.json
listings:
- ticker: JPM
  exchange: NYSE
  instrument_type: common_stock
- ticker: JPM$C
  exchange: NYSE
  instrument_type: preferred
- ticker: JPM$D
  exchange: NYSE
  instrument_type: preferred
- ticker: JPM$J
  exchange: NYSE
  instrument_type: preferred
- ticker: JPM$K
  exchange: NYSE
  instrument_type: preferred
- ticker: JPM$L
  exchange: NYSE
  instrument_type: preferred
- ticker: JPM$M
  exchange: NYSE
  instrument_type: preferred
research_filings:
- accession: 0001628280-26-008131
  filed: '2026-02-13'
  form: 10-K
  period_end: '2025-12-31'
  url: https://www.sec.gov/Archives/edgar/data/19617/000162828026008131/0001628280-26-008131-index.html
- accession: 0001628280-26-054343
  filed: '2026-08-06'
  form: 10-Q
  period_end: '2026-06-30'
  url: https://www.sec.gov/Archives/edgar/data/19617/000162828026054343/0001628280-26-054343-index.html
- accession: 0001193125-26-426704
  filed: '2026-10-20'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/19617/000119312526426704/0001193125-26-426704-index.html
research_progress:
  stage: pending
  input_sha256: cba96ea53644f51288a7935915626cce8631673ebec5731c05845b19f621d07e
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
  derived_observations: 5
  model_draft: false
  reviewed: false
sector_assignment:
  sector: financials
  method: project_sic_rule
  sic: '6021'
  sic_description: National Commercial Banks
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0000019617.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/79888139fa1fe8ad3404e6bc04e318eee1474f73/brain/companies/JPM/README.md
full_history_commit: 79888139fa1fe8ad3404e6bc04e318eee1474f73
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# JPM, JPM$C, JPM$D, JPM$J, JPM$K, JPM$L, JPM$M — JPMORGAN CHASE & CO

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/79888139fa1fe8ad3404e6bc04e318eee1474f73/brain/companies/JPM/README.md)

## Business overview

Reported issuer name: **JPMORGAN CHASE & CO**. Stable SEC CIK: **0000019617**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| JPM | NYSE | common_stock | 1 | [S01] |
| JPM$C | NYSE | preferred | 1 | [S01] |
| JPM$D | NYSE | preferred | 1 | [S01] |
| JPM$J | NYSE | preferred | 1 | [S01] |
| JPM$K | NYSE | preferred | 1 | [S01] |
| JPM$L | NYSE | preferred | 1 | [S01] |
| JPM$M | NYSE | preferred | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **6021**: National Commercial Banks. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **financials**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

## Financial performance

Derived observation: Net margin was 31.27% for 2025-01-01 to 2025-12-31 (US GAAP inputs). [S04]
Formula: `net_income / revenue * 100`. Inputs: net_income=57048000000 USD (NetIncomeLoss), revenue=182447000000 USD (Revenues).

Derived observation: Stock compensation / revenue was 1.98% for 2025-01-01 to 2025-12-31 (US GAAP inputs). [S04]
Formula: `stock_based_compensation / revenue * 100`. Inputs: stock_based_compensation=3614000000 USD (ShareBasedCompensation), revenue=182447000000 USD (Revenues).

Derived observation: Annual revenue changed +2.75% from the year ended 2024-12-31 to 2025-12-31. [S04]
Formula: `(current / prior - 1) * 100`. Inputs: revenue=182447000000 USD (Revenues), revenue=177556000000 USD (Revenues).

Derived observation: Annual net income changed -2.43% from the year ended 2024-12-31 to 2025-12-31. [S04]
Formula: `(current / prior - 1) * 100`. Inputs: net_income=57048000000 USD (NetIncomeLoss), net_income=58471000000 USD (NetIncomeLoss).

Derived observation: Operating cash flow / net income was -2.59x for the year ended 2025-12-31. Working capital and non-cash adjustments require separate filing analysis. [S04]
Formula: `operating_cash_flow / net_income`. Inputs: operating_cash_flow=-147782000000 USD (NetCashProvidedByUsedInOperatingActivities), net_income=57048000000 USD (NetIncomeLoss).

Evidence cutoff: 2026-10-24. Source retrieved: 2026-10-24T13:22:57.445127+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-01-01 to 2025-12-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S04] |
| free_cash_flow | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| gross_profit | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income | 57,048,000,000 | USD | US GAAP / reported | NetIncomeLoss | [S04] |
| net_income_common | 55,681,000,000 | USD | US GAAP / reported | NetIncomeLossAvailableToCommonStockholdersBasic | [S04] |
| net_income_including_noncontrolling_interests | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| operating_cash_flow | -147,782,000,000 | USD | US GAAP / reported | NetCashProvidedByUsedInOperatingActivities | [S04] |
| operating_income | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | 182,447,000,000 | USD | US GAAP / reported | Revenues | [S04] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S04] |
| stock_based_compensation | 3,614,000,000 | USD | US GAAP / reported | ShareBasedCompensation | [S04] |


### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S05] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S05] |
| free_cash_flow | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| gross_profit | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income | 21,155,000,000 | USD | US GAAP / reported | NetIncomeLoss | [S05] |
| net_income_common | 20,752,000,000 | USD | US GAAP / reported | NetIncomeLossAvailableToCommonStockholdersBasic | [S05] |
| net_income_including_noncontrolling_interests | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| operating_cash_flow | -25,283,000,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S05] [S09] |
| operating_income | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S05] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S05] |
| stock_based_compensation | 1,167,000,000 | USD | US GAAP / reported | ShareBasedCompensation | [S05] |



## Balance sheet and capital allocation

Evidence cutoff: 2026-10-24. Source retrieved: 2026-10-24T13:22:57.445127+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-01-01 to 2025-12-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_total | Unavailable / blocked | USD | US GAAP / derived / not model usable | LongTermDebtAndCapitalLeaseObligationsIncludingCurrentMaturities + ShortTermBorrowings; debt_scope_requires_filing_review, derived_input_requires_review | [S05] |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtAndCapitalLeaseObligationsIncludingCurrentMaturities; debt_scope_requires_filing_review | [S05] |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S04] |
| short_term_borrowings | 64,776,000,000 | USD | US GAAP / reported | ShortTermBorrowings | [S05] |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |


### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_total | Unavailable / blocked | USD | US GAAP / derived / not model usable | LongTermDebtAndCapitalLeaseObligationsIncludingCurrentMaturities + ShortTermBorrowings; debt_scope_requires_filing_review, derived_input_requires_review | [S05] |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtAndCapitalLeaseObligationsIncludingCurrentMaturities; debt_scope_requires_filing_review | [S05] |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_borrowings | 72,430,000,000 | USD | US GAAP / reported | ShortTermBorrowings | [S05] |
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
- Collector status: quality_review_required; last action: new_financial_filing; last checked: 2026-10-24T13:27:19.764903+00:00.

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

Calculation gaps: Operating margin: compatible positive revenue and usable inputs are required. Free cash flow margin: compatible positive revenue and usable inputs are required. operating_income: annual growth withheld because periods, definitions or a positive prior denominator are not verified. operating_cash_flow: annual growth withheld because periods, definitions or a positive prior denominator are not verified. free_cash_flow: annual growth withheld because periods, definitions or a positive prior denominator are not verified.

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest five available filing metadata records; document bodies have not been analyzed here.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-10-23 | 424B2 | 0001918704-26-032504 | — | [S17] |
| 2026-10-23 | 424B2 | 0001918704-26-032495 | — | [S18] |
| 2026-10-23 | FWP | 0001918704-26-032485 | — | [S19] |
| 2026-10-23 | 424B2 | 0001918704-26-032470 | — | [S20] |
| 2026-10-23 | 424B2 | 0001918704-26-032465 | — | [S21] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-30T16:00:12.358089+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0000019617.json) — published not supplied; retrieved 2026-10-24T13:22:51.759433+00:00.

[S03] [SEC CompanyFacts source](https://data.sec.gov/api/xbrl/companyfacts/CIK0000019617.json) — published not supplied; retrieved 2026-10-24T13:22:57.445127+00:00.

[S04] [10-K 0001628280-26-008131](https://www.sec.gov/Archives/edgar/data/19617/000162828026008131/0001628280-26-008131-index.html) — published 2026-02-13; retrieved 2026-10-24T13:22:57.445127+00:00.

[S05] [10-Q 0001628280-26-054343](https://www.sec.gov/Archives/edgar/data/19617/000162828026054343/0001628280-26-054343-index.html) — published 2026-08-06; retrieved 2026-10-24T13:22:57.445127+00:00.

[S09] [10-Q 0001628280-26-029344](https://www.sec.gov/Archives/edgar/data/19617/000162828026029344/0001628280-26-029344-index.html) — published 2026-05-01; retrieved 2026-10-24T13:22:57.445127+00:00.

[S17] [424B2 0001918704-26-032504](https://www.sec.gov/Archives/edgar/data/19617/000191870426032504/0001918704-26-032504-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S18] [424B2 0001918704-26-032495](https://www.sec.gov/Archives/edgar/data/19617/000191870426032495/0001918704-26-032495-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S19] [FWP 0001918704-26-032485](https://www.sec.gov/Archives/edgar/data/19617/000191870426032485/0001918704-26-032485-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S20] [424B2 0001918704-26-032470](https://www.sec.gov/Archives/edgar/data/19617/000191870426032470/0001918704-26-032470-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S21] [424B2 0001918704-26-032465](https://www.sec.gov/Archives/edgar/data/19617/000191870426032465/0001918704-26-032465-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

Source release: `coverage-20261030-41085569265-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/79888139fa1fe8ad3404e6bc04e318eee1474f73/brain/companies/JPM/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
