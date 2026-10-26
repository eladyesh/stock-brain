---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001737927
cik: 0001737927
company_name: Canopy Growth Corp
tickers:
- CGC
status: stub
canonical_reviewed: false
as_of: '2026-10-26'
updated_at: '2026-10-26T16:16:21.148680+00:00'
reviewed_at: null
coverage_release: coverage-20261026-40356450615-1
source_commit: ffd7836f4c177b9a174b16eab4288980decb7e24
financial_history_available: false
curated_research: null
financial_gap:
  reason: latest_filing_incomplete
  next_action: Resolve the latest financial filing/CompanyFacts mismatch; any historical
    bootstrap must keep the latest-period gap explicit.
  observed_forms:
  - 10-K
  - 10-K/A
  - 10-Q
  - '25'
  - 25/A
  - '3'
  - 3/A
  - '4'
  - 4/A
  - 40-F
  - 40FR12B
  - 424B3
  - 424B5
  - 424B7
  - 6-K
  - 6-K/A
  - 8-A12B
  - 8-A12B/A
  - 8-K
  - 8-K/A
  - ARS
  - CERT
  - CORRESP
  - DEF 14A
  - DEFA14A
  - EFFECT
  - F-X
  - NT 10-K
  - NT 10-K/A
  - POS AM
  - POSASR
  - PRE 14A
  - PRER14A
  - S-1
  - S-3
  - S-3ASR
  - S-8
  - SC 13D
  - SC 13D/A
  - SC TO-I
  - SC TO-I/A
  - SD
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001737927.json
    sha256: 77a3f45a263560452b1ca7c032e6a7518e6307d8785e7389d665d7ddbaca02a5
    retrieved_at: '2026-10-24T13:22:51.759433+00:00'
    archive: &id001
      member: CIK0001737927.json
      sha256: 593fbbea6512ef5ec729a5e513c465fbedaac8a66602c0abe00d0ba5a4d18732
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: nasdaqlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt
  published_at: null
  retrieved_at: '2026-10-26T16:11:31.228419+00:00'
  sha256: 74146fcda2f9b3b43b06280df0ad9584dffa78b2237460917eda3c2892e7a706
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001737927.json
  published_at: null
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 77a3f45a263560452b1ca7c032e6a7518e6307d8785e7389d665d7ddbaca02a5
- id: S03
  title: 8-K 0001104659-26-118521
  url: https://www.sec.gov/Archives/edgar/data/1737927/000110465926118521/0001104659-26-118521-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S04
  title: DEFA14A 0001104659-26-116641
  url: https://www.sec.gov/Archives/edgar/data/1737927/000110465926116641/0001104659-26-116641-index.html
  published_at: '2026-10-16'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S05
  title: 8-K 0001104659-26-116639
  url: https://www.sec.gov/Archives/edgar/data/1737927/000110465926116639/0001104659-26-116639-index.html
  published_at: '2026-10-16'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S06
  title: DEFA14A 0001104659-26-114053
  url: https://www.sec.gov/Archives/edgar/data/1737927/000110465926114053/0001104659-26-114053-index.html
  published_at: '2026-10-06'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S07
  title: 4 0001104659-26-112364
  url: https://www.sec.gov/Archives/edgar/data/1737927/000110465926112364/0001104659-26-112364-index.html
  published_at: '2026-09-30'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S53
  url: https://www.sec.gov/Archives/edgar/data/1737927/000110465926118521/tm2627754d1_8k.htm
  title: 8-K 0001104659-26-118521
  published_at: '2026-10-23'
  retrieved_at: '2026-10-25T14:04:52.208324+00:00'
  sha256: 932175b353c77532572a94e39690beafcfa8ab111b0e19342408dbd323567329
- id: S54
  url: https://www.sec.gov/Archives/edgar/data/1737927/000110465926092759/tm2620644-3_def14a.htm
  title: DEF 14A 0001104659-26-092759
  published_at: '2026-08-07'
  retrieved_at: '2026-10-25T14:04:48.711904+00:00'
  sha256: 12366eca6931b30424ff7d58bd1ea401230f2b486cea3019b81f89a858615db8
- id: S55
  url: https://www.sec.gov/Archives/edgar/data/1737927/000119312526339076/cgc-20260630.htm
  title: 10-Q 0001193125-26-339076
  published_at: '2026-08-07'
  retrieved_at: '2026-10-25T14:04:50.518156+00:00'
  sha256: 6d5e7e09a86cc29f3854bb6885bf40d5afbf14d5463f733cd961686222e19ae4
- id: S56
  url: https://www.sec.gov/Archives/edgar/data/1737927/000119312526270260/cgc-20260331.htm
  title: 10-K 0001193125-26-270260
  published_at: '2026-06-15'
  retrieved_at: '2026-10-25T14:04:45.735571+00:00'
  sha256: 1915590b877672eec6cef5a23642fb113ce7edaaecbcfe8e04e836df0372c0af
issuer_classification:
  cik: 0001737927
  classification_status: reported_sic
  entity_type: operating
  name: Canopy Growth Corp
  sic: '2833'
  sic_description: Medicinal Chemicals & Botanical Products
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 77a3f45a263560452b1ca7c032e6a7518e6307d8785e7389d665d7ddbaca02a5
  url: https://data.sec.gov/submissions/CIK0001737927.json
listings:
- ticker: CGC
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001193125-26-270260
  filed: '2026-06-15'
  form: 10-K
  period_end: '2026-03-31'
  url: https://www.sec.gov/Archives/edgar/data/1737927/000119312526270260/0001193125-26-270260-index.html
- accession: 0001193125-26-339076
  filed: '2026-08-07'
  form: 10-Q
  period_end: '2026-06-30'
  url: https://www.sec.gov/Archives/edgar/data/1737927/000119312526339076/0001193125-26-339076-index.html
- accession: 0001104659-26-092759
  filed: '2026-08-07'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/1737927/000110465926092759/0001104659-26-092759-index.html
- accession: 0001104659-26-118521
  filed: '2026-10-23'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/1737927/000110465926118521/0001104659-26-118521-index.html
- accession: 0001193125-23-082330
  filed: '2023-03-28'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1737927/000119312523082330/0001193125-23-082330-index.html
- accession: 0001564590-22-028256
  filed: '2022-08-08'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1737927/000156459022028256/0001564590-22-028256-index.html
research_progress:
  stage: evidence_collected
  input_sha256: 06d2eebfb1927d6d18195ddb0f55f5e047fe52e304df3662757734b0d81f898f
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
  sector: health-care
  method: project_sic_rule
  sic: '2833'
  sic_description: Medicinal Chemicals & Botanical Products
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001737927.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/6ec0c5a139b27efe3be9111dc20cf938bd839c1e/brain/companies/CGC/README.md
full_history_commit: 6ec0c5a139b27efe3be9111dc20cf938bd839c1e
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# CGC — Canopy Growth Corp

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/6ec0c5a139b27efe3be9111dc20cf938bd839c1e/brain/companies/CGC/README.md)

## Business overview

Reported issuer name: **Canopy Growth Corp**. Stable SEC CIK: **0001737927**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| CGC | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — DEF 14A, filed 2026-08-07, L57:

> This proxy statement contains proposals to be voted on at the Meeting and other information about Canopy Growth Corporation (the “Company,” “Canopy Growth” “our” or “we”) and our corporate governance practices. Below we provide a brief summary of certain information contained in this proxy statement. The summary does not contain all of the information you should consider. Please read the entire proxy statement carefully before voting. [S54]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 10-Q, filed 2026-08-07, L5900:

> These segments reflect how the Company’s operations are managed, how the Company’s Chief Executive Officer, who is the Chief Operating Decision Maker (“CODM”), allocates resources and evaluates performance, and how the Company’s internal management financial reporting is structured. The Company’s CODM evaluates the performance of these segments, with a focus on (i) segment net revenue, and (ii) segment gross margin as the measure of segment profit or loss. Accordingly, information regarding segment net revenue and segment gross margin for the comparative periods has been restated to reflect the aforementioned change in reportable segments. [S55]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — DEF 14A, filed 2026-08-07, L1799:

> Through its onboarding program, new directors are given the opportunity to meet with members of management to review the budget, forecast and strategic plan for the Company, as well as key corporate projects. When circumstances permit, a new director shall participate in a site tour of the Company’s operating facilities and of the retail stores carrying our products and receive an overview of the past year of activities, the competitive landscape and insight into distribution channels. [S54]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 10-K, filed 2026-06-15, L1097:

> We depend on fast and efficient courier services to distribute our products to our customers. Any prolonged disruption of this courier service could have a material adverse effect on our business, financial condition, results of operations and growth prospects. Rising costs associated with the courier services that we use to ship our products may also adversely affect our business and our ability to operate profitably. [S56]

## Industry and value chain

SEC-reported SIC **2833**: Medicinal Chemicals & Botanical Products. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — DEF 14A, filed 2026-08-07, L1151:

> Luc Mongeau is the Chief Executive Officer (“CEO”) of Canopy Growth and also serves on the Board. Mr. Mongeau is a seasoned executive with over 25 years of experience spearheading consumer goods companies throughout North America, including Weston Foods and Mars Petcare. Mr. Mongeau is an established leader with demonstrated expertise in marketing, sales, supply chain operations, and mergers and acquisitions. Prior to Canopy Growth, from September 2022 to January 2025, Mr. Mongeau was the CEO of eSolutions Furniture Inc., formerly Bestar-Bush, where he led the transformation of the business to deepen its share of the digital commerce furniture industry. This included reconfiguring the North American manufacturing network and enhancing the company’s global supply chain. From September 2017 to March 2022, during Mr. Mongeau’s tenure as President of Weston Foods, he spearheaded the strategic realignment and end-to-end operational leadership of the North American bakery, overseeing a team of over 6,000 employees across 40 facilities. He also directed the development of commercial strategies across branded and private label categories for major North American retailers and managed the sale of Weston Foods. Prior to this, in his role as President of Mars Petcare North America, Mr. Mongeau provided strategic and operational leadership to the North American organization with more than … [S54]

Navigation sector: **health-care**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — DEF 14A, filed 2026-08-07, L3685:

> With the engagement of our executive compensation consultant Mercer, the CGCN Committee re-evaluated Canopy Growth’s publicly-traded peer group in Fiscal 2023. We believe this peer group, with the adjustments noted below, reflects the current reality of Canopy Growth and the cannabis industry and the companies we compete with for talent. [S54]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — DEF 14A, filed 2026-08-07, L1525:

> Prior to joining Canopy Growth, Dr. Gedeon served in a number of senior leadership roles including Chief Legal Officer and Corporate Secretary at Aphria, Inc. from July 2018 to August 2021 and Chief Legal Officer of The Metals Company, a deep-sea mining company, from August 2021 to August 2022. Prior to joining Aphria, Dr. Gedeon was a Partner at Fasken Martineau DuMoulin LLP, a leading Canadian law firm. Through these roles, she developed extensive experience in the cannabis industry and in the management of complex regulatory structures, intellectual property management, corporate governance, government relations, and strategic acquisitions, all capabilities that are critical to advancing Canopy Growth’s strategy for North American leadership. [S54]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — DEF 14A, filed 2026-08-07, L2620:

> MTL is known for its cultivation expertise and high quality flower, and the additional production capacity is expected to support the Company’s growth strategy both in Canada and internationally. [S54]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 8-K, filed 2026-10-23, L115:

> the board of directors of Canopy Growth (the “Board”) or any responsible committee thereof to fix their remuneration [S53]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — DEF 14A, filed 2026-08-07, L1616:

> The Board oversees the management of risks inherent in the operation of our business, with a focus on the most significant risks that we face. The Board performs this role primarily through its Audit Committee and CGCN Committee. Each Board committee addresses the risks specific to the function of that committee. For example, the Board committees address the following risks: [S54]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Resolve the latest financial filing/CompanyFacts mismatch; any historical bootstrap must keep the latest-period gap explicit.
- Forms observed in the retained filing inventory: 10-K, 10-K/A, 10-Q, 25, 25/A, 3, 3/A, 4, 4/A, 40-F, 40FR12B, 424B3, 424B5, 424B7, 6-K, 6-K/A, 8-A12B, 8-A12B/A, 8-K, 8-K/A, ARS, CERT, CORRESP, DEF 14A, DEFA14A, EFFECT, F-X, NT 10-K, NT 10-K/A, POS AM, POSASR, PRE 14A, PRER14A, S-1, S-3, S-3ASR, S-8, SC 13D, SC 13D/A, SC TO-I, SC TO-I/A, SD, UPLOAD
- Collector status: quality_review_required; last action: filings_only_financials_incomplete; last checked: 2026-10-24T13:35:21.196256+00:00.

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
| 2026-10-23 | 8-K | 0001104659-26-118521 | — | [S03] |
| 2026-10-16 | DEFA14A | 0001104659-26-116641 | — | [S04] |
| 2026-10-16 | 8-K | 0001104659-26-116639 | — | [S05] |
| 2026-10-06 | DEFA14A | 0001104659-26-114053 | — | [S06] |
| 2026-09-30 | 4 | 0001104659-26-112364 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-26T16:11:31.228419+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001737927.json) — published not supplied; retrieved 2026-10-24T13:22:51.759433+00:00.

[S03] [8-K 0001104659-26-118521](https://www.sec.gov/Archives/edgar/data/1737927/000110465926118521/0001104659-26-118521-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S04] [DEFA14A 0001104659-26-116641](https://www.sec.gov/Archives/edgar/data/1737927/000110465926116641/0001104659-26-116641-index.html) — published 2026-10-16; retrieved 2026-10-24T13:22:51.759433+00:00.

[S05] [8-K 0001104659-26-116639](https://www.sec.gov/Archives/edgar/data/1737927/000110465926116639/0001104659-26-116639-index.html) — published 2026-10-16; retrieved 2026-10-24T13:22:51.759433+00:00.

[S06] [DEFA14A 0001104659-26-114053](https://www.sec.gov/Archives/edgar/data/1737927/000110465926114053/0001104659-26-114053-index.html) — published 2026-10-06; retrieved 2026-10-24T13:22:51.759433+00:00.

[S07] [4 0001104659-26-112364](https://www.sec.gov/Archives/edgar/data/1737927/000110465926112364/0001104659-26-112364-index.html) — published 2026-09-30; retrieved 2026-10-24T13:22:51.759433+00:00.

[S53] [8-K 0001104659-26-118521](https://www.sec.gov/Archives/edgar/data/1737927/000110465926118521/tm2627754d1_8k.htm) — published 2026-10-23; retrieved 2026-10-25T14:04:52.208324+00:00.

[S54] [DEF 14A 0001104659-26-092759](https://www.sec.gov/Archives/edgar/data/1737927/000110465926092759/tm2620644-3_def14a.htm) — published 2026-08-07; retrieved 2026-10-25T14:04:48.711904+00:00.

[S55] [10-Q 0001193125-26-339076](https://www.sec.gov/Archives/edgar/data/1737927/000119312526339076/cgc-20260630.htm) — published 2026-08-07; retrieved 2026-10-25T14:04:50.518156+00:00.

[S56] [10-K 0001193125-26-270260](https://www.sec.gov/Archives/edgar/data/1737927/000119312526270260/cgc-20260331.htm) — published 2026-06-15; retrieved 2026-10-25T14:04:45.735571+00:00.

Source release: `coverage-20261026-40356450615-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/6ec0c5a139b27efe3be9111dc20cf938bd839c1e/brain/companies/CGC/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
