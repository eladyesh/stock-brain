---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001894693
cik: 0001894693
company_name: SaverOne 2014 Ltd.
tickers:
- SVRE
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
  - 20-F
  - '3'
  - '4'
  - 424B3
  - 424B4
  - 424B5
  - 6-K
  - 6-K/A
  - 8-A12B
  - CERT
  - CORRESP
  - D
  - DRS
  - DRS/A
  - DRSLTR
  - EFFECT
  - F-1
  - F-1/A
  - F-3
  - F-3/A
  - FWP
  - POS AM
  - S-8
  - SC 13D
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13D
  - SCHEDULE 13D/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001894693.json
    sha256: 531c447d5d6fa958ca999ecc1404e440fa6fa7dc6d63c6a991361ca11719d4fb
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001894693.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: nasdaqlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt
  published_at: null
  retrieved_at: '2026-10-23T14:17:54.530395+00:00'
  sha256: a31379ea4791bd232005b22547c9cfa517e0cb9e9f14ff7091be845f143d5c71
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001894693.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 531c447d5d6fa958ca999ecc1404e440fa6fa7dc6d63c6a991361ca11719d4fb
- id: S03
  title: EFFECT 9999999995-26-003203
  url: https://www.sec.gov/Archives/edgar/data/1894693/999999999526003203/9999999995-26-003203-index.html
  published_at: '2026-10-09'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: EFFECT 9999999995-26-003146
  url: https://www.sec.gov/Archives/edgar/data/1894693/999999999526003146/9999999995-26-003146-index.html
  published_at: '2026-10-05'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 6-K 0001213900-26-106114
  url: https://www.sec.gov/Archives/edgar/data/1894693/000121390026106114/0001213900-26-106114-index.html
  published_at: '2026-10-02'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 6-K 0001213900-26-104319
  url: https://www.sec.gov/Archives/edgar/data/1894693/000121390026104319/0001213900-26-104319-index.html
  published_at: '2026-09-29'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: POS AM 0001213900-26-104160
  url: https://www.sec.gov/Archives/edgar/data/1894693/000121390026104160/0001213900-26-104160-index.html
  published_at: '2026-09-28'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0001894693
  classification_status: reported_sic
  entity_type: other
  name: SaverOne 2014 Ltd.
  sic: '7371'
  sic_description: Services-Computer Programming Services
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 531c447d5d6fa958ca999ecc1404e440fa6fa7dc6d63c6a991361ca11719d4fb
  url: https://data.sec.gov/submissions/CIK0001894693.json
listings:
- ticker: SVRE
  exchange: NASDAQ
  instrument_type: depositary_receipt
research_filings:
- accession: 0001213900-26-035545
  filed: '2026-03-27'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1894693/000121390026035545/0001213900-26-035545-index.html
- accession: 0001213900-26-106114
  filed: '2026-10-02'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1894693/000121390026106114/0001213900-26-106114-index.html
- accession: 0001213900-25-015508
  filed: '2025-02-20'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1894693/000121390025015508/0001213900-25-015508-index.html
- accession: 0001213900-25-015435
  filed: '2025-02-20'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1894693/000121390025015435/0001213900-25-015435-index.html
- accession: 0001213900-24-073357
  filed: '2024-08-28'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1894693/000121390024073357/0001213900-24-073357-index.html
- accession: 0001213900-23-083624
  filed: '2023-11-06'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1894693/000121390023083624/0001213900-23-083624-index.html
research_progress:
  stage: pending
  input_sha256: f1aa7da09b5985ce219048f51b0d900d34f1b290543624f741186b036cd310cc
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
  derived_observations: 0
  model_draft: false
  reviewed: false
sector_assignment:
  sector: information-technology
  method: project_sic_rule
  sic: '7371'
  sic_description: Services-Computer Programming Services
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001894693.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/d523cff21b18141b9a37cddd98ad6af6e1a30fa5/brain/companies/SVRE/README.md
full_history_commit: d523cff21b18141b9a37cddd98ad6af6e1a30fa5
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# SVRE — SaverOne 2014 Ltd.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/d523cff21b18141b9a37cddd98ad6af6e1a30fa5/brain/companies/SVRE/README.md)

## Business overview

Reported issuer name: **SaverOne 2014 Ltd.**. Stable SEC CIK: **0001894693**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| SVRE | NASDAQ | depositary_receipt | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **7371**: Services-Computer Programming Services. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **information-technology**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

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
- Forms observed in the retained filing inventory: 20-F, 3, 4, 424B3, 424B4, 424B5, 6-K, 6-K/A, 8-A12B, CERT, CORRESP, D, DRS, DRS/A, DRSLTR, EFFECT, F-1, F-1/A, F-3, F-3/A, FWP, POS AM, S-8, SC 13D, SC 13G, SC 13G/A, SCHEDULE 13D, SCHEDULE 13D/A, SCHEDULE 13G, SCHEDULE 13G/A, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-23T14:34:15.770297+00:00.

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
| 2026-10-09 | EFFECT | 9999999995-26-003203 | — | [S03] |
| 2026-10-05 | EFFECT | 9999999995-26-003146 | — | [S04] |
| 2026-10-02 | 6-K | 0001213900-26-106114 | — | [S05] |
| 2026-09-29 | 6-K | 0001213900-26-104319 | — | [S06] |
| 2026-09-28 | POS AM | 0001213900-26-104160 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-23T14:17:54.530395+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001894693.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [EFFECT 9999999995-26-003203](https://www.sec.gov/Archives/edgar/data/1894693/999999999526003203/9999999995-26-003203-index.html) — published 2026-10-09; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [EFFECT 9999999995-26-003146](https://www.sec.gov/Archives/edgar/data/1894693/999999999526003146/9999999995-26-003146-index.html) — published 2026-10-05; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [6-K 0001213900-26-106114](https://www.sec.gov/Archives/edgar/data/1894693/000121390026106114/0001213900-26-106114-index.html) — published 2026-10-02; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [6-K 0001213900-26-104319](https://www.sec.gov/Archives/edgar/data/1894693/000121390026104319/0001213900-26-104319-index.html) — published 2026-09-29; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [POS AM 0001213900-26-104160](https://www.sec.gov/Archives/edgar/data/1894693/000121390026104160/0001213900-26-104160-index.html) — published 2026-09-28; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261023-39968262770-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/d523cff21b18141b9a37cddd98ad6af6e1a30fa5/brain/companies/SVRE/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
