---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001025996
cik: 0001025996
company_name: KILROY REALTY CORP
tickers:
- KRC
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
  reason: latest_filing_incomplete
  next_action: Resolve the latest financial filing/CompanyFacts mismatch; any historical
    bootstrap must keep the latest-period gap explicit.
  observed_forms:
  - 10-K
  - 10-Q
  - '144'
  - '3'
  - '4'
  - 4/A
  - 424B2
  - 424B5
  - 424B7
  - 8-K
  - 8-K/A
  - ARS
  - CORRESP
  - DEF 14A
  - DEFA14A
  - FWP
  - PRE 14A
  - S-3ASR
  - S-8
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001025996.json
    sha256: a437ea0eb6964f4f0733b43a82ccafc7a40f21951b11d9873afdb0d463e39d57
    retrieved_at: '2026-10-24T13:22:51.759433+00:00'
    archive: &id001
      member: CIK0001025996.json
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
  url: https://data.sec.gov/submissions/CIK0001025996.json
  published_at: null
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: a437ea0eb6964f4f0733b43a82ccafc7a40f21951b11d9873afdb0d463e39d57
- id: S03
  title: 10-Q 0001628280-26-067051
  url: https://www.sec.gov/Archives/edgar/data/1025996/000162828026067051/0001628280-26-067051-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S04
  title: 8-K 0001628280-26-066920
  url: https://www.sec.gov/Archives/edgar/data/1025996/000162828026066920/0001628280-26-066920-index.html
  published_at: '2026-10-22'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S05
  title: 4 0001628280-26-066185
  url: https://www.sec.gov/Archives/edgar/data/1025996/000162828026066185/0001628280-26-066185-index.html
  published_at: '2026-10-16'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S06
  title: 4 0001628280-26-066184
  url: https://www.sec.gov/Archives/edgar/data/1025996/000162828026066184/0001628280-26-066184-index.html
  published_at: '2026-10-16'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S07
  title: 4 0001628280-26-066183
  url: https://www.sec.gov/Archives/edgar/data/1025996/000162828026066183/0001628280-26-066183-index.html
  published_at: '2026-10-16'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S53
  url: https://www.sec.gov/Archives/edgar/data/1025996/000162828026067051/krc-20260930.htm
  title: 10-Q 0001628280-26-067051
  published_at: '2026-10-23'
  retrieved_at: '2026-10-28T16:25:55.588585+00:00'
  sha256: 143c35afeb2d07a36291189dfa4787abaec90bb5b03c26b65e82950019cf2b29
- id: S55
  url: https://www.sec.gov/Archives/edgar/data/1025996/000119312526149727/d27549ddef14a.htm
  title: DEF 14A 0001193125-26-149727
  published_at: '2026-04-09'
  retrieved_at: '2026-10-28T16:25:52.035372+00:00'
  sha256: d778e2580b63ce4031c6051c2ca5f4750e67fb4d848221983f09bfbe9f161c4f
- id: S56
  url: https://www.sec.gov/Archives/edgar/data/1025996/000162828026007051/krc-20251231.htm
  title: 10-K 0001628280-26-007051
  published_at: '2026-02-11'
  retrieved_at: '2026-10-28T16:25:49.841692+00:00'
  sha256: 0957d4c51dc0c2a0cc2f98f8130d915ac08aced89c320c14ad9f5c6c8376bce7
issuer_classification:
  cik: 0001025996
  classification_status: reported_sic
  entity_type: operating
  name: KILROY REALTY CORP
  sic: '6798'
  sic_description: Real Estate Investment Trusts
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: a437ea0eb6964f4f0733b43a82ccafc7a40f21951b11d9873afdb0d463e39d57
  url: https://data.sec.gov/submissions/CIK0001025996.json
listings:
- ticker: KRC
  exchange: NYSE
  instrument_type: common_stock
research_filings:
- accession: 0001628280-26-007051
  filed: '2026-02-11'
  form: 10-K
  period_end: '2025-12-31'
  url: https://www.sec.gov/Archives/edgar/data/1025996/000162828026007051/0001628280-26-007051-index.html
- accession: 0001628280-26-067051
  filed: '2026-10-23'
  form: 10-Q
  period_end: '2026-09-30'
  url: https://www.sec.gov/Archives/edgar/data/1025996/000162828026067051/0001628280-26-067051-index.html
- accession: 0001193125-26-149727
  filed: '2026-04-09'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/1025996/000119312526149727/0001193125-26-149727-index.html
- accession: 0001628280-26-066920
  filed: '2026-10-22'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/1025996/000162828026066920/0001628280-26-066920-index.html
- accession: 0001025996-23-000142
  filed: '2023-06-23'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1025996/000102599623000142/0001025996-23-000142-index.html
research_progress:
  stage: evidence_collected
  input_sha256: e92592e83b5c977be5eae4fcfdfbf85b6a8c1642c0225e3745e2081286756830
  last_attempt_at: '2026-10-28T16:19:58.196907+00:00'
  last_success_at: '2026-10-28T16:19:58.196907+00:00'
  next_retry_at: null
  source_set_current: true
  evidence_topics:
  - business-overview
  - competitive-landscape
  - growth-drivers
  - industry-and-value-chain
  - management-and-governance
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
  sic: '6798'
  sic_description: Real Estate Investment Trusts
  rule_version: 1
  reason: Missing, ambiguous or unmapped reported industry; company-specific review
    is required.
full_history_url: https://github.com/eladyesh/stock-brain/blob/79888139fa1fe8ad3404e6bc04e318eee1474f73/brain/companies/KRC/README.md
full_history_commit: 79888139fa1fe8ad3404e6bc04e318eee1474f73
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# KRC — KILROY REALTY CORP

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/79888139fa1fe8ad3404e6bc04e318eee1474f73/brain/companies/KRC/README.md)

## Business overview

Reported issuer name: **KILROY REALTY CORP**. Stable SEC CIK: **0001025996**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| KRC | NYSE | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 10-Q, filed 2026-10-23, L756:

> We own our interests in all of our real estate assets through Kilroy Realty, L.P. (the “Operating Partnership”) and conduct substantially all of our operations through the Operating Partnership. Unless stated otherwise or the context otherwise requires, the terms “Kilroy Realty Corporation” or the “Company,” “we,” “our,” and “us” refer to Kilroy Realty Corporation and its consolidated subsidiaries, including the Operating Partnership, and the term “Operating Partnership” refers to Kilroy Realty, L.P. and its consolidated subsidiaries. The descriptions of our business, employees, and properties apply to both the Company and the Operating Partnership. [S53]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 10-Q, filed 2026-10-23, L1193:

> We conduct our business on a consolidated basis in one operating segment and therefore have one reportable segment. Asset information by segment is not reported because the Company does not use this measure to assess performance. [S53]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 10-K, filed 2026-02-11, L497:

> Our business is also gradually seeing the use of artificial intelligence to complement our decision making in order to improve our services and tailor our interactions. In recent years, the use of these methods has come under increased regulatory scrutiny. New laws, guidance, and/or decisions in this area may limit our ability to use our artificial intelligence models, or require us to make changes to our operations that may decrease our operational efficiency, result in an increase to operating costs, and/or hinder our ability to improve our services. For example, in October 2023, the President of the United States issued an executive order on the Safe, Secure and Trustworthy Development and Use of AI, emphasizing the need for transparency, accountability, and fairness in the development and use of AI. Any actual or perceived failure to comply with evolving regulatory frameworks around the development and use of AI, machine learning, and automated decision making could adversely affect us. [S56]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **6798**: Real Estate Investment Trusts. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — DEF 14A, filed 2026-04-09, L897:

> Supply Chain Responsibility. Kilroy is committed to conducting its business in compliance with the law and the highest levels of integrity, trust, and respect for the environment and human rights, and we expect our vendors and suppliers to uphold these principles. To ensure alignment, in 2025, we published an updated Vendor and Supplier Code of Conduct, which our vendors and suppliers are expected to comply with and which is posted on our website at https://kilroyrealty.com/sustainability. [S55]

Navigation sector: **unclassified**. Method: `unresolved`. Missing, ambiguous or unmapped reported industry; company-specific review is required.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 10-Q, filed 2026-10-23, L2062:

> Implicit in historical cost accounting for real estate assets in accordance with GAAP is the assumption that the value of real estate assets diminishes predictably over time. Since real estate values have historically risen or fallen with market conditions, many industry investors and analysts have considered presentations of operating results for real estate companies using historical cost accounting alone to be insufficient. Because FFO excludes depreciation and amortization of real estate assets, we believe that FFO along with the required GAAP presentations provides a more complete measurement of our performance relative to our competitors and a more appropriate basis on which to make decisions involving operating, financing, and investing activities than the required GAAP presentations alone would provide. [S53]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 10-Q, filed 2026-10-23, L1919:

> Our general strategy is to maintain a conservative balance sheet with a strong credit profile and to maintain a capital structure that allows for financial flexibility and diversification of capital resources. We manage our capital structure to reflect a long-term investment approach and utilize multiple sources of capital to meet our long-term capital requirements. We believe that our current projected liquidity requirements for the next twelve-month period, as set forth above under the caption “—Liquidity Uses,” will be satisfied using a combination of the liquidity sources listed above, although there can be no assurance in this regard. We believe our disciplined capital structure and staggered debt maturities provide us with financial flexibility and enhance our ability to obtain additional sources of liquidity if necessary, and, therefore, we are well-positioned to refinance or repay maturing debt and to pursue our strategy of seeking attractive acquisition opportunities, which we may finance, as necessary, with future public and private issuances of debt and equity securities, although there can be no assurance in this regard. [S53]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 10-Q, filed 2026-10-23, L1844:

> The Company intends to continue to make, but has not committed to making, regular quarterly cash distributions to common stockholders. All such distributions are at the discretion of the Board of Directors. The Company considers market factors and its performance in addition to REIT requirements in determining its distribution levels. Amounts accumulated for distribution to stockholders are invested primarily in interest-bearing accounts and short-term interest-bearing securities, which is consistent with the Company’s intention to maintain its qualification as a REIT. Such investments may include, for example, [S53]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 10-Q, filed 2026-10-23, L1045:

> We and our properties are subject to routine litigation incidental to our business. As of September 30, 2026, we are not a defendant in, and our properties are not subject to, any legal proceedings that we believe, if determined adversely to us, would have a material adverse effect upon our financial condition, results of operations or cash flows. [S53]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Resolve the latest financial filing/CompanyFacts mismatch; any historical bootstrap must keep the latest-period gap explicit.
- Forms observed in the retained filing inventory: 10-K, 10-Q, 144, 3, 4, 4/A, 424B2, 424B5, 424B7, 8-K, 8-K/A, ARS, CORRESP, DEF 14A, DEFA14A, FWP, PRE 14A, S-3ASR, S-8, SC 13G, SC 13G/A, SCHEDULE 13G, SCHEDULE 13G/A, UPLOAD
- Collector status: quality_review_required; last action: filings_only_financials_incomplete; last checked: 2026-10-24T13:30:57.453913+00:00.

### Research work queue

Collection stage: **evidence_collected**. Extracted evidence is not a reviewed conclusion. Daily collection resumes from durable state; unchanged accessions are reused.

- **Business overview** (source excerpts available; assess the claim): Explain what the company does, who pays it, and why the business exists. Cite primary sources.
- **Revenue model and segments** (source excerpts available; assess the claim): Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.
- **Products and services** (source excerpts available; assess the claim): Describe the main products, customer problems solved, distribution, and product dependencies.
- **Customers and end markets** (evidence or analysis still needed): Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.
- **Industry and value chain** (source excerpts available; assess the claim): Place the company among suppliers, distribution channels, customers, and substitutes. Explain cyclicality and supply constraints.
- **Competitive landscape** (source excerpts available; assess the claim): Identify direct competitors and alternatives. Compare specific products or business segments, with sources.
- **Moat and differentiation** (evidence or analysis still needed): Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.
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
| 2026-10-23 | 10-Q | 0001628280-26-067051 | — | [S03] |
| 2026-10-22 | 8-K | 0001628280-26-066920 | — | [S04] |
| 2026-10-16 | 4 | 0001628280-26-066185 | — | [S05] |
| 2026-10-16 | 4 | 0001628280-26-066184 | — | [S06] |
| 2026-10-16 | 4 | 0001628280-26-066183 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-30T16:00:12.358089+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001025996.json) — published not supplied; retrieved 2026-10-24T13:22:51.759433+00:00.

[S03] [10-Q 0001628280-26-067051](https://www.sec.gov/Archives/edgar/data/1025996/000162828026067051/0001628280-26-067051-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S04] [8-K 0001628280-26-066920](https://www.sec.gov/Archives/edgar/data/1025996/000162828026066920/0001628280-26-066920-index.html) — published 2026-10-22; retrieved 2026-10-24T13:22:51.759433+00:00.

[S05] [4 0001628280-26-066185](https://www.sec.gov/Archives/edgar/data/1025996/000162828026066185/0001628280-26-066185-index.html) — published 2026-10-16; retrieved 2026-10-24T13:22:51.759433+00:00.

[S06] [4 0001628280-26-066184](https://www.sec.gov/Archives/edgar/data/1025996/000162828026066184/0001628280-26-066184-index.html) — published 2026-10-16; retrieved 2026-10-24T13:22:51.759433+00:00.

[S07] [4 0001628280-26-066183](https://www.sec.gov/Archives/edgar/data/1025996/000162828026066183/0001628280-26-066183-index.html) — published 2026-10-16; retrieved 2026-10-24T13:22:51.759433+00:00.

[S53] [10-Q 0001628280-26-067051](https://www.sec.gov/Archives/edgar/data/1025996/000162828026067051/krc-20260930.htm) — published 2026-10-23; retrieved 2026-10-28T16:25:55.588585+00:00.

[S55] [DEF 14A 0001193125-26-149727](https://www.sec.gov/Archives/edgar/data/1025996/000119312526149727/d27549ddef14a.htm) — published 2026-04-09; retrieved 2026-10-28T16:25:52.035372+00:00.

[S56] [10-K 0001628280-26-007051](https://www.sec.gov/Archives/edgar/data/1025996/000162828026007051/krc-20251231.htm) — published 2026-02-11; retrieved 2026-10-28T16:25:49.841692+00:00.

Source release: `coverage-20261030-41085569265-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/79888139fa1fe8ad3404e6bc04e318eee1474f73/brain/companies/KRC/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
