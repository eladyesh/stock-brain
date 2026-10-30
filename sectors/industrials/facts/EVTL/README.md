---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001867102
cik: 0001867102
company_name: Vertical Aerospace Ltd.
tickers:
- EVTL
status: stub
canonical_reviewed: false
as_of: '2026-10-30'
updated_at: '2026-10-30T16:05:25.650854+00:00'
reviewed_at: null
coverage_release: coverage-20261030-41085569265-1
source_commit: f9a34108789a82bf7c75f9d65a0e9552aa5552db
financial_history_available: false
curated_research: null
financial_gap:
  reason: foreign_reporting_adapter
  next_action: Add support for the observed 20-F, 40-F or 6-K reporting forms and
    verify the actual accounting taxonomy before normalization.
  observed_forms:
  - '144'
  - 144/A
  - 20-F
  - 25-NSE
  - '3'
  - '4'
  - 424B3
  - 424B5
  - '425'
  - 6-K
  - 6-K/A
  - 8-A12B
  - CERT
  - CORRESP
  - EFFECT
  - F-1
  - F-3
  - F-3/A
  - F-3MEF
  - F-4
  - F-4/A
  - FWP
  - POS AM
  - POS EX
  - S-8
  - S-8 POS
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13D/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - SEC STAFF LETTER
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001867102.json
    sha256: c0e8b8b39a5294e84dc1c9968769b47532a0c31fff34b13b7ca3e4b441d05c4d
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001867102.json
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
  url: https://data.sec.gov/submissions/CIK0001867102.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: c0e8b8b39a5294e84dc1c9968769b47532a0c31fff34b13b7ca3e4b441d05c4d
- id: S03
  title: 6-K 0001104659-26-118145
  url: https://www.sec.gov/Archives/edgar/data/1867102/000110465926118145/0001104659-26-118145-index.html
  published_at: '2026-10-22'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 6-K 0001104659-26-117549
  url: https://www.sec.gov/Archives/edgar/data/1867102/000110465926117549/0001104659-26-117549-index.html
  published_at: '2026-10-21'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 4 0001104659-26-116675
  url: https://www.sec.gov/Archives/edgar/data/1867102/000110465926116675/0001104659-26-116675-index.html
  published_at: '2026-10-16'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 6-K 0001104659-26-116373
  url: https://www.sec.gov/Archives/edgar/data/1867102/000110465926116373/0001104659-26-116373-index.html
  published_at: '2026-10-16'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 3 0001104659-26-115669
  url: https://www.sec.gov/Archives/edgar/data/1867102/000110465926115669/0001104659-26-115669-index.html
  published_at: '2026-10-13'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0001867102
  classification_status: reported_sic
  entity_type: other
  name: Vertical Aerospace Ltd.
  sic: '3721'
  sic_description: Aircraft
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: c0e8b8b39a5294e84dc1c9968769b47532a0c31fff34b13b7ca3e4b441d05c4d
  url: https://data.sec.gov/submissions/CIK0001867102.json
listings:
- ticker: EVTL
  exchange: NYSE
  instrument_type: common_stock
research_filings:
- accession: 0001104659-26-033487
  filed: '2026-03-24'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1867102/000110465926033487/0001104659-26-033487-index.html
- accession: 0001104659-26-118145
  filed: '2026-10-22'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1867102/000110465926118145/0001104659-26-118145-index.html
- accession: 0001104659-25-105893
  filed: '2025-11-04'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1867102/000110465925105893/0001104659-25-105893-index.html
- accession: 0001104659-25-000052
  filed: '2025-01-02'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1867102/000110465925000052/0001104659-25-000052-index.html
- accession: 0001104659-24-027114
  filed: '2024-02-23'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1867102/000110465924027114/0001104659-24-027114-index.html
- accession: 0001104659-21-150946
  filed: '2021-12-17'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1867102/000110465921150946/0001104659-21-150946-index.html
research_progress:
  stage: pending
  input_sha256: 1b9242890e7337fcdd241a840693504fdac7fddc872831af116c7b6bc626f77d
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
  derived_observations: 0
  model_draft: false
  reviewed: false
sector_assignment:
  sector: industrials
  method: project_sic_rule
  sic: '3721'
  sic_description: Aircraft
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001867102.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/1b4771bc41dec553e210323f72d9bfc908288c04/brain/companies/EVTL/README.md
full_history_commit: 1b4771bc41dec553e210323f72d9bfc908288c04
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# EVTL — Vertical Aerospace Ltd.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/1b4771bc41dec553e210323f72d9bfc908288c04/brain/companies/EVTL/README.md)

## Business overview

Reported issuer name: **Vertical Aerospace Ltd.**. Stable SEC CIK: **0001867102**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| EVTL | NYSE | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **3721**: Aircraft. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **industrials**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

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
- Forms observed in the retained filing inventory: 144, 144/A, 20-F, 25-NSE, 3, 4, 424B3, 424B5, 425, 6-K, 6-K/A, 8-A12B, CERT, CORRESP, EFFECT, F-1, F-3, F-3/A, F-3MEF, F-4, F-4/A, FWP, POS AM, POS EX, S-8, S-8 POS, SC 13D, SC 13D/A, SC 13G, SC 13G/A, SCHEDULE 13D/A, SCHEDULE 13G, SCHEDULE 13G/A, SEC STAFF LETTER, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:36:14.646923+00:00.

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
| 2026-10-22 | 6-K | 0001104659-26-118145 | — | [S03] |
| 2026-10-21 | 6-K | 0001104659-26-117549 | — | [S04] |
| 2026-10-16 | 4 | 0001104659-26-116675 | — | [S05] |
| 2026-10-16 | 6-K | 0001104659-26-116373 | — | [S06] |
| 2026-10-13 | 3 | 0001104659-26-115669 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-30T16:00:12.358089+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001867102.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [6-K 0001104659-26-118145](https://www.sec.gov/Archives/edgar/data/1867102/000110465926118145/0001104659-26-118145-index.html) — published 2026-10-22; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [6-K 0001104659-26-117549](https://www.sec.gov/Archives/edgar/data/1867102/000110465926117549/0001104659-26-117549-index.html) — published 2026-10-21; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [4 0001104659-26-116675](https://www.sec.gov/Archives/edgar/data/1867102/000110465926116675/0001104659-26-116675-index.html) — published 2026-10-16; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [6-K 0001104659-26-116373](https://www.sec.gov/Archives/edgar/data/1867102/000110465926116373/0001104659-26-116373-index.html) — published 2026-10-16; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [3 0001104659-26-115669](https://www.sec.gov/Archives/edgar/data/1867102/000110465926115669/0001104659-26-115669-index.html) — published 2026-10-13; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261030-41085569265-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/1b4771bc41dec553e210323f72d9bfc908288c04/brain/companies/EVTL/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
