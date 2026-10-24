---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001178819
cik: 0001178819
company_name: ALAMOS GOLD INC
tickers:
- AGI
status: stub
canonical_reviewed: false
as_of: '2026-10-24'
updated_at: '2026-10-24T13:37:20.730682+00:00'
reviewed_at: null
coverage_release: coverage-20261024-40097864335-1
source_commit: 88540b30f4be3c56b6c7fa8ba3dede59893b9834
financial_history_available: false
curated_research: null
financial_gap:
  reason: foreign_reporting_adapter
  next_action: Add support for the observed 20-F, 40-F or 6-K reporting forms and
    verify the actual accounting taxonomy before normalization.
  observed_forms:
  - '144'
  - 15F-12G
  - 20-F
  - 20-F/A
  - 20FR12G
  - 25-NSE
  - 40-F
  - 40-F/A
  - 40FR12B
  - 40FR12B/A
  - '425'
  - 6-K
  - 6-K/A
  - 8-A12B
  - 8-K12G3
  - CERTNYS
  - CORRESP
  - D
  - EFFECT
  - F-10
  - F-10/A
  - F-3
  - F-3D
  - F-3DPOS
  - F-X
  - FWP
  - REGDEX
  - RW
  - S-8
  - S-8 POS
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SC TO-T
  - SC TO-T/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - SD
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001178819.json
    sha256: e137359edfd2e2393eb9088270167779318774f91fc7a5dbb590d9b2c87f45dc
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001178819.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: otherlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt
  published_at: null
  retrieved_at: '2026-10-24T13:23:33.193038+00:00'
  sha256: 94335ed3f4abc4bbd58a4415d105d453184f5484eaf6a2884d1bfb0120d850c9
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001178819.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: e137359edfd2e2393eb9088270167779318774f91fc7a5dbb590d9b2c87f45dc
- id: S03
  title: 6-K 0001178819-26-000090
  url: https://www.sec.gov/Archives/edgar/data/1178819/000117881926000090/0001178819-26-000090-index.html
  published_at: '2026-09-30'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 144 0001193125-26-392040
  url: https://www.sec.gov/Archives/edgar/data/1178819/000119312526392040/0001193125-26-392040-index.html
  published_at: '2026-09-15'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 6-K 0001178819-26-000088
  url: https://www.sec.gov/Archives/edgar/data/1178819/000117881926000088/0001178819-26-000088-index.html
  published_at: '2026-08-31'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 6-K 0001178819-26-000086
  url: https://www.sec.gov/Archives/edgar/data/1178819/000117881926000086/0001178819-26-000086-index.html
  published_at: '2026-08-27'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: SCHEDULE 13G/A 0000869178-26-000058
  url: https://www.sec.gov/Archives/edgar/data/1178819/000086917826000058/0000869178-26-000058-index.html
  published_at: '2026-08-13'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0001178819
  classification_status: reported_sic
  entity_type: other
  name: ALAMOS GOLD INC
  sic: '1040'
  sic_description: Gold and Silver Ores
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: e137359edfd2e2393eb9088270167779318774f91fc7a5dbb590d9b2c87f45dc
  url: https://data.sec.gov/submissions/CIK0001178819.json
listings:
- ticker: AGI
  exchange: NYSE
  instrument_type: common_stock
research_filings:
- accession: 0001178819-26-000048
  filed: '2026-03-26'
  form: 40-F
  url: https://www.sec.gov/Archives/edgar/data/1178819/000117881926000048/0001178819-26-000048-index.html
- accession: 0001137171-06-000772
  filed: '2006-03-31'
  form: 40-F/A
  url: https://www.sec.gov/Archives/edgar/data/1178819/000113717106000772/0001137171-06-000772-index.html
- accession: 0001178819-26-000090
  filed: '2026-09-30'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1178819/000117881926000090/0001178819-26-000090-index.html
- accession: 0001178819-26-000038
  filed: '2026-02-19'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1178819/000117881926000038/0001178819-26-000038-index.html
research_progress:
  stage: pending
  input_sha256: 346d1b874d77b67411aec528ed7e5dcaafaafae8078f814968d05a2582f0e671
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
  source_url: https://data.sec.gov/submissions/CIK0001178819.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/aad7b261e69b9f214b9c5e20228523ca644ed670/brain/companies/AGI/README.md
full_history_commit: aad7b261e69b9f214b9c5e20228523ca644ed670
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# AGI — ALAMOS GOLD INC

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/aad7b261e69b9f214b9c5e20228523ca644ed670/brain/companies/AGI/README.md)

## Business overview

Reported issuer name: **ALAMOS GOLD INC**. Stable SEC CIK: **0001178819**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| AGI | NYSE | common_stock | 1 | [S01] |

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
- Forms observed in the retained filing inventory: 144, 15F-12G, 20-F, 20-F/A, 20FR12G, 25-NSE, 40-F, 40-F/A, 40FR12B, 40FR12B/A, 425, 6-K, 6-K/A, 8-A12B, 8-K12G3, CERTNYS, CORRESP, D, EFFECT, F-10, F-10/A, F-3, F-3D, F-3DPOS, F-X, FWP, REGDEX, RW, S-8, S-8 POS, SC 13D, SC 13D/A, SC 13G, SC 13G/A, SC TO-T, SC TO-T/A, SCHEDULE 13G, SCHEDULE 13G/A, SD, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:32:07.582061+00:00.

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
| 2026-09-30 | 6-K | 0001178819-26-000090 | — | [S03] |
| 2026-09-15 | 144 | 0001193125-26-392040 | — | [S04] |
| 2026-08-31 | 6-K | 0001178819-26-000088 | — | [S05] |
| 2026-08-27 | 6-K | 0001178819-26-000086 | — | [S06] |
| 2026-08-13 | SCHEDULE 13G/A | 0000869178-26-000058 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-24T13:23:33.193038+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001178819.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [6-K 0001178819-26-000090](https://www.sec.gov/Archives/edgar/data/1178819/000117881926000090/0001178819-26-000090-index.html) — published 2026-09-30; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [144 0001193125-26-392040](https://www.sec.gov/Archives/edgar/data/1178819/000119312526392040/0001193125-26-392040-index.html) — published 2026-09-15; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [6-K 0001178819-26-000088](https://www.sec.gov/Archives/edgar/data/1178819/000117881926000088/0001178819-26-000088-index.html) — published 2026-08-31; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [6-K 0001178819-26-000086](https://www.sec.gov/Archives/edgar/data/1178819/000117881926000086/0001178819-26-000086-index.html) — published 2026-08-27; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [SCHEDULE 13G/A 0000869178-26-000058](https://www.sec.gov/Archives/edgar/data/1178819/000086917826000058/0000869178-26-000058-index.html) — published 2026-08-13; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261024-40097864335-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/aad7b261e69b9f214b9c5e20228523ca644ed670/brain/companies/AGI/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
