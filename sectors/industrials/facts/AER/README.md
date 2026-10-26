---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001378789
cik: 0001378789
company_name: AerCap Holdings N.V.
tickers:
- AER
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
  reason: foreign_reporting_adapter
  next_action: Add support for the observed 20-F, 40-F or 6-K reporting forms and
    verify the actual accounting taxonomy before normalization.
  observed_forms:
  - '144'
  - 20-F
  - 20-F/A
  - 25-NSE
  - '3'
  - '4'
  - 4/A
  - 424B3
  - 424B4
  - 424B5
  - 424B7
  - '425'
  - 6-K
  - 6-K/A
  - 8-A12B
  - CERT
  - CORRESP
  - CT ORDER
  - EFFECT
  - F-3ASR
  - F-4
  - F-4/A
  - F-4MEF
  - FWP
  - S-8
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001378789.json
    sha256: 8685eb5435bf55b2b48a62c551f4e6e55fa7f88d1eeba39a9a8e20bffe18885d
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001378789.json
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
  url: https://data.sec.gov/submissions/CIK0001378789.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 8685eb5435bf55b2b48a62c551f4e6e55fa7f88d1eeba39a9a8e20bffe18885d
- id: S03
  title: 6-K 0000950157-26-001081
  url: https://www.sec.gov/Archives/edgar/data/1378789/000095015726001081/0000950157-26-001081-index.html
  published_at: '2026-10-07'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 424B5 0001193125-26-402843
  url: https://www.sec.gov/Archives/edgar/data/1378789/000119312526402843/0001193125-26-402843-index.html
  published_at: '2026-09-25'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 424B3 0001193125-26-398572
  url: https://www.sec.gov/Archives/edgar/data/1378789/000119312526398572/0001193125-26-398572-index.html
  published_at: '2026-09-23'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 6-K 0000950157-26-001041
  url: https://www.sec.gov/Archives/edgar/data/1378789/000095015726001041/0000950157-26-001041-index.html
  published_at: '2026-09-23'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: FWP 0000950157-26-001040
  url: https://www.sec.gov/Archives/edgar/data/1378789/000095015726001040/0000950157-26-001040-index.html
  published_at: '2026-09-23'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0001378789
  classification_status: reported_sic
  entity_type: other
  name: AerCap Holdings N.V.
  sic: '7359'
  sic_description: Services-Equipment Rental & Leasing, NEC
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 8685eb5435bf55b2b48a62c551f4e6e55fa7f88d1eeba39a9a8e20bffe18885d
  url: https://data.sec.gov/submissions/CIK0001378789.json
listings:
- ticker: AER
  exchange: NYSE
  instrument_type: common_stock
research_filings:
- accession: 0001628280-26-007513
  filed: '2026-02-12'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1378789/000162828026007513/0001628280-26-007513-index.html
- accession: 0001378789-24-000030
  filed: '2024-09-13'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1378789/000137878924000030/0001378789-24-000030-index.html
- accession: 0000950157-22-000595
  filed: '2022-05-17'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1378789/000095015722000595/0000950157-22-000595-index.html
- accession: 0001104659-11-021310
  filed: '2011-04-20'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1378789/000110465911021310/0001104659-11-021310-index.html
- accession: 0000950157-26-001081
  filed: '2026-10-07'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1378789/000095015726001081/0000950157-26-001081-index.html
- accession: 0000950157-26-000232
  filed: '2026-03-05'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1378789/000095015726000232/0000950157-26-000232-index.html
- accession: 0001378789-19-000018
  filed: '2019-09-20'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1378789/000137878919000018/0001378789-19-000018-index.html
- accession: 0001104659-12-075414
  filed: '2012-11-07'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1378789/000110465912075414/0001104659-12-075414-index.html
- accession: 0001104659-12-014392
  filed: '2012-02-29'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1378789/000110465912014392/0001104659-12-014392-index.html
- accession: 0001104659-11-039483
  filed: '2011-07-18'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1378789/000110465911039483/0001104659-11-039483-index.html
research_progress:
  stage: pending
  input_sha256: e863618fa1cf87cbe1923d2fb000318e6246fd61c772ca0098bc25385d683965
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
  sic: '7359'
  sic_description: Services-Equipment Rental & Leasing, NEC
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001378789.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/30a5d1cd40fce8d4a64ca29ee815b726555957d3/brain/companies/AER/README.md
full_history_commit: 30a5d1cd40fce8d4a64ca29ee815b726555957d3
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# AER — AerCap Holdings N.V.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/30a5d1cd40fce8d4a64ca29ee815b726555957d3/brain/companies/AER/README.md)

## Business overview

Reported issuer name: **AerCap Holdings N.V.**. Stable SEC CIK: **0001378789**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| AER | NYSE | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **7359**: Services-Equipment Rental & Leasing, NEC. [S02]

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
- Forms observed in the retained filing inventory: 144, 20-F, 20-F/A, 25-NSE, 3, 4, 4/A, 424B3, 424B4, 424B5, 424B7, 425, 6-K, 6-K/A, 8-A12B, CERT, CORRESP, CT ORDER, EFFECT, F-3ASR, F-4, F-4/A, F-4MEF, FWP, S-8, SC 13D, SC 13D/A, SC 13G, SC 13G/A, SCHEDULE 13G/A, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:32:56.550192+00:00.

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
| 2026-10-07 | 6-K | 0000950157-26-001081 | — | [S03] |
| 2026-09-25 | 424B5 | 0001193125-26-402843 | — | [S04] |
| 2026-09-23 | 424B3 | 0001193125-26-398572 | — | [S05] |
| 2026-09-23 | 6-K | 0000950157-26-001041 | — | [S06] |
| 2026-09-23 | FWP | 0000950157-26-001040 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-26T16:11:31.806354+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001378789.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [6-K 0000950157-26-001081](https://www.sec.gov/Archives/edgar/data/1378789/000095015726001081/0000950157-26-001081-index.html) — published 2026-10-07; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [424B5 0001193125-26-402843](https://www.sec.gov/Archives/edgar/data/1378789/000119312526402843/0001193125-26-402843-index.html) — published 2026-09-25; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [424B3 0001193125-26-398572](https://www.sec.gov/Archives/edgar/data/1378789/000119312526398572/0001193125-26-398572-index.html) — published 2026-09-23; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [6-K 0000950157-26-001041](https://www.sec.gov/Archives/edgar/data/1378789/000095015726001041/0000950157-26-001041-index.html) — published 2026-09-23; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [FWP 0000950157-26-001040](https://www.sec.gov/Archives/edgar/data/1378789/000095015726001040/0000950157-26-001040-index.html) — published 2026-09-23; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261026-40356450615-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/30a5d1cd40fce8d4a64ca29ee815b726555957d3/brain/companies/AER/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
