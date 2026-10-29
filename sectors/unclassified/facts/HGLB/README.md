---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001622148
cik: 0001622148
company_name: HIGHLAND GLOBAL ALLOCATION FUND
tickers:
- HGLB
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
  - '4'
  - 40-17G
  - 40-APP
  - 424B3
  - 8-A12B
  - 8-K
  - APP WD
  - AW
  - CERT
  - CORRESP
  - DEF 14A
  - DEFR14A
  - DEL AM
  - EFFECT
  - N-1A
  - N-2
  - N-2/A
  - N-8A
  - N-CEN
  - N-CSR
  - N-CSR/A
  - N-CSRS
  - N-PX
  - NPORT-EX
  - NPORT-P
  - NPORT-P/A
  - POS 8C
  - SC 13G
  - SCHEDULE 13G/A
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001622148.json
    sha256: 8b60d976757fa173c4fc9fab48eb32774358f6aa745b96bef37ccb6da2b9bd7d
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001622148.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
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
  url: https://data.sec.gov/submissions/CIK0001622148.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 8b60d976757fa173c4fc9fab48eb32774358f6aa745b96bef37ccb6da2b9bd7d
- id: S03
  title: NPORT-P/A 0002048251-26-007606
  url: https://www.sec.gov/Archives/edgar/data/1622148/000204825126007606/0002048251-26-007606-index.html
  published_at: '2026-09-02'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: NPORT-P 0002048251-26-007596
  url: https://www.sec.gov/Archives/edgar/data/1622148/000204825126007596/0002048251-26-007596-index.html
  published_at: '2026-08-31'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: N-PX 0001438934-26-000896
  url: https://www.sec.gov/Archives/edgar/data/1622148/000143893426000896/0001438934-26-000896-index.html
  published_at: '2026-08-17'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: SCHEDULE 13G/A 0001084208-26-000007
  url: https://www.sec.gov/Archives/edgar/data/1622148/000108420826000007/0001084208-26-000007-index.html
  published_at: '2026-08-03'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: APP WD 0000898432-26-000562
  url: https://www.sec.gov/Archives/edgar/data/1622148/000089843226000562/0000898432-26-000562-index.html
  published_at: '2026-07-29'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0001622148
  classification_status: missing_or_invalid_sic
  entity_type: investment
  name: HIGHLAND GLOBAL ALLOCATION FUND
  sic: null
  sic_description: ''
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 8b60d976757fa173c4fc9fab48eb32774358f6aa745b96bef37ccb6da2b9bd7d
  url: https://data.sec.gov/submissions/CIK0001622148.json
listings:
- ticker: HGLB
  exchange: NYSE
  instrument_type: common_stock
research_filings:
- accession: 0001193125-26-211603
  filed: '2026-05-07'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/1622148/000119312526211603/0001193125-26-211603-index.html
- accession: 0001193125-26-026847
  filed: '2026-01-28'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/1622148/000119312526026847/0001193125-26-026847-index.html
research_progress:
  stage: pending
  input_sha256: f845a4a9e7cd00d08e6927d3503850952993af83a1db66641e862f19b32bf430
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
full_history_url: https://github.com/eladyesh/stock-brain/blob/c26f59bc72c00102d2490e95b07449f8cd848491/brain/companies/HGLB/README.md
full_history_commit: c26f59bc72c00102d2490e95b07449f8cd848491
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# HGLB — HIGHLAND GLOBAL ALLOCATION FUND

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/c26f59bc72c00102d2490e95b07449f8cd848491/brain/companies/HGLB/README.md)

## Business overview

Reported issuer name: **HIGHLAND GLOBAL ALLOCATION FUND**. Stable SEC CIK: **0001622148**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| HGLB | NYSE | common_stock | 1 | [S01] |

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
- Forms observed in the retained filing inventory: 3, 4, 40-17G, 40-APP, 424B3, 8-A12B, 8-K, APP WD, AW, CERT, CORRESP, DEF 14A, DEFR14A, DEL AM, EFFECT, N-1A, N-2, N-2/A, N-8A, N-CEN, N-CSR, N-CSR/A, N-CSRS, N-PX, NPORT-EX, NPORT-P, NPORT-P/A, POS 8C, SC 13G, SCHEDULE 13G/A
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:34:36.569798+00:00.

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
| 2026-09-02 | NPORT-P/A | 0002048251-26-007606 | — | [S03] |
| 2026-08-31 | NPORT-P | 0002048251-26-007596 | — | [S04] |
| 2026-08-17 | N-PX | 0001438934-26-000896 | — | [S05] |
| 2026-08-03 | SCHEDULE 13G/A | 0001084208-26-000007 | — | [S06] |
| 2026-07-29 | APP WD | 0000898432-26-000562 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-29T16:14:13.951866+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001622148.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [NPORT-P/A 0002048251-26-007606](https://www.sec.gov/Archives/edgar/data/1622148/000204825126007606/0002048251-26-007606-index.html) — published 2026-09-02; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [NPORT-P 0002048251-26-007596](https://www.sec.gov/Archives/edgar/data/1622148/000204825126007596/0002048251-26-007596-index.html) — published 2026-08-31; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [N-PX 0001438934-26-000896](https://www.sec.gov/Archives/edgar/data/1622148/000143893426000896/0001438934-26-000896-index.html) — published 2026-08-17; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [SCHEDULE 13G/A 0001084208-26-000007](https://www.sec.gov/Archives/edgar/data/1622148/000108420826000007/0001084208-26-000007-index.html) — published 2026-08-03; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [APP WD 0000898432-26-000562](https://www.sec.gov/Archives/edgar/data/1622148/000089843226000562/0000898432-26-000562-index.html) — published 2026-07-29; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261029-40909364006-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/c26f59bc72c00102d2490e95b07449f8cd848491/brain/companies/HGLB/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
