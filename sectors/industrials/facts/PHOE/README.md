---
schema_version: 1
document_type: company_facts
company_id: company-cik-0002035709
cik: 0002035709
company_name: Phoenix Asia Holdings Ltd
tickers:
- PHOE
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
  - '3'
  - 424B3
  - 424B4
  - 6-K
  - 8-A12B
  - CERT
  - CORRESP
  - DRS
  - DRS/A
  - DRSLTR
  - EFFECT
  - F-1
  - F-1/A
  - FWP
  - NT 20-F
  - S-8
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0002035709.json
    sha256: 03f2be9b7dc731eab66b086704f913dced8341010b6ea104456372bb0a5d66ee
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0002035709.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: nasdaqlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt
  published_at: null
  retrieved_at: '2026-10-29T16:14:13.115716+00:00'
  sha256: 0695ffec283534755d4efe90771a9cacee840d7affb7ba717f62899195a301c6
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0002035709.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 03f2be9b7dc731eab66b086704f913dced8341010b6ea104456372bb0a5d66ee
- id: S03
  title: 20-F 0001493152-26-038397
  url: https://www.sec.gov/Archives/edgar/data/2035709/000149315226038397/0001493152-26-038397-index.html
  published_at: '2026-08-14'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: NT 20-F 0001493152-26-035552
  url: https://www.sec.gov/Archives/edgar/data/2035709/000149315226035552/0001493152-26-035552-index.html
  published_at: '2026-07-31'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 6-K 0001493152-26-021113
  url: https://www.sec.gov/Archives/edgar/data/2035709/000149315226021113/0001493152-26-021113-index.html
  published_at: '2026-05-04'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 3 0001493152-26-016687
  url: https://www.sec.gov/Archives/edgar/data/2035709/000149315226016687/0001493152-26-016687-index.html
  published_at: '2026-04-15'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 3 0001493152-26-016043
  url: https://www.sec.gov/Archives/edgar/data/2035709/000149315226016043/0001493152-26-016043-index.html
  published_at: '2026-04-10'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0002035709
  classification_status: reported_sic
  entity_type: other
  name: Phoenix Asia Holdings Ltd
  sic: '1700'
  sic_description: Construction - Special Trade Contractors
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 03f2be9b7dc731eab66b086704f913dced8341010b6ea104456372bb0a5d66ee
  url: https://data.sec.gov/submissions/CIK0002035709.json
listings:
- ticker: PHOE
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001493152-26-038397
  filed: '2026-08-14'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/2035709/000149315226038397/0001493152-26-038397-index.html
- accession: 0001493152-26-021113
  filed: '2026-05-04'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/2035709/000149315226021113/0001493152-26-021113-index.html
research_progress:
  stage: pending
  input_sha256: 08a0b84f9e768f75a30d76969fd510ae30a16833d4645d5369a586c54ea6b146
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
  sic: '1700'
  sic_description: Construction - Special Trade Contractors
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0002035709.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/c26f59bc72c00102d2490e95b07449f8cd848491/brain/companies/PHOE/README.md
full_history_commit: c26f59bc72c00102d2490e95b07449f8cd848491
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# PHOE — Phoenix Asia Holdings Ltd

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/c26f59bc72c00102d2490e95b07449f8cd848491/brain/companies/PHOE/README.md)

## Business overview

Reported issuer name: **Phoenix Asia Holdings Ltd**. Stable SEC CIK: **0002035709**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| PHOE | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **1700**: Construction - Special Trade Contractors. [S02]

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
- Forms observed in the retained filing inventory: 20-F, 3, 424B3, 424B4, 6-K, 8-A12B, CERT, CORRESP, DRS, DRS/A, DRSLTR, EFFECT, F-1, F-1/A, FWP, NT 20-F, S-8, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:36:35.614383+00:00.

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
| 2026-08-14 | 20-F | 0001493152-26-038397 | — | [S03] |
| 2026-07-31 | NT 20-F | 0001493152-26-035552 | — | [S04] |
| 2026-05-04 | 6-K | 0001493152-26-021113 | — | [S05] |
| 2026-04-15 | 3 | 0001493152-26-016687 | — | [S06] |
| 2026-04-10 | 3 | 0001493152-26-016043 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-29T16:14:13.115716+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0002035709.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [20-F 0001493152-26-038397](https://www.sec.gov/Archives/edgar/data/2035709/000149315226038397/0001493152-26-038397-index.html) — published 2026-08-14; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [NT 20-F 0001493152-26-035552](https://www.sec.gov/Archives/edgar/data/2035709/000149315226035552/0001493152-26-035552-index.html) — published 2026-07-31; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [6-K 0001493152-26-021113](https://www.sec.gov/Archives/edgar/data/2035709/000149315226021113/0001493152-26-021113-index.html) — published 2026-05-04; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [3 0001493152-26-016687](https://www.sec.gov/Archives/edgar/data/2035709/000149315226016687/0001493152-26-016687-index.html) — published 2026-04-15; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [3 0001493152-26-016043](https://www.sec.gov/Archives/edgar/data/2035709/000149315226016043/0001493152-26-016043-index.html) — published 2026-04-10; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261029-40909364006-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/c26f59bc72c00102d2490e95b07449f8cd848491/brain/companies/PHOE/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
