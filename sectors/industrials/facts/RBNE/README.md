---
schema_version: 1
document_type: company_facts
company_id: company-cik-0002039060
cik: 0002039060
company_name: Robin Energy Ltd.
tickers:
- RBNE
status: stub
canonical_reviewed: false
as_of: '2026-11-01'
updated_at: '2026-11-01T16:11:48.803754+00:00'
reviewed_at: null
coverage_release: coverage-20261101-41324509967-1
source_commit: 68485afc2c279cc446102d99a1310528fc8bf3ae
financial_history_available: false
curated_research: null
financial_gap:
  reason: foreign_reporting_adapter
  next_action: Add support for the observed 20-F, 40-F or 6-K reporting forms and
    verify the actual accounting taxonomy before normalization.
  observed_forms:
  - 20-F
  - 20FR12B
  - 20FR12B/A
  - '3'
  - 424B5
  - 6-K
  - CERT
  - CORRESP
  - DRS
  - DRS/A
  - DRSLTR
  - EFFECT
  - F-1
  - F-3
  - RW
  - SC TO-I
  - SC TO-I/A
  - SCHEDULE 13D
  - SCHEDULE 13D/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - SEC STAFF ACTION
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0002039060.json
    sha256: 62c2bb0b0649cf03e96a48f55aeec101f02e17dd85a5d383a7d17016d02b9400
    retrieved_at: '2026-10-24T13:22:51.759433+00:00'
    archive: &id001
      member: CIK0002039060.json
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
  url: https://data.sec.gov/submissions/CIK0002039060.json
  published_at: null
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 62c2bb0b0649cf03e96a48f55aeec101f02e17dd85a5d383a7d17016d02b9400
- id: S03
  title: 6-K 0001140361-26-040600
  url: https://www.sec.gov/Archives/edgar/data/2039060/000114036126040600/0001140361-26-040600-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S04
  title: RW 0001140361-26-040382
  url: https://www.sec.gov/Archives/edgar/data/2039060/000114036126040382/0001140361-26-040382-index.html
  published_at: '2026-10-21'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S05
  title: F-1 0001140361-26-039848
  url: https://www.sec.gov/Archives/edgar/data/2039060/000114036126039848/0001140361-26-039848-index.html
  published_at: '2026-10-16'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S06
  title: 6-K 0001140361-26-039199
  url: https://www.sec.gov/Archives/edgar/data/2039060/000114036126039199/0001140361-26-039199-index.html
  published_at: '2026-10-09'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S07
  title: DRS 0001140361-26-038123
  url: https://www.sec.gov/Archives/edgar/data/2039060/000114036126038123/0001140361-26-038123-index.html
  published_at: '2026-10-01'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S54
  url: https://www.sec.gov/Archives/edgar/data/2039060/000114036126014136/ef20060626_20f.htm
  title: 20-F 0001140361-26-014136
  published_at: '2026-04-10'
  retrieved_at: '2026-10-31T15:36:30.502180+00:00'
  sha256: 51164cb58745fa156136ba74229bd265bc9b258dd8a84e5050bc4dc426458806
issuer_classification:
  cik: 0002039060
  classification_status: reported_sic
  entity_type: other
  name: Robin Energy Ltd.
  sic: '4412'
  sic_description: Deep Sea Foreign Transportation of  Freight
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 62c2bb0b0649cf03e96a48f55aeec101f02e17dd85a5d383a7d17016d02b9400
  url: https://data.sec.gov/submissions/CIK0002039060.json
listings:
- ticker: RBNE
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001140361-26-014136
  filed: '2026-04-10'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/2039060/000114036126014136/0001140361-26-014136-index.html
- accession: 0001140361-26-040600
  filed: '2026-10-23'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/2039060/000114036126040600/0001140361-26-040600-index.html
research_progress:
  stage: evidence_collected
  input_sha256: ca9935e38c9f0df31b7c543b675ecffc1becb79ee05afc900d1ca855100948d4
  last_attempt_at: '2026-10-31T15:34:51.132722+00:00'
  last_success_at: '2026-10-31T15:34:51.132722+00:00'
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
  sic: '4412'
  sic_description: Deep Sea Foreign Transportation of  Freight
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0002039060.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/9a2d93421bf50e1b28d316e7c6a7d3bd950c2718/brain/companies/RBNE/README.md
full_history_commit: 9a2d93421bf50e1b28d316e7c6a7d3bd950c2718
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# RBNE — Robin Energy Ltd.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/9a2d93421bf50e1b28d316e7c6a7d3bd950c2718/brain/companies/RBNE/README.md)

## Business overview

Reported issuer name: **Robin Energy Ltd.**. Stable SEC CIK: **0002039060**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| RBNE | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 20-F, filed 2026-04-10, L418:

> our business strategy, expected capital spending and other plans and objectives for future operations, including our ability to expand our business as a new [S54]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 20-F, filed 2026-04-10, L2404:

> the tanker segment, we determined that, with effect from the third quarter of 2025, we operated in two reportable segments: (i) tanker segment and (ii) LPG carrier segment. The reportable segments reflect our internal organization and the way [S54]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 20-F, filed 2026-04-10, L630:

> Future growth in the demand for our services will depend among others on changes in supply and demand, economic growth in the world economy and demand for [S54]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 20-F, filed 2026-04-10, L853:

> incurred to the extent we employ onboard security guards, could also increase due to acts of piracy or other maritime incidents, including attacks on vessels. Our customers could also suffer significant losses, impairing their ability to make [S54]

## Industry and value chain

SEC-reported SIC **4412**: Deep Sea Foreign Transportation of  Freight. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 20-F, filed 2026-04-10, L869:

> trade protectionism and has created supply chain disruptions. The United States has similarly seen a rise in protectionist policies. For example, in 2018, China and the United States each began implementing increasingly protective trade measures, [S54]

Navigation sector: **industrials**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 20-F, filed 2026-04-10, L759:

> our business.” Periods of low demand can cause excess vessel supply and intensify the competition in the industry, which often results in vessels being idle for long periods of time, which could reduce our revenues and materially harm [S54]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 20-F, filed 2026-04-10, L1010:

> the inherent complexity and pace of change may result in unforeseen challenges. Key areas of concern include data privacy, data protection, ethical AI use, and intellectual property. Additionally, failure to adapt to technological advancements [S54]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 20-F, filed 2026-04-10, L418:

> our business strategy, expected capital spending and other plans and objectives for future operations, including our ability to expand our business as a new [S54]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 20-F, filed 2026-04-10, L130:

> received by any of the registrant’s executive officers during the relevant recovery period pursuant to §240.10D-1(b).  ☐ [S54]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 20-F, filed 2026-04-10, L552:

> from those contained in any forward-looking statement. See “Item 3. Key Information—D. Risk Factors” for a more detailed discussion of these risks and uncertainties and for other risks and uncertainties. [S54]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 20-F, 20FR12B, 20FR12B/A, 3, 424B5, 6-K, CERT, CORRESP, DRS, DRS/A, DRSLTR, EFFECT, F-1, F-3, RW, SC TO-I, SC TO-I/A, SCHEDULE 13D, SCHEDULE 13D/A, SCHEDULE 13G, SCHEDULE 13G/A, SEC STAFF ACTION, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:36:35.825651+00:00.

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
| 2026-10-23 | 6-K | 0001140361-26-040600 | — | [S03] |
| 2026-10-21 | RW | 0001140361-26-040382 | — | [S04] |
| 2026-10-16 | F-1 | 0001140361-26-039848 | — | [S05] |
| 2026-10-09 | 6-K | 0001140361-26-039199 | — | [S06] |
| 2026-10-01 | DRS | 0001140361-26-038123 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-11-01T16:07:03.070084+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0002039060.json) — published not supplied; retrieved 2026-10-24T13:22:51.759433+00:00.

[S03] [6-K 0001140361-26-040600](https://www.sec.gov/Archives/edgar/data/2039060/000114036126040600/0001140361-26-040600-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S04] [RW 0001140361-26-040382](https://www.sec.gov/Archives/edgar/data/2039060/000114036126040382/0001140361-26-040382-index.html) — published 2026-10-21; retrieved 2026-10-24T13:22:51.759433+00:00.

[S05] [F-1 0001140361-26-039848](https://www.sec.gov/Archives/edgar/data/2039060/000114036126039848/0001140361-26-039848-index.html) — published 2026-10-16; retrieved 2026-10-24T13:22:51.759433+00:00.

[S06] [6-K 0001140361-26-039199](https://www.sec.gov/Archives/edgar/data/2039060/000114036126039199/0001140361-26-039199-index.html) — published 2026-10-09; retrieved 2026-10-24T13:22:51.759433+00:00.

[S07] [DRS 0001140361-26-038123](https://www.sec.gov/Archives/edgar/data/2039060/000114036126038123/0001140361-26-038123-index.html) — published 2026-10-01; retrieved 2026-10-24T13:22:51.759433+00:00.

[S54] [20-F 0001140361-26-014136](https://www.sec.gov/Archives/edgar/data/2039060/000114036126014136/ef20060626_20f.htm) — published 2026-04-10; retrieved 2026-10-31T15:36:30.502180+00:00.

Source release: `coverage-20261101-41324509967-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/9a2d93421bf50e1b28d316e7c6a7d3bd950c2718/brain/companies/RBNE/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
