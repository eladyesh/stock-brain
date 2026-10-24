---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001341170
cik: '0001341170'
company_name: EUROSEAS LTD.
tickers:
- ESEA
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
  - 20-F
  - 20-F/A
  - '3'
  - 3/A
  - '4'
  - 424B1
  - 424B3
  - 424B4
  - 424B5
  - '425'
  - 6-K
  - 6-K/A
  - 8-A12B
  - 8-A12G
  - AW
  - CERTNAS
  - CORRESP
  - EFFECT
  - F-1
  - F-1/A
  - F-3
  - F-3/A
  - F-4
  - F-4/A
  - FWP
  - NT 20-F
  - POS AM
  - REGDEX
  - S-8
  - S-8 POS
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001341170.json
    sha256: 56697cb612f328ace9852eb03fb727a28854b054052163958da21a5ac594b41b
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001341170.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: nasdaqlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt
  published_at: null
  retrieved_at: '2026-10-24T13:23:32.568444+00:00'
  sha256: 59ac9b74ff663c6de40f5c93a54d5e12eb3fbef74f82e8a7cfc1456ad9f969ec
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001341170.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 56697cb612f328ace9852eb03fb727a28854b054052163958da21a5ac594b41b
- id: S03
  title: F-3/A 0000919574-26-007131
  url: https://www.sec.gov/Archives/edgar/data/1341170/000091957426007131/0000919574-26-007131-index.html
  published_at: '2026-10-22'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 6-K 0001317861-26-000052
  url: https://www.sec.gov/Archives/edgar/data/1341170/000131786126000052/0001317861-26-000052-index.html
  published_at: '2026-10-19'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 6-K 0001171843-26-006556
  url: https://www.sec.gov/Archives/edgar/data/1341170/000117184326006556/0001171843-26-006556-index.html
  published_at: '2026-10-09'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 4 0002127484-26-000019
  url: https://www.sec.gov/Archives/edgar/data/1341170/000212748426000019/0002127484-26-000019-index.html
  published_at: '2026-10-05'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 4 0001927715-26-000011
  url: https://www.sec.gov/Archives/edgar/data/1341170/000192771526000011/0001927715-26-000011-index.html
  published_at: '2026-10-05'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: '0001341170'
  classification_status: reported_sic
  entity_type: other
  name: EUROSEAS LTD.
  sic: '4412'
  sic_description: Deep Sea Foreign Transportation of  Freight
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 56697cb612f328ace9852eb03fb727a28854b054052163958da21a5ac594b41b
  url: https://data.sec.gov/submissions/CIK0001341170.json
listings:
- ticker: ESEA
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001171843-26-002807
  filed: '2026-04-29'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1341170/000117184326002807/0001171843-26-002807-index.html
- accession: 0000919574-18-003228
  filed: '2018-05-01'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1341170/000091957418003228/0000919574-18-003228-index.html
- accession: 0001171843-13-002325
  filed: '2013-05-30'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1341170/000117184313002325/0001171843-13-002325-index.html
- accession: 0001171843-12-002037
  filed: '2012-05-29'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1341170/000117184312002037/0001171843-12-002037-index.html
- accession: 0001317861-26-000052
  filed: '2026-10-19'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1341170/000131786126000052/0001317861-26-000052-index.html
- accession: 0001171843-25-006863
  filed: '2025-10-31'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1341170/000117184325006863/0001171843-25-006863-index.html
- accession: 0000919574-18-006758
  filed: '2018-10-23'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1341170/000091957418006758/0000919574-18-006758-index.html
- accession: 0000919574-16-011610
  filed: '2016-03-04'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1341170/000091957416011610/0000919574-16-011610-index.html
- accession: 0000919574-14-005537
  filed: '2014-10-06'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1341170/000091957414005537/0000919574-14-005537-index.html
- accession: 0000919574-13-006043
  filed: '2013-10-31'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1341170/000091957413006043/0000919574-13-006043-index.html
- accession: 0000919574-09-011575
  filed: '2009-06-03'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1341170/000091957409011575/0000919574-09-011575-index.html
- accession: 0001317861-08-000405
  filed: '2008-11-19'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1341170/000131786108000405/0001317861-08-000405-index.html
research_progress:
  stage: pending
  input_sha256: 891e5886e6f582d017908421b26207756e5ab9fb6068f5c03d875aa5972c6e57
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
  sic: '4412'
  sic_description: Deep Sea Foreign Transportation of  Freight
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001341170.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/aad7b261e69b9f214b9c5e20228523ca644ed670/brain/companies/ESEA/README.md
full_history_commit: aad7b261e69b9f214b9c5e20228523ca644ed670
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# ESEA — EUROSEAS LTD.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/aad7b261e69b9f214b9c5e20228523ca644ed670/brain/companies/ESEA/README.md)

## Business overview

Reported issuer name: **EUROSEAS LTD.**. Stable SEC CIK: **0001341170**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| ESEA | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **4412**: Deep Sea Foreign Transportation of  Freight. [S02]

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
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 144, 20-F, 20-F/A, 3, 3/A, 4, 424B1, 424B3, 424B4, 424B5, 425, 6-K, 6-K/A, 8-A12B, 8-A12G, AW, CERTNAS, CORRESP, EFFECT, F-1, F-1/A, F-3, F-3/A, F-4, F-4/A, FWP, NT 20-F, POS AM, REGDEX, S-8, S-8 POS, SC 13D, SC 13D/A, SC 13G, SC 13G/A, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:32:42.886200+00:00.

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
| 2026-10-22 | F-3/A | 0000919574-26-007131 | — | [S03] |
| 2026-10-19 | 6-K | 0001317861-26-000052 | — | [S04] |
| 2026-10-09 | 6-K | 0001171843-26-006556 | — | [S05] |
| 2026-10-05 | 4 | 0002127484-26-000019 | — | [S06] |
| 2026-10-05 | 4 | 0001927715-26-000011 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-24T13:23:32.568444+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001341170.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [F-3/A 0000919574-26-007131](https://www.sec.gov/Archives/edgar/data/1341170/000091957426007131/0000919574-26-007131-index.html) — published 2026-10-22; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [6-K 0001317861-26-000052](https://www.sec.gov/Archives/edgar/data/1341170/000131786126000052/0001317861-26-000052-index.html) — published 2026-10-19; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [6-K 0001171843-26-006556](https://www.sec.gov/Archives/edgar/data/1341170/000117184326006556/0001171843-26-006556-index.html) — published 2026-10-09; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [4 0002127484-26-000019](https://www.sec.gov/Archives/edgar/data/1341170/000212748426000019/0002127484-26-000019-index.html) — published 2026-10-05; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [4 0001927715-26-000011](https://www.sec.gov/Archives/edgar/data/1341170/000192771526000011/0001927715-26-000011-index.html) — published 2026-10-05; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261024-40097864335-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/aad7b261e69b9f214b9c5e20228523ca644ed670/brain/companies/ESEA/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
