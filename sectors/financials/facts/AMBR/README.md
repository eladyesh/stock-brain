---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001697818
cik: 0001697818
company_name: Amber International Holding Ltd
tickers:
- AMBR
status: stub
canonical_reviewed: false
as_of: '2026-10-24'
updated_at: '2026-10-24T13:37:20.730682+00:00'
reviewed_at: null
coverage_release: coverage-20261024-40097864335-1
source_commit: 88540b30f4be3c56b6c7fa8ba3dede59893b9834
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
  - '3'
  - '4'
  - 424B3
  - 424B4
  - 424B5
  - 6-K
  - 8-A12B
  - CERT
  - CORRESP
  - DEL AM
  - DRS
  - DRS/A
  - DRSLTR
  - EFFECT
  - F-1
  - F-1/A
  - F-3
  - F-3ASR
  - F-3MEF
  - F-6
  - F-6 POS
  - F-6EF
  - FWP
  - NT 20-F
  - RW
  - S-8
  - SC 13D
  - SC 13D/A
  - SC 13E3
  - SC 13E3/A
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13D
  - SCHEDULE 13D/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001697818.json
    sha256: 33e57f75548c5f4bff25cf5c64eb4bf229da1a2c2ba7a97f6fe74f36e0c5de18
    retrieved_at: '2026-10-24T13:22:51.759433+00:00'
    archive: &id001
      member: CIK0001697818.json
      sha256: 593fbbea6512ef5ec729a5e513c465fbedaac8a66602c0abe00d0ba5a4d18732
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: nasdaqlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt
  published_at: null
  retrieved_at: '2026-10-24T13:23:32.568444+00:00'
  sha256: 59ac9b74ff663c6de40f5c93a54d5e12eb3fbef74f82e8a7cfc1456ad9f969ec
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001697818.json
  published_at: null
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 33e57f75548c5f4bff25cf5c64eb4bf229da1a2c2ba7a97f6fe74f36e0c5de18
- id: S03
  title: 6-K 0001104659-26-118256
  url: https://www.sec.gov/Archives/edgar/data/1697818/000110465926118256/0001104659-26-118256-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S04
  title: 6-K 0001104659-26-115742
  url: https://www.sec.gov/Archives/edgar/data/1697818/000110465926115742/0001104659-26-115742-index.html
  published_at: '2026-10-14'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S05
  title: 6-K 0001104659-26-111204
  url: https://www.sec.gov/Archives/edgar/data/1697818/000110465926111204/0001104659-26-111204-index.html
  published_at: '2026-09-28'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S06
  title: 6-K 0001104659-26-106504
  url: https://www.sec.gov/Archives/edgar/data/1697818/000110465926106504/0001104659-26-106504-index.html
  published_at: '2026-09-10'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S07
  title: 6-K 0001104659-26-104924
  url: https://www.sec.gov/Archives/edgar/data/1697818/000110465926104924/0001104659-26-104924-index.html
  published_at: '2026-09-03'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S54
  url: https://www.sec.gov/Archives/edgar/data/1697818/000110465926060362/ambr-20251231x20f.htm
  title: 20-F 0001104659-26-060362
  published_at: '2026-05-13'
  retrieved_at: '2026-10-24T13:46:00.374223+00:00'
  sha256: bff3ef9d379b0f7abe20e933230aab9ec47cfbeb9a73f16c30b7c92e5e7cbc63
issuer_classification:
  cik: 0001697818
  classification_status: reported_sic
  entity_type: other
  name: Amber International Holding Ltd
  sic: '6199'
  sic_description: Finance Services
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 33e57f75548c5f4bff25cf5c64eb4bf229da1a2c2ba7a97f6fe74f36e0c5de18
  url: https://data.sec.gov/submissions/CIK0001697818.json
listings:
- ticker: AMBR
  exchange: NASDAQ
  instrument_type: depositary_receipt
research_filings:
- accession: 0001104659-26-060362
  filed: '2026-05-13'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1697818/000110465926060362/0001104659-26-060362-index.html
- accession: 0001104659-23-112704
  filed: '2023-10-31'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1697818/000110465923112704/0001104659-23-112704-index.html
- accession: 0001193125-18-187354
  filed: '2018-06-08'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1697818/000119312518187354/0001193125-18-187354-index.html
- accession: 0001104659-26-118256
  filed: '2026-10-23'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1697818/000110465926118256/0001104659-26-118256-index.html
research_progress:
  stage: evidence_collected
  input_sha256: c38be4cb128382bd0b877ed3be1cd7dd3daa493b7f318524877fff26220685b4
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
  - revenue-model-and-segments
  - risks-and-thesis-breakers
  derived_observations: 0
  model_draft: false
  reviewed: false
sector_assignment:
  sector: financials
  method: project_sic_rule
  sic: '6199'
  sic_description: Finance Services
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001697818.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/aad7b261e69b9f214b9c5e20228523ca644ed670/brain/companies/AMBR/README.md
full_history_commit: aad7b261e69b9f214b9c5e20228523ca644ed670
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# AMBR — Amber International Holding Ltd

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/aad7b261e69b9f214b9c5e20228523ca644ed670/brain/companies/AMBR/README.md)

## Business overview

Reported issuer name: **Amber International Holding Ltd**. Stable SEC CIK: **0001697818**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| AMBR | NASDAQ | depositary_receipt | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 20-F, filed 2026-05-13, L485:

> During the reporting period, we provided institutional crypto financial services and solutions operating under the brand name “Amber Premium”. We optimized our business to drive returns to the shareholders through proactive monitoring our operations and market trends. As of the end of 2025, certain operations under iClick were classified as held-for-sale, and we completed one of the disposals in October 2025. The disposed business was deconsolidated from the Group upon the respective disposal and the results of the held-for-sale and disposed businesses are reflected in the Group’s consolidated financial statements included in this annual report as discontinued operations accordingly. See Note 5 to the financial statements included elsewhere in this annual report. [S54]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 20-F, filed 2026-05-13, L1889:

> Web3 Tools – We use state-of-the-art blockchain security measures, including advanced encryption, cold and hot wallet storage solutions and multi-factor authentication. This robust infrastructure ensures the safety of client assets and personal data, positioning us as a trusted player in the digital asset industry. AI and Data Analytics – We utilize artificial intelligence and advanced data analytics to enhance our investment strategies and risk management processes. For instance, MIA, our first in-house developed AI agent, has been deployed externally for content generation, social media consistency, and investor engagement, and internally as a proactive workspace assistant accelerating workflows via a proprietary skill hub and secure internal database. In addition, we are actively developing the A-Suite, a cohesive architecture of three AI-native operating systems designed not only to power businesses such as Amber Premium but also to intelligently coordinate liquidity, yield management and asset distribution at scale. In the first quarter of 2026, we expect to officially announce the first of these three operating systems: an AI-native autonomous workflow engine for digital asset liquidity management. Over time, we anticipate that the A-Suite will unlock new, scalable revenue streams and significantly enhance our operating leverage in the periods following its launch. [S54]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 20-F, filed 2026-05-13, L629:

> If we cannot keep pace with rapid industry changes to provide new and innovative products and services, the use of our products and services, and consequently our revenue, could decline, which could adversely impact our business, operating results, and financial condition. [S54]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 20-F, filed 2026-05-13, L1077:

> We are actively exploring and developing initiatives related to AI as part of our growth strategy. For instance, MIA, our first in-house developed AI agent, has been deployed externally for content generation, social media consistency, and investor engagement, and internally as a proactive workspace assistant accelerating workflows via a proprietary skill hub and secure internal database. We intend to leverage AI technologies to enhance our investment strategies and risk management processes. AI has been developing at a rapid pace, and continues to evolve and change. If we are unable to keep up with the changing AI landscape or in developing services to meet our customers’ evolving AI needs, or if the AI landscape does not develop to the extent we expect, our business, operating results, financial condition, and future prospects may be adversely impacted. Additionally, we may incur significant costs and experience significant delays in developing new products and services to adapt to the changing AI landscape, and may not achieve a return on investment or capitalize on the opportunities presented by demand for AI solutions. Moreover, while AI adoption is likely to continue and may accelerate, the long-term trajectory of this technological trend is uncertain, and market acceptance, understanding, and valuation of solutions and services that incorporate AI technologies are … [S54]

## Industry and value chain

SEC-reported SIC **6199**: Finance Services. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 20-F, filed 2026-05-13, L2032:

> In addition, the online marketing technology market is highly competitive, fragmented and rapidly changing. We mainly compete with online marketing technology companies that offer marketing solutions through demand side platform and use advanced technologies to optimize marketing campaigns for marketers. We compete for content distribution opportunities based on our ability to maximize the value for content distribution channels partners, provide them with a wide array of solutions covering various types of content distribution opportunities and our ability to increase fill rates. We also face competitive pressure from large and well-established internet companies and marketing agencies. With respect to our enterprise solutions, our competitors include local cloud-based commerce and marketing service providers and international SaaS companies. [S54]

Navigation sector: **financials**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 20-F, filed 2026-05-13, L785:

> increased competition from other payment services or other digital assets that exhibit better speed, security, scalability, or other characteristics; [S54]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 20-F, filed 2026-05-13, L857:

> Our brand and reputation are key assets and a competitive advantage, and maintaining a strong brand and reputation will be an important factor in the success and the development of our business. Protecting and enhancing our brand depends largely on the success of our marketing efforts, our ability to provide consistent, high-quality, and secure products, services, features, and support, and our ability to successfully secure, maintain and defend our rights to use our corporate names, logos, and other trademarks important to our brand. Thus, maintaining, protecting, and enhancing our reputation is also important to our development plans and relationships with our partners and counterparties. Furthermore, we believe that the importance of our brand and reputation may increase as competition in both the traditional financial services industry and the digital asset industry further intensifies. Our brand and reputation could be harmed if we fail to achieve these objectives or if our public image were to be tarnished by negative publicity, unexpected events, or actions by third parties. Unfavorable publicity regarding, for example, the quality of or changes to our products and services, litigation or regulatory activity, privacy practices, data security compromises or breaches, terms of service, employment matters, the use of our products, services, or supported digital assets for … [S54]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 20-F, filed 2026-05-13, L904:

> As we continue to expand our business worldwide, we have become increasingly obligated to comply with the laws, rules, regulations, policies, and legal interpretations of both the jurisdictions in which we operate and those into which we offer services on a cross-border basis. For instance, financial regulators outside the United States have increased their scrutiny of digital asset exchanges over time. Moreover, laws regulating financial services, the internet, mobile technologies, digital assets, AI, and related technologies outside of the United States are highly evolving, extensive and often impose different, more specific, or even conflicting obligations on us, as well as broader liability. In addition, it is required to comply with laws and regulations related to economic sanctions and export controls enforced by the U.S. Department of the Treasury’s Office of Foreign Assets Control (“OFAC”), the U.S. Department of Commerce’s Bureau of Industry and Security, and U.S. anti-money laundering and counter-terrorist financing laws and regulations, enforced by FinCEN and certain state financial services regulators. U.S. sanctions and export control laws and regulations generally restrict dealings by persons subject to U.S. jurisdiction with certain jurisdictions that are the target of comprehensive embargoes, as well as with persons, entities, and governments identified on … [S54]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 20-F, filed 2026-05-13, L138:

> Indicate by check mark whether any of those error corrections are restatements that required a recovery analysis of incentive-based compensation received by any of the registrant’s executive officers during the relevant recovery period pursuant to §240.10D-1(b). ☐ [S54]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 20-F, filed 2026-05-13, L529:

> You should read this annual report and the documents that we refer to in this annual report and have filed as exhibits to this annual report completely and with the understanding that our actual future results may be materially different from what we expect. Other sections of this annual report discuss factors which could adversely impact our business and financial performance. Moreover, we operate in an evolving environment. New risk factors emerge from time to time and it is not possible for our management to predict all risk factors, nor can we assess the impact of all factors on our business or the extent to which any factor, or combination of factors, may cause actual results to differ materially from those contained in any forward-looking statements. We qualify all of our forward-looking statements by these cautionary statements. [S54]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 144, 20-F, 20-F/A, 3, 4, 424B3, 424B4, 424B5, 6-K, 8-A12B, CERT, CORRESP, DEL AM, DRS, DRS/A, DRSLTR, EFFECT, F-1, F-1/A, F-3, F-3ASR, F-3MEF, F-6, F-6 POS, F-6EF, FWP, NT 20-F, RW, S-8, SC 13D, SC 13D/A, SC 13E3, SC 13E3/A, SC 13G, SC 13G/A, SCHEDULE 13D, SCHEDULE 13D/A, SCHEDULE 13G, SCHEDULE 13G/A, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:35:06.155343+00:00.

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
| 2026-10-23 | 6-K | 0001104659-26-118256 | — | [S03] |
| 2026-10-14 | 6-K | 0001104659-26-115742 | — | [S04] |
| 2026-09-28 | 6-K | 0001104659-26-111204 | — | [S05] |
| 2026-09-10 | 6-K | 0001104659-26-106504 | — | [S06] |
| 2026-09-03 | 6-K | 0001104659-26-104924 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-24T13:23:32.568444+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001697818.json) — published not supplied; retrieved 2026-10-24T13:22:51.759433+00:00.

[S03] [6-K 0001104659-26-118256](https://www.sec.gov/Archives/edgar/data/1697818/000110465926118256/0001104659-26-118256-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S04] [6-K 0001104659-26-115742](https://www.sec.gov/Archives/edgar/data/1697818/000110465926115742/0001104659-26-115742-index.html) — published 2026-10-14; retrieved 2026-10-24T13:22:51.759433+00:00.

[S05] [6-K 0001104659-26-111204](https://www.sec.gov/Archives/edgar/data/1697818/000110465926111204/0001104659-26-111204-index.html) — published 2026-09-28; retrieved 2026-10-24T13:22:51.759433+00:00.

[S06] [6-K 0001104659-26-106504](https://www.sec.gov/Archives/edgar/data/1697818/000110465926106504/0001104659-26-106504-index.html) — published 2026-09-10; retrieved 2026-10-24T13:22:51.759433+00:00.

[S07] [6-K 0001104659-26-104924](https://www.sec.gov/Archives/edgar/data/1697818/000110465926104924/0001104659-26-104924-index.html) — published 2026-09-03; retrieved 2026-10-24T13:22:51.759433+00:00.

[S54] [20-F 0001104659-26-060362](https://www.sec.gov/Archives/edgar/data/1697818/000110465926060362/ambr-20251231x20f.htm) — published 2026-05-13; retrieved 2026-10-24T13:46:00.374223+00:00.

Source release: `coverage-20261024-40097864335-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/aad7b261e69b9f214b9c5e20228523ca644ed670/brain/companies/AMBR/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
