---
schema_version: 1
document_type: company_facts
company_id: company-cik-0002025774
cik: '0002025774'
company_name: Alps Group Inc
tickers:
- ALPS
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
  - 20-F
  - '3'
  - 424B3
  - '425'
  - 6-K
  - 6-K/A
  - 8-A12B
  - CERT
  - CORRESP
  - DRS
  - DRS/A
  - DRSLTR
  - EFFECT
  - F-1
  - F-4
  - F-4/A
  - NT 20-F
  - SCHEDULE 13D
  - SCHEDULE 13G
  - SEC STAFF LETTER
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0002025774.json
    sha256: 5ac2542760ec756165b9e8633f1fa09e63f655ccb69678f4345371d76d6bbb5f
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0002025774.json
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
  url: https://data.sec.gov/submissions/CIK0002025774.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 5ac2542760ec756165b9e8633f1fa09e63f655ccb69678f4345371d76d6bbb5f
- id: S03
  title: 6-K 0001493152-26-047250
  url: https://www.sec.gov/Archives/edgar/data/2025774/000149315226047250/0001493152-26-047250-index.html
  published_at: '2026-10-15'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 6-K 0001493152-26-046334
  url: https://www.sec.gov/Archives/edgar/data/2025774/000149315226046334/0001493152-26-046334-index.html
  published_at: '2026-10-08'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 6-K 0001493152-26-036587
  url: https://www.sec.gov/Archives/edgar/data/2025774/000149315226036587/0001493152-26-036587-index.html
  published_at: '2026-08-07'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 20-F 0001493152-26-036364
  url: https://www.sec.gov/Archives/edgar/data/2025774/000149315226036364/0001493152-26-036364-index.html
  published_at: '2026-08-06'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: NT 20-F 0001493152-26-035650
  url: https://www.sec.gov/Archives/edgar/data/2025774/000149315226035650/0001493152-26-035650-index.html
  published_at: '2026-07-31'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: '0002025774'
  classification_status: reported_sic
  entity_type: other
  name: Alps Group Inc
  sic: '8000'
  sic_description: Services-Health Services
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 5ac2542760ec756165b9e8633f1fa09e63f655ccb69678f4345371d76d6bbb5f
  url: https://data.sec.gov/submissions/CIK0002025774.json
listings:
- ticker: ALPS
  exchange: NASDAQ
  instrument_type: equity_candidate
research_filings:
- accession: 0001493152-26-036364
  filed: '2026-08-06'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/2025774/000149315226036364/0001493152-26-036364-index.html
- accession: 0001493152-26-047250
  filed: '2026-10-15'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/2025774/000149315226047250/0001493152-26-047250-index.html
- accession: 0001493152-25-020312
  filed: '2025-10-31'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/2025774/000149315225020312/0001493152-25-020312-index.html
research_progress:
  stage: pending
  input_sha256: 4557b731866325a05673e043c99790226084d4912f6a198cc25025b9a0ca23ec
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
  derived_observations: 0
  model_draft: false
  reviewed: false
sector_assignment:
  sector: health-care
  method: project_sic_rule
  sic: '8000'
  sic_description: Services-Health Services
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0002025774.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/1b4771bc41dec553e210323f72d9bfc908288c04/brain/companies/ALPS/README.md
full_history_commit: 1b4771bc41dec553e210323f72d9bfc908288c04
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# ALPS — Alps Group Inc

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/1b4771bc41dec553e210323f72d9bfc908288c04/brain/companies/ALPS/README.md)

## Business overview

Reported issuer name: **Alps Group Inc**. Stable SEC CIK: **0002025774**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| ALPS | NASDAQ | equity_candidate | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **8000**: Services-Health Services. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **health-care**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

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
- Forms observed in the retained filing inventory: 20-F, 3, 424B3, 425, 6-K, 6-K/A, 8-A12B, CERT, CORRESP, DRS, DRS/A, DRSLTR, EFFECT, F-1, F-4, F-4/A, NT 20-F, SCHEDULE 13D, SCHEDULE 13G, SEC STAFF LETTER, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:36:34.257374+00:00.

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
| 2026-10-15 | 6-K | 0001493152-26-047250 | — | [S03] |
| 2026-10-08 | 6-K | 0001493152-26-046334 | — | [S04] |
| 2026-08-07 | 6-K | 0001493152-26-036587 | — | [S05] |
| 2026-08-06 | 20-F | 0001493152-26-036364 | — | [S06] |
| 2026-07-31 | NT 20-F | 0001493152-26-035650 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-30T16:00:11.183681+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0002025774.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [6-K 0001493152-26-047250](https://www.sec.gov/Archives/edgar/data/2025774/000149315226047250/0001493152-26-047250-index.html) — published 2026-10-15; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [6-K 0001493152-26-046334](https://www.sec.gov/Archives/edgar/data/2025774/000149315226046334/0001493152-26-046334-index.html) — published 2026-10-08; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [6-K 0001493152-26-036587](https://www.sec.gov/Archives/edgar/data/2025774/000149315226036587/0001493152-26-036587-index.html) — published 2026-08-07; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [20-F 0001493152-26-036364](https://www.sec.gov/Archives/edgar/data/2025774/000149315226036364/0001493152-26-036364-index.html) — published 2026-08-06; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [NT 20-F 0001493152-26-035650](https://www.sec.gov/Archives/edgar/data/2025774/000149315226035650/0001493152-26-035650-index.html) — published 2026-07-31; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261030-41085569265-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/1b4771bc41dec553e210323f72d9bfc908288c04/brain/companies/ALPS/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
