---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001264136
cik: '0001264136'
company_name: WOORI FINANCIAL GROUP INC.
tickers:
- WF
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
  - 15-12B
  - 20-F
  - 20-F/A
  - 20FR12B
  - 25-NSE
  - 424B3
  - '425'
  - 6-K
  - 6-K/A
  - CB
  - CERTNYS
  - CORRESP
  - EFFECT
  - F-4
  - F-4/A
  - F-6
  - F-6EF
  - F-X
  - IRANNOTICE
  - NT 20-F
  - POS AM
  - SC 13G
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001264136.json
    sha256: 18fde7d798e9e8c57151a30682eca597806ec5dd594fa70611a3ffd7ade0cb8d
    retrieved_at: '2026-10-24T13:22:51.759433+00:00'
    archive: &id001
      member: CIK0001264136.json
      sha256: 593fbbea6512ef5ec729a5e513c465fbedaac8a66602c0abe00d0ba5a4d18732
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: otherlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt
  published_at: null
  retrieved_at: '2026-10-24T13:23:33.193038+00:00'
  sha256: 94335ed3f4abc4bbd58a4415d105d453184f5484eaf6a2884d1bfb0120d850c9
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001264136.json
  published_at: null
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 18fde7d798e9e8c57151a30682eca597806ec5dd594fa70611a3ffd7ade0cb8d
- id: S03
  title: 6-K 0001193125-26-429411
  url: https://www.sec.gov/Archives/edgar/data/1264136/000119312526429411/0001193125-26-429411-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S04
  title: 6-K 0001193125-26-429409
  url: https://www.sec.gov/Archives/edgar/data/1264136/000119312526429409/0001193125-26-429409-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S05
  title: 6-K 0001193125-26-429403
  url: https://www.sec.gov/Archives/edgar/data/1264136/000119312526429403/0001193125-26-429403-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S06
  title: 6-K 0001193125-26-425646
  url: https://www.sec.gov/Archives/edgar/data/1264136/000119312526425646/0001193125-26-425646-index.html
  published_at: '2026-10-20'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S07
  title: 6-K 0001193125-26-351111
  url: https://www.sec.gov/Archives/edgar/data/1264136/000119312526351111/0001193125-26-351111-index.html
  published_at: '2026-08-14'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
issuer_classification:
  cik: '0001264136'
  classification_status: reported_sic
  entity_type: other
  name: WOORI FINANCIAL GROUP INC.
  sic: '6029'
  sic_description: Commercial Banks, NEC
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 18fde7d798e9e8c57151a30682eca597806ec5dd594fa70611a3ffd7ade0cb8d
  url: https://data.sec.gov/submissions/CIK0001264136.json
listings:
- ticker: WF
  exchange: NYSE
  instrument_type: depositary_receipt
research_filings:
- accession: 0001193125-26-168715
  filed: '2026-04-22'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1264136/000119312526168715/0001193125-26-168715-index.html
- accession: 0001193125-12-247984
  filed: '2012-05-25'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1264136/000119312512247984/0001193125-12-247984-index.html
- accession: 0000950123-11-066669
  filed: '2011-07-20'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1264136/000095012311066669/0000950123-11-066669-index.html
- accession: 0001193125-26-429411
  filed: '2026-10-23'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1264136/000119312526429411/0001193125-26-429411-index.html
- accession: 0001193125-26-222864
  filed: '2026-05-14'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1264136/000119312526222864/0001193125-26-222864-index.html
- accession: 0001193125-26-188810
  filed: '2026-04-29'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1264136/000119312526188810/0001193125-26-188810-index.html
- accession: 0001193125-26-078982
  filed: '2026-02-27'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1264136/000119312526078982/0001193125-26-078982-index.html
- accession: 0001193125-25-116393
  filed: '2025-05-09'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1264136/000119312525116393/0001193125-25-116393-index.html
- accession: 0001193125-24-069839
  filed: '2024-03-18'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1264136/000119312524069839/0001193125-24-069839-index.html
- accession: 0001193125-24-047245
  filed: '2024-02-27'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1264136/000119312524047245/0001193125-24-047245-index.html
- accession: 0001193125-23-168416
  filed: '2023-06-16'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1264136/000119312523168416/0001193125-23-168416-index.html
- accession: 0001193125-23-168415
  filed: '2023-06-16'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1264136/000119312523168415/0001193125-23-168415-index.html
research_progress:
  stage: pending
  input_sha256: ab97d08c75afd9ba2ce075c4ea665bf531c470a07453ff9e9711c5e263d07fc9
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
  source_url: https://data.sec.gov/submissions/CIK0001264136.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/aad7b261e69b9f214b9c5e20228523ca644ed670/brain/companies/WF/README.md
full_history_commit: aad7b261e69b9f214b9c5e20228523ca644ed670
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# WF — WOORI FINANCIAL GROUP INC.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/aad7b261e69b9f214b9c5e20228523ca644ed670/brain/companies/WF/README.md)

## Business overview

Reported issuer name: **WOORI FINANCIAL GROUP INC.**. Stable SEC CIK: **0001264136**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| WF | NYSE | depositary_receipt | 1 | [S01] |

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
- Forms observed in the retained filing inventory: 15-12B, 20-F, 20-F/A, 20FR12B, 25-NSE, 424B3, 425, 6-K, 6-K/A, CB, CERTNYS, CORRESP, EFFECT, F-4, F-4/A, F-6, F-6EF, F-X, IRANNOTICE, NT 20-F, POS AM, SC 13G, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:32:16.565768+00:00.

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
| 2026-10-23 | 6-K | 0001193125-26-429411 | — | [S03] |
| 2026-10-23 | 6-K | 0001193125-26-429409 | — | [S04] |
| 2026-10-23 | 6-K | 0001193125-26-429403 | — | [S05] |
| 2026-10-20 | 6-K | 0001193125-26-425646 | — | [S06] |
| 2026-08-14 | 6-K | 0001193125-26-351111 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-24T13:23:33.193038+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001264136.json) — published not supplied; retrieved 2026-10-24T13:22:51.759433+00:00.

[S03] [6-K 0001193125-26-429411](https://www.sec.gov/Archives/edgar/data/1264136/000119312526429411/0001193125-26-429411-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S04] [6-K 0001193125-26-429409](https://www.sec.gov/Archives/edgar/data/1264136/000119312526429409/0001193125-26-429409-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S05] [6-K 0001193125-26-429403](https://www.sec.gov/Archives/edgar/data/1264136/000119312526429403/0001193125-26-429403-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S06] [6-K 0001193125-26-425646](https://www.sec.gov/Archives/edgar/data/1264136/000119312526425646/0001193125-26-425646-index.html) — published 2026-10-20; retrieved 2026-10-24T13:22:51.759433+00:00.

[S07] [6-K 0001193125-26-351111](https://www.sec.gov/Archives/edgar/data/1264136/000119312526351111/0001193125-26-351111-index.html) — published 2026-08-14; retrieved 2026-10-24T13:22:51.759433+00:00.

Source release: `coverage-20261024-40097864335-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/aad7b261e69b9f214b9c5e20228523ca644ed670/brain/companies/WF/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
