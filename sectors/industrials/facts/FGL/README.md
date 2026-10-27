---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001989930
cik: 0001989930
company_name: Founder Group Ltd
tickers:
- FGL
status: stub
canonical_reviewed: false
as_of: '2026-10-27'
updated_at: '2026-10-27T15:30:18.641431+00:00'
reviewed_at: null
coverage_release: coverage-20261027-40530587641-1
source_commit: 79ea404d09f86d838fefd71cf88a566d57bc57a2
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
  - '4'
  - 424B1
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
  - POS AM
  - SCHEDULE 13D
  - SCHEDULE 13D/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001989930.json
    sha256: b9fb1eb7e19955b93c42ae2672a289490a3dc392acce7be2988da49c29555665
    retrieved_at: '2026-10-24T13:22:51.759433+00:00'
    archive: &id001
      member: CIK0001989930.json
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
  url: https://data.sec.gov/submissions/CIK0001989930.json
  published_at: null
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: b9fb1eb7e19955b93c42ae2672a289490a3dc392acce7be2988da49c29555665
- id: S03
  title: 6-K 0001213900-26-111870
  url: https://www.sec.gov/Archives/edgar/data/1989930/000121390026111870/0001213900-26-111870-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S04
  title: 6-K 0001213900-26-101797
  url: https://www.sec.gov/Archives/edgar/data/1989930/000121390026101797/0001213900-26-101797-index.html
  published_at: '2026-09-21'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S05
  title: 6-K 0001213900-26-097414
  url: https://www.sec.gov/Archives/edgar/data/1989930/000121390026097414/0001213900-26-097414-index.html
  published_at: '2026-09-04'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S06
  title: 4 0001475597-26-000225
  url: https://www.sec.gov/Archives/edgar/data/1989930/000147559726000225/0001475597-26-000225-index.html
  published_at: '2026-09-01'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S07
  title: 4 0001475597-26-000219
  url: https://www.sec.gov/Archives/edgar/data/1989930/000147559726000219/0001475597-26-000219-index.html
  published_at: '2026-08-28'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S54
  url: https://www.sec.gov/Archives/edgar/data/1989930/000121390026048554/ea0287754-20f_founder.htm
  title: 20-F 0001213900-26-048554
  published_at: '2026-04-28'
  retrieved_at: '2026-10-26T16:27:58.752953+00:00'
  sha256: 78f5e098d9bd68bae4caec70825d2b9b5406eb3607817cd5d77d9b9e88252d37
issuer_classification:
  cik: 0001989930
  classification_status: reported_sic
  entity_type: other
  name: Founder Group Ltd
  sic: '1700'
  sic_description: Construction - Special Trade Contractors
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: b9fb1eb7e19955b93c42ae2672a289490a3dc392acce7be2988da49c29555665
  url: https://data.sec.gov/submissions/CIK0001989930.json
listings:
- ticker: FGL
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001213900-26-048554
  filed: '2026-04-28'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1989930/000121390026048554/0001213900-26-048554-index.html
- accession: 0001213900-26-111870
  filed: '2026-10-23'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1989930/000121390026111870/0001213900-26-111870-index.html
research_progress:
  stage: evidence_collected
  input_sha256: 6e8cefff290f8121130058133f6b17237179af32a1f64b50cdcd5877f35ba734
  last_attempt_at: '2026-10-26T16:22:31.694168+00:00'
  last_success_at: '2026-10-26T16:22:31.694168+00:00'
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
  sector: industrials
  method: project_sic_rule
  sic: '1700'
  sic_description: Construction - Special Trade Contractors
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001989930.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/ea9dd09e5d047ff0620d4500849876915bb10e87/brain/companies/FGL/README.md
full_history_commit: ea9dd09e5d047ff0620d4500849876915bb10e87
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# FGL — Founder Group Ltd

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/ea9dd09e5d047ff0620d4500849876915bb10e87/brain/companies/FGL/README.md)

## Business overview

Reported issuer name: **Founder Group Ltd**. Stable SEC CIK: **0001989930**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| FGL | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 20-F, filed 2026-04-28, L394:

> evolving industry makes it difficult to accurately forecast our future operating results and evaluate our business prospects. [S54]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 20-F, filed 2026-04-28, L489:

> requirements and timelines. If there are delays, cancellations, or reduced project activity from these customers, our revenue stream could [S54]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 20-F, filed 2026-04-28, L617:

> customers to delay, reduce, or abandon their plans to engage our services. As such, there can be no assurance that political, social and [S54]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 20-F, filed 2026-04-28, L629:

> our strategies and future plans effectively, we may not be able to take advantage of market opportunities or meet the demand of our customers. [S54]

## Industry and value chain

SEC-reported SIC **1700**: Construction - Special Trade Contractors. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 20-F, filed 2026-04-28, L505:

> few suppliers, any interruption of the operations of our suppliers, any failure of our suppliers to accommodate our growing business scale, [S54]

Navigation sector: **industrials**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 20-F, filed 2026-04-28, L590:

> and rapidly evolving, with many new companies joining the competition in recent years and a few leading companies. Competition is expected [S54]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 20-F, filed 2026-04-28, L714:

> their proprietary intellectual property rights, which could cause us to incur significant legal expenses and prevent us from promoting [S54]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 20-F, filed 2026-04-28, L465:

> Growth Strategies-Expand Our Investment in Renewable Energy Assets, Such as Solar PV Systems.” To carry out this project, Founder [S54]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 20-F, filed 2026-04-28, L735:

> our key personnel, including our executive officers, senior management, and key employees, our ongoing operations and growth could be [S54]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 20-F, filed 2026-04-28, L454:

> in a material adverse impact on our operations. Although Founder Energy (Malaysia) has rectified this non-compliance by promptly declaring [S54]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 144, 20-F, 3, 4, 424B1, 424B3, 424B4, 6-K, 8-A12B, CERT, CORRESP, DRS, DRS/A, DRSLTR, EFFECT, F-1, F-1/A, POS AM, SCHEDULE 13D, SCHEDULE 13D/A, SCHEDULE 13G, SCHEDULE 13G/A, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:36:30.133535+00:00.

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
| 2026-10-23 | 6-K | 0001213900-26-111870 | — | [S03] |
| 2026-09-21 | 6-K | 0001213900-26-101797 | — | [S04] |
| 2026-09-04 | 6-K | 0001213900-26-097414 | — | [S05] |
| 2026-09-01 | 4 | 0001475597-26-000225 | — | [S06] |
| 2026-08-28 | 4 | 0001475597-26-000219 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-27T15:25:33.739265+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001989930.json) — published not supplied; retrieved 2026-10-24T13:22:51.759433+00:00.

[S03] [6-K 0001213900-26-111870](https://www.sec.gov/Archives/edgar/data/1989930/000121390026111870/0001213900-26-111870-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S04] [6-K 0001213900-26-101797](https://www.sec.gov/Archives/edgar/data/1989930/000121390026101797/0001213900-26-101797-index.html) — published 2026-09-21; retrieved 2026-10-24T13:22:51.759433+00:00.

[S05] [6-K 0001213900-26-097414](https://www.sec.gov/Archives/edgar/data/1989930/000121390026097414/0001213900-26-097414-index.html) — published 2026-09-04; retrieved 2026-10-24T13:22:51.759433+00:00.

[S06] [4 0001475597-26-000225](https://www.sec.gov/Archives/edgar/data/1989930/000147559726000225/0001475597-26-000225-index.html) — published 2026-09-01; retrieved 2026-10-24T13:22:51.759433+00:00.

[S07] [4 0001475597-26-000219](https://www.sec.gov/Archives/edgar/data/1989930/000147559726000219/0001475597-26-000219-index.html) — published 2026-08-28; retrieved 2026-10-24T13:22:51.759433+00:00.

[S54] [20-F 0001213900-26-048554](https://www.sec.gov/Archives/edgar/data/1989930/000121390026048554/ea0287754-20f_founder.htm) — published 2026-04-28; retrieved 2026-10-26T16:27:58.752953+00:00.

Source release: `coverage-20261027-40530587641-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/ea9dd09e5d047ff0620d4500849876915bb10e87/brain/companies/FGL/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
