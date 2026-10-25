---
schema_version: 1
document_type: company_facts
company_id: company-cik-0002136387
cik: 0002136387
company_name: Real REMAX Group Inc.
tickers:
- REAX
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
  reason: unsupported_reporting_inventory
  next_action: Review primary filing evidence and identify the reporting regime; do
    not infer financial values from directory membership.
  observed_forms:
  - '144'
  - '3'
  - '4'
  - 4/A
  - 424B3
  - 8-K
  - 8-K12B
  - EFFECT
  - S-4
  - S-4/A
  - S-8
  - SCHEDULE 13D
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0002136387.json
    sha256: 5966faaa9343eab4fbf6654c3d1044f90e5f3e29e68f42a858ce39e89155e79c
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0002136387.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: nasdaqlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt
  published_at: null
  retrieved_at: '2026-10-25T13:45:47.626200+00:00'
  sha256: 59ac9b74ff663c6de40f5c93a54d5e12eb3fbef74f82e8a7cfc1456ad9f969ec
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0002136387.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 5966faaa9343eab4fbf6654c3d1044f90e5f3e29e68f42a858ce39e89155e79c
- id: S03
  title: 4/A 0000950138-26-000032
  url: https://www.sec.gov/Archives/edgar/data/2136387/000095013826000032/0000950138-26-000032-index.html
  published_at: '2026-10-02'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 4 0000950138-26-000030
  url: https://www.sec.gov/Archives/edgar/data/2136387/000095013826000030/0000950138-26-000030-index.html
  published_at: '2026-09-28'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: SCHEDULE 13D 0001104659-26-110396
  url: https://www.sec.gov/Archives/edgar/data/2136387/000110465926110396/0001104659-26-110396-index.html
  published_at: '2026-09-24'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 4 0000950138-26-000028
  url: https://www.sec.gov/Archives/edgar/data/2136387/000095013826000028/0000950138-26-000028-index.html
  published_at: '2026-09-21'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 4 0002052698-26-000008
  url: https://www.sec.gov/Archives/edgar/data/2136387/000205269826000008/0002052698-26-000008-index.html
  published_at: '2026-09-18'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0002136387
  classification_status: reported_sic
  entity_type: other
  name: Real REMAX Group Inc.
  sic: '6531'
  sic_description: Real Estate Agents & Managers (For Others)
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 5966faaa9343eab4fbf6654c3d1044f90e5f3e29e68f42a858ce39e89155e79c
  url: https://data.sec.gov/submissions/CIK0002136387.json
listings:
- ticker: REAX
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001104659-26-103266
  filed: '2026-08-28'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/2136387/000110465926103266/0001104659-26-103266-index.html
research_progress:
  stage: pending
  input_sha256: 4672c082559eda8486861e5e0c5289eaeef1a239d3b3c6e8406453a960cd3435
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
  derived_observations: 0
  model_draft: false
  reviewed: false
sector_assignment:
  sector: real-estate
  method: project_sic_rule
  sic: '6531'
  sic_description: Real Estate Agents & Managers (For Others)
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0002136387.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/71fcd4775048604503d616351f7f309068b23e1b/brain/companies/REAX/README.md
full_history_commit: 71fcd4775048604503d616351f7f309068b23e1b
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# REAX — Real REMAX Group Inc.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/71fcd4775048604503d616351f7f309068b23e1b/brain/companies/REAX/README.md)

## Business overview

Reported issuer name: **Real REMAX Group Inc.**. Stable SEC CIK: **0002136387**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| REAX | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **6531**: Real Estate Agents & Managers (For Others). [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **real-estate**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

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
- Next collection task: Review primary filing evidence and identify the reporting regime; do not infer financial values from directory membership.
- Forms observed in the retained filing inventory: 144, 3, 4, 4/A, 424B3, 8-K, 8-K12B, EFFECT, S-4, S-4/A, S-8, SCHEDULE 13D
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:36:43.174424+00:00.

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
| 2026-10-02 | 4/A | 0000950138-26-000032 | — | [S03] |
| 2026-09-28 | 4 | 0000950138-26-000030 | — | [S04] |
| 2026-09-24 | SCHEDULE 13D | 0001104659-26-110396 | — | [S05] |
| 2026-09-21 | 4 | 0000950138-26-000028 | — | [S06] |
| 2026-09-18 | 4 | 0002052698-26-000008 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-25T13:45:47.626200+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0002136387.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [4/A 0000950138-26-000032](https://www.sec.gov/Archives/edgar/data/2136387/000095013826000032/0000950138-26-000032-index.html) — published 2026-10-02; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [4 0000950138-26-000030](https://www.sec.gov/Archives/edgar/data/2136387/000095013826000030/0000950138-26-000030-index.html) — published 2026-09-28; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [SCHEDULE 13D 0001104659-26-110396](https://www.sec.gov/Archives/edgar/data/2136387/000110465926110396/0001104659-26-110396-index.html) — published 2026-09-24; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [4 0000950138-26-000028](https://www.sec.gov/Archives/edgar/data/2136387/000095013826000028/0000950138-26-000028-index.html) — published 2026-09-21; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [4 0002052698-26-000008](https://www.sec.gov/Archives/edgar/data/2136387/000205269826000008/0002052698-26-000008-index.html) — published 2026-09-18; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261025-40199010718-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/71fcd4775048604503d616351f7f309068b23e1b/brain/companies/REAX/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
