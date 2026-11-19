---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001811216
cik: 0001811216
company_name: Baosheng Media Group Holdings Ltd
tickers:
- BAOS
status: stub
canonical_reviewed: false
as_of: '2026-11-01'
updated_at: '2026-11-01T16:11:48.803754+00:00'
reviewed_at: null
coverage_release: coverage-20261101-41324509967-1
source_commit: 107777182f87f961989f84e51ee16bb872074fdf
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
  - F-3
  - F-3/A
  - FWP
  - NT 20-F
  - S-8
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001811216.json
    sha256: faa198078bdd7e256fa2714ac17a8297c910b56af90616291c1ee4186b7311f1
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001811216.json
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
  url: https://data.sec.gov/submissions/CIK0001811216.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: faa198078bdd7e256fa2714ac17a8297c910b56af90616291c1ee4186b7311f1
- id: S03
  title: 6-K 0001104659-26-116640
  url: https://www.sec.gov/Archives/edgar/data/1811216/000110465926116640/0001104659-26-116640-index.html
  published_at: '2026-10-16'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: EFFECT 9999999995-26-003018
  url: https://www.sec.gov/Archives/edgar/data/1811216/999999999526003018/9999999995-26-003018-index.html
  published_at: '2026-09-21'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 6-K 0001104659-26-108972
  url: https://www.sec.gov/Archives/edgar/data/1811216/000110465926108972/0001104659-26-108972-index.html
  published_at: '2026-09-18'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: EFFECT 9999999995-26-002997
  url: https://www.sec.gov/Archives/edgar/data/1811216/999999999526002997/9999999995-26-002997-index.html
  published_at: '2026-09-17'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 6-K 0001104659-26-107944
  url: https://www.sec.gov/Archives/edgar/data/1811216/000110465926107944/0001104659-26-107944-index.html
  published_at: '2026-09-15'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S53
  url: https://www.sec.gov/Archives/edgar/data/1811216/000110465926116640/baos-20260630x6k.htm
  title: 6-K 0001104659-26-116640
  published_at: '2026-10-16'
  retrieved_at: '2026-11-19T21:13:17.496667+00:00'
  sha256: 8690e67017b074bd85b4e014dad2268e8c6d820a5d31f5ab86f0f7a88c46cfa2
- id: S54
  url: https://www.sec.gov/Archives/edgar/data/1811216/000110465926053161/baos-20251231x20f.htm
  title: 20-F 0001104659-26-053161
  published_at: '2026-04-30'
  retrieved_at: '2026-11-19T21:13:15.483110+00:00'
  sha256: 8bbb9d2e2336ebcd047f91435d9988cf709e275d03de7bc289111da92b9b7558
issuer_classification:
  cik: 0001811216
  classification_status: reported_sic
  entity_type: other
  name: Baosheng Media Group Holdings Ltd
  sic: '7389'
  sic_description: Services-Business Services, NEC
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: faa198078bdd7e256fa2714ac17a8297c910b56af90616291c1ee4186b7311f1
  url: https://data.sec.gov/submissions/CIK0001811216.json
listings:
- ticker: BAOS
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001104659-26-053161
  filed: '2026-04-30'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1811216/000110465926053161/0001104659-26-053161-index.html
- accession: 0001104659-26-116640
  filed: '2026-10-16'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1811216/000110465926116640/0001104659-26-116640-index.html
- accession: 0001104659-25-071173
  filed: '2025-07-28'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1811216/000110465925071173/0001104659-25-071173-index.html
- accession: 0001104659-23-100251
  filed: '2023-09-13'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1811216/000110465923100251/0001104659-23-100251-index.html
research_progress:
  stage: evidence_collected
  input_sha256: 98bc87a24d6ce7262ad3d0becfdff2e14e8bfb78b6460dccbc516c5ab9bf593c
  last_attempt_at: '2026-11-19T21:08:42.711300+00:00'
  last_success_at: '2026-11-19T21:08:42.711300+00:00'
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
  source_url: https://data.sec.gov/submissions/CIK0001811216.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/0f49b319f95dcee8e757e592a38a028a04a7bc3c/brain/companies/BAOS/README.md
full_history_commit: 0f49b319f95dcee8e757e592a38a028a04a7bc3c
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# BAOS — Baosheng Media Group Holdings Ltd

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/0f49b319f95dcee8e757e592a38a028a04a7bc3c/brain/companies/BAOS/README.md)

## Business overview

Reported issuer name: **Baosheng Media Group Holdings Ltd**. Stable SEC CIK: **0001811216**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| BAOS | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 20-F, filed 2026-04-30, L576:

> \| \| ● \| “authorized agency status” are to the qualification to serve as a designated agency for the media in identifying and procuring advertisers to purchase ad inventory from the media, facilitating the transaction process, and assisting ad deployment. See “Item 4. Information on the Company — B. Business Overview” in this annual report for more information on our authorized agency status with media. [S54]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 20-F, filed 2026-04-30, L13517:

> Since the Company operates in one reportable segment, all financial information required can be found in the consolidated financial statements. [S54]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 20-F, filed 2026-04-30, L704:

> \| \| ● \| Adverse changes in political and economic policies of the PRC government could have a material adverse effect on the overall economic growth of the PRC, which could reduce the demand for our products and materially and adversely affect our competitive position. [S54]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 20-F, filed 2026-04-30, L852:

> Our top five customers during the fiscal years 2025, 2024 and 2023 include search engine operators, short-video platform operators, and advertising agencies who place ads for their advertiser clients through us. The identities of our customers vary depending on the type of revenue and the nature of the business transaction, comprising both advertisers and publishers (or their authorized agencies). See “Item 4. Information on the Company - B. Business Overview - Customers.” For the fiscal year ended December 31, 2025, three customers, accounted for more than 10% of our total revenue, representing approximately 43.0% 19.3% and 16.6% of our total revenue, respectively. For the fiscal year ended December 31, 2024, three customers accounted for more than 10% of our total revenue, representing approximately 47.7%, 19.3% and 15.6% of our total revenue, respectively. For the fiscal year ended December 31, 2023, two customers accounted for more than 10% of our total revenue, representing approximately 47.7% and 12.2% of our total revenue, respectively. [S54]

## Industry and value chain

SEC-reported SIC **7389**: Services-Business Services, NEC. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 20-F, filed 2026-04-30, L1932:

> In-feed ads on various content distribution channels, including one of the most popular news portals and short-video apps in China. [S54]

Navigation sector: **industrials**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 20-F, filed 2026-04-30, L840:

> \| \| ● \| our ability to compete effectively with our competitors in the online advertising industry. [S54]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 20-F, filed 2026-04-30, L989:

> Unauthorized use of our intellectual property by third parties and expenses incurred in protecting our intellectual property rights may adversely affect our business, reputation and competitive edge. [S54]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 20-F, filed 2026-04-30, L730:

> Regardless of the merits of these proceedings, litigation and related disputes can be costly, time-consuming, and disruptive to our business. We have incurred substantial legal fees, expert and advisory costs, and other expenses, and these proceedings have diverted the attention of our management and key personnel from operating our business and executing our strategy. They may also result in adverse publicity and reputational harm, which could negatively affect our relationships with investors, customers, business partners and other stakeholders, and could contribute to volatility or a decline in the market price of our securities. [S54]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 20-F, filed 2026-04-30, L161:

> Indicate by check mark whether any of those error corrections are restatements that required a recovery analysis of incentive based compensation received by any of the registrant’s executive officers during the relevant recovery period pursuant to §240.10D-1(b). ☐ [S54]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 6-K, filed 2026-10-16, L46:

> Many of these statements are based on assumptions about factors that are beyond the Company’s ability to control or predict and are subject to significant risks and uncertainties that are described more fully in “Item 3. Key Information—3.D. Risk Factors” of our annual report on Form 20-F for the fiscal year ended December 31, 2025, filed with the U.S. Securities and Exchange Commission on April 30, 2026. Any of these factors or a combination of these factors could materially affect our future results of operations and the ultimate accuracy of the forward-looking statements. Fluctuations in our future financial results may negatively impact the value of our ordinary shares. Should any of these risks or uncertainties materialize, should any of our assumptions prove incorrect, or should we be unable to address any of the foregoing factors, our actual results may vary in material and adverse respects from those projected in these forward-looking statements. Consequently, there can be no assurance that actual results or developments anticipated by us will be realized or, even if substantially realized, that they will have the expected consequences to, or effects, on us. Given these uncertainties, prospective investors are cautioned not to place undue reliance on such forward-looking statements. [S53]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 144, 20-F, 3, 424B4, 424B5, 6-K, 6-K/A, 8-A12B, CERT, CORRESP, DRS, DRS/A, DRSLTR, EFFECT, F-1, F-1/A, F-1MEF, F-3, F-3/A, FWP, NT 20-F, S-8, SC 13D, SC 13D/A, SC 13G, SC 13G/A, SCHEDULE 13G/A, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:35:46.683439+00:00.

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
| 2026-10-16 | 6-K | 0001104659-26-116640 | — | [S03] |
| 2026-09-21 | EFFECT | 9999999995-26-003018 | — | [S04] |
| 2026-09-18 | 6-K | 0001104659-26-108972 | — | [S05] |
| 2026-09-17 | EFFECT | 9999999995-26-002997 | — | [S06] |
| 2026-09-15 | 6-K | 0001104659-26-107944 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-11-01T16:07:03.070084+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001811216.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [6-K 0001104659-26-116640](https://www.sec.gov/Archives/edgar/data/1811216/000110465926116640/0001104659-26-116640-index.html) — published 2026-10-16; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [EFFECT 9999999995-26-003018](https://www.sec.gov/Archives/edgar/data/1811216/999999999526003018/9999999995-26-003018-index.html) — published 2026-09-21; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [6-K 0001104659-26-108972](https://www.sec.gov/Archives/edgar/data/1811216/000110465926108972/0001104659-26-108972-index.html) — published 2026-09-18; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [EFFECT 9999999995-26-002997](https://www.sec.gov/Archives/edgar/data/1811216/999999999526002997/9999999995-26-002997-index.html) — published 2026-09-17; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [6-K 0001104659-26-107944](https://www.sec.gov/Archives/edgar/data/1811216/000110465926107944/0001104659-26-107944-index.html) — published 2026-09-15; retrieved 2026-10-23T08:33:02.691743+00:00.

[S53] [6-K 0001104659-26-116640](https://www.sec.gov/Archives/edgar/data/1811216/000110465926116640/baos-20260630x6k.htm) — published 2026-10-16; retrieved 2026-11-19T21:13:17.496667+00:00.

[S54] [20-F 0001104659-26-053161](https://www.sec.gov/Archives/edgar/data/1811216/000110465926053161/baos-20251231x20f.htm) — published 2026-04-30; retrieved 2026-11-19T21:13:15.483110+00:00.

Source release: `coverage-20261101-41324509967-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/0f49b319f95dcee8e757e592a38a028a04a7bc3c/brain/companies/BAOS/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
