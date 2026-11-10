---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001903870
cik: 0001903870
company_name: Forafric Global PLC
tickers:
- AFRI
status: stub
canonical_reviewed: false
as_of: '2026-11-01'
updated_at: '2026-11-01T16:11:48.803754+00:00'
reviewed_at: null
coverage_release: coverage-20261101-41324509967-1
source_commit: 6dea3be4625120db9da80155a96f14ed62690190
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
  - '425'
  - 6-K
  - 8-A12B
  - 8-K
  - CERT
  - CORRESP
  - EFFECT
  - F-1
  - F-1/A
  - NT 20-F
  - POS AM
  - S-4
  - S-4/A
  - S-8
  - SC 13D
  - SC 13G
  - SC 13G/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001903870.json
    sha256: e54ca06a42e2f080256ab606087e9dfe7c07ef067e1b0b54f01bc855d2ed0d0a
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001903870.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: nasdaqlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt
  published_at: null
  retrieved_at: '2026-11-01T16:07:03.070084+00:00'
  sha256: b160a2f2814e5df68d7e414fba70f808f7ad3d20cbbdd167a8a2e38a10044168
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001903870.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: e54ca06a42e2f080256ab606087e9dfe7c07ef067e1b0b54f01bc855d2ed0d0a
- id: S03
  title: 6-K 0001493152-26-046143
  url: https://www.sec.gov/Archives/edgar/data/1903870/000149315226046143/0001493152-26-046143-index.html
  published_at: '2026-10-07'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 6-K 0001493152-26-036191
  url: https://www.sec.gov/Archives/edgar/data/1903870/000149315226036191/0001493152-26-036191-index.html
  published_at: '2026-08-05'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 6-K 0001493152-26-033535
  url: https://www.sec.gov/Archives/edgar/data/1903870/000149315226033535/0001493152-26-033535-index.html
  published_at: '2026-07-16'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 20-F 0001493152-26-023781
  url: https://www.sec.gov/Archives/edgar/data/1903870/000149315226023781/0001493152-26-023781-index.html
  published_at: '2026-05-15'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: NT 20-F 0001493152-26-020589
  url: https://www.sec.gov/Archives/edgar/data/1903870/000149315226020589/0001493152-26-020589-index.html
  published_at: '2026-04-30'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S53
  url: https://www.sec.gov/Archives/edgar/data/1903870/000149315226023781/form20-f.htm
  title: 20-F 0001493152-26-023781
  published_at: '2026-05-15'
  retrieved_at: '2026-11-06T19:55:24.160482+00:00'
  sha256: f146e7074ec3a26ae2fa00633155e71033536c414fb475d3737bb37df460b192
issuer_classification:
  cik: 0001903870
  classification_status: reported_sic
  entity_type: other
  name: Forafric Global PLC
  sic: '2040'
  sic_description: Grain Mill Products
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: e54ca06a42e2f080256ab606087e9dfe7c07ef067e1b0b54f01bc855d2ed0d0a
  url: https://data.sec.gov/submissions/CIK0001903870.json
listings:
- ticker: AFRI
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001493152-26-023781
  filed: '2026-05-15'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1903870/000149315226023781/0001493152-26-023781-index.html
- accession: 0001493152-26-046143
  filed: '2026-10-07'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1903870/000149315226046143/0001493152-26-046143-index.html
- accession: 0001493152-22-016864
  filed: '2022-06-15'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/1903870/000149315222016864/0001493152-22-016864-index.html
research_progress:
  stage: retry
  input_sha256: a18e608f56c54503900874d6b06d8d66652358480d03ad313db0bd982ecf2ef1
  last_attempt_at: '2026-11-06T19:49:30.346586+00:00'
  last_success_at: null
  next_retry_at: '2026-11-07T19:49:30.346586+00:00'
  source_set_current: false
  evidence_topics:
  - business-overview
  - competitive-landscape
  - customers-and-end-markets
  - growth-drivers
  - industry-and-value-chain
  - management-and-governance
  - moat-and-differentiation
  - products-and-services
  - recent-developments
  - revenue-model-and-segments
  - risks-and-thesis-breakers
  derived_observations: 0
  model_draft: false
  reviewed: false
sector_assignment:
  sector: consumer-staples
  method: project_sic_rule
  sic: '2040'
  sic_description: Grain Mill Products
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001903870.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/876d144f6387664050d096ed943ae2c26137a2cb/brain/companies/AFRI/README.md
full_history_commit: 876d144f6387664050d096ed943ae2c26137a2cb
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# AFRI — Forafric Global PLC

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/876d144f6387664050d096ed943ae2c26137a2cb/brain/companies/AFRI/README.md)

## Business overview

Reported issuer name: **Forafric Global PLC**. Stable SEC CIK: **0001903870**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| AFRI | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 20-F, filed 2026-05-15, L441; prior source set, update pending:

> cautionary statements. Other sections of this annual report include additional factors which could adversely affect our business and [S53]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 20-F, filed 2026-05-15, L7191; prior source set, update pending:

> on a segment-level basis. The Company has designated reportable segments based on how management views its business. The Company does [S53]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 20-F, filed 2026-05-15, L572; prior source set, update pending:

> may not be able to retain existing customers, attract new customers, expand product offerings, and increase processed volumes and [S53]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 20-F, filed 2026-05-15, L922; prior source set, update pending:

> brands, reputation and relationships with our customers. None of such persons is subject to long-term written employment arrangements. [S53]

## Industry and value chain

SEC-reported SIC **2040**: Grain Mill Products. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 20-F, filed 2026-05-15, L773; prior source set, update pending:

> we cannot control the average selling price of our finished products, any increase in the cost of raw materials has a direct impact on [S53]

Navigation sector: **consumer-staples**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 20-F, filed 2026-05-15, L1032; prior source set, update pending:

> face significant competition in each of our businesses, and we have numerous competitors, some of which are larger and have greater financial [S53]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 20-F, filed 2026-05-15, L1043; prior source set, update pending:

> ordinary course of business, we collect, store and transmit confidential information (including but not limited to intellectual property, [S53]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 20-F, filed 2026-05-15, L813; prior source set, update pending:

> are a global business with all of our assets and operations located outside the United States. In addition, part of our strategy involves [S53]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 20-F, filed 2026-05-15, L138; prior source set, update pending:

> received by any of the registrant’s executive officers during the relevant recovery period pursuant to §240.10D-1(b). ☐ [S53]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 20-F, filed 2026-05-15, L442; prior source set, update pending:

> financial performance. New risk factors and uncertainties emerge from time to time, and it is not possible for our management to predict [S53]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 20-F, 3, 424B3, 424B4, 425, 6-K, 8-A12B, 8-K, CERT, CORRESP, EFFECT, F-1, F-1/A, NT 20-F, POS AM, S-4, S-4/A, S-8, SC 13D, SC 13G, SC 13G/A, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:36:21.188932+00:00.

### Research work queue

Collection stage: **retry**. Extracted evidence is not a reviewed conclusion. Daily collection resumes from durable state; unchanged accessions are reused.

- **Business overview** (source excerpts available; assess the claim): Explain what the company does, who pays it, and why the business exists. Cite primary sources.
- **Revenue model and segments** (source excerpts available; assess the claim): Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.
- **Products and services** (source excerpts available; assess the claim): Describe the main products, customer problems solved, distribution, and product dependencies.
- **Customers and end markets** (source excerpts available; assess the claim): Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.
- **Industry and value chain** (source excerpts available; assess the claim): Place the company among suppliers, distribution channels, customers, and substitutes. Explain cyclicality and supply constraints.
- **Competitive landscape** (source excerpts available; assess the claim): Identify direct competitors and alternatives. Compare specific products or business segments, with sources.
- **Moat and differentiation** (source excerpts available; assess the claim): Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.
- **Growth drivers** (source excerpts available; assess the claim): Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.
- **Financial performance** (evidence or analysis still needed): Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.
- **Balance sheet and capital allocation** (evidence or analysis still needed): Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.
- **Management and governance** (source excerpts available; assess the claim): Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.
- **Valuation context** (evidence or analysis still needed): Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.
- **Catalysts** (evidence or analysis still needed): List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.
- **Risks and thesis breakers** (source excerpts available; assess the claim): Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.
- **Scenarios and open questions** (evidence or analysis still needed): Separate bull, base, and bear assumptions from facts. Record missing data, disputed evidence, and research questions without inventing answers.
- **Relationships and themes** (evidence or analysis still needed): Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.
- **Recent developments** (source excerpts available; assess the claim): Keep a dated, source-backed log of material changes. Distinguish the event date from the article date and explain what changed in the profile.

Calculation gaps: Validated financial history is missing.

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest five available filing metadata records; document bodies have not been analyzed here.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-10-07 | 6-K | 0001493152-26-046143 | — | [S03] |
| 2026-08-05 | 6-K | 0001493152-26-036191 | — | [S04] |
| 2026-07-16 | 6-K | 0001493152-26-033535 | — | [S05] |
| 2026-05-15 | 20-F | 0001493152-26-023781 | — | [S06] |
| 2026-04-30 | NT 20-F | 0001493152-26-020589 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-11-01T16:07:03.070084+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001903870.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [6-K 0001493152-26-046143](https://www.sec.gov/Archives/edgar/data/1903870/000149315226046143/0001493152-26-046143-index.html) — published 2026-10-07; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [6-K 0001493152-26-036191](https://www.sec.gov/Archives/edgar/data/1903870/000149315226036191/0001493152-26-036191-index.html) — published 2026-08-05; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [6-K 0001493152-26-033535](https://www.sec.gov/Archives/edgar/data/1903870/000149315226033535/0001493152-26-033535-index.html) — published 2026-07-16; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [20-F 0001493152-26-023781](https://www.sec.gov/Archives/edgar/data/1903870/000149315226023781/0001493152-26-023781-index.html) — published 2026-05-15; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [NT 20-F 0001493152-26-020589](https://www.sec.gov/Archives/edgar/data/1903870/000149315226020589/0001493152-26-020589-index.html) — published 2026-04-30; retrieved 2026-10-23T08:33:02.691743+00:00.

[S53] [20-F 0001493152-26-023781](https://www.sec.gov/Archives/edgar/data/1903870/000149315226023781/form20-f.htm) — published 2026-05-15; retrieved 2026-11-06T19:55:24.160482+00:00.

Source release: `coverage-20261101-41324509967-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/876d144f6387664050d096ed943ae2c26137a2cb/brain/companies/AFRI/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
