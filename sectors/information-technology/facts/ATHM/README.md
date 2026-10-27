---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001527636
cik: '0001527636'
company_name: Autohome Inc.
tickers:
- ATHM
status: stub
canonical_reviewed: false
as_of: '2026-10-27'
updated_at: '2026-10-27T15:30:18.641431+00:00'
reviewed_at: null
coverage_release: coverage-20261027-40530587641-1
source_commit: 77264ce478c0c699392c0a049f464d4fda44c9f8
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
  - '4'
  - 424B3
  - 424B4
  - 424B5
  - 6-K
  - 8-A12B
  - CERTNYS
  - CORRESP
  - CT ORDER
  - DRS
  - DRS/A
  - EFFECT
  - F-1
  - F-1/A
  - F-3ASR
  - F-6
  - FWP
  - IRANNOTICE
  - S-8
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13D
  - SCHEDULE 13D/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001527636.json
    sha256: 8ed113c44577c37c18781a8bbd0169d023c1864bb26d19465b7b0948dfcd1c8d
    retrieved_at: '2026-10-24T13:22:51.759433+00:00'
    archive: &id001
      member: CIK0001527636.json
      sha256: 593fbbea6512ef5ec729a5e513c465fbedaac8a66602c0abe00d0ba5a4d18732
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: otherlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt
  published_at: null
  retrieved_at: '2026-10-27T15:25:35.250901+00:00'
  sha256: 3e845dbd702671bbfbbc700f50d314d4d4cb439640ee0fe6fbf22fc3344c7f42
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001527636.json
  published_at: null
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 8ed113c44577c37c18781a8bbd0169d023c1864bb26d19465b7b0948dfcd1c8d
- id: S03
  title: 6-K 0001193125-26-429429
  url: https://www.sec.gov/Archives/edgar/data/1527636/000119312526429429/0001193125-26-429429-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S04
  title: 6-K 0001193125-26-421013
  url: https://www.sec.gov/Archives/edgar/data/1527636/000119312526421013/0001193125-26-421013-index.html
  published_at: '2026-10-14'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S05
  title: 4 0001976012-26-000008
  url: https://www.sec.gov/Archives/edgar/data/1527636/000197601226000008/0001976012-26-000008-index.html
  published_at: '2026-10-01'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S06
  title: 4 0001975515-26-000006
  url: https://www.sec.gov/Archives/edgar/data/1527636/000197551526000006/0001975515-26-000006-index.html
  published_at: '2026-10-01'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S07
  title: 4 0001975234-26-000008
  url: https://www.sec.gov/Archives/edgar/data/1527636/000197523426000008/0001975234-26-000008-index.html
  published_at: '2026-10-01'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S54
  url: https://www.sec.gov/Archives/edgar/data/1527636/000119312526155932/athm-20251231.htm
  title: 20-F 0001193125-26-155932
  published_at: '2026-04-15'
  retrieved_at: '2026-10-24T13:48:50.004948+00:00'
  sha256: 55645138ebfdbbb9513d3e7d2e9ed356da0c2ffe22a2f29c57b4547fedb67c8a
issuer_classification:
  cik: '0001527636'
  classification_status: reported_sic
  entity_type: other
  name: Autohome Inc.
  sic: '7374'
  sic_description: Services-Computer Processing & Data Preparation
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 8ed113c44577c37c18781a8bbd0169d023c1864bb26d19465b7b0948dfcd1c8d
  url: https://data.sec.gov/submissions/CIK0001527636.json
listings:
- ticker: ATHM
  exchange: NYSE
  instrument_type: depositary_receipt
research_filings:
- accession: 0001193125-26-155932
  filed: '2026-04-15'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1527636/000119312526155932/0001193125-26-155932-index.html
- accession: 0001193125-26-429429
  filed: '2026-10-23'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1527636/000119312526429429/0001193125-26-429429-index.html
research_progress:
  stage: evidence_collected
  input_sha256: 3184062b20ad23def543435a8e8252a65c26c547cc665ab70a8968c2ed3155fd
  last_attempt_at: '2026-10-24T13:43:29.782673+00:00'
  last_success_at: '2026-10-24T13:43:29.782673+00:00'
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
  sic: '7374'
  sic_description: Services-Computer Processing & Data Preparation
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001527636.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/f974cdc6ffee05a6e0489d88d3e13c8eebf0b613/brain/companies/ATHM/README.md
full_history_commit: f974cdc6ffee05a6e0489d88d3e13c8eebf0b613
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# ATHM — Autohome Inc.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/f974cdc6ffee05a6e0489d88d3e13c8eebf0b613/brain/companies/ATHM/README.md)

## Business overview

Reported issuer name: **Autohome Inc.**. Stable SEC CIK: **0001527636**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| ATHM | NYSE | depositary_receipt | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 20-F, filed 2026-04-15, L458:

> This annual report contains forward-looking statements that reflect our current expectations and views of future events. The forward-looking statements are contained principally in the sections titled “Item 3. Key Information—D. Risk Factors,” “Item 4. Information on the Company—B. Business Overview” and “Item 5. Operating and Financial Review and Prospects.” These forward-looking statements are made under the “safe-harbor” provisions of the U.S. Private Securities Litigation Reform Act of 1995. Known and unknown risks, uncertainties and other factors, including those listed under “Item 3. Key Information—D. Risk Factors,” may cause our actual results, performance or achievements to be materially different from those expressed or implied by the forward-looking statements. [S54]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 20-F, filed 2026-04-15, L503:

> If the PRC government finds that the agreements that establish the structure for operating our services in China do not comply with PRC governmental restrictions on foreign investment in internet businesses, or if these regulations or the interpretation of existing regulations change in the future, we may face significant adverse consequences to our business operations and corporate structure. Our holding company, our China subsidiaries and the VIEs, and investors of our company face uncertainty about potential future actions by the PRC government that could affect the enforceability of the contractual arrangements with the VIEs and, consequently, significantly affect the financial performance of the VIEs and our company as a whole. For a detailed description of the risks associated with our corporate structure, please refer to risks disclosed under “Item 3. Key Information—D. Risk Factors—Risks Related to Our Corporate Structure.” [S54]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 20-F, filed 2026-04-15, L4621:

> In addition, one element of our growth strategy is to expand our services to customers. As a result, we have added additional services in the past few years. To serve our dealer customers, we had local sales and service representatives covering 134 cities across mainland China as of December 31, 2025. We intend to increase our penetration in existing dealer advertising and subscription services markets. We have implemented business strategies to further monetize our large dealer network by enlarging the offering of products and services with new technologies on our dealer digital platform, increasing the average spending of our existing dealer subscribers and upselling our dealership packages for our leads generation services. In order to increase the average spending of our existing dealer subscribers, we keep close communications and negotiations with relevant parties such as dealers, dealer groups and automakers. However, we may not succeed in making our customers sufficiently aware of existing and future services or in creating customer acceptance of these services at the prices we would like to charge, and we cannot guarantee that our pricing strategy and measures will always be agreed and accepted by any and all of our customers. We may not be able to achieve the market acceptance of our products and services as we expect and thus may fail to achieve an increase from our … [S54]

## Industry and value chain

SEC-reported SIC **7374**: Services-Computer Processing & Data Preparation. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 20-F, filed 2026-04-15, L5178:

> Governance. In 2025, 100% of our directors and employees completed integrity training, reinforcing our zero-tolerance stance on corruption. We actively encourage suppliers and business partners to conduct their activities with honesty, integrity, self-discipline, and in full compliance with applicable laws. Accordingly, 100% of our suppliers and business partners signed the Commitment on Integrity (Anti-Corruption and Anti-Bribery) during the year. [S54]

Navigation sector: **information-technology**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 20-F, filed 2026-04-15, L4545:

> We face significant competition, and if we fail to compete effectively, we may lose market share and our business, prospects and results of operations may be materially and adversely affected. [S54]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 20-F, filed 2026-04-15, L4728:

> We and our directors and officers may be subject to claims, suits, and government investigations involving competition, intellectual property, privacy, consumer protection, tax, fiduciary duty, labor and employment, commercial disputes, advertisements and content placed on our websites and mobile applications, and other matters. Our business may also face intellectual property infringement claims, as further discussed elsewhere in this annual report, that expose us to the risk of reputation damage. Such claims, suits, and government investigations are inherently uncertain and their results cannot be predicted with certainty. Regardless of the outcome, any of these types of legal proceedings can have an adverse impact on us and our directors and officers due to the legal costs, diversion of management resources, negative publicity and other factors involved therein. It is possible that one or more of such proceedings could result in substantial fines and penalties that could adversely affect our business. [S54]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 20-F, filed 2026-04-15, L4605:

> The markets for our services are highly competitive. With respect to our auto media and leads generation businesses, we face competition from China’s automotive vertical websites and mobile applications, such as BitAuto, Dongchedi, Xcar and PCauto, from the automotive channels of major internet portals, such as Sina and Sohu, and from companies engaged in mobile social media, news, video and live-streaming applications. We may also face competition from online platforms that are engaged in automobile transaction services, such as Meituan, JD.com, Uxin, Guazi and Renrenche as we develop our new car and used car transaction businesses. Our auto finance business faces competition from other auto finance companies, such as Yixin and Souche. In addition, we also face competition from companies engaged in social media business, such as ByteDance and Tencent, companies engaged in data product offering, such as BitAuto and Dongchedi, and companies engaged in AI and big data technologies. We may also face competition from mobile applications of automakers as some automakers explore to connect with users directly. As we expand our involvement in automotive transactions and establish a network of franchised offline stores, some automakers and dealers may also view us as a competitor in these regional markets. Competition with these and other websites and mobile applications is primarily … [S54]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 20-F, filed 2026-04-15, L118:

> Indicate by check mark whether any of those error corrections are restatements that required a recovery analysis of incentive-based compensation received by any of the registrant’s executive officers during the relevant recovery period pursuant to § 240.10D-1(b). ☐ [S54]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 20-F, filed 2026-04-15, L458:

> This annual report contains forward-looking statements that reflect our current expectations and views of future events. The forward-looking statements are contained principally in the sections titled “Item 3. Key Information—D. Risk Factors,” “Item 4. Information on the Company—B. Business Overview” and “Item 5. Operating and Financial Review and Prospects.” These forward-looking statements are made under the “safe-harbor” provisions of the U.S. Private Securities Litigation Reform Act of 1995. Known and unknown risks, uncertainties and other factors, including those listed under “Item 3. Key Information—D. Risk Factors,” may cause our actual results, performance or achievements to be materially different from those expressed or implied by the forward-looking statements. [S54]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 144, 20-F, 3, 4, 424B3, 424B4, 424B5, 6-K, 8-A12B, CERTNYS, CORRESP, CT ORDER, DRS, DRS/A, EFFECT, F-1, F-1/A, F-3ASR, F-6, FWP, IRANNOTICE, S-8, SC 13D, SC 13D/A, SC 13G, SC 13G/A, SCHEDULE 13D, SCHEDULE 13D/A, SCHEDULE 13G, SCHEDULE 13G/A, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:33:55.504603+00:00.

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
| 2026-10-23 | 6-K | 0001193125-26-429429 | — | [S03] |
| 2026-10-14 | 6-K | 0001193125-26-421013 | — | [S04] |
| 2026-10-01 | 4 | 0001976012-26-000008 | — | [S05] |
| 2026-10-01 | 4 | 0001975515-26-000006 | — | [S06] |
| 2026-10-01 | 4 | 0001975234-26-000008 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-27T15:25:35.250901+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001527636.json) — published not supplied; retrieved 2026-10-24T13:22:51.759433+00:00.

[S03] [6-K 0001193125-26-429429](https://www.sec.gov/Archives/edgar/data/1527636/000119312526429429/0001193125-26-429429-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S04] [6-K 0001193125-26-421013](https://www.sec.gov/Archives/edgar/data/1527636/000119312526421013/0001193125-26-421013-index.html) — published 2026-10-14; retrieved 2026-10-24T13:22:51.759433+00:00.

[S05] [4 0001976012-26-000008](https://www.sec.gov/Archives/edgar/data/1527636/000197601226000008/0001976012-26-000008-index.html) — published 2026-10-01; retrieved 2026-10-24T13:22:51.759433+00:00.

[S06] [4 0001975515-26-000006](https://www.sec.gov/Archives/edgar/data/1527636/000197551526000006/0001975515-26-000006-index.html) — published 2026-10-01; retrieved 2026-10-24T13:22:51.759433+00:00.

[S07] [4 0001975234-26-000008](https://www.sec.gov/Archives/edgar/data/1527636/000197523426000008/0001975234-26-000008-index.html) — published 2026-10-01; retrieved 2026-10-24T13:22:51.759433+00:00.

[S54] [20-F 0001193125-26-155932](https://www.sec.gov/Archives/edgar/data/1527636/000119312526155932/athm-20251231.htm) — published 2026-04-15; retrieved 2026-10-24T13:48:50.004948+00:00.

Source release: `coverage-20261027-40530587641-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/f974cdc6ffee05a6e0489d88d3e13c8eebf0b613/brain/companies/ATHM/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
