---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001036262
cik: '0001036262'
company_name: INTEST CORP
tickers:
- INTT
status: stub
canonical_reviewed: false
as_of: '2026-10-27'
updated_at: '2026-10-27T15:30:18.641431+00:00'
reviewed_at: null
coverage_release: coverage-20261027-40530587641-1
source_commit: 79ea404d09f86d838fefd71cf88a566d57bc57a2
financial_history_available: false
curated_research: null
financial_gap:
  reason: latest_filing_incomplete
  next_action: Resolve the latest financial filing/CompanyFacts mismatch; any historical
    bootstrap must keep the latest-period gap explicit.
  observed_forms:
  - 10-K
  - 10-K/A
  - 10-Q
  - 10-Q/A
  - '144'
  - '25'
  - '3'
  - '4'
  - 4/A
  - 424B5
  - '5'
  - 8-A12B
  - 8-A12G/A
  - 8-K
  - 8-K/A
  - ARS
  - CERTNYS
  - CORRESP
  - DEF 14A
  - DEFA14A
  - DEFR14A
  - EFFECT
  - NT 10-K
  - NT 10-Q
  - RW
  - S-3
  - S-3/A
  - S-8
  - S-8 POS
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - SD
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001036262.json
    sha256: 5b097de1b1f98e09e6a9acba24507493fac4978a592c28d642e9ef005bddbb96
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001036262.json
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
  url: https://data.sec.gov/submissions/CIK0001036262.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 5b097de1b1f98e09e6a9acba24507493fac4978a592c28d642e9ef005bddbb96
- id: S03
  title: 4 0000891839-26-000470
  url: https://www.sec.gov/Archives/edgar/data/1036262/000089183926000470/0000891839-26-000470-index.html
  published_at: '2026-10-13'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 8-K 0001036262-26-000057
  url: https://www.sec.gov/Archives/edgar/data/1036262/000103626226000057/0001036262-26-000057-index.html
  published_at: '2026-10-05'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 4 0000891839-26-000454
  url: https://www.sec.gov/Archives/edgar/data/1036262/000089183926000454/0000891839-26-000454-index.html
  published_at: '2026-10-05'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: S-8 0001036262-26-000053
  url: https://www.sec.gov/Archives/edgar/data/1036262/000103626226000053/0001036262-26-000053-index.html
  published_at: '2026-09-02'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 8-K 0001036262-26-000047
  url: https://www.sec.gov/Archives/edgar/data/1036262/000103626226000047/0001036262-26-000047-index.html
  published_at: '2026-08-17'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: '0001036262'
  classification_status: reported_sic
  entity_type: operating
  name: INTEST CORP
  sic: '3825'
  sic_description: Instruments For Meas & Testing of  Electricity & Elec Signals
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 5b097de1b1f98e09e6a9acba24507493fac4978a592c28d642e9ef005bddbb96
  url: https://data.sec.gov/submissions/CIK0001036262.json
listings:
- ticker: INTT
  exchange: NYSE_AMERICAN
  instrument_type: common_stock
research_filings:
- accession: 0001036262-26-000012
  filed: '2026-03-12'
  form: 10-K
  period_end: '2025-12-31'
  url: https://www.sec.gov/Archives/edgar/data/1036262/000103626226000012/0001036262-26-000012-index.html
- accession: 0001036262-26-000045
  filed: '2026-08-10'
  form: 10-Q
  period_end: '2026-06-30'
  url: https://www.sec.gov/Archives/edgar/data/1036262/000103626226000045/0001036262-26-000045-index.html
- accession: 0001036262-26-000024
  filed: '2026-04-28'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/1036262/000103626226000024/0001036262-26-000024-index.html
- accession: 0001036262-26-000057
  filed: '2026-10-05'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/1036262/000103626226000057/0001036262-26-000057-index.html
- accession: 0001437749-24-016634
  filed: '2024-05-14'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1036262/000143774924016634/0001437749-24-016634-index.html
- accession: 0001437749-20-022526
  filed: '2020-11-04'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1036262/000143774920022526/0001437749-20-022526-index.html
- accession: 0001437749-19-016562
  filed: '2019-08-13'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1036262/000143774919016562/0001437749-19-016562-index.html
- accession: 0001437749-18-004759
  filed: '2018-03-15'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1036262/000143774918004759/0001437749-18-004759-index.html
- accession: 0001437749-17-019372
  filed: '2017-11-14'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1036262/000143774917019372/0001437749-17-019372-index.html
- accession: 0001437749-17-014382
  filed: '2017-08-10'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1036262/000143774917014382/0001437749-17-014382-index.html
- accession: 0001036262-14-000022
  filed: '2014-05-09'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1036262/000103626214000022/0001036262-14-000022-index.html
- accession: 0001036262-14-000015
  filed: '2014-05-06'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1036262/000103626214000015/0001036262-14-000015-index.html
research_progress:
  stage: pending
  input_sha256: d7591a6d42e6bb9fe2a37aa6c567c7ec94d8c6b49df9d19c6fa819c8992e2065
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
  derived_observations: 0
  model_draft: false
  reviewed: false
sector_assignment:
  sector: information-technology
  method: project_sic_rule
  sic: '3825'
  sic_description: Instruments For Meas & Testing of  Electricity & Elec Signals
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001036262.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/ea9dd09e5d047ff0620d4500849876915bb10e87/brain/companies/INTT/README.md
full_history_commit: ea9dd09e5d047ff0620d4500849876915bb10e87
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# INTT — INTEST CORP

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/ea9dd09e5d047ff0620d4500849876915bb10e87/brain/companies/INTT/README.md)

## Business overview

Reported issuer name: **INTEST CORP**. Stable SEC CIK: **0001036262**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| INTT | NYSE_AMERICAN | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **3825**: Instruments For Meas & Testing of  Electricity & Elec Signals. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **information-technology**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

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
- Forms observed in the retained filing inventory: 10-K, 10-K/A, 10-Q, 10-Q/A, 144, 25, 3, 4, 4/A, 424B5, 5, 8-A12B, 8-A12G/A, 8-K, 8-K/A, ARS, CERTNYS, CORRESP, DEF 14A, DEFA14A, DEFR14A, EFFECT, NT 10-K, NT 10-Q, RW, S-3, S-3/A, S-8, S-8 POS, SC 13D, SC 13D/A, SC 13G, SC 13G/A, SCHEDULE 13G, SCHEDULE 13G/A, SD, UPLOAD
- Collector status: quality_review_required; last action: filings_only_financials_incomplete; last checked: 2026-10-24T13:31:02.073109+00:00.

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
| 2026-10-13 | 4 | 0000891839-26-000470 | — | [S03] |
| 2026-10-05 | 8-K | 0001036262-26-000057 | — | [S04] |
| 2026-10-05 | 4 | 0000891839-26-000454 | — | [S05] |
| 2026-09-02 | S-8 | 0001036262-26-000053 | — | [S06] |
| 2026-08-17 | 8-K | 0001036262-26-000047 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-27T15:25:35.250901+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001036262.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [4 0000891839-26-000470](https://www.sec.gov/Archives/edgar/data/1036262/000089183926000470/0000891839-26-000470-index.html) — published 2026-10-13; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [8-K 0001036262-26-000057](https://www.sec.gov/Archives/edgar/data/1036262/000103626226000057/0001036262-26-000057-index.html) — published 2026-10-05; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [4 0000891839-26-000454](https://www.sec.gov/Archives/edgar/data/1036262/000089183926000454/0000891839-26-000454-index.html) — published 2026-10-05; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [S-8 0001036262-26-000053](https://www.sec.gov/Archives/edgar/data/1036262/000103626226000053/0001036262-26-000053-index.html) — published 2026-09-02; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [8-K 0001036262-26-000047](https://www.sec.gov/Archives/edgar/data/1036262/000103626226000047/0001036262-26-000047-index.html) — published 2026-08-17; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261027-40530587641-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/ea9dd09e5d047ff0620d4500849876915bb10e87/brain/companies/INTT/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
