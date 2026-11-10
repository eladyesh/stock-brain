---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001603993
cik: 0001603993
company_name: AIOS Tech Inc.
tickers:
- AIOS
status: stub
canonical_reviewed: false
as_of: '2026-11-01'
updated_at: '2026-11-01T16:11:48.803754+00:00'
reviewed_at: null
coverage_release: coverage-20261101-41324509967-1
source_commit: 6dea3be4625120db9da80155a96f14ed62690190
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
  - 4/A
  - 424B3
  - 424B5
  - 6-K
  - 6-K/A
  - 8-A12B
  - 8-A12B/A
  - CERTNAS
  - CORRESP
  - DRS
  - DRS/A
  - DRSLTR
  - EFFECT
  - F-1
  - F-1/A
  - F-3
  - NT 20-F
  - POS AM
  - S-8
  - S-8 POS
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13D
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001603993.json
    sha256: fe64e3b0b388bdaab0e5fc7535185e8212b5268815bff4a85f8ce543e59cbf9b
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001603993.json
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
  url: https://data.sec.gov/submissions/CIK0001603993.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: fe64e3b0b388bdaab0e5fc7535185e8212b5268815bff4a85f8ce543e59cbf9b
- id: S03
  title: 6-K 0001213900-26-110699
  url: https://www.sec.gov/Archives/edgar/data/1603993/000121390026110699/0001213900-26-110699-index.html
  published_at: '2026-10-19'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 6-K 0001213900-26-105272
  url: https://www.sec.gov/Archives/edgar/data/1603993/000121390026105272/0001213900-26-105272-index.html
  published_at: '2026-09-30'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 6-K 0001213900-26-101658
  url: https://www.sec.gov/Archives/edgar/data/1603993/000121390026101658/0001213900-26-101658-index.html
  published_at: '2026-09-21'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: EFFECT 9999999995-26-002464
  url: https://www.sec.gov/Archives/edgar/data/1603993/999999999526002464/9999999995-26-002464-index.html
  published_at: '2026-07-27'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: F-3 0001213900-26-079154
  url: https://www.sec.gov/Archives/edgar/data/1603993/000121390026079154/0001213900-26-079154-index.html
  published_at: '2026-07-17'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S54
  url: https://www.sec.gov/Archives/edgar/data/1603993/000121390026045606/ea0282962-20f_aiostech.htm
  title: 20-F 0001213900-26-045606
  published_at: '2026-04-20'
  retrieved_at: '2026-11-08T18:16:48.963036+00:00'
  sha256: a1543acd0ab0b36219485fc4f25ea3b3b8b08d75ca52777432c3dedcfb5bdee1
issuer_classification:
  cik: 0001603993
  classification_status: reported_sic
  entity_type: other
  name: AIOS Tech Inc.
  sic: '7373'
  sic_description: Services-Computer Integrated Systems Design
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: fe64e3b0b388bdaab0e5fc7535185e8212b5268815bff4a85f8ce543e59cbf9b
  url: https://data.sec.gov/submissions/CIK0001603993.json
listings:
- ticker: AIOS
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001213900-26-045606
  filed: '2026-04-20'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1603993/000121390026045606/0001213900-26-045606-index.html
- accession: 0001144204-18-005567
  filed: '2018-02-05'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1603993/000114420418005567/0001144204-18-005567-index.html
- accession: 0001213900-26-110699
  filed: '2026-10-19'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1603993/000121390026110699/0001213900-26-110699-index.html
- accession: 0001213900-22-008927
  filed: '2022-02-23'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1603993/000121390022008927/0001213900-22-008927-index.html
- accession: 0001144204-18-022483
  filed: '2018-04-26'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1603993/000114420418022483/0001144204-18-022483-index.html
research_progress:
  stage: evidence_collected
  input_sha256: 5ee26b6d320bd0cc003df4f10c96ba6e0d6ec1d0eb9369af5f71e1e6dac6d1ea
  last_attempt_at: '2026-11-08T18:13:06.363886+00:00'
  last_success_at: '2026-11-08T18:13:06.363886+00:00'
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
  sic: '7373'
  sic_description: Services-Computer Integrated Systems Design
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001603993.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/876d144f6387664050d096ed943ae2c26137a2cb/brain/companies/AIOS/README.md
full_history_commit: 876d144f6387664050d096ed943ae2c26137a2cb
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# AIOS — AIOS Tech Inc.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/876d144f6387664050d096ed943ae2c26137a2cb/brain/companies/AIOS/README.md)

## Business overview

Reported issuer name: **AIOS Tech Inc.**. Stable SEC CIK: **0001603993**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| AIOS | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 20-F, filed 2026-04-20, L383:

> references to our business and operations in fiscal years 2023 and 2024 and the period prior to December 2025 also include our “former [S54]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 20-F, filed 2026-04-20, L8363:

> November 2023, the FASB issued ASU 2023-07, Segment Reporting (Topic 280): Improvements to Reportable Segment Disclosures. ASU 2023-07 [S54]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 20-F, filed 2026-04-20, L965:

> innovation in the IT services and fintech industries, the demand for our services could stagnate or substantially decline, our business [S54]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 20-F, filed 2026-04-20, L769:

> rely on our cooperation with our customers and industry partners, and if our technology solutions or services cannot meet the needs or [S54]

## Industry and value chain

SEC-reported SIC **7373**: Services-Computer Integrated Systems Design. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 20-F, filed 2026-04-20, L518:

> \| FanShengke Supply Chain (Fujian) Co., Ltd. (“Fanshengke Fujian”) (also referred to as 范圣克供应链（福建）有限公司), a wholly-owned subsidiary of Fanshengke; and [S54]

Navigation sector: **information-technology**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 20-F, filed 2026-04-20, L779:

> use their in-house research and development capabilities or choose our competitors to develop their digital platforms and AI solutions. [S54]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 20-F, filed 2026-04-20, L1000:

> our operations and could result in the loss or leakage of proprietary data or intellectual property. [S54]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 20-F, filed 2026-04-20, L783:

> ability to maintain and expand our customer base and build long-term relationships with our partners also depends on a number of other [S54]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 20-F, filed 2026-04-20, L104:

> received by any of the registrant’s executive officers during the relevant recovery period pursuant to §240.10D-1(b). ☐ [S54]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 20-F, filed 2026-04-20, L801:

> business, financial condition, operating results and prospects may be materially adversely affected if our technology solutions or services [S54]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 20-F, 20-F/A, 3, 4, 4/A, 424B3, 424B5, 6-K, 6-K/A, 8-A12B, 8-A12B/A, CERTNAS, CORRESP, DRS, DRS/A, DRSLTR, EFFECT, F-1, F-1/A, F-3, NT 20-F, POS AM, S-8, S-8 POS, SC 13D, SC 13D/A, SC 13G, SC 13G/A, SCHEDULE 13D, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:34:28.763157+00:00.

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
| 2026-10-19 | 6-K | 0001213900-26-110699 | — | [S03] |
| 2026-09-30 | 6-K | 0001213900-26-105272 | — | [S04] |
| 2026-09-21 | 6-K | 0001213900-26-101658 | — | [S05] |
| 2026-07-27 | EFFECT | 9999999995-26-002464 | — | [S06] |
| 2026-07-17 | F-3 | 0001213900-26-079154 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-11-01T16:07:03.070084+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001603993.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [6-K 0001213900-26-110699](https://www.sec.gov/Archives/edgar/data/1603993/000121390026110699/0001213900-26-110699-index.html) — published 2026-10-19; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [6-K 0001213900-26-105272](https://www.sec.gov/Archives/edgar/data/1603993/000121390026105272/0001213900-26-105272-index.html) — published 2026-09-30; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [6-K 0001213900-26-101658](https://www.sec.gov/Archives/edgar/data/1603993/000121390026101658/0001213900-26-101658-index.html) — published 2026-09-21; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [EFFECT 9999999995-26-002464](https://www.sec.gov/Archives/edgar/data/1603993/999999999526002464/9999999995-26-002464-index.html) — published 2026-07-27; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [F-3 0001213900-26-079154](https://www.sec.gov/Archives/edgar/data/1603993/000121390026079154/0001213900-26-079154-index.html) — published 2026-07-17; retrieved 2026-10-23T08:33:02.691743+00:00.

[S54] [20-F 0001213900-26-045606](https://www.sec.gov/Archives/edgar/data/1603993/000121390026045606/ea0282962-20f_aiostech.htm) — published 2026-04-20; retrieved 2026-11-08T18:16:48.963036+00:00.

Source release: `coverage-20261101-41324509967-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/876d144f6387664050d096ed943ae2c26137a2cb/brain/companies/AIOS/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
