---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001279014
cik: 0001279014
company_name: ALLSPRING UTILITIES & HIGH INCOME FUND
tickers:
- ERH
status: stub
canonical_reviewed: false
as_of: '2026-10-25'
updated_at: '2026-10-25T13:50:29.910841+00:00'
reviewed_at: null
coverage_release: coverage-20261025-40199010718-1
source_commit: d4303e1efab53027fe4e6e90633e2c69b11c599c
financial_history_available: false
curated_research: null
financial_gap:
  reason: fund_reporting_review
  next_action: Review the instrument against its N-CSR/N-CSRS reporting evidence before
    applying an operating-company model. This signal alone is not a final fund classification.
  observed_forms:
  - '144'
  - '3'
  - 3/A
  - '4'
  - 4/A
  - 40-17G
  - 40-17G/A
  - 40-APP/A
  - '497'
  - '5'
  - 8-A12B
  - 8-K
  - CERTAMX
  - CORRESP
  - DEF 14A
  - DEFA14A
  - DEFR14A
  - N-2
  - N-2/A
  - N-23C-2
  - N-2MEF
  - N-8A
  - N-CEN
  - N-CEN/A
  - N-CSR
  - N-CSRS
  - N-CSRS/A
  - N-PX
  - N-Q
  - N-Q/A
  - NPORT-EX
  - NPORT-P
  - NPORT-P/A
  - NSAR-A
  - NSAR-B
  - NSAR-B/A
  - PRE 14A
  - SC 13G
  - SC 13G/A
  - SC TO-C
  - SC TO-I
  - SC TO-I/A
  - SCHEDULE 13G
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001279014.json
    sha256: fa186750cfadfcdd46118d999e3e8142fd9f2f2099aed8a0fdbc8990855c9f3d
    retrieved_at: '2026-10-24T13:22:51.759433+00:00'
    archive: &id001
      member: CIK0001279014.json
      sha256: 593fbbea6512ef5ec729a5e513c465fbedaac8a66602c0abe00d0ba5a4d18732
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: otherlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt
  published_at: null
  retrieved_at: '2026-10-25T13:45:48.334682+00:00'
  sha256: 94335ed3f4abc4bbd58a4415d105d453184f5484eaf6a2884d1bfb0120d850c9
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001279014.json
  published_at: null
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: fa186750cfadfcdd46118d999e3e8142fd9f2f2099aed8a0fdbc8990855c9f3d
- id: S03
  title: DEF 14A 0001279014-26-000006
  url: https://www.sec.gov/Archives/edgar/data/1279014/000127901426000006/0001279014-26-000006-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S04
  title: 8-K 0001279014-26-000004
  url: https://www.sec.gov/Archives/edgar/data/1279014/000127901426000004/0001279014-26-000004-index.html
  published_at: '2026-10-22'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S05
  title: 40-17G 0001279014-26-000001
  url: https://www.sec.gov/Archives/edgar/data/1279014/000127901426000001/0001279014-26-000001-index.html
  published_at: '2026-09-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S06
  title: NPORT-P/A 0001410368-26-091197
  url: https://www.sec.gov/Archives/edgar/data/1279014/000141036826091197/0001410368-26-091197-index.html
  published_at: '2026-09-10'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S07
  title: N-PX 0001081400-26-000395
  url: https://www.sec.gov/Archives/edgar/data/1279014/000108140026000395/0001081400-26-000395-index.html
  published_at: '2026-08-24'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
issuer_classification:
  cik: 0001279014
  classification_status: missing_or_invalid_sic
  entity_type: investment
  name: ALLSPRING UTILITIES & HIGH INCOME FUND
  sic: null
  sic_description: ''
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: fa186750cfadfcdd46118d999e3e8142fd9f2f2099aed8a0fdbc8990855c9f3d
  url: https://data.sec.gov/submissions/CIK0001279014.json
listings:
- ticker: ERH
  exchange: NYSE_AMERICAN
  instrument_type: common_stock
research_filings:
- accession: 0001279014-26-000006
  filed: '2026-10-23'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/1279014/000127901426000006/0001279014-26-000006-index.html
- accession: 0001279014-26-000004
  filed: '2026-10-22'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/1279014/000127901426000004/0001279014-26-000004-index.html
research_progress:
  stage: pending
  input_sha256: 4e06bac9b0cfa1e6776ac8e63ee832fcee63ceb9da5c75f9b9ec205dbb412b50
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
full_history_url: https://github.com/eladyesh/stock-brain/blob/c6b3af0cefe967faceb0323aa590d422e87cbc29/brain/companies/ERH/README.md
full_history_commit: c6b3af0cefe967faceb0323aa590d422e87cbc29
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# ERH — ALLSPRING UTILITIES & HIGH INCOME FUND

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/c6b3af0cefe967faceb0323aa590d422e87cbc29/brain/companies/ERH/README.md)

## Business overview

Reported issuer name: **ALLSPRING UTILITIES & HIGH INCOME FUND**. Stable SEC CIK: **0001279014**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| ERH | NYSE_AMERICAN | common_stock | 1 | [S01] |

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
- Forms observed in the retained filing inventory: 144, 3, 3/A, 4, 4/A, 40-17G, 40-17G/A, 40-APP/A, 497, 5, 8-A12B, 8-K, CERTAMX, CORRESP, DEF 14A, DEFA14A, DEFR14A, N-2, N-2/A, N-23C-2, N-2MEF, N-8A, N-CEN, N-CEN/A, N-CSR, N-CSRS, N-CSRS/A, N-PX, N-Q, N-Q/A, NPORT-EX, NPORT-P, NPORT-P/A, NSAR-A, NSAR-B, NSAR-B/A, PRE 14A, SC 13G, SC 13G/A, SC TO-C, SC TO-I, SC TO-I/A, SCHEDULE 13G
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:32:20.329655+00:00.

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
| 2026-10-23 | DEF 14A | 0001279014-26-000006 | — | [S03] |
| 2026-10-22 | 8-K | 0001279014-26-000004 | — | [S04] |
| 2026-09-23 | 40-17G | 0001279014-26-000001 | — | [S05] |
| 2026-09-10 | NPORT-P/A | 0001410368-26-091197 | — | [S06] |
| 2026-08-24 | N-PX | 0001081400-26-000395 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-25T13:45:48.334682+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001279014.json) — published not supplied; retrieved 2026-10-24T13:22:51.759433+00:00.

[S03] [DEF 14A 0001279014-26-000006](https://www.sec.gov/Archives/edgar/data/1279014/000127901426000006/0001279014-26-000006-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S04] [8-K 0001279014-26-000004](https://www.sec.gov/Archives/edgar/data/1279014/000127901426000004/0001279014-26-000004-index.html) — published 2026-10-22; retrieved 2026-10-24T13:22:51.759433+00:00.

[S05] [40-17G 0001279014-26-000001](https://www.sec.gov/Archives/edgar/data/1279014/000127901426000001/0001279014-26-000001-index.html) — published 2026-09-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S06] [NPORT-P/A 0001410368-26-091197](https://www.sec.gov/Archives/edgar/data/1279014/000141036826091197/0001410368-26-091197-index.html) — published 2026-09-10; retrieved 2026-10-24T13:22:51.759433+00:00.

[S07] [N-PX 0001081400-26-000395](https://www.sec.gov/Archives/edgar/data/1279014/000108140026000395/0001081400-26-000395-index.html) — published 2026-08-24; retrieved 2026-10-24T13:22:51.759433+00:00.

Source release: `coverage-20261025-40199010718-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/c6b3af0cefe967faceb0323aa590d422e87cbc29/brain/companies/ERH/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
