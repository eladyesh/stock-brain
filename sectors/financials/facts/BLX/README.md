---
schema_version: 1
document_type: company_facts
company_id: company-cik-0000890541
cik: 0000890541
company_name: BLADEX, INC.
tickers:
- BLX
status: stub
canonical_reviewed: false
as_of: '2026-10-30'
updated_at: '2026-10-30T16:05:25.650854+00:00'
reviewed_at: null
coverage_release: coverage-20261030-41085569265-1
source_commit: f9a34108789a82bf7c75f9d65a0e9552aa5552db
financial_history_available: false
curated_research: null
financial_gap:
  reason: foreign_reporting_adapter
  next_action: Add support for the observed 20-F, 40-F or 6-K reporting forms and
    verify the actual accounting taxonomy before normalization.
  observed_forms:
  - 20-F
  - 20-F/A
  - '4'
  - 424B3
  - 6-K
  - 6-K/A
  - CORRESP
  - F-2
  - F-2/A
  - S-8
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0000890541.json
    sha256: 18cab4aa28bb14cb4f04e0a5906eb7c5a05e3b3aef886136e931b0d0cbcd8bfa
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0000890541.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: otherlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt
  published_at: null
  retrieved_at: '2026-10-30T16:00:12.358089+00:00'
  sha256: a960a0bfc5439fac9e467fe07ef1f44afe893ba2afc3297648321a80ce09971e
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0000890541.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 18cab4aa28bb14cb4f04e0a5906eb7c5a05e3b3aef886136e931b0d0cbcd8bfa
- id: S03
  title: 6-K 0001628280-26-062304
  url: https://www.sec.gov/Archives/edgar/data/890541/000162828026062304/0001628280-26-062304-index.html
  published_at: '2026-09-16'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 4 0000890541-26-000011
  url: https://www.sec.gov/Archives/edgar/data/890541/000089054126000011/0000890541-26-000011-index.html
  published_at: '2026-08-31'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 4 0000890541-26-000009
  url: https://www.sec.gov/Archives/edgar/data/890541/000089054126000009/0000890541-26-000009-index.html
  published_at: '2026-08-24'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 6-K 0001628280-26-051633
  url: https://www.sec.gov/Archives/edgar/data/890541/000162828026051633/0001628280-26-051633-index.html
  published_at: '2026-08-03'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 6-K 0001628280-26-050270
  url: https://www.sec.gov/Archives/edgar/data/890541/000162828026050270/0001628280-26-050270-index.html
  published_at: '2026-07-29'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0000890541
  classification_status: reported_sic
  entity_type: other
  name: BLADEX, INC.
  sic: '6029'
  sic_description: Commercial Banks, NEC
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 18cab4aa28bb14cb4f04e0a5906eb7c5a05e3b3aef886136e931b0d0cbcd8bfa
  url: https://data.sec.gov/submissions/CIK0000890541.json
listings:
- ticker: BLX
  exchange: NYSE
  instrument_type: common_stock
research_filings:
- accession: 0001628280-26-026056
  filed: '2026-04-20'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/890541/000162828026026056/0001628280-26-026056-index.html
- accession: 0001144204-08-012200
  filed: '2008-02-28'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/890541/000114420408012200/0001144204-08-012200-index.html
- accession: 0001193125-03-005460
  filed: '2003-05-15'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/890541/000119312503005460/0001193125-03-005460-index.html
- accession: 0001628280-26-062304
  filed: '2026-09-16'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/890541/000162828026062304/0001628280-26-062304-index.html
- accession: 0001144204-18-063024
  filed: '2018-12-04'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/890541/000114420418063024/0001144204-18-063024-index.html
- accession: 0001144204-16-112090
  filed: '2016-07-08'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/890541/000114420416112090/0001144204-16-112090-index.html
- accession: 0001144204-16-106183
  filed: '2016-06-01'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/890541/000114420416106183/0001144204-16-106183-index.html
research_progress:
  stage: pending
  input_sha256: f871aec6356e65d48b3a89fc5c3c86bcfc8c1833867684d5f5641bf83df54a34
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
  derived_observations: 0
  model_draft: false
  reviewed: false
sector_assignment:
  sector: financials
  method: project_sic_rule
  sic: '6029'
  sic_description: Commercial Banks, NEC
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0000890541.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/1b4771bc41dec553e210323f72d9bfc908288c04/brain/companies/BLX/README.md
full_history_commit: 1b4771bc41dec553e210323f72d9bfc908288c04
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# BLX — BLADEX, INC.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/1b4771bc41dec553e210323f72d9bfc908288c04/brain/companies/BLX/README.md)

## Business overview

Reported issuer name: **BLADEX, INC.**. Stable SEC CIK: **0000890541**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| BLX | NYSE | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **6029**: Commercial Banks, NEC. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **financials**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

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
- Forms observed in the retained filing inventory: 20-F, 20-F/A, 4, 424B3, 6-K, 6-K/A, CORRESP, F-2, F-2/A, S-8, SC 13G, SC 13G/A, SCHEDULE 13G, SCHEDULE 13G/A, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:30:05.414143+00:00.

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
| 2026-09-16 | 6-K | 0001628280-26-062304 | — | [S03] |
| 2026-08-31 | 4 | 0000890541-26-000011 | — | [S04] |
| 2026-08-24 | 4 | 0000890541-26-000009 | — | [S05] |
| 2026-08-03 | 6-K | 0001628280-26-051633 | — | [S06] |
| 2026-07-29 | 6-K | 0001628280-26-050270 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-30T16:00:12.358089+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0000890541.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [6-K 0001628280-26-062304](https://www.sec.gov/Archives/edgar/data/890541/000162828026062304/0001628280-26-062304-index.html) — published 2026-09-16; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [4 0000890541-26-000011](https://www.sec.gov/Archives/edgar/data/890541/000089054126000011/0000890541-26-000011-index.html) — published 2026-08-31; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [4 0000890541-26-000009](https://www.sec.gov/Archives/edgar/data/890541/000089054126000009/0000890541-26-000009-index.html) — published 2026-08-24; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [6-K 0001628280-26-051633](https://www.sec.gov/Archives/edgar/data/890541/000162828026051633/0001628280-26-051633-index.html) — published 2026-08-03; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [6-K 0001628280-26-050270](https://www.sec.gov/Archives/edgar/data/890541/000162828026050270/0001628280-26-050270-index.html) — published 2026-07-29; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261030-41085569265-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/1b4771bc41dec553e210323f72d9bfc908288c04/brain/companies/BLX/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
