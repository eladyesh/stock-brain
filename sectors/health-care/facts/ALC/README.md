---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001167379
cik: 0001167379
company_name: ALCON INC
tickers:
- ALC
status: stub
canonical_reviewed: false
as_of: '2026-10-28'
updated_at: '2026-10-28T16:13:42.115634+00:00'
reviewed_at: null
coverage_release: coverage-20261028-40722802424-1
source_commit: 8a30d18f29f6ce6c61cbe955ca3f23f6f12ef180
financial_history_available: false
curated_research: null
financial_gap:
  reason: foreign_reporting_adapter
  next_action: Add support for the observed 20-F, 40-F or 6-K reporting forms and
    verify the actual accounting taxonomy before normalization.
  observed_forms:
  - 11-K
  - '144'
  - 15-12B
  - 20-F
  - 20FR12B
  - 20FR12B/A
  - 25-NSE
  - 424B5
  - '425'
  - 6-K
  - 6-K/A
  - 8-A12B
  - CERT
  - CERTNYS
  - CORRESP
  - DEFA14A
  - DEFM14A
  - DFAN14A
  - F-1
  - F-1/A
  - IRANNOTICE
  - NT 11-K
  - S-8
  - S-8 POS
  - SC 13D
  - SC 13D/A
  - SC 13E3
  - SC 13E3/A
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13G/A
  - SD
  - SEC ACTION
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001167379.json
    sha256: e900917d42eb27d33c8f63090ca8336bef55feedc16e8aede90d067cdf020c17
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001167379.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: otherlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt
  published_at: null
  retrieved_at: '2026-10-28T16:09:02.154543+00:00'
  sha256: 9075fbed01d898a38c24f9b203cac1b6a4eed581edb2da888a321447f3bb55cc
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001167379.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: e900917d42eb27d33c8f63090ca8336bef55feedc16e8aede90d067cdf020c17
- id: S03
  title: 6-K 0001167379-26-000030
  url: https://www.sec.gov/Archives/edgar/data/1167379/000116737926000030/0001167379-26-000030-index.html
  published_at: '2026-08-10'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: SD 0001167379-26-000025
  url: https://www.sec.gov/Archives/edgar/data/1167379/000116737926000025/0001167379-26-000025-index.html
  published_at: '2026-05-15'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 6-K 0001167379-26-000022
  url: https://www.sec.gov/Archives/edgar/data/1167379/000116737926000022/0001167379-26-000022-index.html
  published_at: '2026-05-05'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 6-K 0001167379-26-000019
  url: https://www.sec.gov/Archives/edgar/data/1167379/000116737926000019/0001167379-26-000019-index.html
  published_at: '2026-04-02'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 144 0001959173-26-001543
  url: https://www.sec.gov/Archives/edgar/data/1167379/000195917326001543/0001959173-26-001543-index.html
  published_at: '2026-02-26'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0001167379
  classification_status: reported_sic
  entity_type: other
  name: ALCON INC
  sic: '3851'
  sic_description: Ophthalmic Goods
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: e900917d42eb27d33c8f63090ca8336bef55feedc16e8aede90d067cdf020c17
  url: https://data.sec.gov/submissions/CIK0001167379.json
listings:
- ticker: ALC
  exchange: NYSE
  instrument_type: common_stock
research_filings:
- accession: 0001167379-26-000014
  filed: '2026-02-24'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1167379/000116737926000014/0001167379-26-000014-index.html
- accession: 0001167379-26-000030
  filed: '2026-08-10'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1167379/000116737926000030/0001167379-26-000030-index.html
- accession: 0001167379-09-000099
  filed: '2009-07-28'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1167379/000116737909000099/0001167379-09-000099-index.html
research_progress:
  stage: pending
  input_sha256: e6e875bda5cf2399ea50833cca3c9c7c881a7948dbf9ee05a2743d0e5f50b3cf
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
  derived_observations: 0
  model_draft: false
  reviewed: false
sector_assignment:
  sector: health-care
  method: project_sic_rule
  sic: '3851'
  sic_description: Ophthalmic Goods
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001167379.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/5da532c3abee5b40a5400c5864c6f3f4593276d7/brain/companies/ALC/README.md
full_history_commit: 5da532c3abee5b40a5400c5864c6f3f4593276d7
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# ALC — ALCON INC

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/5da532c3abee5b40a5400c5864c6f3f4593276d7/brain/companies/ALC/README.md)

## Business overview

Reported issuer name: **ALCON INC**. Stable SEC CIK: **0001167379**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| ALC | NYSE | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **3851**: Ophthalmic Goods. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **health-care**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

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
- Forms observed in the retained filing inventory: 11-K, 144, 15-12B, 20-F, 20FR12B, 20FR12B/A, 25-NSE, 424B5, 425, 6-K, 6-K/A, 8-A12B, CERT, CERTNYS, CORRESP, DEFA14A, DEFM14A, DFAN14A, F-1, F-1/A, IRANNOTICE, NT 11-K, S-8, S-8 POS, SC 13D, SC 13D/A, SC 13E3, SC 13E3/A, SC 13G, SC 13G/A, SCHEDULE 13G/A, SD, SEC ACTION, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:32:02.919786+00:00.

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
| 2026-08-10 | 6-K | 0001167379-26-000030 | — | [S03] |
| 2026-05-15 | SD | 0001167379-26-000025 | — | [S04] |
| 2026-05-05 | 6-K | 0001167379-26-000022 | — | [S05] |
| 2026-04-02 | 6-K | 0001167379-26-000019 | — | [S06] |
| 2026-02-26 | 144 | 0001959173-26-001543 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-28T16:09:02.154543+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001167379.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [6-K 0001167379-26-000030](https://www.sec.gov/Archives/edgar/data/1167379/000116737926000030/0001167379-26-000030-index.html) — published 2026-08-10; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [SD 0001167379-26-000025](https://www.sec.gov/Archives/edgar/data/1167379/000116737926000025/0001167379-26-000025-index.html) — published 2026-05-15; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [6-K 0001167379-26-000022](https://www.sec.gov/Archives/edgar/data/1167379/000116737926000022/0001167379-26-000022-index.html) — published 2026-05-05; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [6-K 0001167379-26-000019](https://www.sec.gov/Archives/edgar/data/1167379/000116737926000019/0001167379-26-000019-index.html) — published 2026-04-02; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [144 0001959173-26-001543](https://www.sec.gov/Archives/edgar/data/1167379/000195917326001543/0001959173-26-001543-index.html) — published 2026-02-26; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261028-40722802424-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/5da532c3abee5b40a5400c5864c6f3f4593276d7/brain/companies/ALC/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
