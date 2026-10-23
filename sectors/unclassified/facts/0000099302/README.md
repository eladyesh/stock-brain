---
schema_version: 1
document_type: company_facts
company_id: company-cik-0000099302
cik: 0000099302
company_name: TRANSCAT INC
tickers:
- TRNS
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
  - '144'
  - 144/A
  - '3'
  - 3/A
  - '4'
  - 4/A
  - 424B3
  - 424B5
  - '5'
  - 8-K
  - 8-K/A
  - ARS
  - CORRESP
  - DEF 14A
  - DEFA14A
  - EFFECT
  - PRE 14A
  - S-3
  - S-3/A
  - S-3ASR
  - S-3MEF
  - S-8
  - S-8 POS
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  history:
    url: https://data.sec.gov/api/xbrl/companyfacts/CIK0000099302.json
    sha256: 898117c7986c9dc7028bb7a4d7a919c58e6db062de96b15211a690a36b90e5dc
    retrieved_at: '2026-10-22T17:39:41.848518+00:00'
    archive:
      member: CIK0000099302.json
      sha256: 7457a528288f1e3425cba6ffd7370c6c205845aba12761763aa5ae3683c0fdc2
      url: https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip
    acquisition: operator_supplied_sec_bulk_archive
  submissions:
    url: https://data.sec.gov/submissions/CIK0000099302.json
    sha256: 3b91dae5715a853ea40f22dd6f71c4348e7912a0b1468f7e27d446a7a74c0517
    retrieved_at: '2026-10-22T17:39:35.977490+00:00'
    archive: &id001
      member: CIK0000099302.json
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
  url: https://data.sec.gov/submissions/CIK0000099302.json
  published_at: null
  retrieved_at: '2026-10-22T17:39:35.977490+00:00'
  sha256: 3b91dae5715a853ea40f22dd6f71c4348e7912a0b1468f7e27d446a7a74c0517
- id: S03
  title: SEC CompanyFacts source
  url: https://data.sec.gov/api/xbrl/companyfacts/CIK0000099302.json
  published_at: null
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: 898117c7986c9dc7028bb7a4d7a919c58e6db062de96b15211a690a36b90e5dc
- id: S04
  title: 10-K 0001437749-26-018588
  url: https://www.sec.gov/Archives/edgar/data/99302/000143774926018588/0001437749-26-018588-index.html
  published_at: '2026-05-27'
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: null
- id: S05
  title: 10-Q 0001628280-26-052738
  url: https://www.sec.gov/Archives/edgar/data/99302/000162828026052738/0001628280-26-052738-index.html
  published_at: '2026-08-04'
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: null
- id: S17
  title: 8-K 0001628280-26-061346
  url: https://www.sec.gov/Archives/edgar/data/99302/000162828026061346/0001628280-26-061346-index.html
  published_at: '2026-09-10'
  retrieved_at: '2026-10-22T17:39:35.977490+00:00'
  sha256: null
- id: S18
  title: 4 0000891839-26-000404
  url: https://www.sec.gov/Archives/edgar/data/99302/000089183926000404/0000891839-26-000404-index.html
  published_at: '2026-09-10'
  retrieved_at: '2026-10-22T17:39:35.977490+00:00'
  sha256: null
- id: S19
  title: 4 0000891839-26-000403
  url: https://www.sec.gov/Archives/edgar/data/99302/000089183926000403/0000891839-26-000403-index.html
  published_at: '2026-09-10'
  retrieved_at: '2026-10-22T17:39:35.977490+00:00'
  sha256: null
- id: S20
  title: 4 0000891839-26-000402
  url: https://www.sec.gov/Archives/edgar/data/99302/000089183926000402/0000891839-26-000402-index.html
  published_at: '2026-09-10'
  retrieved_at: '2026-10-22T17:39:35.977490+00:00'
  sha256: null
- id: S21
  title: 4 0000891839-26-000401
  url: https://www.sec.gov/Archives/edgar/data/99302/000089183926000401/0000891839-26-000401-index.html
  published_at: '2026-09-10'
  retrieved_at: '2026-10-22T17:39:35.977490+00:00'
  sha256: null
issuer_classification:
  cik: 0000099302
  name: TRANSCAT INC
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-22T17:39:35.977490+00:00'
  sha256: 3b91dae5715a853ea40f22dd6f71c4348e7912a0b1468f7e27d446a7a74c0517
  url: https://data.sec.gov/submissions/CIK0000099302.json
sector_assignment:
  sector: unclassified
  method: unresolved
  sic: null
  sic_description: null
  rule_version: 1
  reason: Missing, ambiguous or unmapped reported industry; company-specific review
    is required.
full_history_url: https://github.com/eladyesh/stock-brain/blob/f1dea1c5fdf869d02b10266fe4da900fd3a13544/brain/companies/0000099302/README.md
full_history_commit: f1dea1c5fdf869d02b10266fe4da900fd3a13544
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# TRANSCAT INC — TRNS

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/f1dea1c5fdf869d02b10266fe4da900fd3a13544/brain/companies/0000099302/README.md)

## Business overview

Reported issuer name: **TRANSCAT INC**. Stable SEC CIK: **0000099302**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| TRNS | NASDAQ | common_stock | 1 | [S01] |

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

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:39:41.848518+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-03-30 to 2026-03-28

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -15,298,000 | USD | US GAAP / reported | PaymentsToAcquirePropertyPlantAndEquipment; Cash outflow = negative of reported PaymentsToAcquirePropertyPlantAndEquipment; source value retained. | [S04] |
| cost_of_revenue | 223,573,000 | USD | US GAAP / reported | CostOfGoodsAndServicesSold | [S04] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S04] |
| free_cash_flow | 19,552,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment | [S04] |
| gross_profit | 108,304,000 | USD | US GAAP / reported | GrossProfit | [S04] |
| net_income | 5,376,000 | USD | US GAAP / reported | NetIncomeLoss | [S04] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income_including_noncontrolling_interests | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| operating_cash_flow | 34,850,000 | USD | US GAAP / reported | NetCashProvidedByUsedInOperatingActivities | [S04] |
| operating_income | 13,263,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S04] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | 331,877,000 | USD | US GAAP / reported | Revenues | [S04] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S04] |
| stock_based_compensation | 7,549,000 | USD | US GAAP / reported | ShareBasedCompensation | [S04] |


### quarterly: 2026-03-29 to 2026-06-27

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -3,982,000 | USD | US GAAP / reported | PaymentsToAcquirePropertyPlantAndEquipment; Cash outflow = negative of reported PaymentsToAcquirePropertyPlantAndEquipment; source value retained. | [S05] |
| cost_of_revenue | 62,211,000 | USD | US GAAP / reported | CostOfGoodsAndServicesSold | [S05] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S05] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S05] |
| free_cash_flow | 4,835,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment | [S05] |
| gross_profit | 30,734,000 | USD | US GAAP / reported | GrossProfit | [S05] |
| net_income | 1,331,000 | USD | US GAAP / reported | NetIncomeLoss | [S05] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income_including_noncontrolling_interests | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| operating_cash_flow | 8,817,000 | USD | US GAAP / reported | NetCashProvidedByUsedInOperatingActivities | [S05] |
| operating_income | 3,719,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S05] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | 92,945,000 | USD | US GAAP / reported | Revenues | [S05] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S05] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S05] |
| stock_based_compensation | 1,978,000 | USD | US GAAP / reported | ShareBasedCompensation | [S05] |



## Balance sheet and capital allocation

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:39:41.848518+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-03-30 to 2026-03-28

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 4,942,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S05] |
| debt_current | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtCurrent; debt_scope_requires_filing_review | [S04] |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtNoncurrent; debt_scope_requires_filing_review | [S05] |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S05] |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |


### quarterly: 2026-03-29 to 2026-06-27

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 6,709,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S05] |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtNoncurrent; debt_scope_requires_filing_review | [S05] |
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
- Collector status: quality_review_required; last action: new_financial_filing; last checked: 2026-10-22T18:35:17.895070+00:00.

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest five available filing metadata records; document bodies have not been analyzed here.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-09-10 | 8-K | 0001628280-26-061346 | — | [S17] |
| 2026-09-10 | 4 | 0000891839-26-000404 | — | [S18] |
| 2026-09-10 | 4 | 0000891839-26-000403 | — | [S19] |
| 2026-09-10 | 4 | 0000891839-26-000402 | — | [S20] |
| 2026-09-10 | 4 | 0000891839-26-000401 | — | [S21] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-22T18:30:07.617970+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0000099302.json) — published not supplied; retrieved 2026-10-22T17:39:35.977490+00:00.

[S03] [SEC CompanyFacts source](https://data.sec.gov/api/xbrl/companyfacts/CIK0000099302.json) — published not supplied; retrieved 2026-10-22T17:39:41.848518+00:00.

[S04] [10-K 0001437749-26-018588](https://www.sec.gov/Archives/edgar/data/99302/000143774926018588/0001437749-26-018588-index.html) — published 2026-05-27; retrieved 2026-10-22T17:39:41.848518+00:00.

[S05] [10-Q 0001628280-26-052738](https://www.sec.gov/Archives/edgar/data/99302/000162828026052738/0001628280-26-052738-index.html) — published 2026-08-04; retrieved 2026-10-22T17:39:41.848518+00:00.

[S17] [8-K 0001628280-26-061346](https://www.sec.gov/Archives/edgar/data/99302/000162828026061346/0001628280-26-061346-index.html) — published 2026-09-10; retrieved 2026-10-22T17:39:35.977490+00:00.

[S18] [4 0000891839-26-000404](https://www.sec.gov/Archives/edgar/data/99302/000089183926000404/0000891839-26-000404-index.html) — published 2026-09-10; retrieved 2026-10-22T17:39:35.977490+00:00.

[S19] [4 0000891839-26-000403](https://www.sec.gov/Archives/edgar/data/99302/000089183926000403/0000891839-26-000403-index.html) — published 2026-09-10; retrieved 2026-10-22T17:39:35.977490+00:00.

[S20] [4 0000891839-26-000402](https://www.sec.gov/Archives/edgar/data/99302/000089183926000402/0000891839-26-000402-index.html) — published 2026-09-10; retrieved 2026-10-22T17:39:35.977490+00:00.

[S21] [4 0000891839-26-000401](https://www.sec.gov/Archives/edgar/data/99302/000089183926000401/0000891839-26-000401-index.html) — published 2026-09-10; retrieved 2026-10-22T17:39:35.977490+00:00.

Source release: `coverage-20261022-39831584719-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/f1dea1c5fdf869d02b10266fe4da900fd3a13544/brain/companies/0000099302/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
