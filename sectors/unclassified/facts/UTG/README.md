---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001263994
cik: 0001263994
company_name: REAVES UTILITY INCOME FUND
tickers:
- UTG
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
  - '3'
  - 3/A
  - '4'
  - 4/A
  - 40-17G
  - 40-17G/A
  - 40-6C
  - 40-6C/A
  - 40-APP/A
  - 424B3
  - 424B5
  - '497'
  - 497AD
  - '5'
  - 5/A
  - 8-A12B
  - 8-K
  - APP NTC
  - APP ORDR
  - CERTAMX
  - CORRESP
  - DEF 14A
  - DEFA14A
  - DEFR14A
  - EFFECT
  - N-2
  - N-2/A
  - N-23C-2
  - N-2ASR
  - N-8A
  - N-CEN
  - N-CSR
  - N-CSR/A
  - N-CSRS
  - N-CSRS/A
  - N-PX
  - N-PX/A
  - N-Q
  - NPORT-EX
  - NPORT-P
  - NSAR-A
  - NSAR-B
  - NSAR-B/A
  - POS AMI
  - POS EX
  - PRE 14A
  - RW
  - SC 13G
  - SC 13G/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001263994.json
    sha256: 80998351faf66f6076d3f07af7cbbb9ee632e7f03221880d8644e12cc68242b1
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001263994.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
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
  url: https://data.sec.gov/submissions/CIK0001263994.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 80998351faf66f6076d3f07af7cbbb9ee632e7f03221880d8644e12cc68242b1
- id: S03
  title: NPORT-P 0001263994-26-000021
  url: https://www.sec.gov/Archives/edgar/data/1263994/000126399426000021/0001263994-26-000021-index.html
  published_at: '2026-09-28'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: N-PX 0002000324-26-003338
  url: https://www.sec.gov/Archives/edgar/data/1263994/000200032426003338/0002000324-26-003338-index.html
  published_at: '2026-08-07'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 3 0002143813-26-000001
  url: https://www.sec.gov/Archives/edgar/data/1263994/000214381326000001/0002143813-26-000001-index.html
  published_at: '2026-07-07'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: N-CSRS 0001999371-26-014196
  url: https://www.sec.gov/Archives/edgar/data/1263994/000199937126014196/0001999371-26-014196-index.html
  published_at: '2026-07-02'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 4 0001717520-26-000001
  url: https://www.sec.gov/Archives/edgar/data/1263994/000171752026000001/0001717520-26-000001-index.html
  published_at: '2026-06-26'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0001263994
  classification_status: missing_or_invalid_sic
  entity_type: other
  name: REAVES UTILITY INCOME FUND
  sic: null
  sic_description: ''
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 80998351faf66f6076d3f07af7cbbb9ee632e7f03221880d8644e12cc68242b1
  url: https://data.sec.gov/submissions/CIK0001263994.json
listings:
- ticker: UTG
  exchange: NYSE_AMERICAN
  instrument_type: common_stock
research_filings:
- accession: 0001999371-26-003335
  filed: '2026-02-13'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/1263994/000199937126003335/0001999371-26-003335-index.html
- accession: 0001999371-24-003422
  filed: '2024-03-12'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/1263994/000199937124003422/0001999371-24-003422-index.html
research_progress:
  stage: pending
  input_sha256: ff729f332b3575235223cdb527f8b366664c6408e57f0d79200419fd045100f8
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
full_history_url: https://github.com/eladyesh/stock-brain/blob/c6b3af0cefe967faceb0323aa590d422e87cbc29/brain/companies/UTG/README.md
full_history_commit: c6b3af0cefe967faceb0323aa590d422e87cbc29
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# UTG — REAVES UTILITY INCOME FUND

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/c6b3af0cefe967faceb0323aa590d422e87cbc29/brain/companies/UTG/README.md)

## Business overview

Reported issuer name: **REAVES UTILITY INCOME FUND**. Stable SEC CIK: **0001263994**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| UTG | NYSE_AMERICAN | common_stock | 1 | [S01] |

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
- Forms observed in the retained filing inventory: 3, 3/A, 4, 4/A, 40-17G, 40-17G/A, 40-6C, 40-6C/A, 40-APP/A, 424B3, 424B5, 497, 497AD, 5, 5/A, 8-A12B, 8-K, APP NTC, APP ORDR, CERTAMX, CORRESP, DEF 14A, DEFA14A, DEFR14A, EFFECT, N-2, N-2/A, N-23C-2, N-2ASR, N-8A, N-CEN, N-CSR, N-CSR/A, N-CSRS, N-CSRS/A, N-PX, N-PX/A, N-Q, NPORT-EX, NPORT-P, NSAR-A, NSAR-B, NSAR-B/A, POS AMI, POS EX, PRE 14A, RW, SC 13G, SC 13G/A, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:32:16.551800+00:00.

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
| 2026-09-28 | NPORT-P | 0001263994-26-000021 | — | [S03] |
| 2026-08-07 | N-PX | 0002000324-26-003338 | — | [S04] |
| 2026-07-07 | 3 | 0002143813-26-000001 | — | [S05] |
| 2026-07-02 | N-CSRS | 0001999371-26-014196 | — | [S06] |
| 2026-06-26 | 4 | 0001717520-26-000001 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-25T13:45:48.334682+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001263994.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [NPORT-P 0001263994-26-000021](https://www.sec.gov/Archives/edgar/data/1263994/000126399426000021/0001263994-26-000021-index.html) — published 2026-09-28; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [N-PX 0002000324-26-003338](https://www.sec.gov/Archives/edgar/data/1263994/000200032426003338/0002000324-26-003338-index.html) — published 2026-08-07; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [3 0002143813-26-000001](https://www.sec.gov/Archives/edgar/data/1263994/000214381326000001/0002143813-26-000001-index.html) — published 2026-07-07; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [N-CSRS 0001999371-26-014196](https://www.sec.gov/Archives/edgar/data/1263994/000199937126014196/0001999371-26-014196-index.html) — published 2026-07-02; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [4 0001717520-26-000001](https://www.sec.gov/Archives/edgar/data/1263994/000171752026000001/0001717520-26-000001-index.html) — published 2026-06-26; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261025-40199010718-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/c6b3af0cefe967faceb0323aa590d422e87cbc29/brain/companies/UTG/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
