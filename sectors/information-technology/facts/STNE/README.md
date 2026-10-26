---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001745431
cik: '0001745431'
company_name: StoneCo Ltd.
tickers:
- STNE
status: stub
canonical_reviewed: false
as_of: '2026-10-26'
updated_at: '2026-10-26T16:16:21.148680+00:00'
reviewed_at: null
coverage_release: coverage-20261026-40356450615-1
source_commit: ffd7836f4c177b9a174b16eab4288980decb7e24
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
  - 424B3
  - 424B4
  - 424B5
  - '425'
  - 6-K
  - 6-K/A
  - 8-A12B
  - CERT
  - CORRESP
  - CT ORDER
  - DRS
  - DRS/A
  - DRSLTR
  - EFFECT
  - F-1
  - F-1/A
  - F-1MEF
  - F-3ASR
  - F-4
  - F-4/A
  - FWP
  - IRANNOTICE
  - S-8
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13D/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001745431.json
    sha256: bd42c983f0206c0899daed502bdeb9fd290fa80b9e7632bb30cf9c0b94d95712
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001745431.json
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
  url: https://data.sec.gov/submissions/CIK0001745431.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: bd42c983f0206c0899daed502bdeb9fd290fa80b9e7632bb30cf9c0b94d95712
- id: S03
  title: 4 0002070979-26-000284
  url: https://www.sec.gov/Archives/edgar/data/1745431/000207097926000284/0002070979-26-000284-index.html
  published_at: '2026-10-14'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 4 0002070979-26-000282
  url: https://www.sec.gov/Archives/edgar/data/1745431/000207097926000282/0002070979-26-000282-index.html
  published_at: '2026-10-07'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: SCHEDULE 13D/A 0001545458-26-000003
  url: https://www.sec.gov/Archives/edgar/data/1745431/000154545826000003/0001545458-26-000003-index.html
  published_at: '2026-10-07'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 4 0002070979-26-000280
  url: https://www.sec.gov/Archives/edgar/data/1745431/000207097926000280/0002070979-26-000280-index.html
  published_at: '2026-09-10'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 144 0002063736-26-000005
  url: https://www.sec.gov/Archives/edgar/data/1745431/000206373626000005/0002063736-26-000005-index.html
  published_at: '2026-09-02'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: '0001745431'
  classification_status: reported_sic
  entity_type: other
  name: StoneCo Ltd.
  sic: '7374'
  sic_description: Services-Computer Processing & Data Preparation
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: bd42c983f0206c0899daed502bdeb9fd290fa80b9e7632bb30cf9c0b94d95712
  url: https://data.sec.gov/submissions/CIK0001745431.json
listings:
- ticker: STNE
  exchange: NASDAQ
  instrument_type: equity_candidate
research_filings:
- accession: 0002070979-26-000170
  filed: '2026-04-23'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1745431/000207097926000170/0002070979-26-000170-index.html
- accession: 0000950103-19-006867
  filed: '2019-05-29'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1745431/000095010319006867/0000950103-19-006867-index.html
- accession: 0002070979-26-000275
  filed: '2026-08-13'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1745431/000207097926000275/0002070979-26-000275-index.html
- accession: 0000950103-23-005809
  filed: '2023-04-18'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1745431/000095010323005809/0000950103-23-005809-index.html
- accession: 0000950103-23-004153
  filed: '2023-03-15'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1745431/000095010323004153/0000950103-23-004153-index.html
- accession: 0000950103-20-019654
  filed: '2020-10-05'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1745431/000095010320019654/0000950103-20-019654-index.html
- accession: 0000950103-19-003973
  filed: '2019-03-29'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1745431/000095010319003973/0000950103-19-003973-index.html
research_progress:
  stage: pending
  input_sha256: 007ee6ed6f3134e03fe24b92c2981bb6d67301cd6e5b133e6124d1856a6c1f38
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
  derived_observations: 0
  model_draft: false
  reviewed: false
sector_assignment:
  sector: information-technology
  method: project_sic_rule
  sic: '7374'
  sic_description: Services-Computer Processing & Data Preparation
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001745431.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/6ec0c5a139b27efe3be9111dc20cf938bd839c1e/brain/companies/STNE/README.md
full_history_commit: 6ec0c5a139b27efe3be9111dc20cf938bd839c1e
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# STNE — StoneCo Ltd.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/6ec0c5a139b27efe3be9111dc20cf938bd839c1e/brain/companies/STNE/README.md)

## Business overview

Reported issuer name: **StoneCo Ltd.**. Stable SEC CIK: **0001745431**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| STNE | NASDAQ | equity_candidate | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **7374**: Services-Computer Processing & Data Preparation. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **information-technology**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

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
- Forms observed in the retained filing inventory: 144, 20-F, 20-F/A, 3, 3/A, 4, 424B3, 424B4, 424B5, 425, 6-K, 6-K/A, 8-A12B, CERT, CORRESP, CT ORDER, DRS, DRS/A, DRSLTR, EFFECT, F-1, F-1/A, F-1MEF, F-3ASR, F-4, F-4/A, FWP, IRANNOTICE, S-8, SC 13D, SC 13D/A, SC 13G, SC 13G/A, SCHEDULE 13D/A, SCHEDULE 13G, SCHEDULE 13G/A, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:35:23.195917+00:00.

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
| 2026-10-14 | 4 | 0002070979-26-000284 | — | [S03] |
| 2026-10-07 | 4 | 0002070979-26-000282 | — | [S04] |
| 2026-10-07 | SCHEDULE 13D/A | 0001545458-26-000003 | — | [S05] |
| 2026-09-10 | 4 | 0002070979-26-000280 | — | [S06] |
| 2026-09-02 | 144 | 0002063736-26-000005 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-26T16:11:31.228419+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001745431.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [4 0002070979-26-000284](https://www.sec.gov/Archives/edgar/data/1745431/000207097926000284/0002070979-26-000284-index.html) — published 2026-10-14; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [4 0002070979-26-000282](https://www.sec.gov/Archives/edgar/data/1745431/000207097926000282/0002070979-26-000282-index.html) — published 2026-10-07; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [SCHEDULE 13D/A 0001545458-26-000003](https://www.sec.gov/Archives/edgar/data/1745431/000154545826000003/0001545458-26-000003-index.html) — published 2026-10-07; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [4 0002070979-26-000280](https://www.sec.gov/Archives/edgar/data/1745431/000207097926000280/0002070979-26-000280-index.html) — published 2026-09-10; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [144 0002063736-26-000005](https://www.sec.gov/Archives/edgar/data/1745431/000206373626000005/0002063736-26-000005-index.html) — published 2026-09-02; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261026-40356450615-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/6ec0c5a139b27efe3be9111dc20cf938bd839c1e/brain/companies/STNE/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
