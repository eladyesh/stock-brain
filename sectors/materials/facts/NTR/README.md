---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001725964
cik: 0001725964
company_name: Nutrien Ltd.
tickers:
- NTR
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
  - 11-K
  - 40-F
  - 6-K
  - 6-K/A
  - 8-K12B
  - ARS
  - CORRESP
  - F-10
  - F-10/A
  - F-X
  - F-X/A
  - FWP
  - S-8
  - SC 13D/A
  - SC 13G
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - SD
  - SUPPL
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001725964.json
    sha256: a3eda661a136d334ee071fa18097873c40448f6ca62afd4d88e7e88e647def3d
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001725964.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: otherlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt
  published_at: null
  retrieved_at: '2026-10-23T14:17:55.298415+00:00'
  sha256: be329650ef672c0314f0e16b2e41951f6af4ae314df9a04a32dc11ddb70b194e
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001725964.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: a3eda661a136d334ee071fa18097873c40448f6ca62afd4d88e7e88e647def3d
- id: S03
  title: 6-K 0001193125-26-413251
  url: https://www.sec.gov/Archives/edgar/data/1725964/000119312526413251/0001193125-26-413251-index.html
  published_at: '2026-10-05'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: SD 0001193125-26-339095
  url: https://www.sec.gov/Archives/edgar/data/1725964/000119312526339095/0001193125-26-339095-index.html
  published_at: '2026-08-07'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 6-K 0001193125-26-336192
  url: https://www.sec.gov/Archives/edgar/data/1725964/000119312526336192/0001193125-26-336192-index.html
  published_at: '2026-08-06'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 6-K 0001193125-26-335517
  url: https://www.sec.gov/Archives/edgar/data/1725964/000119312526335517/0001193125-26-335517-index.html
  published_at: '2026-08-05'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: SCHEDULE 13G 0002100119-26-001516
  url: https://www.sec.gov/Archives/edgar/data/1725964/000210011926001516/0002100119-26-001516-index.html
  published_at: '2026-07-31'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0001725964
  classification_status: reported_sic
  entity_type: other
  name: Nutrien Ltd.
  sic: '2870'
  sic_description: Agricultural Chemicals
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: a3eda661a136d334ee071fa18097873c40448f6ca62afd4d88e7e88e647def3d
  url: https://data.sec.gov/submissions/CIK0001725964.json
listings:
- ticker: NTR
  exchange: NYSE
  instrument_type: common_stock
research_filings:
- accession: 0001193125-26-081326
  filed: '2026-02-27'
  form: 40-F
  url: https://www.sec.gov/Archives/edgar/data/1725964/000119312526081326/0001193125-26-081326-index.html
- accession: 0001193125-26-413251
  filed: '2026-10-05'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1725964/000119312526413251/0001193125-26-413251-index.html
- accession: 0001193125-22-211573
  filed: '2022-08-04'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1725964/000119312522211573/0001193125-22-211573-index.html
- accession: 0001193125-18-082492
  filed: '2018-03-14'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1725964/000119312518082492/0001193125-18-082492-index.html
research_progress:
  stage: pending
  input_sha256: d5ad7a7232f45e3a834f2f17794f57e2ea04381ff54e69a7f07e1aafdaecfe17
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
  sic: '2870'
  sic_description: Agricultural Chemicals
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001725964.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/d523cff21b18141b9a37cddd98ad6af6e1a30fa5/brain/companies/NTR/README.md
full_history_commit: d523cff21b18141b9a37cddd98ad6af6e1a30fa5
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# NTR — Nutrien Ltd.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/d523cff21b18141b9a37cddd98ad6af6e1a30fa5/brain/companies/NTR/README.md)

## Business overview

Reported issuer name: **Nutrien Ltd.**. Stable SEC CIK: **0001725964**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| NTR | NYSE | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **2870**: Agricultural Chemicals. [S02]

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
- Forms observed in the retained filing inventory: 11-K, 40-F, 6-K, 6-K/A, 8-K12B, ARS, CORRESP, F-10, F-10/A, F-X, F-X/A, FWP, S-8, SC 13D/A, SC 13G, SCHEDULE 13G, SCHEDULE 13G/A, SD, SUPPL, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-23T14:32:43.977165+00:00.

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
| 2026-10-05 | 6-K | 0001193125-26-413251 | — | [S03] |
| 2026-08-07 | SD | 0001193125-26-339095 | — | [S04] |
| 2026-08-06 | 6-K | 0001193125-26-336192 | — | [S05] |
| 2026-08-05 | 6-K | 0001193125-26-335517 | — | [S06] |
| 2026-07-31 | SCHEDULE 13G | 0002100119-26-001516 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-23T14:17:55.298415+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001725964.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [6-K 0001193125-26-413251](https://www.sec.gov/Archives/edgar/data/1725964/000119312526413251/0001193125-26-413251-index.html) — published 2026-10-05; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [SD 0001193125-26-339095](https://www.sec.gov/Archives/edgar/data/1725964/000119312526339095/0001193125-26-339095-index.html) — published 2026-08-07; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [6-K 0001193125-26-336192](https://www.sec.gov/Archives/edgar/data/1725964/000119312526336192/0001193125-26-336192-index.html) — published 2026-08-06; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [6-K 0001193125-26-335517](https://www.sec.gov/Archives/edgar/data/1725964/000119312526335517/0001193125-26-335517-index.html) — published 2026-08-05; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [SCHEDULE 13G 0002100119-26-001516](https://www.sec.gov/Archives/edgar/data/1725964/000210011926001516/0002100119-26-001516-index.html) — published 2026-07-31; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261023-39968262770-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/d523cff21b18141b9a37cddd98ad6af6e1a30fa5/brain/companies/NTR/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
