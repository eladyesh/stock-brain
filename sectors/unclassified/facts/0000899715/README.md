---
schema_version: 1
document_type: company_facts
company_id: company-cik-0000899715
cik: 0000899715
company_name: TANGER INC.
tickers:
- SKT
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
  - 10-K/A
  - 10-Q
  - 10-Q/A
  - '144'
  - 144/A
  - '3'
  - 3/A
  - '4'
  - 4/A
  - 424B5
  - 424B7
  - '5'
  - 8-K
  - 8-K/A
  - ARS
  - CORRESP
  - DEF 14A
  - DEFA14A
  - FWP
  - S-3ASR
  - S-8
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  history:
    url: https://data.sec.gov/api/xbrl/companyfacts/CIK0000899715.json
    sha256: 07d1b37c4ef7072f7602898f27fbdb23b7807841989c9dc5606a6e3bb77d0c2a
    retrieved_at: '2026-10-22T17:39:41.848518+00:00'
    archive:
      member: CIK0000899715.json
      sha256: 7457a528288f1e3425cba6ffd7370c6c205845aba12761763aa5ae3683c0fdc2
      url: https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip
    acquisition: operator_supplied_sec_bulk_archive
  submissions:
    url: https://data.sec.gov/submissions/CIK0000899715.json
    sha256: 2982097d8420c3fe8eebec72c79ae942462dc85ae9bdf822280a4242bcb76156
    retrieved_at: '2026-10-22T17:39:35.977490+00:00'
    archive: &id001
      member: CIK0000899715.json
      sha256: b6534bf3efaca6ea2a0a9509deb9eb4c612cb9aa12d4913fdb641a526cc4b033
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: otherlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt
  published_at: null
  retrieved_at: '2026-10-22T18:30:08.162126+00:00'
  sha256: 0be94d79fa8280e4e5fed634f305f620ea01ab67dda25960ecd76d3206dc969d
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0000899715.json
  published_at: null
  retrieved_at: '2026-10-22T17:39:35.977490+00:00'
  sha256: 2982097d8420c3fe8eebec72c79ae942462dc85ae9bdf822280a4242bcb76156
- id: S03
  title: SEC CompanyFacts source
  url: https://data.sec.gov/api/xbrl/companyfacts/CIK0000899715.json
  published_at: null
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: 07d1b37c4ef7072f7602898f27fbdb23b7807841989c9dc5606a6e3bb77d0c2a
- id: S04
  title: 10-Q 0001628280-26-053864
  url: https://www.sec.gov/Archives/edgar/data/899715/000162828026053864/0001628280-26-053864-index.html
  published_at: '2026-08-06'
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: null
- id: S16
  title: 4 0001628280-26-065147
  url: https://www.sec.gov/Archives/edgar/data/899715/000162828026065147/0001628280-26-065147-index.html
  published_at: '2026-10-05'
  retrieved_at: '2026-10-22T17:39:35.977490+00:00'
  sha256: null
- id: S17
  title: 4 0001628280-26-057367
  url: https://www.sec.gov/Archives/edgar/data/899715/000162828026057367/0001628280-26-057367-index.html
  published_at: '2026-08-17'
  retrieved_at: '2026-10-22T17:39:35.977490+00:00'
  sha256: null
- id: S18
  title: 10-Q 0001628280-26-053864
  url: https://www.sec.gov/Archives/edgar/data/899715/000162828026053864/0001628280-26-053864-index.html
  published_at: '2026-08-06'
  retrieved_at: '2026-10-22T17:39:35.977490+00:00'
  sha256: null
- id: S19
  title: SCHEDULE 13G/A 0000315066-26-002147
  url: https://www.sec.gov/Archives/edgar/data/899715/000031506626002147/0000315066-26-002147-index.html
  published_at: '2026-08-06'
  retrieved_at: '2026-10-22T17:39:35.977490+00:00'
  sha256: null
- id: S20
  title: 8-K 0001628280-26-052544
  url: https://www.sec.gov/Archives/edgar/data/899715/000162828026052544/0001628280-26-052544-index.html
  published_at: '2026-08-04'
  retrieved_at: '2026-10-22T17:39:35.977490+00:00'
  sha256: null
issuer_classification:
  cik: 0000899715
  name: TANGER INC.
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-22T17:39:35.977490+00:00'
  sha256: 2982097d8420c3fe8eebec72c79ae942462dc85ae9bdf822280a4242bcb76156
  url: https://data.sec.gov/submissions/CIK0000899715.json
sector_assignment:
  sector: unclassified
  method: unresolved
  sic: null
  sic_description: null
  rule_version: 1
  reason: Missing, ambiguous or unmapped reported industry; company-specific review
    is required.
full_history_url: https://github.com/eladyesh/stock-brain/blob/f1dea1c5fdf869d02b10266fe4da900fd3a13544/brain/companies/0000899715/README.md
full_history_commit: f1dea1c5fdf869d02b10266fe4da900fd3a13544
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# TANGER INC. — SKT

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/f1dea1c5fdf869d02b10266fe4da900fd3a13544/brain/companies/0000899715/README.md)

## Business overview

Reported issuer name: **TANGER INC.**. Stable SEC CIK: **0000899715**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| SKT | NYSE | common_stock | 1 | [S01] |

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

### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; missing_annual_anchor, share_split_and_corporate_action_basis_unverified | [S04] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; missing_annual_anchor, share_split_and_corporate_action_basis_unverified | [S04] |
| free_cash_flow | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| gross_profit | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| net_income | Unavailable / blocked | USD | US GAAP / reported / not model usable | NetIncomeLoss; missing_annual_anchor | [S04] |
| net_income_common | Unavailable / blocked | USD | US GAAP / reported / not model usable | NetIncomeLossAvailableToCommonStockholdersBasic; missing_annual_anchor | [S04] |
| net_income_including_noncontrolling_interests | Unavailable / blocked | USD | US GAAP / reported / not model usable | ProfitLoss; missing_annual_anchor | [S04] |
| operating_cash_flow | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| operating_income | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | RevenueFromContractWithCustomerExcludingAssessedTax; alternative_tag_scope_differs, definition_changed_across_series, missing_annual_anchor | [S04] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; missing_annual_anchor, share_split_and_corporate_action_basis_unverified | [S04] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; missing_annual_anchor, share_split_and_corporate_action_basis_unverified | [S04] |
| stock_based_compensation | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |



## Balance sheet and capital allocation

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:39:41.848518+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | Unavailable / blocked | USD | US GAAP / reported / not model usable | CashAndCashEquivalentsAtCarryingValue; missing_annual_anchor | [S04] |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebt; debt_scope_requires_filing_review, missing_annual_anchor | [S04] |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; missing_annual_anchor, share_split_and_corporate_action_basis_unverified | [S04] |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / reported / not model usable | ShortTermInvestments; missing_annual_anchor | [S04] |



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
- Collector status: quality_review_required; last action: new_financial_filing; last checked: 2026-10-22T18:37:39.523487+00:00.

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest five available filing metadata records; document bodies have not been analyzed here.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-10-05 | 4 | 0001628280-26-065147 | — | [S16] |
| 2026-08-17 | 4 | 0001628280-26-057367 | — | [S17] |
| 2026-08-06 | 10-Q | 0001628280-26-053864 | — | [S18] |
| 2026-08-06 | SCHEDULE 13G/A | 0000315066-26-002147 | — | [S19] |
| 2026-08-04 | 8-K | 0001628280-26-052544 | — | [S20] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-22T18:30:08.162126+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0000899715.json) — published not supplied; retrieved 2026-10-22T17:39:35.977490+00:00.

[S03] [SEC CompanyFacts source](https://data.sec.gov/api/xbrl/companyfacts/CIK0000899715.json) — published not supplied; retrieved 2026-10-22T17:39:41.848518+00:00.

[S04] [10-Q 0001628280-26-053864](https://www.sec.gov/Archives/edgar/data/899715/000162828026053864/0001628280-26-053864-index.html) — published 2026-08-06; retrieved 2026-10-22T17:39:41.848518+00:00.

[S16] [4 0001628280-26-065147](https://www.sec.gov/Archives/edgar/data/899715/000162828026065147/0001628280-26-065147-index.html) — published 2026-10-05; retrieved 2026-10-22T17:39:35.977490+00:00.

[S17] [4 0001628280-26-057367](https://www.sec.gov/Archives/edgar/data/899715/000162828026057367/0001628280-26-057367-index.html) — published 2026-08-17; retrieved 2026-10-22T17:39:35.977490+00:00.

[S18] [10-Q 0001628280-26-053864](https://www.sec.gov/Archives/edgar/data/899715/000162828026053864/0001628280-26-053864-index.html) — published 2026-08-06; retrieved 2026-10-22T17:39:35.977490+00:00.

[S19] [SCHEDULE 13G/A 0000315066-26-002147](https://www.sec.gov/Archives/edgar/data/899715/000031506626002147/0000315066-26-002147-index.html) — published 2026-08-06; retrieved 2026-10-22T17:39:35.977490+00:00.

[S20] [8-K 0001628280-26-052544](https://www.sec.gov/Archives/edgar/data/899715/000162828026052544/0001628280-26-052544-index.html) — published 2026-08-04; retrieved 2026-10-22T17:39:35.977490+00:00.

Source release: `coverage-20261022-39831584719-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/f1dea1c5fdf869d02b10266fe4da900fd3a13544/brain/companies/0000899715/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
