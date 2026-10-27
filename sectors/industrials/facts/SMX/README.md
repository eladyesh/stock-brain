---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001940674
cik: 0001940674
company_name: SMX (Security Matters) Public Ltd Co
tickers:
- SMX
status: stub
canonical_reviewed: false
as_of: '2026-10-27'
updated_at: '2026-10-27T15:30:18.641431+00:00'
reviewed_at: null
coverage_release: coverage-20261027-40530587641-1
source_commit: 77264ce478c0c699392c0a049f464d4fda44c9f8
financial_history_available: false
curated_research: null
financial_gap:
  reason: foreign_reporting_adapter
  next_action: Add support for the observed 20-F, 40-F or 6-K reporting forms and
    verify the actual accounting taxonomy before normalization.
  observed_forms:
  - 20-F
  - 20-F/A
  - '3'
  - '4'
  - 424B3
  - '425'
  - 6-K
  - 6-K/A
  - 8-A12B
  - CERT
  - CORRESP
  - D
  - DRS
  - DRSLTR
  - EFFECT
  - F-1
  - F-1/A
  - F-3
  - F-3/A
  - F-4
  - F-4/A
  - NT 20-F
  - POS AM
  - POS EX
  - S-8
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13D
  - SCHEDULE 13D/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001940674.json
    sha256: ec0351432e5da49644d9a722fd1e954e34ca3309777cba64ef73a6095db9ec4d
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001940674.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: nasdaqlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt
  published_at: null
  retrieved_at: '2026-10-27T15:25:33.739265+00:00'
  sha256: 29c7cedde394d9fb806c731f8be32ec8c78cad2668852342db80ae28619465f0
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001940674.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: ec0351432e5da49644d9a722fd1e954e34ca3309777cba64ef73a6095db9ec4d
- id: S03
  title: 6-K 0001493152-26-041732
  url: https://www.sec.gov/Archives/edgar/data/1940674/000149315226041732/0001493152-26-041732-index.html
  published_at: '2026-09-08'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 424B3 0001493152-26-036188
  url: https://www.sec.gov/Archives/edgar/data/1940674/000149315226036188/0001493152-26-036188-index.html
  published_at: '2026-08-05'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: EFFECT 9999999995-26-002540
  url: https://www.sec.gov/Archives/edgar/data/1940674/999999999526002540/9999999995-26-002540-index.html
  published_at: '2026-08-04'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: F-1 0001493152-26-035243
  url: https://www.sec.gov/Archives/edgar/data/1940674/000149315226035243/0001493152-26-035243-index.html
  published_at: '2026-07-29'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 6-K 0001493152-26-035025
  url: https://www.sec.gov/Archives/edgar/data/1940674/000149315226035025/0001493152-26-035025-index.html
  published_at: '2026-07-28'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0001940674
  classification_status: reported_sic
  entity_type: other
  name: SMX (Security Matters) Public Ltd Co
  sic: '3590'
  sic_description: Misc Industrial & Commercial Machinery & Equipment
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: ec0351432e5da49644d9a722fd1e954e34ca3309777cba64ef73a6095db9ec4d
  url: https://data.sec.gov/submissions/CIK0001940674.json
listings:
- ticker: SMX
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001493152-26-011985
  filed: '2026-03-20'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1940674/000149315226011985/0001493152-26-011985-index.html
- accession: 0001641172-25-010997
  filed: '2025-05-15'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1940674/000164117225010997/0001641172-25-010997-index.html
- accession: 0001493152-24-017776
  filed: '2024-05-03'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1940674/000149315224017776/0001493152-24-017776-index.html
- accession: 0001493152-26-041732
  filed: '2026-09-08'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1940674/000149315226041732/0001493152-26-041732-index.html
- accession: 0001493152-26-022198
  filed: '2026-05-11'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1940674/000149315226022198/0001493152-26-022198-index.html
- accession: 0001493152-25-027979
  filed: '2025-12-16'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1940674/000149315225027979/0001493152-25-027979-index.html
- accession: 0001493152-24-024327
  filed: '2024-06-18'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1940674/000149315224024327/0001493152-24-024327-index.html
- accession: 0001493152-23-020859
  filed: '2023-06-12'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1940674/000149315223020859/0001493152-23-020859-index.html
research_progress:
  stage: pending
  input_sha256: 262fed62d814dd26f2eaa61794561579d8dfe659c93b7b40a1a1d9675e3eb4e2
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
  derived_observations: 0
  model_draft: false
  reviewed: false
sector_assignment:
  sector: industrials
  method: project_sic_rule
  sic: '3590'
  sic_description: Misc Industrial & Commercial Machinery & Equipment
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001940674.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/f974cdc6ffee05a6e0489d88d3e13c8eebf0b613/brain/companies/SMX/README.md
full_history_commit: f974cdc6ffee05a6e0489d88d3e13c8eebf0b613
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# SMX — SMX (Security Matters) Public Ltd Co

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/f974cdc6ffee05a6e0489d88d3e13c8eebf0b613/brain/companies/SMX/README.md)

## Business overview

Reported issuer name: **SMX (Security Matters) Public Ltd Co**. Stable SEC CIK: **0001940674**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| SMX | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **3590**: Misc Industrial & Commercial Machinery & Equipment. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **industrials**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

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
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 20-F, 20-F/A, 3, 4, 424B3, 425, 6-K, 6-K/A, 8-A12B, CERT, CORRESP, D, DRS, DRSLTR, EFFECT, F-1, F-1/A, F-3, F-3/A, F-4, F-4/A, NT 20-F, POS AM, POS EX, S-8, SC 13D, SC 13D/A, SC 13G, SC 13G/A, SCHEDULE 13D, SCHEDULE 13D/A, SCHEDULE 13G, SCHEDULE 13G/A, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:36:24.890964+00:00.

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

Calculation gaps: Validated financial history is missing.

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest five available filing metadata records; document bodies have not been analyzed here.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-09-08 | 6-K | 0001493152-26-041732 | — | [S03] |
| 2026-08-05 | 424B3 | 0001493152-26-036188 | — | [S04] |
| 2026-08-04 | EFFECT | 9999999995-26-002540 | — | [S05] |
| 2026-07-29 | F-1 | 0001493152-26-035243 | — | [S06] |
| 2026-07-28 | 6-K | 0001493152-26-035025 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-27T15:25:33.739265+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001940674.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [6-K 0001493152-26-041732](https://www.sec.gov/Archives/edgar/data/1940674/000149315226041732/0001493152-26-041732-index.html) — published 2026-09-08; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [424B3 0001493152-26-036188](https://www.sec.gov/Archives/edgar/data/1940674/000149315226036188/0001493152-26-036188-index.html) — published 2026-08-05; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [EFFECT 9999999995-26-002540](https://www.sec.gov/Archives/edgar/data/1940674/999999999526002540/9999999995-26-002540-index.html) — published 2026-08-04; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [F-1 0001493152-26-035243](https://www.sec.gov/Archives/edgar/data/1940674/000149315226035243/0001493152-26-035243-index.html) — published 2026-07-29; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [6-K 0001493152-26-035025](https://www.sec.gov/Archives/edgar/data/1940674/000149315226035025/0001493152-26-035025-index.html) — published 2026-07-28; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261027-40530587641-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/f974cdc6ffee05a6e0489d88d3e13c8eebf0b613/brain/companies/SMX/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
