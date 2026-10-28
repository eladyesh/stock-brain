---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001817740
cik: 0001817740
company_name: Austin Gold Corp.
tickers:
- AUST
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
  - 20-F
  - 424B3
  - 424B4
  - 6-K
  - 8-A12B
  - CERT
  - CORRESP
  - D
  - DRS
  - DRS/A
  - DRSLTR
  - EFFECT
  - F-3
  - S-1
  - S-1/A
  - S-8
  - SC 13D
  - SCHEDULE 13D/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001817740.json
    sha256: ac29b3088740739a2afb5e38c07f7b0423d7c427a5ffb1138ca364b599aa07d0
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001817740.json
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
  url: https://data.sec.gov/submissions/CIK0001817740.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: ac29b3088740739a2afb5e38c07f7b0423d7c427a5ffb1138ca364b599aa07d0
- id: S03
  title: 6-K 0001104659-26-091322
  url: https://www.sec.gov/Archives/edgar/data/1817740/000110465926091322/0001104659-26-091322-index.html
  published_at: '2026-08-06'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: EFFECT 9999999995-26-002223
  url: https://www.sec.gov/Archives/edgar/data/1817740/999999999526002223/9999999995-26-002223-index.html
  published_at: '2026-07-08'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: F-3 0001104659-26-076502
  url: https://www.sec.gov/Archives/edgar/data/1817740/000110465926076502/0001104659-26-076502-index.html
  published_at: '2026-06-23'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 6-K 0001062993-26-003170
  url: https://www.sec.gov/Archives/edgar/data/1817740/000106299326003170/0001062993-26-003170-index.html
  published_at: '2026-06-12'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 6-K 0001062993-26-002969
  url: https://www.sec.gov/Archives/edgar/data/1817740/000106299326002969/0001062993-26-002969-index.html
  published_at: '2026-06-02'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0001817740
  classification_status: reported_sic
  entity_type: other
  name: Austin Gold Corp.
  sic: '1040'
  sic_description: Gold and Silver Ores
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: ac29b3088740739a2afb5e38c07f7b0423d7c427a5ffb1138ca364b599aa07d0
  url: https://data.sec.gov/submissions/CIK0001817740.json
listings:
- ticker: AUST
  exchange: NYSE_AMERICAN
  instrument_type: common_stock
research_filings:
- accession: 0001104659-26-035225
  filed: '2026-03-26'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1817740/000110465926035225/0001104659-26-035225-index.html
- accession: 0001104659-26-091322
  filed: '2026-08-06'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1817740/000110465926091322/0001104659-26-091322-index.html
research_progress:
  stage: pending
  input_sha256: 234608bcde3aa3ad59179322d850670d33ad3cbf8fabc1a98fc83c2ad501abb7
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
  source_url: https://data.sec.gov/submissions/CIK0001817740.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/5da532c3abee5b40a5400c5864c6f3f4593276d7/brain/companies/AUST/README.md
full_history_commit: 5da532c3abee5b40a5400c5864c6f3f4593276d7
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# AUST — Austin Gold Corp.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/5da532c3abee5b40a5400c5864c6f3f4593276d7/brain/companies/AUST/README.md)

## Business overview

Reported issuer name: **Austin Gold Corp.**. Stable SEC CIK: **0001817740**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| AUST | NYSE_AMERICAN | common_stock | 1 | [S01] |

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
- Forms observed in the retained filing inventory: 20-F, 424B3, 424B4, 6-K, 8-A12B, CERT, CORRESP, D, DRS, DRS/A, DRSLTR, EFFECT, F-3, S-1, S-1/A, S-8, SC 13D, SCHEDULE 13D/A, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:35:48.699166+00:00.

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
| 2026-08-06 | 6-K | 0001104659-26-091322 | — | [S03] |
| 2026-07-08 | EFFECT | 9999999995-26-002223 | — | [S04] |
| 2026-06-23 | F-3 | 0001104659-26-076502 | — | [S05] |
| 2026-06-12 | 6-K | 0001062993-26-003170 | — | [S06] |
| 2026-06-02 | 6-K | 0001062993-26-002969 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-28T16:09:02.154543+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001817740.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [6-K 0001104659-26-091322](https://www.sec.gov/Archives/edgar/data/1817740/000110465926091322/0001104659-26-091322-index.html) — published 2026-08-06; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [EFFECT 9999999995-26-002223](https://www.sec.gov/Archives/edgar/data/1817740/999999999526002223/9999999995-26-002223-index.html) — published 2026-07-08; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [F-3 0001104659-26-076502](https://www.sec.gov/Archives/edgar/data/1817740/000110465926076502/0001104659-26-076502-index.html) — published 2026-06-23; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [6-K 0001062993-26-003170](https://www.sec.gov/Archives/edgar/data/1817740/000106299326003170/0001062993-26-003170-index.html) — published 2026-06-12; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [6-K 0001062993-26-002969](https://www.sec.gov/Archives/edgar/data/1817740/000106299326002969/0001062993-26-002969-index.html) — published 2026-06-02; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261028-40722802424-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/5da532c3abee5b40a5400c5864c6f3f4593276d7/brain/companies/AUST/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
