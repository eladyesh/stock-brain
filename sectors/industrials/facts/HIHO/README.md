---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001026785
cik: 0001026785
company_name: HIGHWAY HOLDINGS LTD
tickers:
- HIHO
status: stub
canonical_reviewed: false
as_of: '2026-10-26'
updated_at: '2026-10-26T16:16:21.148680+00:00'
reviewed_at: null
coverage_release: coverage-20261026-40356450615-1
source_commit: 1a2786cc3cffc8c9981965ab9c208315321385f6
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
  - 6-K
  - 8-A12B
  - ARS
  - CORRESP
  - EFFECT
  - F-3
  - F-3/A
  - NT 20-F
  - POS AM
  - S-8
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13G/A
  - SEC STAFF ACTION
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001026785.json
    sha256: f66f2d3b8a4fee62453397964ef95e1cf913b719aec2f8c9c98cfb956a6f7c4c
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001026785.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: nasdaqlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt
  published_at: null
  retrieved_at: '2026-10-26T16:11:31.228419+00:00'
  sha256: 74146fcda2f9b3b43b06280df0ad9584dffa78b2237460917eda3c2892e7a706
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001026785.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: f66f2d3b8a4fee62453397964ef95e1cf913b719aec2f8c9c98cfb956a6f7c4c
- id: S03
  title: 6-K 0001213900-26-104029
  url: https://www.sec.gov/Archives/edgar/data/1026785/000121390026104029/0001213900-26-104029-index.html
  published_at: '2026-09-28'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 6-K 0001213900-26-101059
  url: https://www.sec.gov/Archives/edgar/data/1026785/000121390026101059/0001213900-26-101059-index.html
  published_at: '2026-09-18'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 6-K 0001213900-26-087382
  url: https://www.sec.gov/Archives/edgar/data/1026785/000121390026087382/0001213900-26-087382-index.html
  published_at: '2026-08-11'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 6-K 0001213900-26-084146
  url: https://www.sec.gov/Archives/edgar/data/1026785/000121390026084146/0001213900-26-084146-index.html
  published_at: '2026-08-03'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 6-K 0001213900-26-082985
  url: https://www.sec.gov/Archives/edgar/data/1026785/000121390026082985/0001213900-26-082985-index.html
  published_at: '2026-07-30'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0001026785
  classification_status: reported_sic
  entity_type: other
  name: HIGHWAY HOLDINGS LTD
  sic: '3490'
  sic_description: Miscellaneous Fabricated Metal Products
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: f66f2d3b8a4fee62453397964ef95e1cf913b719aec2f8c9c98cfb956a6f7c4c
  url: https://data.sec.gov/submissions/CIK0001026785.json
listings:
- ticker: HIHO
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001213900-26-077959
  filed: '2026-07-14'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1026785/000121390026077959/0001213900-26-077959-index.html
- accession: 0001213900-23-068948
  filed: '2023-08-18'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1026785/000121390023068948/0001213900-23-068948-index.html
- accession: 0001213900-20-023036
  filed: '2020-08-20'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1026785/000121390020023036/0001213900-20-023036-index.html
- accession: 0001144204-09-059556
  filed: '2009-11-16'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1026785/000114420409059556/0001144204-09-059556-index.html
- accession: 0001213900-26-104029
  filed: '2026-09-28'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1026785/000121390026104029/0001213900-26-104029-index.html
research_progress:
  stage: pending
  input_sha256: 4c609f7ecbcdf220cc50fa4f5c702c2aa4a7bd7557ea135ba3ae0ad730575a68
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
  sic: '3490'
  sic_description: Miscellaneous Fabricated Metal Products
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001026785.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/30a5d1cd40fce8d4a64ca29ee815b726555957d3/brain/companies/HIHO/README.md
full_history_commit: 30a5d1cd40fce8d4a64ca29ee815b726555957d3
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# HIHO — HIGHWAY HOLDINGS LTD

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/30a5d1cd40fce8d4a64ca29ee815b726555957d3/brain/companies/HIHO/README.md)

## Business overview

Reported issuer name: **HIGHWAY HOLDINGS LTD**. Stable SEC CIK: **0001026785**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| HIHO | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **3490**: Miscellaneous Fabricated Metal Products. [S02]

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
- Forms observed in the retained filing inventory: 20-F, 20-F/A, 3, 4, 6-K, 8-A12B, ARS, CORRESP, EFFECT, F-3, F-3/A, NT 20-F, POS AM, S-8, SC 13G, SC 13G/A, SCHEDULE 13G/A, SEC STAFF ACTION, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:30:57.690129+00:00.

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
| 2026-09-28 | 6-K | 0001213900-26-104029 | — | [S03] |
| 2026-09-18 | 6-K | 0001213900-26-101059 | — | [S04] |
| 2026-08-11 | 6-K | 0001213900-26-087382 | — | [S05] |
| 2026-08-03 | 6-K | 0001213900-26-084146 | — | [S06] |
| 2026-07-30 | 6-K | 0001213900-26-082985 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-26T16:11:31.228419+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001026785.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [6-K 0001213900-26-104029](https://www.sec.gov/Archives/edgar/data/1026785/000121390026104029/0001213900-26-104029-index.html) — published 2026-09-28; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [6-K 0001213900-26-101059](https://www.sec.gov/Archives/edgar/data/1026785/000121390026101059/0001213900-26-101059-index.html) — published 2026-09-18; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [6-K 0001213900-26-087382](https://www.sec.gov/Archives/edgar/data/1026785/000121390026087382/0001213900-26-087382-index.html) — published 2026-08-11; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [6-K 0001213900-26-084146](https://www.sec.gov/Archives/edgar/data/1026785/000121390026084146/0001213900-26-084146-index.html) — published 2026-08-03; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [6-K 0001213900-26-082985](https://www.sec.gov/Archives/edgar/data/1026785/000121390026082985/0001213900-26-082985-index.html) — published 2026-07-30; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261026-40356450615-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/30a5d1cd40fce8d4a64ca29ee815b726555957d3/brain/companies/HIHO/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
