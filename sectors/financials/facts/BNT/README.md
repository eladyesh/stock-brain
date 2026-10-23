---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001837429
cik: 0001837429
company_name: Brookfield Wealth Solutions Ltd.
tickers:
- BNT
status: stub
canonical_reviewed: false
as_of: '2026-10-23'
updated_at: '2026-10-23T14:35:22.252685+00:00'
reviewed_at: null
coverage_release: coverage-20261023-39968262770-1
source_commit: 3f697433c3580d4ca83edbe44c66580ac926c8d7
financial_history_available: false
curated_research: null
financial_gap:
  reason: foreign_reporting_adapter
  next_action: Add support for the observed 20-F, 40-F or 6-K reporting forms and
    verify the actual accounting taxonomy before normalization.
  observed_forms:
  - 20-F
  - 25-NSE
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
  - F-1
  - F-1/A
  - F-3
  - F-4
  - F-4/A
  - F-N
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001837429.json
    sha256: 35d86620081f12be193806ca266013c03a3866a9408a20b369f16ff065e6febd
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001837429.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: otherlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt
  published_at: null
  retrieved_at: '2026-10-23T14:17:55.298415+00:00'
  sha256: be329650ef672c0314f0e16b2e41951f6af4ae314df9a04a32dc11ddb70b194e
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001837429.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 35d86620081f12be193806ca266013c03a3866a9408a20b369f16ff065e6febd
- id: S03
  title: 6-K 0001837429-26-000018
  url: https://www.sec.gov/Archives/edgar/data/1837429/000183742926000018/0001837429-26-000018-index.html
  published_at: '2026-08-14'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 6-K 0001171843-26-005475
  url: https://www.sec.gov/Archives/edgar/data/1837429/000117184326005475/0001171843-26-005475-index.html
  published_at: '2026-08-13'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 3 0000950142-26-002167
  url: https://www.sec.gov/Archives/edgar/data/1837429/000095014226002167/0000950142-26-002167-index.html
  published_at: '2026-07-27'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 6-K 0001104659-26-084375
  url: https://www.sec.gov/Archives/edgar/data/1837429/000110465926084375/0001104659-26-084375-index.html
  published_at: '2026-07-17'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 6-K 0001104659-26-071030
  url: https://www.sec.gov/Archives/edgar/data/1837429/000110465926071030/0001104659-26-071030-index.html
  published_at: '2026-06-05'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0001837429
  classification_status: reported_sic
  entity_type: other
  name: Brookfield Wealth Solutions Ltd.
  sic: '6399'
  sic_description: Insurance Carriers, NEC
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 35d86620081f12be193806ca266013c03a3866a9408a20b369f16ff065e6febd
  url: https://data.sec.gov/submissions/CIK0001837429.json
listings:
- ticker: BNT
  exchange: NYSE
  instrument_type: equity_candidate
research_filings:
- accession: 0001837429-26-000008
  filed: '2026-03-26'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1837429/000183742926000008/0001837429-26-000008-index.html
- accession: 0001837429-26-000018
  filed: '2026-08-14'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1837429/000183742926000018/0001837429-26-000018-index.html
research_progress:
  stage: pending
  input_sha256: 347b442ff6cf29c9bde5f9bed178bdbbec0ca142d9966c6800136d5ae4da6dba
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
  sic: '6399'
  sic_description: Insurance Carriers, NEC
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001837429.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/d523cff21b18141b9a37cddd98ad6af6e1a30fa5/brain/companies/BNT/README.md
full_history_commit: d523cff21b18141b9a37cddd98ad6af6e1a30fa5
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# BNT — Brookfield Wealth Solutions Ltd.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/d523cff21b18141b9a37cddd98ad6af6e1a30fa5/brain/companies/BNT/README.md)

## Business overview

Reported issuer name: **Brookfield Wealth Solutions Ltd.**. Stable SEC CIK: **0001837429**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| BNT | NYSE | equity_candidate | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **6399**: Insurance Carriers, NEC. [S02]

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
- Forms observed in the retained filing inventory: 20-F, 25-NSE, 3, 424B3, 425, 6-K, 8-A12B, CERT, CORRESP, DRS, DRS/A, DRSLTR, EFFECT, F-1, F-1/A, F-3, F-4, F-4/A, F-N, SC 13D, SC 13D/A, SC 13G, SC 13G/A, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-23T14:33:47.358614+00:00.

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
| 2026-08-14 | 6-K | 0001837429-26-000018 | — | [S03] |
| 2026-08-13 | 6-K | 0001171843-26-005475 | — | [S04] |
| 2026-07-27 | 3 | 0000950142-26-002167 | — | [S05] |
| 2026-07-17 | 6-K | 0001104659-26-084375 | — | [S06] |
| 2026-06-05 | 6-K | 0001104659-26-071030 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-23T14:17:55.298415+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001837429.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [6-K 0001837429-26-000018](https://www.sec.gov/Archives/edgar/data/1837429/000183742926000018/0001837429-26-000018-index.html) — published 2026-08-14; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [6-K 0001171843-26-005475](https://www.sec.gov/Archives/edgar/data/1837429/000117184326005475/0001171843-26-005475-index.html) — published 2026-08-13; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [3 0000950142-26-002167](https://www.sec.gov/Archives/edgar/data/1837429/000095014226002167/0000950142-26-002167-index.html) — published 2026-07-27; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [6-K 0001104659-26-084375](https://www.sec.gov/Archives/edgar/data/1837429/000110465926084375/0001104659-26-084375-index.html) — published 2026-07-17; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [6-K 0001104659-26-071030](https://www.sec.gov/Archives/edgar/data/1837429/000110465926071030/0001104659-26-071030-index.html) — published 2026-06-05; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261023-39968262770-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/d523cff21b18141b9a37cddd98ad6af6e1a30fa5/brain/companies/BNT/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
