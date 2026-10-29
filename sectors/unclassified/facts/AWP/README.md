---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001390195
cik: 0001390195
company_name: abrdn Global Premier Properties Fund
tickers:
- AWP
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
  - 40-17G
  - 40-APP
  - 40-APP/A
  - 424B2
  - 424B3
  - '497'
  - '5'
  - 8-A12B
  - 8-K
  - CERTNYS
  - CORRESP
  - DEF 14A
  - DEFA14A
  - DEFR14A
  - EFFECT
  - N-2
  - N-2/A
  - N-2MEF
  - N-8A
  - N-CEN
  - N-CEN/A
  - N-CSR
  - N-CSR/A
  - N-CSRS
  - N-PX
  - N-PX/A
  - N-Q
  - NPORT-EX
  - NPORT-P
  - NSAR-A
  - NSAR-B
  - PRE 14A
  - SC 13G
  - SC 13G/A
  - SC TO-C
  - SC TO-I
  - SC TO-I/A
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001390195.json
    sha256: 3a609d46550e70b5e567d82187280cc0ccb57169dfe47d5368cd319e5fddd4f3
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001390195.json
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
  url: https://data.sec.gov/submissions/CIK0001390195.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 3a609d46550e70b5e567d82187280cc0ccb57169dfe47d5368cd319e5fddd4f3
- id: S03
  title: NPORT-P 0001410368-26-101731
  url: https://www.sec.gov/Archives/edgar/data/1390195/000141036826101731/0001410368-26-101731-index.html
  published_at: '2026-09-29'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 40-17G 0001104659-26-110246
  url: https://www.sec.gov/Archives/edgar/data/1390195/000110465926110246/0001104659-26-110246-index.html
  published_at: '2026-09-24'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: N-PX 0001104659-26-099455
  url: https://www.sec.gov/Archives/edgar/data/1390195/000110465926099455/0001104659-26-099455-index.html
  published_at: '2026-08-21'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: N-CSRS 0001104659-26-082284
  url: https://www.sec.gov/Archives/edgar/data/1390195/000110465926082284/0001104659-26-082284-index.html
  published_at: '2026-07-09'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 424B3 0001104659-26-079867
  url: https://www.sec.gov/Archives/edgar/data/1390195/000110465926079867/0001104659-26-079867-index.html
  published_at: '2026-07-01'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0001390195
  classification_status: missing_or_invalid_sic
  entity_type: other
  name: abrdn Global Premier Properties Fund
  sic: null
  sic_description: ''
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 3a609d46550e70b5e567d82187280cc0ccb57169dfe47d5368cd319e5fddd4f3
  url: https://data.sec.gov/submissions/CIK0001390195.json
listings:
- ticker: AWP
  exchange: NYSE
  instrument_type: common_stock
research_filings:
- accession: 0001104659-26-040401
  filed: '2026-04-07'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/1390195/000110465926040401/0001104659-26-040401-index.html
- accession: 0001104659-26-038615
  filed: '2026-04-01'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/1390195/000110465926038615/0001104659-26-038615-index.html
research_progress:
  stage: pending
  input_sha256: ceb5dd2a5884e47dcefa21a2d0dc282e55457b64927c0d63149ed70a505a93ed
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
full_history_url: https://github.com/eladyesh/stock-brain/blob/c26f59bc72c00102d2490e95b07449f8cd848491/brain/companies/AWP/README.md
full_history_commit: c26f59bc72c00102d2490e95b07449f8cd848491
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# AWP — abrdn Global Premier Properties Fund

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/c26f59bc72c00102d2490e95b07449f8cd848491/brain/companies/AWP/README.md)

## Business overview

Reported issuer name: **abrdn Global Premier Properties Fund**. Stable SEC CIK: **0001390195**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| AWP | NYSE | common_stock | 1 | [S01] |

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
- Forms observed in the retained filing inventory: 3, 3/A, 4, 40-17G, 40-APP, 40-APP/A, 424B2, 424B3, 497, 5, 8-A12B, 8-K, CERTNYS, CORRESP, DEF 14A, DEFA14A, DEFR14A, EFFECT, N-2, N-2/A, N-2MEF, N-8A, N-CEN, N-CEN/A, N-CSR, N-CSR/A, N-CSRS, N-PX, N-PX/A, N-Q, NPORT-EX, NPORT-P, NSAR-A, NSAR-B, PRE 14A, SC 13G, SC 13G/A, SC TO-C, SC TO-I, SC TO-I/A
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:33:00.702306+00:00.

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
| 2026-09-29 | NPORT-P | 0001410368-26-101731 | — | [S03] |
| 2026-09-24 | 40-17G | 0001104659-26-110246 | — | [S04] |
| 2026-08-21 | N-PX | 0001104659-26-099455 | — | [S05] |
| 2026-07-09 | N-CSRS | 0001104659-26-082284 | — | [S06] |
| 2026-07-01 | 424B3 | 0001104659-26-079867 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-29T16:14:13.951866+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001390195.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [NPORT-P 0001410368-26-101731](https://www.sec.gov/Archives/edgar/data/1390195/000141036826101731/0001410368-26-101731-index.html) — published 2026-09-29; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [40-17G 0001104659-26-110246](https://www.sec.gov/Archives/edgar/data/1390195/000110465926110246/0001104659-26-110246-index.html) — published 2026-09-24; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [N-PX 0001104659-26-099455](https://www.sec.gov/Archives/edgar/data/1390195/000110465926099455/0001104659-26-099455-index.html) — published 2026-08-21; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [N-CSRS 0001104659-26-082284](https://www.sec.gov/Archives/edgar/data/1390195/000110465926082284/0001104659-26-082284-index.html) — published 2026-07-09; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [424B3 0001104659-26-079867](https://www.sec.gov/Archives/edgar/data/1390195/000110465926079867/0001104659-26-079867-index.html) — published 2026-07-01; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261029-40909364006-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/c26f59bc72c00102d2490e95b07449f8cd848491/brain/companies/AWP/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
