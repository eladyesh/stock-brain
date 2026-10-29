---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001940941
cik: 0001940941
company_name: mF International Ltd
tickers:
- MFI
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
  - 20-F
  - '3'
  - 424B4
  - 424B7
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
  - F-1MEF
  - F-3
  - F-3/A
  - F-3ASR
  - FWP
  - NT 20-F
  - SC 13G
  - SCHEDULE 13D
  - SCHEDULE 13D/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001940941.json
    sha256: d807e0a5508a707c9528ecb196416c5297cf30c3038261761570e333dc8c1ef6
    retrieved_at: '2026-10-24T13:22:51.759433+00:00'
    archive: &id001
      member: CIK0001940941.json
      sha256: 593fbbea6512ef5ec729a5e513c465fbedaac8a66602c0abe00d0ba5a4d18732
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: nasdaqlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt
  published_at: null
  retrieved_at: '2026-10-29T16:14:13.115716+00:00'
  sha256: 0695ffec283534755d4efe90771a9cacee840d7affb7ba717f62899195a301c6
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001940941.json
  published_at: null
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: d807e0a5508a707c9528ecb196416c5297cf30c3038261761570e333dc8c1ef6
- id: S03
  title: 6-K 0001493152-26-048234
  url: https://www.sec.gov/Archives/edgar/data/1940941/000149315226048234/0001493152-26-048234-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S04
  title: 6-K 0001628280-26-061240
  url: https://www.sec.gov/Archives/edgar/data/1940941/000162828026061240/0001628280-26-061240-index.html
  published_at: '2026-09-10'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S05
  title: 6-K 0001493152-26-039373
  url: https://www.sec.gov/Archives/edgar/data/1940941/000149315226039373/0001493152-26-039373-index.html
  published_at: '2026-08-20'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S06
  title: 20-F 0001628280-26-045993
  url: https://www.sec.gov/Archives/edgar/data/1940941/000162828026045993/0001628280-26-045993-index.html
  published_at: '2026-06-29'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S07
  title: 6-K 0001493152-26-025016
  url: https://www.sec.gov/Archives/edgar/data/1940941/000149315226025016/0001493152-26-025016-index.html
  published_at: '2026-05-22'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S54
  url: https://www.sec.gov/Archives/edgar/data/1940941/000162828026045993/mfi-20251231.htm
  title: 20-F 0001628280-26-045993
  published_at: '2026-06-29'
  retrieved_at: '2026-10-29T16:28:53.126354+00:00'
  sha256: 7f77726bff99c35ca8693be649f40a6b8c993ec986e932bc1d8a9b8791ccc69f
issuer_classification:
  cik: 0001940941
  classification_status: reported_sic
  entity_type: other
  name: mF International Ltd
  sic: '7371'
  sic_description: Services-Computer Programming Services
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: d807e0a5508a707c9528ecb196416c5297cf30c3038261761570e333dc8c1ef6
  url: https://data.sec.gov/submissions/CIK0001940941.json
listings:
- ticker: MFI
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001628280-26-045993
  filed: '2026-06-29'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1940941/000162828026045993/0001628280-26-045993-index.html
- accession: 0001493152-26-048234
  filed: '2026-10-23'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1940941/000149315226048234/0001493152-26-048234-index.html
- accession: 0001641172-25-010258
  filed: '2025-05-14'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1940941/000164117225010258/0001641172-25-010258-index.html
research_progress:
  stage: evidence_collected
  input_sha256: 80025d872e01b83ed0b9b7849bc1b04cc12a81a0ea8419ed82c69831d4517323
  last_attempt_at: '2026-10-29T16:24:48.518388+00:00'
  last_success_at: '2026-10-29T16:24:48.518388+00:00'
  next_retry_at: null
  source_set_current: true
  evidence_topics:
  - business-overview
  - competitive-landscape
  - customers-and-end-markets
  - growth-drivers
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
  source_url: https://data.sec.gov/submissions/CIK0001940941.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/c26f59bc72c00102d2490e95b07449f8cd848491/brain/companies/MFI/README.md
full_history_commit: c26f59bc72c00102d2490e95b07449f8cd848491
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# MFI — mF International Ltd

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/c26f59bc72c00102d2490e95b07449f8cd848491/brain/companies/MFI/README.md)

## Business overview

Reported issuer name: **mF International Ltd**. Stable SEC CIK: **0001940941**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| MFI | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 20-F, filed 2026-06-29, L377:

> On August 15, 2025, mF International Limited established two subsidiaries, CAT Strategy Limited, a Hong Kong limited liability company, and iBCH Inc., a British Virgin Islands limited liability company, to introduce investment management. As of the date of this annual report, we conduct our business operations through our Operating Subsidiaries in Hong Kong and the British Virgin Islands. [S54]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 20-F, filed 2026-06-29, L2640:

> In accordance with ASC 280, Segment Reporting, an operating segment is identified as a component of an enterprise of which separate financial information and operating results are available and regularly reviewed by the Company’s chief operating decision maker (“CODM”). The Company has one core operating and reportable segment with one business activity – sale of financial trading solutions via internet or platform to customers. The Company’s CODM is its Chief Executive Officer. The Company’s CODM reviews financial information presented on a consolidated basis. The CODM uses the consolidated income or loss from operations and net income (loss) to evaluate financial performance, make decisions and allocate resources. The CODM also reviews the functional expenses such as selling and marketing expenses, research and development expenses and general and administrative expenses at the consolidated level to manage the Company’s operation. The Company’s operation is located in Hong Kong and all of the Company’s management and employees physically reside in Hong Kong. The CODM does not use asset or liability information in assessing the Company’s operating segment. [S54]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 20-F, filed 2026-06-29, L407:

> Under the current practice of the Inland Revenue Department of Hong Kong, no tax is payable in Hong Kong in respect of dividends paid by us. As of the date of this annual report, there are no restrictions or limitations under the laws of Hong Kong imposed on the conversion of HK$ into foreign currencies and the remittance of currencies out of Hong Kong or across borders and to U.S investors. The laws and regulations of the PRC do not currently have any material impact on the transfer of cash from us to our Operating Subsidiaries or from our Operating Subsidiaries to us, our shareholders and U.S. investors. However, the Chinese government may, in the future, impose restrictions or limitations on our ability to transfer money out of Hong Kong, to distribute earnings and pay dividends to and from the other entities within our organization, or to reinvest in our business outside of Hong Kong. Such restrictions and limitations, if imposed in the future, may delay or hinder the expansion of our business outside of Hong Kong and may affect our ability to receive funds from the Operating Subsidiaries in Hong Kong. The promulgation of new laws or regulations, or the new interpretation of existing laws and regulations, in each case, that restrict or otherwise unfavorably impact the ability or way we or the Operating Subsidiaries conduct business, could require us to change certain … [S54]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 20-F, filed 2026-06-29, L644:

> as in the United States or other countries. Accordingly, we cannot predict the effect of future developments in the Hong Kong legal system, including the promulgation of new laws, changes to existing laws or the interpretation or enforcement thereof, or the preemption of local regulations by national laws. These uncertainties could limit the legal protections available to our Operating Subsidiaries, including their ability to enforce agreements with our customers. [S54]

## Industry and value chain

SEC-reported SIC **7371**: Services-Computer Programming Services. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **information-technology**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 20-F, filed 2026-06-29, L514:

> •increased competition from other payment services or other digital assets that exhibit better speed, security, scalability, or other characteristics; [S54]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 20-F, filed 2026-06-29, L638:

> However, if the PRC attempts to alter its agreement to allow Hong Kong to function autonomously, this could potentially impact Hong Kong’s common law legal system and may in turn bring about uncertainty in, for example, the enforcement of the contractual rights of our Operating Subsidiaries. This could, in turn, materially and adversely affect business and operations of our Operating Subsidiaries. Additionally, intellectual property rights and confidentiality protections in Hong Kong may not be as effective as in the United States or other countries. Accordingly, we cannot predict the effect of future developments in the Hong Kong legal system, including the promulgation of new laws, changes to existing laws or the interpretation or enforcement thereof, or the preemption of local regulations by national laws. These uncertainties could limit the legal protections available to us, including the ability to enforce agreements with the customers. [S54]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 20-F, filed 2026-06-29, L493:

> We expect that a large portion of our assets will be concentrated in our digital assets holdings. The concentration of our assets limits our ability to mitigate risk that could otherwise be achieved by holding a more diversified portfolio of treasury assets. Our digital treasury strategy has not been tested over an extended period of time or under different market conditions. We are continually examining the risks and rewards of our strategy to acquire and hold digital assets. This strategy has not been tested over an extended period of time or under different market conditions. For example, although we believe BCH has the potential to serve as a hedge against inflation in the long term, the short-term price of BCH declined in recent periods during which the inflation rate increased. If BCH prices were to decline or our digital treasury strategy otherwise proves unsuccessful, our financial condition, results of operations, and the market price of our listed securities would be materially adversely impacted. [S54]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 20-F, filed 2026-06-29, L62:

> Indicate by check mark whether any of those error corrections are restatements that required a recovery analysis of incentive based compensation received by any of the registrant’s executive officers during the relevant recovery period pursuant to §240.10D-1(b). o [S54]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 20-F, filed 2026-06-29, L396:

> performance and/or the value of our Class A Ordinary Shares or impair our ability to raise money. See “— D. Risk Factors —Risks Related to Our Corporate Structure — Substantially all of the Operating Subsidiaries’ operations are conducted in Hong Kong. However, due to the long arm provisions under the current PRC laws and regulations, the Chinese government may exercise significant oversight and discretion over the conduct of such business and may intervene in or influence such operations at any time, which could result in a material change in the operations of the Operating Subsidiaries and/or the value of our Class A Ordinary Shares. The PRC government may also intervene or impose restrictions on our ability to move money out of Hong Kong to distribute earnings and pay dividends or to reinvest in our business outside of Hong Kong. Changes in the policies, regulations, rules, and the enforcement of laws of the Chinese government may also occur quickly with little advance notice and our assertions and beliefs of the risk imposed by the PRC legal and regulatory system cannot be certain.” [S54]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 20-F, 3, 424B4, 424B7, 6-K, 6-K/A, 8-A12B, CERT, CORRESP, DRS, DRS/A, DRSLTR, EFFECT, F-1, F-1/A, F-1MEF, F-3, F-3/A, F-3ASR, FWP, NT 20-F, SC 13G, SCHEDULE 13D, SCHEDULE 13D/A, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:36:24.906758+00:00.

### Research work queue

Collection stage: **evidence_collected**. Extracted evidence is not a reviewed conclusion. Daily collection resumes from durable state; unchanged accessions are reused.

- **Business overview** (source excerpts available; assess the claim): Explain what the company does, who pays it, and why the business exists. Cite primary sources.
- **Revenue model and segments** (source excerpts available; assess the claim): Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.
- **Products and services** (source excerpts available; assess the claim): Describe the main products, customer problems solved, distribution, and product dependencies.
- **Customers and end markets** (source excerpts available; assess the claim): Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.
- **Industry and value chain** (evidence or analysis still needed): Place the company among suppliers, distribution channels, customers, and substitutes. Explain cyclicality and supply constraints.
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
| 2026-10-23 | 6-K | 0001493152-26-048234 | — | [S03] |
| 2026-09-10 | 6-K | 0001628280-26-061240 | — | [S04] |
| 2026-08-20 | 6-K | 0001493152-26-039373 | — | [S05] |
| 2026-06-29 | 20-F | 0001628280-26-045993 | — | [S06] |
| 2026-05-22 | 6-K | 0001493152-26-025016 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-29T16:14:13.115716+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001940941.json) — published not supplied; retrieved 2026-10-24T13:22:51.759433+00:00.

[S03] [6-K 0001493152-26-048234](https://www.sec.gov/Archives/edgar/data/1940941/000149315226048234/0001493152-26-048234-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S04] [6-K 0001628280-26-061240](https://www.sec.gov/Archives/edgar/data/1940941/000162828026061240/0001628280-26-061240-index.html) — published 2026-09-10; retrieved 2026-10-24T13:22:51.759433+00:00.

[S05] [6-K 0001493152-26-039373](https://www.sec.gov/Archives/edgar/data/1940941/000149315226039373/0001493152-26-039373-index.html) — published 2026-08-20; retrieved 2026-10-24T13:22:51.759433+00:00.

[S06] [20-F 0001628280-26-045993](https://www.sec.gov/Archives/edgar/data/1940941/000162828026045993/0001628280-26-045993-index.html) — published 2026-06-29; retrieved 2026-10-24T13:22:51.759433+00:00.

[S07] [6-K 0001493152-26-025016](https://www.sec.gov/Archives/edgar/data/1940941/000149315226025016/0001493152-26-025016-index.html) — published 2026-05-22; retrieved 2026-10-24T13:22:51.759433+00:00.

[S54] [20-F 0001628280-26-045993](https://www.sec.gov/Archives/edgar/data/1940941/000162828026045993/mfi-20251231.htm) — published 2026-06-29; retrieved 2026-10-29T16:28:53.126354+00:00.

Source release: `coverage-20261029-40909364006-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/c26f59bc72c00102d2490e95b07449f8cd848491/brain/companies/MFI/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
