---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001845840
cik: 0001845840
company_name: Telesat Corp
tickers:
- TSAT
status: stub
canonical_reviewed: false
as_of: '2026-10-29'
updated_at: '2026-10-29T16:18:46.634043+00:00'
reviewed_at: null
coverage_release: coverage-20261029-40909364006-1
source_commit: aa19db75827ed3c73031b70e9a0a2e63baffc491
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
  - '425'
  - 6-K
  - 8-A12B
  - CERT
  - CORRESP
  - DRS
  - DRS/A
  - DRSLTR
  - EFFECT
  - F-4
  - F-4/A
  - S-8
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13D/A
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001845840.json
    sha256: e433bf8aa4182eda2534618428581831a7634fe69b27d4c4804b6bef7c2ac6b0
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001845840.json
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
  url: https://data.sec.gov/submissions/CIK0001845840.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: e433bf8aa4182eda2534618428581831a7634fe69b27d4c4804b6bef7c2ac6b0
- id: S03
  title: SCHEDULE 13G/A 0001104659-26-097110
  url: https://www.sec.gov/Archives/edgar/data/1845840/000110465926097110/0001104659-26-097110-index.html
  published_at: '2026-08-14'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 6-K 0001213900-26-088683
  url: https://www.sec.gov/Archives/edgar/data/1845840/000121390026088683/0001213900-26-088683-index.html
  published_at: '2026-08-13'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 6-K 0001213900-26-088672
  url: https://www.sec.gov/Archives/edgar/data/1845840/000121390026088672/0001213900-26-088672-index.html
  published_at: '2026-08-13'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 6-K 0001213900-26-084907
  url: https://www.sec.gov/Archives/edgar/data/1845840/000121390026084907/0001213900-26-084907-index.html
  published_at: '2026-08-04'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 6-K 0001213900-26-076539
  url: https://www.sec.gov/Archives/edgar/data/1845840/000121390026076539/0001213900-26-076539-index.html
  published_at: '2026-07-09'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0001845840
  classification_status: reported_sic
  entity_type: other
  name: Telesat Corp
  sic: '4899'
  sic_description: Communications Services, NEC
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: e433bf8aa4182eda2534618428581831a7634fe69b27d4c4804b6bef7c2ac6b0
  url: https://data.sec.gov/submissions/CIK0001845840.json
listings:
- ticker: TSAT
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001213900-26-028638
  filed: '2026-03-17'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1845840/000121390026028638/0001213900-26-028638-index.html
- accession: 0001213900-26-088683
  filed: '2026-08-13'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1845840/000121390026088683/0001213900-26-088683-index.html
research_progress:
  stage: pending
  input_sha256: 8539c78ed8d4878ca92263387243477428c5a92a7108c37b38500dc64fb77e8d
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
  derived_observations: 0
  model_draft: false
  reviewed: false
sector_assignment:
  sector: communication-services
  method: project_sic_rule
  sic: '4899'
  sic_description: Communications Services, NEC
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001845840.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/c26f59bc72c00102d2490e95b07449f8cd848491/brain/companies/TSAT/README.md
full_history_commit: c26f59bc72c00102d2490e95b07449f8cd848491
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# TSAT — Telesat Corp

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/c26f59bc72c00102d2490e95b07449f8cd848491/brain/companies/TSAT/README.md)

## Business overview

Reported issuer name: **Telesat Corp**. Stable SEC CIK: **0001845840**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| TSAT | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **4899**: Communications Services, NEC. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **communication-services**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

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
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 20-F, 3, 424B3, 425, 6-K, 8-A12B, CERT, CORRESP, DRS, DRS/A, DRSLTR, EFFECT, F-4, F-4/A, S-8, SC 13D, SC 13D/A, SC 13G, SC 13G/A, SCHEDULE 13D/A, SCHEDULE 13G/A, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:36:06.296749+00:00.

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
| 2026-08-14 | SCHEDULE 13G/A | 0001104659-26-097110 | — | [S03] |
| 2026-08-13 | 6-K | 0001213900-26-088683 | — | [S04] |
| 2026-08-13 | 6-K | 0001213900-26-088672 | — | [S05] |
| 2026-08-04 | 6-K | 0001213900-26-084907 | — | [S06] |
| 2026-07-09 | 6-K | 0001213900-26-076539 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-29T16:14:13.115716+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001845840.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [SCHEDULE 13G/A 0001104659-26-097110](https://www.sec.gov/Archives/edgar/data/1845840/000110465926097110/0001104659-26-097110-index.html) — published 2026-08-14; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [6-K 0001213900-26-088683](https://www.sec.gov/Archives/edgar/data/1845840/000121390026088683/0001213900-26-088683-index.html) — published 2026-08-13; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [6-K 0001213900-26-088672](https://www.sec.gov/Archives/edgar/data/1845840/000121390026088672/0001213900-26-088672-index.html) — published 2026-08-13; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [6-K 0001213900-26-084907](https://www.sec.gov/Archives/edgar/data/1845840/000121390026084907/0001213900-26-084907-index.html) — published 2026-08-04; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [6-K 0001213900-26-076539](https://www.sec.gov/Archives/edgar/data/1845840/000121390026076539/0001213900-26-076539-index.html) — published 2026-07-09; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261029-40909364006-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/c26f59bc72c00102d2490e95b07449f8cd848491/brain/companies/TSAT/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
