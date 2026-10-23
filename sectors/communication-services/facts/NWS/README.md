---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001564708
cik: 0001564708
company_name: NEWS CORP
tickers:
- NWS
- NWSA
status: stub
canonical_reviewed: false
as_of: '2026-10-23'
updated_at: '2026-10-23T14:35:22.252685+00:00'
reviewed_at: null
coverage_release: coverage-20261023-39968262770-1
source_commit: 3f697433c3580d4ca83edbe44c66580ac926c8d7
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
  - 424B7
  - 8-K
  - ARS
  - CORRESP
  - CT ORDER
  - DEF 14A
  - DEFA14A
  - DEFC14A
  - DFAN14A
  - FWP
  - PRE 14A
  - PREC14A
  - S-3ASR
  - S-8 POS
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13D
  - SCHEDULE 13G
  - SCHEDULE 13G/A
input_sources:
  history:
    url: https://data.sec.gov/api/xbrl/companyfacts/CIK0001564708.json
    sha256: a93a5df01fd389bf264e65b6651d42b3e49e6549f68d79e6d37c7670e2dd4952
    retrieved_at: '2026-10-22T18:10:35.452616+00:00'
    archive:
      member: CIK0001564708.json
      sha256: 7457a528288f1e3425cba6ffd7370c6c205845aba12761763aa5ae3683c0fdc2
      url: https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip
    acquisition: operator_supplied_sec_bulk_archive
  submissions:
    url: https://data.sec.gov/submissions/CIK0001564708.json
    sha256: 9745e39b36566c1bba59da25581abc167bfc84737106bba3111133edfcb4a676
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001564708.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: nasdaqlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt
  published_at: null
  retrieved_at: '2026-10-23T14:17:54.530395+00:00'
  sha256: a31379ea4791bd232005b22547c9cfa517e0cb9e9f14ff7091be845f143d5c71
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001564708.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 9745e39b36566c1bba59da25581abc167bfc84737106bba3111133edfcb4a676
- id: S03
  title: SEC CompanyFacts source
  url: https://data.sec.gov/api/xbrl/companyfacts/CIK0001564708.json
  published_at: null
  retrieved_at: '2026-10-22T18:10:35.452616+00:00'
  sha256: a93a5df01fd389bf264e65b6651d42b3e49e6549f68d79e6d37c7670e2dd4952
- id: S04
  title: 10-K 0001564708-26-000175
  url: https://www.sec.gov/Archives/edgar/data/1564708/000156470826000175/0001564708-26-000175-index.html
  published_at: '2026-08-07'
  retrieved_at: '2026-10-22T18:10:35.452616+00:00'
  sha256: null
- id: S08
  title: 10-Q 0001564708-26-000103
  url: https://www.sec.gov/Archives/edgar/data/1564708/000156470826000103/0001564708-26-000103-index.html
  published_at: '2026-05-08'
  retrieved_at: '2026-10-22T18:10:35.452616+00:00'
  sha256: null
- id: S17
  title: 8-K 0001564708-26-000234
  url: https://www.sec.gov/Archives/edgar/data/1564708/000156470826000234/0001564708-26-000234-index.html
  published_at: '2026-10-22'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S18
  title: 8-K 0001564708-26-000233
  url: https://www.sec.gov/Archives/edgar/data/1564708/000156470826000233/0001564708-26-000233-index.html
  published_at: '2026-10-21'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S19
  title: 8-K 0001564708-26-000232
  url: https://www.sec.gov/Archives/edgar/data/1564708/000156470826000232/0001564708-26-000232-index.html
  published_at: '2026-10-20'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S20
  title: 8-K 0001564708-26-000231
  url: https://www.sec.gov/Archives/edgar/data/1564708/000156470826000231/0001564708-26-000231-index.html
  published_at: '2026-10-19'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S21
  title: 8-K 0001564708-26-000230
  url: https://www.sec.gov/Archives/edgar/data/1564708/000156470826000230/0001564708-26-000230-index.html
  published_at: '2026-10-16'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0001564708
  classification_status: reported_sic
  entity_type: operating
  name: NEWS CORP
  sic: '2711'
  sic_description: 'Newspapers: Publishing or  Publishing & Printing'
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 9745e39b36566c1bba59da25581abc167bfc84737106bba3111133edfcb4a676
  url: https://data.sec.gov/submissions/CIK0001564708.json
listings:
- ticker: NWS
  exchange: NASDAQ
  instrument_type: common_stock
- ticker: NWSA
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001564708-26-000175
  filed: '2026-08-07'
  form: 10-K
  period_end: '2026-06-30'
  url: https://www.sec.gov/Archives/edgar/data/1564708/000156470826000175/0001564708-26-000175-index.html
- accession: 0001564708-26-000103
  filed: '2026-05-08'
  form: 10-Q
  period_end: '2026-03-31'
  url: https://www.sec.gov/Archives/edgar/data/1564708/000156470826000103/0001564708-26-000103-index.html
- accession: 0001104659-26-109969
  filed: '2026-09-23'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/1564708/000110465926109969/0001104659-26-109969-index.html
- accession: 0001564708-26-000234
  filed: '2026-10-22'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/1564708/000156470826000234/0001564708-26-000234-index.html
research_progress:
  stage: pending
  input_sha256: 2ff49e14d108c37bd02c6380eb02b48f3a1502e0dc8d7cd7d95b4df77346a272
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
  derived_observations: 3
  model_draft: false
  reviewed: false
sector_assignment:
  sector: communication-services
  method: project_sic_rule
  sic: '2711'
  sic_description: 'Newspapers: Publishing or  Publishing & Printing'
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001564708.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/d523cff21b18141b9a37cddd98ad6af6e1a30fa5/brain/companies/NWS/README.md
full_history_commit: d523cff21b18141b9a37cddd98ad6af6e1a30fa5
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# NWS, NWSA — NEWS CORP

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/d523cff21b18141b9a37cddd98ad6af6e1a30fa5/brain/companies/NWS/README.md)

## Business overview

Reported issuer name: **NEWS CORP**. Stable SEC CIK: **0001564708**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| NWS | NASDAQ | common_stock | 1 | [S01] |
| NWSA | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **2711**: Newspapers: Publishing or  Publishing & Printing. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **communication-services**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

## Financial performance

Derived observation: Net margin was 6.35% for 2025-07-01 to 2026-06-30 (US GAAP inputs). [S04]
Formula: `net_income / revenue * 100`. Inputs: net_income=573000000 USD (NetIncomeLoss), revenue=9028000000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Annual revenue changed +6.81% from the year ended 2025-06-30 to 2026-06-30. [S04]
Formula: `(current / prior - 1) * 100`. Inputs: revenue=9028000000 USD (RevenueFromContractWithCustomerExcludingAssessedTax), revenue=8452000000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Annual net income changed -51.44% from the year ended 2025-06-30 to 2026-06-30. [S04]
Formula: `(current / prior - 1) * 100`. Inputs: net_income=573000000 USD (NetIncomeLoss), net_income=1180000000 USD (NetIncomeLoss).

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T18:10:35.452616+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-07-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -426,000,000 | USD | US GAAP / reported | PaymentsToAcquirePropertyPlantAndEquipment; Cash outflow = negative of reported PaymentsToAcquirePropertyPlantAndEquipment; source value retained. | [S04] |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S04] |
| free_cash_flow | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| gross_profit | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income | 573,000,000 | USD | US GAAP / reported | NetIncomeLoss | [S04] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income_including_noncontrolling_interests | 743,000,000 | USD | US GAAP / reported | ProfitLoss | [S04] |
| operating_cash_flow | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| operating_income | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | 9,028,000,000 | USD | US GAAP / reported | RevenueFromContractWithCustomerExcludingAssessedTax | [S04] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S04] |
| stock_based_compensation | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |


### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -146,000,000 | USD | US GAAP / derived | PaymentsToAcquirePropertyPlantAndEquipment; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| free_cash_flow | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| gross_profit | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income | 179,000,000 | USD | US GAAP / derived | NetIncomeLoss; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income_including_noncontrolling_interests | 230,000,000 | USD | US GAAP / derived | ProfitLoss; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| operating_cash_flow | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| operating_income | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | Unavailable / blocked | USD | US GAAP / derived / not model usable | RevenueFromContractWithCustomerExcludingAssessedTax; cross_filing_derivation, definition_changed_across_series, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| shares_basic | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_diluted | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| stock_based_compensation | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |



## Balance sheet and capital allocation

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T18:10:35.452616+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-07-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 2,095,000,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S04] |
| debt_current | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtCurrent; debt_scope_requires_filing_review | [S04] |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtNoncurrent; debt_scope_requires_filing_review | [S04] |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebt; debt_scope_requires_filing_review | [S04] |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |


### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 2,095,000,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S04] |
| debt_current | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtCurrent; debt_scope_requires_filing_review | [S04] |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtNoncurrent; debt_scope_requires_filing_review | [S04] |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebt; debt_scope_requires_filing_review | [S04] |
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
- Collector status: quality_review_required; last action: new_financial_filing; last checked: 2026-10-23T14:31:16.004163+00:00.

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

Calculation gaps: Operating margin: compatible positive revenue and usable inputs are required. Free cash flow margin: compatible positive revenue and usable inputs are required. Stock compensation / revenue: compatible positive revenue and usable inputs are required. operating_income: annual growth withheld because periods, definitions or a positive prior denominator are not verified. operating_cash_flow: annual growth withheld because periods, definitions or a positive prior denominator are not verified. free_cash_flow: annual growth withheld because periods, definitions or a positive prior denominator are not verified.

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest five available filing metadata records; document bodies have not been analyzed here.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-10-22 | 8-K | 0001564708-26-000234 | — | [S17] |
| 2026-10-21 | 8-K | 0001564708-26-000233 | — | [S18] |
| 2026-10-20 | 8-K | 0001564708-26-000232 | — | [S19] |
| 2026-10-19 | 8-K | 0001564708-26-000231 | — | [S20] |
| 2026-10-16 | 8-K | 0001564708-26-000230 | — | [S21] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-23T14:17:54.530395+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001564708.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [SEC CompanyFacts source](https://data.sec.gov/api/xbrl/companyfacts/CIK0001564708.json) — published not supplied; retrieved 2026-10-22T18:10:35.452616+00:00.

[S04] [10-K 0001564708-26-000175](https://www.sec.gov/Archives/edgar/data/1564708/000156470826000175/0001564708-26-000175-index.html) — published 2026-08-07; retrieved 2026-10-22T18:10:35.452616+00:00.

[S08] [10-Q 0001564708-26-000103](https://www.sec.gov/Archives/edgar/data/1564708/000156470826000103/0001564708-26-000103-index.html) — published 2026-05-08; retrieved 2026-10-22T18:10:35.452616+00:00.

[S17] [8-K 0001564708-26-000234](https://www.sec.gov/Archives/edgar/data/1564708/000156470826000234/0001564708-26-000234-index.html) — published 2026-10-22; retrieved 2026-10-23T08:33:02.691743+00:00.

[S18] [8-K 0001564708-26-000233](https://www.sec.gov/Archives/edgar/data/1564708/000156470826000233/0001564708-26-000233-index.html) — published 2026-10-21; retrieved 2026-10-23T08:33:02.691743+00:00.

[S19] [8-K 0001564708-26-000232](https://www.sec.gov/Archives/edgar/data/1564708/000156470826000232/0001564708-26-000232-index.html) — published 2026-10-20; retrieved 2026-10-23T08:33:02.691743+00:00.

[S20] [8-K 0001564708-26-000231](https://www.sec.gov/Archives/edgar/data/1564708/000156470826000231/0001564708-26-000231-index.html) — published 2026-10-19; retrieved 2026-10-23T08:33:02.691743+00:00.

[S21] [8-K 0001564708-26-000230](https://www.sec.gov/Archives/edgar/data/1564708/000156470826000230/0001564708-26-000230-index.html) — published 2026-10-16; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261023-39968262770-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/d523cff21b18141b9a37cddd98ad6af6e1a30fa5/brain/companies/NWS/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
