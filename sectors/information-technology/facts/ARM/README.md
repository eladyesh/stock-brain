---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001973239
cik: 0001973239
company_name: ARM HOLDINGS PLC /UK
tickers:
- ARM
status: stub
canonical_reviewed: false
as_of: '2026-11-01'
updated_at: '2026-11-01T16:11:48.803754+00:00'
reviewed_at: null
coverage_release: coverage-20261101-41324509967-1
source_commit: 234e59eb75b5e3b9e02d4dd8de10d83fc60c027c
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
  - F-6
  - F-6/A
  - IRANNOTICE
  - S-8
  - S-8 POS
  - SC 13G
  - SD
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001973239.json
    sha256: 075421d51ae45a917fc266357e515a4b21d2ee74e0ce4922fa7b38e2da2355fa
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001973239.json
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
  url: https://data.sec.gov/submissions/CIK0001973239.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 075421d51ae45a917fc266357e515a4b21d2ee74e0ce4922fa7b38e2da2355fa
- id: S03
  title: 4 0001973239-26-000136
  url: https://www.sec.gov/Archives/edgar/data/1973239/000197323926000136/0001973239-26-000136-index.html
  published_at: '2026-09-23'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 144 0001959173-26-007048
  url: https://www.sec.gov/Archives/edgar/data/1973239/000195917326007048/0001959173-26-007048-index.html
  published_at: '2026-09-21'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 6-K 0001973239-26-000135
  url: https://www.sec.gov/Archives/edgar/data/1973239/000197323926000135/0001973239-26-000135-index.html
  published_at: '2026-09-18'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 4 0001973239-26-000133
  url: https://www.sec.gov/Archives/edgar/data/1973239/000197323926000133/0001973239-26-000133-index.html
  published_at: '2026-09-16'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 4 0001973239-26-000130
  url: https://www.sec.gov/Archives/edgar/data/1973239/000197323926000130/0001973239-26-000130-index.html
  published_at: '2026-09-10'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S54
  url: https://www.sec.gov/Archives/edgar/data/1973239/000197323926000097/arm-20260331.htm
  title: 20-F 0001973239-26-000097
  published_at: '2026-05-26'
  retrieved_at: '2026-11-14T18:43:01.708889+00:00'
  sha256: 8ff0426902d1670f189dc9f1c4e928a8fd7ff4ede0b956a89426428ce9dd0927
issuer_classification:
  cik: 0001973239
  classification_status: reported_sic
  entity_type: other
  name: ARM HOLDINGS PLC /UK
  sic: '3674'
  sic_description: Semiconductors & Related Devices
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 075421d51ae45a917fc266357e515a4b21d2ee74e0ce4922fa7b38e2da2355fa
  url: https://data.sec.gov/submissions/CIK0001973239.json
listings:
- ticker: ARM
  exchange: NASDAQ
  instrument_type: depositary_receipt
research_filings:
- accession: 0001973239-26-000097
  filed: '2026-05-26'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1973239/000197323926000097/0001973239-26-000097-index.html
- accession: 0001973239-26-000135
  filed: '2026-09-18'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1973239/000197323926000135/0001973239-26-000135-index.html
research_progress:
  stage: evidence_collected
  input_sha256: f695f43368684574e139c6be850adb844cdc18f3900382f6d45ce1a15424870c
  last_attempt_at: '2026-11-14T18:39:40.176158+00:00'
  last_success_at: '2026-11-14T18:39:40.176158+00:00'
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
  sector: information-technology
  method: project_sic_rule
  sic: '3674'
  sic_description: Semiconductors & Related Devices
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001973239.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/8c5afb0854b43beae818b88ec42b173c9411d269/brain/companies/ARM/README.md
full_history_commit: 8c5afb0854b43beae818b88ec42b173c9411d269
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# ARM — ARM HOLDINGS PLC /UK

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/8c5afb0854b43beae818b88ec42b173c9411d269/brain/companies/ARM/README.md)

## Business overview

Reported issuer name: **ARM HOLDINGS PLC /UK**. Stable SEC CIK: **0001973239**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| ARM | NASDAQ | depositary_receipt | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 20-F, filed 2026-05-26, L266:

> We have historically conducted our business through Arm Limited. As a result of the corporate reorganization between entities under common control, the historical consolidated financial statements of the Company were retrospectively adjusted for the change in reporting entity. Therefore, the historical consolidated financial statements of Arm Limited became the historical consolidated financial statements of Arm Holdings plc as of the date of the corporate reorganization. Our corporate reorganization is described in the section titled “Item 4. Information on the Company—A. History and Development of the Company—Corporate Reorganization.” [S54]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 20-F, filed 2026-05-26, L414:

> Our IP business relies on our customers to design, manufacture and sell chips incorporating our products in order to generate royalty revenue. A substantial portion of our revenue depends upon the commencement of new design projects by semiconductor companies, OEMs, and CSPs, and their ability to provide complete chips based on our products to meet the specific application needs of their customers. However, our customers are not contractually obligated to design, manufacture, sell or deploy chips using our products on an exclusive basis or at all. Some of our existing customers design, manufacture, sell and deploy chips based on competing technology, including their own, and other existing or potential customers may do so in the future. To the extent that our customers elect to license technology from competitors, our competitive position could be adversely affected and we could lose market share. Furthermore, under many of our arrangements with customers, there is generally no minimum purchase obligation or guaranteed revenue stream. [S54]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 20-F, filed 2026-05-26, L269:

> This Annual Report contains estimates, projections and other information concerning our industry, our business and the markets for our products, including, but not limited to, our general expectations and market position, market opportunity and market size. Information that is based on estimates, forecasts, projections, market research or similar methodologies is inherently subject to uncertainties, and actual events or circumstances may differ materially from events and circumstances that are assumed in this information. Unless otherwise expressly stated, we obtained this industry, business, market and other data from our own internal estimates and research as well as from reports, research surveys, studies and similar data prepared by market research firms and other third parties, industry and general publications, government data and similar sources. While we are responsible for the accuracy of such information and believe our internal company research as to such matters is reliable and the market definitions are appropriate, neither such research nor these definitions have been verified by any independent source. [S54]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 20-F, filed 2026-05-26, L275:

> •our dependence on the semiconductor and electronics industries and the demand for our products and the products of our customers; [S54]

## Industry and value chain

SEC-reported SIC **3674**: Semiconductors & Related Devices. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 20-F, filed 2026-05-26, L372:

> Our entry into production silicon exposes us to new manufacturing, supply chain, and inventory risks that differ materially from our traditional IP licensing business, including dependence on third-party foundry partners and contract manufacturers for fabrication with limited control over their production capacity, costs, yields, or delivery schedules; the potential for manufacturing defects, lower-than-expected yields, and quality control issues, any of which could result in product recalls, warranty claims, and reputational damage; significant upfront capital commitments and purchase obligations for wafer supply, packaging, and testing services that may be difficult to adjust in response to demand fluctuations; inventory management challenges, including obsolescence risk, write-downs, and the need to maintain safety stock; complex supply chain dependencies on memory suppliers, packaging vendors, and system integrators; price [S54]

Navigation sector: **information-technology**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 20-F, filed 2026-05-26, L370:

> There are risks inherent in the manufacturing of next-generation process technologies, such as the Arm AGI CPU, including production timing delays, lower-than-anticipated manufacturing yields, and product defects and errors. Such products often have long manufacturing lead times. If we inaccurately estimate demand, or if our customers change orders, we may not be able to reduce our supply commitments in time, at the same rate, or at all. If we underestimate demand, and our third-party foundry partners and contract manufacturers are unable to increase production or provide sufficient supply, we may not be able to meet customer demand or achieve our expected time to market in a timely manner, or at all. In either event, our reputation and customer relationships could be damaged and we could lose revenue and market share. Similarly, if we overestimate demand, or if customers cancel or defer orders or choose to purchase from our competitors, we may not be able to utilize on-hand inventory or reduce purchase commitments accordingly. [S54]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 20-F, filed 2026-05-26, L285:

> •our ability to protect our proprietary products and our brand, and the costs of protecting such intellectual property (“IP”) rights, particularly as a result of litigation; [S54]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 20-F, filed 2026-05-26, L452:

> A significant portion of our total revenue is generated from a limited number of key customers. In particular, our top five customers (including Arm China and SoftBank Group) collectively accounted for approximately 57%, 56% and 54% of our total revenue for the fiscal years ended March 31, 2026, 2025 and 2024, respectively, and our largest customer individually, Arm China, accounted for approximately 16%, 17% and 21% of our total revenue, respectively, during those fiscal years. A portion of our near-term revenue is dependent on commercial arrangements with SoftBank Group and/or its affiliates. Any reduction, restructuring, delay, or termination of such arrangements could adversely affect our business, results of operations, and financial condition. As a result of this customer concentration, we are particularly susceptible to adverse developments affecting our key customers and their respective businesses, including industry downturns, decreased demand for their products, increased competition, changes in trade protection and other government policies, financial hardship and changes in their business model, purchasing behavior and strategic priorities, among other factors, many of which are beyond our control. In particular, developments in our key customers’ respective businesses that adversely affect their ability to satisfy their payment obligations to us or result in … [S54]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 20-F, filed 2026-05-26, L74:

> Indicate by check mark whether any of those error corrections are restatements that required a recovery analysis of incentive based compensation received by any of the registrant’s executive officers during the relevant recovery period pursuant to §240.10D-1(b). ☐ [S54]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 20-F, filed 2026-05-26, L270:

> In addition, assumptions and estimates of our and our industry’s future performance are necessarily subject to a high degree of uncertainty and risk due to a variety of factors, including those described in the section titled “Item 3. Key Information—D. Risk Factors.” These and other factors could cause our future performance to differ materially from our assumptions and estimates. See “Special Note Regarding Forward-Looking Statements.” [S54]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 144, 20-F, 3, 4, 424B4, 6-K, 8-A12B, CERT, CORRESP, DRS, DRS/A, DRSLTR, EFFECT, F-1, F-1/A, F-6, F-6/A, IRANNOTICE, S-8, S-8 POS, SC 13G, SD, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:36:28.478902+00:00.

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
| 2026-09-23 | 4 | 0001973239-26-000136 | — | [S03] |
| 2026-09-21 | 144 | 0001959173-26-007048 | — | [S04] |
| 2026-09-18 | 6-K | 0001973239-26-000135 | — | [S05] |
| 2026-09-16 | 4 | 0001973239-26-000133 | — | [S06] |
| 2026-09-10 | 4 | 0001973239-26-000130 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-11-01T16:07:03.070084+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001973239.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [4 0001973239-26-000136](https://www.sec.gov/Archives/edgar/data/1973239/000197323926000136/0001973239-26-000136-index.html) — published 2026-09-23; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [144 0001959173-26-007048](https://www.sec.gov/Archives/edgar/data/1973239/000195917326007048/0001959173-26-007048-index.html) — published 2026-09-21; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [6-K 0001973239-26-000135](https://www.sec.gov/Archives/edgar/data/1973239/000197323926000135/0001973239-26-000135-index.html) — published 2026-09-18; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [4 0001973239-26-000133](https://www.sec.gov/Archives/edgar/data/1973239/000197323926000133/0001973239-26-000133-index.html) — published 2026-09-16; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [4 0001973239-26-000130](https://www.sec.gov/Archives/edgar/data/1973239/000197323926000130/0001973239-26-000130-index.html) — published 2026-09-10; retrieved 2026-10-23T08:33:02.691743+00:00.

[S54] [20-F 0001973239-26-000097](https://www.sec.gov/Archives/edgar/data/1973239/000197323926000097/arm-20260331.htm) — published 2026-05-26; retrieved 2026-11-14T18:43:01.708889+00:00.

Source release: `coverage-20261101-41324509967-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/8c5afb0854b43beae818b88ec42b173c9411d269/brain/companies/ARM/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
