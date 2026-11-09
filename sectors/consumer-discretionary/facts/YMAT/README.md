---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001875016
cik: 0001875016
company_name: J-Star Holding Co., Ltd.
tickers:
- YMAT
status: stub
canonical_reviewed: false
as_of: '2026-11-01'
updated_at: '2026-11-01T16:11:48.803754+00:00'
reviewed_at: null
coverage_release: coverage-20261101-41324509967-1
source_commit: 24b45739301817a91334ded2f20d99ded4cc7ea6
financial_history_available: false
curated_research: null
financial_gap:
  reason: foreign_reporting_adapter
  next_action: Add support for the observed 20-F, 40-F or 6-K reporting forms and
    verify the actual accounting taxonomy before normalization.
  observed_forms:
  - 20-F
  - '3'
  - 424B4
  - 6-K
  - 8-A12B
  - 8-A12B/A
  - CERT
  - CORRESP
  - DRS
  - DRS/A
  - DRSLTR
  - EFFECT
  - F-1
  - F-1/A
  - F-3
  - F-3/A
  - FWP
  - RW
  - S-8
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001875016.json
    sha256: 843a392b36f56ce16c4cbbaf5c48f7e1fffb53d7100d2817601dd332bf2c3b4c
    retrieved_at: '2026-10-24T13:22:51.759433+00:00'
    archive: &id001
      member: CIK0001875016.json
      sha256: 593fbbea6512ef5ec729a5e513c465fbedaac8a66602c0abe00d0ba5a4d18732
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
  url: https://data.sec.gov/submissions/CIK0001875016.json
  published_at: null
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 843a392b36f56ce16c4cbbaf5c48f7e1fffb53d7100d2817601dd332bf2c3b4c
- id: S03
  title: 6-K 0001493152-26-048239
  url: https://www.sec.gov/Archives/edgar/data/1875016/000149315226048239/0001493152-26-048239-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S04
  title: 6-K 0001493152-26-046580
  url: https://www.sec.gov/Archives/edgar/data/1875016/000149315226046580/0001493152-26-046580-index.html
  published_at: '2026-10-09'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S05
  title: 6-K 0001493152-26-044808
  url: https://www.sec.gov/Archives/edgar/data/1875016/000149315226044808/0001493152-26-044808-index.html
  published_at: '2026-09-29'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S06
  title: 6-K 0001493152-26-044624
  url: https://www.sec.gov/Archives/edgar/data/1875016/000149315226044624/0001493152-26-044624-index.html
  published_at: '2026-09-28'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S07
  title: EFFECT 9999999995-26-003042
  url: https://www.sec.gov/Archives/edgar/data/1875016/999999999526003042/9999999995-26-003042-index.html
  published_at: '2026-09-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S53
  url: https://www.sec.gov/Archives/edgar/data/1875016/000149315226048239/form6-k.htm
  title: 6-K 0001493152-26-048239
  published_at: '2026-10-23'
  retrieved_at: '2026-11-02T22:07:49.547642+00:00'
  sha256: 71c9859fc6b42d728de75226b7d3ef51916c629a686944a960199026a7578af5
- id: S54
  url: https://www.sec.gov/Archives/edgar/data/1875016/000149315226019802/form20-f.htm
  title: 20-F 0001493152-26-019802
  published_at: '2026-04-30'
  retrieved_at: '2026-11-02T22:07:47.275256+00:00'
  sha256: bde9cdf136dedb959df55de6333ef61bd80ef5e27f7e54713182cf9e02f5b619
issuer_classification:
  cik: 0001875016
  classification_status: reported_sic
  entity_type: other
  name: J-Star Holding Co., Ltd.
  sic: '3949'
  sic_description: Sporting & Athletic Goods, NEC
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 843a392b36f56ce16c4cbbaf5c48f7e1fffb53d7100d2817601dd332bf2c3b4c
  url: https://data.sec.gov/submissions/CIK0001875016.json
listings:
- ticker: YMAT
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001493152-26-019802
  filed: '2026-04-30'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1875016/000149315226019802/0001493152-26-019802-index.html
- accession: 0001493152-26-048239
  filed: '2026-10-23'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1875016/000149315226048239/0001493152-26-048239-index.html
research_progress:
  stage: evidence_collected
  input_sha256: 09368203c8353a03f30caa0552bbb963805e28c3e7c2d40f40c864cdb3f9c7f6
  last_attempt_at: '2026-11-02T22:04:14.646377+00:00'
  last_success_at: '2026-11-02T22:04:14.646377+00:00'
  next_retry_at: null
  source_set_current: true
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
  sector: consumer-discretionary
  method: project_sic_rule
  sic: '3949'
  sic_description: Sporting & Athletic Goods, NEC
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001875016.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/2a475d5f7d7de42ae2b318e51e43cda99027f72f/brain/companies/YMAT/README.md
full_history_commit: 2a475d5f7d7de42ae2b318e51e43cda99027f72f
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# YMAT — J-Star Holding Co., Ltd.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/2a475d5f7d7de42ae2b318e51e43cda99027f72f/brain/companies/YMAT/README.md)

## Business overview

Reported issuer name: **J-Star Holding Co., Ltd.**. Stable SEC CIK: **0001875016**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| YMAT | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 6-K, filed 2026-10-23, L4000:

> to operate our business; changes in customers’ preferences and needs; changes in competitive conditions and our ability to compete [S53]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 20-F, filed 2026-04-30, L3467:

> factories to the U.S. and Europe. We primarily generate revenue through three divisions and revenue streams, namely (i) sales of [S54]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 20-F, filed 2026-04-30, L1201:

> most of our products are manufactured in the PRC through outsourcing. Accordingly, our business, prospects, financial condition and results [S54]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 20-F, filed 2026-04-30, L1402:

> in China. As such, we may collect certain personal data from our customers in connection with our business and operations and we are [S54]

## Industry and value chain

SEC-reported SIC **3949**: Sporting & Athletic Goods, NEC. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 20-F, filed 2026-04-30, L1708:

> regulations related to import of raw materials or export of processed materials may result in fines and legal or administrative actions, [S54]

Navigation sector: **consumer-discretionary**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 20-F, filed 2026-04-30, L2163:

> so as to keep up with the market trends and industry competition. If we are unable to anticipate the evolving customer requirements and [S54]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 20-F, filed 2026-04-30, L655:

> censorship and other restriction on material which can be transmitted over the Internet, security, intellectual property, money laundering, [S54]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 20-F, filed 2026-04-30, L3374:

> line in order to expand our scope of carbon composite sporting goods to sports bicycles. In 2017, we produced our first electric bicycle [S54]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 6-K, filed 2026-10-23, L894:

> accompanying unaudited interim condensed consolidated financial statements were authorized for issuance by the Board of Directors on [S53]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 20-F, filed 2026-04-30, L638:

> to doing business in the PRC and Taiwan, and our listing, see “Item 3. Key Information—D. Risk Factors— Risks Related [S54]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 20-F, 3, 424B4, 6-K, 8-A12B, 8-A12B/A, CERT, CORRESP, DRS, DRS/A, DRSLTR, EFFECT, F-1, F-1/A, F-3, F-3/A, FWP, RW, S-8, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:36:16.475118+00:00.

### Research work queue

Collection stage: **evidence_collected**. Extracted evidence is not a reviewed conclusion. Daily collection resumes from durable state; unchanged accessions are reused.

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
| 2026-10-23 | 6-K | 0001493152-26-048239 | — | [S03] |
| 2026-10-09 | 6-K | 0001493152-26-046580 | — | [S04] |
| 2026-09-29 | 6-K | 0001493152-26-044808 | — | [S05] |
| 2026-09-28 | 6-K | 0001493152-26-044624 | — | [S06] |
| 2026-09-23 | EFFECT | 9999999995-26-003042 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-11-01T16:07:03.070084+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001875016.json) — published not supplied; retrieved 2026-10-24T13:22:51.759433+00:00.

[S03] [6-K 0001493152-26-048239](https://www.sec.gov/Archives/edgar/data/1875016/000149315226048239/0001493152-26-048239-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S04] [6-K 0001493152-26-046580](https://www.sec.gov/Archives/edgar/data/1875016/000149315226046580/0001493152-26-046580-index.html) — published 2026-10-09; retrieved 2026-10-24T13:22:51.759433+00:00.

[S05] [6-K 0001493152-26-044808](https://www.sec.gov/Archives/edgar/data/1875016/000149315226044808/0001493152-26-044808-index.html) — published 2026-09-29; retrieved 2026-10-24T13:22:51.759433+00:00.

[S06] [6-K 0001493152-26-044624](https://www.sec.gov/Archives/edgar/data/1875016/000149315226044624/0001493152-26-044624-index.html) — published 2026-09-28; retrieved 2026-10-24T13:22:51.759433+00:00.

[S07] [EFFECT 9999999995-26-003042](https://www.sec.gov/Archives/edgar/data/1875016/999999999526003042/9999999995-26-003042-index.html) — published 2026-09-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S53] [6-K 0001493152-26-048239](https://www.sec.gov/Archives/edgar/data/1875016/000149315226048239/form6-k.htm) — published 2026-10-23; retrieved 2026-11-02T22:07:49.547642+00:00.

[S54] [20-F 0001493152-26-019802](https://www.sec.gov/Archives/edgar/data/1875016/000149315226019802/form20-f.htm) — published 2026-04-30; retrieved 2026-11-02T22:07:47.275256+00:00.

Source release: `coverage-20261101-41324509967-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/2a475d5f7d7de42ae2b318e51e43cda99027f72f/brain/companies/YMAT/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
