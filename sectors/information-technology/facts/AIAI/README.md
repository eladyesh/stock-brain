---
schema_version: 1
document_type: company_facts
company_id: company-cik-0002096362
cik: 0002096362
company_name: AIAI Holdings Corp
tickers:
- AIAI
status: stub
canonical_reviewed: false
as_of: '2026-11-01'
updated_at: '2026-11-01T16:11:48.803754+00:00'
reviewed_at: null
coverage_release: coverage-20261101-41324509967-1
source_commit: 897a5ec8e06dcb4c9844b83dea2f5d822553ed72
financial_history_available: false
curated_research: null
financial_gap:
  reason: latest_filing_incomplete
  next_action: Resolve the latest financial filing/CompanyFacts mismatch; any historical
    bootstrap must keep the latest-period gap explicit.
  observed_forms:
  - 10-Q
  - '3'
  - '4'
  - 424B4
  - 8-A12B
  - 8-K
  - CERT
  - DRS
  - DRS/A
  - EFFECT
  - S-1
  - S-1/A
  - S-8
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0002096362.json
    sha256: bb240882e8216dddbba7ea1b78a151a78199070a856e876de07eae269a3eb83e
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0002096362.json
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
  url: https://data.sec.gov/submissions/CIK0002096362.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: bb240882e8216dddbba7ea1b78a151a78199070a856e876de07eae269a3eb83e
- id: S03
  title: S-1 0001493152-26-047623
  url: https://www.sec.gov/Archives/edgar/data/2096362/000149315226047623/0001493152-26-047623-index.html
  published_at: '2026-10-19'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 4 0001493152-26-043974
  url: https://www.sec.gov/Archives/edgar/data/2096362/000149315226043974/0001493152-26-043974-index.html
  published_at: '2026-09-23'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: DRS/A 0001493152-26-043521
  url: https://www.sec.gov/Archives/edgar/data/2096362/000149315226043521/0001493152-26-043521-index.html
  published_at: '2026-09-21'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 8-K 0001493152-26-043456
  url: https://www.sec.gov/Archives/edgar/data/2096362/000149315226043456/0001493152-26-043456-index.html
  published_at: '2026-09-21'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 4 0001493152-26-039953
  url: https://www.sec.gov/Archives/edgar/data/2096362/000149315226039953/0001493152-26-039953-index.html
  published_at: '2026-08-25'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S53
  url: https://www.sec.gov/Archives/edgar/data/2096362/000119312526352653/aiai-20260630.htm
  title: 10-Q 0001193125-26-352653
  published_at: '2026-08-14'
  retrieved_at: '2026-11-07T18:03:40.381199+00:00'
  sha256: 9a145d3f07b070bfcf3854acf02cc7c39dcce1621fe57be970e162b3b835d3cb
issuer_classification:
  cik: 0002096362
  classification_status: reported_sic
  entity_type: operating
  name: AIAI Holdings Corp
  sic: '7374'
  sic_description: Services-Computer Processing & Data Preparation
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: bb240882e8216dddbba7ea1b78a151a78199070a856e876de07eae269a3eb83e
  url: https://data.sec.gov/submissions/CIK0002096362.json
listings:
- ticker: AIAI
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001193125-26-352653
  filed: '2026-08-14'
  form: 10-Q
  period_end: '2026-06-30'
  url: https://www.sec.gov/Archives/edgar/data/2096362/000119312526352653/0001193125-26-352653-index.html
- accession: 0001493152-26-043456
  filed: '2026-09-21'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/2096362/000149315226043456/0001493152-26-043456-index.html
research_progress:
  stage: evidence_collected
  input_sha256: da8bc0f58de2419ae244f607e477dfb134694552507eb60a6fe0b06c94ccf9fe
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
  - revenue-model-and-segments
  - risks-and-thesis-breakers
  derived_observations: 0
  model_draft: false
  reviewed: false
sector_assignment:
  sector: information-technology
  method: project_sic_rule
  sic: '7374'
  sic_description: Services-Computer Processing & Data Preparation
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0002096362.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/9ce9ba7dde955e58421992481cd013c9475dbbdb/brain/companies/AIAI/README.md
full_history_commit: 9ce9ba7dde955e58421992481cd013c9475dbbdb
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# AIAI — AIAI Holdings Corp

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/9ce9ba7dde955e58421992481cd013c9475dbbdb/brain/companies/AIAI/README.md)

## Business overview

Reported issuer name: **AIAI Holdings Corp**. Stable SEC CIK: **0002096362**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| AIAI | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 10-Q, filed 2026-08-14, L251:

> the implementation of our business model and strategic plans and the timing, progress and results of our acquisition program; [S53]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 10-Q, filed 2026-08-14, L5101:

> Constellation: Constellation is a digital evidence ecosystem that provides products and services designed to create a trust-based exchange for a communications bridge. Constellation operates multiple revenue streams across hardware, software, and enterprise divisions and is advancing its mission to provide provable guarantees on the world's data through the application of its blockchain protocol to the United States military's digital infrastructure. [S53]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 10-Q, filed 2026-08-14, L248:

> This document contains forward-looking statements within the meaning of the federal securities laws. Any statements that do not relate to historical or current facts or matters are forward-looking statements. You can identify some of the forward-looking statements by the use of forward-looking words, such as “may,” “will,” “could,” “would,” “project,” “believe,” “anticipate,” “expect,” “estimate,” “continue,” “potential,” “plan,” “forecast,” and the like, or the use of future tense. Statements concerning current conditions may also be forward-looking if they imply a continuation of current conditions. Examples of forward-looking statements include, but are not limited to, statements concerning: the impact of the global macroeconomic environment, including tariffs; expectations regarding demand trends and market conditions for our services; expectations regarding our tax resolutions, effective tax rate and unrecognized tax benefits; expectations regarding the merits of our positions and plans with respect to certain litigation matters; and our beliefs regarding our capital allocation plans and the sufficiency of our available liquidity to meet our working capital, debt and capital expenditure needs. [S53]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 10-Q, filed 2026-08-14, L5146:

> Technology revenue is generated from blockchain-based enterprise data and technology solutions and associated equipment sales, digital asset rewards earned by operating validator nodes and participating in blockchain staking activities, and blockchain network licensing arrangements. Additionally, technology revenues include marketing and remarketing of printer, scanner, and copier products and subscription-based document solutions. Technology customers include both public-sector and private-sector customers, including government-related applications supporting defense and national security initiatives, as well as business-to-business and business-to-consumer commercial customers. Revenue is recognized in accordance with ASC 606 as the Company satisfies its contractual performance obligations under customer contracts. Specific revenue recognition policies with respect to our principal technology offerings are as follows: [S53]

## Industry and value chain

SEC-reported SIC **7374**: Services-Computer Processing & Data Preparation. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 10-Q, filed 2026-08-14, L269:

> disruptions to our operations or our supply chain, including damage or disruption to our operations or to those of our suppliers; [S53]

Navigation sector: **information-technology**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 10-Q, filed 2026-08-14, L10595:

> (3) Industry Agnostic AI Platform: A significant reason we believe we will have an accelerated platform is technical in nature. The AI technology we are licensing from M42 is supported by over one billion lines of code and configuration, industry specific and non-industry specific APIs and extremely advanced mathematics and science. As a result, our platform does not require traditional data cleansing, data extraction, data transformation, and data loading “extract transform load” (ETL) processes. We can leave the data in its data silo rather than “normalizing” disparate data types, and going through a centralized ETL process, we can “loosely associate” unstructured or structured disparate data silos and analyze them in place. This approach enables us to process very large data volumes and deliver insights significantly faster than traditional solutions, which often remain constrained by extended periods of data cleansing and normalization efforts. This capability allows us to access portfolio companies’ data and business applications and deliver AI-enabled insights within days or weeks while our competitors continue to spend extended periods manually cleansing, normalizing, integrating and extracting data. [S53]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 10-Q, filed 2026-08-14, L10592:

> Our anticipated accelerated timeline of four to six months for the implementation of our AI technology, compared to our perceived industry standard of 24-36 months, represents a significant competitive advantage and drives our financial performance. This accelerated time frame for the implementation of our AI should enable faster revenue recognition from technology services while allowing more rapid realization of operational improvements in acquired companies. There are several reasons why we believe our implementation process will occur more rapidly than traditional software implementations: [S53]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 10-Q, filed 2026-08-14, L10611:

> AIAI is a diversified holding company operating through subsidiaries across the construction, healthcare and technology sectors. On May 6, 2026, concurrently with the effectiveness of AIAI's Registration Statement, we completed the Acquisitions and began operating as an integrated platform of businesses. Our strategy is to enhance the operating performance our subsidiaries through the implementation of licensed artificial intelligence technology, operational improvements, and strategic acquisitions that complement and expand its platform. [S53]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 10-Q, filed 2026-08-14, L9326:

> The Company accounts for share‑based compensation in accordance with ASC 718, Compensation – Stock Compensation, which requires measurement of compensation cost at the grant‑date fair value of equity awards and recognition of expense over the requisite service period. AIAI's 2026 Equity Incentive Plan (the “2026 Plan”) was adopted by the Board of Directors in January 2026 and approved by stockholders, becoming effective at the Closing Date. The 2026 Plan authorizes the grant of stock options and other equity-based awards to employees, directors, and consultants. [S53]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 10-Q, filed 2026-08-14, L289:

> the other factors set forth under “Risk Factors” in our Registration Statement on Form S-1/A (File No. 333-292963), as filed with the Securities and Exchange Commission on May 1, 2026. [S53]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Resolve the latest financial filing/CompanyFacts mismatch; any historical bootstrap must keep the latest-period gap explicit.
- Forms observed in the retained filing inventory: 10-Q, 3, 4, 424B4, 8-A12B, 8-K, CERT, DRS, DRS/A, EFFECT, S-1, S-1/A, S-8
- Collector status: quality_review_required; last action: filings_only_financials_incomplete; last checked: 2026-10-24T13:36:41.367734+00:00.

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
- **Recent developments** (evidence or analysis still needed): Keep a dated, source-backed log of material changes. Distinguish the event date from the article date and explain what changed in the profile.

Calculation gaps: Validated financial history is missing.

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest five available filing metadata records; document bodies have not been analyzed here.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-10-19 | S-1 | 0001493152-26-047623 | — | [S03] |
| 2026-09-23 | 4 | 0001493152-26-043974 | — | [S04] |
| 2026-09-21 | DRS/A | 0001493152-26-043521 | — | [S05] |
| 2026-09-21 | 8-K | 0001493152-26-043456 | — | [S06] |
| 2026-08-25 | 4 | 0001493152-26-039953 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-11-01T16:07:03.070084+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0002096362.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [S-1 0001493152-26-047623](https://www.sec.gov/Archives/edgar/data/2096362/000149315226047623/0001493152-26-047623-index.html) — published 2026-10-19; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [4 0001493152-26-043974](https://www.sec.gov/Archives/edgar/data/2096362/000149315226043974/0001493152-26-043974-index.html) — published 2026-09-23; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [DRS/A 0001493152-26-043521](https://www.sec.gov/Archives/edgar/data/2096362/000149315226043521/0001493152-26-043521-index.html) — published 2026-09-21; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [8-K 0001493152-26-043456](https://www.sec.gov/Archives/edgar/data/2096362/000149315226043456/0001493152-26-043456-index.html) — published 2026-09-21; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [4 0001493152-26-039953](https://www.sec.gov/Archives/edgar/data/2096362/000149315226039953/0001493152-26-039953-index.html) — published 2026-08-25; retrieved 2026-10-23T08:33:02.691743+00:00.

[S53] [10-Q 0001193125-26-352653](https://www.sec.gov/Archives/edgar/data/2096362/000119312526352653/aiai-20260630.htm) — published 2026-08-14; retrieved 2026-11-07T18:03:40.381199+00:00.

Source release: `coverage-20261101-41324509967-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/9ce9ba7dde955e58421992481cd013c9475dbbdb/brain/companies/AIAI/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
