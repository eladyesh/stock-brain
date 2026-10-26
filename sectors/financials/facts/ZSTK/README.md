---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001790169
cik: 0001790169
company_name: ZeroStack Corp.
tickers:
- ZSTK
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
  - 1-A
  - 1-A POS
  - 1-A/A
  - 1-K
  - 1-SA
  - 1-U
  - 10-K
  - 10-K/A
  - 10-Q
  - '144'
  - 20-F
  - 20-F/A
  - 253G2
  - 253G3
  - '3'
  - '4'
  - 424B3
  - 424B4
  - 424B5
  - 6-K
  - 6-K/A
  - 8-A12B
  - 8-K
  - 8-K/A
  - 8-K12B
  - ARS
  - AW
  - CERT
  - CORRESP
  - D
  - DEF 14A
  - DEFA14A
  - DRS
  - DRS/A
  - EFFECT
  - F-1
  - F-1/A
  - F-3
  - F-X
  - FWP
  - NT 20-F
  - POS AM
  - PRE 14A
  - PRER14A
  - QUALIF
  - S-1
  - S-3
  - S-3/A
  - S-4
  - S-4 POS
  - S-8
  - S-8 POS
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13D
  - SCHEDULE 13D/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001790169.json
    sha256: 781c8799b71648cd1ee3130abb4109005f1dca84ef1d30eab5bdccd0141985d6
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001790169.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: nasdaqlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt
  published_at: null
  retrieved_at: '2026-10-26T16:11:31.228419+00:00'
  sha256: 74146fcda2f9b3b43b06280df0ad9584dffa78b2237460917eda3c2892e7a706
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001790169.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 781c8799b71648cd1ee3130abb4109005f1dca84ef1d30eab5bdccd0141985d6
- id: S03
  title: SCHEDULE 13G 0002155749-26-000003
  url: https://www.sec.gov/Archives/edgar/data/1790169/000215574926000003/0002155749-26-000003-index.html
  published_at: '2026-10-19'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: EFFECT 9999999995-26-002967
  url: https://www.sec.gov/Archives/edgar/data/1790169/999999999526002967/9999999995-26-002967-index.html
  published_at: '2026-09-15'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: POS AM 0001062993-26-004837
  url: https://www.sec.gov/Archives/edgar/data/1790169/000106299326004837/0001062993-26-004837-index.html
  published_at: '2026-09-04'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: AW 0001062993-26-004835
  url: https://www.sec.gov/Archives/edgar/data/1790169/000106299326004835/0001062993-26-004835-index.html
  published_at: '2026-09-04'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: SCHEDULE 13G 0000912282-26-001229
  url: https://www.sec.gov/Archives/edgar/data/1790169/000091228226001229/0000912282-26-001229-index.html
  published_at: '2026-09-04'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0001790169
  classification_status: reported_sic
  entity_type: operating
  name: ZeroStack Corp.
  sic: '6199'
  sic_description: Finance Services
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 781c8799b71648cd1ee3130abb4109005f1dca84ef1d30eab5bdccd0141985d6
  url: https://data.sec.gov/submissions/CIK0001790169.json
listings:
- ticker: ZSTK
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001062993-26-001203
  filed: '2026-02-27'
  form: 10-K
  period_end: '2025-12-31'
  url: https://www.sec.gov/Archives/edgar/data/1790169/000106299326001203/0001062993-26-001203-index.html
- accession: 0001062993-26-003961
  filed: '2026-07-31'
  form: 10-Q
  period_end: '2026-06-30'
  url: https://www.sec.gov/Archives/edgar/data/1790169/000106299326003961/0001062993-26-003961-index.html
- accession: 0001062993-25-016455
  filed: '2025-11-04'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/1790169/000106299325016455/0001062993-25-016455-index.html
- accession: 0001062993-26-004559
  filed: '2026-08-21'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/1790169/000106299326004559/0001062993-26-004559-index.html
- accession: 0001062993-24-011760
  filed: '2024-06-04'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1790169/000106299324011760/0001062993-24-011760-index.html
research_progress:
  stage: pending
  input_sha256: 02554d29c3de8f2319c72db40b143e6e649318882813878ee43e2334dd51341e
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
  sic: '6199'
  sic_description: Finance Services
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001790169.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/30a5d1cd40fce8d4a64ca29ee815b726555957d3/brain/companies/ZSTK/README.md
full_history_commit: 30a5d1cd40fce8d4a64ca29ee815b726555957d3
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# ZSTK — ZeroStack Corp.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/30a5d1cd40fce8d4a64ca29ee815b726555957d3/brain/companies/ZSTK/README.md)

## Business overview

Reported issuer name: **ZeroStack Corp.**. Stable SEC CIK: **0001790169**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| ZSTK | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **6199**: Finance Services. [S02]

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
- Next collection task: Resolve the latest financial filing/CompanyFacts mismatch; any historical bootstrap must keep the latest-period gap explicit.
- Forms observed in the retained filing inventory: 1-A, 1-A POS, 1-A/A, 1-K, 1-SA, 1-U, 10-K, 10-K/A, 10-Q, 144, 20-F, 20-F/A, 253G2, 253G3, 3, 4, 424B3, 424B4, 424B5, 6-K, 6-K/A, 8-A12B, 8-K, 8-K/A, 8-K12B, ARS, AW, CERT, CORRESP, D, DEF 14A, DEFA14A, DRS, DRS/A, EFFECT, F-1, F-1/A, F-3, F-X, FWP, NT 20-F, POS AM, PRE 14A, PRER14A, QUALIF, S-1, S-3, S-3/A, S-4, S-4 POS, S-8, S-8 POS, SC 13D, SC 13D/A, SC 13G, SC 13G/A, SCHEDULE 13D, SCHEDULE 13D/A, SCHEDULE 13G, SCHEDULE 13G/A, UPLOAD
- Collector status: quality_review_required; last action: filings_only_financials_incomplete; last checked: 2026-10-24T13:35:38.963375+00:00.

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
| 2026-10-19 | SCHEDULE 13G | 0002155749-26-000003 | — | [S03] |
| 2026-09-15 | EFFECT | 9999999995-26-002967 | — | [S04] |
| 2026-09-04 | POS AM | 0001062993-26-004837 | — | [S05] |
| 2026-09-04 | AW | 0001062993-26-004835 | — | [S06] |
| 2026-09-04 | SCHEDULE 13G | 0000912282-26-001229 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-26T16:11:31.228419+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001790169.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [SCHEDULE 13G 0002155749-26-000003](https://www.sec.gov/Archives/edgar/data/1790169/000215574926000003/0002155749-26-000003-index.html) — published 2026-10-19; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [EFFECT 9999999995-26-002967](https://www.sec.gov/Archives/edgar/data/1790169/999999999526002967/9999999995-26-002967-index.html) — published 2026-09-15; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [POS AM 0001062993-26-004837](https://www.sec.gov/Archives/edgar/data/1790169/000106299326004837/0001062993-26-004837-index.html) — published 2026-09-04; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [AW 0001062993-26-004835](https://www.sec.gov/Archives/edgar/data/1790169/000106299326004835/0001062993-26-004835-index.html) — published 2026-09-04; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [SCHEDULE 13G 0000912282-26-001229](https://www.sec.gov/Archives/edgar/data/1790169/000091228226001229/0000912282-26-001229-index.html) — published 2026-09-04; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261026-40356450615-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/30a5d1cd40fce8d4a64ca29ee815b726555957d3/brain/companies/ZSTK/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
