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
as_of: '2026-10-22'
updated_at: '2026-10-22T18:45:53.881812+00:00'
reviewed_at: null
coverage_release: coverage-20261022-39831584719-1
source_commit: c640ba8ecaf78dc0ecb247c1e3ebadf4b6fa77ae
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
    retrieved_at: '2026-10-22T17:52:50.185860+00:00'
    archive: &id001
      member: CIK0000020286.json
      sha256: b6534bf3efaca6ea2a0a9509deb9eb4c612cb9aa12d4913fdb641a526cc4b033
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: nasdaqlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt
  published_at: null
  retrieved_at: '2026-10-22T18:30:07.617970+00:00'
  sha256: 484b32c59991d6364287abb8172f2106fc4eea58e5cb0256601a455a37cadda1
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0000020286.json
  published_at: null
  retrieved_at: '2026-10-22T17:52:50.185860+00:00'
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
  retrieved_at: '2026-10-22T17:52:50.185860+00:00'
  sha256: null
- id: S20
  title: 4 0001289454-26-000006
  url: https://www.sec.gov/Archives/edgar/data/20286/000128945426000006/0001289454-26-000006-index.html
  published_at: '2026-08-27'
  retrieved_at: '2026-10-22T17:52:50.185860+00:00'
  sha256: null
- id: S21
  title: N-PX 0001104659-26-101132
  url: https://www.sec.gov/Archives/edgar/data/20286/000110465926101132/0001104659-26-101132-index.html
  published_at: '2026-08-26'
  retrieved_at: '2026-10-22T17:52:50.185860+00:00'
  sha256: null
- id: S22
  title: 8-K 0000020286-26-000049
  url: https://www.sec.gov/Archives/edgar/data/20286/000002028626000049/0000020286-26-000049-index.html
  published_at: '2026-08-25'
  retrieved_at: '2026-10-22T17:52:50.185860+00:00'
  sha256: null
- id: S23
  title: 8-K 0000020286-26-000047
  url: https://www.sec.gov/Archives/edgar/data/20286/000002028626000047/0000020286-26-000047-index.html
  published_at: '2026-08-21'
  retrieved_at: '2026-10-22T17:52:50.185860+00:00'
  sha256: null
issuer_classification:
  cik: 0000020286
  name: CINCINNATI FINANCIAL CORP
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-22T17:52:50.185860+00:00'
  sha256: acbaa6f02061e22330310977da3b9b9cbd4bae35b73fc8753b4ce5bebf258423
  url: https://data.sec.gov/submissions/CIK0000020286.json
sector_assignment:
  sector: unclassified
  method: unresolved
  sic: null
  sic_description: null
  rule_version: 1
  reason: Missing, ambiguous or unmapped reported industry; company-specific review
    is required.
full_history_url: https://github.com/eladyesh/stock-brain/blob/f1dea1c5fdf869d02b10266fe4da900fd3a13544/brain/companies/0000020286/README.md
full_history_commit: f1dea1c5fdf869d02b10266fe4da900fd3a13544
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# CINCINNATI FINANCIAL CORP — CINF

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/f1dea1c5fdf869d02b10266fe4da900fd3a13544/brain/companies/0000020286/README.md)

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

Not available: substantive research has not been completed. Place the company among suppliers, distribution channels, customers, and substitutes. Explain cyclicality and supply constraints.

Navigation sector: **unclassified**. Method: `unresolved`. Missing, ambiguous or unmapped reported industry; company-specific review is required.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

## Financial performance

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
- Collector status: quality_review_required; last action: new_financial_filing; last checked: 2026-10-22T18:34:16.758449+00:00.

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

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-22T18:30:07.617970+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0000020286.json) — published not supplied; retrieved 2026-10-22T17:52:50.185860+00:00.

[S03] [SEC CompanyFacts source](https://data.sec.gov/api/xbrl/companyfacts/CIK0000020286.json) — published not supplied; retrieved 2026-10-22T17:53:02.398600+00:00.

[S04] [10-K 0000020286-26-000008](https://www.sec.gov/Archives/edgar/data/20286/000002028626000008/0000020286-26-000008-index.html) — published 2026-02-23; retrieved 2026-10-22T17:53:02.398600+00:00.

[S05] [10-Q 0000020286-26-000045](https://www.sec.gov/Archives/edgar/data/20286/000002028626000045/0000020286-26-000045-index.html) — published 2026-07-27; retrieved 2026-10-22T17:53:02.398600+00:00.

[S14] [10-Q 0000020286-26-000026](https://www.sec.gov/Archives/edgar/data/20286/000002028626000026/0000020286-26-000026-index.html) — published 2026-04-27; retrieved 2026-10-22T17:53:02.398600+00:00.

[S19] [8-K 0000020286-26-000052](https://www.sec.gov/Archives/edgar/data/20286/000002028626000052/0000020286-26-000052-index.html) — published 2026-09-28; retrieved 2026-10-22T17:52:50.185860+00:00.

[S20] [4 0001289454-26-000006](https://www.sec.gov/Archives/edgar/data/20286/000128945426000006/0001289454-26-000006-index.html) — published 2026-08-27; retrieved 2026-10-22T17:52:50.185860+00:00.

[S21] [N-PX 0001104659-26-101132](https://www.sec.gov/Archives/edgar/data/20286/000110465926101132/0001104659-26-101132-index.html) — published 2026-08-26; retrieved 2026-10-22T17:52:50.185860+00:00.

[S22] [8-K 0000020286-26-000049](https://www.sec.gov/Archives/edgar/data/20286/000002028626000049/0000020286-26-000049-index.html) — published 2026-08-25; retrieved 2026-10-22T17:52:50.185860+00:00.

[S23] [8-K 0000020286-26-000047](https://www.sec.gov/Archives/edgar/data/20286/000002028626000047/0000020286-26-000047-index.html) — published 2026-08-21; retrieved 2026-10-22T17:52:50.185860+00:00.

Source release: `coverage-20261022-39831584719-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/f1dea1c5fdf869d02b10266fe4da900fd3a13544/brain/companies/0000020286/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
