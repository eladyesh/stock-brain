---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001277866
cik: 0001277866
company_name: ENDEAVOUR SILVER CORP
tickers:
- EXK
status: stub
canonical_reviewed: false
as_of: '2026-10-28'
updated_at: '2026-10-28T16:13:42.115634+00:00'
reviewed_at: null
coverage_release: coverage-20261028-40722802424-1
source_commit: 8a30d18f29f6ce6c61cbe955ca3f23f6f12ef180
financial_history_available: false
curated_research: null
financial_gap:
  reason: foreign_reporting_adapter
  next_action: Add support for the observed 20-F, 40-F or 6-K reporting forms and
    verify the actual accounting taxonomy before normalization.
  observed_forms:
  - '25'
  - 40-F
  - 40-F/A
  - 40FR12B
  - 424B3
  - 6-K
  - 6-K/A
  - 8-A12B
  - CB
  - CB/A
  - CERTAMX
  - CERTNYS
  - CORRESP
  - D
  - EFFECT
  - F-10
  - F-10/A
  - F-3
  - F-X
  - F-X/A
  - FWP
  - REGDEX
  - SC 13D
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
    url: https://data.sec.gov/submissions/CIK0001277866.json
    sha256: f97874f14ec656295a8de6968eff6f92892621255c2138778c127a3d959ceae4
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001277866.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: otherlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt
  published_at: null
  retrieved_at: '2026-10-28T16:09:02.154543+00:00'
  sha256: 9075fbed01d898a38c24f9b203cac1b6a4eed581edb2da888a321447f3bb55cc
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001277866.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: f97874f14ec656295a8de6968eff6f92892621255c2138778c127a3d959ceae4
- id: S03
  title: 6-K 0001171843-26-006604
  url: https://www.sec.gov/Archives/edgar/data/1277866/000117184326006604/0001171843-26-006604-index.html
  published_at: '2026-10-13'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 6-K 0001171843-26-006526
  url: https://www.sec.gov/Archives/edgar/data/1277866/000117184326006526/0001171843-26-006526-index.html
  published_at: '2026-10-08'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 6-K 0001171843-26-006158
  url: https://www.sec.gov/Archives/edgar/data/1277866/000117184326006158/0001171843-26-006158-index.html
  published_at: '2026-09-22'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: SD 0001062993-26-004892
  url: https://www.sec.gov/Archives/edgar/data/1277866/000106299326004892/0001062993-26-004892-index.html
  published_at: '2026-09-10'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 6-K 0001171843-26-005712
  url: https://www.sec.gov/Archives/edgar/data/1277866/000117184326005712/0001171843-26-005712-index.html
  published_at: '2026-08-24'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0001277866
  classification_status: reported_sic
  entity_type: other
  name: ENDEAVOUR SILVER CORP
  sic: '1040'
  sic_description: Gold and Silver Ores
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: f97874f14ec656295a8de6968eff6f92892621255c2138778c127a3d959ceae4
  url: https://data.sec.gov/submissions/CIK0001277866.json
listings:
- ticker: EXK
  exchange: NYSE
  instrument_type: common_stock
research_filings:
- accession: 0001062993-26-001662
  filed: '2026-03-30'
  form: 40-F
  url: https://www.sec.gov/Archives/edgar/data/1277866/000106299326001662/0001062993-26-001662-index.html
- accession: 0001062993-26-001944
  filed: '2026-04-13'
  form: 40-F/A
  url: https://www.sec.gov/Archives/edgar/data/1277866/000106299326001944/0001062993-26-001944-index.html
- accession: 0001062993-18-001528
  filed: '2018-04-06'
  form: 40-F/A
  url: https://www.sec.gov/Archives/edgar/data/1277866/000106299318001528/0001062993-18-001528-index.html
- accession: 0001062993-18-001119
  filed: '2018-03-08'
  form: 40-F/A
  url: https://www.sec.gov/Archives/edgar/data/1277866/000106299318001119/0001062993-18-001119-index.html
- accession: 0001062993-10-000161
  filed: '2010-01-19'
  form: 40-F/A
  url: https://www.sec.gov/Archives/edgar/data/1277866/000106299310000161/0001062993-10-000161-index.html
- accession: 0000912282-08-001498
  filed: '2008-10-10'
  form: 40-F/A
  url: https://www.sec.gov/Archives/edgar/data/1277866/000091228208001498/0000912282-08-001498-index.html
- accession: 0001171843-26-006604
  filed: '2026-10-13'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1277866/000117184326006604/0001171843-26-006604-index.html
- accession: 0001062993-26-003916
  filed: '2026-07-30'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1277866/000106299326003916/0001062993-26-003916-index.html
- accession: 0001171843-26-000313
  filed: '2026-01-16'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1277866/000117184326000313/0001171843-26-000313-index.html
- accession: 0001171843-22-005545
  filed: '2022-08-09'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1277866/000117184322005545/0001171843-22-005545-index.html
- accession: 0001062993-20-001691
  filed: '2020-04-08'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1277866/000106299320001691/0001062993-20-001691-index.html
- accession: 0001062993-13-005374
  filed: '2013-11-05'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1277866/000106299313005374/0001062993-13-005374-index.html
research_progress:
  stage: pending
  input_sha256: e06f6581525ff7d3f573bebd8f6807c7566f910d13ade15c317c31bd59034828
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
  sic: '1040'
  sic_description: Gold and Silver Ores
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001277866.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/5da532c3abee5b40a5400c5864c6f3f4593276d7/brain/companies/EXK/README.md
full_history_commit: 5da532c3abee5b40a5400c5864c6f3f4593276d7
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# EXK — ENDEAVOUR SILVER CORP

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/5da532c3abee5b40a5400c5864c6f3f4593276d7/brain/companies/EXK/README.md)

## Business overview

Reported issuer name: **ENDEAVOUR SILVER CORP**. Stable SEC CIK: **0001277866**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| EXK | NYSE | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **1040**: Gold and Silver Ores. [S02]

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
- Forms observed in the retained filing inventory: 25, 40-F, 40-F/A, 40FR12B, 424B3, 6-K, 6-K/A, 8-A12B, CB, CB/A, CERTAMX, CERTNYS, CORRESP, D, EFFECT, F-10, F-10/A, F-3, F-X, F-X/A, FWP, REGDEX, SC 13D, SC 13D/A, SC 13G, SC 13G/A, SCHEDULE 13G, SCHEDULE 13G/A, SD, SUPPL, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:32:19.753466+00:00.

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
| 2026-10-13 | 6-K | 0001171843-26-006604 | — | [S03] |
| 2026-10-08 | 6-K | 0001171843-26-006526 | — | [S04] |
| 2026-09-22 | 6-K | 0001171843-26-006158 | — | [S05] |
| 2026-09-10 | SD | 0001062993-26-004892 | — | [S06] |
| 2026-08-24 | 6-K | 0001171843-26-005712 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-28T16:09:02.154543+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001277866.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [6-K 0001171843-26-006604](https://www.sec.gov/Archives/edgar/data/1277866/000117184326006604/0001171843-26-006604-index.html) — published 2026-10-13; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [6-K 0001171843-26-006526](https://www.sec.gov/Archives/edgar/data/1277866/000117184326006526/0001171843-26-006526-index.html) — published 2026-10-08; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [6-K 0001171843-26-006158](https://www.sec.gov/Archives/edgar/data/1277866/000117184326006158/0001171843-26-006158-index.html) — published 2026-09-22; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [SD 0001062993-26-004892](https://www.sec.gov/Archives/edgar/data/1277866/000106299326004892/0001062993-26-004892-index.html) — published 2026-09-10; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [6-K 0001171843-26-005712](https://www.sec.gov/Archives/edgar/data/1277866/000117184326005712/0001171843-26-005712-index.html) — published 2026-08-24; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261028-40722802424-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/5da532c3abee5b40a5400c5864c6f3f4593276d7/brain/companies/EXK/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
