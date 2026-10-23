---
schema_version: 1
document_type: company_facts
company_id: company-cik-0002061473
cik: '0002061473'
company_name: Perimeter Acquisition Corp. I
tickers:
- PMTR
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
  - 8-A12B
  - 8-K
  - CERT
  - CORRESP
  - EFFECT
  - S-1
  - S-1/A
  - S-1MEF
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  history:
    url: https://data.sec.gov/api/xbrl/companyfacts/CIK0002061473.json
    sha256: 6403d9ffaa696a6d0e510a751d4567b56a74d162611c11c18e8053bf0d0831c7
    retrieved_at: '2026-10-22T17:39:41.848518+00:00'
    archive:
      member: CIK0002061473.json
      sha256: 7457a528288f1e3425cba6ffd7370c6c205845aba12761763aa5ae3683c0fdc2
      url: https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip
    acquisition: operator_supplied_sec_bulk_archive
  submissions:
    url: https://data.sec.gov/submissions/CIK0002061473.json
    sha256: 77b141ed052f0d0f928570a18ebcc78c7ab2eef9f5142b5ff64ea24d6cad42e0
    retrieved_at: '2026-10-22T17:39:35.977490+00:00'
    archive: &id001
      member: CIK0002061473.json
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
  url: https://data.sec.gov/submissions/CIK0002061473.json
  published_at: null
  retrieved_at: '2026-10-22T17:39:35.977490+00:00'
  sha256: 77b141ed052f0d0f928570a18ebcc78c7ab2eef9f5142b5ff64ea24d6cad42e0
- id: S03
  title: SEC CompanyFacts source
  url: https://data.sec.gov/api/xbrl/companyfacts/CIK0002061473.json
  published_at: null
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: 6403d9ffaa696a6d0e510a751d4567b56a74d162611c11c18e8053bf0d0831c7
- id: S04
  title: 10-Q 0001493152-26-037779
  url: https://www.sec.gov/Archives/edgar/data/2061473/000149315226037779/0001493152-26-037779-index.html
  published_at: '2026-08-13'
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: null
- id: S08
  title: SCHEDULE 13G/A 0001193125-26-351088
  url: https://www.sec.gov/Archives/edgar/data/2061473/000119312526351088/0001193125-26-351088-index.html
  published_at: '2026-08-14'
  retrieved_at: '2026-10-22T17:39:35.977490+00:00'
  sha256: null
- id: S09
  title: 10-Q 0001493152-26-037779
  url: https://www.sec.gov/Archives/edgar/data/2061473/000149315226037779/0001493152-26-037779-index.html
  published_at: '2026-08-13'
  retrieved_at: '2026-10-22T17:39:35.977490+00:00'
  sha256: null
- id: S10
  title: SCHEDULE 13G 0001688382-26-000018
  url: https://www.sec.gov/Archives/edgar/data/2061473/000168838226000018/0001688382-26-000018-index.html
  published_at: '2026-05-15'
  retrieved_at: '2026-10-22T17:39:35.977490+00:00'
  sha256: null
- id: S11
  title: 10-Q 0001493152-26-023853
  url: https://www.sec.gov/Archives/edgar/data/2061473/000149315226023853/0001493152-26-023853-index.html
  published_at: '2026-05-15'
  retrieved_at: '2026-10-22T17:39:35.977490+00:00'
  sha256: null
- id: S12
  title: 10-K 0001493152-26-013411
  url: https://www.sec.gov/Archives/edgar/data/2061473/000149315226013411/0001493152-26-013411-index.html
  published_at: '2026-03-30'
  retrieved_at: '2026-10-22T17:39:35.977490+00:00'
  sha256: null
issuer_classification:
  cik: '0002061473'
  name: Perimeter Acquisition Corp. I
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-22T17:39:35.977490+00:00'
  sha256: 77b141ed052f0d0f928570a18ebcc78c7ab2eef9f5142b5ff64ea24d6cad42e0
  url: https://data.sec.gov/submissions/CIK0002061473.json
sector_assignment:
  sector: unclassified
  method: unresolved
  sic: null
  sic_description: null
  rule_version: 1
  reason: Missing, ambiguous or unmapped reported industry; company-specific review
    is required.
full_history_url: https://github.com/eladyesh/stock-brain/blob/f1dea1c5fdf869d02b10266fe4da900fd3a13544/brain/companies/0002061473/README.md
full_history_commit: f1dea1c5fdf869d02b10266fe4da900fd3a13544
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# Perimeter Acquisition Corp. I — PMTR

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/f1dea1c5fdf869d02b10266fe4da900fd3a13544/brain/companies/0002061473/README.md)

## Business overview

Reported issuer name: **Perimeter Acquisition Corp. I**. Stable SEC CIK: **0002061473**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| PMTR | NASDAQ | common_stock | 1 | [S01] |

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
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| free_cash_flow | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| gross_profit | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| net_income | Unavailable / blocked | USD | US GAAP / reported / not model usable | NetIncomeLoss; missing_annual_anchor | [S04] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| net_income_including_noncontrolling_interests | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| operating_cash_flow | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| operating_income | Unavailable / blocked | USD | US GAAP / reported / not model usable | OperatingIncomeLoss; missing_annual_anchor | [S04] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| revenue | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| shares_basic | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| shares_diluted | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| stock_based_compensation | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |



## Balance sheet and capital allocation

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:39:41.848518+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermNotesPayable; debt_scope_requires_filing_review, missing_annual_anchor | [S04] |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |



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
- Collector status: quality_review_required; last action: new_financial_filing; last checked: 2026-10-22T18:45:19.216910+00:00.

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest five available filing metadata records; document bodies have not been analyzed here.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-08-14 | SCHEDULE 13G/A | 0001193125-26-351088 | — | [S08] |
| 2026-08-13 | 10-Q | 0001493152-26-037779 | — | [S09] |
| 2026-05-15 | SCHEDULE 13G | 0001688382-26-000018 | — | [S10] |
| 2026-05-15 | 10-Q | 0001493152-26-023853 | — | [S11] |
| 2026-03-30 | 10-K | 0001493152-26-013411 | — | [S12] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-22T18:30:07.617970+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0002061473.json) — published not supplied; retrieved 2026-10-22T17:39:35.977490+00:00.

[S03] [SEC CompanyFacts source](https://data.sec.gov/api/xbrl/companyfacts/CIK0002061473.json) — published not supplied; retrieved 2026-10-22T17:39:41.848518+00:00.

[S04] [10-Q 0001493152-26-037779](https://www.sec.gov/Archives/edgar/data/2061473/000149315226037779/0001493152-26-037779-index.html) — published 2026-08-13; retrieved 2026-10-22T17:39:41.848518+00:00.

[S08] [SCHEDULE 13G/A 0001193125-26-351088](https://www.sec.gov/Archives/edgar/data/2061473/000119312526351088/0001193125-26-351088-index.html) — published 2026-08-14; retrieved 2026-10-22T17:39:35.977490+00:00.

[S09] [10-Q 0001493152-26-037779](https://www.sec.gov/Archives/edgar/data/2061473/000149315226037779/0001493152-26-037779-index.html) — published 2026-08-13; retrieved 2026-10-22T17:39:35.977490+00:00.

[S10] [SCHEDULE 13G 0001688382-26-000018](https://www.sec.gov/Archives/edgar/data/2061473/000168838226000018/0001688382-26-000018-index.html) — published 2026-05-15; retrieved 2026-10-22T17:39:35.977490+00:00.

[S11] [10-Q 0001493152-26-023853](https://www.sec.gov/Archives/edgar/data/2061473/000149315226023853/0001493152-26-023853-index.html) — published 2026-05-15; retrieved 2026-10-22T17:39:35.977490+00:00.

[S12] [10-K 0001493152-26-013411](https://www.sec.gov/Archives/edgar/data/2061473/000149315226013411/0001493152-26-013411-index.html) — published 2026-03-30; retrieved 2026-10-22T17:39:35.977490+00:00.

Source release: `coverage-20261022-39831584719-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/f1dea1c5fdf869d02b10266fe4da900fd3a13544/brain/companies/0002061473/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
