---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001565025
cik: '0001565025'
company_name: AMBEV S.A.
tickers:
- ABEV
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
  - '144'
  - 20-F
  - 20-F/A
  - '3'
  - 3/A
  - '4'
  - 6-K
  - 6-K/A
  - CORRESP
  - F-6EF
  - SC 13D/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001565025.json
    sha256: 74f5c3f34682b4a59d67ffb8c73d14eecabf176bb1f5385de3d53c706f26cd26
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001565025.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: otherlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt
  published_at: null
  retrieved_at: '2026-10-28T16:09:02.154543+00:00'
  sha256: 9075fbed01d898a38c24f9b203cac1b6a4eed581edb2da888a321447f3bb55cc
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001565025.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 74f5c3f34682b4a59d67ffb8c73d14eecabf176bb1f5385de3d53c706f26cd26
- id: S03
  title: 6-K 0001292814-26-004974
  url: https://www.sec.gov/Archives/edgar/data/1565025/000129281426004974/0001292814-26-004974-index.html
  published_at: '2026-10-22'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 6-K 0001292814-26-004926
  url: https://www.sec.gov/Archives/edgar/data/1565025/000129281426004926/0001292814-26-004926-index.html
  published_at: '2026-10-14'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 6-K 0001292814-26-004886
  url: https://www.sec.gov/Archives/edgar/data/1565025/000129281426004886/0001292814-26-004886-index.html
  published_at: '2026-10-09'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 6-K 0001292814-26-004884
  url: https://www.sec.gov/Archives/edgar/data/1565025/000129281426004884/0001292814-26-004884-index.html
  published_at: '2026-10-09'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 4 0001193125-26-418085
  url: https://www.sec.gov/Archives/edgar/data/1565025/000119312526418085/0001193125-26-418085-index.html
  published_at: '2026-10-08'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S54
  url: https://www.sec.gov/Archives/edgar/data/1565025/000129281426002779/abev20260505_6ka.htm
  title: 6-K/A 0001292814-26-002779
  published_at: '2026-05-05'
  retrieved_at: '2026-10-23T18:26:09.501960+00:00'
  sha256: 47f0e685474d749c8d190f51096311136553728b8e3af0105e717b71e09f17c4
- id: S57
  url: https://www.sec.gov/Archives/edgar/data/1565025/000129281426000640/abevform20f_2025.htm
  title: 20-F 0001292814-26-000640
  published_at: '2026-03-03'
  retrieved_at: '2026-10-23T18:26:04.039839+00:00'
  sha256: e2dbea34abb53ea1a4e4d6d8b7fa09672cd655e16039f506d282d48000a760bf
issuer_classification:
  cik: '0001565025'
  classification_status: reported_sic
  entity_type: other
  name: AMBEV S.A.
  sic: '2080'
  sic_description: Beverages
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 74f5c3f34682b4a59d67ffb8c73d14eecabf176bb1f5385de3d53c706f26cd26
  url: https://data.sec.gov/submissions/CIK0001565025.json
listings:
- ticker: ABEV
  exchange: NYSE
  instrument_type: depositary_receipt
research_filings:
- accession: 0001292814-26-000640
  filed: '2026-03-03'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1565025/000129281426000640/0001292814-26-000640-index.html
- accession: 0001292814-17-001473
  filed: '2017-05-31'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1565025/000129281417001473/0001292814-17-001473-index.html
- accession: 0001292814-26-004974
  filed: '2026-10-22'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1565025/000129281426004974/0001292814-26-004974-index.html
- accession: 0001292814-26-002779
  filed: '2026-05-05'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1565025/000129281426002779/0001292814-26-002779-index.html
- accession: 0001292814-26-002092
  filed: '2026-04-03'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1565025/000129281426002092/0001292814-26-002092-index.html
- accession: 0001292814-26-002090
  filed: '2026-04-03'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1565025/000129281426002090/0001292814-26-002090-index.html
- accession: 0001292814-26-000306
  filed: '2026-02-11'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1565025/000129281426000306/0001292814-26-000306-index.html
- accession: 0001292814-25-003753
  filed: '2025-11-03'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1565025/000129281425003753/0001292814-25-003753-index.html
- accession: 0001292814-25-001938
  filed: '2025-05-08'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1565025/000129281425001938/0001292814-25-001938-index.html
- accession: 0001292814-25-001914
  filed: '2025-05-08'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1565025/000129281425001914/0001292814-25-001914-index.html
- accession: 0001292814-25-001912
  filed: '2025-05-08'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1565025/000129281425001912/0001292814-25-001912-index.html
- accession: 0001292814-24-000377
  filed: '2024-02-09'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1565025/000129281424000377/0001292814-24-000377-index.html
research_progress:
  stage: evidence_collected
  input_sha256: 91ab4571b3379edfbae00e6be30b387a1a12315612cf0890a5ac6d8ba6fd599e
  last_attempt_at: '2026-10-23T18:20:50.371071+00:00'
  last_success_at: '2026-10-23T18:20:50.371071+00:00'
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
  sic: '2080'
  sic_description: Beverages
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001565025.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/d9e673c37aaa38580be4e36b4880e8ab015a9390/brain/companies/ABEV/README.md
full_history_commit: d9e673c37aaa38580be4e36b4880e8ab015a9390
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# ABEV — AMBEV S.A.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/d9e673c37aaa38580be4e36b4880e8ab015a9390/brain/companies/ABEV/README.md)

## Business overview

Reported issuer name: **AMBEV S.A.**. Stable SEC CIK: **0001565025**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| ABEV | NYSE | depositary_receipt | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 20-F, filed 2026-03-03, L269:

> organizations and associations, other contacts within the industries in which we operate and, in some cases, upon published statistical [S57]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 20-F, filed 2026-03-03, L2394:

> Antigua Brewery Limited, and Dominica Brewery & Beverages Limited, all of which form part of the CAC reportable segment. [S57]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 20-F, filed 2026-03-03, L274:

> in which we sell our products. Although we have no reason to believe any of this information or these reports are inaccurate in any material [S57]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 20-F, filed 2026-03-03, L2713:

> with our customers, and improving overall service level by: (i) providing products suggestions based on customers’ profile and product [S57]

## Industry and value chain

SEC-reported SIC **2080**: Beverages. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 20-F, filed 2026-03-03, L586:

> water reservoirs, availability of our suppliers to meet demand of raw and packaging materials, among other operational and environmental [S57]

Navigation sector: **consumer-staples**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 20-F, filed 2026-03-03, L267:

> us) or other statements presented in this Form 20-F regarding our position (or that of companies acquired by us) relative to our competitors [S57]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 20-F, filed 2026-03-03, L691:

> delays in our financial reporting or the loss of or damage to intellectual property through a security breach. As with all information [S57]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 20-F, filed 2026-03-03, L1216:

> condition. As we continue to expand our operations, there is a greater risk that we may be subject to negative publicity or misinformation [S57]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 6-K/A, filed 2026-05-05, L40:

> of Ambev S.A. (“Company”) that, as indicated in the Minutes of the meeting of the Board of Directors held on 04 May [S54]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 20-F, filed 2026-03-03, L393:

> those identified under “Item 3. Key Information—D. Risk Factors” in this annual report. As a result, investors are cautioned [S57]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 144, 20-F, 20-F/A, 3, 3/A, 4, 6-K, 6-K/A, CORRESP, F-6EF, SC 13D/A, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:34:10.703069+00:00.

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
| 2026-10-22 | 6-K | 0001292814-26-004974 | — | [S03] |
| 2026-10-14 | 6-K | 0001292814-26-004926 | — | [S04] |
| 2026-10-09 | 6-K | 0001292814-26-004886 | — | [S05] |
| 2026-10-09 | 6-K | 0001292814-26-004884 | — | [S06] |
| 2026-10-08 | 4 | 0001193125-26-418085 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-28T16:09:02.154543+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001565025.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [6-K 0001292814-26-004974](https://www.sec.gov/Archives/edgar/data/1565025/000129281426004974/0001292814-26-004974-index.html) — published 2026-10-22; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [6-K 0001292814-26-004926](https://www.sec.gov/Archives/edgar/data/1565025/000129281426004926/0001292814-26-004926-index.html) — published 2026-10-14; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [6-K 0001292814-26-004886](https://www.sec.gov/Archives/edgar/data/1565025/000129281426004886/0001292814-26-004886-index.html) — published 2026-10-09; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [6-K 0001292814-26-004884](https://www.sec.gov/Archives/edgar/data/1565025/000129281426004884/0001292814-26-004884-index.html) — published 2026-10-09; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [4 0001193125-26-418085](https://www.sec.gov/Archives/edgar/data/1565025/000119312526418085/0001193125-26-418085-index.html) — published 2026-10-08; retrieved 2026-10-23T08:33:02.691743+00:00.

[S54] [6-K/A 0001292814-26-002779](https://www.sec.gov/Archives/edgar/data/1565025/000129281426002779/abev20260505_6ka.htm) — published 2026-05-05; retrieved 2026-10-23T18:26:09.501960+00:00.

[S57] [20-F 0001292814-26-000640](https://www.sec.gov/Archives/edgar/data/1565025/000129281426000640/abevform20f_2025.htm) — published 2026-03-03; retrieved 2026-10-23T18:26:04.039839+00:00.

Source release: `coverage-20261028-40722802424-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/d9e673c37aaa38580be4e36b4880e8ab015a9390/brain/companies/ABEV/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
