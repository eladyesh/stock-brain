---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001713748
cik: 0001713748
company_name: Skeena Resources Ltd
tickers:
- SKE
status: stub
canonical_reviewed: false
as_of: '2026-10-25'
updated_at: '2026-10-25T13:50:29.910841+00:00'
reviewed_at: null
coverage_release: coverage-20261025-40199010718-1
source_commit: d4303e1efab53027fe4e6e90633e2c69b11c599c
financial_history_available: false
curated_research: null
financial_gap:
  reason: foreign_reporting_adapter
  next_action: Add support for the observed 20-F, 40-F or 6-K reporting forms and
    verify the actual accounting taxonomy before normalization.
  observed_forms:
  - 25-NSE
  - 40-F
  - 40FR12B
  - 40FR12B/A
  - 6-K
  - 8-A12B
  - CERT
  - D
  - D/A
  - F-10
  - F-X
  - FWP
  - S-8
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - SD
  - SEC STAFF ACTION
  - SUPPL
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001713748.json
    sha256: f6fc115d2280660255bcb8e4a856ec330c96119b668e11aa1ff53efb4c0be90a
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001713748.json
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
  url: https://data.sec.gov/submissions/CIK0001713748.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: f6fc115d2280660255bcb8e4a856ec330c96119b668e11aa1ff53efb4c0be90a
- id: S03
  title: SD 0001104659-26-108608
  url: https://www.sec.gov/Archives/edgar/data/1713748/000110465926108608/0001104659-26-108608-index.html
  published_at: '2026-09-17'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: SCHEDULE 13G/A 0000869178-26-000089
  url: https://www.sec.gov/Archives/edgar/data/1713748/000086917826000089/0000869178-26-000089-index.html
  published_at: '2026-08-14'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 6-K 0001104659-26-096000
  url: https://www.sec.gov/Archives/edgar/data/1713748/000110465926096000/0001104659-26-096000-index.html
  published_at: '2026-08-13'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 6-K 0001171843-26-004234
  url: https://www.sec.gov/Archives/edgar/data/1713748/000117184326004234/0001171843-26-004234-index.html
  published_at: '2026-06-23'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 6-K 0001104659-26-064053
  url: https://www.sec.gov/Archives/edgar/data/1713748/000110465926064053/0001104659-26-064053-index.html
  published_at: '2026-05-20'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0001713748
  classification_status: reported_sic
  entity_type: other
  name: Skeena Resources Ltd
  sic: '1040'
  sic_description: Gold and Silver Ores
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: f6fc115d2280660255bcb8e4a856ec330c96119b668e11aa1ff53efb4c0be90a
  url: https://data.sec.gov/submissions/CIK0001713748.json
listings:
- ticker: SKE
  exchange: NYSE
  instrument_type: common_stock
research_filings:
- accession: 0001104659-26-033959
  filed: '2026-03-24'
  form: 40-F
  url: https://www.sec.gov/Archives/edgar/data/1713748/000110465926033959/0001104659-26-033959-index.html
- accession: 0001104659-26-096000
  filed: '2026-08-13'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1713748/000110465926096000/0001104659-26-096000-index.html
research_progress:
  stage: pending
  input_sha256: d90fbd8909229b6b4c5ea3a5b509daf2e8ef91d1b91c40becc956cf5cda2dd1e
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
  source_url: https://data.sec.gov/submissions/CIK0001713748.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/c6b3af0cefe967faceb0323aa590d422e87cbc29/brain/companies/SKE/README.md
full_history_commit: c6b3af0cefe967faceb0323aa590d422e87cbc29
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# SKE — Skeena Resources Ltd

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/c6b3af0cefe967faceb0323aa590d422e87cbc29/brain/companies/SKE/README.md)

## Business overview

Reported issuer name: **Skeena Resources Ltd**. Stable SEC CIK: **0001713748**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| SKE | NYSE | common_stock | 1 | [S01] |

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
- Forms observed in the retained filing inventory: 25-NSE, 40-F, 40FR12B, 40FR12B/A, 6-K, 8-A12B, CERT, D, D/A, F-10, F-X, FWP, S-8, SC 13G, SC 13G/A, SCHEDULE 13G, SCHEDULE 13G/A, SD, SEC STAFF ACTION, SUPPL
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:35:14.043259+00:00.

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
| 2026-09-17 | SD | 0001104659-26-108608 | — | [S03] |
| 2026-08-14 | SCHEDULE 13G/A | 0000869178-26-000089 | — | [S04] |
| 2026-08-13 | 6-K | 0001104659-26-096000 | — | [S05] |
| 2026-06-23 | 6-K | 0001171843-26-004234 | — | [S06] |
| 2026-05-20 | 6-K | 0001104659-26-064053 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-25T13:45:48.334682+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001713748.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [SD 0001104659-26-108608](https://www.sec.gov/Archives/edgar/data/1713748/000110465926108608/0001104659-26-108608-index.html) — published 2026-09-17; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [SCHEDULE 13G/A 0000869178-26-000089](https://www.sec.gov/Archives/edgar/data/1713748/000086917826000089/0000869178-26-000089-index.html) — published 2026-08-14; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [6-K 0001104659-26-096000](https://www.sec.gov/Archives/edgar/data/1713748/000110465926096000/0001104659-26-096000-index.html) — published 2026-08-13; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [6-K 0001171843-26-004234](https://www.sec.gov/Archives/edgar/data/1713748/000117184326004234/0001171843-26-004234-index.html) — published 2026-06-23; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [6-K 0001104659-26-064053](https://www.sec.gov/Archives/edgar/data/1713748/000110465926064053/0001104659-26-064053-index.html) — published 2026-05-20; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261025-40199010718-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/c6b3af0cefe967faceb0323aa590d422e87cbc29/brain/companies/SKE/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
