---
schema_version: 1
document_type: company_facts
company_id: company-cik-0002009233
cik: 0002009233
company_name: Agroz Inc.
tickers:
- AGRZ
status: stub
canonical_reviewed: false
as_of: '2026-11-01'
updated_at: '2026-11-01T16:11:48.803754+00:00'
reviewed_at: null
coverage_release: coverage-20261101-41324509967-1
source_commit: da985d7cdd310eab261be4fd3662836a26873702
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
  - NT 20-F
  - POS AM
  - SCHEDULE 13D
  - SCHEDULE 13G
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0002009233.json
    sha256: 1a14550bec692bb7488b52089a23636902e191c6e40988418d2df6395b780670
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0002009233.json
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
  url: https://data.sec.gov/submissions/CIK0002009233.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 1a14550bec692bb7488b52089a23636902e191c6e40988418d2df6395b780670
- id: S03
  title: 20-F 0001213900-26-104158
  url: https://www.sec.gov/Archives/edgar/data/2009233/000121390026104158/0001213900-26-104158-index.html
  published_at: '2026-09-28'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 6-K 0001213900-26-097279
  url: https://www.sec.gov/Archives/edgar/data/2009233/000121390026097279/0001213900-26-097279-index.html
  published_at: '2026-09-03'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 6-K 0001213900-26-073402
  url: https://www.sec.gov/Archives/edgar/data/2009233/000121390026073402/0001213900-26-073402-index.html
  published_at: '2026-06-30'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 6-K 0001213900-26-062816
  url: https://www.sec.gov/Archives/edgar/data/2009233/000121390026062816/0001213900-26-062816-index.html
  published_at: '2026-05-29'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 6-K 0001213900-26-058726
  url: https://www.sec.gov/Archives/edgar/data/2009233/000121390026058726/0001213900-26-058726-index.html
  published_at: '2026-05-19'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S53
  url: https://www.sec.gov/Archives/edgar/data/2009233/000121390026104158/ea0306404-20f_agrozinc.htm
  title: 20-F 0001213900-26-104158
  published_at: '2026-09-28'
  retrieved_at: '2026-11-07T18:01:34.987536+00:00'
  sha256: da725306a3ee3684f47733371983c63578717bc9aa0749b89a59aef122bc4f7c
issuer_classification:
  cik: 0002009233
  classification_status: reported_sic
  entity_type: other
  name: Agroz Inc.
  sic: '0100'
  sic_description: Agricultural Production-Crops
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 1a14550bec692bb7488b52089a23636902e191c6e40988418d2df6395b780670
  url: https://data.sec.gov/submissions/CIK0002009233.json
listings:
- ticker: AGRZ
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001213900-26-104158
  filed: '2026-09-28'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/2009233/000121390026104158/0001213900-26-104158-index.html
- accession: 0001213900-26-097279
  filed: '2026-09-03'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/2009233/000121390026097279/0001213900-26-097279-index.html
research_progress:
  stage: evidence_collected
  input_sha256: 14b68c0982f4d082d934170216d3d4dc577e531f62f0edd75de93535fad635b3
  last_attempt_at: '2026-11-07T17:58:19.720602+00:00'
  last_success_at: '2026-11-07T17:58:19.720602+00:00'
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
  sector: consumer-staples
  method: project_sic_rule
  sic: '0100'
  sic_description: Agricultural Production-Crops
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0002009233.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/6e1c8271c74cf7335265700a5a223e692b47544f/brain/companies/AGRZ/README.md
full_history_commit: 6e1c8271c74cf7335265700a5a223e692b47544f
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# AGRZ — Agroz Inc.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/6e1c8271c74cf7335265700a5a223e692b47544f/brain/companies/AGRZ/README.md)

## Business overview

Reported issuer name: **Agroz Inc.**. Stable SEC CIK: **0002009233**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| AGRZ | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 20-F, filed 2026-09-28, L537:

> to evaluate our business and it will continue to be difficult to make accurate predictions and forecasts on our growth and future prospects. [S53]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 20-F, filed 2026-09-28, L2003:

> separate from the services that comprise the first and second revenue streams identified in the “Principal activities” subsection [S53]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 20-F, filed 2026-09-28, L538:

> There is no guarantee that our products or services will remain attractive to potential and current clients as our business continues [S53]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 20-F, filed 2026-09-28, L1430:

> to our customers. We go beyond organic practices by growing clean and fresh vegetables in a safe and sustainable manner. The CEA vertical [S53]

## Industry and value chain

SEC-reported SIC **0100**: Agricultural Production-Crops. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 20-F, filed 2026-09-28, L618:

> the supply chain for key inputs could materially impact our business, financial condition and operating results. If our suppliers encounter [S53]

Navigation sector: **consumer-staples**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 20-F, filed 2026-09-28, L605:

> the quality of our products from those of our competitors, and the effectiveness of marketing and advertising campaigns for our products. [S53]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 20-F, filed 2026-09-28, L723:

> part on our rights to copyright, service marks, trademarks, trade names and other intellectual property rights we own or license. If we [S53]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 20-F, filed 2026-09-28, L569:

> a growth strategy for the expansion of our operations by further developing and improving our products and services. Our ability to rapidly [S53]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 20-F, filed 2026-09-28, L1044:

> or not we distribute dividends at all is entirely at the discretion of the Board of Directors, you must rely on price appreciation of [S53]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 20-F, filed 2026-09-28, L500:

> the Securities Exchange Act of 1934, as amended (the “Exchange Act”) that involve significant risks and uncertainties. All [S53]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 20-F, 3, 4, 424B3, 6-K, 8-A12B, CERT, CORRESP, DRS, DRS/A, DRSLTR, EFFECT, F-1, F-1/A, NT 20-F, POS AM, SCHEDULE 13D, SCHEDULE 13G, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:36:32.012326+00:00.

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
| 2026-09-28 | 20-F | 0001213900-26-104158 | — | [S03] |
| 2026-09-03 | 6-K | 0001213900-26-097279 | — | [S04] |
| 2026-06-30 | 6-K | 0001213900-26-073402 | — | [S05] |
| 2026-05-29 | 6-K | 0001213900-26-062816 | — | [S06] |
| 2026-05-19 | 6-K | 0001213900-26-058726 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-11-01T16:07:03.070084+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0002009233.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [20-F 0001213900-26-104158](https://www.sec.gov/Archives/edgar/data/2009233/000121390026104158/0001213900-26-104158-index.html) — published 2026-09-28; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [6-K 0001213900-26-097279](https://www.sec.gov/Archives/edgar/data/2009233/000121390026097279/0001213900-26-097279-index.html) — published 2026-09-03; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [6-K 0001213900-26-073402](https://www.sec.gov/Archives/edgar/data/2009233/000121390026073402/0001213900-26-073402-index.html) — published 2026-06-30; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [6-K 0001213900-26-062816](https://www.sec.gov/Archives/edgar/data/2009233/000121390026062816/0001213900-26-062816-index.html) — published 2026-05-29; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [6-K 0001213900-26-058726](https://www.sec.gov/Archives/edgar/data/2009233/000121390026058726/0001213900-26-058726-index.html) — published 2026-05-19; retrieved 2026-10-23T08:33:02.691743+00:00.

[S53] [20-F 0001213900-26-104158](https://www.sec.gov/Archives/edgar/data/2009233/000121390026104158/ea0306404-20f_agrozinc.htm) — published 2026-09-28; retrieved 2026-11-07T18:01:34.987536+00:00.

Source release: `coverage-20261101-41324509967-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/6e1c8271c74cf7335265700a5a223e692b47544f/brain/companies/AGRZ/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
