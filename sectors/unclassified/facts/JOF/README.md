---
schema_version: 1
document_type: company_facts
company_id: company-cik-0000859796
cik: 0000859796
company_name: JAPAN SMALLER CAPITALIZATION FUND INC
tickers:
- JOF
status: stub
canonical_reviewed: false
as_of: '2026-10-29'
updated_at: '2026-10-29T16:18:46.634043+00:00'
reviewed_at: null
coverage_release: coverage-20261029-40909364006-1
source_commit: aa19db75827ed3c73031b70e9a0a2e63baffc491
financial_history_available: false
curated_research: null
financial_gap:
  reason: fund_reporting_review
  next_action: Review the instrument against its N-CSR/N-CSRS reporting evidence before
    applying an operating-company model. This signal alone is not a final fund classification.
  observed_forms:
  - '3'
  - 3/A
  - '4'
  - 4/A
  - 40-17G
  - 40-17G/A
  - 40-APP
  - 40-APP/A
  - '497'
  - 497AD
  - 8-K
  - CORRESP
  - DEF 14A
  - DEFA14A
  - DEFR14A
  - EFFECT
  - N-2
  - N-2/A
  - N-30D
  - N-CEN
  - N-CSR
  - N-CSR/A
  - N-CSRS
  - N-PX
  - N-Q
  - NPORT-P
  - NSAR-A
  - NSAR-B
  - NT-NCSR
  - NT-NSAR
  - POS EX
  - PRE 14A
  - PRER14A
  - SC 13G
  - SC 13G/A
  - SC TO-C
  - SC TO-I
  - SC TO-I/A
  - SCHEDULE 13D
  - SCHEDULE 13D/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0000859796.json
    sha256: d4913da772ded5291c7443b4a3cc5b92daef720a765d03ad38785b47d5daa15d
    retrieved_at: '2026-10-24T13:22:51.759433+00:00'
    archive: &id001
      member: CIK0000859796.json
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
  url: https://data.sec.gov/submissions/CIK0000859796.json
  published_at: null
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: d4913da772ded5291c7443b4a3cc5b92daef720a765d03ad38785b47d5daa15d
- id: S03
  title: SCHEDULE 13G/A 0001072613-26-000835
  url: https://www.sec.gov/Archives/edgar/data/859796/000107261326000835/0001072613-26-000835-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S04
  title: 4 0001510281-26-000363
  url: https://www.sec.gov/Archives/edgar/data/859796/000151028126000363/0001510281-26-000363-index.html
  published_at: '2026-10-20'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S05
  title: 4 0001510281-26-000353
  url: https://www.sec.gov/Archives/edgar/data/859796/000151028126000353/0001510281-26-000353-index.html
  published_at: '2026-10-16'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S06
  title: 3 0001510281-26-000352
  url: https://www.sec.gov/Archives/edgar/data/859796/000151028126000352/0001510281-26-000352-index.html
  published_at: '2026-10-16'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S07
  title: DEFR14A 0001133228-26-013352
  url: https://www.sec.gov/Archives/edgar/data/859796/000113322826013352/0001133228-26-013352-index.html
  published_at: '2026-10-16'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
issuer_classification:
  cik: 0000859796
  classification_status: missing_or_invalid_sic
  entity_type: other
  name: JAPAN SMALLER CAPITALIZATION FUND INC
  sic: null
  sic_description: ''
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: d4913da772ded5291c7443b4a3cc5b92daef720a765d03ad38785b47d5daa15d
  url: https://data.sec.gov/submissions/CIK0000859796.json
listings:
- ticker: JOF
  exchange: NYSE
  instrument_type: common_stock
research_filings:
- accession: 0001133228-26-013230
  filed: '2026-10-13'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/859796/000113322826013230/0001133228-26-013230-index.html
- accession: 0001140361-24-039769
  filed: '2024-08-30'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/859796/000114036124039769/0001140361-24-039769-index.html
research_progress:
  stage: pending
  input_sha256: 1b33719e2ab600de6d2b7b8fd592fde13a73c741b98bd7af7a480006f7471e2d
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
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
full_history_url: https://github.com/eladyesh/stock-brain/blob/c26f59bc72c00102d2490e95b07449f8cd848491/brain/companies/JOF/README.md
full_history_commit: c26f59bc72c00102d2490e95b07449f8cd848491
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# JOF — JAPAN SMALLER CAPITALIZATION FUND INC

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/c26f59bc72c00102d2490e95b07449f8cd848491/brain/companies/JOF/README.md)

## Business overview

Reported issuer name: **JAPAN SMALLER CAPITALIZATION FUND INC**. Stable SEC CIK: **0000859796**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| JOF | NYSE | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

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
- Forms observed in the retained filing inventory: 3, 3/A, 4, 4/A, 40-17G, 40-17G/A, 40-APP, 40-APP/A, 497, 497AD, 8-K, CORRESP, DEF 14A, DEFA14A, DEFR14A, EFFECT, N-2, N-2/A, N-30D, N-CEN, N-CSR, N-CSR/A, N-CSRS, N-PX, N-Q, NPORT-P, NSAR-A, NSAR-B, NT-NCSR, NT-NSAR, POS EX, PRE 14A, PRER14A, SC 13G, SC 13G/A, SC TO-C, SC TO-I, SC TO-I/A, SCHEDULE 13D, SCHEDULE 13D/A, SCHEDULE 13G, SCHEDULE 13G/A, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:29:42.051181+00:00.

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
| 2026-10-23 | SCHEDULE 13G/A | 0001072613-26-000835 | — | [S03] |
| 2026-10-20 | 4 | 0001510281-26-000363 | — | [S04] |
| 2026-10-16 | 4 | 0001510281-26-000353 | — | [S05] |
| 2026-10-16 | 3 | 0001510281-26-000352 | — | [S06] |
| 2026-10-16 | DEFR14A | 0001133228-26-013352 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-29T16:14:13.951866+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0000859796.json) — published not supplied; retrieved 2026-10-24T13:22:51.759433+00:00.

[S03] [SCHEDULE 13G/A 0001072613-26-000835](https://www.sec.gov/Archives/edgar/data/859796/000107261326000835/0001072613-26-000835-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S04] [4 0001510281-26-000363](https://www.sec.gov/Archives/edgar/data/859796/000151028126000363/0001510281-26-000363-index.html) — published 2026-10-20; retrieved 2026-10-24T13:22:51.759433+00:00.

[S05] [4 0001510281-26-000353](https://www.sec.gov/Archives/edgar/data/859796/000151028126000353/0001510281-26-000353-index.html) — published 2026-10-16; retrieved 2026-10-24T13:22:51.759433+00:00.

[S06] [3 0001510281-26-000352](https://www.sec.gov/Archives/edgar/data/859796/000151028126000352/0001510281-26-000352-index.html) — published 2026-10-16; retrieved 2026-10-24T13:22:51.759433+00:00.

[S07] [DEFR14A 0001133228-26-013352](https://www.sec.gov/Archives/edgar/data/859796/000113322826013352/0001133228-26-013352-index.html) — published 2026-10-16; retrieved 2026-10-24T13:22:51.759433+00:00.

Source release: `coverage-20261029-40909364006-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/c26f59bc72c00102d2490e95b07449f8cd848491/brain/companies/JOF/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
