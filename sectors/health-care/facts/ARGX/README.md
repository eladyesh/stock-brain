---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001697862
cik: 0001697862
company_name: ARGENX SE
tickers:
- ARGX
status: stub
canonical_reviewed: false
as_of: '2026-11-01'
updated_at: '2026-11-01T16:11:48.803754+00:00'
reviewed_at: null
coverage_release: coverage-20261101-41324509967-1
source_commit: 19d922c3a340e07ae75733aff6f0ed5f91038456
financial_history_available: false
curated_research: null
financial_gap:
  reason: foreign_reporting_adapter
  next_action: Add support for the observed 20-F, 40-F or 6-K reporting forms and
    verify the actual accounting taxonomy before normalization.
  observed_forms:
  - 20-F
  - 424B4
  - 424B5
  - 6-K
  - 8-A12B
  - CERTNAS
  - CORRESP
  - CT ORDER
  - DRS
  - DRS/A
  - DRSLTR
  - EFFECT
  - F-1
  - F-1/A
  - F-1MEF
  - F-3ASR
  - FWP
  - S-8
  - SC 13G
  - SC 13G/A
  - SC TO-C
  - SC TO-T
  - SC TO-T/A
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001697862.json
    sha256: 9fa23c74382ebe27ba3e6dc76f2da5598ed40801f77c38e5f4544b2b3a3f5230
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001697862.json
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
  url: https://data.sec.gov/submissions/CIK0001697862.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 9fa23c74382ebe27ba3e6dc76f2da5598ed40801f77c38e5f4544b2b3a3f5230
- id: S03
  title: 6-K 0001697862-26-000034
  url: https://www.sec.gov/Archives/edgar/data/1697862/000169786226000034/0001697862-26-000034-index.html
  published_at: '2026-10-22'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 6-K 0001104659-26-116751
  url: https://www.sec.gov/Archives/edgar/data/1697862/000110465926116751/0001104659-26-116751-index.html
  published_at: '2026-10-19'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 6-K 0001104659-26-114491
  url: https://www.sec.gov/Archives/edgar/data/1697862/000110465926114491/0001104659-26-114491-index.html
  published_at: '2026-10-08'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 6-K 0001104659-26-111631
  url: https://www.sec.gov/Archives/edgar/data/1697862/000110465926111631/0001104659-26-111631-index.html
  published_at: '2026-09-29'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 6-K 0001140361-26-034700
  url: https://www.sec.gov/Archives/edgar/data/1697862/000114036126034700/0001140361-26-034700-index.html
  published_at: '2026-08-27'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S54
  url: https://www.sec.gov/Archives/edgar/data/1697862/000169786226000032/argx-20251231.htm
  title: 20-F 0001697862-26-000032
  published_at: '2026-03-19'
  retrieved_at: '2026-11-14T18:41:18.775307+00:00'
  sha256: 52c41f3acbaf04ebb29039760c52dc5175eec1ce424188c8e3b8b2dbf0c0013e
issuer_classification:
  cik: 0001697862
  classification_status: reported_sic
  entity_type: other
  name: ARGENX SE
  sic: '2836'
  sic_description: Biological Products, (No Diagnostic Substances)
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 9fa23c74382ebe27ba3e6dc76f2da5598ed40801f77c38e5f4544b2b3a3f5230
  url: https://data.sec.gov/submissions/CIK0001697862.json
listings:
- ticker: ARGX
  exchange: NASDAQ
  instrument_type: depositary_receipt
research_filings:
- accession: 0001697862-26-000032
  filed: '2026-03-19'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1697862/000169786226000032/0001697862-26-000032-index.html
- accession: 0001697862-26-000034
  filed: '2026-10-22'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1697862/000169786226000034/0001697862-26-000034-index.html
research_progress:
  stage: evidence_collected
  input_sha256: cf6ca42880a370b8a9e9a3a097b4ad7b2fde5009a147ddc4b6bc451e80e07644
  last_attempt_at: '2026-11-14T18:39:40.176158+00:00'
  last_success_at: '2026-11-14T18:39:40.176158+00:00'
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
  sic: '2836'
  sic_description: Biological Products, (No Diagnostic Substances)
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001697862.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/2f077c0023bcb685dbbb970d68a962dd99ff31fe/brain/companies/ARGX/README.md
full_history_commit: 2f077c0023bcb685dbbb970d68a962dd99ff31fe
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# ARGX — ARGENX SE

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/2f077c0023bcb685dbbb970d68a962dd99ff31fe/brain/companies/ARGX/README.md)

## Business overview

Reported issuer name: **ARGENX SE**. Stable SEC CIK: **0001697862**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| ARGX | NASDAQ | depositary_receipt | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 20-F, filed 2026-03-19, L537:

> •the expansion of our business, including the further development of our sales and marketing abilities and our IIP, and [S54]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 20-F, filed 2026-03-19, L14946:

> reinvested in our business and that cash dividends will not be paid until we have an established revenue stream to [S54]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 20-F, filed 2026-03-19, L539:

> •the potential attributes, benefits, and side effects of our products and product candidates, including new indications, [S54]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 20-F, filed 2026-03-19, L620:

> government for our products and the reimbursement our customers may obtain from the government. Changes in such [S54]

## Industry and value chain

SEC-reported SIC **2836**: Biological Products, (No Diagnostic Substances). [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 20-F, filed 2026-03-19, L652:

> •Disruptions caused by our reliance on third parties for our raw materials and manufacturing process may delay or [S54]

Navigation sector: **health-care**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 20-F, filed 2026-03-19, L627:

> product candidates, our competitors may be able to sell products to treat the same conditions and our revenue may be [S54]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 20-F, filed 2026-03-19, L625:

> •If we fail to obtain orphan drug designation or we do not have valid and enforceable patents covering our products [S54]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 20-F, filed 2026-03-19, L793:

> of any of our products or product candidates into new markets will require us to further expand our sales and marketing [S54]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 20-F, filed 2026-03-19, L106:

> Indicate by check mark whether any of those error corrections are restatements that required a recovery analysis of incentive-based compensation received by any of the registrant’s executive officers [S54]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 20-F, filed 2026-03-19, L581:

> These include changes in general economic and business conditions. You should refer to ”Item 3.D — Risk Factors” of [S54]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 20-F, 424B4, 424B5, 6-K, 8-A12B, CERTNAS, CORRESP, CT ORDER, DRS, DRS/A, DRSLTR, EFFECT, F-1, F-1/A, F-1MEF, F-3ASR, FWP, S-8, SC 13G, SC 13G/A, SC TO-C, SC TO-T, SC TO-T/A, SCHEDULE 13G/A, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:35:06.279638+00:00.

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
| 2026-10-22 | 6-K | 0001697862-26-000034 | — | [S03] |
| 2026-10-19 | 6-K | 0001104659-26-116751 | — | [S04] |
| 2026-10-08 | 6-K | 0001104659-26-114491 | — | [S05] |
| 2026-09-29 | 6-K | 0001104659-26-111631 | — | [S06] |
| 2026-08-27 | 6-K | 0001140361-26-034700 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-11-01T16:07:03.070084+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001697862.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [6-K 0001697862-26-000034](https://www.sec.gov/Archives/edgar/data/1697862/000169786226000034/0001697862-26-000034-index.html) — published 2026-10-22; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [6-K 0001104659-26-116751](https://www.sec.gov/Archives/edgar/data/1697862/000110465926116751/0001104659-26-116751-index.html) — published 2026-10-19; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [6-K 0001104659-26-114491](https://www.sec.gov/Archives/edgar/data/1697862/000110465926114491/0001104659-26-114491-index.html) — published 2026-10-08; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [6-K 0001104659-26-111631](https://www.sec.gov/Archives/edgar/data/1697862/000110465926111631/0001104659-26-111631-index.html) — published 2026-09-29; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [6-K 0001140361-26-034700](https://www.sec.gov/Archives/edgar/data/1697862/000114036126034700/0001140361-26-034700-index.html) — published 2026-08-27; retrieved 2026-10-23T08:33:02.691743+00:00.

[S54] [20-F 0001697862-26-000032](https://www.sec.gov/Archives/edgar/data/1697862/000169786226000032/argx-20251231.htm) — published 2026-03-19; retrieved 2026-11-14T18:41:18.775307+00:00.

Source release: `coverage-20261101-41324509967-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/2f077c0023bcb685dbbb970d68a962dd99ff31fe/brain/companies/ARGX/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
