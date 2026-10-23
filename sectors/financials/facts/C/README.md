---
schema_version: 1
document_type: company_facts
company_id: company-cik-0000831001
cik: 0000831001
company_name: CITIGROUP INC
tickers:
- C
- C$R
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
  reason: latest_filing_incomplete
  next_action: Resolve the latest financial filing/CompanyFacts mismatch; any historical
    bootstrap must keep the latest-period gap explicit.
  observed_forms:
  - '4'
  - 424B2
  - 424B3
  - 424B8
  - 8-K
  - FWP
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0000831001.json
    sha256: 977ecf280c6e1a855501ac8244519a268b7c817de7f5571d3dd333f74f5296f0
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0000831001.json
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
  url: https://data.sec.gov/submissions/CIK0000831001.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 977ecf280c6e1a855501ac8244519a268b7c817de7f5571d3dd333f74f5296f0
- id: S03
  title: 424B2 0001918704-26-032394
  url: https://www.sec.gov/Archives/edgar/data/831001/000191870426032394/0001918704-26-032394-index.html
  published_at: '2026-10-22'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 424B2 0001918704-26-032378
  url: https://www.sec.gov/Archives/edgar/data/831001/000191870426032378/0001918704-26-032378-index.html
  published_at: '2026-10-22'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 424B2 0001918704-26-032349
  url: https://www.sec.gov/Archives/edgar/data/831001/000191870426032349/0001918704-26-032349-index.html
  published_at: '2026-10-22'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 424B2 0001918704-26-032314
  url: https://www.sec.gov/Archives/edgar/data/831001/000191870426032314/0001918704-26-032314-index.html
  published_at: '2026-10-22'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 424B2 0001918704-26-032301
  url: https://www.sec.gov/Archives/edgar/data/831001/000191870426032301/0001918704-26-032301-index.html
  published_at: '2026-10-22'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0000831001
  classification_status: reported_sic
  entity_type: operating
  name: CITIGROUP INC
  sic: '6021'
  sic_description: National Commercial Banks
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 977ecf280c6e1a855501ac8244519a268b7c817de7f5571d3dd333f74f5296f0
  url: https://data.sec.gov/submissions/CIK0000831001.json
listings:
- ticker: C
  exchange: NYSE
  instrument_type: common_stock
- ticker: C$R
  exchange: NYSE
  instrument_type: preferred
research_filings:
- accession: 0000831001-26-000011
  filed: '2026-02-20'
  form: 10-K
  period_end: '2025-12-31'
  url: https://www.sec.gov/Archives/edgar/data/831001/000083100126000011/0000831001-26-000011-index.html
- accession: 0000831001-26-000045
  filed: '2026-08-06'
  form: 10-Q
  period_end: '2026-06-30'
  url: https://www.sec.gov/Archives/edgar/data/831001/000083100126000045/0000831001-26-000045-index.html
- accession: 0001104659-26-118193
  filed: '2026-10-22'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/831001/000110465926118193/0001104659-26-118193-index.html
research_progress:
  stage: pending
  input_sha256: 1a405214e9ef2998d2d883f79c219cb451c84b82ff399a9ab73734327e534a29
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
  sic: '6021'
  sic_description: National Commercial Banks
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0000831001.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/d523cff21b18141b9a37cddd98ad6af6e1a30fa5/brain/companies/C/README.md
full_history_commit: d523cff21b18141b9a37cddd98ad6af6e1a30fa5
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# C, C$R — CITIGROUP INC

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/d523cff21b18141b9a37cddd98ad6af6e1a30fa5/brain/companies/C/README.md)

## Business overview

Reported issuer name: **CITIGROUP INC**. Stable SEC CIK: **0000831001**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| C | NYSE | common_stock | 1 | [S01] |
| C$R | NYSE | preferred | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **6021**: National Commercial Banks. [S02]

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
- Forms observed in the retained filing inventory: 4, 424B2, 424B3, 424B8, 8-K, FWP
- Collector status: quality_review_required; last action: filings_only_financials_incomplete; last checked: 2026-10-23T14:25:20.190193+00:00.

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
| 2026-10-22 | 424B2 | 0001918704-26-032394 | — | [S03] |
| 2026-10-22 | 424B2 | 0001918704-26-032378 | — | [S04] |
| 2026-10-22 | 424B2 | 0001918704-26-032349 | — | [S05] |
| 2026-10-22 | 424B2 | 0001918704-26-032314 | — | [S06] |
| 2026-10-22 | 424B2 | 0001918704-26-032301 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-23T14:17:55.298415+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0000831001.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [424B2 0001918704-26-032394](https://www.sec.gov/Archives/edgar/data/831001/000191870426032394/0001918704-26-032394-index.html) — published 2026-10-22; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [424B2 0001918704-26-032378](https://www.sec.gov/Archives/edgar/data/831001/000191870426032378/0001918704-26-032378-index.html) — published 2026-10-22; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [424B2 0001918704-26-032349](https://www.sec.gov/Archives/edgar/data/831001/000191870426032349/0001918704-26-032349-index.html) — published 2026-10-22; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [424B2 0001918704-26-032314](https://www.sec.gov/Archives/edgar/data/831001/000191870426032314/0001918704-26-032314-index.html) — published 2026-10-22; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [424B2 0001918704-26-032301](https://www.sec.gov/Archives/edgar/data/831001/000191870426032301/0001918704-26-032301-index.html) — published 2026-10-22; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261023-39968262770-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/d523cff21b18141b9a37cddd98ad6af6e1a30fa5/brain/companies/C/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
