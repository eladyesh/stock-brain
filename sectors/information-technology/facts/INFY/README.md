---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001067491
cik: 0001067491
company_name: Infosys Ltd
tickers:
- INFY
status: stub
canonical_reviewed: false
as_of: '2026-10-29'
updated_at: '2026-10-29T16:18:46.634043+00:00'
reviewed_at: null
coverage_release: coverage-20261029-40909364006-1
source_commit: aa19db75827ed3c73031b70e9a0a2e63baffc491
financial_history_available: false
curated_research: null
financial_gap:
  reason: foreign_reporting_adapter
  next_action: Add support for the observed 20-F, 40-F or 6-K reporting forms and
    verify the actual accounting taxonomy before normalization.
  observed_forms:
  - '144'
  - 20-F
  - 20-F/A
  - '25'
  - '3'
  - 3/A
  - '4'
  - 424B3
  - 424B4
  - 424B5
  - 6-K
  - 6-K/A
  - 8-A12B
  - 8-A12G
  - CERTNYS
  - CORRESP
  - F-1
  - F-1/A
  - F-3
  - F-3/A
  - F-3ASR
  - F-6
  - F-6 POS
  - F-6EF
  - POS AM
  - S-8
  - S-8 POS
  - SC 13G
  - SC 13G/A
  - SC TO-C
  - SC TO-I
  - SC TO-I/A
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001067491.json
    sha256: 65e00f589bfdeaca39e0c30f7b75d268cc0bd208fa468ec8d4a0415e8fe9a881
    retrieved_at: '2026-10-24T13:22:51.759433+00:00'
    archive: &id001
      member: CIK0001067491.json
      sha256: 593fbbea6512ef5ec729a5e513c465fbedaac8a66602c0abe00d0ba5a4d18732
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: otherlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt
  published_at: null
  retrieved_at: '2026-10-29T16:14:13.951866+00:00'
  sha256: 2ac9bdaf5d770442eb34b0b33eb6a5240dbd11a3f2077f7b88051dbb82d4313b
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001067491.json
  published_at: null
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 65e00f589bfdeaca39e0c30f7b75d268cc0bd208fa468ec8d4a0415e8fe9a881
- id: S03
  title: 6-K 0001067491-26-000042
  url: https://www.sec.gov/Archives/edgar/data/1067491/000106749126000042/0001067491-26-000042-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S04
  title: 6-K 0001067491-26-000040
  url: https://www.sec.gov/Archives/edgar/data/1067491/000106749126000040/0001067491-26-000040-index.html
  published_at: '2026-10-13'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S05
  title: F-6 POS 0000950127-26-000087
  url: https://www.sec.gov/Archives/edgar/data/1067491/000095012726000087/0000950127-26-000087-index.html
  published_at: '2026-08-28'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S06
  title: F-6EF 0000950127-26-000083
  url: https://www.sec.gov/Archives/edgar/data/1067491/000095012726000083/0000950127-26-000083-index.html
  published_at: '2026-08-12'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S07
  title: 6-K 0001067491-26-000038
  url: https://www.sec.gov/Archives/edgar/data/1067491/000106749126000038/0001067491-26-000038-index.html
  published_at: '2026-07-28'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S54
  url: https://www.sec.gov/Archives/edgar/data/1067491/000119312526270520/infy-20260331.htm
  title: 20-F 0001193125-26-270520
  published_at: '2026-06-15'
  retrieved_at: '2026-10-28T16:23:00.997483+00:00'
  sha256: 1d0ad1d21f120834ed5ca66c7e29e3355403585de05fef8bbca4b3938b3489fe
issuer_classification:
  cik: 0001067491
  classification_status: reported_sic
  entity_type: other
  name: Infosys Ltd
  sic: '7371'
  sic_description: Services-Computer Programming Services
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 65e00f589bfdeaca39e0c30f7b75d268cc0bd208fa468ec8d4a0415e8fe9a881
  url: https://data.sec.gov/submissions/CIK0001067491.json
listings:
- ticker: INFY
  exchange: NYSE
  instrument_type: depositary_receipt
research_filings:
- accession: 0001193125-26-270520
  filed: '2026-06-15'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1067491/000119312526270520/0001193125-26-270520-index.html
- accession: 0001193125-05-072007
  filed: '2005-04-07'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1067491/000119312505072007/0001193125-05-072007-index.html
- accession: 0000891618-03-002481
  filed: '2003-05-13'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1067491/000089161803002481/0000891618-03-002481-index.html
- accession: 0001012870-01-500703
  filed: '2001-05-10'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1067491/000101287001500703/0001012870-01-500703-index.html
- accession: 0001067491-26-000042
  filed: '2026-10-23'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1067491/000106749126000042/0001067491-26-000042-index.html
- accession: 0000891618-03-001618
  filed: '2003-04-01'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1067491/000089161803001618/0000891618-03-001618-index.html
- accession: 0000891618-03-001195
  filed: '2003-03-11'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1067491/000089161803001195/0000891618-03-001195-index.html
research_progress:
  stage: evidence_collected
  input_sha256: 4a44a1d605116186d302bc24759db23bfa57304a650e02de66e58ce40f7010a9
  last_attempt_at: '2026-10-28T16:19:58.196907+00:00'
  last_success_at: '2026-10-28T16:19:58.196907+00:00'
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
  sic: '7371'
  sic_description: Services-Computer Programming Services
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001067491.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/c26f59bc72c00102d2490e95b07449f8cd848491/brain/companies/INFY/README.md
full_history_commit: c26f59bc72c00102d2490e95b07449f8cd848491
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# INFY — Infosys Ltd

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/c26f59bc72c00102d2490e95b07449f8cd848491/brain/companies/INFY/README.md)

## Business overview

Reported issuer name: **Infosys Ltd**. Stable SEC CIK: **0001067491**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| INFY | NYSE | depositary_receipt | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 20-F, filed 2026-06-15, L133:

> This Annual Report on Form 20-F contains ‘forward-looking statements’ within the meaning of Section 27A of the Securities Act of 1933, as amended (the “Securities Act”), and Section 21E of the Securities Exchange Act of 1934, as amended (the “Exchange Act”). Forward-looking statements generally relate to future events or our future financial or operating performance and are based on our current expectations, assumptions, estimates and projections about the Company, our industry, economic conditions in the markets in which we operate, and certain other matters. Generally, these forward-looking statements can be identified by the use of forward-looking terminology such as ‘may’, ‘anticipate’, ‘believe’, ‘estimate’, ‘expect’, ‘continue’, ‘intend’, ‘will’, ‘project’, ‘seek’, ‘could’, ‘would’, ‘should’ and similar expressions. These statements are subject to substantial known and unknown risks, uncertainties and other factors, which may cause actual results or outcomes to differ materially from those implied by the forward-looking statements. Important factors that may cause actual results or outcomes to differ from those implied by the forward-looking statements include, but are not limited to, risks and uncertainties regarding the execution of our business strategy, increased competition for talent, our ability to attract and retain personnel, increase in wages, investments to … [S54]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 20-F, filed 2026-06-15, L745:

> Our AI first services are inherently designed with AI as the core execution layer, enabling new business models, products, and revenue streams for our clients by embedding intelligence directly into enterprise operations and decision making. [S54]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 20-F, filed 2026-06-15, L354:

> Increased regulations, changes to existing regulations or increased government interventions, including sanctions, tariffs or trade restrictions in the industries in which our clients operate or economic uncertainty due to inflation, geopolitical conflicts and potential global economic slowdown may adversely affect our client’s businesses and may reduce demand for our services or cause us to incur additional costs in our processes or personnel, thereby negatively affecting our business, results of operations and financial condition. For instance, our clients may be subject to more stringent compliance requirements, including industry-specific compliance, privacy and security standards for handling data, which could impact the manner in which we provide our services. Additionally, geopolitical conflicts, including conflicts in the Middle East, Eastern Europe and India - Pakistan, may adversely affect certain of our clients’ operations or cause them to redirect spending toward business continuity, which may reduce their IT spend. A general slowdown in key geographies where our clients operate or depend on for their supply chain may adversely affect our revenues and profitability. [S54]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 20-F, filed 2026-06-15, L1078:

> Infosys Topaz Center of Excellence played a pivotal role in industrializing AI across client ecosystems, delivering several Generative AI engagements. This strong execution was underpinned by deep engineering rigor and a relentless focus on measurable business outcomes. We also saw significant traction in agentic AI, with several agent‑based solutions successfully deployed in production and generating tangible value for our customers. [S54]

## Industry and value chain

SEC-reported SIC **7371**: Services-Computer Programming Services. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 20-F, filed 2026-06-15, L354:

> Increased regulations, changes to existing regulations or increased government interventions, including sanctions, tariffs or trade restrictions in the industries in which our clients operate or economic uncertainty due to inflation, geopolitical conflicts and potential global economic slowdown may adversely affect our client’s businesses and may reduce demand for our services or cause us to incur additional costs in our processes or personnel, thereby negatively affecting our business, results of operations and financial condition. For instance, our clients may be subject to more stringent compliance requirements, including industry-specific compliance, privacy and security standards for handling data, which could impact the manner in which we provide our services. Additionally, geopolitical conflicts, including conflicts in the Middle East, Eastern Europe and India - Pakistan, may adversely affect certain of our clients’ operations or cause them to redirect spending toward business continuity, which may reduce their IT spend. A general slowdown in key geographies where our clients operate or depend on for their supply chain may adversely affect our revenues and profitability. [S54]

Navigation sector: **information-technology**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 20-F, filed 2026-06-15, L133:

> This Annual Report on Form 20-F contains ‘forward-looking statements’ within the meaning of Section 27A of the Securities Act of 1933, as amended (the “Securities Act”), and Section 21E of the Securities Exchange Act of 1934, as amended (the “Exchange Act”). Forward-looking statements generally relate to future events or our future financial or operating performance and are based on our current expectations, assumptions, estimates and projections about the Company, our industry, economic conditions in the markets in which we operate, and certain other matters. Generally, these forward-looking statements can be identified by the use of forward-looking terminology such as ‘may’, ‘anticipate’, ‘believe’, ‘estimate’, ‘expect’, ‘continue’, ‘intend’, ‘will’, ‘project’, ‘seek’, ‘could’, ‘would’, ‘should’ and similar expressions. These statements are subject to substantial known and unknown risks, uncertainties and other factors, which may cause actual results or outcomes to differ materially from those implied by the forward-looking statements. Important factors that may cause actual results or outcomes to differ from those implied by the forward-looking statements include, but are not limited to, risks and uncertainties regarding the execution of our business strategy, increased competition for talent, our ability to attract and retain personnel, increase in wages, investments to … [S54]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 20-F, filed 2026-06-15, L302:

> Wage pressures and the hiring of employees and sub-contractors either outside or in India may prevent us from sustaining our competitive advantage and may reduce our profits. [S54]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 20-F, filed 2026-06-15, L300:

> Any inability to manage our growth could disrupt our business, reduce our profitability and adversely impact our ability to implement our growth strategy. [S54]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 20-F, filed 2026-06-15, L101:

> Indicate by check mark whether any of those error corrections are restatements that required a recovery analysis of incentive-based compensation received by any of the registrant’s executive officers during the relevant recovery period pursuant to §240.10D-1(b). ☐ [S54]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 20-F, filed 2026-06-15, L133:

> This Annual Report on Form 20-F contains ‘forward-looking statements’ within the meaning of Section 27A of the Securities Act of 1933, as amended (the “Securities Act”), and Section 21E of the Securities Exchange Act of 1934, as amended (the “Exchange Act”). Forward-looking statements generally relate to future events or our future financial or operating performance and are based on our current expectations, assumptions, estimates and projections about the Company, our industry, economic conditions in the markets in which we operate, and certain other matters. Generally, these forward-looking statements can be identified by the use of forward-looking terminology such as ‘may’, ‘anticipate’, ‘believe’, ‘estimate’, ‘expect’, ‘continue’, ‘intend’, ‘will’, ‘project’, ‘seek’, ‘could’, ‘would’, ‘should’ and similar expressions. These statements are subject to substantial known and unknown risks, uncertainties and other factors, which may cause actual results or outcomes to differ materially from those implied by the forward-looking statements. Important factors that may cause actual results or outcomes to differ from those implied by the forward-looking statements include, but are not limited to, risks and uncertainties regarding the execution of our business strategy, increased competition for talent, our ability to attract and retain personnel, increase in wages, investments to … [S54]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 144, 20-F, 20-F/A, 25, 3, 3/A, 4, 424B3, 424B4, 424B5, 6-K, 6-K/A, 8-A12B, 8-A12G, CERTNYS, CORRESP, F-1, F-1/A, F-3, F-3/A, F-3ASR, F-6, F-6 POS, F-6EF, POS AM, S-8, S-8 POS, SC 13G, SC 13G/A, SC TO-C, SC TO-I, SC TO-I/A, SCHEDULE 13G/A, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:31:22.856716+00:00.

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
| 2026-10-23 | 6-K | 0001067491-26-000042 | — | [S03] |
| 2026-10-13 | 6-K | 0001067491-26-000040 | — | [S04] |
| 2026-08-28 | F-6 POS | 0000950127-26-000087 | — | [S05] |
| 2026-08-12 | F-6EF | 0000950127-26-000083 | — | [S06] |
| 2026-07-28 | 6-K | 0001067491-26-000038 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-29T16:14:13.951866+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001067491.json) — published not supplied; retrieved 2026-10-24T13:22:51.759433+00:00.

[S03] [6-K 0001067491-26-000042](https://www.sec.gov/Archives/edgar/data/1067491/000106749126000042/0001067491-26-000042-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S04] [6-K 0001067491-26-000040](https://www.sec.gov/Archives/edgar/data/1067491/000106749126000040/0001067491-26-000040-index.html) — published 2026-10-13; retrieved 2026-10-24T13:22:51.759433+00:00.

[S05] [F-6 POS 0000950127-26-000087](https://www.sec.gov/Archives/edgar/data/1067491/000095012726000087/0000950127-26-000087-index.html) — published 2026-08-28; retrieved 2026-10-24T13:22:51.759433+00:00.

[S06] [F-6EF 0000950127-26-000083](https://www.sec.gov/Archives/edgar/data/1067491/000095012726000083/0000950127-26-000083-index.html) — published 2026-08-12; retrieved 2026-10-24T13:22:51.759433+00:00.

[S07] [6-K 0001067491-26-000038](https://www.sec.gov/Archives/edgar/data/1067491/000106749126000038/0001067491-26-000038-index.html) — published 2026-07-28; retrieved 2026-10-24T13:22:51.759433+00:00.

[S54] [20-F 0001193125-26-270520](https://www.sec.gov/Archives/edgar/data/1067491/000119312526270520/infy-20260331.htm) — published 2026-06-15; retrieved 2026-10-28T16:23:00.997483+00:00.

Source release: `coverage-20261029-40909364006-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/c26f59bc72c00102d2490e95b07449f8cd848491/brain/companies/INFY/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
