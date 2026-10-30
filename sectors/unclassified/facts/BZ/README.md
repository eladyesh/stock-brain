---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001842827
cik: 0001842827
company_name: Kanzhun Ltd
tickers:
- BZ
status: stub
canonical_reviewed: false
as_of: '2026-10-30'
updated_at: '2026-10-30T16:05:25.650854+00:00'
reviewed_at: null
coverage_release: coverage-20261030-41085569265-1
source_commit: f9a34108789a82bf7c75f9d65a0e9552aa5552db
financial_history_available: false
curated_research: null
financial_gap:
  reason: foreign_reporting_adapter
  next_action: Add support for the observed 20-F, 40-F or 6-K reporting forms and
    verify the actual accounting taxonomy before normalization.
  observed_forms:
  - '144'
  - 144/A
  - 20-F
  - '3'
  - 3/A
  - '4'
  - 424B3
  - 424B4
  - 424B5
  - 6-K
  - 6-K/A
  - 8-A12B
  - CERT
  - CORRESP
  - DRS
  - DRS/A
  - DRSLTR
  - EFFECT
  - F-1
  - F-1/A
  - F-3ASR
  - F-6
  - F-6/A
  - FWP
  - S-8
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001842827.json
    sha256: caf59c4d74c9d5f55cfecfdb40015727b5b95ba28582ab8661df791986782133
    retrieved_at: '2026-10-24T13:22:51.759433+00:00'
    archive: &id001
      member: CIK0001842827.json
      sha256: 593fbbea6512ef5ec729a5e513c465fbedaac8a66602c0abe00d0ba5a4d18732
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: nasdaqlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt
  published_at: null
  retrieved_at: '2026-10-30T16:00:11.183681+00:00'
  sha256: 64301e84a89de015f12206ec26fa4a677c38e33277e47d0b3a6b91e370e8d274
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001842827.json
  published_at: null
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: caf59c4d74c9d5f55cfecfdb40015727b5b95ba28582ab8661df791986782133
- id: S03
  title: 6-K 0001104659-26-118472
  url: https://www.sec.gov/Archives/edgar/data/1842827/000110465926118472/0001104659-26-118472-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S04
  title: 6-K 0001104659-26-114353
  url: https://www.sec.gov/Archives/edgar/data/1842827/000110465926114353/0001104659-26-114353-index.html
  published_at: '2026-10-07'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S05
  title: 6-K 0001104659-26-113056
  url: https://www.sec.gov/Archives/edgar/data/1842827/000110465926113056/0001104659-26-113056-index.html
  published_at: '2026-10-02'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S06
  title: 6-K 0001104659-26-112318
  url: https://www.sec.gov/Archives/edgar/data/1842827/000110465926112318/0001104659-26-112318-index.html
  published_at: '2026-09-30'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S07
  title: 6-K 0001104659-26-109970
  url: https://www.sec.gov/Archives/edgar/data/1842827/000110465926109970/0001104659-26-109970-index.html
  published_at: '2026-09-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S54
  url: https://www.sec.gov/Archives/edgar/data/1842827/000110465926050959/bz-20251231x20f.htm
  title: 20-F 0001104659-26-050959
  published_at: '2026-04-29'
  retrieved_at: '2026-10-25T14:02:39.290075+00:00'
  sha256: 2f549f33324a4d52e0414b5b85a1ef45f9e494ee0379553fe9250ec441f171e9
issuer_classification:
  cik: 0001842827
  classification_status: reported_sic
  entity_type: other
  name: Kanzhun Ltd
  sic: '7370'
  sic_description: Services-Computer Programming, Data Processing, Etc.
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: caf59c4d74c9d5f55cfecfdb40015727b5b95ba28582ab8661df791986782133
  url: https://data.sec.gov/submissions/CIK0001842827.json
listings:
- ticker: BZ
  exchange: NASDAQ
  instrument_type: depositary_receipt
research_filings:
- accession: 0001104659-26-050959
  filed: '2026-04-29'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1842827/000110465926050959/0001104659-26-050959-index.html
- accession: 0001104659-26-118472
  filed: '2026-10-23'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1842827/000110465926118472/0001104659-26-118472-index.html
- accession: 0001104659-25-052623
  filed: '2025-05-27'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1842827/000110465925052623/0001104659-25-052623-index.html
research_progress:
  stage: evidence_collected
  input_sha256: eed3d2e29507400a34826ff22f808729fbaabb47ff88da1379ad454cc08e6abf
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
  sector: unclassified
  method: unresolved
  sic: '7370'
  sic_description: Services-Computer Programming, Data Processing, Etc.
  rule_version: 1
  reason: Missing, ambiguous or unmapped reported industry; company-specific review
    is required.
full_history_url: https://github.com/eladyesh/stock-brain/blob/1b4771bc41dec553e210323f72d9bfc908288c04/brain/companies/BZ/README.md
full_history_commit: 1b4771bc41dec553e210323f72d9bfc908288c04
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# BZ — Kanzhun Ltd

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/1b4771bc41dec553e210323f72d9bfc908288c04/brain/companies/BZ/README.md)

## Business overview

Reported issuer name: **Kanzhun Ltd**. Stable SEC CIK: **0001842827**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| BZ | NASDAQ | depositary_receipt | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 20-F, filed 2026-04-29, L581:

> \| \| ● \| our expectations regarding the prospects of our business model and demand for and market acceptance of our services; [S54]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 20-F, filed 2026-04-29, L14404:

> The Group has one operating and reportable segment mainly engaged in providing online recruitment services. The Group’s chief operating decision maker (“CODM”) is the Chief Executive Officer. The CODM assesses performance and determines resource allocation for the one operating segment based on the consolidated income from operations. The consolidated results regularly provided to the CODM include revenues, significant segment expenses and consolidated income from operations, which are consistent with those reported on the consolidated statements of comprehensive income. The CODM considers year-over-year fluctuations and budget-to-actual variances of these consolidated results when assessing performance and making operating decisions. The Group manages assets on a consolidated basis as reported on the consolidated balance sheets. Additionally, the Group’s long-lived assets are substantially located in the PRC and substantially all of the Group’s revenues are derived from entities within the PRC. [S54]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 20-F, filed 2026-04-29, L581:

> \| \| ● \| our expectations regarding the prospects of our business model and demand for and market acceptance of our services; [S54]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 20-F, filed 2026-04-29, L4467:

> Moreover, the U.S. has implemented policies restricting international trade and investment, such as tariffs, export controls, economic or trade sanctions, and foreign investment filing and approval requirements. These actions may materially and adversely affect international trade, global financial markets, and the stability of the global economic condition. For example, since early 2025, the United States has implemented significant changes to U.S. trade policy with China, including by imposing additional tariffs on Chinese imports. China has responded by imposing, and proposing to impose additional or higher tariffs on products imported from the United States, among other measures. There remain considerable uncertainties regarding future tariff rates and the trajectory of U.S.-China trade relations. Major developments in trade relations, including the imposition of new or increased tariffs by the U.S. and/or other countries could alter the trade environment and negatively affect the hiring demands of our customers which, in turn, could have an adverse effect on our financial condition and results of operations. Escalating U.S.-China tariff tensions have triggered a chain reaction of economic and political repercussions, potentially worsening bilateral relations. U.S. legislative and policy initiatives may impose stricter measures on China-based companies listed on U.S. … [S54]

## Industry and value chain

SEC-reported SIC **7370**: Services-Computer Programming, Data Processing, Etc.. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 20-F, filed 2026-04-29, L4584:

> We offer our online recruitment services through our online recruitment platform, an important component of which is our mobile applications. Our mobile applications are offered via app stores operated by third parties, such as Apple’s App Store and various Android app stores, which could suspend or terminate our users’ access to our mobile applications, increase access costs or change the terms of access in a way that makes our mobile applications less desirable or harder to access. As such, the promotion, distribution and operation of our mobile applications are subject to such distribution platforms’ standard terms and policies for application developers, which are subject to the interpretation of, and frequent changes by, these distribution channels. If Apple’s App Store or any Android app stores interpret or change their standard terms and conditions in a manner that is detrimental to us, or terminate their existing relationship with us, our business, financial condition and results of operations may be materially and adversely affected. In the future, it is possible that compliance requirements of app stores may cause us to suspend our mobile applications from such stores. As a result, our ability to expand our user base may be hindered if potential users experience difficulties in or are barred from accessing our mobile applications. Any such incident may adversely … [S54]

Navigation sector: **unclassified**. Method: `unresolved`. Missing, ambiguous or unmapped reported industry; company-specific review is required.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 20-F, filed 2026-04-29, L4397:

> \| \| ● \| We face significant competition in China’s dynamic online recruitment service market, potential market entries by established players from other industries and new technology-driven startups may further intensify competition. Our market share, financial condition and results of operations may be materially and adversely affected if we are unable to compete effectively. [S54]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 20-F, filed 2026-04-29, L4580:

> Our online recruitment platform and technology systems rely on software, including software developed or maintained internally and/or by third parties. In addition, our online recruitment platform and technology systems depend on the ability of such software to store and process large amount of data. The software on which we rely in the past has contained, and may now or in the future contain, undetected programming errors, bugs, or vulnerabilities. Some errors may only be discovered after the code has been released for external or internal use. Errors, vulnerabilities, or other design defects within the software on which we rely may result in a negative experience for users using our online recruitment platform, delay introductions of new features or enhancements, result in errors or compromise our ability to protect the data of our users and/or our intellectual property or lead to reductions in our ability to provide some or all of our services. In addition, any errors, bugs, vulnerabilities, or defects discovered in the software on which we rely, and any associated degradations or interruptions of service, could result in harm to our reputation and loss of users, which could adversely affect our business, financial condition and operating results. [S54]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 20-F, filed 2026-04-29, L4481:

> In 2023, 2024 and 2025, approximately 99% of our revenues were generated from enterprise customers. Enterprise customers are by far the most important source of revenue for us, and attracting more enterprise users to our online recruitment platform is therefore of critical importance to us. Due to their contribution to our revenues and ability to spend, large businesses with sufficient funds would benefit us most as a revenue source, and we need to invest in developing and promoting services that meet their needs. Additionally, SMEs can also be a source of enterprise user growth for us, as they have historically been underserved and usually lack direct access to a scaled user base and effective means to recruit widely. In order to expand our market reach to more small and mid-sized businesses, especially in less developed cities, we provide free or lower-fee services or subscription packages to them so they can take advantage of our online recruitment platform. We, however, cannot assure you that our efforts will convince more enterprise users to use our online recruitment platform. There is also no guarantee that our existing enterprise customers will continue to pay for our online recruitment services at the same frequency or price going forward, as competition or alternative means of job hunting may put pressure on the demand and pricing for our online recruitment services. … [S54]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 20-F, filed 2026-04-29, L182:

> Indicate by check mark whether any of those error corrections are restatements that required a recovery analysis of incentive- based compensation received by any of the registrant’s executive officers during the relevant recovery period pursuant to §240.10D-1(b). ☐ [S54]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 20-F, filed 2026-04-29, L589:

> You should read thoroughly this annual report and the documents that we refer to in this annual report and have filed as exhibits to this annual report completely and with the understanding that our actual future results may be materially different from and worse than what we expect. Other sections of this annual report discuss factors which could adversely impact our business and financial performance. Moreover, we operate in an evolving environment. New risk factors emerge from time to time and it is not possible for our management to predict all risk factors, nor can we assess the impact of all factors on our business or the extent to which any factor, or combination of factors, may cause actual results to differ materially from those contained in any forward-looking statements. We qualify all of our forward-looking statements by these cautionary statements. [S54]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 144, 144/A, 20-F, 3, 3/A, 4, 424B3, 424B4, 424B5, 6-K, 6-K/A, 8-A12B, CERT, CORRESP, DRS, DRS/A, DRSLTR, EFFECT, F-1, F-1/A, F-3ASR, F-6, F-6/A, FWP, S-8, SC 13G, SC 13G/A, SCHEDULE 13G, SCHEDULE 13G/A, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:36:05.185859+00:00.

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
| 2026-10-23 | 6-K | 0001104659-26-118472 | — | [S03] |
| 2026-10-07 | 6-K | 0001104659-26-114353 | — | [S04] |
| 2026-10-02 | 6-K | 0001104659-26-113056 | — | [S05] |
| 2026-09-30 | 6-K | 0001104659-26-112318 | — | [S06] |
| 2026-09-23 | 6-K | 0001104659-26-109970 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-30T16:00:11.183681+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001842827.json) — published not supplied; retrieved 2026-10-24T13:22:51.759433+00:00.

[S03] [6-K 0001104659-26-118472](https://www.sec.gov/Archives/edgar/data/1842827/000110465926118472/0001104659-26-118472-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S04] [6-K 0001104659-26-114353](https://www.sec.gov/Archives/edgar/data/1842827/000110465926114353/0001104659-26-114353-index.html) — published 2026-10-07; retrieved 2026-10-24T13:22:51.759433+00:00.

[S05] [6-K 0001104659-26-113056](https://www.sec.gov/Archives/edgar/data/1842827/000110465926113056/0001104659-26-113056-index.html) — published 2026-10-02; retrieved 2026-10-24T13:22:51.759433+00:00.

[S06] [6-K 0001104659-26-112318](https://www.sec.gov/Archives/edgar/data/1842827/000110465926112318/0001104659-26-112318-index.html) — published 2026-09-30; retrieved 2026-10-24T13:22:51.759433+00:00.

[S07] [6-K 0001104659-26-109970](https://www.sec.gov/Archives/edgar/data/1842827/000110465926109970/0001104659-26-109970-index.html) — published 2026-09-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S54] [20-F 0001104659-26-050959](https://www.sec.gov/Archives/edgar/data/1842827/000110465926050959/bz-20251231x20f.htm) — published 2026-04-29; retrieved 2026-10-25T14:02:39.290075+00:00.

Source release: `coverage-20261030-41085569265-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/1b4771bc41dec553e210323f72d9bfc908288c04/brain/companies/BZ/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
