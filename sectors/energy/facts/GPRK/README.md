---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001464591
cik: 0001464591
company_name: GeoPark Ltd
tickers:
- GPRK
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
  - '4'
  - 424B1
  - 6-K
  - 6-K/A
  - 8-A12B
  - CERT
  - CERTNYS
  - CORRESP
  - CT ORDER
  - D
  - DRS
  - EFFECT
  - F-1
  - F-1/A
  - FWP
  - S-8
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SC TO-C
  - SC TO-I
  - SC TO-I/A
  - SCHEDULE 13D
  - SCHEDULE 13D/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - SD
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001464591.json
    sha256: 392629419926d81b074068246e819c85979833a78c86cc264f70780c7f75cd4b
    retrieved_at: '2026-10-24T13:22:51.759433+00:00'
    archive: &id001
      member: CIK0001464591.json
      sha256: 593fbbea6512ef5ec729a5e513c465fbedaac8a66602c0abe00d0ba5a4d18732
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: otherlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt
  published_at: null
  retrieved_at: '2026-10-30T16:00:12.358089+00:00'
  sha256: a960a0bfc5439fac9e467fe07ef1f44afe893ba2afc3297648321a80ce09971e
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001464591.json
  published_at: null
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 392629419926d81b074068246e819c85979833a78c86cc264f70780c7f75cd4b
- id: S03
  title: 6-K 0000950103-26-016049
  url: https://www.sec.gov/Archives/edgar/data/1464591/000095010326016049/0000950103-26-016049-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S04
  title: 6-K 0000950103-26-015979
  url: https://www.sec.gov/Archives/edgar/data/1464591/000095010326015979/0000950103-26-015979-index.html
  published_at: '2026-10-22'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S05
  title: 6-K 0001104659-26-117643
  url: https://www.sec.gov/Archives/edgar/data/1464591/000110465926117643/0001104659-26-117643-index.html
  published_at: '2026-10-21'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S06
  title: 6-K 0000950103-26-015692
  url: https://www.sec.gov/Archives/edgar/data/1464591/000095010326015692/0000950103-26-015692-index.html
  published_at: '2026-10-16'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S07
  title: 6-K 0000950103-26-015691
  url: https://www.sec.gov/Archives/edgar/data/1464591/000095010326015691/0000950103-26-015691-index.html
  published_at: '2026-10-16'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S54
  url: https://www.sec.gov/Archives/edgar/data/1464591/000110465926037819/gprk-20251231x20f.htm
  title: 20-F 0001104659-26-037819
  published_at: '2026-03-31'
  retrieved_at: '2026-10-27T15:40:56.043595+00:00'
  sha256: ffbe6a7741f937e902e57fc9dd963857e54eb16f5e7bf4c5090496d41ec8511d
issuer_classification:
  cik: 0001464591
  classification_status: reported_sic
  entity_type: other
  name: GeoPark Ltd
  sic: '1311'
  sic_description: Crude Petroleum & Natural Gas
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 392629419926d81b074068246e819c85979833a78c86cc264f70780c7f75cd4b
  url: https://data.sec.gov/submissions/CIK0001464591.json
listings:
- ticker: GPRK
  exchange: NYSE
  instrument_type: common_stock
research_filings:
- accession: 0001104659-26-037819
  filed: '2026-03-31'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1464591/000110465926037819/0001104659-26-037819-index.html
- accession: 0000950103-26-016049
  filed: '2026-10-23'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1464591/000095010326016049/0000950103-26-016049-index.html
- accession: 0000950103-20-005878
  filed: '2020-03-24'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1464591/000095010320005878/0000950103-20-005878-index.html
research_progress:
  stage: evidence_collected
  input_sha256: aa3e20b22276beee83142811c2181bcd14f91129a1eb8f23ab2a428eae7dc071
  last_attempt_at: '2026-10-27T15:36:38.956292+00:00'
  last_success_at: '2026-10-27T15:36:38.956292+00:00'
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
  sector: energy
  method: project_sic_rule
  sic: '1311'
  sic_description: Crude Petroleum & Natural Gas
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001464591.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/79888139fa1fe8ad3404e6bc04e318eee1474f73/brain/companies/GPRK/README.md
full_history_commit: 79888139fa1fe8ad3404e6bc04e318eee1474f73
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# GPRK — GeoPark Ltd

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/79888139fa1fe8ad3404e6bc04e318eee1474f73/brain/companies/GPRK/README.md)

## Business overview

Reported issuer name: **GeoPark Ltd**. Stable SEC CIK: **0001464591**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| GPRK | NYSE | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 20-F, filed 2026-03-31, L748:

> Market data, other statistical information, information regarding recent developments in the countries in which we operate, and certain industry forecast data used in this annual report were obtained from internal reports and studies, where appropriate, as well as estimates, market research, publicly available information and industry publications. Industry publications generally state that the information they include has been obtained from sources believed to be reliable, but that the accuracy and completeness of such information is not guaranteed. Similarly, internal reports and studies, estimates and market research, which we believe to be reliable and accurately extracted by us for use in this annual report, have not been independently verified. However, we believe such data is accurate and agree that we are responsible for the accurate extraction of such information from such sources and its correct reproduction in this annual report. [S54]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 20-F, filed 2026-03-31, L15809:

> Operating segments are reported in a manner consistent with the internal reporting provided to the chief operating decision-maker. The chief operating decision-maker, who is responsible for allocating resources and assessing performance of the operating segments, has been identified as the Executive Committee. This committee is integrated by the Chief Executive Officer, Chief Financial Officer, Chief Exploration and Development Officer, Chief Operating Officer and Chief People Officer. This committee reviews the Group’s internal reporting in order to assess performance and allocate resources. Management has determined the operating segments based on these reports. The committee considers the business from a geographic perspective. No operating segments have been aggregated to form the reportable segments. [S54]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 20-F, filed 2026-03-31, L998:

> financing may reduce customers’ liquidity and ability to make payments or perform obligations. Some customers may be highly leveraged and subject to their own operating expenses, which may increase risk. Customers may also be subject to regulatory changes that could increase default risk. Financial problems could impair our assets, decrease operating cash flows, and reduce or curtail customers’ future use of our products and services, adversely affecting revenues and potentially leading to a reduction in reserves. [S54]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 20-F, filed 2026-03-31, L994:

> We are exposed to the credit risks of our customers and any material nonpayment or nonperformance by our key customers could adversely affect our cash flow and results of operations. [S54]

## Industry and value chain

SEC-reported SIC **1311**: Crude Petroleum & Natural Gas. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 20-F, filed 2026-03-31, L788:

> \| \| ● \| potential impacts that tariffs may have on our cost structure, supply chain, and commodity markets; [S54]

Navigation sector: **energy**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 20-F, filed 2026-03-31, L849:

> Our results are highly sensitive to crude oil and natural gas price volatility. A substantial or extended decline in prices, wider differentials, or higher transportation costs could materially and adversely affect our business, financial condition and results of operations and may require changes to our corporate strategy. Our ability to sustain production depends on replacing reserves and successfully identifying and developing commercial prospects, and our reserve estimates rely on assumptions that may prove inaccurate. Drilling and development activities are subject to subsurface uncertainty and execution risks, including well under‑performance, cost overruns and delays, and we face competition for capital, acreage, services and talent as well as potential shortages or late delivery of key inputs and constraints in third‑party infrastructure (including pipelines, trucking and ports), which may limit volumes and increase costs. [S54]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 20-F, filed 2026-03-31, L1047:

> We rely on information technology systems, including systems which are managed or provided by third-party providers, to conduct our business and support our exploration, development, and production activities. We increasingly depend on digital technologies, such as applications, a cloud environment, mobile platforms, computers, and telecommunications systems. We collect, use, transmit, store, and otherwise process data using information technology systems, including systems owned and maintained by us or our third-party providers. These data include confidential information and intellectual property belonging to us or our customers or other business partners. [S54]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 20-F, filed 2026-03-31, L851:

> We are subject to obligations under E&P contracts, exploration permits, exploitation concessions and concession agreements (including minimum work, reporting and discovery declarations) to retain our interests; failure to comply may result in penalties or the loss or early termination of rights in undeveloped areas, and some rights are subject to expiration or early termination based on operating conditions. We may not control budgets, timing, costs or production rates in non‑operated or non‑wholly owned assets. Our strategy includes acquisitions, strategic investments, partnerships and alliances; completed acquisitions may be difficult to integrate and may divert management attention, dilute stockholder value or lead to impairments, and future or pending transactions may be delayed, re‑priced, fail to close or otherwise not deliver expected benefits. We also derive a significant portion of revenues from a few key customers, exposing us to counterparty and credit risks, and U.S. trade tariffs or supply‑chain constraints could adversely affect costs and market access. [S54]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 20-F, filed 2026-03-31, L102:

> Indicate by check mark whether any of those error corrections are restatements that required a recovery analysis of incentive-based compensation received by any of the registrant’s executive officers during the relevant recovery period pursuant to §240.10D-1(b). ☐ [S54]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 20-F, filed 2026-03-31, L757:

> Forward-looking statements appear in several places in this annual report and include, but are not limited to, statements regarding our intent, belief or current expectations. Forward-looking statements are based on our management’s beliefs and assumptions and on information currently available to our management. Such statements are subject to risks and uncertainties, and actual results may differ materially from those expressed or implied in the forward-looking statements due to various factors, including, but not limited to, those identified under the section “Item 3. Key Information—D. Risk factors” in this annual report. These risks and uncertainties include factors relating to: [S54]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 144, 20-F, 3, 4, 424B1, 6-K, 6-K/A, 8-A12B, CERT, CERTNYS, CORRESP, CT ORDER, D, DRS, EFFECT, F-1, F-1/A, FWP, S-8, SC 13D, SC 13D/A, SC 13G, SC 13G/A, SC TO-C, SC TO-I, SC TO-I/A, SCHEDULE 13D, SCHEDULE 13D/A, SCHEDULE 13G, SCHEDULE 13G/A, SD, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:33:28.880314+00:00.

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
| 2026-10-23 | 6-K | 0000950103-26-016049 | — | [S03] |
| 2026-10-22 | 6-K | 0000950103-26-015979 | — | [S04] |
| 2026-10-21 | 6-K | 0001104659-26-117643 | — | [S05] |
| 2026-10-16 | 6-K | 0000950103-26-015692 | — | [S06] |
| 2026-10-16 | 6-K | 0000950103-26-015691 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-30T16:00:12.358089+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001464591.json) — published not supplied; retrieved 2026-10-24T13:22:51.759433+00:00.

[S03] [6-K 0000950103-26-016049](https://www.sec.gov/Archives/edgar/data/1464591/000095010326016049/0000950103-26-016049-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S04] [6-K 0000950103-26-015979](https://www.sec.gov/Archives/edgar/data/1464591/000095010326015979/0000950103-26-015979-index.html) — published 2026-10-22; retrieved 2026-10-24T13:22:51.759433+00:00.

[S05] [6-K 0001104659-26-117643](https://www.sec.gov/Archives/edgar/data/1464591/000110465926117643/0001104659-26-117643-index.html) — published 2026-10-21; retrieved 2026-10-24T13:22:51.759433+00:00.

[S06] [6-K 0000950103-26-015692](https://www.sec.gov/Archives/edgar/data/1464591/000095010326015692/0000950103-26-015692-index.html) — published 2026-10-16; retrieved 2026-10-24T13:22:51.759433+00:00.

[S07] [6-K 0000950103-26-015691](https://www.sec.gov/Archives/edgar/data/1464591/000095010326015691/0000950103-26-015691-index.html) — published 2026-10-16; retrieved 2026-10-24T13:22:51.759433+00:00.

[S54] [20-F 0001104659-26-037819](https://www.sec.gov/Archives/edgar/data/1464591/000110465926037819/gprk-20251231x20f.htm) — published 2026-03-31; retrieved 2026-10-27T15:40:56.043595+00:00.

Source release: `coverage-20261030-41085569265-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/79888139fa1fe8ad3404e6bc04e318eee1474f73/brain/companies/GPRK/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
