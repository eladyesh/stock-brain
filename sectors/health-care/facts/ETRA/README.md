---
schema_version: 1
document_type: company_facts
company_id: company-cik-0002088082
cik: 0002088082
company_name: Electra Therapeutics, Inc.
tickers:
- ETRA
status: stub
canonical_reviewed: false
as_of: '2026-10-28'
updated_at: '2026-10-28T16:13:42.115634+00:00'
reviewed_at: null
coverage_release: coverage-20261028-40722802424-1
source_commit: 48056b79cf1dc5f5270bd576defc5c9bc49d62cf
financial_history_available: false
curated_research: null
financial_gap:
  reason: unsupported_reporting_inventory
  next_action: Review primary filing evidence and identify the reporting regime; do
    not infer financial values from directory membership.
  observed_forms:
  - '3'
  - '4'
  - 424B4
  - 8-A12B
  - 8-K
  - CERT
  - D
  - DRS
  - DRS/A
  - EFFECT
  - S-1
  - S-1/A
  - S-1MEF
  - S-8
  - SCHEDULE 13D
  - SCHEDULE 13G
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0002088082.json
    sha256: 7e87259c61c76f8d3e3deb1e3025986ad1f989bc2d0e7ca8f8e4fe1ff1eded13
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0002088082.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: nasdaqlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt
  published_at: null
  retrieved_at: '2026-10-28T16:09:01.738588+00:00'
  sha256: b555e192b928396dc88877226e82c2c8e9470c389cf2def559495683c673510d
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0002088082.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 7e87259c61c76f8d3e3deb1e3025986ad1f989bc2d0e7ca8f8e4fe1ff1eded13
- id: S03
  title: SCHEDULE 13G 0001193125-26-405752
  url: https://www.sec.gov/Archives/edgar/data/2088082/000119312526405752/0001193125-26-405752-index.html
  published_at: '2026-09-28'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: SCHEDULE 13G 0001104659-26-111478
  url: https://www.sec.gov/Archives/edgar/data/2088082/000110465926111478/0001104659-26-111478-index.html
  published_at: '2026-09-28'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: SCHEDULE 13D 0000947871-26-000898
  url: https://www.sec.gov/Archives/edgar/data/2088082/000094787126000898/0000947871-26-000898-index.html
  published_at: '2026-09-25'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 4 0000947871-26-000881
  url: https://www.sec.gov/Archives/edgar/data/2088082/000094787126000881/0000947871-26-000881-index.html
  published_at: '2026-09-23'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 4 0000947871-26-000880
  url: https://www.sec.gov/Archives/edgar/data/2088082/000094787126000880/0000947871-26-000880-index.html
  published_at: '2026-09-23'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0002088082
  classification_status: reported_sic
  entity_type: other
  name: Electra Therapeutics, Inc.
  sic: '2836'
  sic_description: Biological Products, (No Diagnostic Substances)
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 7e87259c61c76f8d3e3deb1e3025986ad1f989bc2d0e7ca8f8e4fe1ff1eded13
  url: https://data.sec.gov/submissions/CIK0002088082.json
listings:
- ticker: ETRA
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001193125-26-396646
  filed: '2026-09-21'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/2088082/000119312526396646/0001193125-26-396646-index.html
research_progress:
  stage: pending
  input_sha256: f5dd239bba6e884ce5b40c1eff04c9bd7257d49840745615b6a3443c57a14442
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
  sic: '2836'
  sic_description: Biological Products, (No Diagnostic Substances)
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0002088082.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/d9e673c37aaa38580be4e36b4880e8ab015a9390/brain/companies/ETRA/README.md
full_history_commit: d9e673c37aaa38580be4e36b4880e8ab015a9390
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# ETRA — Electra Therapeutics, Inc.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/d9e673c37aaa38580be4e36b4880e8ab015a9390/brain/companies/ETRA/README.md)

## Business overview

Reported issuer name: **Electra Therapeutics, Inc.**. Stable SEC CIK: **0002088082**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| ETRA | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **2836**: Biological Products, (No Diagnostic Substances). [S02]

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
- Next collection task: Review primary filing evidence and identify the reporting regime; do not infer financial values from directory membership.
- Forms observed in the retained filing inventory: 3, 4, 424B4, 8-A12B, 8-K, CERT, D, DRS, DRS/A, EFFECT, S-1, S-1/A, S-1MEF, S-8, SCHEDULE 13D, SCHEDULE 13G
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:36:40.680321+00:00.

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
| 2026-09-28 | SCHEDULE 13G | 0001193125-26-405752 | — | [S03] |
| 2026-09-28 | SCHEDULE 13G | 0001104659-26-111478 | — | [S04] |
| 2026-09-25 | SCHEDULE 13D | 0000947871-26-000898 | — | [S05] |
| 2026-09-23 | 4 | 0000947871-26-000881 | — | [S06] |
| 2026-09-23 | 4 | 0000947871-26-000880 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-28T16:09:01.738588+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0002088082.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [SCHEDULE 13G 0001193125-26-405752](https://www.sec.gov/Archives/edgar/data/2088082/000119312526405752/0001193125-26-405752-index.html) — published 2026-09-28; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [SCHEDULE 13G 0001104659-26-111478](https://www.sec.gov/Archives/edgar/data/2088082/000110465926111478/0001104659-26-111478-index.html) — published 2026-09-28; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [SCHEDULE 13D 0000947871-26-000898](https://www.sec.gov/Archives/edgar/data/2088082/000094787126000898/0000947871-26-000898-index.html) — published 2026-09-25; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [4 0000947871-26-000881](https://www.sec.gov/Archives/edgar/data/2088082/000094787126000881/0000947871-26-000881-index.html) — published 2026-09-23; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [4 0000947871-26-000880](https://www.sec.gov/Archives/edgar/data/2088082/000094787126000880/0000947871-26-000880-index.html) — published 2026-09-23; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261028-40722802424-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/d9e673c37aaa38580be4e36b4880e8ab015a9390/brain/companies/ETRA/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
