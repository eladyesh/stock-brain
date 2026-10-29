---
schema_version: 1
document_type: company_facts
company_id: company-cik-0000075398
cik: 0000075398
company_name: Western Asset Investment Grade Income Fund Inc.
tickers:
- PAI
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
  - 4/A
  - 40-17G
  - 40-17G/A
  - 8-K
  - CORRESP
  - DEF 14A
  - DEFA14A
  - N-30D
  - N-CEN
  - N-CSR
  - N-CSR/A
  - N-CSRS
  - N-PX
  - N-Q
  - NPORT-EX
  - NPORT-P
  - NSAR-A
  - NSAR-B
  - NSAR-B/A
  - NTFNCSR
  - PRE 14A
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13G/A
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0000075398.json
    sha256: 1fc15a2afe471f2a410b4ab24864a4f6a3a28caba3ccf43e26196efc9a7b7b98
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0000075398.json
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
  url: https://data.sec.gov/submissions/CIK0000075398.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 1fc15a2afe471f2a410b4ab24864a4f6a3a28caba3ccf43e26196efc9a7b7b98
- id: S03
  title: NPORT-P 0000940400-26-034744
  url: https://www.sec.gov/Archives/edgar/data/75398/000094040026034744/0000940400-26-034744-index.html
  published_at: '2026-08-26'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: N-CSRS 0001133228-26-011557
  url: https://www.sec.gov/Archives/edgar/data/75398/000113322826011557/0001133228-26-011557-index.html
  published_at: '2026-08-25'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: N-PX 0001193125-26-351336
  url: https://www.sec.gov/Archives/edgar/data/75398/000119312526351336/0001193125-26-351336-index.html
  published_at: '2026-08-14'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: SCHEDULE 13G/A 0001172661-26-003707
  url: https://www.sec.gov/Archives/edgar/data/75398/000117266126003707/0001172661-26-003707-index.html
  published_at: '2026-08-14'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: NPORT-P 0000940400-26-021642
  url: https://www.sec.gov/Archives/edgar/data/75398/000094040026021642/0000940400-26-021642-index.html
  published_at: '2026-05-28'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0000075398
  classification_status: missing_or_invalid_sic
  entity_type: other
  name: Western Asset Investment Grade Income Fund Inc.
  sic: null
  sic_description: ''
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 1fc15a2afe471f2a410b4ab24864a4f6a3a28caba3ccf43e26196efc9a7b7b98
  url: https://data.sec.gov/submissions/CIK0000075398.json
listings:
- ticker: PAI
  exchange: NYSE
  instrument_type: equity_candidate
research_filings:
- accession: 0001193125-26-161602
  filed: '2026-04-17'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/75398/000119312526161602/0001193125-26-161602-index.html
- accession: 0001193125-20-286386
  filed: '2020-11-05'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/75398/000119312520286386/0001193125-20-286386-index.html
research_progress:
  stage: pending
  input_sha256: 99dff845d46c6370605fe9088169e8b430096a9b1246d6c0cdb7784031f0bdb9
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
full_history_url: https://github.com/eladyesh/stock-brain/blob/c26f59bc72c00102d2490e95b07449f8cd848491/brain/companies/PAI/README.md
full_history_commit: c26f59bc72c00102d2490e95b07449f8cd848491
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# PAI — Western Asset Investment Grade Income Fund Inc.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/c26f59bc72c00102d2490e95b07449f8cd848491/brain/companies/PAI/README.md)

## Business overview

Reported issuer name: **Western Asset Investment Grade Income Fund Inc.**. Stable SEC CIK: **0000075398**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| PAI | NYSE | equity_candidate | 1 | [S01] |

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
- Forms observed in the retained filing inventory: 3, 4, 4/A, 40-17G, 40-17G/A, 8-K, CORRESP, DEF 14A, DEFA14A, N-30D, N-CEN, N-CSR, N-CSR/A, N-CSRS, N-PX, N-Q, NPORT-EX, NPORT-P, NSAR-A, NSAR-B, NSAR-B/A, NTFNCSR, PRE 14A, SC 13G, SC 13G/A, SCHEDULE 13G/A
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:27:57.527218+00:00.

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
| 2026-08-26 | NPORT-P | 0000940400-26-034744 | — | [S03] |
| 2026-08-25 | N-CSRS | 0001133228-26-011557 | — | [S04] |
| 2026-08-14 | N-PX | 0001193125-26-351336 | — | [S05] |
| 2026-08-14 | SCHEDULE 13G/A | 0001172661-26-003707 | — | [S06] |
| 2026-05-28 | NPORT-P | 0000940400-26-021642 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-29T16:14:13.951866+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0000075398.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [NPORT-P 0000940400-26-034744](https://www.sec.gov/Archives/edgar/data/75398/000094040026034744/0000940400-26-034744-index.html) — published 2026-08-26; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [N-CSRS 0001133228-26-011557](https://www.sec.gov/Archives/edgar/data/75398/000113322826011557/0001133228-26-011557-index.html) — published 2026-08-25; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [N-PX 0001193125-26-351336](https://www.sec.gov/Archives/edgar/data/75398/000119312526351336/0001193125-26-351336-index.html) — published 2026-08-14; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [SCHEDULE 13G/A 0001172661-26-003707](https://www.sec.gov/Archives/edgar/data/75398/000117266126003707/0001172661-26-003707-index.html) — published 2026-08-14; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [NPORT-P 0000940400-26-021642](https://www.sec.gov/Archives/edgar/data/75398/000094040026021642/0000940400-26-021642-index.html) — published 2026-05-28; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261029-40909364006-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/c26f59bc72c00102d2490e95b07449f8cd848491/brain/companies/PAI/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
