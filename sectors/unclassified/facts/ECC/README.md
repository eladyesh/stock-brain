---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001604174
cik: '0001604174'
company_name: Eagle Point Credit Co
tickers:
- ECC
status: stub
canonical_reviewed: false
as_of: '2026-10-30'
updated_at: '2026-10-30T16:05:25.650854+00:00'
reviewed_at: null
coverage_release: coverage-20261030-41085569265-1
source_commit: ef2ed016c2c344c23ee7fb991b25bf93660da77e
financial_history_available: false
curated_research: null
financial_gap:
  reason: fund_reporting_review
  next_action: Review the instrument against its N-CSR/N-CSRS reporting evidence before
    applying an operating-company model. This signal alone is not a final fund classification.
  observed_forms:
  - 25-NSE
  - 25-NSE/A
  - '3'
  - 3/A
  - 305B2
  - '4'
  - 4/A
  - 40-17G
  - 40-17G/A
  - 40-APP
  - 40-APP/A
  - 424B2
  - 424B3
  - 424B5
  - 486BPOS
  - '497'
  - 497AD
  - 8-A12B
  - 8-K
  - APP NTC
  - APP ORDR
  - AW
  - CERT
  - CERTNYS
  - CORRESP
  - DEF 14A
  - DEFA14A
  - EFFECT
  - FWP
  - N-2
  - N-2 POSASR
  - N-2/A
  - N-23C-2
  - N-2ASR
  - N-2MEF
  - N-30B-2
  - N-8A
  - N-8A/A
  - N-CEN
  - N-CSR
  - N-CSR/A
  - N-CSRS
  - N-CSRS/A
  - N-PX
  - N-Q
  - NPORT-P
  - NSAR-A
  - NSAR-B
  - NSAR-B/A
  - POS 8C
  - POS EX
  - PRE 14A
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001604174.json
    sha256: befb97389f682a9b588308c362624e878268938aec1561b1ca2c410095ebdfa6
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001604174.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: otherlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt
  published_at: null
  retrieved_at: '2026-10-30T16:00:12.358089+00:00'
  sha256: a960a0bfc5439fac9e467fe07ef1f44afe893ba2afc3297648321a80ce09971e
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001604174.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: befb97389f682a9b588308c362624e878268938aec1561b1ca2c410095ebdfa6
- id: S03
  title: 497AD 0001104659-26-116604
  url: https://www.sec.gov/Archives/edgar/data/1604174/000110465926116604/0001104659-26-116604-index.html
  published_at: '2026-10-16'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 8-K 0001104659-26-115755
  url: https://www.sec.gov/Archives/edgar/data/1604174/000110465926115755/0001104659-26-115755-index.html
  published_at: '2026-10-14'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 497AD 0001104659-26-108241
  url: https://www.sec.gov/Archives/edgar/data/1604174/000110465926108241/0001104659-26-108241-index.html
  published_at: '2026-09-16'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 8-K 0001104659-26-107566
  url: https://www.sec.gov/Archives/edgar/data/1604174/000110465926107566/0001104659-26-107566-index.html
  published_at: '2026-09-14'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: NPORT-P 0001104659-26-103270
  url: https://www.sec.gov/Archives/edgar/data/1604174/000110465926103270/0001104659-26-103270-index.html
  published_at: '2026-08-28'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: '0001604174'
  classification_status: missing_or_invalid_sic
  entity_type: other
  name: Eagle Point Credit Co
  sic: null
  sic_description: ''
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: befb97389f682a9b588308c362624e878268938aec1561b1ca2c410095ebdfa6
  url: https://data.sec.gov/submissions/CIK0001604174.json
listings:
- ticker: ECC
  exchange: NYSE
  instrument_type: equity_candidate
research_filings:
- accession: 0001104659-26-039960
  filed: '2026-04-06'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/1604174/000110465926039960/0001104659-26-039960-index.html
- accession: 0001104659-26-115755
  filed: '2026-10-14'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/1604174/000110465926115755/0001104659-26-115755-index.html
research_progress:
  stage: pending
  input_sha256: e61c5084e38c597fca827620b571798508aa35567c46b8611b91c3cc774c6d99
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
full_history_url: https://github.com/eladyesh/stock-brain/blob/79888139fa1fe8ad3404e6bc04e318eee1474f73/brain/companies/ECC/README.md
full_history_commit: 79888139fa1fe8ad3404e6bc04e318eee1474f73
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# ECC — Eagle Point Credit Co

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/79888139fa1fe8ad3404e6bc04e318eee1474f73/brain/companies/ECC/README.md)

## Business overview

Reported issuer name: **Eagle Point Credit Co**. Stable SEC CIK: **0001604174**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| ECC | NYSE | equity_candidate | 1 | [S01] |

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
- Forms observed in the retained filing inventory: 25-NSE, 25-NSE/A, 3, 3/A, 305B2, 4, 4/A, 40-17G, 40-17G/A, 40-APP, 40-APP/A, 424B2, 424B3, 424B5, 486BPOS, 497, 497AD, 8-A12B, 8-K, APP NTC, APP ORDR, AW, CERT, CERTNYS, CORRESP, DEF 14A, DEFA14A, EFFECT, FWP, N-2, N-2 POSASR, N-2/A, N-23C-2, N-2ASR, N-2MEF, N-30B-2, N-8A, N-8A/A, N-CEN, N-CSR, N-CSR/A, N-CSRS, N-CSRS/A, N-PX, N-Q, NPORT-P, NSAR-A, NSAR-B, NSAR-B/A, POS 8C, POS EX, PRE 14A, SC 13D, SC 13D/A, SC 13G, SC 13G/A, SCHEDULE 13G, SCHEDULE 13G/A, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:34:28.948966+00:00.

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
| 2026-10-16 | 497AD | 0001104659-26-116604 | — | [S03] |
| 2026-10-14 | 8-K | 0001104659-26-115755 | — | [S04] |
| 2026-09-16 | 497AD | 0001104659-26-108241 | — | [S05] |
| 2026-09-14 | 8-K | 0001104659-26-107566 | — | [S06] |
| 2026-08-28 | NPORT-P | 0001104659-26-103270 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-30T16:00:12.358089+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001604174.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [497AD 0001104659-26-116604](https://www.sec.gov/Archives/edgar/data/1604174/000110465926116604/0001104659-26-116604-index.html) — published 2026-10-16; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [8-K 0001104659-26-115755](https://www.sec.gov/Archives/edgar/data/1604174/000110465926115755/0001104659-26-115755-index.html) — published 2026-10-14; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [497AD 0001104659-26-108241](https://www.sec.gov/Archives/edgar/data/1604174/000110465926108241/0001104659-26-108241-index.html) — published 2026-09-16; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [8-K 0001104659-26-107566](https://www.sec.gov/Archives/edgar/data/1604174/000110465926107566/0001104659-26-107566-index.html) — published 2026-09-14; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [NPORT-P 0001104659-26-103270](https://www.sec.gov/Archives/edgar/data/1604174/000110465926103270/0001104659-26-103270-index.html) — published 2026-08-28; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261030-41085569265-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/79888139fa1fe8ad3404e6bc04e318eee1474f73/brain/companies/ECC/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
