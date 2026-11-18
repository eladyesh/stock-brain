---
schema_version: 1
document_type: company_facts
company_id: company-cik-0000901832
cik: 0000901832
company_name: ASTRAZENECA PLC
tickers:
- AZN
status: stub
canonical_reviewed: false
as_of: '2026-11-01'
updated_at: '2026-11-01T16:11:48.803754+00:00'
reviewed_at: null
coverage_release: coverage-20261101-41324509967-1
source_commit: ddae9173dac59b8f117d07d566c062594b1014b4
financial_history_available: false
curated_research: null
financial_gap:
  reason: foreign_reporting_adapter
  next_action: Add support for the observed 20-F, 40-F or 6-K reporting forms and
    verify the actual accounting taxonomy before normalization.
  observed_forms:
  - 11-K
  - '144'
  - 20-F
  - '25'
  - 25-NSE
  - '3'
  - 3/A
  - '4'
  - 424B2
  - 424B3
  - '425'
  - 6-K
  - 6-K/A
  - 8-A12B
  - CERT
  - CORRESP
  - DFAN14A
  - EFFECT
  - F-3ASR
  - F-4
  - F-4/A
  - F-6
  - F-6EF
  - FWP
  - IRANNOTICE
  - S-8
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SC TO-C
  - SC TO-T
  - SC TO-T/A
  - SCHEDULE 13D/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0000901832.json
    sha256: 8e96ebbc673d67adadc1722919daf66b0cb8ae72e0453e3c06582a313bfeea98
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0000901832.json
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
  url: https://data.sec.gov/submissions/CIK0000901832.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 8e96ebbc673d67adadc1722919daf66b0cb8ae72e0453e3c06582a313bfeea98
- id: S03
  title: 6-K 0001654954-26-009093
  url: https://www.sec.gov/Archives/edgar/data/901832/000165495426009093/0001654954-26-009093-index.html
  published_at: '2026-10-22'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 4 0002122411-26-000002
  url: https://www.sec.gov/Archives/edgar/data/901832/000212241126000002/0002122411-26-000002-index.html
  published_at: '2026-10-08'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 6-K 0001654954-26-008783
  url: https://www.sec.gov/Archives/edgar/data/901832/000165495426008783/0001654954-26-008783-index.html
  published_at: '2026-10-05'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 6-K 0001654954-26-008760
  url: https://www.sec.gov/Archives/edgar/data/901832/000165495426008760/0001654954-26-008760-index.html
  published_at: '2026-10-02'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 6-K 0001654954-26-008741
  url: https://www.sec.gov/Archives/edgar/data/901832/000165495426008741/0001654954-26-008741-index.html
  published_at: '2026-10-01'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S54
  url: https://www.sec.gov/Archives/edgar/data/901832/000110465926019130/azn-20251231x20f.htm
  title: 20-F 0001104659-26-019130
  published_at: '2026-02-24'
  retrieved_at: '2026-11-18T21:06:24.905060+00:00'
  sha256: 036de3c82522a7f52d5c0858dd9fad787923e3428b42542e40244a972382e5a5
issuer_classification:
  cik: 0000901832
  classification_status: reported_sic
  entity_type: other
  name: ASTRAZENECA PLC
  sic: '2834'
  sic_description: Pharmaceutical Preparations
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 8e96ebbc673d67adadc1722919daf66b0cb8ae72e0453e3c06582a313bfeea98
  url: https://data.sec.gov/submissions/CIK0000901832.json
listings:
- ticker: AZN
  exchange: NYSE
  instrument_type: common_stock
research_filings:
- accession: 0001104659-26-019130
  filed: '2026-02-24'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/901832/000110465926019130/0001104659-26-019130-index.html
- accession: 0001654954-26-009093
  filed: '2026-10-22'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/901832/000165495426009093/0001654954-26-009093-index.html
- accession: 0001104659-21-097940
  filed: '2021-07-30'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/901832/000110465921097940/0001104659-21-097940-index.html
- accession: 0001104659-20-089187
  filed: '2020-07-31'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/901832/000110465920089187/0001104659-20-089187-index.html
research_progress:
  stage: evidence_collected
  input_sha256: 8503c98c283578df7e162d36cc2daf36614dc5d0fd4e610a3f0b8e73fd1a7d7c
  last_attempt_at: '2026-11-18T21:00:27.361756+00:00'
  last_success_at: '2026-11-18T21:00:27.361756+00:00'
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
  sic: '2834'
  sic_description: Pharmaceutical Preparations
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0000901832.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/b9d67ef2f16565081e0df464efbaff4348778881/brain/companies/AZN/README.md
full_history_commit: b9d67ef2f16565081e0df464efbaff4348778881
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# AZN — ASTRAZENECA PLC

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/b9d67ef2f16565081e0df464efbaff4348778881/brain/companies/AZN/README.md)

## Business overview

Reported issuer name: **ASTRAZENECA PLC**. Stable SEC CIK: **0000901832**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| AZN | NYSE | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 20-F, filed 2026-02-24, L435:

> Operating in the pharmaceutical sector carries various inherent risks and uncertainties that may affect our business. In this section, we describe the risks and uncertainties that we consider material to our business, in that they may have a significant effect on our financial condition, results of operations and/or reputation. [S54]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 20-F, filed 2026-02-24, L23144:

> The Group has assessed the prospects of the Group over a period longer than the required 12 months from the date of Board approval of these Consolidated Financial Statements, with no deterioration noted requiring a further extension of this review. The Group’s revenues are largely derived from sales of medicines covered by patents, which provide a relatively high level of resilience and predictability to cash inflows, although government price interventions in response to budgetary constraints are expected to continue to adversely affect revenues in some of our significant markets. The Group, however, anticipates new revenue streams from both recently launched medicines and those in development, and the Group has a wide diversity of customers and suppliers across different geographic areas. [S54]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 20-F, filed 2026-02-24, L484:

> We are subject to laws and regulations that control our ability to market our pharmaceutical products. Our development programmes must meet many standards to prove our products are safe, effective and of high quality. Health authorities, such as the FDA in the US and the European Medicines Agency in the EU, can refuse to approve our products or require us to conduct additional clinical trials or scientific testing before they will approve them for marketing. Many factors influence health authority decisions to approve or reject a marketing application for a pharmaceutical product. These include advances in science and technology, new laws, regulations and policies, and different standards for evaluating safety and effectiveness. [S54]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 20-F, filed 2026-02-24, L50462:

> Given the profile of our customers, including large wholesalers and government-backed agencies, no further credit risk has been identified with the Trade receivables not past due other than those balances for which an allowance has been made. [S54]

## Industry and value chain

SEC-reported SIC **2834**: Pharmaceutical Preparations. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 20-F, filed 2026-02-24, L578:

> &gt; Supply shortages or delays in construction of facilities to support future demand of our products caused by significant unforecasted demand growth or supply chain disruptions (e.g. natural disasters, climate impacts, pandemics, conflict or political unrest, failure in IT (including cyber-attack)). [S54]

Navigation sector: **health-care**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 20-F, filed 2026-02-24, L467:

> Competition from other pharmaceutical companies means that we may have to pay a significant premium over book or market values for our acquisitions. Failure to complete collaborative projects in a timely, cost-effective manner may limit our ability to access a greater portfolio of products, intellectual property (IP), technology and shared expertise. In many cases, we make milestone payments in advance of the commercialisation of the products, with no assurance of recouping costs. [S54]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 20-F, filed 2026-02-24, L467:

> Competition from other pharmaceutical companies means that we may have to pay a significant premium over book or market values for our acquisitions. Failure to complete collaborative projects in a timely, cost-effective manner may limit our ability to access a greater portfolio of products, intellectual property (IP), technology and shared expertise. In many cases, we make milestone payments in advance of the commercialisation of the products, with no assurance of recouping costs. [S54]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 20-F, filed 2026-02-24, L461:

> In addition to developing products in-house, we continue to expand our portfolio through licensing arrangements and strategic collaborations which may not ultimately be successful. [S54]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 20-F, filed 2026-02-24, L382:

> Indicate by check mark whether any of those error corrections are restatements that required a recovery analysis of incentive-based compensation received by any of the registrant’s executive officers during the relevant recovery period pursuant to §240.10D-1(b). ☐ [S54]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 20-F, filed 2026-02-24, L508:

> Our pricing approach, as described in the previous paragraph, is a key contributor to our success. However, there are various external risk factors that could compromise our ability to execute our pricing strategies as planned. The market access environment is highly complex and subject to dynamic economic, political and social pressures. Globally, there are increasing cost-containment measures, greater calls for net price and R&D cost transparency, as well as early discussions towards pooled procurement mechanisms beyond emergency countermeasures and essential medicines. [S54]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 11-K, 144, 20-F, 25, 25-NSE, 3, 3/A, 4, 424B2, 424B3, 425, 6-K, 6-K/A, 8-A12B, CERT, CORRESP, DFAN14A, EFFECT, F-3ASR, F-4, F-4/A, F-6, F-6EF, FWP, IRANNOTICE, S-8, SC 13D, SC 13D/A, SC 13G, SC 13G/A, SC TO-C, SC TO-T, SC TO-T/A, SCHEDULE 13D/A, SCHEDULE 13G, SCHEDULE 13G/A, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:30:14.371377+00:00.

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
| 2026-10-22 | 6-K | 0001654954-26-009093 | — | [S03] |
| 2026-10-08 | 4 | 0002122411-26-000002 | — | [S04] |
| 2026-10-05 | 6-K | 0001654954-26-008783 | — | [S05] |
| 2026-10-02 | 6-K | 0001654954-26-008760 | — | [S06] |
| 2026-10-01 | 6-K | 0001654954-26-008741 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-11-01T16:07:03.340031+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0000901832.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [6-K 0001654954-26-009093](https://www.sec.gov/Archives/edgar/data/901832/000165495426009093/0001654954-26-009093-index.html) — published 2026-10-22; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [4 0002122411-26-000002](https://www.sec.gov/Archives/edgar/data/901832/000212241126000002/0002122411-26-000002-index.html) — published 2026-10-08; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [6-K 0001654954-26-008783](https://www.sec.gov/Archives/edgar/data/901832/000165495426008783/0001654954-26-008783-index.html) — published 2026-10-05; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [6-K 0001654954-26-008760](https://www.sec.gov/Archives/edgar/data/901832/000165495426008760/0001654954-26-008760-index.html) — published 2026-10-02; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [6-K 0001654954-26-008741](https://www.sec.gov/Archives/edgar/data/901832/000165495426008741/0001654954-26-008741-index.html) — published 2026-10-01; retrieved 2026-10-23T08:33:02.691743+00:00.

[S54] [20-F 0001104659-26-019130](https://www.sec.gov/Archives/edgar/data/901832/000110465926019130/azn-20251231x20f.htm) — published 2026-02-24; retrieved 2026-11-18T21:06:24.905060+00:00.

Source release: `coverage-20261101-41324509967-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/b9d67ef2f16565081e0df464efbaff4348778881/brain/companies/AZN/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
