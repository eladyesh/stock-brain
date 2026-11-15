---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001122411
cik: '0001122411'
company_name: ASE Technology Holding Co., Ltd.
tickers:
- ASX
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
  - 20-F
  - 20-F/A
  - 25-NSE
  - '3'
  - 3/A
  - '4'
  - 424B1
  - 424B3
  - 424B4
  - 424B5
  - '425'
  - 6-K
  - 6-K/A
  - 8-A12B
  - 8-K12B
  - CORRESP
  - EFFECT
  - F-1
  - F-1/A
  - F-3
  - F-3/A
  - F-3ASR
  - F-4
  - F-4/A
  - F-6
  - F-6 POS
  - F-6EF
  - POS AM
  - RW
  - S-8
  - S-8 POS
  - SC 13D
  - SC 13D/A
  - SC 13E3
  - SC 13E3/A
  - SC 13G
  - SC 13G/A
  - SC 14D9
  - SC TO-C
  - SC TO-T
  - SC TO-T/A
  - SCHEDULE 13D/A
  - SD
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001122411.json
    sha256: 2b1d076fb6bd4379f62310b9b536dcbb6903cd2cf19d7589b9bf7fe2306d86ab
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001122411.json
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
  url: https://data.sec.gov/submissions/CIK0001122411.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 2b1d076fb6bd4379f62310b9b536dcbb6903cd2cf19d7589b9bf7fe2306d86ab
- id: S03
  title: 4 0000950103-26-015546
  url: https://www.sec.gov/Archives/edgar/data/1122411/000095010326015546/0000950103-26-015546-index.html
  published_at: '2026-10-14'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 6-K 0000950103-26-015458
  url: https://www.sec.gov/Archives/edgar/data/1122411/000095010326015458/0000950103-26-015458-index.html
  published_at: '2026-10-13'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 4 0000950103-26-014420
  url: https://www.sec.gov/Archives/edgar/data/1122411/000095010326014420/0000950103-26-014420-index.html
  published_at: '2026-09-24'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 4 0000950103-26-013694
  url: https://www.sec.gov/Archives/edgar/data/1122411/000095010326013694/0000950103-26-013694-index.html
  published_at: '2026-09-09'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 4 0000950103-26-013693
  url: https://www.sec.gov/Archives/edgar/data/1122411/000095010326013693/0000950103-26-013693-index.html
  published_at: '2026-09-09'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S55
  url: https://www.sec.gov/Archives/edgar/data/1122411/000119312526135585/d50802d20f.htm
  title: 20-F 0001193125-26-135585
  published_at: '2026-04-01'
  retrieved_at: '2026-11-15T19:21:12.591505+00:00'
  sha256: 94214bb7f175cbe5effb5969968a2a10e380e943ab68dba33b2c8d59e4a90877
issuer_classification:
  cik: '0001122411'
  classification_status: reported_sic
  entity_type: other
  name: ASE Technology Holding Co., Ltd.
  sic: '3674'
  sic_description: Semiconductors & Related Devices
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 2b1d076fb6bd4379f62310b9b536dcbb6903cd2cf19d7589b9bf7fe2306d86ab
  url: https://data.sec.gov/submissions/CIK0001122411.json
listings:
- ticker: ASX
  exchange: NYSE
  instrument_type: depositary_receipt
research_filings:
- accession: 0001193125-26-135585
  filed: '2026-04-01'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1122411/000119312526135585/0001193125-26-135585-index.html
- accession: 0000950103-20-009583
  filed: '2020-05-15'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1122411/000095010320009583/0000950103-20-009583-index.html
- accession: 0000950103-07-001728
  filed: '2007-07-05'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1122411/000095010307001728/0000950103-07-001728-index.html
- accession: 0000950103-26-015458
  filed: '2026-10-13'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1122411/000095010326015458/0000950103-26-015458-index.html
- accession: 0000950103-26-007005
  filed: '2026-05-08'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1122411/000095010326007005/0000950103-26-007005-index.html
- accession: 0000950103-25-004448
  filed: '2025-04-07'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1122411/000095010325004448/0000950103-25-004448-index.html
- accession: 0000950103-11-001429
  filed: '2011-04-15'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1122411/000095010311001429/0000950103-11-001429-index.html
research_progress:
  stage: evidence_collected
  input_sha256: 80aa4739b97e3c1c79e654721ac1a99c29a127c027f39671db8275d05c3bc127
  last_attempt_at: '2026-11-15T19:14:21.222490+00:00'
  last_success_at: '2026-11-15T19:14:21.222490+00:00'
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
  source_url: https://data.sec.gov/submissions/CIK0001122411.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/8c5afb0854b43beae818b88ec42b173c9411d269/brain/companies/ASX/README.md
full_history_commit: 8c5afb0854b43beae818b88ec42b173c9411d269
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# ASX — ASE Technology Holding Co., Ltd.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/8c5afb0854b43beae818b88ec42b173c9411d269/brain/companies/ASX/README.md)

## Business overview

Reported issuer name: **ASE Technology Holding Co., Ltd.**. Stable SEC CIK: **0001122411**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| ASX | NYSE | depositary_receipt | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 20-F, filed 2026-04-01, L983:

> This annual report on Form 20-F contains “forward-looking statements” within the meaning of Section 27A of the Securities Act and Section 21E of the Exchange Act. Although these forward-looking statements, which may include statements regarding our future results of operations, financial condition, or business prospects, are based on our own information and information from other sources we believe to be reliable, you should not place undue reliance on these forward-looking statements, which apply only as of the date of this annual report. The words “anticipate,” “believe,” “estimate,” “expect,” “intend,” “plan” and similar expressions, as they relate to us, are intended to identify these forward-looking statements in this annual report. Our actual results of operations, financial condition or business prospects may differ materially from those expressed or implied in these forward-looking statements for a variety of reasons, including risks associated with cyclicality and market conditions in the semiconductor or electronics industry; changes in our regulatory environment, including our ability to comply with new or stricter environmental regulations and to resolve environmental liabilities; demand for the outsourced semiconductor packaging, testing and EMS we offer and for such outsourced services generally; the highly competitive semiconductor or manufacturing industry we … [S55]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 20-F, filed 2026-04-01, L73037:

> The Group has the following reportable segments: Packaging, Testing and EMS. The Group packages bare semiconductors into finished semiconductors with enhanced electrical and thermal characteristics; provides testing services, including front-end engineering testing, wafer probing and final testing services; engages in the designing, assembling, manufacturing and sale of electronic components and telecommunications equipment motherboards. Information about other business activities and operating segments that are not reportable are combined and disclosed in “Others.” The Group engages in other activities such as substrate production as well as sale and leasing of real estate properties. [S55]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 20-F, filed 2026-04-01, L1004:

> Since we are dependent on the highly cyclical semiconductor and electronics industries and conditions in the markets for the end-use applications of our products, our revenues and net income may fluctuate significantly. [S55]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 20-F, filed 2026-04-01, L1132:

> Our business is affected by market conditions in the highly cyclical semiconductor and electronics industries. Most of our customers operate in this industry, and variations in order levels from our customers and service fee rates may result in volatility in our revenues and net income. From time to time, the semiconductor and electronics industries experience significant, and sometimes prolonged, downturns. As our business is, and will continue to be, dependent on the requirements for independent packaging, testing and EMS, any future downturn in the industry would reduce demand for our services. If we cannot reduce our costs or adjust our product mix to sufficiently offset any decline in sales volumes, our profitability will suffer, and we may incur losses. [S55]

## Industry and value chain

SEC-reported SIC **3674**: Semiconductors & Related Devices. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 20-F, filed 2026-04-01, L1049:

> Our revenues and profitability may decline if we are unable to obtain adequate supplies of raw materials and energy in a timely manner and at a reasonable price. [S55]

Navigation sector: **information-technology**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 20-F, filed 2026-04-01, L1135:

> Market conditions in the semiconductor and electronics industries depend to a large degree on conditions in the markets for the end-use applications of various products, such as communications, computing, and consumer electronics products. Any deterioration of conditions in the markets for the end-use applications would reduce demand for our services and would likely have a material adverse effect on our financial condition and results of operations. In 2025, approximately 45.8%, 24.0% and 30.2% of our operating revenues from packaging and testing of semiconductors were attributed to communications, computing and consumer electronics/industrial/automotive/other applications, respectively. In the same year, approximately 31.0%, 10.2%, 35.7%, 12.8% and 10.3% of our operating revenues from EMS were attributed to communications, computing, consumer electronics applications, industrial, and automotive applications and others, respectively. Across end-use applications, our customers face intense competition and significant shifts in demand, which could put pricing pressure on our services and may adversely affect our revenues and net income. [S55]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 20-F, filed 2026-04-01, L1352:

> In addition to the Director Removal Case, on July 8, 2021, SFIPC filed an additional class action to request Dr. Tien Wu and other three defendants of the aforementioned criminal proceeding of insider trading to be jointly liable for the damages caused by the alleged insider trading activities. The Intellectual Property and Commercial Court of the R.O.C. ruled in favor of SFIPC and portion of the damages was awarded on August 18, 2022, and all defendants of this class action filed appeals against the August 18 judgment. The Supreme Court of the R.O.C. reversed the August 18 judgment and remanded the case to the Intellectual Property and Commercial Court on March 14, 2024, where it is now being tried. The proceedings in connection with this incident, or potential regulatory scrutiny, might attract further media attention. Any negative publicity in connection with the legal proceedings may adversely affect our brand and reputation, which might result in a material adverse impact on our business operations and prospects. [S55]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 20-F, filed 2026-04-01, L1287:

> Our future success may depend on acquiring businesses and technologies, making investments, or forming joint ventures that complement, enhance, or expand our current product offerings or otherwise offer growth opportunities. In pursuing such acquisitions, we may face competition from other companies in the semiconductor industry. Mergers and acquisitions involve certain integration risks and uncertainties, including the difficulty in integrating technologies, systems, products, policies and operations, coordinating geographically separate organizations and combining different corporate cultures, utilizing capital and other resources in an optimal manner and addressing unanticipated costs or liabilities. Furthermore, our ability to acquire or invest in suitable targets may be limited by applicable laws and regulations in the R.O.C., P.R.C., U.S., European countries, and other jurisdictions where we do business. Even if the businesses we acquire are successfully integrated with our existing business, the benefits of such transactions may not be realized within the anticipated time frame or at all. Each of these risks could have a material adverse effect on our business, financial condition, and results of operations. [S55]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 20-F, filed 2026-04-01, L139:

> Indicate by check mark whether any of those error corrections are restatements that required a recovery analysis of incentive-based compensation received by any of the registrant’s executive officers during the relevant recovery period pursuant to [S55]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 20-F, filed 2026-04-01, L983:

> This annual report on Form 20-F contains “forward-looking statements” within the meaning of Section 27A of the Securities Act and Section 21E of the Exchange Act. Although these forward-looking statements, which may include statements regarding our future results of operations, financial condition, or business prospects, are based on our own information and information from other sources we believe to be reliable, you should not place undue reliance on these forward-looking statements, which apply only as of the date of this annual report. The words “anticipate,” “believe,” “estimate,” “expect,” “intend,” “plan” and similar expressions, as they relate to us, are intended to identify these forward-looking statements in this annual report. Our actual results of operations, financial condition or business prospects may differ materially from those expressed or implied in these forward-looking statements for a variety of reasons, including risks associated with cyclicality and market conditions in the semiconductor or electronics industry; changes in our regulatory environment, including our ability to comply with new or stricter environmental regulations and to resolve environmental liabilities; demand for the outsourced semiconductor packaging, testing and EMS we offer and for such outsourced services generally; the highly competitive semiconductor or manufacturing industry we … [S55]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 20-F, 20-F/A, 25-NSE, 3, 3/A, 4, 424B1, 424B3, 424B4, 424B5, 425, 6-K, 6-K/A, 8-A12B, 8-K12B, CORRESP, EFFECT, F-1, F-1/A, F-3, F-3/A, F-3ASR, F-4, F-4/A, F-6, F-6 POS, F-6EF, POS AM, RW, S-8, S-8 POS, SC 13D, SC 13D/A, SC 13E3, SC 13E3/A, SC 13G, SC 13G/A, SC 14D9, SC TO-C, SC TO-T, SC TO-T/A, SCHEDULE 13D/A, SD, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:31:48.017156+00:00.

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
| 2026-10-14 | 4 | 0000950103-26-015546 | — | [S03] |
| 2026-10-13 | 6-K | 0000950103-26-015458 | — | [S04] |
| 2026-09-24 | 4 | 0000950103-26-014420 | — | [S05] |
| 2026-09-09 | 4 | 0000950103-26-013694 | — | [S06] |
| 2026-09-09 | 4 | 0000950103-26-013693 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-11-01T16:07:03.340031+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001122411.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [4 0000950103-26-015546](https://www.sec.gov/Archives/edgar/data/1122411/000095010326015546/0000950103-26-015546-index.html) — published 2026-10-14; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [6-K 0000950103-26-015458](https://www.sec.gov/Archives/edgar/data/1122411/000095010326015458/0000950103-26-015458-index.html) — published 2026-10-13; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [4 0000950103-26-014420](https://www.sec.gov/Archives/edgar/data/1122411/000095010326014420/0000950103-26-014420-index.html) — published 2026-09-24; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [4 0000950103-26-013694](https://www.sec.gov/Archives/edgar/data/1122411/000095010326013694/0000950103-26-013694-index.html) — published 2026-09-09; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [4 0000950103-26-013693](https://www.sec.gov/Archives/edgar/data/1122411/000095010326013693/0000950103-26-013693-index.html) — published 2026-09-09; retrieved 2026-10-23T08:33:02.691743+00:00.

[S55] [20-F 0001193125-26-135585](https://www.sec.gov/Archives/edgar/data/1122411/000119312526135585/d50802d20f.htm) — published 2026-04-01; retrieved 2026-11-15T19:21:12.591505+00:00.

Source release: `coverage-20261101-41324509967-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/8c5afb0854b43beae818b88ec42b173c9411d269/brain/companies/ASX/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
