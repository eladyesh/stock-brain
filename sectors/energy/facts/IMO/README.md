---
schema_version: 1
document_type: company_facts
company_id: company-cik-0000049938
cik: 0000049938
company_name: IMPERIAL OIL LTD
tickers:
- IMO
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
  reason: latest_filing_incomplete
  next_action: Resolve the latest financial filing/CompanyFacts mismatch; any historical
    bootstrap must keep the latest-period gap explicit.
  observed_forms:
  - 10-K
  - 10-Q
  - 10-Q/A
  - 424B3
  - 8-K
  - 8-K/A
  - CORRESP
  - IRANNOTICE
  - S-8
  - SC 13G
  - SC 13G/A
  - SC TO-C
  - SC TO-I
  - SC TO-I/A
  - SCHEDULE 13G/A
  - SD
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0000049938.json
    sha256: ef1cdbecf0acc42fb9b183d8c434d7ddc643ea3c03b1432f4df3d59ed16b6a76
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0000049938.json
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
  url: https://data.sec.gov/submissions/CIK0000049938.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: ef1cdbecf0acc42fb9b183d8c434d7ddc643ea3c03b1432f4df3d59ed16b6a76
- id: S03
  title: 8-K 0000049938-26-000045
  url: https://www.sec.gov/Archives/edgar/data/49938/000004993826000045/0000049938-26-000045-index.html
  published_at: '2026-10-20'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: SD 0000049938-26-000042
  url: https://www.sec.gov/Archives/edgar/data/49938/000004993826000042/0000049938-26-000042-index.html
  published_at: '2026-09-25'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 10-Q 0000049938-26-000040
  url: https://www.sec.gov/Archives/edgar/data/49938/000004993826000040/0000049938-26-000040-index.html
  published_at: '2026-08-03'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 8-K 0000049938-26-000038
  url: https://www.sec.gov/Archives/edgar/data/49938/000004993826000038/0000049938-26-000038-index.html
  published_at: '2026-07-31'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 8-K 0000049938-26-000036
  url: https://www.sec.gov/Archives/edgar/data/49938/000004993826000036/0000049938-26-000036-index.html
  published_at: '2026-07-31'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0000049938
  classification_status: reported_sic
  entity_type: operating
  name: IMPERIAL OIL LTD
  sic: '2911'
  sic_description: Petroleum Refining
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: ef1cdbecf0acc42fb9b183d8c434d7ddc643ea3c03b1432f4df3d59ed16b6a76
  url: https://data.sec.gov/submissions/CIK0000049938.json
listings:
- ticker: IMO
  exchange: NYSE_AMERICAN
  instrument_type: common_stock
research_filings:
- accession: 0000049938-26-000009
  filed: '2026-02-18'
  form: 10-K
  period_end: '2025-12-31'
  url: https://www.sec.gov/Archives/edgar/data/49938/000004993826000009/0000049938-26-000009-index.html
- accession: 0000049938-26-000040
  filed: '2026-08-03'
  form: 10-Q
  period_end: '2026-06-30'
  url: https://www.sec.gov/Archives/edgar/data/49938/000004993826000040/0000049938-26-000040-index.html
- accession: 0000049938-26-000045
  filed: '2026-10-20'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/49938/000004993826000045/0000049938-26-000045-index.html
- accession: 0000049938-25-000073
  filed: '2025-11-26'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/49938/000004993825000073/0000049938-25-000073-index.html
- accession: 0001193125-20-001141
  filed: '2020-01-03'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/49938/000119312520001141/0001193125-20-001141-index.html
research_progress:
  stage: pending
  input_sha256: 43bfffaaaf56b56f47b3b4c83a0ed674d172ef246a7149592136f574e421032c
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
  derived_observations: 0
  model_draft: false
  reviewed: false
sector_assignment:
  sector: energy
  method: project_sic_rule
  sic: '2911'
  sic_description: Petroleum Refining
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0000049938.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/f974cdc6ffee05a6e0489d88d3e13c8eebf0b613/brain/companies/IMO/README.md
full_history_commit: f974cdc6ffee05a6e0489d88d3e13c8eebf0b613
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# IMO — IMPERIAL OIL LTD

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/f974cdc6ffee05a6e0489d88d3e13c8eebf0b613/brain/companies/IMO/README.md)

## Business overview

Reported issuer name: **IMPERIAL OIL LTD**. Stable SEC CIK: **0000049938**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| IMO | NYSE_AMERICAN | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **2911**: Petroleum Refining. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **energy**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

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
- Forms observed in the retained filing inventory: 10-K, 10-Q, 10-Q/A, 424B3, 8-K, 8-K/A, CORRESP, IRANNOTICE, S-8, SC 13G, SC 13G/A, SC TO-C, SC TO-I, SC TO-I/A, SCHEDULE 13G/A, SD, UPLOAD
- Collector status: quality_review_required; last action: filings_only_financials_incomplete; last checked: 2026-10-24T13:27:40.263099+00:00.

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
| 2026-10-20 | 8-K | 0000049938-26-000045 | — | [S03] |
| 2026-09-25 | SD | 0000049938-26-000042 | — | [S04] |
| 2026-08-03 | 10-Q | 0000049938-26-000040 | — | [S05] |
| 2026-07-31 | 8-K | 0000049938-26-000038 | — | [S06] |
| 2026-07-31 | 8-K | 0000049938-26-000036 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-27T15:25:35.250901+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0000049938.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [8-K 0000049938-26-000045](https://www.sec.gov/Archives/edgar/data/49938/000004993826000045/0000049938-26-000045-index.html) — published 2026-10-20; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [SD 0000049938-26-000042](https://www.sec.gov/Archives/edgar/data/49938/000004993826000042/0000049938-26-000042-index.html) — published 2026-09-25; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [10-Q 0000049938-26-000040](https://www.sec.gov/Archives/edgar/data/49938/000004993826000040/0000049938-26-000040-index.html) — published 2026-08-03; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [8-K 0000049938-26-000038](https://www.sec.gov/Archives/edgar/data/49938/000004993826000038/0000049938-26-000038-index.html) — published 2026-07-31; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [8-K 0000049938-26-000036](https://www.sec.gov/Archives/edgar/data/49938/000004993826000036/0000049938-26-000036-index.html) — published 2026-07-31; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261027-40530587641-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/f974cdc6ffee05a6e0489d88d3e13c8eebf0b613/brain/companies/IMO/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
