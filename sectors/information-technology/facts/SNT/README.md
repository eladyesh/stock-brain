---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001993727
cik: 0001993727
company_name: Senstar Technologies Corp
tickers:
- SNT
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
  reason: foreign_reporting_adapter
  next_action: Add support for the observed 20-F, 40-F or 6-K reporting forms and
    verify the actual accounting taxonomy before normalization.
  observed_forms:
  - '144'
  - 20-F
  - 20-F/A
  - '3'
  - 424B3
  - 6-K
  - 8-K12B
  - CORRESP
  - EFFECT
  - F-4
  - F-4/A
  - NT 20-F
  - S-8
  - SD
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001993727.json
    sha256: e4479ecaed635ba22a4051adf63ca27aac29d49797c79e09ed6c198efaa55722
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001993727.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: nasdaqlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt
  published_at: null
  retrieved_at: '2026-10-30T16:00:11.183681+00:00'
  sha256: 64301e84a89de015f12206ec26fa4a677c38e33277e47d0b3a6b91e370e8d274
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001993727.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: e4479ecaed635ba22a4051adf63ca27aac29d49797c79e09ed6c198efaa55722
- id: S03
  title: 6-K 0001178913-26-004247
  url: https://www.sec.gov/Archives/edgar/data/1993727/000117891326004247/0001178913-26-004247-index.html
  published_at: '2026-08-25'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 6-K 0001178913-26-003361
  url: https://www.sec.gov/Archives/edgar/data/1993727/000117891326003361/0001178913-26-003361-index.html
  published_at: '2026-06-29'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 6-K 0001178913-26-003120
  url: https://www.sec.gov/Archives/edgar/data/1993727/000117891326003120/0001178913-26-003120-index.html
  published_at: '2026-06-05'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: SD 0001178913-26-002979
  url: https://www.sec.gov/Archives/edgar/data/1993727/000117891326002979/0001178913-26-002979-index.html
  published_at: '2026-05-28'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 6-K 0001178913-26-002952
  url: https://www.sec.gov/Archives/edgar/data/1993727/000117891326002952/0001178913-26-002952-index.html
  published_at: '2026-05-28'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0001993727
  classification_status: reported_sic
  entity_type: other
  name: Senstar Technologies Corp
  sic: '3669'
  sic_description: Communications Equipment, NEC
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: e4479ecaed635ba22a4051adf63ca27aac29d49797c79e09ed6c198efaa55722
  url: https://data.sec.gov/submissions/CIK0001993727.json
listings:
- ticker: SNT
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001178913-26-002328
  filed: '2026-05-04'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1993727/000117891326002328/0001178913-26-002328-index.html
- accession: 0001178913-26-002698
  filed: '2026-05-14'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1993727/000117891326002698/0001178913-26-002698-index.html
- accession: 0001178913-26-004247
  filed: '2026-08-25'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1993727/000117891326004247/0001178913-26-004247-index.html
research_progress:
  stage: pending
  input_sha256: 0af0eb5aa3e3d7949103bc08ab93bc9c9858bb46f2e29e80b365baca552e33a2
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
  sic: '3669'
  sic_description: Communications Equipment, NEC
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001993727.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/79888139fa1fe8ad3404e6bc04e318eee1474f73/brain/companies/SNT/README.md
full_history_commit: 79888139fa1fe8ad3404e6bc04e318eee1474f73
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# SNT — Senstar Technologies Corp

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/79888139fa1fe8ad3404e6bc04e318eee1474f73/brain/companies/SNT/README.md)

## Business overview

Reported issuer name: **Senstar Technologies Corp**. Stable SEC CIK: **0001993727**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| SNT | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **3669**: Communications Equipment, NEC. [S02]

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
- Forms observed in the retained filing inventory: 144, 20-F, 20-F/A, 3, 424B3, 6-K, 8-K12B, CORRESP, EFFECT, F-4, F-4/A, NT 20-F, S-8, SD, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:36:30.480749+00:00.

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
| 2026-08-25 | 6-K | 0001178913-26-004247 | — | [S03] |
| 2026-06-29 | 6-K | 0001178913-26-003361 | — | [S04] |
| 2026-06-05 | 6-K | 0001178913-26-003120 | — | [S05] |
| 2026-05-28 | SD | 0001178913-26-002979 | — | [S06] |
| 2026-05-28 | 6-K | 0001178913-26-002952 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-30T16:00:11.183681+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001993727.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [6-K 0001178913-26-004247](https://www.sec.gov/Archives/edgar/data/1993727/000117891326004247/0001178913-26-004247-index.html) — published 2026-08-25; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [6-K 0001178913-26-003361](https://www.sec.gov/Archives/edgar/data/1993727/000117891326003361/0001178913-26-003361-index.html) — published 2026-06-29; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [6-K 0001178913-26-003120](https://www.sec.gov/Archives/edgar/data/1993727/000117891326003120/0001178913-26-003120-index.html) — published 2026-06-05; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [SD 0001178913-26-002979](https://www.sec.gov/Archives/edgar/data/1993727/000117891326002979/0001178913-26-002979-index.html) — published 2026-05-28; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [6-K 0001178913-26-002952](https://www.sec.gov/Archives/edgar/data/1993727/000117891326002952/0001178913-26-002952-index.html) — published 2026-05-28; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261030-41085569265-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/79888139fa1fe8ad3404e6bc04e318eee1474f73/brain/companies/SNT/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
