---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001057877
cik: 0001057877
company_name: IDACORP INC
tickers:
- IDA
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
  reason: latest_filing_incomplete
  next_action: Resolve the latest financial filing/CompanyFacts mismatch; any historical
    bootstrap must keep the latest-period gap explicit.
  observed_forms:
  - 10-K
  - 10-Q
  - 11-K
  - '144'
  - 144/A
  - '3'
  - 3/A
  - '4'
  - 4/A
  - 424B3
  - 424B5
  - '5'
  - 8-K
  - ARS
  - CORRESP
  - CT ORDER
  - DEF 14A
  - DEFA14A
  - NO ACT
  - PRE 14A
  - S-3ASR
  - S-8
  - S-8 POS
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001057877.json
    sha256: 858d7b1797de6d752bd0184101068b6aeca26d4ba371ebb4467e9f229d79c6a6
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001057877.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
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
  url: https://data.sec.gov/submissions/CIK0001057877.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 858d7b1797de6d752bd0184101068b6aeca26d4ba371ebb4467e9f229d79c6a6
- id: S03
  title: SCHEDULE 13G/A 0000902219-26-000270
  url: https://www.sec.gov/Archives/edgar/data/1057877/000090221926000270/0000902219-26-000270-index.html
  published_at: '2026-08-13'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 8-K 0001057877-26-000130
  url: https://www.sec.gov/Archives/edgar/data/1057877/000105787726000130/0001057877-26-000130-index.html
  published_at: '2026-07-30'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 10-Q 0001057877-26-000129
  url: https://www.sec.gov/Archives/edgar/data/1057877/000105787726000129/0001057877-26-000129-index.html
  published_at: '2026-07-30'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 11-K 0001057877-26-000123
  url: https://www.sec.gov/Archives/edgar/data/1057877/000105787726000123/0001057877-26-000123-index.html
  published_at: '2026-06-25'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 4 0001057877-26-000118
  url: https://www.sec.gov/Archives/edgar/data/1057877/000105787726000118/0001057877-26-000118-index.html
  published_at: '2026-06-11'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0001057877
  classification_status: reported_sic
  entity_type: operating
  name: IDACORP INC
  sic: '4911'
  sic_description: Electric Services
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 858d7b1797de6d752bd0184101068b6aeca26d4ba371ebb4467e9f229d79c6a6
  url: https://data.sec.gov/submissions/CIK0001057877.json
listings:
- ticker: IDA
  exchange: NYSE
  instrument_type: common_stock
research_filings:
- accession: 0001057877-26-000028
  filed: '2026-02-19'
  form: 10-K
  period_end: '2025-12-31'
  url: https://www.sec.gov/Archives/edgar/data/1057877/000105787726000028/0001057877-26-000028-index.html
- accession: 0001057877-26-000129
  filed: '2026-07-30'
  form: 10-Q
  period_end: '2026-06-30'
  url: https://www.sec.gov/Archives/edgar/data/1057877/000105787726000129/0001057877-26-000129-index.html
- accession: 0001057877-26-000091
  filed: '2026-04-02'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/1057877/000105787726000091/0001057877-26-000091-index.html
- accession: 0001057877-26-000130
  filed: '2026-07-30'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/1057877/000105787726000130/0001057877-26-000130-index.html
research_progress:
  stage: pending
  input_sha256: 3cba63c03bc448b18d66acd6a050fe71d9ea94ffc4abe9f87362c7decafc3c51
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
  derived_observations: 0
  model_draft: false
  reviewed: false
sector_assignment:
  sector: utilities
  method: project_sic_rule
  sic: '4911'
  sic_description: Electric Services
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001057877.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/c26f59bc72c00102d2490e95b07449f8cd848491/brain/companies/IDA/README.md
full_history_commit: c26f59bc72c00102d2490e95b07449f8cd848491
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# IDA — IDACORP INC

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/c26f59bc72c00102d2490e95b07449f8cd848491/brain/companies/IDA/README.md)

## Business overview

Reported issuer name: **IDACORP INC**. Stable SEC CIK: **0001057877**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| IDA | NYSE | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **4911**: Electric Services. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **utilities**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

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
- Forms observed in the retained filing inventory: 10-K, 10-Q, 11-K, 144, 144/A, 3, 3/A, 4, 4/A, 424B3, 424B5, 5, 8-K, ARS, CORRESP, CT ORDER, DEF 14A, DEFA14A, NO ACT, PRE 14A, S-3ASR, S-8, S-8 POS, SC 13G, SC 13G/A, SCHEDULE 13G, SCHEDULE 13G/A, UPLOAD
- Collector status: quality_review_required; last action: filings_only_financials_incomplete; last checked: 2026-10-24T13:31:17.949113+00:00.

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
| 2026-08-13 | SCHEDULE 13G/A | 0000902219-26-000270 | — | [S03] |
| 2026-07-30 | 8-K | 0001057877-26-000130 | — | [S04] |
| 2026-07-30 | 10-Q | 0001057877-26-000129 | — | [S05] |
| 2026-06-25 | 11-K | 0001057877-26-000123 | — | [S06] |
| 2026-06-11 | 4 | 0001057877-26-000118 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-29T16:14:13.951866+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001057877.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [SCHEDULE 13G/A 0000902219-26-000270](https://www.sec.gov/Archives/edgar/data/1057877/000090221926000270/0000902219-26-000270-index.html) — published 2026-08-13; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [8-K 0001057877-26-000130](https://www.sec.gov/Archives/edgar/data/1057877/000105787726000130/0001057877-26-000130-index.html) — published 2026-07-30; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [10-Q 0001057877-26-000129](https://www.sec.gov/Archives/edgar/data/1057877/000105787726000129/0001057877-26-000129-index.html) — published 2026-07-30; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [11-K 0001057877-26-000123](https://www.sec.gov/Archives/edgar/data/1057877/000105787726000123/0001057877-26-000123-index.html) — published 2026-06-25; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [4 0001057877-26-000118](https://www.sec.gov/Archives/edgar/data/1057877/000105787726000118/0001057877-26-000118-index.html) — published 2026-06-11; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261029-40909364006-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/c26f59bc72c00102d2490e95b07449f8cd848491/brain/companies/IDA/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
