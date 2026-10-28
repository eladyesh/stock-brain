---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001445930
cik: 0001445930
company_name: KB Financial Group Inc.
tickers:
- KB
status: stub
canonical_reviewed: false
as_of: '2026-10-28'
updated_at: '2026-10-28T16:13:42.115634+00:00'
reviewed_at: null
coverage_release: coverage-20261028-40722802424-1
source_commit: 48056b79cf1dc5f5270bd576defc5c9bc49d62cf
financial_history_available: false
curated_research: null
financial_gap:
  reason: foreign_reporting_adapter
  next_action: Add support for the observed 20-F, 40-F or 6-K reporting forms and
    verify the actual accounting taxonomy before normalization.
  observed_forms:
  - 20-F
  - 20-F/A
  - 424B5
  - 6-K
  - 6-K/A
  - 8-K12G3
  - CB
  - CORRESP
  - EFFECT
  - F-3ASR
  - F-6
  - F-6EF
  - F-X
  - POS AM
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001445930.json
    sha256: 5ca5a5ce1cfbb21331251acfa443941ffe3d3c147270b3e82390dae26a88d974
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001445930.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: otherlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt
  published_at: null
  retrieved_at: '2026-10-28T16:09:02.154543+00:00'
  sha256: 9075fbed01d898a38c24f9b203cac1b6a4eed581edb2da888a321447f3bb55cc
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001445930.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 5ca5a5ce1cfbb21331251acfa443941ffe3d3c147270b3e82390dae26a88d974
- id: S03
  title: 6-K 0001193125-26-427149
  url: https://www.sec.gov/Archives/edgar/data/1445930/000119312526427149/0001193125-26-427149-index.html
  published_at: '2026-10-21'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 6-K 0001193125-26-422217
  url: https://www.sec.gov/Archives/edgar/data/1445930/000119312526422217/0001193125-26-422217-index.html
  published_at: '2026-10-15'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 6-K 0001193125-26-411212
  url: https://www.sec.gov/Archives/edgar/data/1445930/000119312526411212/0001193125-26-411212-index.html
  published_at: '2026-10-02'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 6-K 0001193125-26-359831
  url: https://www.sec.gov/Archives/edgar/data/1445930/000119312526359831/0001193125-26-359831-index.html
  published_at: '2026-08-21'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 6-K 0001193125-26-350220
  url: https://www.sec.gov/Archives/edgar/data/1445930/000119312526350220/0001193125-26-350220-index.html
  published_at: '2026-08-14'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0001445930
  classification_status: reported_sic
  entity_type: other
  name: KB Financial Group Inc.
  sic: '6029'
  sic_description: Commercial Banks, NEC
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 5ca5a5ce1cfbb21331251acfa443941ffe3d3c147270b3e82390dae26a88d974
  url: https://data.sec.gov/submissions/CIK0001445930.json
listings:
- ticker: KB
  exchange: NYSE
  instrument_type: equity_candidate
research_filings:
- accession: 0001193125-26-183398
  filed: '2026-04-28'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1445930/000119312526183398/0001193125-26-183398-index.html
- accession: 0001193125-11-181096
  filed: '2011-07-05'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1445930/000119312511181096/0001193125-11-181096-index.html
- accession: 0000950123-10-066672
  filed: '2010-07-21'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1445930/000095012310066672/0000950123-10-066672-index.html
- accession: 0001193125-26-427149
  filed: '2026-10-21'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1445930/000119312526427149/0001193125-26-427149-index.html
- accession: 0001193125-26-229593
  filed: '2026-05-19'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1445930/000119312526229593/0001193125-26-229593-index.html
- accession: 0001193125-21-301504
  filed: '2021-10-19'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1445930/000119312521301504/0001193125-21-301504-index.html
- accession: 0001193125-21-132515
  filed: '2021-04-27'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1445930/000119312521132515/0001193125-21-132515-index.html
- accession: 0001193125-20-274139
  filed: '2020-10-22'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1445930/000119312520274139/0001193125-20-274139-index.html
- accession: 0001193125-18-090243
  filed: '2018-03-21'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1445930/000119312518090243/0001193125-18-090243-index.html
- accession: 0001193125-17-339955
  filed: '2017-11-13'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1445930/000119312517339955/0001193125-17-339955-index.html
- accession: 0001193125-17-339951
  filed: '2017-11-13'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1445930/000119312517339951/0001193125-17-339951-index.html
- accession: 0001193125-17-320406
  filed: '2017-10-26'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1445930/000119312517320406/0001193125-17-320406-index.html
research_progress:
  stage: pending
  input_sha256: eaa15d6af26b854c9bd8c98e32a6b745d53a8f529ceefc18c1d156c7611e69ec
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
  source_url: https://data.sec.gov/submissions/CIK0001445930.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/d9e673c37aaa38580be4e36b4880e8ab015a9390/brain/companies/KB/README.md
full_history_commit: d9e673c37aaa38580be4e36b4880e8ab015a9390
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# KB — KB Financial Group Inc.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/d9e673c37aaa38580be4e36b4880e8ab015a9390/brain/companies/KB/README.md)

## Business overview

Reported issuer name: **KB Financial Group Inc.**. Stable SEC CIK: **0001445930**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| KB | NYSE | equity_candidate | 1 | [S01] |

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
- Forms observed in the retained filing inventory: 20-F, 20-F/A, 424B5, 6-K, 6-K/A, 8-K12G3, CB, CORRESP, EFFECT, F-3ASR, F-6, F-6EF, F-X, POS AM, SC 13G, SC 13G/A, SCHEDULE 13G, SCHEDULE 13G/A, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:33:24.940114+00:00.

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
| 2026-10-21 | 6-K | 0001193125-26-427149 | — | [S03] |
| 2026-10-15 | 6-K | 0001193125-26-422217 | — | [S04] |
| 2026-10-02 | 6-K | 0001193125-26-411212 | — | [S05] |
| 2026-08-21 | 6-K | 0001193125-26-359831 | — | [S06] |
| 2026-08-14 | 6-K | 0001193125-26-350220 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-28T16:09:02.154543+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001445930.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [6-K 0001193125-26-427149](https://www.sec.gov/Archives/edgar/data/1445930/000119312526427149/0001193125-26-427149-index.html) — published 2026-10-21; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [6-K 0001193125-26-422217](https://www.sec.gov/Archives/edgar/data/1445930/000119312526422217/0001193125-26-422217-index.html) — published 2026-10-15; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [6-K 0001193125-26-411212](https://www.sec.gov/Archives/edgar/data/1445930/000119312526411212/0001193125-26-411212-index.html) — published 2026-10-02; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [6-K 0001193125-26-359831](https://www.sec.gov/Archives/edgar/data/1445930/000119312526359831/0001193125-26-359831-index.html) — published 2026-08-21; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [6-K 0001193125-26-350220](https://www.sec.gov/Archives/edgar/data/1445930/000119312526350220/0001193125-26-350220-index.html) — published 2026-08-14; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261028-40722802424-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/d9e673c37aaa38580be4e36b4880e8ab015a9390/brain/companies/KB/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
