---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001577552
cik: '0001577552'
company_name: Alibaba Group Holding Ltd
tickers:
- BABA
status: stub
canonical_reviewed: false
as_of: '2026-11-01'
updated_at: '2026-11-01T16:11:48.803754+00:00'
reviewed_at: null
coverage_release: coverage-20261101-41324509967-1
source_commit: 107777182f87f961989f84e51ee16bb872074fdf
financial_history_available: false
curated_research: null
financial_gap:
  reason: foreign_reporting_adapter
  next_action: Add support for the observed 20-F, 40-F or 6-K reporting forms and
    verify the actual accounting taxonomy before normalization.
  observed_forms:
  - 13F-HR
  - '144'
  - 20-F
  - 20-F/A
  - '3'
  - '4'
  - 424B2
  - 424B3
  - 424B4
  - 424B5
  - 6-K
  - 8-A12B
  - CERTNYS
  - CORRESP
  - CT ORDER
  - DRS
  - EFFECT
  - F-1
  - F-1/A
  - F-3ASR
  - F-4
  - F-4/A
  - F-6
  - F-6EF
  - FWP
  - IRANNOTICE
  - N-PX
  - S-8
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13D/A
  - SCHEDULE 13G/A
  - SD
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001577552.json
    sha256: 6ac9ebe730af8c2646bb69e3241bff37356192d0afa18c7849e4e605844ff918
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001577552.json
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
  url: https://data.sec.gov/submissions/CIK0001577552.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 6ac9ebe730af8c2646bb69e3241bff37356192d0afa18c7849e4e605844ff918
- id: S03
  title: S-8 0001104659-26-115478
  url: https://www.sec.gov/Archives/edgar/data/1577552/000110465926115478/0001104659-26-115478-index.html
  published_at: '2026-10-13'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 6-K 0001104659-26-114191
  url: https://www.sec.gov/Archives/edgar/data/1577552/000110465926114191/0001104659-26-114191-index.html
  published_at: '2026-10-07'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 4 0001193125-26-413036
  url: https://www.sec.gov/Archives/edgar/data/1577552/000119312526413036/0001193125-26-413036-index.html
  published_at: '2026-10-05'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 4 0001193125-26-413032
  url: https://www.sec.gov/Archives/edgar/data/1577552/000119312526413032/0001193125-26-413032-index.html
  published_at: '2026-10-05'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 4 0001193125-26-411206
  url: https://www.sec.gov/Archives/edgar/data/1577552/000119312526411206/0001193125-26-411206-index.html
  published_at: '2026-10-02'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S54
  url: https://www.sec.gov/Archives/edgar/data/1577552/000119312526231755/baba-20260331.htm
  title: 20-F 0001193125-26-231755
  published_at: '2026-05-20'
  retrieved_at: '2026-11-19T21:11:10.142841+00:00'
  sha256: 6e34845baa0e03f3563cfc4de65a1feefae29216f4f03b8b6572bb158b486c20
issuer_classification:
  cik: '0001577552'
  classification_status: reported_sic
  entity_type: other
  name: Alibaba Group Holding Ltd
  sic: '7389'
  sic_description: Services-Business Services, NEC
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 6ac9ebe730af8c2646bb69e3241bff37356192d0afa18c7849e4e605844ff918
  url: https://data.sec.gov/submissions/CIK0001577552.json
listings:
- ticker: BABA
  exchange: NYSE
  instrument_type: depositary_receipt
research_filings:
- accession: 0001193125-26-231755
  filed: '2026-05-20'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1577552/000119312526231755/0001193125-26-231755-index.html
- accession: 0001193125-24-044480
  filed: '2024-02-23'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1577552/000119312524044480/0001193125-24-044480-index.html
- accession: 0001104659-26-114191
  filed: '2026-10-07'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1577552/000110465926114191/0001104659-26-114191-index.html
research_progress:
  stage: evidence_collected
  input_sha256: 12d51ca5f0d214683347506eb60e232000d86291e2a0a7b389fde921bc1c727b
  last_attempt_at: '2026-11-19T21:08:42.711300+00:00'
  last_success_at: '2026-11-19T21:08:42.711300+00:00'
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
  sic: '7389'
  sic_description: Services-Business Services, NEC
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001577552.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/0f49b319f95dcee8e757e592a38a028a04a7bc3c/brain/companies/BABA/README.md
full_history_commit: 0f49b319f95dcee8e757e592a38a028a04a7bc3c
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# BABA — Alibaba Group Holding Ltd

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/0f49b319f95dcee8e757e592a38a028a04a7bc3c/brain/companies/BABA/README.md)

## Business overview

Reported issuer name: **Alibaba Group Holding Ltd**. Stable SEC CIK: **0001577552**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| BABA | NYSE | depositary_receipt | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 20-F, filed 2026-05-20, L586:

> trends and competition in commerce and cloud computing and the other industries in which we operate, both in China and globally, as well as trends in technology innovation, research and development and application, including AI technologies; [S54]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 20-F, filed 2026-05-20, L23676:

> Operating segments are reported in a manner consistent with the internal reporting provided to the chief operating decision maker (the “CODM”), which is comprised of the Company’s Chief Executive Officer and Chief Financial Officer. When the Company changes the structure of its internal organization in a manner that causes the composition of its reportable segments to change, the corresponding information for earlier periods would be recast unless it is impracticable to do so. [S54]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 20-F, filed 2026-05-20, L5013:

> Malicious actors may also target our AI infrastructure through cyber-attacks, potentially compromising our system integrity, gaining access to our proprietary technology and information hosted on our systems, and causing service disruptions, which could undermine trust in our AI product offerings and materially and adversely affect our business operations and financial [S54]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 20-F, filed 2026-05-20, L351:

> Growth is the constant theme at Alibaba. We are committed to technology innovation and incorporating leading-edge technology into our core businesses to create value for our customers and, ultimately, for our shareholders. To prevail in an intensely competitive environment, Alibaba must maintain our growth mindset – embracing change, investing patiently in our capabilities, and securing our future through long-term thinking. This is who we are. [S54]

## Industry and value chain

SEC-reported SIC **7389**: Services-Business Services, NEC. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 20-F, filed 2026-05-20, L4905:

> Our ability to continue to grow in the future depends on a number of factors, including the number and engagement of consumers on our platforms, the value that our businesses are able to offer to our customers, our ability to attract and retain AI + Cloud customers and our data and technology capabilities. See “Item 5. Operating and Financial Review and Prospects — A. Operating Results — Factors Affecting Our Results of Operations — Our Ability to Create Value for Our Users and Generate Revenue.” Our growth is also affected by competition and other factors that may not be within our control, including technological disruptions, supply chain constraints, the macroeconomic environment (including inflation, deflation and consumer and business confidence), disruptions to the economy and business operations from pandemics, natural disasters, armed conflicts or other events, as well as the geopolitical landscape and government policies. Furthermore, due to the size and scale we have achieved, our businesses may not continue to grow as quickly or at all. [S54]

Navigation sector: **industrials**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 20-F, filed 2026-05-20, L586:

> trends and competition in commerce and cloud computing and the other industries in which we operate, both in China and globally, as well as trends in technology innovation, research and development and application, including AI technologies; [S54]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 20-F, filed 2026-05-20, L4760:

> We are a holding company with no operation other than ownership of operating subsidiaries in Chinese mainland, Hong Kong S.A.R., and elsewhere that own and operate our marketplaces and other businesses as well as a portfolio of intellectual property rights. As a result, we rely on dividends and other distributions paid by our operating subsidiaries for our cash and financing requirements, including the funds necessary to repurchase shares, to pay dividends and other cash distribution to our shareholders, fund inter-company loans, service outstanding debts and pay our expenses. If our operating subsidiaries incur additional debt on their own, the instruments governing the debt may restrict the ability of our operating subsidiaries to pay dividends or make other distributions or remittances, including loans, to us. [S54]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 20-F, filed 2026-05-20, L4945:

> Our businesses have become increasingly complex as the scale, diversity and geographic coverage of our businesses and our workforce continue to expand through both organic growth and acquisitions. The complexity and scale of our operations require us to effectively allocate resources among our various businesses and oversee the operations of our various businesses, including in the areas of capital management and compliance and risk management, placing a significant strain on our management, operational and financial resources. We have and, from time to time, may continue to implement organizational changes to align with our strategy and improve our operations. However, organizational changes may be disruptive to our businesses, incur substantive time, resources and costs and divest our management’s attention, which could have a material adverse effect on our business, financial condition, results of operations and prospects. Moreover, the current and planned staffing, systems, policies, procedures and controls of our businesses may not be adequate to support their future operations. To effectively manage continuing expansion and growth of their operations and workforce, our businesses will need to continue to improve their personnel management, transaction processing, operational and financial systems, policies, procedures and controls, particularly as our businesses operate … [S54]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 20-F, filed 2026-05-20, L112:

> Indicate by check mark whether any of those error corrections are restatements that required a recovery analysis of incentive-based compensation received by any of the registrant’s executive officers during the relevant recovery period pursuant to §240.10D-1(b).  [S54]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 20-F, filed 2026-05-20, L603:

> Forward-looking statements involve inherent risks and uncertainties. A number of factors could cause actual results to differ materially from those contained in any forward-looking statement. These factors include but are not limited to the following: our corporate structure, including the VIE structure we use to operate certain businesses in the PRC; our ability to maintain the trusted status of our ecosystem; our ability to compete, innovate and maintain or grow our revenue or business, including expanding our international and cross-border businesses and operations, adopting new technologies, including the development, deployment and use of AI technologies, and managing a large and complex organization; risks associated with sustained investments in our businesses; fluctuations in general economic and business conditions in China and globally; uncertainties arising from competition among countries and geopolitical tensions, including national trade, investment, protectionist or other policies and export control, economic or trade sanctions; risks associated with our strategic transactions; uncertainties and risks associated with a broad range of complex laws and regulations (including in the areas of data security and privacy protection, anti-monopoly and anti-unfair competition, content regulation, consumer protection and regulation of Internet platforms) in the PRC and … [S54]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 13F-HR, 144, 20-F, 20-F/A, 3, 4, 424B2, 424B3, 424B4, 424B5, 6-K, 8-A12B, CERTNYS, CORRESP, CT ORDER, DRS, EFFECT, F-1, F-1/A, F-3ASR, F-4, F-4/A, F-6, F-6EF, FWP, IRANNOTICE, N-PX, S-8, SC 13D, SC 13D/A, SC 13G, SC 13G/A, SCHEDULE 13D/A, SCHEDULE 13G/A, SD, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:34:15.981749+00:00.

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
| 2026-10-13 | S-8 | 0001104659-26-115478 | — | [S03] |
| 2026-10-07 | 6-K | 0001104659-26-114191 | — | [S04] |
| 2026-10-05 | 4 | 0001193125-26-413036 | — | [S05] |
| 2026-10-05 | 4 | 0001193125-26-413032 | — | [S06] |
| 2026-10-02 | 4 | 0001193125-26-411206 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-11-01T16:07:03.340031+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001577552.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [S-8 0001104659-26-115478](https://www.sec.gov/Archives/edgar/data/1577552/000110465926115478/0001104659-26-115478-index.html) — published 2026-10-13; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [6-K 0001104659-26-114191](https://www.sec.gov/Archives/edgar/data/1577552/000110465926114191/0001104659-26-114191-index.html) — published 2026-10-07; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [4 0001193125-26-413036](https://www.sec.gov/Archives/edgar/data/1577552/000119312526413036/0001193125-26-413036-index.html) — published 2026-10-05; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [4 0001193125-26-413032](https://www.sec.gov/Archives/edgar/data/1577552/000119312526413032/0001193125-26-413032-index.html) — published 2026-10-05; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [4 0001193125-26-411206](https://www.sec.gov/Archives/edgar/data/1577552/000119312526411206/0001193125-26-411206-index.html) — published 2026-10-02; retrieved 2026-10-23T08:33:02.691743+00:00.

[S54] [20-F 0001193125-26-231755](https://www.sec.gov/Archives/edgar/data/1577552/000119312526231755/baba-20260331.htm) — published 2026-05-20; retrieved 2026-11-19T21:11:10.142841+00:00.

Source release: `coverage-20261101-41324509967-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/0f49b319f95dcee8e757e592a38a028a04a7bc3c/brain/companies/BABA/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
