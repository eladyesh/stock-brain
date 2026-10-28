---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001506184
cik: 0001506184
company_name: IMMUTEP Ltd
tickers:
- IMMP
status: stub
canonical_reviewed: false
as_of: '2026-10-28'
updated_at: '2026-10-28T16:13:42.115634+00:00'
reviewed_at: null
coverage_release: coverage-20261028-40722802424-1
source_commit: 48056b79cf1dc5f5270bd576defc5c9bc49d62cf
financial_history_available: false
curated_research: null
financial_gap:
  reason: foreign_reporting_adapter
  next_action: Add support for the observed 20-F, 40-F or 6-K reporting forms and
    verify the actual accounting taxonomy before normalization.
  observed_forms:
  - 20-F
  - 20-F/A
  - 20FR12B
  - 20FR12B/A
  - '3'
  - 424B3
  - 424B5
  - 6-K
  - CERTNAS
  - CORRESP
  - CT ORDER
  - D
  - EFFECT
  - F-3
  - F-6
  - RW
  - SC 13G
  - SC 13G/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001506184.json
    sha256: 4c184d6271702b54ca5e886637cc79f3b6659f6215410a541b455ab3706338b0
    retrieved_at: '2026-10-24T13:22:51.759433+00:00'
    archive: &id001
      member: CIK0001506184.json
      sha256: 593fbbea6512ef5ec729a5e513c465fbedaac8a66602c0abe00d0ba5a4d18732
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: nasdaqlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt
  published_at: null
  retrieved_at: '2026-10-28T16:09:01.738588+00:00'
  sha256: b555e192b928396dc88877226e82c2c8e9470c389cf2def559495683c673510d
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001506184.json
  published_at: null
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 4c184d6271702b54ca5e886637cc79f3b6659f6215410a541b455ab3706338b0
- id: S03
  title: 20-F 0001193125-26-429413
  url: https://www.sec.gov/Archives/edgar/data/1506184/000119312526429413/0001193125-26-429413-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S04
  title: 6-K 0001193125-26-420840
  url: https://www.sec.gov/Archives/edgar/data/1506184/000119312526420840/0001193125-26-420840-index.html
  published_at: '2026-10-14'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S05
  title: 6-K 0001193125-26-397189
  url: https://www.sec.gov/Archives/edgar/data/1506184/000119312526397189/0001193125-26-397189-index.html
  published_at: '2026-09-22'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S06
  title: 6-K 0001193125-26-389402
  url: https://www.sec.gov/Archives/edgar/data/1506184/000119312526389402/0001193125-26-389402-index.html
  published_at: '2026-09-11'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S07
  title: 6-K 0001193125-26-379062
  url: https://www.sec.gov/Archives/edgar/data/1506184/000119312526379062/0001193125-26-379062-index.html
  published_at: '2026-09-02'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S53
  url: https://www.sec.gov/Archives/edgar/data/1506184/000119312526429413/d109552d20f.htm
  title: 20-F 0001193125-26-429413
  published_at: '2026-10-23'
  retrieved_at: '2026-10-28T16:22:29.843041+00:00'
  sha256: dd9a049cb69cabf348934087bc6591d681d8164de6fd679c72aa9a874099d4a2
issuer_classification:
  cik: 0001506184
  classification_status: reported_sic
  entity_type: other
  name: IMMUTEP Ltd
  sic: '2834'
  sic_description: Pharmaceutical Preparations
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 4c184d6271702b54ca5e886637cc79f3b6659f6215410a541b455ab3706338b0
  url: https://data.sec.gov/submissions/CIK0001506184.json
listings:
- ticker: IMMP
  exchange: NASDAQ
  instrument_type: depositary_receipt
research_filings:
- accession: 0001193125-26-429413
  filed: '2026-10-23'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1506184/000119312526429413/0001193125-26-429413-index.html
- accession: 0001193125-17-216819
  filed: '2017-06-28'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1506184/000119312517216819/0001193125-17-216819-index.html
- accession: 0001193125-12-489357
  filed: '2012-12-03'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1506184/000119312512489357/0001193125-12-489357-index.html
- accession: 0001193125-26-420840
  filed: '2026-10-14'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1506184/000119312526420840/0001193125-26-420840-index.html
research_progress:
  stage: evidence_collected
  input_sha256: 4b773e1682e7355900c70e72383169c5bdcbbbe074e1eb453d2ef4228b777f1f
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
  source_url: https://data.sec.gov/submissions/CIK0001506184.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/d9e673c37aaa38580be4e36b4880e8ab015a9390/brain/companies/IMMP/README.md
full_history_commit: d9e673c37aaa38580be4e36b4880e8ab015a9390
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# IMMP — IMMUTEP Ltd

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/d9e673c37aaa38580be4e36b4880e8ab015a9390/brain/companies/IMMP/README.md)

## Business overview

Reported issuer name: **IMMUTEP Ltd**. Stable SEC CIK: **0001506184**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| IMMP | NASDAQ | depositary_receipt | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 20-F, filed 2026-10-23, L1009:

> The following risks relate specifically to our business and should be considered carefully. Our business, financial condition and results of operations could be harmed by any of the following risks. As a result, the trading price of our ordinary shares and our American Depositary Shares, or ADSs, could decline and the holders could lose part or all of their investment. [S53]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 20-F, filed 2026-10-23, L1114:

> If we are unable to secure sufficient capital to fund our operations, we may be required to delay, limit, reduce or terminate our product development or future commercialization efforts or grant rights to third parties to develop and market products or product candidates that we would otherwise prefer to develop and market ourselves. For example, additional strategic collaborations could require us to share commercial rights to our product candidates with third parties in ways that we do not intend currently or on terms that may not be favorable to us. Moreover, we may also have to relinquish valuable rights to our technologies, future revenue streams, research programs or product candidates or grant licenses on terms that may not be favorable to us. [S53]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 20-F, filed 2026-10-23, L932:

> our product development and business strategy, including the potential size of the markets for our products and future development and/or expansion of our products and therapies in our markets; [S53]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **2834**: Pharmaceutical Preparations. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 20-F, filed 2026-10-23, L1397:

> The manufacturing process for a product candidate is subject to FDA and foreign regulatory authority review. Suppliers and manufacturers must meet applicable manufacturing requirements and undergo rigorous facility and process validation tests required by regulatory authorities in order to comply with regulatory standards, such as cGMP. In the event that any of our suppliers or manufacturers fails to comply with such requirements or to perform its obligations to us in relation to quality, timing or otherwise, or if our supply of components or other materials becomes limited or interrupted for other reasons, we may be forced to manufacture the materials ourselves or enter into an agreement with another third party, which would be costly and delay any future clinical trials. [S53]

Navigation sector: **health-care**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 20-F, filed 2026-10-23, L1388:

> a collaborator could independently move forward with a competing product developed either independently or in collaboration with others, including our competitors; and [S53]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 20-F, filed 2026-10-23, L1022:

> Our second LAG-3 product candidate is IMP701 (INN: ieramilimab, also known as LAG525), an antagonist antibody that acts to stimulate T cell proliferation in cancer patients. IMP701 was fully licensed to CoStim Pharmaceuticals, which was subsequently acquired by Novartis. In August 2026, the exclusive license and collaboration agreement was terminated on notice from Novartis, and Novartis will assign its ownership interest in the jointly owned LAG-3 patents arising under the collaboration to Immutep S.A.S. Our third LAG-3 product candidate is IMP731, a depleting antibody that could remove T cells involved in autoimmunity. IMP731 was licensed to a major pharmaceutical company and has been transferred back to Immutep. Our fourth LAG-3 product candidate is IMP761, a clinical-stage product candidate which is being developed as our first agonist antibody of LAG-3 for application in autoimmune disease. We have discontinued our early-stage small molecule anti-LAG-3 research program, although our exclusive license agreement with Cardiff University has not been terminated. In addition to these products, Immutep has a dedicated R&D laboratory close to Paris with ongoing research capabilities as well as external research collaborations. Immutep also currently generates modest income from sales of LAG-3 research reagents. [S53]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 20-F, filed 2026-10-23, L1049:

> We have historically devoted most of our financial resources to research and development, including pre-clinical and clinical development and manufacturing activities. To date, we have financed a significant amount of our operations through public and private financing. The amount of our future net losses will depend, in part, on the rate of our future expenditures and our ability to obtain funding through equity or debt financing or strategic collaborations. The amount of such future net losses, as well as the possibility of future profitability, will also depend on our success in developing and commercializing products that generate significant revenue. Our failure to become and remain profitable would depress the value of our ordinary shares or ADSs and could impair our ability to raise capital, expand our business, maintain our research and development efforts, diversify our product offerings, or even continue our operations. [S53]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 20-F, filed 2026-10-23, L127:

> Indicate by check mark whether any of those error corrections are restatements that required a recovery analysis of incentive based compensation received by any of the registrant’s executive officers during the relevant recovery period pursuant to [S53]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 20-F, filed 2026-10-23, L988:

> We remind investors that forward-looking statements are merely predictions and therefore inherently subject to uncertainties and other factors and involve known and unknown risks that could cause the actual results, performance, levels of activity, our achievements or industry results, to be materially different from any future results, performance, levels of activity, or our achievements expressed or implied by such forward-looking statements. Investors are cautioned not to place undue reliance on these forward-looking statements, which speak only as of the date hereof. Except as required by applicable law, including the securities laws of the United States, we undertake no obligation to publicly release any update or revision to any forward-looking statements to reflect new information, future events, or circumstances, or otherwise after the date hereof. Please see the Risk Factors section that appears in “Item 3. Key Information – D. Risk Factors.” [S53]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 20-F, 20-F/A, 20FR12B, 20FR12B/A, 3, 424B3, 424B5, 6-K, CERTNAS, CORRESP, CT ORDER, D, EFFECT, F-3, F-6, RW, SC 13G, SC 13G/A, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:33:45.715431+00:00.

### Research work queue

Collection stage: **evidence_collected**. Extracted evidence is not a reviewed conclusion. Daily collection resumes from durable state; unchanged accessions are reused.

- **Business overview** (source excerpts available; assess the claim): Explain what the company does, who pays it, and why the business exists. Cite primary sources.
- **Revenue model and segments** (source excerpts available; assess the claim): Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.
- **Products and services** (source excerpts available; assess the claim): Describe the main products, customer problems solved, distribution, and product dependencies.
- **Customers and end markets** (evidence or analysis still needed): Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.
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
| 2026-10-23 | 20-F | 0001193125-26-429413 | — | [S03] |
| 2026-10-14 | 6-K | 0001193125-26-420840 | — | [S04] |
| 2026-09-22 | 6-K | 0001193125-26-397189 | — | [S05] |
| 2026-09-11 | 6-K | 0001193125-26-389402 | — | [S06] |
| 2026-09-02 | 6-K | 0001193125-26-379062 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-28T16:09:01.738588+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001506184.json) — published not supplied; retrieved 2026-10-24T13:22:51.759433+00:00.

[S03] [20-F 0001193125-26-429413](https://www.sec.gov/Archives/edgar/data/1506184/000119312526429413/0001193125-26-429413-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S04] [6-K 0001193125-26-420840](https://www.sec.gov/Archives/edgar/data/1506184/000119312526420840/0001193125-26-420840-index.html) — published 2026-10-14; retrieved 2026-10-24T13:22:51.759433+00:00.

[S05] [6-K 0001193125-26-397189](https://www.sec.gov/Archives/edgar/data/1506184/000119312526397189/0001193125-26-397189-index.html) — published 2026-09-22; retrieved 2026-10-24T13:22:51.759433+00:00.

[S06] [6-K 0001193125-26-389402](https://www.sec.gov/Archives/edgar/data/1506184/000119312526389402/0001193125-26-389402-index.html) — published 2026-09-11; retrieved 2026-10-24T13:22:51.759433+00:00.

[S07] [6-K 0001193125-26-379062](https://www.sec.gov/Archives/edgar/data/1506184/000119312526379062/0001193125-26-379062-index.html) — published 2026-09-02; retrieved 2026-10-24T13:22:51.759433+00:00.

[S53] [20-F 0001193125-26-429413](https://www.sec.gov/Archives/edgar/data/1506184/000119312526429413/d109552d20f.htm) — published 2026-10-23; retrieved 2026-10-28T16:22:29.843041+00:00.

Source release: `coverage-20261028-40722802424-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/d9e673c37aaa38580be4e36b4880e8ab015a9390/brain/companies/IMMP/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
