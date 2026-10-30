---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001808110
cik: 0001808110
company_name: DDC Enterprise Ltd
tickers:
- DDC
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
  - 20-F
  - '3'
  - '4'
  - 424B3
  - 424B4
  - 6-K
  - 8-A12B
  - CERT
  - CORRESP
  - D
  - DRS
  - DRS/A
  - DRSLTR
  - EFFECT
  - F-1
  - F-1/A
  - F-3
  - F-3/A
  - FWP
  - NT 20-F
  - S-8
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001808110.json
    sha256: 790e67e87e0e4b54a737d6bb074c62e4b11061aabc91675c60c6e61dc900a2ce
    retrieved_at: '2026-10-24T13:22:51.759433+00:00'
    archive: &id001
      member: CIK0001808110.json
      sha256: 593fbbea6512ef5ec729a5e513c465fbedaac8a66602c0abe00d0ba5a4d18732
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: otherlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt
  published_at: null
  retrieved_at: '2026-10-30T16:00:12.358089+00:00'
  sha256: a960a0bfc5439fac9e467fe07ef1f44afe893ba2afc3297648321a80ce09971e
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001808110.json
  published_at: null
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 790e67e87e0e4b54a737d6bb074c62e4b11061aabc91675c60c6e61dc900a2ce
- id: S03
  title: 6-K 0001213900-26-112138
  url: https://www.sec.gov/Archives/edgar/data/1808110/000121390026112138/0001213900-26-112138-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S04
  title: 4 0001213900-26-101844
  url: https://www.sec.gov/Archives/edgar/data/1808110/000121390026101844/0001213900-26-101844-index.html
  published_at: '2026-09-21'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S05
  title: 6-K 0001213900-26-096455
  url: https://www.sec.gov/Archives/edgar/data/1808110/000121390026096455/0001213900-26-096455-index.html
  published_at: '2026-09-02'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S06
  title: S-8 0001213900-26-089486
  url: https://www.sec.gov/Archives/edgar/data/1808110/000121390026089486/0001213900-26-089486-index.html
  published_at: '2026-08-14'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S07
  title: 6-K 0001213900-26-075751
  url: https://www.sec.gov/Archives/edgar/data/1808110/000121390026075751/0001213900-26-075751-index.html
  published_at: '2026-07-07'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S53
  url: https://www.sec.gov/Archives/edgar/data/1808110/000121390026112138/ea0309121-6k_ddc.htm
  title: 6-K 0001213900-26-112138
  published_at: '2026-10-23'
  retrieved_at: '2026-10-26T16:24:13.532810+00:00'
  sha256: 2cbace3ca618997ffc355e072a4e5d121f29dc336f1ac9990d2244d36b16e1e6
- id: S54
  url: https://www.sec.gov/Archives/edgar/data/1808110/000121390026045881/ea0285722-20f_ddcenter.htm
  title: 20-F 0001213900-26-045881
  published_at: '2026-04-21'
  retrieved_at: '2026-10-26T16:24:11.469240+00:00'
  sha256: c7fb2467e19d4967a49ec1067c9118c62eb83c1efee60d75fc5d50960e578a44
issuer_classification:
  cik: 0001808110
  classification_status: reported_sic
  entity_type: other
  name: DDC Enterprise Ltd
  sic: '2000'
  sic_description: Food and Kindred Products
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 790e67e87e0e4b54a737d6bb074c62e4b11061aabc91675c60c6e61dc900a2ce
  url: https://data.sec.gov/submissions/CIK0001808110.json
listings:
- ticker: DDC
  exchange: NYSE_AMERICAN
  instrument_type: common_stock
research_filings:
- accession: 0001213900-26-045881
  filed: '2026-04-21'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1808110/000121390026045881/0001213900-26-045881-index.html
- accession: 0001213900-26-112138
  filed: '2026-10-23'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1808110/000121390026112138/0001213900-26-112138-index.html
research_progress:
  stage: evidence_collected
  input_sha256: ac2b753a30e9033657c7b445ed087c8710dfc2a55a52c1e1d1b54ac5ecb9450c
  last_attempt_at: '2026-10-26T16:22:31.694168+00:00'
  last_success_at: '2026-10-26T16:22:31.694168+00:00'
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
  sector: consumer-staples
  method: project_sic_rule
  sic: '2000'
  sic_description: Food and Kindred Products
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001808110.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/1b4771bc41dec553e210323f72d9bfc908288c04/brain/companies/DDC/README.md
full_history_commit: 1b4771bc41dec553e210323f72d9bfc908288c04
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# DDC — DDC Enterprise Ltd

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/1b4771bc41dec553e210323f72d9bfc908288c04/brain/companies/DDC/README.md)

## Business overview

Reported issuer name: **DDC Enterprise Ltd**. Stable SEC CIK: **0001808110**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| DDC | NYSE_AMERICAN | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 6-K, filed 2026-10-23, L43:

> Competition — The food and e-commerce industries in China are highly competitive. We compete with different competitors in each of our business lines. There are certain barriers to entry that have limited the number and success of foreign entrants, emerging, and traditional-cum-emerging brands, including our (i) brand awareness, (ii) E2E supply-chain visibility, (iii) strategic and preferred service agreements with product and distribution partners, (iv) product R&D and go-to-market capabilities, and (v) board of directors and advisory network. [S53]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 20-F, filed 2026-04-21, L5588:

> This acquisition was completed during the nation-wide lock down when the company expedited its strategy to diversify revenue streams and [S54]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 6-K, filed 2026-10-23, L28:

> We have an omni-channel (online and offline) sales, end-to-end (“E2E”) product development and distribution strategy. We have access to a network of direct-to-consumer (“D2C”) retail, wholesale Point-of-Sales (“POS”), and other corporate partnerships for the offline sale and distribution of our products. We continue to engage and grow our customer-base through curated and relevant video-content, product placement, and a customer-feedback informed product development and distribution strategy. [S53]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 20-F, filed 2026-04-21, L751:

> and logistics service expenditures. Benefiting from our deep engagement with our customers, we are in a good position to analyze consumers’ [S54]

## Industry and value chain

SEC-reported SIC **2000**: Food and Kindred Products. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 6-K, filed 2026-10-23, L71:

> The increase in total revenue was primarily driven by the expansion of our offline distribution channels and broader retail penetration across our culinary brand portfolio. The growth is attributable to our diversified and solid offline sales channels, which have been optimized and expanded continuously during the first half of 2026, including the increased number in regional distributors and strengthened cooperation with them, driving a steady rise in offline sales volume. [S53]

Navigation sector: **consumer-staples**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 6-K, filed 2026-10-23, L43:

> Competition — The food and e-commerce industries in China are highly competitive. We compete with different competitors in each of our business lines. There are certain barriers to entry that have limited the number and success of foreign entrants, emerging, and traditional-cum-emerging brands, including our (i) brand awareness, (ii) E2E supply-chain visibility, (iii) strategic and preferred service agreements with product and distribution partners, (iv) product R&D and go-to-market capabilities, and (v) board of directors and advisory network. [S53]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 6-K, filed 2026-10-23, L119:

> We regard our trademarks, copyrights, domain names, know-how, patents, and similar intellectual property as critical to our success, and we rely on a combination of intellectual property laws and contractual arrangements, including confidentiality and non-compete agreements with our employees and others, to protect our proprietary rights As of June 30, 2026, we had registered 279 trademarks, 1 copyright of works and 5 computer software copyrights in China, including three registered trademarks in Hong Kong. [S53]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 6-K, filed 2026-10-23, L27:

> We are a global Asian food platform and digital asset treasury company in China. We have strategically positioned Bitcoin as a core reserve asset while continuing to expand our portfolio of culinary brands. We are at the forefront of public companies integrating bitcoin into our financial architecture. We offer easy, convenient food. They reduce the time and energy needed to prepare a meal at home while never compromising on food safety, variety, and selection. [S53]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 6-K, filed 2026-10-23, L43:

> Competition — The food and e-commerce industries in China are highly competitive. We compete with different competitors in each of our business lines. There are certain barriers to entry that have limited the number and success of foreign entrants, emerging, and traditional-cum-emerging brands, including our (i) brand awareness, (ii) E2E supply-chain visibility, (iii) strategic and preferred service agreements with product and distribution partners, (iv) product R&D and go-to-market capabilities, and (v) board of directors and advisory network. [S53]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 20-F, filed 2026-04-21, L241:

> titled “Risk Factors” for a discussion of important factors that may cause our actual results to differ materially from those [S54]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 20-F, 3, 4, 424B3, 424B4, 6-K, 8-A12B, CERT, CORRESP, D, DRS, DRS/A, DRSLTR, EFFECT, F-1, F-1/A, F-3, F-3/A, FWP, NT 20-F, S-8, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:35:45.156970+00:00.

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
| 2026-10-23 | 6-K | 0001213900-26-112138 | — | [S03] |
| 2026-09-21 | 4 | 0001213900-26-101844 | — | [S04] |
| 2026-09-02 | 6-K | 0001213900-26-096455 | — | [S05] |
| 2026-08-14 | S-8 | 0001213900-26-089486 | — | [S06] |
| 2026-07-07 | 6-K | 0001213900-26-075751 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-30T16:00:12.358089+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001808110.json) — published not supplied; retrieved 2026-10-24T13:22:51.759433+00:00.

[S03] [6-K 0001213900-26-112138](https://www.sec.gov/Archives/edgar/data/1808110/000121390026112138/0001213900-26-112138-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S04] [4 0001213900-26-101844](https://www.sec.gov/Archives/edgar/data/1808110/000121390026101844/0001213900-26-101844-index.html) — published 2026-09-21; retrieved 2026-10-24T13:22:51.759433+00:00.

[S05] [6-K 0001213900-26-096455](https://www.sec.gov/Archives/edgar/data/1808110/000121390026096455/0001213900-26-096455-index.html) — published 2026-09-02; retrieved 2026-10-24T13:22:51.759433+00:00.

[S06] [S-8 0001213900-26-089486](https://www.sec.gov/Archives/edgar/data/1808110/000121390026089486/0001213900-26-089486-index.html) — published 2026-08-14; retrieved 2026-10-24T13:22:51.759433+00:00.

[S07] [6-K 0001213900-26-075751](https://www.sec.gov/Archives/edgar/data/1808110/000121390026075751/0001213900-26-075751-index.html) — published 2026-07-07; retrieved 2026-10-24T13:22:51.759433+00:00.

[S53] [6-K 0001213900-26-112138](https://www.sec.gov/Archives/edgar/data/1808110/000121390026112138/ea0309121-6k_ddc.htm) — published 2026-10-23; retrieved 2026-10-26T16:24:13.532810+00:00.

[S54] [20-F 0001213900-26-045881](https://www.sec.gov/Archives/edgar/data/1808110/000121390026045881/ea0285722-20f_ddcenter.htm) — published 2026-04-21; retrieved 2026-10-26T16:24:11.469240+00:00.

Source release: `coverage-20261030-41085569265-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/1b4771bc41dec553e210323f72d9bfc908288c04/brain/companies/DDC/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
