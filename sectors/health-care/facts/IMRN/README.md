---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001660046
cik: '0001660046'
company_name: Immuron Ltd
tickers:
- IMRN
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
  - 25-NSE
  - '3'
  - 424B3
  - 424B4
  - 424B5
  - 6-K
  - 6-K/A
  - 8-A12B
  - CERTNAS
  - CORRESP
  - CT ORDER
  - EFFECT
  - F-1
  - F-1/A
  - F-1MEF
  - F-3
  - FWP
  - NT 20-F
  - POS AM
  - RW
  - SC 13D
  - SC 13G
  - SC 13G/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001660046.json
    sha256: 9d2b3826bb1e51a1a31a92c2f9f4589c1406581e8cde3da546a87958433ae95f
    retrieved_at: '2026-10-24T13:22:51.759433+00:00'
    archive: &id001
      member: CIK0001660046.json
      sha256: 593fbbea6512ef5ec729a5e513c465fbedaac8a66602c0abe00d0ba5a4d18732
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
  url: https://data.sec.gov/submissions/CIK0001660046.json
  published_at: null
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 9d2b3826bb1e51a1a31a92c2f9f4589c1406581e8cde3da546a87958433ae95f
- id: S03
  title: 6-K 0001213900-26-112204
  url: https://www.sec.gov/Archives/edgar/data/1660046/000121390026112204/0001213900-26-112204-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S04
  title: 424B5 0001213900-26-112198
  url: https://www.sec.gov/Archives/edgar/data/1660046/000121390026112198/0001213900-26-112198-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S05
  title: 6-K 0001213900-26-111439
  url: https://www.sec.gov/Archives/edgar/data/1660046/000121390026111439/0001213900-26-111439-index.html
  published_at: '2026-10-22'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S06
  title: 6-K 0001213900-26-110026
  url: https://www.sec.gov/Archives/edgar/data/1660046/000121390026110026/0001213900-26-110026-index.html
  published_at: '2026-10-16'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S07
  title: 6-K 0001213900-26-108742
  url: https://www.sec.gov/Archives/edgar/data/1660046/000121390026108742/0001213900-26-108742-index.html
  published_at: '2026-10-13'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S54
  url: https://www.sec.gov/Archives/edgar/data/1660046/000121390026102838/ea0305398-20f_immuron.htm
  title: 20-F 0001213900-26-102838
  published_at: '2026-09-24'
  retrieved_at: '2026-10-28T16:22:37.577356+00:00'
  sha256: 9b9df602c1d9611a1dc7c34fb985fdf4042e9ea07a894749442efb36c85f2d58
issuer_classification:
  cik: '0001660046'
  classification_status: reported_sic
  entity_type: other
  name: Immuron Ltd
  sic: '2834'
  sic_description: Pharmaceutical Preparations
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 9d2b3826bb1e51a1a31a92c2f9f4589c1406581e8cde3da546a87958433ae95f
  url: https://data.sec.gov/submissions/CIK0001660046.json
listings:
- ticker: IMRN
  exchange: NASDAQ
  instrument_type: depositary_receipt
research_filings:
- accession: 0001213900-26-102838
  filed: '2026-09-24'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1660046/000121390026102838/0001213900-26-102838-index.html
- accession: 0001213900-26-112204
  filed: '2026-10-23'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1660046/000121390026112204/0001213900-26-112204-index.html
- accession: 0001213900-24-046748
  filed: '2024-05-28'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1660046/000121390024046748/0001213900-24-046748-index.html
- accession: 0001213900-20-015368
  filed: '2020-06-19'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1660046/000121390020015368/0001213900-20-015368-index.html
- accession: 0001615774-19-005432
  filed: '2019-04-08'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1660046/000161577419005432/0001615774-19-005432-index.html
research_progress:
  stage: evidence_collected
  input_sha256: 889bb43084300f5943f67ba4b9177456f06a9385094ada42413a3fd0e734e061
  last_attempt_at: '2026-10-28T16:19:58.196907+00:00'
  last_success_at: '2026-10-28T16:19:58.196907+00:00'
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
  sector: health-care
  method: project_sic_rule
  sic: '2834'
  sic_description: Pharmaceutical Preparations
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001660046.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/c26f59bc72c00102d2490e95b07449f8cd848491/brain/companies/IMRN/README.md
full_history_commit: c26f59bc72c00102d2490e95b07449f8cd848491
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# IMRN — Immuron Ltd

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/c26f59bc72c00102d2490e95b07449f8cd848491/brain/companies/IMRN/README.md)

## Business overview

Reported issuer name: **Immuron Ltd**. Stable SEC CIK: **0001660046**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| IMRN | NASDAQ | depositary_receipt | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 20-F, filed 2026-09-24, L134:

> amended, or the Exchange Act, and the Private Securities Litigation Reform Act of 1995, as amended, with respect to our business, financial [S54]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 20-F, filed 2026-09-24, L6495:

> Management considers the business from both a product and a geographic perspective and has identified two reportable segments: Research and development (R&D) and Hyper-immune products. See Note 15 for more details. [S54]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 20-F, filed 2026-09-24, L90:

> which continues to grow as we seek to increase sales of our existing commercial products and to expand our product portfolio and distribution [S54]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 20-F, filed 2026-09-24, L1331:

> through our customers, subject to various federal and state fraud and abuse laws, including, without limitation, the federal Anti- Kickback [S54]

## Industry and value chain

SEC-reported SIC **2834**: Pharmaceutical Preparations. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 20-F, filed 2026-09-24, L4645:

> seven full-time employees and one part time employee. Of the full-time employees, two are our Supply Chain Senior Associate and Quality [S54]

Navigation sector: **health-care**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 20-F, filed 2026-09-24, L816:

> regulatory hurdles, competition, as well as other factors, may make our targets, lead therapies or product candidates unattractive for [S54]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 20-F, filed 2026-09-24, L594:

> our ability to protect our intellectual property and our proprietary technology, to operate without infringing the proprietary rights [S54]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 20-F, filed 2026-09-24, L90:

> which continues to grow as we seek to increase sales of our existing commercial products and to expand our product portfolio and distribution [S54]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 20-F, filed 2026-09-24, L1515:

> \| (1) a majority of our executive officers or directors must not be U.S. citizens or residents; (2) more than 50% of our assets cannot be located in the United States; and (3) our business must be administered principally outside the United States. [S54]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 20-F, filed 2026-09-24, L145:

> and other factors affecting forward-looking statements in the Risk Factors section that appears in Item 3.D. “Key Information-Risk [S54]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 20-F, 25-NSE, 3, 424B3, 424B4, 424B5, 6-K, 6-K/A, 8-A12B, CERTNAS, CORRESP, CT ORDER, EFFECT, F-1, F-1/A, F-1MEF, F-3, FWP, NT 20-F, POS AM, RW, SC 13D, SC 13G, SC 13G/A, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:34:52.407016+00:00.

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
| 2026-10-23 | 6-K | 0001213900-26-112204 | — | [S03] |
| 2026-10-23 | 424B5 | 0001213900-26-112198 | — | [S04] |
| 2026-10-22 | 6-K | 0001213900-26-111439 | — | [S05] |
| 2026-10-16 | 6-K | 0001213900-26-110026 | — | [S06] |
| 2026-10-13 | 6-K | 0001213900-26-108742 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-29T16:14:13.115716+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001660046.json) — published not supplied; retrieved 2026-10-24T13:22:51.759433+00:00.

[S03] [6-K 0001213900-26-112204](https://www.sec.gov/Archives/edgar/data/1660046/000121390026112204/0001213900-26-112204-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S04] [424B5 0001213900-26-112198](https://www.sec.gov/Archives/edgar/data/1660046/000121390026112198/0001213900-26-112198-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S05] [6-K 0001213900-26-111439](https://www.sec.gov/Archives/edgar/data/1660046/000121390026111439/0001213900-26-111439-index.html) — published 2026-10-22; retrieved 2026-10-24T13:22:51.759433+00:00.

[S06] [6-K 0001213900-26-110026](https://www.sec.gov/Archives/edgar/data/1660046/000121390026110026/0001213900-26-110026-index.html) — published 2026-10-16; retrieved 2026-10-24T13:22:51.759433+00:00.

[S07] [6-K 0001213900-26-108742](https://www.sec.gov/Archives/edgar/data/1660046/000121390026108742/0001213900-26-108742-index.html) — published 2026-10-13; retrieved 2026-10-24T13:22:51.759433+00:00.

[S54] [20-F 0001213900-26-102838](https://www.sec.gov/Archives/edgar/data/1660046/000121390026102838/ea0305398-20f_immuron.htm) — published 2026-09-24; retrieved 2026-10-28T16:22:37.577356+00:00.

Source release: `coverage-20261029-40909364006-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/c26f59bc72c00102d2490e95b07449f8cd848491/brain/companies/IMRN/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
