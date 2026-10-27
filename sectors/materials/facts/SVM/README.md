---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001340677
cik: '0001340677'
company_name: SILVERCORP METALS INC
tickers:
- SVM
status: stub
canonical_reviewed: false
as_of: '2026-10-27'
updated_at: '2026-10-27T15:30:18.641431+00:00'
reviewed_at: null
coverage_release: coverage-20261027-40530587641-1
source_commit: 77264ce478c0c699392c0a049f464d4fda44c9f8
financial_history_available: false
curated_research: null
financial_gap:
  reason: foreign_reporting_adapter
  next_action: Add support for the observed 20-F, 40-F or 6-K reporting forms and
    verify the actual accounting taxonomy before normalization.
  observed_forms:
  - '25'
  - 25-NSE
  - 40-F
  - 40-F/A
  - 40FR12B
  - '425'
  - 6-K
  - 6-K/A
  - 8-A12B
  - 8-A12B/A
  - CERTNYS
  - CORRESP
  - D
  - EFFECT
  - F-10
  - F-10/A
  - F-8
  - F-X
  - F-X/A
  - FWP
  - REGDEX
  - S-8
  - S-8 POS
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - SD
  - SUPPL
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001340677.json
    sha256: 8f7eb41105cc011c9886dacfcb8c170d8dc7f562ab3d40ce46530a42fd7ed3c4
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001340677.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: otherlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt
  published_at: null
  retrieved_at: '2026-10-27T15:25:35.250901+00:00'
  sha256: 3e845dbd702671bbfbbc700f50d314d4d4cb439640ee0fe6fbf22fc3344c7f42
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001340677.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 8f7eb41105cc011c9886dacfcb8c170d8dc7f562ab3d40ce46530a42fd7ed3c4
- id: S03
  title: 6-K 0001279569-26-000976
  url: https://www.sec.gov/Archives/edgar/data/1340677/000127956926000976/0001279569-26-000976-index.html
  published_at: '2026-10-20'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 6-K 0001104659-26-114418
  url: https://www.sec.gov/Archives/edgar/data/1340677/000110465926114418/0001104659-26-114418-index.html
  published_at: '2026-10-08'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 6-K 0001279569-26-000948
  url: https://www.sec.gov/Archives/edgar/data/1340677/000127956926000948/0001279569-26-000948-index.html
  published_at: '2026-10-05'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 6-K 0001104659-26-113420
  url: https://www.sec.gov/Archives/edgar/data/1340677/000110465926113420/0001104659-26-113420-index.html
  published_at: '2026-10-05'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 6-K 0001279569-26-000930
  url: https://www.sec.gov/Archives/edgar/data/1340677/000127956926000930/0001279569-26-000930-index.html
  published_at: '2026-09-30'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: '0001340677'
  classification_status: reported_sic
  entity_type: other
  name: SILVERCORP METALS INC
  sic: '1040'
  sic_description: Gold and Silver Ores
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 8f7eb41105cc011c9886dacfcb8c170d8dc7f562ab3d40ce46530a42fd7ed3c4
  url: https://data.sec.gov/submissions/CIK0001340677.json
listings:
- ticker: SVM
  exchange: NYSE_AMERICAN
  instrument_type: common_stock
research_filings:
- accession: 0001104659-26-079021
  filed: '2026-06-30'
  form: 40-F
  url: https://www.sec.gov/Archives/edgar/data/1340677/000110465926079021/0001104659-26-079021-index.html
- accession: 0001176256-18-000115
  filed: '2018-06-28'
  form: 40-F/A
  url: https://www.sec.gov/Archives/edgar/data/1340677/000117625618000115/0001176256-18-000115-index.html
- accession: 0001176256-13-000434
  filed: '2013-08-02'
  form: 40-F/A
  url: https://www.sec.gov/Archives/edgar/data/1340677/000117625613000434/0001176256-13-000434-index.html
- accession: 0000950123-09-013848
  filed: '2009-06-15'
  form: 40-F/A
  url: https://www.sec.gov/Archives/edgar/data/1340677/000095012309013848/0000950123-09-013848-index.html
- accession: 0001279569-26-000976
  filed: '2026-10-20'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1340677/000127956926000976/0001279569-26-000976-index.html
- accession: 0001104659-26-071052
  filed: '2026-06-05'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1340677/000110465926071052/0001104659-26-071052-index.html
- accession: 0001176256-13-000384
  filed: '2013-06-28'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1340677/000117625613000384/0001176256-13-000384-index.html
- accession: 0001176256-12-000639
  filed: '2012-09-10'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1340677/000117625612000639/0001176256-12-000639-index.html
- accession: 0001176256-11-000719
  filed: '2011-09-15'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1340677/000117625611000719/0001176256-11-000719-index.html
research_progress:
  stage: pending
  input_sha256: 808def72823269e9d61fbd14a814df38c312b34846203be0c84f86679530619c
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
  derived_observations: 0
  model_draft: false
  reviewed: false
sector_assignment:
  sector: materials
  method: project_sic_rule
  sic: '1040'
  sic_description: Gold and Silver Ores
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001340677.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/f974cdc6ffee05a6e0489d88d3e13c8eebf0b613/brain/companies/SVM/README.md
full_history_commit: f974cdc6ffee05a6e0489d88d3e13c8eebf0b613
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# SVM — SILVERCORP METALS INC

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/f974cdc6ffee05a6e0489d88d3e13c8eebf0b613/brain/companies/SVM/README.md)

## Business overview

Reported issuer name: **SILVERCORP METALS INC**. Stable SEC CIK: **0001340677**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| SVM | NYSE_AMERICAN | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **1040**: Gold and Silver Ores. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **materials**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

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
- Forms observed in the retained filing inventory: 25, 25-NSE, 40-F, 40-F/A, 40FR12B, 425, 6-K, 6-K/A, 8-A12B, 8-A12B/A, CERTNYS, CORRESP, D, EFFECT, F-10, F-10/A, F-8, F-X, F-X/A, FWP, REGDEX, S-8, S-8 POS, SC 13G, SC 13G/A, SCHEDULE 13G, SCHEDULE 13G/A, SD, SUPPL, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:32:42.857188+00:00.

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
| 2026-10-20 | 6-K | 0001279569-26-000976 | — | [S03] |
| 2026-10-08 | 6-K | 0001104659-26-114418 | — | [S04] |
| 2026-10-05 | 6-K | 0001279569-26-000948 | — | [S05] |
| 2026-10-05 | 6-K | 0001104659-26-113420 | — | [S06] |
| 2026-09-30 | 6-K | 0001279569-26-000930 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-27T15:25:35.250901+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001340677.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [6-K 0001279569-26-000976](https://www.sec.gov/Archives/edgar/data/1340677/000127956926000976/0001279569-26-000976-index.html) — published 2026-10-20; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [6-K 0001104659-26-114418](https://www.sec.gov/Archives/edgar/data/1340677/000110465926114418/0001104659-26-114418-index.html) — published 2026-10-08; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [6-K 0001279569-26-000948](https://www.sec.gov/Archives/edgar/data/1340677/000127956926000948/0001279569-26-000948-index.html) — published 2026-10-05; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [6-K 0001104659-26-113420](https://www.sec.gov/Archives/edgar/data/1340677/000110465926113420/0001104659-26-113420-index.html) — published 2026-10-05; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [6-K 0001279569-26-000930](https://www.sec.gov/Archives/edgar/data/1340677/000127956926000930/0001279569-26-000930-index.html) — published 2026-09-30; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261027-40530587641-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/f974cdc6ffee05a6e0489d88d3e13c8eebf0b613/brain/companies/SVM/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
