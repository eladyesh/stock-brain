---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001434265
cik: '0001434265'
company_name: GENMAB A/S
tickers:
- GMAB
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
  - 12G3-2B
  - '144'
  - 20-F
  - '3'
  - '4'
  - 424B4
  - 6-K
  - 6-K/A
  - 8-A12B
  - ARS
  - CERT
  - CORRESP
  - DRS
  - DRS/A
  - DRSLTR
  - EFFECT
  - F-1
  - F-1/A
  - F-1MEF
  - F-6
  - F-6 POS
  - F-6EF
  - FWP
  - S-8
  - SC 13G
  - SC 13G/A
  - SC TO-C
  - SC TO-T
  - SC TO-T/A
  - SCHEDULE 13D
  - SCHEDULE 13D/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - SEC STAFF LETTER
  - SUPPL
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001434265.json
    sha256: 4451107a1c6d3a65abbeb3171b5531722ae035c9f33c742cc9ae783c49c6eb50
    retrieved_at: '2026-10-24T13:22:51.759433+00:00'
    archive: &id001
      member: CIK0001434265.json
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
  url: https://data.sec.gov/submissions/CIK0001434265.json
  published_at: null
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 4451107a1c6d3a65abbeb3171b5531722ae035c9f33c742cc9ae783c49c6eb50
- id: S03
  title: 6-K 0001434265-26-000138
  url: https://www.sec.gov/Archives/edgar/data/1434265/000143426526000138/0001434265-26-000138-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S04
  title: 6-K 0001434265-26-000136
  url: https://www.sec.gov/Archives/edgar/data/1434265/000143426526000136/0001434265-26-000136-index.html
  published_at: '2026-10-13'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S05
  title: 6-K 0001434265-26-000134
  url: https://www.sec.gov/Archives/edgar/data/1434265/000143426526000134/0001434265-26-000134-index.html
  published_at: '2026-10-07'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S06
  title: 6-K 0001434265-26-000132
  url: https://www.sec.gov/Archives/edgar/data/1434265/000143426526000132/0001434265-26-000132-index.html
  published_at: '2026-10-05'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S07
  title: SCHEDULE 13G 0000902664-26-004067
  url: https://www.sec.gov/Archives/edgar/data/1434265/000090266426004067/0000902664-26-004067-index.html
  published_at: '2026-10-05'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S54
  url: https://www.sec.gov/Archives/edgar/data/1434265/000143426526000014/gmab-20251231_d2.htm
  title: 20-F 0001434265-26-000014
  published_at: '2026-02-17'
  retrieved_at: '2026-10-27T15:40:36.172390+00:00'
  sha256: ec8b9e4334572c3459a6dd4cf56d443154c0259eef45079141adcf4310ebf3c4
issuer_classification:
  cik: '0001434265'
  classification_status: reported_sic
  entity_type: other
  name: GENMAB A/S
  sic: '2834'
  sic_description: Pharmaceutical Preparations
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 4451107a1c6d3a65abbeb3171b5531722ae035c9f33c742cc9ae783c49c6eb50
  url: https://data.sec.gov/submissions/CIK0001434265.json
listings:
- ticker: GMAB
  exchange: NASDAQ
  instrument_type: depositary_receipt
research_filings:
- accession: 0001434265-26-000014
  filed: '2026-02-17'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1434265/000143426526000014/0001434265-26-000014-index.html
- accession: 0001434265-26-000138
  filed: '2026-10-23'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1434265/000143426526000138/0001434265-26-000138-index.html
- accession: 0001558370-21-004330
  filed: '2021-04-15'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1434265/000155837021004330/0001558370-21-004330-index.html
research_progress:
  stage: evidence_collected
  input_sha256: b3919c91258cc89102ec306e3c7096b6c0d83937b2a03b395e7a80fa9c4cb6b7
  last_attempt_at: '2026-10-27T15:36:38.956292+00:00'
  last_success_at: '2026-10-27T15:36:38.956292+00:00'
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
  source_url: https://data.sec.gov/submissions/CIK0001434265.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/52b6569b626a07b359d4a15742ebb633a0e48007/brain/companies/GMAB/README.md
full_history_commit: 52b6569b626a07b359d4a15742ebb633a0e48007
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# GMAB — GENMAB A/S

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/52b6569b626a07b359d4a15742ebb633a0e48007/brain/companies/GMAB/README.md)

## Business overview

Reported issuer name: **GENMAB A/S**. Stable SEC CIK: **0001434265**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| GMAB | NASDAQ | depositary_receipt | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 20-F, filed 2026-02-17, L355:

> financial performance and condition, as well as our plans, objectives and expectations for our business operations and [S54]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 20-F, filed 2026-02-17, L390:

> and the ability of such CMOs to manufacture sufficient quantities of our products and product candidates for [S54]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **2834**: Pharmaceutical Preparations. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 20-F, filed 2026-02-17, L1233:

> and safety, human rights and responsible supply chain practices. At the same time, sentiment that is critical of certain ESG [S54]

Navigation sector: **health-care**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 20-F, filed 2026-02-17, L567:

> grow while we remain entitled to royalties. In particular, DARZALEX is subject to intense competition in the MM therapy [S54]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 20-F, filed 2026-02-17, L499:

> •The substantial majority of our revenue comes from royalties on sales of DARZALEX, and our patents underlying [S54]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 20-F, filed 2026-02-17, L1267:

> candidates and proprietary technologies, our strategy and future prospects are based, in particular, on our patent portfolio. [S54]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 20-F, filed 2026-02-17, L111:

> compensation received by any of the registrant’s executive officers during the relevant recovery period pursuant to § 240.10D-1(b). ☐ [S54]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 20-F, filed 2026-02-17, L427:

> Risk Factors.” These are factors that we think could cause our actual results to differ materially from expected results. [S54]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 12G3-2B, 144, 20-F, 3, 4, 424B4, 6-K, 6-K/A, 8-A12B, ARS, CERT, CORRESP, DRS, DRS/A, DRSLTR, EFFECT, F-1, F-1/A, F-1MEF, F-6, F-6 POS, F-6EF, FWP, S-8, SC 13G, SC 13G/A, SC TO-C, SC TO-T, SC TO-T/A, SCHEDULE 13D, SCHEDULE 13D/A, SCHEDULE 13G, SCHEDULE 13G/A, SEC STAFF LETTER, SUPPL, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:33:19.925305+00:00.

### Research work queue

Collection stage: **evidence_collected**. Extracted evidence is not a reviewed conclusion. Daily collection resumes from durable state; unchanged accessions are reused.

- **Business overview** (source excerpts available; assess the claim): Explain what the company does, who pays it, and why the business exists. Cite primary sources.
- **Revenue model and segments** (evidence or analysis still needed): Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.
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
| 2026-10-23 | 6-K | 0001434265-26-000138 | — | [S03] |
| 2026-10-13 | 6-K | 0001434265-26-000136 | — | [S04] |
| 2026-10-07 | 6-K | 0001434265-26-000134 | — | [S05] |
| 2026-10-05 | 6-K | 0001434265-26-000132 | — | [S06] |
| 2026-10-05 | SCHEDULE 13G | 0000902664-26-004067 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-29T16:14:13.115716+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001434265.json) — published not supplied; retrieved 2026-10-24T13:22:51.759433+00:00.

[S03] [6-K 0001434265-26-000138](https://www.sec.gov/Archives/edgar/data/1434265/000143426526000138/0001434265-26-000138-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S04] [6-K 0001434265-26-000136](https://www.sec.gov/Archives/edgar/data/1434265/000143426526000136/0001434265-26-000136-index.html) — published 2026-10-13; retrieved 2026-10-24T13:22:51.759433+00:00.

[S05] [6-K 0001434265-26-000134](https://www.sec.gov/Archives/edgar/data/1434265/000143426526000134/0001434265-26-000134-index.html) — published 2026-10-07; retrieved 2026-10-24T13:22:51.759433+00:00.

[S06] [6-K 0001434265-26-000132](https://www.sec.gov/Archives/edgar/data/1434265/000143426526000132/0001434265-26-000132-index.html) — published 2026-10-05; retrieved 2026-10-24T13:22:51.759433+00:00.

[S07] [SCHEDULE 13G 0000902664-26-004067](https://www.sec.gov/Archives/edgar/data/1434265/000090266426004067/0000902664-26-004067-index.html) — published 2026-10-05; retrieved 2026-10-24T13:22:51.759433+00:00.

[S54] [20-F 0001434265-26-000014](https://www.sec.gov/Archives/edgar/data/1434265/000143426526000014/gmab-20251231_d2.htm) — published 2026-02-17; retrieved 2026-10-27T15:40:36.172390+00:00.

Source release: `coverage-20261029-40909364006-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/52b6569b626a07b359d4a15742ebb633a0e48007/brain/companies/GMAB/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
