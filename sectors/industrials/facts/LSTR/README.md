---
schema_version: 1
document_type: company_facts
company_id: company-cik-0000853816
cik: 0000853816
company_name: LANDSTAR SYSTEM INC
tickers:
- LSTR
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
  - 8-K
  - 8-K/A
  - CORRESP
  - DEF 14A
  - DEFA14A
  - NT 10-Q
  - PRE 14A
  - S-8
  - S-8 POS
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0000853816.json
    sha256: 187b64e439e8370a3a28b99778848a2840784122ac0076e47f93a30c88432c79
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0000853816.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
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
  url: https://data.sec.gov/submissions/CIK0000853816.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 187b64e439e8370a3a28b99778848a2840784122ac0076e47f93a30c88432c79
- id: S03
  title: SCHEDULE 13G/A 0001398344-26-014363
  url: https://www.sec.gov/Archives/edgar/data/853816/000139834426014363/0001398344-26-014363-index.html
  published_at: '2026-08-13'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 3 0000853816-26-000067
  url: https://www.sec.gov/Archives/edgar/data/853816/000085381626000067/0000853816-26-000067-index.html
  published_at: '2026-08-12'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 4 0000853816-26-000062
  url: https://www.sec.gov/Archives/edgar/data/853816/000085381626000062/0000853816-26-000062-index.html
  published_at: '2026-08-04'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 3 0000853816-26-000060
  url: https://www.sec.gov/Archives/edgar/data/853816/000085381626000060/0000853816-26-000060-index.html
  published_at: '2026-08-03'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 10-Q 0001193125-26-322966
  url: https://www.sec.gov/Archives/edgar/data/853816/000119312526322966/0001193125-26-322966-index.html
  published_at: '2026-07-29'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0000853816
  classification_status: reported_sic
  entity_type: operating
  name: LANDSTAR SYSTEM INC
  sic: '4213'
  sic_description: Trucking (No Local)
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 187b64e439e8370a3a28b99778848a2840784122ac0076e47f93a30c88432c79
  url: https://data.sec.gov/submissions/CIK0000853816.json
listings:
- ticker: LSTR
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001193125-26-064756
  filed: '2026-02-24'
  form: 10-K
  period_end: '2025-12-27'
  url: https://www.sec.gov/Archives/edgar/data/853816/000119312526064756/0001193125-26-064756-index.html
- accession: 0001193125-26-322966
  filed: '2026-07-29'
  form: 10-Q
  period_end: '2026-06-27'
  url: https://www.sec.gov/Archives/edgar/data/853816/000119312526322966/0001193125-26-322966-index.html
- accession: 0001193125-26-118697
  filed: '2026-03-23'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/853816/000119312526118697/0001193125-26-118697-index.html
- accession: 0001193125-26-321050
  filed: '2026-07-28'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/853816/000119312526321050/0001193125-26-321050-index.html
- accession: 0001193125-19-154019
  filed: '2019-05-22'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/853816/000119312519154019/0001193125-19-154019-index.html
research_progress:
  stage: pending
  input_sha256: de8e2fae89ce1461c3d790182cd22084e41dfd7e566c2f50679e9cd7d91c7a6f
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
  derived_observations: 0
  model_draft: false
  reviewed: false
sector_assignment:
  sector: industrials
  method: project_sic_rule
  sic: '4213'
  sic_description: Trucking (No Local)
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0000853816.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/52b6569b626a07b359d4a15742ebb633a0e48007/brain/companies/LSTR/README.md
full_history_commit: 52b6569b626a07b359d4a15742ebb633a0e48007
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# LSTR — LANDSTAR SYSTEM INC

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/52b6569b626a07b359d4a15742ebb633a0e48007/brain/companies/LSTR/README.md)

## Business overview

Reported issuer name: **LANDSTAR SYSTEM INC**. Stable SEC CIK: **0000853816**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| LSTR | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **4213**: Trucking (No Local). [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **industrials**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Resolve the latest financial filing/CompanyFacts mismatch; any historical bootstrap must keep the latest-period gap explicit.
- Forms observed in the retained filing inventory: 10-K, 10-Q, 144, 3, 4, 4/A, 8-K, 8-K/A, CORRESP, DEF 14A, DEFA14A, NT 10-Q, PRE 14A, S-8, S-8 POS, SC 13G, SC 13G/A, SCHEDULE 13G, SCHEDULE 13G/A, UPLOAD
- Collector status: quality_review_required; last action: filings_only_financials_incomplete; last checked: 2026-10-24T13:29:40.246167+00:00.

### Research work queue

Collection stage: **pending**. Extracted evidence is not a reviewed conclusion. Daily collection resumes from durable state; unchanged accessions are reused.

- **Business overview** (evidence or analysis still needed): Explain what the company does, who pays it, and why the business exists. Cite primary sources.
- **Revenue model and segments** (evidence or analysis still needed): Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.
- **Products and services** (evidence or analysis still needed): Describe the main products, customer problems solved, distribution, and product dependencies.
- **Customers and end markets** (evidence or analysis still needed): Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.
- **Industry and value chain** (evidence or analysis still needed): Place the company among suppliers, distribution channels, customers, and substitutes. Explain cyclicality and supply constraints.
- **Competitive landscape** (evidence or analysis still needed): Identify direct competitors and alternatives. Compare specific products or business segments, with sources.
- **Moat and differentiation** (evidence or analysis still needed): Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.
- **Growth drivers** (evidence or analysis still needed): Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.
- **Financial performance** (evidence or analysis still needed): Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.
- **Balance sheet and capital allocation** (evidence or analysis still needed): Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.
- **Management and governance** (evidence or analysis still needed): Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.
- **Valuation context** (evidence or analysis still needed): Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.
- **Catalysts** (evidence or analysis still needed): List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.
- **Risks and thesis breakers** (evidence or analysis still needed): Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.
- **Scenarios and open questions** (evidence or analysis still needed): Separate bull, base, and bear assumptions from facts. Record missing data, disputed evidence, and research questions without inventing answers.
- **Relationships and themes** (evidence or analysis still needed): Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.
- **Recent developments** (evidence or analysis still needed): Keep a dated, source-backed log of material changes. Distinguish the event date from the article date and explain what changed in the profile.

Calculation gaps: Validated financial history is missing.

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest five available filing metadata records; document bodies have not been analyzed here.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-08-13 | SCHEDULE 13G/A | 0001398344-26-014363 | — | [S03] |
| 2026-08-12 | 3 | 0000853816-26-000067 | — | [S04] |
| 2026-08-04 | 4 | 0000853816-26-000062 | — | [S05] |
| 2026-08-03 | 3 | 0000853816-26-000060 | — | [S06] |
| 2026-07-29 | 10-Q | 0001193125-26-322966 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-29T16:14:13.115716+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0000853816.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [SCHEDULE 13G/A 0001398344-26-014363](https://www.sec.gov/Archives/edgar/data/853816/000139834426014363/0001398344-26-014363-index.html) — published 2026-08-13; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [3 0000853816-26-000067](https://www.sec.gov/Archives/edgar/data/853816/000085381626000067/0000853816-26-000067-index.html) — published 2026-08-12; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [4 0000853816-26-000062](https://www.sec.gov/Archives/edgar/data/853816/000085381626000062/0000853816-26-000062-index.html) — published 2026-08-04; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [3 0000853816-26-000060](https://www.sec.gov/Archives/edgar/data/853816/000085381626000060/0000853816-26-000060-index.html) — published 2026-08-03; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [10-Q 0001193125-26-322966](https://www.sec.gov/Archives/edgar/data/853816/000119312526322966/0001193125-26-322966-index.html) — published 2026-07-29; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261029-40909364006-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/52b6569b626a07b359d4a15742ebb633a0e48007/brain/companies/LSTR/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
