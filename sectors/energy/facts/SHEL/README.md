---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001306965
cik: 0001306965
company_name: Shell plc
tickers:
- SHEL
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
  - 11-K
  - 20-F
  - 20-F/A
  - 25-NSE
  - 424B2
  - 424B3
  - 424B5
  - 6-K
  - 6-K/A
  - 8-A12B
  - CERT
  - CERTNYS
  - CORRESP
  - EFFECT
  - F-3ASR
  - F-4
  - F-4/A
  - F-6
  - F-6 POS
  - FWP
  - IRANNOTICE
  - POSASR
  - PX14A6G
  - S-8
  - S-8 POS
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13G/A
  - SD
  - SD/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001306965.json
    sha256: f2509790c3fc4d26aee78dd84e4d7aeb1b80c5594fb15985790e44bf8018d97f
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001306965.json
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
  url: https://data.sec.gov/submissions/CIK0001306965.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: f2509790c3fc4d26aee78dd84e4d7aeb1b80c5594fb15985790e44bf8018d97f
- id: S03
  title: 6-K 0001171843-26-006591
  url: https://www.sec.gov/Archives/edgar/data/1306965/000117184326006591/0001171843-26-006591-index.html
  published_at: '2026-10-13'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 6-K 0001171843-26-006483
  url: https://www.sec.gov/Archives/edgar/data/1306965/000117184326006483/0001171843-26-006483-index.html
  published_at: '2026-10-07'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 6-K 0001171843-26-006351
  url: https://www.sec.gov/Archives/edgar/data/1306965/000117184326006351/0001171843-26-006351-index.html
  published_at: '2026-10-02'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 6-K 0001171843-26-006246
  url: https://www.sec.gov/Archives/edgar/data/1306965/000117184326006246/0001171843-26-006246-index.html
  published_at: '2026-09-28'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 25-NSE 0000876661-26-000740
  url: https://www.sec.gov/Archives/edgar/data/1306965/000087666126000740/0000876661-26-000740-index.html
  published_at: '2026-09-14'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0001306965
  classification_status: reported_sic
  entity_type: other
  name: Shell plc
  sic: '1311'
  sic_description: Crude Petroleum & Natural Gas
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: f2509790c3fc4d26aee78dd84e4d7aeb1b80c5594fb15985790e44bf8018d97f
  url: https://data.sec.gov/submissions/CIK0001306965.json
listings:
- ticker: SHEL
  exchange: NYSE
  instrument_type: depositary_receipt
research_filings:
- accession: 0001628280-26-017024
  filed: '2026-03-12'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1306965/000162828026017024/0001628280-26-017024-index.html
- accession: 0001306965-25-000027
  filed: '2025-07-02'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1306965/000130696525000027/0001306965-25-000027-index.html
- accession: 0001306965-25-000025
  filed: '2025-07-02'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1306965/000130696525000025/0001306965-25-000025-index.html
- accession: 0001171843-26-006591
  filed: '2026-10-13'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1306965/000117184326006591/0001171843-26-006591-index.html
- accession: 0001306965-24-000034
  filed: '2024-03-20'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1306965/000130696524000034/0001306965-24-000034-index.html
- accession: 0001171843-23-004708
  filed: '2023-07-27'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1306965/000117184323004708/0001171843-23-004708-index.html
- accession: 0001171843-21-005634
  filed: '2021-08-06'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1306965/000117184321005634/0001171843-21-005634-index.html
- accession: 0001171843-20-000633
  filed: '2020-01-31'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1306965/000117184320000633/0001171843-20-000633-index.html
- accession: 0001309014-17-000882
  filed: '2017-10-18'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1306965/000130901417000882/0001309014-17-000882-index.html
- accession: 0001309014-15-000538
  filed: '2015-08-06'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1306965/000130901415000538/0001309014-15-000538-index.html
- accession: 0001193125-15-029170
  filed: '2015-02-02'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1306965/000119312515029170/0001193125-15-029170-index.html
research_progress:
  stage: pending
  input_sha256: bd9204a86ed5114a66043cf01f57342f00aee48145f6e7c6ccd3ece5f969dbcd
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
  sic: '1311'
  sic_description: Crude Petroleum & Natural Gas
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001306965.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/71fcd4775048604503d616351f7f309068b23e1b/brain/companies/SHEL/README.md
full_history_commit: 71fcd4775048604503d616351f7f309068b23e1b
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# SHEL — Shell plc

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/71fcd4775048604503d616351f7f309068b23e1b/brain/companies/SHEL/README.md)

## Business overview

Reported issuer name: **Shell plc**. Stable SEC CIK: **0001306965**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| SHEL | NYSE | depositary_receipt | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **1311**: Crude Petroleum & Natural Gas. [S02]

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
- Forms observed in the retained filing inventory: 11-K, 20-F, 20-F/A, 25-NSE, 424B2, 424B3, 424B5, 6-K, 6-K/A, 8-A12B, CERT, CERTNYS, CORRESP, EFFECT, F-3ASR, F-4, F-4/A, F-6, F-6 POS, FWP, IRANNOTICE, POSASR, PX14A6G, S-8, S-8 POS, SC 13D, SC 13D/A, SC 13G, SC 13G/A, SCHEDULE 13G/A, SD, SD/A, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:32:29.914954+00:00.

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
| 2026-10-13 | 6-K | 0001171843-26-006591 | — | [S03] |
| 2026-10-07 | 6-K | 0001171843-26-006483 | — | [S04] |
| 2026-10-02 | 6-K | 0001171843-26-006351 | — | [S05] |
| 2026-09-28 | 6-K | 0001171843-26-006246 | — | [S06] |
| 2026-09-14 | 25-NSE | 0000876661-26-000740 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-25T13:45:48.334682+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001306965.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [6-K 0001171843-26-006591](https://www.sec.gov/Archives/edgar/data/1306965/000117184326006591/0001171843-26-006591-index.html) — published 2026-10-13; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [6-K 0001171843-26-006483](https://www.sec.gov/Archives/edgar/data/1306965/000117184326006483/0001171843-26-006483-index.html) — published 2026-10-07; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [6-K 0001171843-26-006351](https://www.sec.gov/Archives/edgar/data/1306965/000117184326006351/0001171843-26-006351-index.html) — published 2026-10-02; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [6-K 0001171843-26-006246](https://www.sec.gov/Archives/edgar/data/1306965/000117184326006246/0001171843-26-006246-index.html) — published 2026-09-28; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [25-NSE 0000876661-26-000740](https://www.sec.gov/Archives/edgar/data/1306965/000087666126000740/0000876661-26-000740-index.html) — published 2026-09-14; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261025-40199010718-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/71fcd4775048604503d616351f7f309068b23e1b/brain/companies/SHEL/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
