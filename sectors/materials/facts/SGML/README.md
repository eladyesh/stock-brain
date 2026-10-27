---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001848309
cik: 0001848309
company_name: Sigma Lithium Corp
tickers:
- SGML
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
  - 40-F
  - 40-F/A
  - 40FR12B
  - 6-K
  - 6-K/A
  - CERT
  - D
  - F-10
  - F-10/A
  - F-X
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - SD
  - SEC STAFF ACTION
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001848309.json
    sha256: 15ff811d6113f378d920a68ad2e70bc5e12a1a320e09c08f3a8bcff145e57916
    retrieved_at: '2026-10-24T13:22:51.759433+00:00'
    archive: &id001
      member: CIK0001848309.json
      sha256: 593fbbea6512ef5ec729a5e513c465fbedaac8a66602c0abe00d0ba5a4d18732
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
  url: https://data.sec.gov/submissions/CIK0001848309.json
  published_at: null
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 15ff811d6113f378d920a68ad2e70bc5e12a1a320e09c08f3a8bcff145e57916
- id: S03
  title: 6-K 0001292814-26-004998
  url: https://www.sec.gov/Archives/edgar/data/1848309/000129281426004998/0001292814-26-004998-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S04
  title: SCHEDULE 13G 0001817646-26-000030
  url: https://www.sec.gov/Archives/edgar/data/1848309/000181764626000030/0001817646-26-000030-index.html
  published_at: '2026-10-07'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S05
  title: 6-K 0001292814-26-004858
  url: https://www.sec.gov/Archives/edgar/data/1848309/000129281426004858/0001292814-26-004858-index.html
  published_at: '2026-10-06'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S06
  title: 6-K 0001292814-26-004782
  url: https://www.sec.gov/Archives/edgar/data/1848309/000129281426004782/0001292814-26-004782-index.html
  published_at: '2026-10-01'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S07
  title: SD 0001292814-26-004724
  url: https://www.sec.gov/Archives/edgar/data/1848309/000129281426004724/0001292814-26-004724-index.html
  published_at: '2026-09-28'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
issuer_classification:
  cik: 0001848309
  classification_status: reported_sic
  entity_type: other
  name: Sigma Lithium Corp
  sic: '1000'
  sic_description: Metal Mining
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 15ff811d6113f378d920a68ad2e70bc5e12a1a320e09c08f3a8bcff145e57916
  url: https://data.sec.gov/submissions/CIK0001848309.json
listings:
- ticker: SGML
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001292814-26-001908
  filed: '2026-03-30'
  form: 40-F
  url: https://www.sec.gov/Archives/edgar/data/1848309/000129281426001908/0001292814-26-001908-index.html
- accession: 0001171843-25-002438
  filed: '2025-04-24'
  form: 40-F/A
  url: https://www.sec.gov/Archives/edgar/data/1848309/000117184325002438/0001171843-25-002438-index.html
- accession: 0001292814-26-004998
  filed: '2026-10-23'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1848309/000129281426004998/0001292814-26-004998-index.html
- accession: 0001104659-22-120290
  filed: '2022-11-18'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1848309/000110465922120290/0001104659-22-120290-index.html
- accession: 0001104659-22-120281
  filed: '2022-11-18'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1848309/000110465922120281/0001104659-22-120281-index.html
research_progress:
  stage: pending
  input_sha256: accdcf64522fdbf8a79244393eb0438662e05025cd540561472b45d8b8049f6d
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
  derived_observations: 0
  model_draft: false
  reviewed: false
sector_assignment:
  sector: materials
  method: project_sic_rule
  sic: '1000'
  sic_description: Metal Mining
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001848309.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/f974cdc6ffee05a6e0489d88d3e13c8eebf0b613/brain/companies/SGML/README.md
full_history_commit: f974cdc6ffee05a6e0489d88d3e13c8eebf0b613
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# SGML — Sigma Lithium Corp

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/f974cdc6ffee05a6e0489d88d3e13c8eebf0b613/brain/companies/SGML/README.md)

## Business overview

Reported issuer name: **Sigma Lithium Corp**. Stable SEC CIK: **0001848309**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| SGML | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **1000**: Metal Mining. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **materials**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

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
- Forms observed in the retained filing inventory: 40-F, 40-F/A, 40FR12B, 6-K, 6-K/A, CERT, D, F-10, F-10/A, F-X, SC 13G, SC 13G/A, SCHEDULE 13G, SCHEDULE 13G/A, SD, SEC STAFF ACTION
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:36:07.167631+00:00.

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
| 2026-10-23 | 6-K | 0001292814-26-004998 | — | [S03] |
| 2026-10-07 | SCHEDULE 13G | 0001817646-26-000030 | — | [S04] |
| 2026-10-06 | 6-K | 0001292814-26-004858 | — | [S05] |
| 2026-10-01 | 6-K | 0001292814-26-004782 | — | [S06] |
| 2026-09-28 | SD | 0001292814-26-004724 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-27T15:25:33.739265+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001848309.json) — published not supplied; retrieved 2026-10-24T13:22:51.759433+00:00.

[S03] [6-K 0001292814-26-004998](https://www.sec.gov/Archives/edgar/data/1848309/000129281426004998/0001292814-26-004998-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S04] [SCHEDULE 13G 0001817646-26-000030](https://www.sec.gov/Archives/edgar/data/1848309/000181764626000030/0001817646-26-000030-index.html) — published 2026-10-07; retrieved 2026-10-24T13:22:51.759433+00:00.

[S05] [6-K 0001292814-26-004858](https://www.sec.gov/Archives/edgar/data/1848309/000129281426004858/0001292814-26-004858-index.html) — published 2026-10-06; retrieved 2026-10-24T13:22:51.759433+00:00.

[S06] [6-K 0001292814-26-004782](https://www.sec.gov/Archives/edgar/data/1848309/000129281426004782/0001292814-26-004782-index.html) — published 2026-10-01; retrieved 2026-10-24T13:22:51.759433+00:00.

[S07] [SD 0001292814-26-004724](https://www.sec.gov/Archives/edgar/data/1848309/000129281426004724/0001292814-26-004724-index.html) — published 2026-09-28; retrieved 2026-10-24T13:22:51.759433+00:00.

Source release: `coverage-20261027-40530587641-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/f974cdc6ffee05a6e0489d88d3e13c8eebf0b613/brain/companies/SGML/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
