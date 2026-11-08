---
schema_version: 1
document_type: company_facts
company_id: company-cik-0000930157
cik: 0000930157
company_name: RENTOKIL INITIAL PLC /FI
tickers:
- RTO
status: stub
canonical_reviewed: false
as_of: '2026-11-01'
updated_at: '2026-11-01T16:11:48.803754+00:00'
reviewed_at: null
coverage_release: coverage-20261101-41324509967-1
source_commit: 204f3cdbbf1aa4d293d16ca1426a5b6c8ba2f16f
financial_history_available: false
curated_research: null
financial_gap:
  reason: foreign_reporting_adapter
  next_action: Add support for the observed 20-F, 40-F or 6-K reporting forms and
    verify the actual accounting taxonomy before normalization.
  observed_forms:
  - 20-F
  - 20-F/A
  - 424B3
  - '425'
  - 6-K
  - 6-K/A
  - 8-A12B
  - ARS
  - CERT
  - CORRESP
  - EFFECT
  - F-4
  - F-4/A
  - S-8
  - S-8 POS
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - SD
  - SUPPL
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0000930157.json
    sha256: 56efd119129b77706474cdca7b3bc3fe545f1dbccb870ab3a1d65a3325a7ed26
    retrieved_at: '2026-10-24T13:22:51.759433+00:00'
    archive: &id001
      member: CIK0000930157.json
      sha256: 593fbbea6512ef5ec729a5e513c465fbedaac8a66602c0abe00d0ba5a4d18732
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: otherlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt
  published_at: null
  retrieved_at: '2026-11-01T16:07:03.340031+00:00'
  sha256: ee0a872edece98430f3ba5a1ed6e9c683d7a1bb4b2980bdc9743c6995f264398
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0000930157.json
  published_at: null
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 56efd119129b77706474cdca7b3bc3fe545f1dbccb870ab3a1d65a3325a7ed26
- id: S03
  title: 6-K 0001654954-26-009119
  url: https://www.sec.gov/Archives/edgar/data/930157/000165495426009119/0001654954-26-009119-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S04
  title: 6-K 0001654954-26-009089
  url: https://www.sec.gov/Archives/edgar/data/930157/000165495426009089/0001654954-26-009089-index.html
  published_at: '2026-10-22'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S05
  title: 6-K 0001654954-26-009087
  url: https://www.sec.gov/Archives/edgar/data/930157/000165495426009087/0001654954-26-009087-index.html
  published_at: '2026-10-22'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S06
  title: 6-K 0001654954-26-008811
  url: https://www.sec.gov/Archives/edgar/data/930157/000165495426008811/0001654954-26-008811-index.html
  published_at: '2026-10-06'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S07
  title: 6-K 0001654954-26-008651
  url: https://www.sec.gov/Archives/edgar/data/930157/000165495426008651/0001654954-26-008651-index.html
  published_at: '2026-09-30'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S54
  url: https://www.sec.gov/Archives/edgar/data/930157/000110465926034062/rto-20251231x20f.htm
  title: 20-F 0001104659-26-034062
  published_at: '2026-03-25'
  retrieved_at: '2026-10-31T15:38:18.029457+00:00'
  sha256: c037b351bf396f665fd939c5811271d7350757538939082b1eaabcf9936a2a41
issuer_classification:
  cik: 0000930157
  classification_status: reported_sic
  entity_type: other
  name: RENTOKIL INITIAL PLC /FI
  sic: '8741'
  sic_description: Services-Management Services
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 56efd119129b77706474cdca7b3bc3fe545f1dbccb870ab3a1d65a3325a7ed26
  url: https://data.sec.gov/submissions/CIK0000930157.json
listings:
- ticker: RTO
  exchange: NYSE
  instrument_type: depositary_receipt
research_filings:
- accession: 0001104659-26-034062
  filed: '2026-03-25'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/930157/000110465926034062/0001104659-26-034062-index.html
- accession: 0001104659-24-012318
  filed: '2024-02-08'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/930157/000110465924012318/0001104659-24-012318-index.html
- accession: 0001654954-26-009119
  filed: '2026-10-23'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/930157/000165495426009119/0001654954-26-009119-index.html
- accession: 0001654954-22-014527
  filed: '2022-11-01'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/930157/000165495422014527/0001654954-22-014527-index.html
research_progress:
  stage: evidence_collected
  input_sha256: 456fdc224a2b459f5c174c192204d68ef388470afcd4f72a1d201f1bd40374ff
  last_attempt_at: '2026-10-31T15:34:51.132722+00:00'
  last_success_at: '2026-10-31T15:34:51.132722+00:00'
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
  sic: '8741'
  sic_description: Services-Management Services
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0000930157.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/d9fa20bef5c93a07dc35e332f689a4b7a8cc1341/brain/companies/RTO/README.md
full_history_commit: d9fa20bef5c93a07dc35e332f689a4b7a8cc1341
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# RTO — RENTOKIL INITIAL PLC /FI

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/d9fa20bef5c93a07dc35e332f689a4b7a8cc1341/brain/companies/RTO/README.md)

## Business overview

Reported issuer name: **RENTOKIL INITIAL PLC /FI**. Stable SEC CIK: **0000930157**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| RTO | NYSE | depositary_receipt | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 20-F, filed 2026-03-25, L220:

> \| \| ● \| our ability to attract, retain and develop key personnel to lead our business; [S54]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 20-F, filed 2026-03-25, L10241:

> Disaggregation of revenue into region, category, and major type of revenue stream is shown below under segment reporting. [S54]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 20-F, filed 2026-03-25, L437:

> Our ability to maintain our customer service and execute our business strategy depends on our ability to attract and retain a suitably skilled and qualified labour force. There can be no assurance that we will be able to recruit, train and retain such a labour force in sufficient numbers or of sufficient quality, or that pressure to recruit will not lead to a significant increase in employee costs. In markets where overall employment rates are high, and/or our business is growing quickly, either organically or through acquisitions, we may have difficulties attracting, training and retaining operational personnel of suitable capability. In addition, changes in the global job market may cause, or continue to cause, difficulty in recruiting, training and retaining a suitably skilled and qualified labour force. As a result, we could experience difficulty in responding to customer calls in a timely fashion or delivering our services in a high-quality or timely manner, and could be forced to increase wages to attract, train and retain colleagues, which would result in higher operating costs and reduced profitability. Any of these factors may have a material adverse effect on our business, reputation, results of operations, financial condition and/or prospects. [S54]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 20-F, filed 2026-03-25, L226:

> \| \| ● \| weakening general economic conditions, including changes in the global job market or decreased consumer confidence or spending levels, especially as they may affect demand from our customers; [S54]

## Industry and value chain

SEC-reported SIC **8741**: Services-Management Services. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 20-F, filed 2026-03-25, L232:

> \| \| ● \| supply chain issues, which may result in product shortages, cost increases or other disruptions to our business; [S54]

Navigation sector: **industrials**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 20-F, filed 2026-03-25, L438:

> Moreover, some of our colleagues are members of local trade unions and similar organisations. Industrial action in key operations could result in diminished customer service levels or higher costs and, if prolonged, could damage our reputation and ability to retain existing customers or acquire new customers. Although we believe that all of our operations have good relations with their colleagues and the trade unions that represent those colleagues (where applicable), there can be no assurance that work stoppages or other labour-related developments (including the introduction of new labour regulations in countries where we operate) will not adversely affect our business, reputation, results of operations, financial condition and/or prospects. In addition, potential competition from key colleagues who leave Rentokil Initial could impact our ability to maintain our market share in certain geographic areas. [S54]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 20-F, filed 2026-03-25, L233:

> \| \| ● \| our ability to protect our intellectual property and other proprietary rights that are material to our business; [S54]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 20-F, filed 2026-03-25, L427:

> In addition, we have sold a number of our businesses in the past and expect to continue to dispose of businesses from time to time if consistent with our strategy. For example, the Group completed the disposal of its Workwear business in France to H.I.G. Capital on 30 September 2025. Under business sale contracts, we may provide warranties and indemnities to purchasers. Accordingly, we may make provisions in our consolidated financial statements for potential liabilities and costs relating to a disposed business. We may also make provisions in our consolidated financial statements for amounts to cover legal or regulatory claims which are known to be outstanding at the time of sale or which may subsequently become apparent. There can be no assurance that such provisions will be sufficient to cover potential liabilities and consequently disposals of our businesses may have a material adverse effect on our business, reputation, results of operations, financial condition and/or prospects. [S54]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 20-F, filed 2026-03-25, L172:

> Indicate by check mark whether any of those error corrections are restatements that required a recovery analysis of incentive-based compensation received by any of the registrant’s executive officers during the relevant recovery period pursuant to §240.10D-1(b).◻ [S54]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 20-F, filed 2026-03-25, L247:

> Further details on the principal risks that may affect the Group can be found in the “Risks and Uncertainties” section detailed on pages 68 to 70 and the left column on page 71 and under the heading “Strategic Report—Responsible Business—Climate-related risk management” on page 62 (in relation to climate-related risks), in each case of the Company’s Annual Report 2025 included as exhibit 15.1 to this Form 20-F, as well as on pages F-51 to F-54 (in relation to financial risks) and under the heading Item 3.D “Risk Factors”, in each case of this Form 20-F. [S54]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 20-F, 20-F/A, 424B3, 425, 6-K, 6-K/A, 8-A12B, ARS, CERT, CORRESP, EFFECT, F-4, F-4/A, S-8, S-8 POS, SC 13D, SC 13D/A, SC 13G, SC 13G/A, SCHEDULE 13G, SCHEDULE 13G/A, SD, SUPPL, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:30:34.034651+00:00.

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
| 2026-10-23 | 6-K | 0001654954-26-009119 | — | [S03] |
| 2026-10-22 | 6-K | 0001654954-26-009089 | — | [S04] |
| 2026-10-22 | 6-K | 0001654954-26-009087 | — | [S05] |
| 2026-10-06 | 6-K | 0001654954-26-008811 | — | [S06] |
| 2026-09-30 | 6-K | 0001654954-26-008651 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-11-01T16:07:03.340031+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0000930157.json) — published not supplied; retrieved 2026-10-24T13:22:51.759433+00:00.

[S03] [6-K 0001654954-26-009119](https://www.sec.gov/Archives/edgar/data/930157/000165495426009119/0001654954-26-009119-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S04] [6-K 0001654954-26-009089](https://www.sec.gov/Archives/edgar/data/930157/000165495426009089/0001654954-26-009089-index.html) — published 2026-10-22; retrieved 2026-10-24T13:22:51.759433+00:00.

[S05] [6-K 0001654954-26-009087](https://www.sec.gov/Archives/edgar/data/930157/000165495426009087/0001654954-26-009087-index.html) — published 2026-10-22; retrieved 2026-10-24T13:22:51.759433+00:00.

[S06] [6-K 0001654954-26-008811](https://www.sec.gov/Archives/edgar/data/930157/000165495426008811/0001654954-26-008811-index.html) — published 2026-10-06; retrieved 2026-10-24T13:22:51.759433+00:00.

[S07] [6-K 0001654954-26-008651](https://www.sec.gov/Archives/edgar/data/930157/000165495426008651/0001654954-26-008651-index.html) — published 2026-09-30; retrieved 2026-10-24T13:22:51.759433+00:00.

[S54] [20-F 0001104659-26-034062](https://www.sec.gov/Archives/edgar/data/930157/000110465926034062/rto-20251231x20f.htm) — published 2026-03-25; retrieved 2026-10-31T15:38:18.029457+00:00.

Source release: `coverage-20261101-41324509967-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/d9fa20bef5c93a07dc35e332f689a4b7a8cc1341/brain/companies/RTO/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
