---
schema_version: 1
document_type: company_facts
company_id: company-cik-0002033122
cik: '0002033122'
company_name: Berto Acquisition Corp.
tickers:
- TACO
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
  - '3'
  - 424B4
  - '425'
  - 8-A12B
  - 8-K
  - CERT
  - CORRESP
  - DRS
  - EFFECT
  - S-1
  - S-1/A
  - S-1MEF
  - SCHEDULE 13G
  - UPLOAD
input_sources:
  history:
    url: https://data.sec.gov/api/xbrl/companyfacts/CIK0002033122.json
    sha256: 8ba32fd9ad50fffe6cb25f7c9acfa35bc2b5fe52b9494b1b78056d09ed92f488
    retrieved_at: '2026-10-22T17:39:41.848518+00:00'
    archive:
      member: CIK0002033122.json
      sha256: 7457a528288f1e3425cba6ffd7370c6c205845aba12761763aa5ae3683c0fdc2
      url: https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip
    acquisition: operator_supplied_sec_bulk_archive
  submissions:
    url: https://data.sec.gov/submissions/CIK0002033122.json
    sha256: 2bf19661769cc6808e933c79ebe32651b195271320e806ff6540af173f0ea1c8
    retrieved_at: '2026-10-22T17:39:35.977490+00:00'
    archive: &id001
      member: CIK0002033122.json
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
  url: https://data.sec.gov/submissions/CIK0002033122.json
  published_at: null
  retrieved_at: '2026-10-22T17:39:35.977490+00:00'
  sha256: 2bf19661769cc6808e933c79ebe32651b195271320e806ff6540af173f0ea1c8
- id: S03
  title: SEC CompanyFacts source
  url: https://data.sec.gov/api/xbrl/companyfacts/CIK0002033122.json
  published_at: null
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: 8ba32fd9ad50fffe6cb25f7c9acfa35bc2b5fe52b9494b1b78056d09ed92f488
- id: S04
  title: 10-K 0001829126-26-002856
  url: https://www.sec.gov/Archives/edgar/data/2033122/000182912626002856/0001829126-26-002856-index.html
  published_at: '2026-03-31'
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: null
- id: S05
  title: 10-Q 0001829126-26-008902
  url: https://www.sec.gov/Archives/edgar/data/2033122/000182912626008902/0001829126-26-008902-index.html
  published_at: '2026-08-14'
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: null
- id: S06
  title: 10-Q 0001829126-26-005372
  url: https://www.sec.gov/Archives/edgar/data/2033122/000182912626005372/0001829126-26-005372-index.html
  published_at: '2026-05-15'
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: null
- id: S10
  title: 10-Q 0001829126-26-008902
  url: https://www.sec.gov/Archives/edgar/data/2033122/000182912626008902/0001829126-26-008902-index.html
  published_at: '2026-08-14'
  retrieved_at: '2026-10-22T17:39:35.977490+00:00'
  sha256: null
- id: S11
  title: 10-Q 0001829126-26-005372
  url: https://www.sec.gov/Archives/edgar/data/2033122/000182912626005372/0001829126-26-005372-index.html
  published_at: '2026-05-15'
  retrieved_at: '2026-10-22T17:39:35.977490+00:00'
  sha256: null
- id: S12
  title: 10-K 0001829126-26-002856
  url: https://www.sec.gov/Archives/edgar/data/2033122/000182912626002856/0001829126-26-002856-index.html
  published_at: '2026-03-31'
  retrieved_at: '2026-10-22T17:39:35.977490+00:00'
  sha256: null
- id: S13
  title: 10-Q 0001829126-25-009131
  url: https://www.sec.gov/Archives/edgar/data/2033122/000182912625009131/0001829126-25-009131-index.html
  published_at: '2025-11-13'
  retrieved_at: '2026-10-22T17:39:35.977490+00:00'
  sha256: null
- id: S14
  title: 425 0001829126-25-008503
  url: https://www.sec.gov/Archives/edgar/data/2033122/000182912625008503/0001829126-25-008503-index.html
  published_at: '2025-10-29'
  retrieved_at: '2026-10-22T17:39:35.977490+00:00'
  sha256: null
issuer_classification:
  cik: '0002033122'
  name: Berto Acquisition Corp.
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-22T17:39:35.977490+00:00'
  sha256: 2bf19661769cc6808e933c79ebe32651b195271320e806ff6540af173f0ea1c8
  url: https://data.sec.gov/submissions/CIK0002033122.json
sector_assignment:
  sector: unclassified
  method: unresolved
  sic: null
  sic_description: null
  rule_version: 1
  reason: Missing, ambiguous or unmapped reported industry; company-specific review
    is required.
full_history_url: https://github.com/eladyesh/stock-brain/blob/f1dea1c5fdf869d02b10266fe4da900fd3a13544/brain/companies/0002033122/README.md
full_history_commit: f1dea1c5fdf869d02b10266fe4da900fd3a13544
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# Berto Acquisition Corp. — TACO

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/f1dea1c5fdf869d02b10266fe4da900fd3a13544/brain/companies/0002033122/README.md)

## Business overview

Reported issuer name: **Berto Acquisition Corp.**. Stable SEC CIK: **0002033122**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| TACO | NASDAQ | common_stock | 1 | [S01] |

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

### annual: 2025-01-01 to 2025-12-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S04] |
| free_cash_flow | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| gross_profit | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income | 7,876,314 | USD | US GAAP / reported | NetIncomeLoss | [S04] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income_including_noncontrolling_interests | 7,876,314 | USD | US GAAP / reported | ProfitLoss | [S04] |
| operating_cash_flow | -1,264,871 | USD | US GAAP / reported | NetCashProvidedByUsedInOperatingActivities | [S04] |
| operating_income | -647,449 | USD | US GAAP / reported | OperatingIncomeLoss | [S04] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_basic | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S04] |
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
| net_income | 1,110,431 | USD | US GAAP / reported | NetIncomeLoss | [S05] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income_including_noncontrolling_interests | 1,110,431 | USD | US GAAP / reported | ProfitLoss | [S05] |
| operating_cash_flow | -62,276 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S05] [S06] |
| operating_income | -1,624,853 | USD | US GAAP / reported | OperatingIncomeLoss | [S05] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_basic | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_diluted | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| stock_based_compensation | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |



## Balance sheet and capital allocation

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:39:41.848518+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-01-01 to 2025-12-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | Unavailable / blocked | USD | US GAAP / reported / not model usable | CashAndCashEquivalentsAtCarryingValue; revision_requires_review | [S05] |
| debt_current | Unavailable / blocked | USD | US GAAP / reported / not model usable | NotesPayableCurrent; debt_scope_requires_filing_review | [S05] |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S05] |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |


### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 146,740 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S05] |
| debt_current | Unavailable / blocked | USD | US GAAP / reported / not model usable | NotesPayableCurrent; debt_scope_requires_filing_review | [S05] |
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
- Collector status: quality_review_required; last action: new_financial_filing; last checked: 2026-10-22T18:45:16.572957+00:00.

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest five available filing metadata records; document bodies have not been analyzed here.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-08-14 | 10-Q | 0001829126-26-008902 | — | [S10] |
| 2026-05-15 | 10-Q | 0001829126-26-005372 | — | [S11] |
| 2026-03-31 | 10-K | 0001829126-26-002856 | — | [S12] |
| 2025-11-13 | 10-Q | 0001829126-25-009131 | — | [S13] |
| 2025-10-29 | 425 | 0001829126-25-008503 | — | [S14] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-22T18:30:07.617970+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0002033122.json) — published not supplied; retrieved 2026-10-22T17:39:35.977490+00:00.

[S03] [SEC CompanyFacts source](https://data.sec.gov/api/xbrl/companyfacts/CIK0002033122.json) — published not supplied; retrieved 2026-10-22T17:39:41.848518+00:00.

[S04] [10-K 0001829126-26-002856](https://www.sec.gov/Archives/edgar/data/2033122/000182912626002856/0001829126-26-002856-index.html) — published 2026-03-31; retrieved 2026-10-22T17:39:41.848518+00:00.

[S05] [10-Q 0001829126-26-008902](https://www.sec.gov/Archives/edgar/data/2033122/000182912626008902/0001829126-26-008902-index.html) — published 2026-08-14; retrieved 2026-10-22T17:39:41.848518+00:00.

[S06] [10-Q 0001829126-26-005372](https://www.sec.gov/Archives/edgar/data/2033122/000182912626005372/0001829126-26-005372-index.html) — published 2026-05-15; retrieved 2026-10-22T17:39:41.848518+00:00.

[S10] [10-Q 0001829126-26-008902](https://www.sec.gov/Archives/edgar/data/2033122/000182912626008902/0001829126-26-008902-index.html) — published 2026-08-14; retrieved 2026-10-22T17:39:35.977490+00:00.

[S11] [10-Q 0001829126-26-005372](https://www.sec.gov/Archives/edgar/data/2033122/000182912626005372/0001829126-26-005372-index.html) — published 2026-05-15; retrieved 2026-10-22T17:39:35.977490+00:00.

[S12] [10-K 0001829126-26-002856](https://www.sec.gov/Archives/edgar/data/2033122/000182912626002856/0001829126-26-002856-index.html) — published 2026-03-31; retrieved 2026-10-22T17:39:35.977490+00:00.

[S13] [10-Q 0001829126-25-009131](https://www.sec.gov/Archives/edgar/data/2033122/000182912625009131/0001829126-25-009131-index.html) — published 2025-11-13; retrieved 2026-10-22T17:39:35.977490+00:00.

[S14] [425 0001829126-25-008503](https://www.sec.gov/Archives/edgar/data/2033122/000182912625008503/0001829126-25-008503-index.html) — published 2025-10-29; retrieved 2026-10-22T17:39:35.977490+00:00.

Source release: `coverage-20261022-39831584719-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/f1dea1c5fdf869d02b10266fe4da900fd3a13544/brain/companies/0002033122/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
