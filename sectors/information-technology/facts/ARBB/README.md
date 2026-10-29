---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001930179
cik: 0001930179
company_name: ARB IOT Group Ltd
tickers:
- ARBB
status: stub
canonical_reviewed: false
as_of: '2026-10-29'
updated_at: '2026-10-29T16:18:46.634043+00:00'
reviewed_at: null
coverage_release: coverage-20261029-40909364006-1
source_commit: 066173dd7c0933a11c2085b144bbb14099b44560
financial_history_available: false
curated_research: null
financial_gap:
  reason: foreign_reporting_adapter
  next_action: Add support for the observed 20-F, 40-F or 6-K reporting forms and
    verify the actual accounting taxonomy before normalization.
  observed_forms:
  - 20-F
  - '3'
  - 424B3
  - 424B4
  - 6-K
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
  - SC 13D
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13D/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001930179.json
    sha256: bec7f5335752664d989a54e8b14e29073169f121b3e7cb44f8cb6754958d2ea3
    retrieved_at: '2026-10-24T13:22:51.759433+00:00'
    archive: &id001
      member: CIK0001930179.json
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
  url: https://data.sec.gov/submissions/CIK0001930179.json
  published_at: null
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: bec7f5335752664d989a54e8b14e29073169f121b3e7cb44f8cb6754958d2ea3
- id: S03
  title: 6-K 0001213900-26-112088
  url: https://www.sec.gov/Archives/edgar/data/1930179/000121390026112088/0001213900-26-112088-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S04
  title: 6-K 0001213900-26-053918
  url: https://www.sec.gov/Archives/edgar/data/1930179/000121390026053918/0001213900-26-053918-index.html
  published_at: '2026-05-08'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S05
  title: 3 0001213900-26-029425
  url: https://www.sec.gov/Archives/edgar/data/1930179/000121390026029425/0001213900-26-029425-index.html
  published_at: '2026-03-18'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S06
  title: 3 0001213900-26-029414
  url: https://www.sec.gov/Archives/edgar/data/1930179/000121390026029414/0001213900-26-029414-index.html
  published_at: '2026-03-18'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S07
  title: 3 0001213900-26-029408
  url: https://www.sec.gov/Archives/edgar/data/1930179/000121390026029408/0001213900-26-029408-index.html
  published_at: '2026-03-18'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S54
  url: https://www.sec.gov/Archives/edgar/data/1930179/000121390025104705/ea0262495-20f_arbiot.htm
  title: 20-F 0001213900-25-104705
  published_at: '2025-10-31'
  retrieved_at: '2026-10-24T13:47:36.644052+00:00'
  sha256: 5e84b4f08f49aa0795f56ef01f8c7dd88e2652c903ba1e3cb3556c7b23b35cbb
issuer_classification:
  cik: 0001930179
  classification_status: reported_sic
  entity_type: other
  name: ARB IOT Group Ltd
  sic: '7373'
  sic_description: Services-Computer Integrated Systems Design
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: bec7f5335752664d989a54e8b14e29073169f121b3e7cb44f8cb6754958d2ea3
  url: https://data.sec.gov/submissions/CIK0001930179.json
listings:
- ticker: ARBB
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001213900-25-104705
  filed: '2025-10-31'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1930179/000121390025104705/0001213900-25-104705-index.html
- accession: 0001213900-26-112088
  filed: '2026-10-23'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1930179/000121390026112088/0001213900-26-112088-index.html
research_progress:
  stage: evidence_collected
  input_sha256: bca30af880aaf5d558e428b1c9a48223fbce379e956c43460338b19e30d4333e
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
  sector: information-technology
  method: project_sic_rule
  sic: '7373'
  sic_description: Services-Computer Integrated Systems Design
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001930179.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/52b6569b626a07b359d4a15742ebb633a0e48007/brain/companies/ARBB/README.md
full_history_commit: 52b6569b626a07b359d4a15742ebb633a0e48007
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# ARBB — ARB IOT Group Ltd

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/52b6569b626a07b359d4a15742ebb633a0e48007/brain/companies/ARBB/README.md)

## Business overview

Reported issuer name: **ARB IOT Group Ltd**. Stable SEC CIK: **0001930179**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| ARBB | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 20-F, filed 2025-10-31, L491:

> statements are based are reasonable and within the bounds of our knowledge of our business and operations as of the date of this Annual [S54]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 20-F, filed 2025-10-31, L2468:

> Officer. We report our results of operations in two reportable segments dedicated to (i) the provision of hardware and software of IoT [S54]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 20-F, filed 2025-10-31, L648:

> or implement our business strategies effectively. If the market for our services does not develop as we expect or if we fail to address [S54]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 20-F, filed 2025-10-31, L551:

> \| We are subject to credit risks associated with a significant amount of accounts receivable, and if we are unable to collect accounts receivable from our customers, our results of operations and cash flows could be materially adversely affected. [S54]

## Industry and value chain

SEC-reported SIC **7373**: Services-Computer Integrated Systems Design. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 20-F, filed 2025-10-31, L573:

> \| Our AI partnerships, regional expansion, and large server orders may not commercialize as expected and expose us to execution, supply chain, and working capital risks [S54]

Navigation sector: **information-technology**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 20-F, filed 2025-10-31, L642:

> \| successfully compete with other companies that are currently in, or may in the future enter, our industry or similar industries; and [S54]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 20-F, filed 2025-10-31, L840:

> in various agreements potentially expose us to substantial liability for intellectual property infringement and other losses. [S54]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 20-F, filed 2025-10-31, L761:

> \| a change in strategic priorities by our clients, resulting in a reduced level of spending on technology services; [S54]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 20-F, filed 2025-10-31, L1527:

> will be made at the discretion of our board of directors and will depend on our results of operations, financial condition, contractual [S54]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 20-F, filed 2025-10-31, L515:

> operations may differ materially from information contained in the forward-looking statements as a result of risk factors, some of which [S54]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 20-F, 3, 424B3, 424B4, 6-K, 8-A12B, CERT, CORRESP, DRS, DRS/A, DRSLTR, EFFECT, F-1, F-1/A, F-3, SC 13D, SC 13G, SC 13G/A, SCHEDULE 13D/A, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:36:23.437096+00:00.

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
| 2026-10-23 | 6-K | 0001213900-26-112088 | — | [S03] |
| 2026-05-08 | 6-K | 0001213900-26-053918 | — | [S04] |
| 2026-03-18 | 3 | 0001213900-26-029425 | — | [S05] |
| 2026-03-18 | 3 | 0001213900-26-029414 | — | [S06] |
| 2026-03-18 | 3 | 0001213900-26-029408 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-29T16:14:13.115716+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001930179.json) — published not supplied; retrieved 2026-10-24T13:22:51.759433+00:00.

[S03] [6-K 0001213900-26-112088](https://www.sec.gov/Archives/edgar/data/1930179/000121390026112088/0001213900-26-112088-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S04] [6-K 0001213900-26-053918](https://www.sec.gov/Archives/edgar/data/1930179/000121390026053918/0001213900-26-053918-index.html) — published 2026-05-08; retrieved 2026-10-24T13:22:51.759433+00:00.

[S05] [3 0001213900-26-029425](https://www.sec.gov/Archives/edgar/data/1930179/000121390026029425/0001213900-26-029425-index.html) — published 2026-03-18; retrieved 2026-10-24T13:22:51.759433+00:00.

[S06] [3 0001213900-26-029414](https://www.sec.gov/Archives/edgar/data/1930179/000121390026029414/0001213900-26-029414-index.html) — published 2026-03-18; retrieved 2026-10-24T13:22:51.759433+00:00.

[S07] [3 0001213900-26-029408](https://www.sec.gov/Archives/edgar/data/1930179/000121390026029408/0001213900-26-029408-index.html) — published 2026-03-18; retrieved 2026-10-24T13:22:51.759433+00:00.

[S54] [20-F 0001213900-25-104705](https://www.sec.gov/Archives/edgar/data/1930179/000121390025104705/ea0262495-20f_arbiot.htm) — published 2025-10-31; retrieved 2026-10-24T13:47:36.644052+00:00.

Source release: `coverage-20261029-40909364006-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/52b6569b626a07b359d4a15742ebb633a0e48007/brain/companies/ARBB/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
