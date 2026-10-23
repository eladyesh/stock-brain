---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001342338
cik: 0001342338
company_name: Himax Technologies, Inc.
tickers:
- HIMX
status: stub
canonical_reviewed: false
as_of: '2026-10-23'
updated_at: '2026-10-23T14:35:22.252685+00:00'
reviewed_at: null
coverage_release: coverage-20261023-39968262770-1
source_commit: 3f697433c3580d4ca83edbe44c66580ac926c8d7
financial_history_available: false
curated_research: null
financial_gap:
  reason: foreign_reporting_adapter
  next_action: Add support for the observed 20-F, 40-F or 6-K reporting forms and
    verify the actual accounting taxonomy before normalization.
  observed_forms:
  - 20-F
  - 20-F/A
  - '3'
  - '4'
  - 424B1
  - 424B3
  - 6-K
  - 6-K/A
  - 8-A12G
  - CORRESP
  - CT ORDER
  - EFFECT
  - F-1
  - F-1/A
  - F-3
  - F-6
  - F-6 POS
  - FWP
  - NT 20-F
  - RW
  - S-8
  - S-8 POS
  - SC 13G
  - SC 13G/A
  - SD
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001342338.json
    sha256: 3d46f4e4fd596ac09694eaf209ce7c486b49deff62b41ea15ca64547515b0701
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001342338.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: nasdaqlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt
  published_at: null
  retrieved_at: '2026-10-23T14:17:54.530395+00:00'
  sha256: a31379ea4791bd232005b22547c9cfa517e0cb9e9f14ff7091be845f143d5c71
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001342338.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 3d46f4e4fd596ac09694eaf209ce7c486b49deff62b41ea15ca64547515b0701
- id: S03
  title: 4 0001171843-26-006302
  url: https://www.sec.gov/Archives/edgar/data/1342338/000117184326006302/0001171843-26-006302-index.html
  published_at: '2026-09-30'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 4 0001171843-26-006301
  url: https://www.sec.gov/Archives/edgar/data/1342338/000117184326006301/0001171843-26-006301-index.html
  published_at: '2026-09-30'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 4 0001171843-26-006228
  url: https://www.sec.gov/Archives/edgar/data/1342338/000117184326006228/0001171843-26-006228-index.html
  published_at: '2026-09-25'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 4 0001171843-26-006227
  url: https://www.sec.gov/Archives/edgar/data/1342338/000117184326006227/0001171843-26-006227-index.html
  published_at: '2026-09-25'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 6-K 0001171843-26-005436
  url: https://www.sec.gov/Archives/edgar/data/1342338/000117184326005436/0001171843-26-005436-index.html
  published_at: '2026-08-12'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0001342338
  classification_status: reported_sic
  entity_type: other
  name: Himax Technologies, Inc.
  sic: '3674'
  sic_description: Semiconductors & Related Devices
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 3d46f4e4fd596ac09694eaf209ce7c486b49deff62b41ea15ca64547515b0701
  url: https://data.sec.gov/submissions/CIK0001342338.json
listings:
- ticker: HIMX
  exchange: NASDAQ
  instrument_type: depositary_receipt
research_filings:
- accession: 0001104659-26-035507
  filed: '2026-03-27'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1342338/000110465926035507/0001104659-26-035507-index.html
- accession: 0001144204-13-030550
  filed: '2013-05-20'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1342338/000114420413030550/0001144204-13-030550-index.html
- accession: 0001171843-12-002670
  filed: '2012-07-24'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1342338/000117184312002670/0001171843-12-002670-index.html
- accession: 0001171843-12-002523
  filed: '2012-07-11'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1342338/000117184312002523/0001171843-12-002523-index.html
- accession: 0001144204-12-026174
  filed: '2012-05-04'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1342338/000114420412026174/0001144204-12-026174-index.html
- accession: 0001171843-26-005436
  filed: '2026-08-12'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1342338/000117184326005436/0001171843-26-005436-index.html
- accession: 0001171843-12-002674
  filed: '2012-07-24'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1342338/000117184312002674/0001171843-12-002674-index.html
research_progress:
  stage: pending
  input_sha256: 6b06f069afec1ffd9af2ea899463e4deb91d8afc348f0ed74dd88cc45d3d2cff
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
  derived_observations: 0
  model_draft: false
  reviewed: false
sector_assignment:
  sector: information-technology
  method: project_sic_rule
  sic: '3674'
  sic_description: Semiconductors & Related Devices
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001342338.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/d523cff21b18141b9a37cddd98ad6af6e1a30fa5/brain/companies/HIMX/README.md
full_history_commit: d523cff21b18141b9a37cddd98ad6af6e1a30fa5
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# HIMX — Himax Technologies, Inc.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/d523cff21b18141b9a37cddd98ad6af6e1a30fa5/brain/companies/HIMX/README.md)

## Business overview

Reported issuer name: **Himax Technologies, Inc.**. Stable SEC CIK: **0001342338**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| HIMX | NASDAQ | depositary_receipt | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **3674**: Semiconductors & Related Devices. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **information-technology**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

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
- Forms observed in the retained filing inventory: 20-F, 20-F/A, 3, 4, 424B1, 424B3, 6-K, 6-K/A, 8-A12G, CORRESP, CT ORDER, EFFECT, F-1, F-1/A, F-3, F-6, F-6 POS, FWP, NT 20-F, RW, S-8, S-8 POS, SC 13G, SC 13G/A, SD, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-23T14:29:14.846323+00:00.

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
| 2026-09-30 | 4 | 0001171843-26-006302 | — | [S03] |
| 2026-09-30 | 4 | 0001171843-26-006301 | — | [S04] |
| 2026-09-25 | 4 | 0001171843-26-006228 | — | [S05] |
| 2026-09-25 | 4 | 0001171843-26-006227 | — | [S06] |
| 2026-08-12 | 6-K | 0001171843-26-005436 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-23T14:17:54.530395+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001342338.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [4 0001171843-26-006302](https://www.sec.gov/Archives/edgar/data/1342338/000117184326006302/0001171843-26-006302-index.html) — published 2026-09-30; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [4 0001171843-26-006301](https://www.sec.gov/Archives/edgar/data/1342338/000117184326006301/0001171843-26-006301-index.html) — published 2026-09-30; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [4 0001171843-26-006228](https://www.sec.gov/Archives/edgar/data/1342338/000117184326006228/0001171843-26-006228-index.html) — published 2026-09-25; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [4 0001171843-26-006227](https://www.sec.gov/Archives/edgar/data/1342338/000117184326006227/0001171843-26-006227-index.html) — published 2026-09-25; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [6-K 0001171843-26-005436](https://www.sec.gov/Archives/edgar/data/1342338/000117184326005436/0001171843-26-005436-index.html) — published 2026-08-12; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261023-39968262770-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/d523cff21b18141b9a37cddd98ad6af6e1a30fa5/brain/companies/HIMX/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
