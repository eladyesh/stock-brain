---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001853717
cik: 0001853717
company_name: Atour Lifestyle Holdings Ltd
tickers:
- ATAT
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
  - '144'
  - 144/A
  - 20-F
  - '3'
  - '4'
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
  - F-1MEF
  - F-3ASR
  - S-8
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001853717.json
    sha256: 310f0f274add7b938313f2143486732993e865105405cb402c75f6a4fa608260
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001853717.json
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
  url: https://data.sec.gov/submissions/CIK0001853717.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 310f0f274add7b938313f2143486732993e865105405cb402c75f6a4fa608260
- id: S03
  title: SCHEDULE 13G 0001193125-26-422539
  url: https://www.sec.gov/Archives/edgar/data/1853717/000119312526422539/0001193125-26-422539-index.html
  published_at: '2026-10-15'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 4 0000950103-26-013589
  url: https://www.sec.gov/Archives/edgar/data/1853717/000095010326013589/0000950103-26-013589-index.html
  published_at: '2026-09-04'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 6-K 0001104659-26-098930
  url: https://www.sec.gov/Archives/edgar/data/1853717/000110465926098930/0001104659-26-098930-index.html
  published_at: '2026-08-20'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: SCHEDULE 13G/A 0001708574-26-000003
  url: https://www.sec.gov/Archives/edgar/data/1853717/000170857426000003/0001708574-26-000003-index.html
  published_at: '2026-08-14'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: SCHEDULE 13G/A 0001374170-26-000055
  url: https://www.sec.gov/Archives/edgar/data/1853717/000137417026000055/0001374170-26-000055-index.html
  published_at: '2026-08-12'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S54
  url: https://www.sec.gov/Archives/edgar/data/1853717/000110465926044551/atat-20251231x20f.htm
  title: 20-F 0001104659-26-044551
  published_at: '2026-04-17'
  retrieved_at: '2026-11-16T22:43:14.624950+00:00'
  sha256: 121e2980ecce41c4dee43fbd76f661e0ac8202bfc61ccfa927fe8ef5d99416c4
issuer_classification:
  cik: 0001853717
  classification_status: reported_sic
  entity_type: other
  name: Atour Lifestyle Holdings Ltd
  sic: '7011'
  sic_description: Hotels & Motels
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 310f0f274add7b938313f2143486732993e865105405cb402c75f6a4fa608260
  url: https://data.sec.gov/submissions/CIK0001853717.json
listings:
- ticker: ATAT
  exchange: NASDAQ
  instrument_type: depositary_receipt
research_filings:
- accession: 0001104659-26-044551
  filed: '2026-04-17'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1853717/000110465926044551/0001104659-26-044551-index.html
- accession: 0001104659-26-098930
  filed: '2026-08-20'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1853717/000110465926098930/0001104659-26-098930-index.html
- accession: 0001104659-25-082823
  filed: '2025-08-26'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1853717/000110465925082823/0001104659-25-082823-index.html
research_progress:
  stage: evidence_collected
  input_sha256: 1dc0f289f3047392023b064de70b56be5248496e1e97911c0167fa5f11a19156
  last_attempt_at: '2026-11-16T22:41:59.123544+00:00'
  last_success_at: '2026-11-16T22:41:59.123544+00:00'
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
  sector: consumer-discretionary
  method: project_sic_rule
  sic: '7011'
  sic_description: Hotels & Motels
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001853717.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/b9d67ef2f16565081e0df464efbaff4348778881/brain/companies/ATAT/README.md
full_history_commit: b9d67ef2f16565081e0df464efbaff4348778881
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# ATAT — Atour Lifestyle Holdings Ltd

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/b9d67ef2f16565081e0df464efbaff4348778881/brain/companies/ATAT/README.md)

## Business overview

Reported issuer name: **Atour Lifestyle Holdings Ltd**. Stable SEC CIK: **0001853717**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| ATAT | NASDAQ | depositary_receipt | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 20-F, filed 2026-04-17, L464:

> Our ability to pay dividends and to service any debt we may incur overseas largely depends upon dividends paid by our subsidiaries. If our subsidiaries incur debt on their own behalf in the future, the instruments governing their debt may restrict their ability to pay dividends to us. Our subsidiaries in China are permitted to pay dividends to us only out of their retained earnings, if any, as determined in accordance with the Accounting Standards for Business Enterprise as promulgated by the Ministry of Finance of the PRC, or the PRC GAAP. Pursuant to the laws and regulations applicable to China’s foreign investment enterprises, our subsidiaries that are foreign investment enterprises in the PRC have to make appropriation from their after-tax profit, as determined under PRC GAAP, to reserve funds including (i) general reserve fund, (ii) enterprise expansion fund and (iii) staff bonus and welfare fund. The appropriation to the general reserve fund must be at least 10% of the after-tax profits calculated in accordance with PRC GAAP. Appropriation is not required if the reserve fund has reached 50% of the registered capital of our subsidiary. Appropriations to the other two reserve funds are at our subsidiaries’ discretion. Our PRC subsidiaries did not make any contribution to the enterprise expansion fund or the staff and bonus welfare fund during the years ended December 31, … [S54]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 20-F, filed 2026-04-17, L12994:

> The Company has determined that it has one reporting unit, which is also its only reportable segment. [S54]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 20-F, filed 2026-04-17, L568:

> In addition, the retail industry in China is highly competitive. We compete with numerous home textile brands as well as the retail business of other hotel brands. Our competitors may have more financial, technical, marketing and other resources than we have, and may devote greater resources to develop, promote and support their products. They may also have more extensive industry relationships, longer operating histories and greater brand recognition than we have. As a result, these competitors may respond more quickly to consumer tastes and trends and introduce new products with designs that are more appealing to consumers. Moreover, our competitors may sell products at more competitive prices, which may create pricing pressure on us and negatively affect our profitability and competitive edge. In addition to existing competitors, the increasing use of digital technology, social media and the internet has lowered the barriers for new participants to enter our markets, which has broadened the array of companies we compete with. New participants can gain access to consumers and become a significant source of competition for our products in a very short period of time. [S54]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 20-F, filed 2026-04-17, L605:

> We have developed seven lifestyle hotel brands, covering the entire chain of midscale to luxury hotels with differentiated appeal to a wide range of guests. However, any new brands that we have launched or may launch in the future may not achieve anticipated returns. The development of a new brand requires significant upfront market research and accurate prediction of customer preferences, followed by development process that takes a considerable amount of time as well as significant sales and marketing activities and costs. We may not possess enough knowledge or experience in expanding into these new market segments and we may face more competition in such new market segments. We cannot assure you that our efforts in developing new hotel brands will be successful. If a new hotel brand is not well received by our customers, we may not be able to generate sufficient revenue to offset related costs and expenses, and our overall financial performance and condition may be adversely affected. [S54]

## Industry and value chain

SEC-reported SIC **7011**: Hotels & Motels. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 20-F, filed 2026-04-17, L575:

> In addition, our retail business may face challenges when we enter new markets, such as differences in consumer preferences, purchasing behavior and price sensitivity, which may require us to tailor our product offerings or pricing strategies accordingly. We may also encounter difficulties in building an effective supply chain and after-sales service network in a new market, especially where local infrastructure or logistics partners are underdeveloped. Furthermore, our retail brand awareness in new markets may be limited, requiring higher upfront investments in marketing and customer acquisition. We may also experience lower conversion rates or repurchase rates in new markets, as customers take longer to recognize and trust our brand and product quality compared to our existing markets where we have established a loyal customer base. Any of the foregoing may adversely affect our results of operations and financial condition. [S54]

Navigation sector: **consumer-discretionary**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 20-F, filed 2026-04-17, L566:

> The hospitality industry in China is highly competitive. Competition for guests and customers is primarily focused on hotel room rates, quality of accommodations, brand recognition, convenience of location, geographic coverage, quality and range of services, other lifestyle offerings, and guest amenities. We mainly compete with other branded and independent hotel operating companies, national and international hotel brands and ownership companies. In addition, we may face competition from new entrants in the hospitality industry in China or increased competition from competitors who are expanding rapidly. Such competitors include vacation rental online marketplace companies. New and existing competitors may offer more competitive rates, greater convenience, superior services or amenities, or superior facilities, possibly attracting guests away from our hotels and resulting in lower occupancy rate and ADR for our hotels. [S54]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 20-F, filed 2026-04-17, L715:

> Any failure to protect our trademarks, patents and other intellectual property rights could have a negative impact on our business. [S54]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 20-F, filed 2026-04-17, L466:

> In 2025, with cash generated from operating activities in the PRC by Atour Shanghai and its subsidiaries, Atour Shanghai distributed RMB800.0 million (US$114.4 million) to our Hong Kong subsidiary, Atour Hotel (HK) Holdings Limited, or Atour Hong Kong. Our subsidiaries in the PRC generate cash from operating activities, which may be reinvested in our business or used to fund share repurchases and dividend distributions. In the future, cash proceeds raised from overseas financing activities may be transferred by us through our Hong Kong subsidiaries to their respective PRC subsidiaries via capital contribution and shareholder loans, as the case may be. Subsequently, these PRC subsidiaries will transfer funds to their own subsidiaries to meet the capital needs of our business operations. For details about the applicable PRC rules that limit transfer of funds from overseas to our PRC subsidiaries, see “Item 3. Key Information — 3.D. Risk Factors — Risks Related to Doing Business in China — PRC regulation of loans to and direct investment in PRC entities by offshore holding companies and governmental regulation of currency conversion may restrict or delay us from using the proceeds of our initial public offering to make loans or additional capital contributions to our PRC subsidiaries, which could adversely affect our liquidity and our ability to fund and expand our business” and … [S54]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 20-F, filed 2026-04-17, L124:

> Indicate by check mark whether any of those error corrections are restatements that required a recovery analysis of incentive-based compensation received by any of the registrant’s executive officers during the relevant recovery period pursuant to § 240.10D-1(b). Yes ☐ No ☒ [S54]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 20-F, filed 2026-04-17, L436:

> Forward-looking statements appear in a number of places in this annual report and include, but are not limited to, statements regarding our intent, belief or current expectations. Forward-looking statements are based on our management’s beliefs and assumptions and on information currently available to our management. Such statements are subject to risks and uncertainties, and actual results may differ materially from those expressed or implied in the forward-looking statements due to various factors, including, but not limited to, those identified under the section entitled “Item 3. Key Information—3.D. Risk Factors” in this annual report. These risks and uncertainties include factors relating to: [S54]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 144, 144/A, 20-F, 3, 4, 424B4, 424B5, 6-K, 6-K/A, 8-A12B, CERT, CORRESP, DRS, DRS/A, DRSLTR, EFFECT, F-1, F-1/A, F-1MEF, F-3ASR, S-8, SC 13G, SC 13G/A, SCHEDULE 13G, SCHEDULE 13G/A, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:36:09.211116+00:00.

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
| 2026-10-15 | SCHEDULE 13G | 0001193125-26-422539 | — | [S03] |
| 2026-09-04 | 4 | 0000950103-26-013589 | — | [S04] |
| 2026-08-20 | 6-K | 0001104659-26-098930 | — | [S05] |
| 2026-08-14 | SCHEDULE 13G/A | 0001708574-26-000003 | — | [S06] |
| 2026-08-12 | SCHEDULE 13G/A | 0001374170-26-000055 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-11-01T16:07:03.070084+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001853717.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [SCHEDULE 13G 0001193125-26-422539](https://www.sec.gov/Archives/edgar/data/1853717/000119312526422539/0001193125-26-422539-index.html) — published 2026-10-15; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [4 0000950103-26-013589](https://www.sec.gov/Archives/edgar/data/1853717/000095010326013589/0000950103-26-013589-index.html) — published 2026-09-04; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [6-K 0001104659-26-098930](https://www.sec.gov/Archives/edgar/data/1853717/000110465926098930/0001104659-26-098930-index.html) — published 2026-08-20; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [SCHEDULE 13G/A 0001708574-26-000003](https://www.sec.gov/Archives/edgar/data/1853717/000170857426000003/0001708574-26-000003-index.html) — published 2026-08-14; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [SCHEDULE 13G/A 0001374170-26-000055](https://www.sec.gov/Archives/edgar/data/1853717/000137417026000055/0001374170-26-000055-index.html) — published 2026-08-12; retrieved 2026-10-23T08:33:02.691743+00:00.

[S54] [20-F 0001104659-26-044551](https://www.sec.gov/Archives/edgar/data/1853717/000110465926044551/atat-20251231x20f.htm) — published 2026-04-17; retrieved 2026-11-16T22:43:14.624950+00:00.

Source release: `coverage-20261101-41324509967-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/b9d67ef2f16565081e0df464efbaff4348778881/brain/companies/ATAT/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
