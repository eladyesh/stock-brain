---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001140625
cik: '0001140625'
company_name: EQUINOR ASA
tickers:
- EQNR
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
  reason: foreign_reporting_adapter
  next_action: Add support for the observed 20-F, 40-F or 6-K reporting forms and
    verify the actual accounting taxonomy before normalization.
  observed_forms:
  - 20-F
  - 20-F/A
  - 424B2
  - 424B3
  - 6-K
  - 6-K/A
  - CORRESP
  - F-3ASR
  - F-6
  - F-6EF
  - FWP
  - IRANNOTICE
  - S-8
  - SCHEDULE 13G
  - SD
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001140625.json
    sha256: d669f4658473b08db95b3c140d384c7c5d43123a993d97c25f44a19c24746f42
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001140625.json
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
  url: https://data.sec.gov/submissions/CIK0001140625.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: d669f4658473b08db95b3c140d384c7c5d43123a993d97c25f44a19c24746f42
- id: S03
  title: 6-K 0001171843-26-006701
  url: https://www.sec.gov/Archives/edgar/data/1140625/000117184326006701/0001171843-26-006701-index.html
  published_at: '2026-10-20'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 6-K 0001171843-26-006700
  url: https://www.sec.gov/Archives/edgar/data/1140625/000117184326006700/0001171843-26-006700-index.html
  published_at: '2026-10-20'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 6-K 0001171843-26-006581
  url: https://www.sec.gov/Archives/edgar/data/1140625/000117184326006581/0001171843-26-006581-index.html
  published_at: '2026-10-13'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 6-K 0001171843-26-006433
  url: https://www.sec.gov/Archives/edgar/data/1140625/000117184326006433/0001171843-26-006433-index.html
  published_at: '2026-10-06'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 6-K 0001171843-26-006352
  url: https://www.sec.gov/Archives/edgar/data/1140625/000117184326006352/0001171843-26-006352-index.html
  published_at: '2026-10-02'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: '0001140625'
  classification_status: reported_sic
  entity_type: other
  name: EQUINOR ASA
  sic: '2911'
  sic_description: Petroleum Refining
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: d669f4658473b08db95b3c140d384c7c5d43123a993d97c25f44a19c24746f42
  url: https://data.sec.gov/submissions/CIK0001140625.json
listings:
- ticker: EQNR
  exchange: NYSE
  instrument_type: equity_candidate
research_filings:
- accession: 0001140625-26-000013
  filed: '2026-03-19'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1140625/000114062526000013/0001140625-26-000013-index.html
- accession: 0001140625-24-000038
  filed: '2024-03-21'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1140625/000114062524000038/0001140625-24-000038-index.html
- accession: 0001140625-22-000044
  filed: '2022-03-18'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1140625/000114062522000044/0001140625-22-000044-index.html
- accession: 0001171843-26-006701
  filed: '2026-10-20'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1140625/000117184326006701/0001171843-26-006701-index.html
- accession: 0001140625-25-000036
  filed: '2025-02-18'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1140625/000114062525000036/0001140625-25-000036-index.html
- accession: 0001171843-22-004198
  filed: '2022-06-07'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1140625/000117184322004198/0001171843-22-004198-index.html
- accession: 0001171843-17-005663
  filed: '2017-09-21'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1140625/000117184317005663/0001171843-17-005663-index.html
research_progress:
  stage: pending
  input_sha256: 03b459627cc7f2bd1c0298ee6046f7fab74215975a92d51b3ac5890f0e9d2509
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
  derived_observations: 0
  model_draft: false
  reviewed: false
sector_assignment:
  sector: energy
  method: project_sic_rule
  sic: '2911'
  sic_description: Petroleum Refining
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001140625.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/c26f59bc72c00102d2490e95b07449f8cd848491/brain/companies/EQNR/README.md
full_history_commit: c26f59bc72c00102d2490e95b07449f8cd848491
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# EQNR — EQUINOR ASA

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/c26f59bc72c00102d2490e95b07449f8cd848491/brain/companies/EQNR/README.md)

## Business overview

Reported issuer name: **EQUINOR ASA**. Stable SEC CIK: **0001140625**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| EQNR | NYSE | equity_candidate | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **2911**: Petroleum Refining. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **energy**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

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
- Forms observed in the retained filing inventory: 20-F, 20-F/A, 424B2, 424B3, 6-K, 6-K/A, CORRESP, F-3ASR, F-6, F-6EF, FWP, IRANNOTICE, S-8, SCHEDULE 13G, SD, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:31:55.276457+00:00.

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
| 2026-10-20 | 6-K | 0001171843-26-006701 | — | [S03] |
| 2026-10-20 | 6-K | 0001171843-26-006700 | — | [S04] |
| 2026-10-13 | 6-K | 0001171843-26-006581 | — | [S05] |
| 2026-10-06 | 6-K | 0001171843-26-006433 | — | [S06] |
| 2026-10-02 | 6-K | 0001171843-26-006352 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-29T16:14:13.951866+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001140625.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [6-K 0001171843-26-006701](https://www.sec.gov/Archives/edgar/data/1140625/000117184326006701/0001171843-26-006701-index.html) — published 2026-10-20; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [6-K 0001171843-26-006700](https://www.sec.gov/Archives/edgar/data/1140625/000117184326006700/0001171843-26-006700-index.html) — published 2026-10-20; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [6-K 0001171843-26-006581](https://www.sec.gov/Archives/edgar/data/1140625/000117184326006581/0001171843-26-006581-index.html) — published 2026-10-13; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [6-K 0001171843-26-006433](https://www.sec.gov/Archives/edgar/data/1140625/000117184326006433/0001171843-26-006433-index.html) — published 2026-10-06; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [6-K 0001171843-26-006352](https://www.sec.gov/Archives/edgar/data/1140625/000117184326006352/0001171843-26-006352-index.html) — published 2026-10-02; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261029-40909364006-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/c26f59bc72c00102d2490e95b07449f8cd848491/brain/companies/EQNR/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
