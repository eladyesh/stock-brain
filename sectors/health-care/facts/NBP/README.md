---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001778016
cik: 0001778016
company_name: NovaBridge Biosciences
tickers:
- NBP
status: stub
canonical_reviewed: false
as_of: '2026-10-30'
updated_at: '2026-10-30T16:05:25.650854+00:00'
reviewed_at: null
coverage_release: coverage-20261030-41085569265-1
source_commit: ef2ed016c2c344c23ee7fb991b25bf93660da77e
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
  - F-3
  - F-3ASR
  - F-6
  - F-6EF
  - POS AM
  - S-8
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13D
  - SCHEDULE 13D/A
  - SCHEDULE 13G
  - SEC STAFF LETTER
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001778016.json
    sha256: 37ddca13ac2fd30439db954c74e17c196a6e4d4668f56d09fbffee6711716672
    retrieved_at: '2026-10-24T13:22:51.759433+00:00'
    archive: &id001
      member: CIK0001778016.json
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
  url: https://data.sec.gov/submissions/CIK0001778016.json
  published_at: null
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 37ddca13ac2fd30439db954c74e17c196a6e4d4668f56d09fbffee6711716672
- id: S03
  title: 6-K 0001193125-26-429548
  url: https://www.sec.gov/Archives/edgar/data/1778016/000119312526429548/0001193125-26-429548-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S04
  title: 4 0002115245-26-000004
  url: https://www.sec.gov/Archives/edgar/data/1778016/000211524526000004/0002115245-26-000004-index.html
  published_at: '2026-10-19'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S05
  title: 6-K 0001193125-26-419669
  url: https://www.sec.gov/Archives/edgar/data/1778016/000119312526419669/0001193125-26-419669-index.html
  published_at: '2026-10-13'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S06
  title: 4 0002089237-26-000008
  url: https://www.sec.gov/Archives/edgar/data/1778016/000208923726000008/0002089237-26-000008-index.html
  published_at: '2026-09-21'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S07
  title: 144 0001973379-26-000341
  url: https://www.sec.gov/Archives/edgar/data/1778016/000197337926000341/0001973379-26-000341-index.html
  published_at: '2026-09-18'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S54
  url: https://www.sec.gov/Archives/edgar/data/1778016/000177801626000006/nbp-20251231.htm
  title: 20-F/A 0001778016-26-000006
  published_at: '2026-06-16'
  retrieved_at: '2026-10-29T16:31:26.593083+00:00'
  sha256: b736cf8ef473778bc4d2ab7658bb3ccb7f17477ad175e6544951b130fe1fd888
- id: S55
  url: https://www.sec.gov/Archives/edgar/data/1778016/000177801626000002/nbp-20251231.htm
  title: 20-F 0001778016-26-000002
  published_at: '2026-04-07'
  retrieved_at: '2026-10-29T16:31:24.567512+00:00'
  sha256: 0a96d71efc8e31d9821dfd3b1d2092b8e81a6336f99b03c736e7500cc97cf29f
issuer_classification:
  cik: 0001778016
  classification_status: reported_sic
  entity_type: other
  name: NovaBridge Biosciences
  sic: '2834'
  sic_description: Pharmaceutical Preparations
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 37ddca13ac2fd30439db954c74e17c196a6e4d4668f56d09fbffee6711716672
  url: https://data.sec.gov/submissions/CIK0001778016.json
listings:
- ticker: NBP
  exchange: NASDAQ
  instrument_type: depositary_receipt
research_filings:
- accession: 0001778016-26-000002
  filed: '2026-04-07'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1778016/000177801626000002/0001778016-26-000002-index.html
- accession: 0001778016-26-000006
  filed: '2026-06-16'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1778016/000177801626000006/0001778016-26-000006-index.html
- accession: 0001193125-26-429548
  filed: '2026-10-23'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1778016/000119312526429548/0001193125-26-429548-index.html
- accession: 0001193125-26-041170
  filed: '2026-02-06'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1778016/000119312526041170/0001193125-26-041170-index.html
- accession: 0001193125-25-249298
  filed: '2025-10-24'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1778016/000119312525249298/0001193125-25-249298-index.html
- accession: 0000950170-25-095288
  filed: '2025-07-11'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1778016/000095017025095288/0000950170-25-095288-index.html
- accession: 0001193125-22-127837
  filed: '2022-04-28'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1778016/000119312522127837/0001193125-22-127837-index.html
- accession: 0001193125-22-091942
  filed: '2022-03-31'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1778016/000119312522091942/0001193125-22-091942-index.html
research_progress:
  stage: evidence_collected
  input_sha256: e23b11bb15b103a7fd33ca3446852a68bdff897d11da4bbb5e2cf291316bc424
  last_attempt_at: '2026-10-29T16:24:48.518388+00:00'
  last_success_at: '2026-10-29T16:24:48.518388+00:00'
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
  source_url: https://data.sec.gov/submissions/CIK0001778016.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/79888139fa1fe8ad3404e6bc04e318eee1474f73/brain/companies/NBP/README.md
full_history_commit: 79888139fa1fe8ad3404e6bc04e318eee1474f73
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# NBP — NovaBridge Biosciences

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/79888139fa1fe8ad3404e6bc04e318eee1474f73/brain/companies/NBP/README.md)

## Business overview

Reported issuer name: **NovaBridge Biosciences**. Stable SEC CIK: **0001778016**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| NBP | NASDAQ | depositary_receipt | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 20-F, filed 2026-04-07, L453:

> This annual report contains estimates, projections and other information concerning our industry, our business and the market for our drug candidates. Information that is based on estimates, forecasts, projections, market research or similar methodologies is inherently subject to uncertainties, and actual events or circumstances may differ materially from events and circumstances that are assumed in this information. Unless otherwise expressly stated, we obtained this industry, business, market and other data from our own internal estimates and research as well as from reports, research surveys, studies and similar data prepared by market research firms and other third parties, industry, medical and general publications, government data and similar sources. While we believe our internal company research related to such matters is reliable and the market definitions are appropriate, neither such research nor these definitions have been verified by any independent source. [S55]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 20-F, filed 2026-04-07, L3300:

> We may decide to enhance our liquidity position or increase our cash reserve for future operations and investments through additional financing. The issuance and sale of additional equity would result in further dilution to our shareholders and ADS holders, and the terms of these securities may include liquidation or other preferences that adversely affect our investors’ rights as ADS holders. The incurrence of indebtedness would result in increased fixed or variable obligations and could result in operating covenants that would restrict our operations, which could potentially dilute the interests of our shareholders. If we raise additional funds through collaborations, strategic alliances or licensing arrangements with third parties, we may have to relinquish valuable rights to our technologies, future revenue streams or research programs or to grant licenses on terms that may not be favorable to us. If we are unable to raise additional funds through equity or debt financings when needed, we may be required to delay, limit, reduce or terminate our product development or future commercialization efforts or grant rights to develop and market products or drug candidates that we would otherwise prefer to develop and market ourselves. [S55]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 20-F, filed 2026-04-07, L574:

> The failure to obtain a patent term extension and data exclusivity for any drug candidates we may develop could increase the risk of generic competition with our products. [S55]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 20-F, filed 2026-04-07, L1483:

> Changes in tax laws or regulations that are applied adversely to us or our customers may have a material adverse effect on our business, cash flow, financial condition, or results of operations. [S55]

## Industry and value chain

SEC-reported SIC **2834**: Pharmaceutical Preparations. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 20-F, filed 2026-04-07, L989:

> raw materials and components used in the manufacturing process, particularly those for which we have no other source or supplier, may not be available or may not be suitable or acceptable for use due to material or component defects; [S55]

Navigation sector: **health-care**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 20-F, filed 2026-04-07, L574:

> The failure to obtain a patent term extension and data exclusivity for any drug candidates we may develop could increase the risk of generic competition with our products. [S55]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 20-F, filed 2026-04-07, L489:

> our ability to obtain and maintain protection of intellectual property for our technology and drug candidates; [S55]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 20-F, filed 2026-04-07, L617:

> Under our new business model, we have expanded and may continue to expand our business through the acquisition of businesses or rights to new drug candidates that could disrupt our business, harm our financial condition and may also dilute current shareholders’ ownership interests in our company. [S55]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 20-F/A, filed 2026-06-16, L91:

> Indicate by check mark whether any of those error corrections are restatements that required a recovery analysis of incentive-based compensation received by any of the registrant’s executive officers during the relevant recovery period pursuant to §240.10D-1(b). ☐ [S54]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 20-F, filed 2026-04-07, L454:

> In addition, assumptions and estimates of our and our industry’s future performance are necessarily subject to a high degree of uncertainty and risk due to a variety of factors, including those described in the section titled “Risk Factors.” These and other factors could cause our future performance to differ materially from our assumptions and estimates. See “Forward-Looking Statements.” [S55]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 144, 20-F, 20-F/A, 3, 3/A, 4, 424B3, 424B4, 424B5, 6-K, 6-K/A, 8-A12B, CERT, CORRESP, DRS, DRS/A, DRSLTR, EFFECT, F-1, F-1/A, F-3, F-3ASR, F-6, F-6EF, POS AM, S-8, SC 13D, SC 13D/A, SC 13G, SC 13G/A, SCHEDULE 13D, SCHEDULE 13D/A, SCHEDULE 13G, SEC STAFF LETTER, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:35:34.185184+00:00.

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
| 2026-10-23 | 6-K | 0001193125-26-429548 | — | [S03] |
| 2026-10-19 | 4 | 0002115245-26-000004 | — | [S04] |
| 2026-10-13 | 6-K | 0001193125-26-419669 | — | [S05] |
| 2026-09-21 | 4 | 0002089237-26-000008 | — | [S06] |
| 2026-09-18 | 144 | 0001973379-26-000341 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-30T16:00:11.183681+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001778016.json) — published not supplied; retrieved 2026-10-24T13:22:51.759433+00:00.

[S03] [6-K 0001193125-26-429548](https://www.sec.gov/Archives/edgar/data/1778016/000119312526429548/0001193125-26-429548-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S04] [4 0002115245-26-000004](https://www.sec.gov/Archives/edgar/data/1778016/000211524526000004/0002115245-26-000004-index.html) — published 2026-10-19; retrieved 2026-10-24T13:22:51.759433+00:00.

[S05] [6-K 0001193125-26-419669](https://www.sec.gov/Archives/edgar/data/1778016/000119312526419669/0001193125-26-419669-index.html) — published 2026-10-13; retrieved 2026-10-24T13:22:51.759433+00:00.

[S06] [4 0002089237-26-000008](https://www.sec.gov/Archives/edgar/data/1778016/000208923726000008/0002089237-26-000008-index.html) — published 2026-09-21; retrieved 2026-10-24T13:22:51.759433+00:00.

[S07] [144 0001973379-26-000341](https://www.sec.gov/Archives/edgar/data/1778016/000197337926000341/0001973379-26-000341-index.html) — published 2026-09-18; retrieved 2026-10-24T13:22:51.759433+00:00.

[S54] [20-F/A 0001778016-26-000006](https://www.sec.gov/Archives/edgar/data/1778016/000177801626000006/nbp-20251231.htm) — published 2026-06-16; retrieved 2026-10-29T16:31:26.593083+00:00.

[S55] [20-F 0001778016-26-000002](https://www.sec.gov/Archives/edgar/data/1778016/000177801626000002/nbp-20251231.htm) — published 2026-04-07; retrieved 2026-10-29T16:31:24.567512+00:00.

Source release: `coverage-20261030-41085569265-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/79888139fa1fe8ad3404e6bc04e318eee1474f73/brain/companies/NBP/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
