---
schema_version: 1
document_type: company_facts
company_id: company-cik-0002090312
cik: 0002090312
company_name: Mobility Global Inc.
tickers:
- MBGL
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
  - 10-12B
  - 10-12B/A
  - 10-Q
  - '3'
  - '4'
  - 8-K
  - CERT
  - DRS
  - DRS/A
  - S-8
  - SCHEDULE 13G
  - SEC STAFF ACTION
input_sources:
  history:
    url: https://data.sec.gov/api/xbrl/companyfacts/CIK0002090312.json
    sha256: 325f0ad8d2b972dee59046b13745a3f159b3bc8416e49930e1e0b0116100ec53
    retrieved_at: '2026-10-22T17:39:41.848518+00:00'
    archive:
      member: CIK0002090312.json
      sha256: 7457a528288f1e3425cba6ffd7370c6c205845aba12761763aa5ae3683c0fdc2
      url: https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip
    acquisition: operator_supplied_sec_bulk_archive
  submissions:
    url: https://data.sec.gov/submissions/CIK0002090312.json
    sha256: 0058b3685ea394f76b41339364d7dca98dc5c9174900afa16f32ddcc5c8d8c88
    retrieved_at: '2026-10-22T17:39:35.977490+00:00'
    archive: &id001
      member: CIK0002090312.json
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
  url: https://data.sec.gov/submissions/CIK0002090312.json
  published_at: null
  retrieved_at: '2026-10-22T17:39:35.977490+00:00'
  sha256: 0058b3685ea394f76b41339364d7dca98dc5c9174900afa16f32ddcc5c8d8c88
- id: S03
  title: SEC CompanyFacts source
  url: https://data.sec.gov/api/xbrl/companyfacts/CIK0002090312.json
  published_at: null
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: 325f0ad8d2b972dee59046b13745a3f159b3bc8416e49930e1e0b0116100ec53
- id: S04
  title: 10-Q 0002090312-26-000014
  url: https://www.sec.gov/Archives/edgar/data/2090312/000209031226000014/0002090312-26-000014-index.html
  published_at: '2026-08-07'
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: null
- id: S05
  title: 4 0002126577-26-000003
  url: https://www.sec.gov/Archives/edgar/data/2090312/000212657726000003/0002126577-26-000003-index.html
  published_at: '2026-09-03'
  retrieved_at: '2026-10-22T17:39:35.977490+00:00'
  sha256: null
- id: S06
  title: 4 0002090312-26-000027
  url: https://www.sec.gov/Archives/edgar/data/2090312/000209031226000027/0002090312-26-000027-index.html
  published_at: '2026-09-02'
  retrieved_at: '2026-10-22T17:39:35.977490+00:00'
  sha256: null
- id: S07
  title: 4 0002090312-26-000025
  url: https://www.sec.gov/Archives/edgar/data/2090312/000209031226000025/0002090312-26-000025-index.html
  published_at: '2026-09-02'
  retrieved_at: '2026-10-22T17:39:35.977490+00:00'
  sha256: null
- id: S08
  title: 4 0002090312-26-000023
  url: https://www.sec.gov/Archives/edgar/data/2090312/000209031226000023/0002090312-26-000023-index.html
  published_at: '2026-09-02'
  retrieved_at: '2026-10-22T17:39:35.977490+00:00'
  sha256: null
- id: S09
  title: 4 0002090312-26-000022
  url: https://www.sec.gov/Archives/edgar/data/2090312/000209031226000022/0002090312-26-000022-index.html
  published_at: '2026-09-02'
  retrieved_at: '2026-10-22T17:39:35.977490+00:00'
  sha256: null
issuer_classification:
  cik: 0002090312
  name: Mobility Global Inc.
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-22T17:39:35.977490+00:00'
  sha256: 0058b3685ea394f76b41339364d7dca98dc5c9174900afa16f32ddcc5c8d8c88
  url: https://data.sec.gov/submissions/CIK0002090312.json
sector_assignment:
  sector: unclassified
  method: unresolved
  sic: null
  sic_description: null
  rule_version: 1
  reason: Missing, ambiguous or unmapped reported industry; company-specific review
    is required.
full_history_url: https://github.com/eladyesh/stock-brain/blob/f1dea1c5fdf869d02b10266fe4da900fd3a13544/brain/companies/0002090312/README.md
full_history_commit: f1dea1c5fdf869d02b10266fe4da900fd3a13544
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# Mobility Global Inc. — MBGL

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/f1dea1c5fdf869d02b10266fe4da900fd3a13544/brain/companies/0002090312/README.md)

## Business overview

Reported issuer name: **Mobility Global Inc.**. Stable SEC CIK: **0002090312**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| MBGL | NYSE | common_stock | 1 | [S01] |

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
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | CostOfRevenue; missing_annual_anchor | [S04] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; missing_annual_anchor, share_split_and_corporate_action_basis_unverified | [S04] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; missing_annual_anchor, share_split_and_corporate_action_basis_unverified | [S04] |
| free_cash_flow | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| gross_profit | Unavailable / blocked | USD | US GAAP / derived / not model usable | CostOfRevenue + RevenueFromContractWithCustomerExcludingAssessedTax; missing_annual_anchor | [S04] |
| net_income | Unavailable / blocked | USD | US GAAP / reported / not model usable | NetIncomeLoss; missing_annual_anchor | [S04] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| net_income_including_noncontrolling_interests | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| operating_cash_flow | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| operating_income | Unavailable / blocked | USD | US GAAP / reported / not model usable | OperatingIncomeLoss; missing_annual_anchor | [S04] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | RevenueFromContractWithCustomerExcludingAssessedTax; missing_annual_anchor | [S04] |
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
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |

Not available: reviewed debt maturity, acquisition, dividend and repurchase analysis.

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
- Collector status: quality_review_required; last action: new_financial_filing; last checked: 2026-10-22T18:45:22.874949+00:00.

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest five available filing metadata records; document bodies have not been analyzed here.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-09-03 | 4 | 0002126577-26-000003 | — | [S05] |
| 2026-09-02 | 4 | 0002090312-26-000027 | — | [S06] |
| 2026-09-02 | 4 | 0002090312-26-000025 | — | [S07] |
| 2026-09-02 | 4 | 0002090312-26-000023 | — | [S08] |
| 2026-09-02 | 4 | 0002090312-26-000022 | — | [S09] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-22T18:30:08.162126+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0002090312.json) — published not supplied; retrieved 2026-10-22T17:39:35.977490+00:00.

[S03] [SEC CompanyFacts source](https://data.sec.gov/api/xbrl/companyfacts/CIK0002090312.json) — published not supplied; retrieved 2026-10-22T17:39:41.848518+00:00.

[S04] [10-Q 0002090312-26-000014](https://www.sec.gov/Archives/edgar/data/2090312/000209031226000014/0002090312-26-000014-index.html) — published 2026-08-07; retrieved 2026-10-22T17:39:41.848518+00:00.

[S05] [4 0002126577-26-000003](https://www.sec.gov/Archives/edgar/data/2090312/000212657726000003/0002126577-26-000003-index.html) — published 2026-09-03; retrieved 2026-10-22T17:39:35.977490+00:00.

[S06] [4 0002090312-26-000027](https://www.sec.gov/Archives/edgar/data/2090312/000209031226000027/0002090312-26-000027-index.html) — published 2026-09-02; retrieved 2026-10-22T17:39:35.977490+00:00.

[S07] [4 0002090312-26-000025](https://www.sec.gov/Archives/edgar/data/2090312/000209031226000025/0002090312-26-000025-index.html) — published 2026-09-02; retrieved 2026-10-22T17:39:35.977490+00:00.

[S08] [4 0002090312-26-000023](https://www.sec.gov/Archives/edgar/data/2090312/000209031226000023/0002090312-26-000023-index.html) — published 2026-09-02; retrieved 2026-10-22T17:39:35.977490+00:00.

[S09] [4 0002090312-26-000022](https://www.sec.gov/Archives/edgar/data/2090312/000209031226000022/0002090312-26-000022-index.html) — published 2026-09-02; retrieved 2026-10-22T17:39:35.977490+00:00.

Source release: `coverage-20261022-39831584719-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/f1dea1c5fdf869d02b10266fe4da900fd3a13544/brain/companies/0002090312/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
