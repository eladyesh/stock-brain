---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001702318
cik: 0001702318
company_name: Akso Health Group
tickers:
- AHG
status: stub
canonical_reviewed: false
as_of: '2026-11-01'
updated_at: '2026-11-01T16:11:48.803754+00:00'
reviewed_at: null
coverage_release: coverage-20261101-41324509967-1
source_commit: da985d7cdd310eab261be4fd3662836a26873702
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
  - 424B3
  - 424B4
  - 424B5
  - 6-K
  - 8-A12B
  - CERTNAS
  - CORRESP
  - DRS
  - DRS/A
  - DRSLTR
  - EFFECT
  - F-1
  - F-1/A
  - F-3
  - F-3/A
  - F-6
  - F-6 POS
  - NT 20-F
  - RW
  - S-8
  - SC 13D
  - SC 13G
  - SC 13G/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001702318.json
    sha256: 4f362f62ce5cada42e0c248060daf17bef5ae4b6644033e0c6a22591b6c7d039
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001702318.json
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
  url: https://data.sec.gov/submissions/CIK0001702318.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 4f362f62ce5cada42e0c248060daf17bef5ae4b6644033e0c6a22591b6c7d039
- id: S03
  title: 20-F 0001213900-26-080868
  url: https://www.sec.gov/Archives/edgar/data/1702318/000121390026080868/0001213900-26-080868-index.html
  published_at: '2026-07-23'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 6-K 0001213900-26-055807
  url: https://www.sec.gov/Archives/edgar/data/1702318/000121390026055807/0001213900-26-055807-index.html
  published_at: '2026-05-13'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 3 0001994381-26-000003
  url: https://www.sec.gov/Archives/edgar/data/1702318/000199438126000003/0001994381-26-000003-index.html
  published_at: '2026-04-06'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 3 0002125169-26-000001
  url: https://www.sec.gov/Archives/edgar/data/1702318/000212516926000001/0002125169-26-000001-index.html
  published_at: '2026-03-30'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 3 0002124073-26-000001
  url: https://www.sec.gov/Archives/edgar/data/1702318/000212407326000001/0002124073-26-000001-index.html
  published_at: '2026-03-27'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S53
  url: https://www.sec.gov/Archives/edgar/data/1702318/000121390026080868/ea0294288-20f_akso.htm
  title: 20-F 0001213900-26-080868
  published_at: '2026-07-23'
  retrieved_at: '2026-11-07T18:02:16.369714+00:00'
  sha256: 956bead0e4cc55287c9f4b28d19d988e48634c93a8d8df8004db5a8d000f5f7d
issuer_classification:
  cik: 0001702318
  classification_status: reported_sic
  entity_type: other
  name: Akso Health Group
  sic: '7389'
  sic_description: Services-Business Services, NEC
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 4f362f62ce5cada42e0c248060daf17bef5ae4b6644033e0c6a22591b6c7d039
  url: https://data.sec.gov/submissions/CIK0001702318.json
listings:
- ticker: AHG
  exchange: NASDAQ
  instrument_type: depositary_receipt
research_filings:
- accession: 0001213900-26-080868
  filed: '2026-07-23'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1702318/000121390026080868/0001213900-26-080868-index.html
- accession: 0001213900-26-055807
  filed: '2026-05-13'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1702318/000121390026055807/0001213900-26-055807-index.html
research_progress:
  stage: evidence_collected
  input_sha256: 649f234c704495df69ce96911a5f6fa98d766b978f1095075ec8488aa3144ae0
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
  source_url: https://data.sec.gov/submissions/CIK0001702318.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/6e1c8271c74cf7335265700a5a223e692b47544f/brain/companies/AHG/README.md
full_history_commit: 6e1c8271c74cf7335265700a5a223e692b47544f
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# AHG — Akso Health Group

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/6e1c8271c74cf7335265700a5a223e692b47544f/brain/companies/AHG/README.md)

## Business overview

Reported issuer name: **Akso Health Group**. Stable SEC CIK: **0001702318**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| AHG | NASDAQ | depositary_receipt | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 20-F, filed 2026-07-23, L254:

> in both China and the United States, and our financial records are maintained in RMB for our business in China and in U.S. dollar for [S53]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 20-F, filed 2026-07-23, L10003:

> In accordance with ASC 280, Segment Reporting, operating segments are defined as components of an enterprise about which separate financial information is available that is evaluated regularly by the chief operating decision maker (“CODM”), or decision—making group, in deciding how to allocate resources and in assessing performance. The Company uses the “management approach” in determining reportable operating segments. The management approach considers the internal organization and reporting used by the Company’s chief operating decision maker for making operating decisions and assessing performance as the source for determining the Company’s reportable segments. The Company operates as a single reportable segment as defined by ASC 280, with the Chief Operating Decision Maker (CODM), identified as the Chief Executive Officer, reviewing consolidated results for the purpose of allocating resources and assessing performance. For the years ended March 31, 2026, 2025 and 2024, the operating expenses related to the reporting operation were US$20.7 million, US$166.0 million and US$8.8 million, respectively. [S53]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 20-F, filed 2026-07-23, L666:

> \| Part of our services could be disrupted by network interruptions. (see “Part of our services could be disrupted by network interruptions.” on page 18 of this annual report); [S53]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 20-F, filed 2026-07-23, L654:

> \| Our ability to protect the confidential information of our customers may be adversely affected by cyberattacks, computer viruses, physical or electronic break-ins or similar disruptions. (see “Our ability to protect the confidential information of our customers may be adversely affected by cyberattacks, computer viruses, physical or electronic break-ins or similar disruptions.” on page 17 of this annual report); [S53]

## Industry and value chain

SEC-reported SIC **7389**: Services-Business Services, NEC. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 20-F, filed 2026-07-23, L636:

> \| We are dependent on our suppliers to reach potential car insurance purchasers for our marketing promotion services business. Failure to maintain cooperation with our suppliers or to secure new suppliers could materially and adversely affect our business. (see “We are dependent on our suppliers to reach potential car insurance purchasers for our marketing promotion services business. Failure to maintain cooperation with our suppliers or to secure new suppliers could materially and adversely affect our business.” on page 16 of this annual report); [S53]

Navigation sector: **industrials**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 20-F, filed 2026-07-23, L381:

> August 1, 2022), the anti-monopoly guidelines for various industries, and the detailed Rules for the Implementation of the Fair Competition [S53]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 20-F, filed 2026-07-23, L721:

> \| We may not be able to prevent others from unauthorized use of our intellectual property, which could harm our business and competitive position. (See “We may not be able to prevent others from unauthorized use of our intellectual property, which could harm our business and competitive position.” on page 26 of this annual report.) [S53]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 20-F, filed 2026-07-23, L811:

> \| PRC regulation of loans to and direct investment in PRC entities by offshore holding companies and governmental control of currency conversion may delay or prevent us from using the proceeds of our initial public offering and the concurrent private placement to make loans to or make additional capital contributions to our PRC subsidiary, which could materially and adversely affect our liquidity and our ability to fund and expand our business. (see “PRC regulation of loans to and direct investment in PRC entities by offshore holding companies and governmental control of currency conversion may delay or prevent us from using the proceeds of our initial public offering and the concurrent private placement to make loans to or make additional capital contributions to our PRC subsidiary, which could materially and adversely affect our liquidity and our ability to fund and expand our business” on page 33 of this annual report); [S53]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 20-F, filed 2026-07-23, L588:

> be paid if this would result in us being unable to pay our debts due in the ordinary course of business. Our board of directors has discretion [S53]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 20-F, filed 2026-07-23, L306:

> not to place undue reliance on these forward-looking statements and you should read these statements in conjunction with the risk factors [S53]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 144, 20-F, 3, 424B3, 424B4, 424B5, 6-K, 8-A12B, CERTNAS, CORRESP, DRS, DRS/A, DRSLTR, EFFECT, F-1, F-1/A, F-3, F-3/A, F-6, F-6 POS, NT 20-F, RW, S-8, SC 13D, SC 13G, SC 13G/A, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:35:08.031735+00:00.

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
| 2026-07-23 | 20-F | 0001213900-26-080868 | — | [S03] |
| 2026-05-13 | 6-K | 0001213900-26-055807 | — | [S04] |
| 2026-04-06 | 3 | 0001994381-26-000003 | — | [S05] |
| 2026-03-30 | 3 | 0002125169-26-000001 | — | [S06] |
| 2026-03-27 | 3 | 0002124073-26-000001 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-11-01T16:07:03.070084+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001702318.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [20-F 0001213900-26-080868](https://www.sec.gov/Archives/edgar/data/1702318/000121390026080868/0001213900-26-080868-index.html) — published 2026-07-23; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [6-K 0001213900-26-055807](https://www.sec.gov/Archives/edgar/data/1702318/000121390026055807/0001213900-26-055807-index.html) — published 2026-05-13; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [3 0001994381-26-000003](https://www.sec.gov/Archives/edgar/data/1702318/000199438126000003/0001994381-26-000003-index.html) — published 2026-04-06; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [3 0002125169-26-000001](https://www.sec.gov/Archives/edgar/data/1702318/000212516926000001/0002125169-26-000001-index.html) — published 2026-03-30; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [3 0002124073-26-000001](https://www.sec.gov/Archives/edgar/data/1702318/000212407326000001/0002124073-26-000001-index.html) — published 2026-03-27; retrieved 2026-10-23T08:33:02.691743+00:00.

[S53] [20-F 0001213900-26-080868](https://www.sec.gov/Archives/edgar/data/1702318/000121390026080868/ea0294288-20f_akso.htm) — published 2026-07-23; retrieved 2026-11-07T18:02:16.369714+00:00.

Source release: `coverage-20261101-41324509967-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/6e1c8271c74cf7335265700a5a223e692b47544f/brain/companies/AHG/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
