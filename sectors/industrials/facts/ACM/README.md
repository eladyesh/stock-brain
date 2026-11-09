---
schema_version: 1
document_type: company_facts
company_id: company-cik-0000868857
cik: 0000868857
company_name: AECOM
tickers:
- ACM
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
  reason: latest_filing_incomplete
  next_action: Resolve the latest financial filing/CompanyFacts mismatch; any historical
    bootstrap must keep the latest-period gap explicit.
  observed_forms:
  - 10-K
  - 10-K/A
  - 10-Q
  - 11-K
  - '144'
  - '3'
  - 3/A
  - '4'
  - 4/A
  - 424B3
  - '425'
  - '5'
  - 8-K
  - ARS
  - CORRESP
  - D
  - DEF 14A
  - DEFA14A
  - DEFR14A
  - EFFECT
  - NO ACT
  - PRE 14A
  - PX14A6G
  - S-4
  - S-4/A
  - S-8
  - S-8 POS
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13D/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - SD
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0000868857.json
    sha256: dc291dcfb0d0df3e402d58f50cf58b622c32c666d685110ed2c33ee818e370a2
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0000868857.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
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
  url: https://data.sec.gov/submissions/CIK0000868857.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: dc291dcfb0d0df3e402d58f50cf58b622c32c666d685110ed2c33ee818e370a2
- id: S03
  title: 3 0002157490-26-000002
  url: https://www.sec.gov/Archives/edgar/data/868857/000215749026000002/0002157490-26-000002-index.html
  published_at: '2026-10-08'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 8-K 0001104659-26-108415
  url: https://www.sec.gov/Archives/edgar/data/868857/000110465926108415/0001104659-26-108415-index.html
  published_at: '2026-09-17'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 8-K 0001104659-26-108255
  url: https://www.sec.gov/Archives/edgar/data/868857/000110465926108255/0001104659-26-108255-index.html
  published_at: '2026-09-16'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: SCHEDULE 13D/A 0001104659-26-094873
  url: https://www.sec.gov/Archives/edgar/data/868857/000110465926094873/0001104659-26-094873-index.html
  published_at: '2026-08-12'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 10-Q 0000868857-26-000021
  url: https://www.sec.gov/Archives/edgar/data/868857/000086885726000021/0000868857-26-000021-index.html
  published_at: '2026-08-11'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S54
  url: https://www.sec.gov/Archives/edgar/data/868857/000086885726000021/acm-20260703.htm
  title: 10-Q 0000868857-26-000021
  published_at: '2026-08-11'
  retrieved_at: '2026-11-03T20:02:32.667265+00:00'
  sha256: a00977c3479116914221c73dc1cbe69ce6f2c6e4c555672710eeca7481bcb5cd
- id: S55
  url: https://www.sec.gov/Archives/edgar/data/868857/000086885726000006/acm-20260119.htm
  title: DEF 14A 0000868857-26-000006
  published_at: '2026-01-20'
  retrieved_at: '2026-11-03T20:02:30.805252+00:00'
  sha256: aa77aa11e40a55be8cb52fe853c5649b365a577adadceaaf6b3750664aaad968
- id: S56
  url: https://www.sec.gov/Archives/edgar/data/868857/000086885725000013/acm-20250930.htm
  title: 10-K 0000868857-25-000013
  published_at: '2025-11-19'
  retrieved_at: '2026-11-03T20:02:28.912558+00:00'
  sha256: 96aac66856dfa7194628c5e46d936e99fe345c5a0289b3c5bdb9e7e5762a985d
issuer_classification:
  cik: 0000868857
  classification_status: reported_sic
  entity_type: operating
  name: AECOM
  sic: '8711'
  sic_description: Services-Engineering Services
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: dc291dcfb0d0df3e402d58f50cf58b622c32c666d685110ed2c33ee818e370a2
  url: https://data.sec.gov/submissions/CIK0000868857.json
listings:
- ticker: ACM
  exchange: NYSE
  instrument_type: common_stock
research_filings:
- accession: 0000868857-25-000013
  filed: '2025-11-19'
  form: 10-K
  period_end: '2025-09-30'
  url: https://www.sec.gov/Archives/edgar/data/868857/000086885725000013/0000868857-25-000013-index.html
- accession: 0000868857-26-000021
  filed: '2026-08-11'
  form: 10-Q
  period_end: '2026-07-03'
  url: https://www.sec.gov/Archives/edgar/data/868857/000086885726000021/0000868857-26-000021-index.html
- accession: 0000868857-26-000006
  filed: '2026-01-20'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/868857/000086885726000006/0000868857-26-000006-index.html
- accession: 0001104659-26-108415
  filed: '2026-09-17'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/868857/000110465926108415/0001104659-26-108415-index.html
research_progress:
  stage: evidence_collected
  input_sha256: 5f7b0664dd2bd2c51e3dfbbbf235c306fc5e55c9a8a8a0a24fd72ad1be5b7a58
  last_attempt_at: '2026-11-03T19:57:53.299416+00:00'
  last_success_at: '2026-11-03T19:57:53.299416+00:00'
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
  sic: '8711'
  sic_description: Services-Engineering Services
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0000868857.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/2a475d5f7d7de42ae2b318e51e43cda99027f72f/brain/companies/ACM/README.md
full_history_commit: 2a475d5f7d7de42ae2b318e51e43cda99027f72f
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# ACM — AECOM

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/2a475d5f7d7de42ae2b318e51e43cda99027f72f/brain/companies/ACM/README.md)

## Business overview

Reported issuer name: **AECOM**. Stable SEC CIK: **0000868857**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| ACM | NYSE | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 10-Q, filed 2026-08-11, L939:

> significantly impact how our business activities are taxed. These proposed changes could have a material impact on the Company’s income tax expense and deferred tax balances. [S54]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 10-Q, filed 2026-08-11, L582:

> The changes in the carrying value of goodwill by reportable segment for the nine months ended June 30, 2026 were as follows: [S54]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 10-Q, filed 2026-08-11, L1201:

> Our revenue is dependent on our ability to attract and retain qualified and productive employees, identify business opportunities, allocate our labor resources and capital to profitable and high growth markets, secure new contracts, and renew existing client agreements. Demand for our services may be vulnerable to sudden economic downturns and reductions in government and private industry spending, which may result in clients delaying, curtailing or canceling proposed and existing projects. Moreover, as a professional services company, maintaining the high quality of the work generated by our employees is integral to our revenue generation and profitability. Given the global nature of our business, our revenue is exposed to currency rate fluctuations that could change from period to period and year to year. [S54]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 10-Q, filed 2026-08-11, L1193:

> We are a leading global provider of professional infrastructure consulting and advisory services for governments, businesses and organizations throughout the world. We provide advisory, planning, consulting, architectural and engineering design, construction and program management services, and investment and development services to public and private clients worldwide in major end markets such as transportation, facilities, water, environmental, and energy. [S54]

## Industry and value chain

SEC-reported SIC **8711**: Services-Engineering Services. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 10-K, filed 2025-11-19, L355:

> We purchase most of the raw materials and components necessary to operate our business from numerous sources. However, the price and availability of raw materials and components may vary from year to year due to customer demand, production capacity, market conditions, and material shortages. While we do not currently foresee the lack of availability of any particular raw materials in the near term, prolonged unavailability of raw materials necessary to our projects and services or significant price increases for those raw materials could have a material adverse effect on our business in the near term. [S56]

Navigation sector: **industrials**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 10-K, filed 2025-11-19, L338:

> The markets we serve are highly fragmented and we compete with a large number of regional, national and international companies. We have numerous competitors, ranging from small private firms to multi-billion dollar companies, some of which have greater financial resources or that are more specialized and concentrate their resources in particular areas of expertise. The extent of our competition varies according to the particular markets and geographic area. The degree and type of competition we face is also influenced by the type and scope of a particular project. The technical and professional aspects of our services generally do not require large upfront capital expenditures and, therefore, provide limited barriers against new competitors. [S56]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 10-Q, filed 2026-08-11, L581:

> The Company completed two business acquisitions during the year ended September 30, 2025 for total consideration of $375.9 million, which included stock consideration of $146.4 million. Neither of these two acquisitions met the quantitative thresholds to require separate disclosure. The Company acquired these businesses to expand its competitive advantage and compound strengths to achieve its long-term profitability targets. The Company preliminarily estimates the amount of identifiable assets as soon as information is available, but not more than 12 months from the date of acquisition. The initial accounting for these acquisitions is not complete as of June 30, 2026 as the Company continues to assess the value of the tax liabilities and the acquired intellectual property, including digital assets. [S54]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — DEF 14A, filed 2026-01-20, L2533:

> record net service revenue, margins and earnings. As a result of our strategy and successes in gaining market share, [S55]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 10-Q, filed 2026-08-11, L1041:

> Other accrued expenses includes primarily accrued dividends payable, current operating lease liabilities noted in Note 12, and accrued VAT taxes of $63.4 million and $62.5 million as of June 30, 2026 and September 30, 2025, respectively. On June 3, 2026, the Company’s Board of Directors declared a quarterly cash dividend of $0.31 per share, which was paid on July 17, 2026 to stockholders of record as of the close of business on July 1, 2026. As of June 30, 2026, accrued and unpaid dividends totaled $42.5 million. [S54]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 10-Q, filed 2026-08-11, L1191:

> All subsequent written and oral forward-looking statements concerning the Company or other matters attributable to the Company or any person acting on its behalf are expressly qualified in their entirety by the cautionary statements above. You are cautioned not to place undue reliance on these forward-looking statements, which speak only to the date they are made. The Company is under no obligation (and expressly disclaims any such obligation) to update or revise any forward-looking statement that may be made from time to time, whether as a result of new information, future developments or otherwise. Please review “Part II, Item 1A—Risk Factors” in this Quarterly Report for a discussion of the factors, risks and uncertainties that could affect our future results. [S54]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Resolve the latest financial filing/CompanyFacts mismatch; any historical bootstrap must keep the latest-period gap explicit.
- Forms observed in the retained filing inventory: 10-K, 10-K/A, 10-Q, 11-K, 144, 3, 3/A, 4, 4/A, 424B3, 425, 5, 8-K, ARS, CORRESP, D, DEF 14A, DEFA14A, DEFR14A, EFFECT, NO ACT, PRE 14A, PX14A6G, S-4, S-4/A, S-8, S-8 POS, SC 13D, SC 13D/A, SC 13G, SC 13G/A, SCHEDULE 13D/A, SCHEDULE 13G, SCHEDULE 13G/A, SD, UPLOAD
- Collector status: quality_review_required; last action: filings_only_financials_incomplete; last checked: 2026-10-24T13:29:47.805591+00:00.

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
| 2026-10-08 | 3 | 0002157490-26-000002 | — | [S03] |
| 2026-09-17 | 8-K | 0001104659-26-108415 | — | [S04] |
| 2026-09-16 | 8-K | 0001104659-26-108255 | — | [S05] |
| 2026-08-12 | SCHEDULE 13D/A | 0001104659-26-094873 | — | [S06] |
| 2026-08-11 | 10-Q | 0000868857-26-000021 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-11-01T16:07:03.340031+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0000868857.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [3 0002157490-26-000002](https://www.sec.gov/Archives/edgar/data/868857/000215749026000002/0002157490-26-000002-index.html) — published 2026-10-08; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [8-K 0001104659-26-108415](https://www.sec.gov/Archives/edgar/data/868857/000110465926108415/0001104659-26-108415-index.html) — published 2026-09-17; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [8-K 0001104659-26-108255](https://www.sec.gov/Archives/edgar/data/868857/000110465926108255/0001104659-26-108255-index.html) — published 2026-09-16; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [SCHEDULE 13D/A 0001104659-26-094873](https://www.sec.gov/Archives/edgar/data/868857/000110465926094873/0001104659-26-094873-index.html) — published 2026-08-12; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [10-Q 0000868857-26-000021](https://www.sec.gov/Archives/edgar/data/868857/000086885726000021/0000868857-26-000021-index.html) — published 2026-08-11; retrieved 2026-10-23T08:33:02.691743+00:00.

[S54] [10-Q 0000868857-26-000021](https://www.sec.gov/Archives/edgar/data/868857/000086885726000021/acm-20260703.htm) — published 2026-08-11; retrieved 2026-11-03T20:02:32.667265+00:00.

[S55] [DEF 14A 0000868857-26-000006](https://www.sec.gov/Archives/edgar/data/868857/000086885726000006/acm-20260119.htm) — published 2026-01-20; retrieved 2026-11-03T20:02:30.805252+00:00.

[S56] [10-K 0000868857-25-000013](https://www.sec.gov/Archives/edgar/data/868857/000086885725000013/acm-20250930.htm) — published 2025-11-19; retrieved 2026-11-03T20:02:28.912558+00:00.

Source release: `coverage-20261101-41324509967-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/2a475d5f7d7de42ae2b318e51e43cda99027f72f/brain/companies/ACM/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
