---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001452477
cik: '0001452477'
company_name: Seven Hills Realty Trust
tickers:
- SEVN
status: stub
canonical_reviewed: false
as_of: '2026-10-30'
updated_at: '2026-10-30T16:05:25.650854+00:00'
reviewed_at: null
coverage_release: coverage-20261030-41085569265-1
source_commit: ef2ed016c2c344c23ee7fb991b25bf93660da77e
financial_history_available: false
curated_research: null
financial_gap:
  reason: latest_filing_incomplete
  next_action: Resolve the latest financial filing/CompanyFacts mismatch; any historical
    bootstrap must keep the latest-period gap explicit.
  observed_forms:
  - 10-K
  - 10-Q
  - 15-12B
  - '25'
  - 25-NSE
  - 25-NSE/A
  - '3'
  - 3/A
  - '4'
  - 4/A
  - 40-17G
  - 40-17G/A
  - 40-8F-2
  - 40-8F-2/A
  - 424B3
  - 424B5
  - '425'
  - '497'
  - 497AD
  - 497J
  - 8-A12B
  - 8-A12B/A
  - 8-K
  - 8-K12B
  - 8F-2 NTC
  - 8F-2 ORDR
  - ARS
  - CERT
  - CORRESP
  - DEF 14A
  - DEFA14A
  - DEFR14A
  - EFFECT
  - N-14 8C
  - N-14 8C/A
  - N-2
  - N-2/A
  - N-23C-2
  - N-8A
  - N-8A/A
  - N-CEN
  - N-CEN/A
  - N-CSR
  - N-CSR/A
  - N-CSRS
  - N-PX
  - N-Q
  - NPORT-P
  - NPORT-P/A
  - NSAR-A
  - NSAR-B
  - NSAR-B/A
  - POS EX
  - PRE 14A
  - S-3
  - S-4
  - S-4/A
  - S-8
  - S-8 POS
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SC TO-C
  - SC TO-I
  - SC TO-I/A
  - SCHEDULE 13D/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001452477.json
    sha256: bb8d54e6104fdbe4c545d2699a377a35e5b223cf6c929833f27ee3d32330e43c
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001452477.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: nasdaqlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt
  published_at: null
  retrieved_at: '2026-10-30T16:00:11.183681+00:00'
  sha256: 64301e84a89de015f12206ec26fa4a677c38e33277e47d0b3a6b91e370e8d274
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001452477.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: bb8d54e6104fdbe4c545d2699a377a35e5b223cf6c929833f27ee3d32330e43c
- id: S03
  title: 8-K 0001104659-26-113721
  url: https://www.sec.gov/Archives/edgar/data/1452477/000110465926113721/0001104659-26-113721-index.html
  published_at: '2026-10-05'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 4 0001104659-26-108919
  url: https://www.sec.gov/Archives/edgar/data/1452477/000110465926108919/0001104659-26-108919-index.html
  published_at: '2026-09-18'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 4 0001104659-26-108918
  url: https://www.sec.gov/Archives/edgar/data/1452477/000110465926108918/0001104659-26-108918-index.html
  published_at: '2026-09-18'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 4 0001104659-26-108917
  url: https://www.sec.gov/Archives/edgar/data/1452477/000110465926108917/0001104659-26-108917-index.html
  published_at: '2026-09-18'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 4 0001104659-26-108916
  url: https://www.sec.gov/Archives/edgar/data/1452477/000110465926108916/0001104659-26-108916-index.html
  published_at: '2026-09-18'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: '0001452477'
  classification_status: reported_sic
  entity_type: operating
  name: Seven Hills Realty Trust
  sic: '6798'
  sic_description: Real Estate Investment Trusts
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: bb8d54e6104fdbe4c545d2699a377a35e5b223cf6c929833f27ee3d32330e43c
  url: https://data.sec.gov/submissions/CIK0001452477.json
listings:
- ticker: SEVN
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001452477-26-000010
  filed: '2026-02-18'
  form: 10-K
  period_end: '2025-12-31'
  url: https://www.sec.gov/Archives/edgar/data/1452477/000145247726000010/0001452477-26-000010-index.html
- accession: 0001452477-26-000029
  filed: '2026-07-28'
  form: 10-Q
  period_end: '2026-06-30'
  url: https://www.sec.gov/Archives/edgar/data/1452477/000145247726000029/0001452477-26-000029-index.html
- accession: 0001104659-26-030948
  filed: '2026-03-18'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/1452477/000110465926030948/0001104659-26-030948-index.html
- accession: 0001104659-26-113721
  filed: '2026-10-05'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/1452477/000110465926113721/0001104659-26-113721-index.html
research_progress:
  stage: pending
  input_sha256: c8e1dddc11ee8f0ab56b9d4fb49c4f9727f48e8305b0db4c6b528611debe3af3
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
  derived_observations: 0
  model_draft: false
  reviewed: false
sector_assignment:
  sector: unclassified
  method: unresolved
  sic: '6798'
  sic_description: Real Estate Investment Trusts
  rule_version: 1
  reason: Fund reporting signal requires instrument review before operating-sector
    classification.
full_history_url: https://github.com/eladyesh/stock-brain/blob/79888139fa1fe8ad3404e6bc04e318eee1474f73/brain/companies/SEVN/README.md
full_history_commit: 79888139fa1fe8ad3404e6bc04e318eee1474f73
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# SEVN — Seven Hills Realty Trust

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/79888139fa1fe8ad3404e6bc04e318eee1474f73/brain/companies/SEVN/README.md)

## Business overview

Reported issuer name: **Seven Hills Realty Trust**. Stable SEC CIK: **0001452477**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| SEVN | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **6798**: Real Estate Investment Trusts. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **unclassified**. Method: `unresolved`. Fund reporting signal requires instrument review before operating-sector classification.

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
- Forms observed in the retained filing inventory: 10-K, 10-Q, 15-12B, 25, 25-NSE, 25-NSE/A, 3, 3/A, 4, 4/A, 40-17G, 40-17G/A, 40-8F-2, 40-8F-2/A, 424B3, 424B5, 425, 497, 497AD, 497J, 8-A12B, 8-A12B/A, 8-K, 8-K12B, 8F-2 NTC, 8F-2 ORDR, ARS, CERT, CORRESP, DEF 14A, DEFA14A, DEFR14A, EFFECT, N-14 8C, N-14 8C/A, N-2, N-2/A, N-23C-2, N-8A, N-8A/A, N-CEN, N-CEN/A, N-CSR, N-CSR/A, N-CSRS, N-PX, N-Q, NPORT-P, NPORT-P/A, NSAR-A, NSAR-B, NSAR-B/A, POS EX, PRE 14A, S-3, S-4, S-4/A, S-8, S-8 POS, SC 13D, SC 13D/A, SC 13G, SC 13G/A, SC TO-C, SC TO-I, SC TO-I/A, SCHEDULE 13D/A, SCHEDULE 13G, SCHEDULE 13G/A, UPLOAD
- Collector status: quality_review_required; last action: filings_only_financials_incomplete; last checked: 2026-10-24T13:33:26.337730+00:00.

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
| 2026-10-05 | 8-K | 0001104659-26-113721 | — | [S03] |
| 2026-09-18 | 4 | 0001104659-26-108919 | — | [S04] |
| 2026-09-18 | 4 | 0001104659-26-108918 | — | [S05] |
| 2026-09-18 | 4 | 0001104659-26-108917 | — | [S06] |
| 2026-09-18 | 4 | 0001104659-26-108916 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-30T16:00:11.183681+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001452477.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [8-K 0001104659-26-113721](https://www.sec.gov/Archives/edgar/data/1452477/000110465926113721/0001104659-26-113721-index.html) — published 2026-10-05; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [4 0001104659-26-108919](https://www.sec.gov/Archives/edgar/data/1452477/000110465926108919/0001104659-26-108919-index.html) — published 2026-09-18; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [4 0001104659-26-108918](https://www.sec.gov/Archives/edgar/data/1452477/000110465926108918/0001104659-26-108918-index.html) — published 2026-09-18; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [4 0001104659-26-108917](https://www.sec.gov/Archives/edgar/data/1452477/000110465926108917/0001104659-26-108917-index.html) — published 2026-09-18; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [4 0001104659-26-108916](https://www.sec.gov/Archives/edgar/data/1452477/000110465926108916/0001104659-26-108916-index.html) — published 2026-09-18; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261030-41085569265-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/79888139fa1fe8ad3404e6bc04e318eee1474f73/brain/companies/SEVN/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
