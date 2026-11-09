---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001033767
cik: '0001033767'
company_name: UNITED MICROELECTRONICS CORP
tickers:
- UMC
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
  - 20-F/A
  - '3'
  - '4'
  - 424B5
  - 6-K
  - 6-K/A
  - CORRESP
  - EFFECT
  - F-3/A
  - F-6
  - F-6 POS
  - F-6EF
  - S-8
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13G/A
  - SD
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001033767.json
    sha256: cf2e7cb99d4360e8f313b46a31bd6ef7f4062ae98f48c3eb3df2adbf1754423c
    retrieved_at: '2026-10-24T13:22:51.759433+00:00'
    archive: &id001
      member: CIK0001033767.json
      sha256: 593fbbea6512ef5ec729a5e513c465fbedaac8a66602c0abe00d0ba5a4d18732
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: otherlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt
  published_at: null
  retrieved_at: '2026-11-01T16:07:03.340031+00:00'
  sha256: ee0a872edece98430f3ba5a1ed6e9c683d7a1bb4b2980bdc9743c6995f264398
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001033767.json
  published_at: null
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: cf2e7cb99d4360e8f313b46a31bd6ef7f4062ae98f48c3eb3df2adbf1754423c
- id: S03
  title: 6-K 0001193125-26-429369
  url: https://www.sec.gov/Archives/edgar/data/1033767/000119312526429369/0001193125-26-429369-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S04
  title: 6-K 0001193125-26-419602
  url: https://www.sec.gov/Archives/edgar/data/1033767/000119312526419602/0001193125-26-419602-index.html
  published_at: '2026-10-13'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S05
  title: 6-K 0001193125-26-414888
  url: https://www.sec.gov/Archives/edgar/data/1033767/000119312526414888/0001193125-26-414888-index.html
  published_at: '2026-10-06'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S06
  title: 6-K/A 0001193125-26-413417
  url: https://www.sec.gov/Archives/edgar/data/1033767/000119312526413417/0001193125-26-413417-index.html
  published_at: '2026-10-05'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S07
  title: 6-K 0001193125-26-413371
  url: https://www.sec.gov/Archives/edgar/data/1033767/000119312526413371/0001193125-26-413371-index.html
  published_at: '2026-10-05'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S55
  url: https://www.sec.gov/Archives/edgar/data/1033767/000119312526193757/d91630d20f.htm
  title: 20-F 0001193125-26-193757
  published_at: '2026-04-30'
  retrieved_at: '2026-11-01T16:23:01.301927+00:00'
  sha256: fb5209e4f5b516ff0b6ab257880715b120d3e6e2f77da288a3f27a24348d10e0
issuer_classification:
  cik: '0001033767'
  classification_status: reported_sic
  entity_type: other
  name: UNITED MICROELECTRONICS CORP
  sic: '3674'
  sic_description: Semiconductors & Related Devices
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: cf2e7cb99d4360e8f313b46a31bd6ef7f4062ae98f48c3eb3df2adbf1754423c
  url: https://data.sec.gov/submissions/CIK0001033767.json
listings:
- ticker: UMC
  exchange: NYSE
  instrument_type: common_stock
research_filings:
- accession: 0001193125-26-193757
  filed: '2026-04-30'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1033767/000119312526193757/0001193125-26-193757-index.html
- accession: 0001193125-06-027814
  filed: '2006-02-13'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1033767/000119312506027814/0001193125-06-027814-index.html
- accession: 0001193125-26-429369
  filed: '2026-10-23'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1033767/000119312526429369/0001193125-26-429369-index.html
- accession: 0001193125-26-413417
  filed: '2026-10-05'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1033767/000119312526413417/0001193125-26-413417-index.html
- accession: 0001564590-21-036027
  filed: '2021-07-08'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1033767/000156459021036027/0001564590-21-036027-index.html
- accession: 0001309014-13-000658
  filed: '2013-09-26'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1033767/000130901413000658/0001309014-13-000658-index.html
research_progress:
  stage: evidence_collected
  input_sha256: 41f99ac6e9a88513f83955edd5db9bfa08f3eabddb3a61d2d28acc167126e711
  last_attempt_at: '2026-11-01T16:17:56.222188+00:00'
  last_success_at: '2026-11-01T16:17:56.222188+00:00'
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
  source_url: https://data.sec.gov/submissions/CIK0001033767.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/2a475d5f7d7de42ae2b318e51e43cda99027f72f/brain/companies/UMC/README.md
full_history_commit: 2a475d5f7d7de42ae2b318e51e43cda99027f72f
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# UMC — UNITED MICROELECTRONICS CORP

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/2a475d5f7d7de42ae2b318e51e43cda99027f72f/brain/companies/UMC/README.md)

## Business overview

Reported issuer name: **UNITED MICROELECTRONICS CORP**. Stable SEC CIK: **0001033767**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| UMC | NYSE | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 20-F, filed 2026-04-30, L499:

> Our disclosure and analysis in this Annual Report contain or incorporate by reference some forward-looking statements. We have based these forward-looking statements on our current expectations and projections about future events. You can identify forward-looking statements by the fact that they do not relate strictly to historical or current facts. The words “may,” “will,” “is/are likely to,” “anticipate,” “believe,” “estimate,” “expect,” “intend,” “plan” and similar expressions are intended to identify a number of these forward-looking statements. Forward-looking statements in this Annual Report include, but are not limited to, statements regarding our business strategies and future plans, anticipated business condition and financial results, our capital expenditure plans, our capacity management plans, expectations as to the capabilities of our technologies and manufacturing process, technological upgrades, investment in research and development, future market demand, regulatory or other developments in our industry, business expansion plans or new investments as well as business acquisitions and financing plans. Please see “Item 3. Key Information—D. Risk Factors” for a further discussion of certain factors that may cause actual results to differ materially from those indicated by our forward-looking statements. Although we believe that these expectations and projections … [S55]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 20-F, filed 2026-04-30, L737:

> In addition, even when these crises have abated, there could be lingering effects from these types of crises on our business, including a significant reduction in orders from our customers, insolvency of key suppliers resulting in product delays, inability of customers to obtain credit to finance purchases of our products, customer insolvencies and bankruptcies, and counterparty failures negatively impacting our treasury operations. Any future systemic political, economic or financial crisis could cause revenues for the semiconductor industry as a whole to decline dramatically, and if the economic condition or financial condition of our customers were to deteriorate, additional accounting related allowances may be required in the future and such additional allowances could increase our operating expenses and therefore reduce our operating income and net income. Any disruption in global trade conditions such as an increase in tariffs or the escalation of regional trade tensions will indirectly impact the global business environment which may adversely impact our business, results of operations and financial condition. [S55]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 20-F, filed 2026-04-30, L736:

> In recent times, several major systemic economic and financial crises have negatively affected global business, banking and financial sectors, including the semiconductor industry and markets. These types of crises cause turmoil in global markets that often result in declines in electronic product sales from which we generate our income through our goods and services. In addition, these crises may cause various indirect effects such as undermining the ability of our customers to remain competitive when faced with the financial and economic challenges created by adverse political and macroeconomic conditions and by companies struggling to survive in the wake of these crises. For example, beginning in early 2023, the semiconductor industry was affected by an economic downturn that resulted in reduced demand for consumer electronics and other products incorporating semiconductors, which in turn affected our business operations and financial condition. While there were signs of recovery since 2024, the industry continued to face challenges from global economic uncertainties. [S55]

## Industry and value chain

SEC-reported SIC **3674**: Semiconductors & Related Devices. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 20-F, filed 2026-04-30, L769:

> our ability to obtain equipment, raw materials, electricity, water and other required utilities on a timely and economic basis; [S55]

Navigation sector: **information-technology**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 20-F, filed 2026-04-30, L810:

> The semiconductor industry is characterized by rapidly evolving and constantly changing technology. If we do not anticipate the technology evolution and rapidly adopt new and innovative technology, we may not be able to produce sufficiently advanced services at competitive prices. Our competitors may adopt new technology before we do and reduce our ability to compete effectively in the market. If we are unable to begin offering advanced services and processes on a competitive and timely basis, we may lose customers to our competitors providing similar technologies, which may cause our operating revenues to decline unless we can replace lost customers with new customers. In addition, the market prices for advanced technology and services tend to fall over time. As a result, if we are unable to offer new advanced services and processes on a competitive and timely basis, we may need to reduce prices that we set for our existing services and processes, which would have a negative effect on our profitability. We also depend upon the introduction of new technologies on a timely basis in order to benefit from the relatively higher prices such new technologies offer in the earlier stages of their life cycles. If we are unable to introduce new technologies on a timely and competitive basis, we may not be able to benefit from the relatively higher prices for new technologies, and our … [S55]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 20-F, filed 2026-04-30, L813:

> In addition, some of our customers rely upon third-party vendors, or intellectual property (IP) vendors, for the IP they embed into their designs. Although we work and collaborate with IP vendors with respect to such matters, there can be no guarantee that we will be successful or that the vendors will deliver according to our requirements or the needs of our customers. Failures to meet the targets or to deliver on a timely basis could cause customers to cancel orders and/or shift capacity to other suppliers. [S55]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 20-F, filed 2026-04-30, L964:

> The success of our business depends upon attracting and retaining experienced executives, engineers and other employees to implement our strategy. The competition for skilled employees is intense in our industry, which is exacerbated by the shortage of qualified personnel with appropriate experiences and expertise. We expect demand for personnel in Taiwan to increase in the future as new wafer fabrication facilities and other businesses are established in Taiwan. We also expect demand for experienced personnel in other locations to increase significantly as our competitors establish and expand their operations. Some of our competitors are willing to offer better compensation than what we do to our executives, engineers and other employees. We do not have long-term employment contracts with any of our employees. If we were unable to retain our existing personnel or attract, assimilate and recruit new experienced personnel in the future, it could seriously disrupt our operations and delay or restrict the growth of our business. [S55]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 20-F, filed 2026-04-30, L127:

> Indicate by check mark whether any of those error corrections are restatements that required a recovery analysis of incentive-based compensation received by any of the registrant’s executive officers during the relevant recovery period pursuant to [S55]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 20-F, filed 2026-04-30, L499:

> Our disclosure and analysis in this Annual Report contain or incorporate by reference some forward-looking statements. We have based these forward-looking statements on our current expectations and projections about future events. You can identify forward-looking statements by the fact that they do not relate strictly to historical or current facts. The words “may,” “will,” “is/are likely to,” “anticipate,” “believe,” “estimate,” “expect,” “intend,” “plan” and similar expressions are intended to identify a number of these forward-looking statements. Forward-looking statements in this Annual Report include, but are not limited to, statements regarding our business strategies and future plans, anticipated business condition and financial results, our capital expenditure plans, our capacity management plans, expectations as to the capabilities of our technologies and manufacturing process, technological upgrades, investment in research and development, future market demand, regulatory or other developments in our industry, business expansion plans or new investments as well as business acquisitions and financing plans. Please see “Item 3. Key Information—D. Risk Factors” for a further discussion of certain factors that may cause actual results to differ materially from those indicated by our forward-looking statements. Although we believe that these expectations and projections … [S55]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 20-F, 20-F/A, 3, 4, 424B5, 6-K, 6-K/A, CORRESP, EFFECT, F-3/A, F-6, F-6 POS, F-6EF, S-8, SC 13D, SC 13D/A, SC 13G, SC 13G/A, SCHEDULE 13G/A, SD, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:30:59.616713+00:00.

### Research work queue

Collection stage: **evidence_collected**. Extracted evidence is not a reviewed conclusion. Daily collection resumes from durable state; unchanged accessions are reused.

- **Business overview** (source excerpts available; assess the claim): Explain what the company does, who pays it, and why the business exists. Cite primary sources.
- **Revenue model and segments** (evidence or analysis still needed): Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.
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
| 2026-10-23 | 6-K | 0001193125-26-429369 | — | [S03] |
| 2026-10-13 | 6-K | 0001193125-26-419602 | — | [S04] |
| 2026-10-06 | 6-K | 0001193125-26-414888 | — | [S05] |
| 2026-10-05 | 6-K/A | 0001193125-26-413417 | — | [S06] |
| 2026-10-05 | 6-K | 0001193125-26-413371 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-11-01T16:07:03.340031+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001033767.json) — published not supplied; retrieved 2026-10-24T13:22:51.759433+00:00.

[S03] [6-K 0001193125-26-429369](https://www.sec.gov/Archives/edgar/data/1033767/000119312526429369/0001193125-26-429369-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S04] [6-K 0001193125-26-419602](https://www.sec.gov/Archives/edgar/data/1033767/000119312526419602/0001193125-26-419602-index.html) — published 2026-10-13; retrieved 2026-10-24T13:22:51.759433+00:00.

[S05] [6-K 0001193125-26-414888](https://www.sec.gov/Archives/edgar/data/1033767/000119312526414888/0001193125-26-414888-index.html) — published 2026-10-06; retrieved 2026-10-24T13:22:51.759433+00:00.

[S06] [6-K/A 0001193125-26-413417](https://www.sec.gov/Archives/edgar/data/1033767/000119312526413417/0001193125-26-413417-index.html) — published 2026-10-05; retrieved 2026-10-24T13:22:51.759433+00:00.

[S07] [6-K 0001193125-26-413371](https://www.sec.gov/Archives/edgar/data/1033767/000119312526413371/0001193125-26-413371-index.html) — published 2026-10-05; retrieved 2026-10-24T13:22:51.759433+00:00.

[S55] [20-F 0001193125-26-193757](https://www.sec.gov/Archives/edgar/data/1033767/000119312526193757/d91630d20f.htm) — published 2026-04-30; retrieved 2026-11-01T16:23:01.301927+00:00.

Source release: `coverage-20261101-41324509967-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/2a475d5f7d7de42ae2b318e51e43cda99027f72f/brain/companies/UMC/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
