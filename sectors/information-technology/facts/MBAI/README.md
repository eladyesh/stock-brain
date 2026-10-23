---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001610590
cik: 0001610590
company_name: MBody AI Ltd.
tickers:
- MBAI
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
  - 20-F/A
  - 25-NSE
  - '3'
  - 424B3
  - 424B4
  - 424B5
  - '425'
  - 6-K
  - 6-K/A
  - 8-A12B
  - CERT
  - CERTNAS
  - CORRESP
  - D
  - DRS
  - DRS/A
  - EFFECT
  - F-1
  - F-1/A
  - F-1MEF
  - F-3
  - F-3/A
  - FWP
  - NT 20-F
  - POS AM
  - S-8
  - S-8 POS
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13D
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001610590.json
    sha256: d2cd24d9c912213da05ee731f3c831bebcbc73642363d67cdde41cbabeaa1594
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001610590.json
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
  url: https://data.sec.gov/submissions/CIK0001610590.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: d2cd24d9c912213da05ee731f3c831bebcbc73642363d67cdde41cbabeaa1594
- id: S03
  title: EFFECT 9999999995-26-003085
  url: https://www.sec.gov/Archives/edgar/data/1610590/999999999526003085/9999999995-26-003085-index.html
  published_at: '2026-09-28'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: SCHEDULE 13D 0001213900-26-102336
  url: https://www.sec.gov/Archives/edgar/data/1610590/000121390026102336/0001213900-26-102336-index.html
  published_at: '2026-09-22'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: F-3 0001213900-26-102275
  url: https://www.sec.gov/Archives/edgar/data/1610590/000121390026102275/0001213900-26-102275-index.html
  published_at: '2026-09-22'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 6-K 0001213900-26-102251
  url: https://www.sec.gov/Archives/edgar/data/1610590/000121390026102251/0001213900-26-102251-index.html
  published_at: '2026-09-22'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 3 0001213900-26-101556
  url: https://www.sec.gov/Archives/edgar/data/1610590/000121390026101556/0001213900-26-101556-index.html
  published_at: '2026-09-18'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0001610590
  classification_status: reported_sic
  entity_type: other
  name: MBody AI Ltd.
  sic: '7373'
  sic_description: Services-Computer Integrated Systems Design
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: d2cd24d9c912213da05ee731f3c831bebcbc73642363d67cdde41cbabeaa1594
  url: https://data.sec.gov/submissions/CIK0001610590.json
listings:
- ticker: MBAI
  exchange: NASDAQ
  instrument_type: equity_candidate
research_filings:
- accession: 0001213900-26-048090
  filed: '2026-04-27'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1610590/000121390026048090/0001213900-26-048090-index.html
- accession: 0001178913-16-005022
  filed: '2016-04-07'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1610590/000117891316005022/0001178913-16-005022-index.html
- accession: 0001213900-26-102251
  filed: '2026-09-22'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1610590/000121390026102251/0001213900-26-102251-index.html
- accession: 0001213900-26-071326
  filed: '2026-06-24'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1610590/000121390026071326/0001213900-26-071326-index.html
- accession: 0001213900-24-031761
  filed: '2024-04-10'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1610590/000121390024031761/0001213900-24-031761-index.html
- accession: 0001178913-21-003302
  filed: '2021-10-29'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1610590/000117891321003302/0001178913-21-003302-index.html
- accession: 0001178913-18-002242
  filed: '2018-08-01'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1610590/000117891318002242/0001178913-18-002242-index.html
- accession: 0001178913-18-000734
  filed: '2018-03-01'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1610590/000117891318000734/0001178913-18-000734-index.html
- accession: 0001178913-17-002884
  filed: '2017-10-25'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1610590/000117891317002884/0001178913-17-002884-index.html
- accession: 0001178913-17-002882
  filed: '2017-10-25'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1610590/000117891317002882/0001178913-17-002882-index.html
- accession: 0001178913-17-002880
  filed: '2017-10-25'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1610590/000117891317002880/0001178913-17-002880-index.html
- accession: 0001178913-17-001597
  filed: '2017-05-24'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1610590/000117891317001597/0001178913-17-001597-index.html
research_progress:
  stage: pending
  input_sha256: c32742dff5416eb65d62aae19d72595533d5bed2a7fce9564f9b1cf1ab009e0e
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
  sic: '7373'
  sic_description: Services-Computer Integrated Systems Design
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001610590.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/d523cff21b18141b9a37cddd98ad6af6e1a30fa5/brain/companies/MBAI/README.md
full_history_commit: d523cff21b18141b9a37cddd98ad6af6e1a30fa5
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# MBAI — MBody AI Ltd.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/d523cff21b18141b9a37cddd98ad6af6e1a30fa5/brain/companies/MBAI/README.md)

## Business overview

Reported issuer name: **MBody AI Ltd.**. Stable SEC CIK: **0001610590**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| MBAI | NASDAQ | equity_candidate | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **7373**: Services-Computer Integrated Systems Design. [S02]

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
- Forms observed in the retained filing inventory: 20-F, 20-F/A, 25-NSE, 3, 424B3, 424B4, 424B5, 425, 6-K, 6-K/A, 8-A12B, CERT, CERTNAS, CORRESP, D, DRS, DRS/A, EFFECT, F-1, F-1/A, F-1MEF, F-3, F-3/A, FWP, NT 20-F, POS AM, S-8, S-8 POS, SC 13D, SC 13D/A, SC 13G, SC 13G/A, SCHEDULE 13D, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-23T14:31:44.747565+00:00.

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
| 2026-09-28 | EFFECT | 9999999995-26-003085 | — | [S03] |
| 2026-09-22 | SCHEDULE 13D | 0001213900-26-102336 | — | [S04] |
| 2026-09-22 | F-3 | 0001213900-26-102275 | — | [S05] |
| 2026-09-22 | 6-K | 0001213900-26-102251 | — | [S06] |
| 2026-09-18 | 3 | 0001213900-26-101556 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-23T14:17:54.530395+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001610590.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [EFFECT 9999999995-26-003085](https://www.sec.gov/Archives/edgar/data/1610590/999999999526003085/9999999995-26-003085-index.html) — published 2026-09-28; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [SCHEDULE 13D 0001213900-26-102336](https://www.sec.gov/Archives/edgar/data/1610590/000121390026102336/0001213900-26-102336-index.html) — published 2026-09-22; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [F-3 0001213900-26-102275](https://www.sec.gov/Archives/edgar/data/1610590/000121390026102275/0001213900-26-102275-index.html) — published 2026-09-22; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [6-K 0001213900-26-102251](https://www.sec.gov/Archives/edgar/data/1610590/000121390026102251/0001213900-26-102251-index.html) — published 2026-09-22; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [3 0001213900-26-101556](https://www.sec.gov/Archives/edgar/data/1610590/000121390026101556/0001213900-26-101556-index.html) — published 2026-09-18; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261023-39968262770-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/d523cff21b18141b9a37cddd98ad6af6e1a30fa5/brain/companies/MBAI/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
