---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001914805
cik: 0001914805
company_name: CBL International Ltd
tickers:
- BANL
status: stub
canonical_reviewed: false
as_of: '2026-10-30'
updated_at: '2026-10-30T16:05:25.650854+00:00'
reviewed_at: null
coverage_release: coverage-20261030-41085569265-1
source_commit: ef2ed016c2c344c23ee7fb991b25bf93660da77e
financial_history_available: false
curated_research: null
financial_gap:
  reason: foreign_reporting_adapter
  next_action: Add support for the observed 20-F, 40-F or 6-K reporting forms and
    verify the actual accounting taxonomy before normalization.
  observed_forms:
  - '144'
  - 20-F
  - '3'
  - 424B3
  - 424B4
  - 424B5
  - 6-K
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
  - SC 13G
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001914805.json
    sha256: 5c70b85f1485f9cb9992de43c8e9371306c1d398315de1e31858c838472e7e40
    retrieved_at: '2026-10-24T13:22:51.759433+00:00'
    archive: &id001
      member: CIK0001914805.json
      sha256: 593fbbea6512ef5ec729a5e513c465fbedaac8a66602c0abe00d0ba5a4d18732
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: nasdaqlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt
  published_at: null
  retrieved_at: '2026-10-30T16:00:11.183681+00:00'
  sha256: 64301e84a89de015f12206ec26fa4a677c38e33277e47d0b3a6b91e370e8d274
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001914805.json
  published_at: null
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 5c70b85f1485f9cb9992de43c8e9371306c1d398315de1e31858c838472e7e40
- id: S03
  title: 6-K 0001493152-26-048176
  url: https://www.sec.gov/Archives/edgar/data/1914805/000149315226048176/0001493152-26-048176-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S04
  title: SCHEDULE 13G/A 0001493152-26-047011
  url: https://www.sec.gov/Archives/edgar/data/1914805/000149315226047011/0001493152-26-047011-index.html
  published_at: '2026-10-14'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S05
  title: 144 0001493152-26-041435
  url: https://www.sec.gov/Archives/edgar/data/1914805/000149315226041435/0001493152-26-041435-index.html
  published_at: '2026-09-04'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S06
  title: 424B5 0001493152-26-040638
  url: https://www.sec.gov/Archives/edgar/data/1914805/000149315226040638/0001493152-26-040638-index.html
  published_at: '2026-08-28'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S07
  title: 6-K 0001493152-26-040637
  url: https://www.sec.gov/Archives/edgar/data/1914805/000149315226040637/0001493152-26-040637-index.html
  published_at: '2026-08-28'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S54
  url: https://www.sec.gov/Archives/edgar/data/1914805/000149315226017832/form20-f.htm
  title: 20-F 0001493152-26-017832
  published_at: '2026-04-17'
  retrieved_at: '2026-10-24T13:49:55.832398+00:00'
  sha256: 73bef201de89f60d64245680c5463af88d26498c9c3099d86869ea26f9924cc4
issuer_classification:
  cik: 0001914805
  classification_status: reported_sic
  entity_type: other
  name: CBL International Ltd
  sic: '5172'
  sic_description: Wholesale-Petroleum & Petroleum Products (No Bulk Stations)
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 5c70b85f1485f9cb9992de43c8e9371306c1d398315de1e31858c838472e7e40
  url: https://data.sec.gov/submissions/CIK0001914805.json
listings:
- ticker: BANL
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001493152-26-017832
  filed: '2026-04-17'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1914805/000149315226017832/0001493152-26-017832-index.html
- accession: 0001493152-26-048176
  filed: '2026-10-23'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1914805/000149315226048176/0001493152-26-048176-index.html
research_progress:
  stage: evidence_collected
  input_sha256: 6dace7a2c42b3216c853afa98fee98fd95974a626b391dcdfdf25fbd035d5480
  last_attempt_at: '2026-10-24T13:43:29.782673+00:00'
  last_success_at: '2026-10-24T13:43:29.782673+00:00'
  next_retry_at: null
  source_set_current: true
  evidence_topics:
  - business-overview
  - competitive-landscape
  - customers-and-end-markets
  - growth-drivers
  - industry-and-value-chain
  - management-and-governance
  - products-and-services
  - recent-developments
  - revenue-model-and-segments
  - risks-and-thesis-breakers
  derived_observations: 0
  model_draft: false
  reviewed: false
sector_assignment:
  sector: energy
  method: project_sic_rule
  sic: '5172'
  sic_description: Wholesale-Petroleum & Petroleum Products (No Bulk Stations)
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001914805.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/79888139fa1fe8ad3404e6bc04e318eee1474f73/brain/companies/BANL/README.md
full_history_commit: 79888139fa1fe8ad3404e6bc04e318eee1474f73
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# BANL — CBL International Ltd

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/79888139fa1fe8ad3404e6bc04e318eee1474f73/brain/companies/BANL/README.md)

## Business overview

Reported issuer name: **CBL International Ltd**. Stable SEC CIK: **0001914805**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| BANL | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 20-F, filed 2026-04-17, L721:

> risks, nor can we assess the impact of such risks on our business or the extent to which any risk, or combination of risks, may cause [S54]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 20-F, filed 2026-04-17, L6400:

> hence, the Company has only one reportable segment. The Company operates and manages its business as a single segment. [S54]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 20-F, filed 2026-04-17, L833:

> is no assurance that our top five customers will continue to use our services or that the Group can successfully maintain the relationship [S54]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 20-F, filed 2026-04-17, L766:

> handling and delivery of marine fuel, including biofuels, to our customers. Under our business model, we are not directly involved in [S54]

## Industry and value chain

SEC-reported SIC **5172**: Wholesale-Petroleum & Petroleum Products (No Bulk Stations). [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 20-F, filed 2026-04-17, L765:

> are a marine fuel logistics company and rely on our suppliers’ permits, licenses, and compliance with applicable laws for the physical [S54]

Navigation sector: **energy**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 20-F, filed 2026-04-17, L853:

> are exposed to the risk that our competitors may undercut marine fuel prices, which would adversely affect our Group’s business [S54]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 20-F, filed 2026-04-17, L1257:

> may delay or inhibit our ability to complete such transactions, which could adversely affect our ability to expand our business or maintain [S54]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 20-F, filed 2026-04-17, L150:

> received by any of the registrant’s executive officers during the relevant recovery period pursuant to §240.10D-1(b). ☐ [S54]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 20-F, filed 2026-04-17, L718:

> should read these statements in conjunction with the risks disclosed in “Item 3. Key Information—D. Risk Factors” of [S54]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 144, 20-F, 3, 424B3, 424B4, 424B5, 6-K, 8-A12B, CERT, CORRESP, D, DRS, DRS/A, DRSLTR, EFFECT, F-1, F-1/A, F-3, SC 13G, SCHEDULE 13G/A, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:36:22.391124+00:00.

### Research work queue

Collection stage: **evidence_collected**. Extracted evidence is not a reviewed conclusion. Daily collection resumes from durable state; unchanged accessions are reused.

- **Business overview** (source excerpts available; assess the claim): Explain what the company does, who pays it, and why the business exists. Cite primary sources.
- **Revenue model and segments** (source excerpts available; assess the claim): Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.
- **Products and services** (source excerpts available; assess the claim): Describe the main products, customer problems solved, distribution, and product dependencies.
- **Customers and end markets** (source excerpts available; assess the claim): Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.
- **Industry and value chain** (source excerpts available; assess the claim): Place the company among suppliers, distribution channels, customers, and substitutes. Explain cyclicality and supply constraints.
- **Competitive landscape** (source excerpts available; assess the claim): Identify direct competitors and alternatives. Compare specific products or business segments, with sources.
- **Moat and differentiation** (evidence or analysis still needed): Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.
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
| 2026-10-23 | 6-K | 0001493152-26-048176 | — | [S03] |
| 2026-10-14 | SCHEDULE 13G/A | 0001493152-26-047011 | — | [S04] |
| 2026-09-04 | 144 | 0001493152-26-041435 | — | [S05] |
| 2026-08-28 | 424B5 | 0001493152-26-040638 | — | [S06] |
| 2026-08-28 | 6-K | 0001493152-26-040637 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-30T16:00:11.183681+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001914805.json) — published not supplied; retrieved 2026-10-24T13:22:51.759433+00:00.

[S03] [6-K 0001493152-26-048176](https://www.sec.gov/Archives/edgar/data/1914805/000149315226048176/0001493152-26-048176-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S04] [SCHEDULE 13G/A 0001493152-26-047011](https://www.sec.gov/Archives/edgar/data/1914805/000149315226047011/0001493152-26-047011-index.html) — published 2026-10-14; retrieved 2026-10-24T13:22:51.759433+00:00.

[S05] [144 0001493152-26-041435](https://www.sec.gov/Archives/edgar/data/1914805/000149315226041435/0001493152-26-041435-index.html) — published 2026-09-04; retrieved 2026-10-24T13:22:51.759433+00:00.

[S06] [424B5 0001493152-26-040638](https://www.sec.gov/Archives/edgar/data/1914805/000149315226040638/0001493152-26-040638-index.html) — published 2026-08-28; retrieved 2026-10-24T13:22:51.759433+00:00.

[S07] [6-K 0001493152-26-040637](https://www.sec.gov/Archives/edgar/data/1914805/000149315226040637/0001493152-26-040637-index.html) — published 2026-08-28; retrieved 2026-10-24T13:22:51.759433+00:00.

[S54] [20-F 0001493152-26-017832](https://www.sec.gov/Archives/edgar/data/1914805/000149315226017832/form20-f.htm) — published 2026-04-17; retrieved 2026-10-24T13:49:55.832398+00:00.

Source release: `coverage-20261030-41085569265-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/79888139fa1fe8ad3404e6bc04e318eee1474f73/brain/companies/BANL/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
