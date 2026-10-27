---
schema_version: 1
document_type: company_facts
company_id: company-cik-0000067088
cik: 0000067088
company_name: MITSUBISHI UFJ FINANCIAL GROUP INC
tickers:
- MUFG
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
  - 13F-HR
  - 15-15D
  - 20-F
  - '3'
  - '4'
  - 424B2
  - 424B5
  - '5'
  - 6-K
  - 6-K/A
  - CORRESP
  - F-3ASR
  - F-N
  - FWP
  - IRANNOTICE
  - N-PX
  - S-8
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13D/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0000067088.json
    sha256: 1fa93b7caa1a62c88348dd878e7db2977f0329cf81d5494d6cc97eeb7f241073
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0000067088.json
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
  url: https://data.sec.gov/submissions/CIK0000067088.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 1fa93b7caa1a62c88348dd878e7db2977f0329cf81d5494d6cc97eeb7f241073
- id: S03
  title: 4 0001193125-26-400093
  url: https://www.sec.gov/Archives/edgar/data/67088/000119312526400093/0001193125-26-400093-index.html
  published_at: '2026-09-24'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 6-K 0001193125-26-395145
  url: https://www.sec.gov/Archives/edgar/data/67088/000119312526395145/0001193125-26-395145-index.html
  published_at: '2026-09-18'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 424B2 0001193125-26-385848
  url: https://www.sec.gov/Archives/edgar/data/67088/000119312526385848/0001193125-26-385848-index.html
  published_at: '2026-09-09'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: FWP 0001193125-26-385822
  url: https://www.sec.gov/Archives/edgar/data/67088/000119312526385822/0001193125-26-385822-index.html
  published_at: '2026-09-09'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 424B5 0001193125-26-384276
  url: https://www.sec.gov/Archives/edgar/data/67088/000119312526384276/0001193125-26-384276-index.html
  published_at: '2026-09-08'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0000067088
  classification_status: reported_sic
  entity_type: other
  name: MITSUBISHI UFJ FINANCIAL GROUP INC
  sic: '6029'
  sic_description: Commercial Banks, NEC
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 1fa93b7caa1a62c88348dd878e7db2977f0329cf81d5494d6cc97eeb7f241073
  url: https://data.sec.gov/submissions/CIK0000067088.json
listings:
- ticker: MUFG
  exchange: NYSE
  instrument_type: common_stock
research_filings:
- accession: 0001628280-26-047095
  filed: '2026-07-06'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/67088/000162828026047095/0001628280-26-047095-index.html
- accession: 0001193125-26-395145
  filed: '2026-09-18'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/67088/000119312526395145/0001193125-26-395145-index.html
- accession: 0001193125-26-280192
  filed: '2026-06-24'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/67088/000119312526280192/0001193125-26-280192-index.html
- accession: 0001193125-26-038395
  filed: '2026-02-05'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/67088/000119312526038395/0001193125-26-038395-index.html
- accession: 0001193125-23-220703
  filed: '2023-08-25'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/67088/000119312523220703/0001193125-23-220703-index.html
- accession: 0001193125-22-165665
  filed: '2022-06-02'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/67088/000119312522165665/0001193125-22-165665-index.html
- accession: 0001193125-20-190725
  filed: '2020-07-10'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/67088/000119312520190725/0001193125-20-190725-index.html
- accession: 0001193125-18-168534
  filed: '2018-05-21'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/67088/000119312518168534/0001193125-18-168534-index.html
- accession: 0001193125-14-229369
  filed: '2014-06-09'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/67088/000119312514229369/0001193125-14-229369-index.html
- accession: 0001193125-12-020992
  filed: '2012-01-24'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/67088/000119312512020992/0001193125-12-020992-index.html
- accession: 0001193125-11-039680
  filed: '2011-02-18'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/67088/000119312511039680/0001193125-11-039680-index.html
research_progress:
  stage: pending
  input_sha256: c60ef173cf35305e2fd1cfaf0e2c303622df1a8f18ca14e59625b02d33602565
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
  derived_observations: 0
  model_draft: false
  reviewed: false
sector_assignment:
  sector: financials
  method: project_sic_rule
  sic: '6029'
  sic_description: Commercial Banks, NEC
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0000067088.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/f974cdc6ffee05a6e0489d88d3e13c8eebf0b613/brain/companies/MUFG/README.md
full_history_commit: f974cdc6ffee05a6e0489d88d3e13c8eebf0b613
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# MUFG — MITSUBISHI UFJ FINANCIAL GROUP INC

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/f974cdc6ffee05a6e0489d88d3e13c8eebf0b613/brain/companies/MUFG/README.md)

## Business overview

Reported issuer name: **MITSUBISHI UFJ FINANCIAL GROUP INC**. Stable SEC CIK: **0000067088**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| MUFG | NYSE | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **6029**: Commercial Banks, NEC. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **financials**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

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
- Forms observed in the retained filing inventory: 13F-HR, 15-15D, 20-F, 3, 4, 424B2, 424B5, 5, 6-K, 6-K/A, CORRESP, F-3ASR, F-N, FWP, IRANNOTICE, N-PX, S-8, SC 13D/A, SC 13G, SC 13G/A, SCHEDULE 13D/A, SCHEDULE 13G, SCHEDULE 13G/A, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:27:50.639359+00:00.

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
| 2026-09-24 | 4 | 0001193125-26-400093 | — | [S03] |
| 2026-09-18 | 6-K | 0001193125-26-395145 | — | [S04] |
| 2026-09-09 | 424B2 | 0001193125-26-385848 | — | [S05] |
| 2026-09-09 | FWP | 0001193125-26-385822 | — | [S06] |
| 2026-09-08 | 424B5 | 0001193125-26-384276 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-27T15:25:35.250901+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0000067088.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [4 0001193125-26-400093](https://www.sec.gov/Archives/edgar/data/67088/000119312526400093/0001193125-26-400093-index.html) — published 2026-09-24; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [6-K 0001193125-26-395145](https://www.sec.gov/Archives/edgar/data/67088/000119312526395145/0001193125-26-395145-index.html) — published 2026-09-18; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [424B2 0001193125-26-385848](https://www.sec.gov/Archives/edgar/data/67088/000119312526385848/0001193125-26-385848-index.html) — published 2026-09-09; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [FWP 0001193125-26-385822](https://www.sec.gov/Archives/edgar/data/67088/000119312526385822/0001193125-26-385822-index.html) — published 2026-09-09; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [424B5 0001193125-26-384276](https://www.sec.gov/Archives/edgar/data/67088/000119312526384276/0001193125-26-384276-index.html) — published 2026-09-08; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261027-40530587641-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/f974cdc6ffee05a6e0489d88d3e13c8eebf0b613/brain/companies/MUFG/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
