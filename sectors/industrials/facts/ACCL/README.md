---
schema_version: 1
document_type: company_facts
company_id: company-cik-0002038378
cik: 0002038378
company_name: Acco Group Holdings Ltd
tickers:
- ACCL
status: stub
canonical_reviewed: false
as_of: '2026-11-01'
updated_at: '2026-11-01T16:11:48.803754+00:00'
reviewed_at: null
coverage_release: coverage-20261101-41324509967-1
source_commit: b7d564f6a774e716acb58b68cc3c1e8b1400a1e5
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
  - NT 20-F
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0002038378.json
    sha256: 6d4a0cea5a9607469ee66cf4102e035598d449ea27fd4dfaa2e5e611d8499df2
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0002038378.json
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
  url: https://data.sec.gov/submissions/CIK0002038378.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 6d4a0cea5a9607469ee66cf4102e035598d449ea27fd4dfaa2e5e611d8499df2
- id: S03
  title: 20-F 0001213900-26-111364
  url: https://www.sec.gov/Archives/edgar/data/2038378/000121390026111364/0001213900-26-111364-index.html
  published_at: '2026-10-21'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 6-K 0001213900-26-098109
  url: https://www.sec.gov/Archives/edgar/data/2038378/000121390026098109/0001213900-26-098109-index.html
  published_at: '2026-09-08'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 6-K 0001213900-26-073728
  url: https://www.sec.gov/Archives/edgar/data/2038378/000121390026073728/0001213900-26-073728-index.html
  published_at: '2026-06-30'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 3 0001213900-26-041249
  url: https://www.sec.gov/Archives/edgar/data/2038378/000121390026041249/0001213900-26-041249-index.html
  published_at: '2026-04-08'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 3 0001213900-26-041248
  url: https://www.sec.gov/Archives/edgar/data/2038378/000121390026041248/0001213900-26-041248-index.html
  published_at: '2026-04-08'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S46
  url: https://www.sec.gov/Archives/edgar/data/2038378/000121390026111364/ea0308052-20f_acco.htm
  title: 20-F 0001213900-26-111364
  published_at: '2026-10-21'
  retrieved_at: '2026-11-02T22:10:49.507465+00:00'
  sha256: fd67a425fd805f23c6f7fb66727ebed12763607f4d0c61f3a55c8e5204e1c424
issuer_classification:
  cik: 0002038378
  classification_status: reported_sic
  entity_type: other
  name: Acco Group Holdings Ltd
  sic: '8742'
  sic_description: Services-Management Consulting Services
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 6d4a0cea5a9607469ee66cf4102e035598d449ea27fd4dfaa2e5e611d8499df2
  url: https://data.sec.gov/submissions/CIK0002038378.json
listings:
- ticker: ACCL
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001213900-26-111364
  filed: '2026-10-21'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/2038378/000121390026111364/0001213900-26-111364-index.html
- accession: 0001213900-26-098109
  filed: '2026-09-08'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/2038378/000121390026098109/0001213900-26-098109-index.html
research_progress:
  stage: evidence_collected
  input_sha256: d59010bdf9960acf854e200b8195f078e75aa9122367372c795738df4c2ad7ac
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
  sector: industrials
  method: project_sic_rule
  sic: '8742'
  sic_description: Services-Management Consulting Services
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0002038378.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/ef36a46d682e789d5949ebe61d4ec5a6bea5f3de/brain/companies/ACCL/README.md
full_history_commit: ef36a46d682e789d5949ebe61d4ec5a6bea5f3de
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# ACCL — Acco Group Holdings Ltd

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/ef36a46d682e789d5949ebe61d4ec5a6bea5f3de/brain/companies/ACCL/README.md)

## Business overview

Reported issuer name: **Acco Group Holdings Ltd**. Stable SEC CIK: **0002038378**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| ACCL | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 20-F, filed 2026-10-21, L147:

> We obtained the industry and market data used in this annual report or any document incorporated by reference from industry publications, research, surveys and studies conducted by third parties and our own internal estimates based on our management’s knowledge and experience in the markets in which we operate. We did not, directly or indirectly, sponsor or participate in the publication of such materials, and these materials are not incorporated in this annual report other than to the extent specifically cited in this annual report. We have sought to provide current information in this annual report and believe that the statistics provided in this annual report remain up-to-date and reliable, and these materials are not incorporated in this annual report other than to the extent specifically cited in this annual report. [S46]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 20-F, filed 2026-10-21, L2343:

> The Group follows FASB ASC Topic 280, Segment Reporting, segments are defined as components of a company that engage in business activities from which they may earn revenues and incur expenses, and for which separate financial information is available and is evaluated regularly by the chief operating decision maker (“CODM”), or decision-making group, in deciding how to allocate resources and in assessing performance. Our chief operating decision maker, who is our chief executive officer, manages the business under three operating segments, which are our reportable segments: (1) Corporate Secretarial Services, (2) Accounting Services; (3) IP Registration Services. [S46]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 20-F, filed 2026-10-21, L167:

> \| \| ● \| any recurrence of the COVID-19 pandemic and scope of related government orders and restrictions and the extent of the impact of the COVID-19 pandemic on the global economy, impact it may have on our operations, the demand for our products and services, and economic activity in general; [S46]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 20-F, filed 2026-10-21, L187:

> Our revenue is primarily derived from corporate secretarial, accounting, and IP registration services, which are not always recurring in nature, and there is no assurance that our customers will provide us with new business. [S46]

## Industry and value chain

SEC-reported SIC **8742**: Services-Management Consulting Services. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 20-F, filed 2026-10-21, L616:

> Driven by (i) the expected policy easing of the Federal Reserve System of the United States in the upcoming years; (ii) continuous consumer spending resilience in early-2024; and (iii) normalization of the global supply chain resulting in rising business investments, it is expected that the economic momentum of the U.S. will improve. In light of this trend, we expect that the demand for corporate services will be soaring in the U.S. We plan to capitalize on the growth of the U.S. corporate service markets by expanding our business into the U.S., such as providing services to U.S.-based clients to set up businesses and register IPs in the U.S. We will tailor our products and services to fit into the U.S. corporate service markets and to conform to its regulatory requirements. Given our established operation history, in-depth industry knowledge and strong client base, we have developed robust expertise in navigating the regulatory frameworks governing formation of corporate entities and IP registrations. We believe we are well-positioned to undertake this expansion and to meet industry and client demands. Currently, we do not have any business presence in the U.S. on our own. To this end, we plan to set up new branches and offices in the U.S. and to recruit suitable and appropriate staffs to support our expansion. We will also continue to explore potential opportunities to … [S46]

Navigation sector: **industrials**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 20-F, filed 2026-10-21, L196:

> The failure to manage the utilization of our professionals, or maintain or increase the rates our Operating Subsidiaries charge our clients for their services, could result in adverse consequences, such as non- or lower-revenue-generating professionals, increased employee turnover, fixed compensation expenses in periods of declining revenues, the inability to appropriately staff engagements (including adding or reducing staff during periods of increased or decreased demand for our services), or special charges associated with reductions in staff or operations. Reductions in workforce or increases of billable rates will not necessarily lead to savings. In such events, our financial results may decline or be adversely impacted. A number of factors affect the utilization of the professionals of our Operating Subsidiaries. Some of these factors we cannot predict with certainty, including general economic and financial market conditions; the complexity, number, type, size and timing of client engagements; the level of demand for our services; appropriate professional staffing levels, in light of changing client demands and market conditions; utilization of professionals across segments and geographic regions; and competition. In addition, our global expansion into or within locations where we are not well-known or where demand for our services is not well-developed could also … [S46]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 20-F, filed 2026-10-21, L163:

> \| \| ● \| our subsidiaries’ ability to protect their intellectual property rights and secure the right to use other intellectual property that they deem to be essential or desirable to the conduct of their business; [S46]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 20-F, filed 2026-10-21, L189:

> In the event that we are unable to maintain our business with our recurring customers or to expand and diversify our customer base by sourcing new customers at desired levels or at all, or to develop and expand our service offerings, or to meet the requirements of our customers regarding service quality and delivery or any other requirements at reasonable or affordable costs, our relationship with our customers, our business, financial condition and results of operations could be materially and adversely affected. [S46]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 20-F, filed 2026-10-21, L68:

> Indicate by check mark whether any of those error corrections are restatements that required a recovery analysis of incentive-based compensation received by any of the registrant’s executive officers during the relevant recovery period pursuant to §240.10D-1(b). ☐ [S46]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 20-F, filed 2026-10-21, L169:

> You should read this annual report and the documents that we refer to in this annual report and have filed as exhibits to this annual report completely and with the understanding that our actual future results may be materially different from what we expect. Factors that may cause actual results to differ materially from current expectations include, among other things, those listed under the heading “Risk Factors” and elsewhere in this annual report. If one or more of these risks or uncertainties occur, or if our underlying assumptions prove to be incorrect, actual events or results may vary significantly from those implied or projected by the forward-looking statements. No forward-looking statement is a guarantee of future performance. [S46]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 20-F, 3, 424B4, 6-K, 8-A12B, CERT, CORRESP, DRS, DRS/A, DRSLTR, EFFECT, F-1, F-1/A, FWP, NT 20-F, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:36:35.767329+00:00.

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
| 2026-10-21 | 20-F | 0001213900-26-111364 | — | [S03] |
| 2026-09-08 | 6-K | 0001213900-26-098109 | — | [S04] |
| 2026-06-30 | 6-K | 0001213900-26-073728 | — | [S05] |
| 2026-04-08 | 3 | 0001213900-26-041249 | — | [S06] |
| 2026-04-08 | 3 | 0001213900-26-041248 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-11-01T16:07:03.070084+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0002038378.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [20-F 0001213900-26-111364](https://www.sec.gov/Archives/edgar/data/2038378/000121390026111364/0001213900-26-111364-index.html) — published 2026-10-21; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [6-K 0001213900-26-098109](https://www.sec.gov/Archives/edgar/data/2038378/000121390026098109/0001213900-26-098109-index.html) — published 2026-09-08; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [6-K 0001213900-26-073728](https://www.sec.gov/Archives/edgar/data/2038378/000121390026073728/0001213900-26-073728-index.html) — published 2026-06-30; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [3 0001213900-26-041249](https://www.sec.gov/Archives/edgar/data/2038378/000121390026041249/0001213900-26-041249-index.html) — published 2026-04-08; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [3 0001213900-26-041248](https://www.sec.gov/Archives/edgar/data/2038378/000121390026041248/0001213900-26-041248-index.html) — published 2026-04-08; retrieved 2026-10-23T08:33:02.691743+00:00.

[S46] [20-F 0001213900-26-111364](https://www.sec.gov/Archives/edgar/data/2038378/000121390026111364/ea0308052-20f_acco.htm) — published 2026-10-21; retrieved 2026-11-02T22:10:49.507465+00:00.

Source release: `coverage-20261101-41324509967-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/ef36a46d682e789d5949ebe61d4ec5a6bea5f3de/brain/companies/ACCL/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
