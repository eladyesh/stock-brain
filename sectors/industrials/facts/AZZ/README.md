---
schema_version: 1
document_type: company_facts
company_id: company-cik-0000008947
cik: 0000008947
company_name: AZZ INC
tickers:
- AZZ
status: stub
canonical_reviewed: false
as_of: '2026-10-26'
updated_at: '2026-10-26T16:16:21.148680+00:00'
reviewed_at: null
coverage_release: coverage-20261026-40356450615-1
source_commit: 1a2786cc3cffc8c9981965ab9c208315321385f6
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
  - 11-K
  - '144'
  - 15-15D
  - '3'
  - 3/A
  - '4'
  - 4/A
  - 424B5
  - '5'
  - 8-A12B
  - 8-K
  - 8-K/A
  - ARS
  - CERT
  - CORRESP
  - DEF 14A
  - DEFA14A
  - NT 10-K
  - NT 10-Q
  - NT 11-K
  - NT 11-K/A
  - PRE 14A
  - S-3ASR
  - S-8
  - S-8 POS
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - SD
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0000008947.json
    sha256: 1236ebcc5f2480d722322ec35bbf36f6f0f3094974ffe9a5e931ce91348b1bdd
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0000008947.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: otherlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt
  published_at: null
  retrieved_at: '2026-10-26T16:11:31.806354+00:00'
  sha256: 13932af456c860d259c16604472ab685dab69d880fb71eb6d5b53159497eb520
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0000008947.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 1236ebcc5f2480d722322ec35bbf36f6f0f3094974ffe9a5e931ce91348b1bdd
- id: S03
  title: 10-Q/A 0000008947-26-000198
  url: https://www.sec.gov/Archives/edgar/data/8947/000000894726000198/0000008947-26-000198-index.html
  published_at: '2026-10-15'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 8-K 0000008947-26-000188
  url: https://www.sec.gov/Archives/edgar/data/8947/000000894726000188/0000008947-26-000188-index.html
  published_at: '2026-10-13'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 10-Q 0000008947-26-000187
  url: https://www.sec.gov/Archives/edgar/data/8947/000000894726000187/0000008947-26-000187-index.html
  published_at: '2026-10-13'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 8-K 0000008947-26-000181
  url: https://www.sec.gov/Archives/edgar/data/8947/000000894726000181/0000008947-26-000181-index.html
  published_at: '2026-10-08'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 144 0001969223-26-000899
  url: https://www.sec.gov/Archives/edgar/data/8947/000196922326000899/0001969223-26-000899-index.html
  published_at: '2026-08-14'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0000008947
  classification_status: reported_sic
  entity_type: operating
  name: AZZ INC
  sic: '3470'
  sic_description: Coating, Engraving & Allied Services
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 1236ebcc5f2480d722322ec35bbf36f6f0f3094974ffe9a5e931ce91348b1bdd
  url: https://data.sec.gov/submissions/CIK0000008947.json
listings:
- ticker: AZZ
  exchange: NYSE
  instrument_type: equity_candidate
research_filings:
- accession: 0000008947-26-000068
  filed: '2026-04-22'
  form: 10-K
  period_end: '2026-02-28'
  url: https://www.sec.gov/Archives/edgar/data/8947/000000894726000068/0000008947-26-000068-index.html
- accession: 0000008947-26-000187
  filed: '2026-10-13'
  form: 10-Q
  period_end: '2026-08-31'
  url: https://www.sec.gov/Archives/edgar/data/8947/000000894726000187/0000008947-26-000187-index.html
- accession: 0000008947-26-000198
  filed: '2026-10-15'
  form: 10-Q/A
  period_end: '2026-08-31'
  url: https://www.sec.gov/Archives/edgar/data/8947/000000894726000198/0000008947-26-000198-index.html
- accession: 0001104659-26-066068
  filed: '2026-05-26'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/8947/000110465926066068/0001104659-26-066068-index.html
- accession: 0000008947-26-000188
  filed: '2026-10-13'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/8947/000000894726000188/0000008947-26-000188-index.html
- accession: 0000008947-26-000046
  filed: '2026-03-05'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/8947/000000894726000046/0000008947-26-000046-index.html
- accession: 0000008947-22-000158
  filed: '2022-07-29'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/8947/000000894722000158/0000008947-22-000158-index.html
- accession: 0000008947-20-000194
  filed: '2020-10-13'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/8947/000000894720000194/0000008947-20-000194-index.html
- accession: 0000008947-14-000114
  filed: '2014-07-23'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/8947/000000894714000114/0000008947-14-000114-index.html
research_progress:
  stage: pending
  input_sha256: e39003c8004cb705b57b2d74e9226d00058ce4d4277f9474fbd6d60f450cb1ca
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
  sic: '3470'
  sic_description: Coating, Engraving & Allied Services
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0000008947.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/30a5d1cd40fce8d4a64ca29ee815b726555957d3/brain/companies/AZZ/README.md
full_history_commit: 30a5d1cd40fce8d4a64ca29ee815b726555957d3
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# AZZ — AZZ INC

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/30a5d1cd40fce8d4a64ca29ee815b726555957d3/brain/companies/AZZ/README.md)

## Business overview

Reported issuer name: **AZZ INC**. Stable SEC CIK: **0000008947**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| AZZ | NYSE | equity_candidate | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **3470**: Coating, Engraving & Allied Services. [S02]

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
- Forms observed in the retained filing inventory: 10-K, 10-K/A, 10-Q, 10-Q/A, 11-K, 144, 15-15D, 3, 3/A, 4, 4/A, 424B5, 5, 8-A12B, 8-K, 8-K/A, ARS, CERT, CORRESP, DEF 14A, DEFA14A, NT 10-K, NT 10-Q, NT 11-K, NT 11-K/A, PRE 14A, S-3ASR, S-8, S-8 POS, SC 13G, SC 13G/A, SCHEDULE 13G, SCHEDULE 13G/A, SD, UPLOAD
- Collector status: quality_review_required; last action: filings_only_financials_incomplete; last checked: 2026-10-24T13:27:13.239658+00:00.

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
| 2026-10-15 | 10-Q/A | 0000008947-26-000198 | — | [S03] |
| 2026-10-13 | 8-K | 0000008947-26-000188 | — | [S04] |
| 2026-10-13 | 10-Q | 0000008947-26-000187 | — | [S05] |
| 2026-10-08 | 8-K | 0000008947-26-000181 | — | [S06] |
| 2026-08-14 | 144 | 0001969223-26-000899 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-26T16:11:31.806354+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0000008947.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [10-Q/A 0000008947-26-000198](https://www.sec.gov/Archives/edgar/data/8947/000000894726000198/0000008947-26-000198-index.html) — published 2026-10-15; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [8-K 0000008947-26-000188](https://www.sec.gov/Archives/edgar/data/8947/000000894726000188/0000008947-26-000188-index.html) — published 2026-10-13; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [10-Q 0000008947-26-000187](https://www.sec.gov/Archives/edgar/data/8947/000000894726000187/0000008947-26-000187-index.html) — published 2026-10-13; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [8-K 0000008947-26-000181](https://www.sec.gov/Archives/edgar/data/8947/000000894726000181/0000008947-26-000181-index.html) — published 2026-10-08; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [144 0001969223-26-000899](https://www.sec.gov/Archives/edgar/data/8947/000196922326000899/0001969223-26-000899-index.html) — published 2026-08-14; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261026-40356450615-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/30a5d1cd40fce8d4a64ca29ee815b726555957d3/brain/companies/AZZ/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
