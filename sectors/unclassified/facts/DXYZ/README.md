---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001843974
cik: 0001843974
company_name: Destiny Tech100 Inc.
tickers:
- DXYZ
status: stub
canonical_reviewed: false
as_of: '2026-10-29'
updated_at: '2026-10-29T16:18:46.634043+00:00'
reviewed_at: null
coverage_release: coverage-20261029-40909364006-1
source_commit: 066173dd7c0933a11c2085b144bbb14099b44560
financial_history_available: false
curated_research: null
financial_gap:
  reason: fund_reporting_review
  next_action: Review the instrument against its N-CSR/N-CSRS reporting evidence before
    applying an operating-company model. This signal alone is not a final fund classification.
  observed_forms:
  - '144'
  - '3'
  - '4'
  - 40-17G
  - 424B3
  - 424B5
  - 497AD
  - 8-A12B
  - CERT
  - CORRESP
  - D
  - D/A
  - DEF 14A
  - DEFA14A
  - DEFR14A
  - EFFECT
  - N-2
  - N-2/A
  - N-2ASR
  - N-8A
  - N-CEN
  - N-CSR
  - N-CSR/A
  - N-CSRS
  - N-CSRS/A
  - N-PX
  - NPORT-P
  - NPORT-P/A
  - NT N-CEN
  - NT-NCEN
  - NT-NCSR
  - POS EX
  - SCHEDULE 13G
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001843974.json
    sha256: 66ff890e80c5ff8088979c7d5ec2301d74f6c1fe543bbf994994684e7a975b29
    retrieved_at: '2026-10-24T13:22:51.759433+00:00'
    archive: &id001
      member: CIK0001843974.json
      sha256: 593fbbea6512ef5ec729a5e513c465fbedaac8a66602c0abe00d0ba5a4d18732
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: otherlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt
  published_at: null
  retrieved_at: '2026-10-29T16:14:13.951866+00:00'
  sha256: 2ac9bdaf5d770442eb34b0b33eb6a5240dbd11a3f2077f7b88051dbb82d4313b
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001843974.json
  published_at: null
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 66ff890e80c5ff8088979c7d5ec2301d74f6c1fe543bbf994994684e7a975b29
- id: S03
  title: DEF 14A 0001999371-26-023456
  url: https://www.sec.gov/Archives/edgar/data/1843974/000199937126023456/0001999371-26-023456-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S04
  title: 4 0000945621-26-001136
  url: https://www.sec.gov/Archives/edgar/data/1843974/000094562126001136/0000945621-26-001136-index.html
  published_at: '2026-09-10'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S05
  title: 3 0000945621-26-001134
  url: https://www.sec.gov/Archives/edgar/data/1843974/000094562126001134/0000945621-26-001134-index.html
  published_at: '2026-09-10'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S06
  title: 4 0000945621-26-001118
  url: https://www.sec.gov/Archives/edgar/data/1843974/000094562126001118/0000945621-26-001118-index.html
  published_at: '2026-09-08'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S07
  title: 424B3 0001575872-26-000627
  url: https://www.sec.gov/Archives/edgar/data/1843974/000157587226000627/0001575872-26-000627-index.html
  published_at: '2026-08-31'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S53
  url: https://www.sec.gov/Archives/edgar/data/1843974/000199937126023456/dxyz-def14a_112026.htm
  title: DEF 14A 0001999371-26-023456
  published_at: '2026-10-23'
  retrieved_at: '2026-10-26T16:25:35.905141+00:00'
  sha256: b20a9cf4711918ff527470b9c4974ab8f2b499e7976e57503663c1e7e2c9ea31
issuer_classification:
  cik: 0001843974
  classification_status: missing_or_invalid_sic
  entity_type: other
  name: Destiny Tech100 Inc.
  sic: null
  sic_description: ''
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 66ff890e80c5ff8088979c7d5ec2301d74f6c1fe543bbf994994684e7a975b29
  url: https://data.sec.gov/submissions/CIK0001843974.json
listings:
- ticker: DXYZ
  exchange: NYSE
  instrument_type: common_stock
research_filings:
- accession: 0001999371-26-023456
  filed: '2026-10-23'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/1843974/000199937126023456/0001999371-26-023456-index.html
research_progress:
  stage: evidence_collected
  input_sha256: ddc72e1570fddbed03da80ab5c79c97b5d3d8885175330a776f10cedb476e999
  last_attempt_at: '2026-10-26T16:22:31.694168+00:00'
  last_success_at: '2026-10-26T16:22:31.694168+00:00'
  next_retry_at: null
  source_set_current: true
  evidence_topics:
  - business-overview
  - management-and-governance
  derived_observations: 0
  model_draft: false
  reviewed: false
sector_assignment:
  sector: unclassified
  method: unresolved
  sic: null
  sic_description: ''
  rule_version: 1
  reason: Fund reporting signal requires instrument review before operating-sector
    classification.
full_history_url: https://github.com/eladyesh/stock-brain/blob/52b6569b626a07b359d4a15742ebb633a0e48007/brain/companies/DXYZ/README.md
full_history_commit: 52b6569b626a07b359d4a15742ebb633a0e48007
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# DXYZ — Destiny Tech100 Inc.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/52b6569b626a07b359d4a15742ebb633a0e48007/brain/companies/DXYZ/README.md)

## Business overview

Reported issuer name: **Destiny Tech100 Inc.**. Stable SEC CIK: **0001843974**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| DXYZ | NYSE | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — DEF 14A, filed 2026-10-23, L1777:

> and do not expect to have any employees. Services necessary for our business are provided by individuals who are employees or officers [S53]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

Not available: substantive research has not been completed. Place the company among suppliers, distribution channels, customers, and substitutes. Explain cyclicality and supply constraints.

Navigation sector: **unclassified**. Method: `unresolved`. Fund reporting signal requires instrument review before operating-sector classification.

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

Source excerpt — DEF 14A, filed 2026-10-23, L78:

> Travis Mason as a Class I member of the board of directors of the Company (the “Board”) to serve until the 2029 [S53]

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
- Next collection task: Review the instrument against its N-CSR/N-CSRS reporting evidence before applying an operating-company model. This signal alone is not a final fund classification.
- Forms observed in the retained filing inventory: 144, 3, 4, 40-17G, 424B3, 424B5, 497AD, 8-A12B, CERT, CORRESP, D, D/A, DEF 14A, DEFA14A, DEFR14A, EFFECT, N-2, N-2/A, N-2ASR, N-8A, N-CEN, N-CSR, N-CSR/A, N-CSRS, N-CSRS/A, N-PX, NPORT-P, NPORT-P/A, NT N-CEN, NT-NCEN, NT-NCSR, POS EX, SCHEDULE 13G, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:36:05.588206+00:00.

### Research work queue

Collection stage: **evidence_collected**. Extracted evidence is not a reviewed conclusion. Daily collection resumes from durable state; unchanged accessions are reused.

- **Business overview** (source excerpts available; assess the claim): Explain what the company does, who pays it, and why the business exists. Cite primary sources.
- **Revenue model and segments** (evidence or analysis still needed): Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.
- **Products and services** (evidence or analysis still needed): Describe the main products, customer problems solved, distribution, and product dependencies.
- **Customers and end markets** (evidence or analysis still needed): Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.
- **Industry and value chain** (evidence or analysis still needed): Place the company among suppliers, distribution channels, customers, and substitutes. Explain cyclicality and supply constraints.
- **Competitive landscape** (evidence or analysis still needed): Identify direct competitors and alternatives. Compare specific products or business segments, with sources.
- **Moat and differentiation** (evidence or analysis still needed): Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.
- **Growth drivers** (evidence or analysis still needed): Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.
- **Financial performance** (evidence or analysis still needed): Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.
- **Balance sheet and capital allocation** (evidence or analysis still needed): Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.
- **Management and governance** (source excerpts available; assess the claim): Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.
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
| 2026-10-23 | DEF 14A | 0001999371-26-023456 | — | [S03] |
| 2026-09-10 | 4 | 0000945621-26-001136 | — | [S04] |
| 2026-09-10 | 3 | 0000945621-26-001134 | — | [S05] |
| 2026-09-08 | 4 | 0000945621-26-001118 | — | [S06] |
| 2026-08-31 | 424B3 | 0001575872-26-000627 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-29T16:14:13.951866+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001843974.json) — published not supplied; retrieved 2026-10-24T13:22:51.759433+00:00.

[S03] [DEF 14A 0001999371-26-023456](https://www.sec.gov/Archives/edgar/data/1843974/000199937126023456/0001999371-26-023456-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S04] [4 0000945621-26-001136](https://www.sec.gov/Archives/edgar/data/1843974/000094562126001136/0000945621-26-001136-index.html) — published 2026-09-10; retrieved 2026-10-24T13:22:51.759433+00:00.

[S05] [3 0000945621-26-001134](https://www.sec.gov/Archives/edgar/data/1843974/000094562126001134/0000945621-26-001134-index.html) — published 2026-09-10; retrieved 2026-10-24T13:22:51.759433+00:00.

[S06] [4 0000945621-26-001118](https://www.sec.gov/Archives/edgar/data/1843974/000094562126001118/0000945621-26-001118-index.html) — published 2026-09-08; retrieved 2026-10-24T13:22:51.759433+00:00.

[S07] [424B3 0001575872-26-000627](https://www.sec.gov/Archives/edgar/data/1843974/000157587226000627/0001575872-26-000627-index.html) — published 2026-08-31; retrieved 2026-10-24T13:22:51.759433+00:00.

[S53] [DEF 14A 0001999371-26-023456](https://www.sec.gov/Archives/edgar/data/1843974/000199937126023456/dxyz-def14a_112026.htm) — published 2026-10-23; retrieved 2026-10-26T16:25:35.905141+00:00.

Source release: `coverage-20261029-40909364006-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/52b6569b626a07b359d4a15742ebb633a0e48007/brain/companies/DXYZ/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
