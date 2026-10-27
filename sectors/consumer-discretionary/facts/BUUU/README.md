---
schema_version: 1
document_type: company_facts
company_id: company-cik-0002047273
cik: '0002047273'
company_name: BUUU Group Ltd
tickers:
- BUUU
status: stub
canonical_reviewed: false
as_of: '2026-10-27'
updated_at: '2026-10-27T15:30:18.641431+00:00'
reviewed_at: null
coverage_release: coverage-20261027-40530587641-1
source_commit: 77264ce478c0c699392c0a049f464d4fda44c9f8
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
  - CERT
  - CORRESP
  - DRS
  - DRS/A
  - DRSLTR
  - EFFECT
  - F-1
  - F-1/A
  - FWP
  - SCHEDULE 13D
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0002047273.json
    sha256: 69ef55145c0c632237b05b36df56cf7c2d0b60f1bcfb08ca0f047de56269c1ed
    retrieved_at: '2026-10-24T13:22:51.759433+00:00'
    archive: &id001
      member: CIK0002047273.json
      sha256: 593fbbea6512ef5ec729a5e513c465fbedaac8a66602c0abe00d0ba5a4d18732
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: nasdaqlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt
  published_at: null
  retrieved_at: '2026-10-27T15:25:33.739265+00:00'
  sha256: 29c7cedde394d9fb806c731f8be32ec8c78cad2668852342db80ae28619465f0
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0002047273.json
  published_at: null
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 69ef55145c0c632237b05b36df56cf7c2d0b60f1bcfb08ca0f047de56269c1ed
- id: S03
  title: 6-K 0001213900-26-112139
  url: https://www.sec.gov/Archives/edgar/data/2047273/000121390026112139/0001213900-26-112139-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S04
  title: 6-K 0001213900-26-109233
  url: https://www.sec.gov/Archives/edgar/data/2047273/000121390026109233/0001213900-26-109233-index.html
  published_at: '2026-10-14'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S05
  title: 6-K 0001213900-26-103244
  url: https://www.sec.gov/Archives/edgar/data/2047273/000121390026103244/0001213900-26-103244-index.html
  published_at: '2026-09-25'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S06
  title: 6-K 0001213900-26-100352
  url: https://www.sec.gov/Archives/edgar/data/2047273/000121390026100352/0001213900-26-100352-index.html
  published_at: '2026-09-16'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S07
  title: 6-K 0001213900-26-096963
  url: https://www.sec.gov/Archives/edgar/data/2047273/000121390026096963/0001213900-26-096963-index.html
  published_at: '2026-09-03'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S41
  url: https://www.sec.gov/Archives/edgar/data/2047273/000121390026112139/ea0308942-6k_buuu.htm
  title: 6-K 0001213900-26-112139
  published_at: '2026-10-23'
  retrieved_at: '2026-10-25T14:01:55.556024+00:00'
  sha256: 4e1122c4b75de8355ae4fecfd4891c2418407b8cc563c1f8853066a24ed927ae
- id: S42
  url: https://www.sec.gov/Archives/edgar/data/2047273/000121390025104702/ea0262735-20f_buuugroup.htm
  title: 20-F 0001213900-25-104702
  published_at: '2025-10-31'
  retrieved_at: '2026-10-25T14:01:53.930738+00:00'
  sha256: 086b0e4820dffcac6fc32b931f778c8c93a65cbf6b176b28a3ce262a0e04325b
issuer_classification:
  cik: '0002047273'
  classification_status: reported_sic
  entity_type: other
  name: BUUU Group Ltd
  sic: '7900'
  sic_description: Services-Amusement & Recreation Services
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 69ef55145c0c632237b05b36df56cf7c2d0b60f1bcfb08ca0f047de56269c1ed
  url: https://data.sec.gov/submissions/CIK0002047273.json
listings:
- ticker: BUUU
  exchange: NASDAQ
  instrument_type: equity_candidate
research_filings:
- accession: 0001213900-25-104702
  filed: '2025-10-31'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/2047273/000121390025104702/0001213900-25-104702-index.html
- accession: 0001213900-26-112139
  filed: '2026-10-23'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/2047273/000121390026112139/0001213900-26-112139-index.html
research_progress:
  stage: evidence_collected
  input_sha256: 5cd42f519bfc22b02c49c076e2e127b14bf864b6340f07343b598c0270600421
  last_attempt_at: '2026-10-25T13:56:40.792803+00:00'
  last_success_at: '2026-10-25T13:56:40.792803+00:00'
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
  sic: '7900'
  sic_description: Services-Amusement & Recreation Services
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0002047273.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/f974cdc6ffee05a6e0489d88d3e13c8eebf0b613/brain/companies/BUUU/README.md
full_history_commit: f974cdc6ffee05a6e0489d88d3e13c8eebf0b613
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# BUUU — BUUU Group Ltd

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/f974cdc6ffee05a6e0489d88d3e13c8eebf0b613/brain/companies/BUUU/README.md)

## Business overview

Reported issuer name: **BUUU Group Ltd**. Stable SEC CIK: **0002047273**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| BUUU | NASDAQ | equity_candidate | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 20-F, filed 2025-10-31, L388:

> third parties and our own internal estimates based on our management’s knowledge and experience in the markets in which we operate. [S42]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 20-F, filed 2025-10-31, L5864:

> In accordance with ASC 280, Segment Reporting, the Company is required to report financial and descriptive information about its reportable segments. Reportable segments are operating segments or aggregations of operating segments that meet specific quantitative thresholds. The identification of operating segments is based on the internal reporting used by the Chief Operating Decision Maker (“CODM”) to assess performance and allocate resources. [S42]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 20-F, filed 2025-10-31, L527:

> could require us to change certain aspects of our business to ensure compliance, which could decrease demand for our services, reduce [S42]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 20-F, filed 2025-10-31, L827:

> our strategic business plan. There is no guarantee that our customers will continue to utilize our services to fulfil their ongoing needs, [S42]

## Industry and value chain

SEC-reported SIC **7900**: Services-Amusement & Recreation Services. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 20-F, filed 2025-10-31, L867:

> obliged to pay our suppliers in a timely manner. As a result, if any of our major customers experience any financial difficulty and fail [S42]

Navigation sector: **consumer-discretionary**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 20-F, filed 2025-10-31, L824:

> for our offerings, and industry competition, many of which are beyond our control. Consequently, we might face challenges in maintaining [S42]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 20-F, filed 2025-10-31, L1088:

> and personal information, interruptions in communication, loss of our intellectual property or theft of our sensitive or proprietary technology, [S42]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 20-F, filed 2025-10-31, L1159:

> competitors, as well as new and emerging entrants. Additionally, as we expand our service offerings, we may face competition from new [S42]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 6-K, filed 2026-10-23, L28:

> Split”). The Forward Split was approved by the Company’s board of directors on September 28, 2026. [S41]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 20-F, filed 2025-10-31, L438:

> from current expectations include, among other things, those listed under the heading “Risk Factors” and elsewhere in this [S42]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 20-F, 3, 424B4, 6-K, 8-A12B, CERT, CORRESP, DRS, DRS/A, DRSLTR, EFFECT, F-1, F-1/A, FWP, SCHEDULE 13D, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:36:36.676143+00:00.

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
| 2026-10-23 | 6-K | 0001213900-26-112139 | — | [S03] |
| 2026-10-14 | 6-K | 0001213900-26-109233 | — | [S04] |
| 2026-09-25 | 6-K | 0001213900-26-103244 | — | [S05] |
| 2026-09-16 | 6-K | 0001213900-26-100352 | — | [S06] |
| 2026-09-03 | 6-K | 0001213900-26-096963 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-27T15:25:33.739265+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0002047273.json) — published not supplied; retrieved 2026-10-24T13:22:51.759433+00:00.

[S03] [6-K 0001213900-26-112139](https://www.sec.gov/Archives/edgar/data/2047273/000121390026112139/0001213900-26-112139-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S04] [6-K 0001213900-26-109233](https://www.sec.gov/Archives/edgar/data/2047273/000121390026109233/0001213900-26-109233-index.html) — published 2026-10-14; retrieved 2026-10-24T13:22:51.759433+00:00.

[S05] [6-K 0001213900-26-103244](https://www.sec.gov/Archives/edgar/data/2047273/000121390026103244/0001213900-26-103244-index.html) — published 2026-09-25; retrieved 2026-10-24T13:22:51.759433+00:00.

[S06] [6-K 0001213900-26-100352](https://www.sec.gov/Archives/edgar/data/2047273/000121390026100352/0001213900-26-100352-index.html) — published 2026-09-16; retrieved 2026-10-24T13:22:51.759433+00:00.

[S07] [6-K 0001213900-26-096963](https://www.sec.gov/Archives/edgar/data/2047273/000121390026096963/0001213900-26-096963-index.html) — published 2026-09-03; retrieved 2026-10-24T13:22:51.759433+00:00.

[S41] [6-K 0001213900-26-112139](https://www.sec.gov/Archives/edgar/data/2047273/000121390026112139/ea0308942-6k_buuu.htm) — published 2026-10-23; retrieved 2026-10-25T14:01:55.556024+00:00.

[S42] [20-F 0001213900-25-104702](https://www.sec.gov/Archives/edgar/data/2047273/000121390025104702/ea0262735-20f_buuugroup.htm) — published 2025-10-31; retrieved 2026-10-25T14:01:53.930738+00:00.

Source release: `coverage-20261027-40530587641-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/f974cdc6ffee05a6e0489d88d3e13c8eebf0b613/brain/companies/BUUU/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
