---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001809691
cik: 0001809691
company_name: AMTD Digital Inc.
tickers:
- HKD
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
  - 20-F/A
  - '3'
  - 424B4
  - 6-K
  - 8-A12B
  - CERT
  - CORRESP
  - DRS
  - DRSLTR
  - EFFECT
  - F-1
  - F-1/A
  - FWP
  - SC 13D
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13D/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001809691.json
    sha256: d686269aee642aaccd23d2bdde8c29e84fdb01b6854c3851adc47f8f1e70a360
    retrieved_at: '2026-10-24T13:22:51.759433+00:00'
    archive: &id001
      member: CIK0001809691.json
      sha256: 593fbbea6512ef5ec729a5e513c465fbedaac8a66602c0abe00d0ba5a4d18732
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: otherlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt
  published_at: null
  retrieved_at: '2026-10-29T16:14:13.951866+00:00'
  sha256: 2ac9bdaf5d770442eb34b0b33eb6a5240dbd11a3f2077f7b88051dbb82d4313b
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001809691.json
  published_at: null
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: d686269aee642aaccd23d2bdde8c29e84fdb01b6854c3851adc47f8f1e70a360
- id: S03
  title: 6-K 0001213900-26-112140
  url: https://www.sec.gov/Archives/edgar/data/1809691/000121390026112140/0001213900-26-112140-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S04
  title: 6-K 0001213900-26-104926
  url: https://www.sec.gov/Archives/edgar/data/1809691/000121390026104926/0001213900-26-104926-index.html
  published_at: '2026-09-30'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S05
  title: 6-K 0001213900-26-069881
  url: https://www.sec.gov/Archives/edgar/data/1809691/000121390026069881/0001213900-26-069881-index.html
  published_at: '2026-06-18'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S06
  title: 6-K 0001213900-26-064153
  url: https://www.sec.gov/Archives/edgar/data/1809691/000121390026064153/0001213900-26-064153-index.html
  published_at: '2026-06-02'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S07
  title: 6-K 0001213900-26-062806
  url: https://www.sec.gov/Archives/edgar/data/1809691/000121390026062806/0001213900-26-062806-index.html
  published_at: '2026-05-29'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S54
  url: https://www.sec.gov/Archives/edgar/data/1809691/000121390026021555/ea0276786-20f_amtd.htm
  title: 20-F 0001213900-26-021555
  published_at: '2026-02-27'
  retrieved_at: '2026-10-27T15:43:25.773800+00:00'
  sha256: d84b9bab081f8358ba17e402947b7316823727237c8c3817f741de905520ec93
issuer_classification:
  cik: 0001809691
  classification_status: reported_sic
  entity_type: other
  name: AMTD Digital Inc.
  sic: '6199'
  sic_description: Finance Services
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: d686269aee642aaccd23d2bdde8c29e84fdb01b6854c3851adc47f8f1e70a360
  url: https://data.sec.gov/submissions/CIK0001809691.json
listings:
- ticker: HKD
  exchange: NYSE
  instrument_type: depositary_receipt
research_filings:
- accession: 0001213900-26-021555
  filed: '2026-02-27'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1809691/000121390026021555/0001213900-26-021555-index.html
- accession: 0001213900-26-017928
  filed: '2026-02-18'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1809691/000121390026017928/0001213900-26-017928-index.html
- accession: 0001213900-25-014872
  filed: '2025-02-18'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1809691/000121390025014872/0001213900-25-014872-index.html
- accession: 0001213900-26-112140
  filed: '2026-10-23'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1809691/000121390026112140/0001213900-26-112140-index.html
research_progress:
  stage: evidence_collected
  input_sha256: 2fcc4b5adf1fbe055523739dd9b53dc47baab05533a8663c2f17cf069e21ac27
  last_attempt_at: '2026-10-27T15:36:38.956292+00:00'
  last_success_at: '2026-10-27T15:36:38.956292+00:00'
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
  sector: financials
  method: project_sic_rule
  sic: '6199'
  sic_description: Finance Services
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001809691.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/52b6569b626a07b359d4a15742ebb633a0e48007/brain/companies/HKD/README.md
full_history_commit: 52b6569b626a07b359d4a15742ebb633a0e48007
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# HKD — AMTD Digital Inc.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/52b6569b626a07b359d4a15742ebb633a0e48007/brain/companies/HKD/README.md)

## Business overview

Reported issuer name: **AMTD Digital Inc.**. Stable SEC CIK: **0001809691**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| HKD | NYSE | depositary_receipt | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 20-F, filed 2026-02-27, L324:

> different from and worse than what we expect. Moreover, we operate in an evolving environment. New risk factors and uncertainties emerge [S54]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 20-F, filed 2026-02-27, L3227:

> entertainment landscape. Our success in attracting and retaining a loyal audience directly impacts our revenue streams, whether through [S54]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 20-F, filed 2026-02-27, L311:

> \| \| ● \| our expectations regarding demand for and market acceptance of our products and services; [S54]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 20-F, filed 2026-02-27, L499:

> which we develop relationships with our customers, and therefore can affect our ability to compete effectively. In the hospitality sector, [S54]

## Industry and value chain

SEC-reported SIC **6199**: Finance Services. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 20-F, filed 2026-02-27, L647:

> to the public or to our workforce, or impacting overall macroeconomic conditions, such as supply chain disruptions, political instability [S54]

Navigation sector: **financials**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 20-F, filed 2026-02-27, L468:

> competition, we need to continually introduce new products and services, improve our existing products and services, or adjust and optimize [S54]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 20-F, filed 2026-02-27, L406:

> \| \| ● \| Our business may suffer if the intellectual property we use in our business is not protected. [S54]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 20-F, filed 2026-02-27, L393:

> \| \| ● \| We face numerous risks and challenges as we continue to operate and expand our businesses and undertake new businesses across a broad [S54]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 20-F, filed 2026-02-27, L96:

> that required a recovery analysis of incentive-based compensation received by any of the registrant’s executive officers during [S54]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 20-F, filed 2026-02-27, L324:

> different from and worse than what we expect. Moreover, we operate in an evolving environment. New risk factors and uncertainties emerge [S54]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 20-F, 20-F/A, 3, 424B4, 6-K, 8-A12B, CERT, CORRESP, DRS, DRSLTR, EFFECT, F-1, F-1/A, FWP, SC 13D, SC 13G, SC 13G/A, SCHEDULE 13D/A, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:35:45.772365+00:00.

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
| 2026-10-23 | 6-K | 0001213900-26-112140 | — | [S03] |
| 2026-09-30 | 6-K | 0001213900-26-104926 | — | [S04] |
| 2026-06-18 | 6-K | 0001213900-26-069881 | — | [S05] |
| 2026-06-02 | 6-K | 0001213900-26-064153 | — | [S06] |
| 2026-05-29 | 6-K | 0001213900-26-062806 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-29T16:14:13.951866+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001809691.json) — published not supplied; retrieved 2026-10-24T13:22:51.759433+00:00.

[S03] [6-K 0001213900-26-112140](https://www.sec.gov/Archives/edgar/data/1809691/000121390026112140/0001213900-26-112140-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S04] [6-K 0001213900-26-104926](https://www.sec.gov/Archives/edgar/data/1809691/000121390026104926/0001213900-26-104926-index.html) — published 2026-09-30; retrieved 2026-10-24T13:22:51.759433+00:00.

[S05] [6-K 0001213900-26-069881](https://www.sec.gov/Archives/edgar/data/1809691/000121390026069881/0001213900-26-069881-index.html) — published 2026-06-18; retrieved 2026-10-24T13:22:51.759433+00:00.

[S06] [6-K 0001213900-26-064153](https://www.sec.gov/Archives/edgar/data/1809691/000121390026064153/0001213900-26-064153-index.html) — published 2026-06-02; retrieved 2026-10-24T13:22:51.759433+00:00.

[S07] [6-K 0001213900-26-062806](https://www.sec.gov/Archives/edgar/data/1809691/000121390026062806/0001213900-26-062806-index.html) — published 2026-05-29; retrieved 2026-10-24T13:22:51.759433+00:00.

[S54] [20-F 0001213900-26-021555](https://www.sec.gov/Archives/edgar/data/1809691/000121390026021555/ea0276786-20f_amtd.htm) — published 2026-02-27; retrieved 2026-10-27T15:43:25.773800+00:00.

Source release: `coverage-20261029-40909364006-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/52b6569b626a07b359d4a15742ebb633a0e48007/brain/companies/HKD/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
