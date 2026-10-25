---
schema_version: 1
document_type: company_facts
company_id: company-cik-0000886986
cik: 0000886986
company_name: TECK RESOURCES LTD
tickers:
- TECK
status: stub
canonical_reviewed: false
as_of: '2026-10-25'
updated_at: '2026-10-25T13:50:29.910841+00:00'
reviewed_at: null
coverage_release: coverage-20261025-40199010718-1
source_commit: f5f88011907841550f3cf7652c3822295b45cb57
financial_history_available: false
curated_research: null
financial_gap:
  reason: foreign_reporting_adapter
  next_action: Add support for the observed 20-F, 40-F or 6-K reporting forms and
    verify the actual accounting taxonomy before normalization.
  observed_forms:
  - 40-F
  - 424B3
  - 6-K
  - CORRESP
  - EFFECT
  - F-10
  - F-10/A
  - F-4
  - F-4/A
  - F-9
  - F-9/A
  - F-X
  - FWP
  - PX14A6G
  - S-8
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - SD
  - SUPPL
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0000886986.json
    sha256: 77d8b3d4f44dcea1eec6a6aa38adcdaa3cee1abbb4f8de3e006d0c6499d305f0
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0000886986.json
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
  url: https://data.sec.gov/submissions/CIK0000886986.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 77d8b3d4f44dcea1eec6a6aa38adcdaa3cee1abbb4f8de3e006d0c6499d305f0
- id: S03
  title: 6-K 0000950142-26-002797
  url: https://www.sec.gov/Archives/edgar/data/886986/000095014226002797/0000950142-26-002797-index.html
  published_at: '2026-10-21'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 6-K 0000950142-26-002704
  url: https://www.sec.gov/Archives/edgar/data/886986/000095014226002704/0000950142-26-002704-index.html
  published_at: '2026-10-08'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 6-K 0000950142-26-002694
  url: https://www.sec.gov/Archives/edgar/data/886986/000095014226002694/0000950142-26-002694-index.html
  published_at: '2026-10-07'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 6-K 0000950142-26-002470
  url: https://www.sec.gov/Archives/edgar/data/886986/000095014226002470/0000950142-26-002470-index.html
  published_at: '2026-09-01'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 6-K 0000950142-26-002318
  url: https://www.sec.gov/Archives/edgar/data/886986/000095014226002318/0000950142-26-002318-index.html
  published_at: '2026-08-12'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0000886986
  classification_status: reported_sic
  entity_type: other
  name: TECK RESOURCES LTD
  sic: '1400'
  sic_description: Mining & Quarrying of  Nonmetallic Minerals (No Fuels)
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 77d8b3d4f44dcea1eec6a6aa38adcdaa3cee1abbb4f8de3e006d0c6499d305f0
  url: https://data.sec.gov/submissions/CIK0000886986.json
listings:
- ticker: TECK
  exchange: NYSE
  instrument_type: common_stock
research_filings:
- accession: 0000886986-26-000004
  filed: '2026-02-19'
  form: 40-F
  url: https://www.sec.gov/Archives/edgar/data/886986/000088698626000004/0000886986-26-000004-index.html
- accession: 0000950142-26-002797
  filed: '2026-10-21'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/886986/000095014226002797/0000950142-26-002797-index.html
research_progress:
  stage: pending
  input_sha256: 9eb2a35234acd8017ea8da0298920c4029392721ff7a370995545159441f9b5d
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
  derived_observations: 0
  model_draft: false
  reviewed: false
sector_assignment:
  sector: materials
  method: project_sic_rule
  sic: '1400'
  sic_description: Mining & Quarrying of  Nonmetallic Minerals (No Fuels)
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0000886986.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/71fcd4775048604503d616351f7f309068b23e1b/brain/companies/TECK/README.md
full_history_commit: 71fcd4775048604503d616351f7f309068b23e1b
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# TECK — TECK RESOURCES LTD

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/71fcd4775048604503d616351f7f309068b23e1b/brain/companies/TECK/README.md)

## Business overview

Reported issuer name: **TECK RESOURCES LTD**. Stable SEC CIK: **0000886986**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| TECK | NYSE | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **1400**: Mining & Quarrying of  Nonmetallic Minerals (No Fuels). [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **materials**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

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
- Forms observed in the retained filing inventory: 40-F, 424B3, 6-K, CORRESP, EFFECT, F-10, F-10/A, F-4, F-4/A, F-9, F-9/A, F-X, FWP, PX14A6G, S-8, SC 13D/A, SC 13G, SC 13G/A, SCHEDULE 13G, SCHEDULE 13G/A, SD, SUPPL, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:30:02.462395+00:00.

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
| 2026-10-21 | 6-K | 0000950142-26-002797 | — | [S03] |
| 2026-10-08 | 6-K | 0000950142-26-002704 | — | [S04] |
| 2026-10-07 | 6-K | 0000950142-26-002694 | — | [S05] |
| 2026-09-01 | 6-K | 0000950142-26-002470 | — | [S06] |
| 2026-08-12 | 6-K | 0000950142-26-002318 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-25T13:45:48.334682+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0000886986.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [6-K 0000950142-26-002797](https://www.sec.gov/Archives/edgar/data/886986/000095014226002797/0000950142-26-002797-index.html) — published 2026-10-21; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [6-K 0000950142-26-002704](https://www.sec.gov/Archives/edgar/data/886986/000095014226002704/0000950142-26-002704-index.html) — published 2026-10-08; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [6-K 0000950142-26-002694](https://www.sec.gov/Archives/edgar/data/886986/000095014226002694/0000950142-26-002694-index.html) — published 2026-10-07; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [6-K 0000950142-26-002470](https://www.sec.gov/Archives/edgar/data/886986/000095014226002470/0000950142-26-002470-index.html) — published 2026-09-01; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [6-K 0000950142-26-002318](https://www.sec.gov/Archives/edgar/data/886986/000095014226002318/0000950142-26-002318-index.html) — published 2026-08-12; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261025-40199010718-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/71fcd4775048604503d616351f7f309068b23e1b/brain/companies/TECK/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
