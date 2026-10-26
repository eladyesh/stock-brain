---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001233087
cik: 0001233087
company_name: FRANKLIN LTD DURATION INCOME TRUST
tickers:
- FTF
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
  reason: fund_reporting_review
  next_action: Review the instrument against its N-CSR/N-CSRS reporting evidence before
    applying an operating-company model. This signal alone is not a final fund classification.
  observed_forms:
  - '3'
  - '4'
  - 4/A
  - 40-17F2
  - 40-17G
  - 40-APP
  - 40-APP/A
  - 424B2
  - '497'
  - 497AD
  - 8-A12B
  - CERTAMX
  - CORRESP
  - DEF 14A
  - DEFA14A
  - DEFC14A
  - DFAN14A
  - EFFECT
  - N-2
  - N-2/A
  - N-23C-2
  - N-2MEF
  - N-8A
  - N-8A/A
  - N-CEN
  - N-CEN/A
  - N-CSR
  - N-CSR/A
  - N-CSRS
  - N-PX
  - N-Q
  - NPORT-EX
  - NPORT-P
  - NPORT-P/A
  - NSAR-A
  - NSAR-B
  - NSAR-B/A
  - NSAR-BT
  - POS EX
  - PRE 14A
  - PREC14A
  - PRRN14A
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SC TO-C
  - SC TO-I
  - SC TO-I/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001233087.json
    sha256: 3cb6c2ce96050a7bbbf79a6283644f497d5ffee9f3d0111fca76e64f4b83d69c
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001233087.json
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
  url: https://data.sec.gov/submissions/CIK0001233087.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 3cb6c2ce96050a7bbbf79a6283644f497d5ffee9f3d0111fca76e64f4b83d69c
- id: S03
  title: 40-17F2 0001233087-26-000004
  url: https://www.sec.gov/Archives/edgar/data/1233087/000123308726000004/0001233087-26-000004-index.html
  published_at: '2026-10-01'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: N-CSRS 0001133228-26-011820
  url: https://www.sec.gov/Archives/edgar/data/1233087/000113322826011820/0001133228-26-011820-index.html
  published_at: '2026-08-28'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: NPORT-P 0002071691-26-020999
  url: https://www.sec.gov/Archives/edgar/data/1233087/000207169126020999/0002071691-26-020999-index.html
  published_at: '2026-08-27'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: DEF 14A 0001655589-26-001170
  url: https://www.sec.gov/Archives/edgar/data/1233087/000165558926001170/0001655589-26-001170-index.html
  published_at: '2026-08-24'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: N-PX 0001193125-26-360509
  url: https://www.sec.gov/Archives/edgar/data/1233087/000119312526360509/0001193125-26-360509-index.html
  published_at: '2026-08-21'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0001233087
  classification_status: missing_or_invalid_sic
  entity_type: other
  name: FRANKLIN LTD DURATION INCOME TRUST
  sic: null
  sic_description: ''
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 3cb6c2ce96050a7bbbf79a6283644f497d5ffee9f3d0111fca76e64f4b83d69c
  url: https://data.sec.gov/submissions/CIK0001233087.json
listings:
- ticker: FTF
  exchange: NYSE_AMERICAN
  instrument_type: common_stock
research_filings:
- accession: 0001655589-26-001170
  filed: '2026-08-24'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/1233087/000165558926001170/0001655589-26-001170-index.html
research_progress:
  stage: pending
  input_sha256: 4a4cebb8ea95f8d5b2c4773e9984a141268909f0e888fe2634af19ba791163f7
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
  sic: null
  sic_description: ''
  rule_version: 1
  reason: Fund reporting signal requires instrument review before operating-sector
    classification.
full_history_url: https://github.com/eladyesh/stock-brain/blob/6ec0c5a139b27efe3be9111dc20cf938bd839c1e/brain/companies/FTF/README.md
full_history_commit: 6ec0c5a139b27efe3be9111dc20cf938bd839c1e
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# FTF — FRANKLIN LTD DURATION INCOME TRUST

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/6ec0c5a139b27efe3be9111dc20cf938bd839c1e/brain/companies/FTF/README.md)

## Business overview

Reported issuer name: **FRANKLIN LTD DURATION INCOME TRUST**. Stable SEC CIK: **0001233087**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| FTF | NYSE_AMERICAN | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

Not available: substantive research has not been completed. Place the company among suppliers, distribution channels, customers, and substitutes. Explain cyclicality and supply constraints.

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
- Next collection task: Review the instrument against its N-CSR/N-CSRS reporting evidence before applying an operating-company model. This signal alone is not a final fund classification.
- Forms observed in the retained filing inventory: 3, 4, 4/A, 40-17F2, 40-17G, 40-APP, 40-APP/A, 424B2, 497, 497AD, 8-A12B, CERTAMX, CORRESP, DEF 14A, DEFA14A, DEFC14A, DFAN14A, EFFECT, N-2, N-2/A, N-23C-2, N-2MEF, N-8A, N-8A/A, N-CEN, N-CEN/A, N-CSR, N-CSR/A, N-CSRS, N-PX, N-Q, NPORT-EX, NPORT-P, NPORT-P/A, NSAR-A, NSAR-B, NSAR-B/A, NSAR-BT, POS EX, PRE 14A, PREC14A, PRRN14A, SC 13D, SC 13D/A, SC 13G, SC 13G/A, SC TO-C, SC TO-I, SC TO-I/A, SCHEDULE 13G, SCHEDULE 13G/A, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:32:13.229689+00:00.

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
| 2026-10-01 | 40-17F2 | 0001233087-26-000004 | — | [S03] |
| 2026-08-28 | N-CSRS | 0001133228-26-011820 | — | [S04] |
| 2026-08-27 | NPORT-P | 0002071691-26-020999 | — | [S05] |
| 2026-08-24 | DEF 14A | 0001655589-26-001170 | — | [S06] |
| 2026-08-21 | N-PX | 0001193125-26-360509 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-26T16:11:31.806354+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001233087.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [40-17F2 0001233087-26-000004](https://www.sec.gov/Archives/edgar/data/1233087/000123308726000004/0001233087-26-000004-index.html) — published 2026-10-01; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [N-CSRS 0001133228-26-011820](https://www.sec.gov/Archives/edgar/data/1233087/000113322826011820/0001133228-26-011820-index.html) — published 2026-08-28; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [NPORT-P 0002071691-26-020999](https://www.sec.gov/Archives/edgar/data/1233087/000207169126020999/0002071691-26-020999-index.html) — published 2026-08-27; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [DEF 14A 0001655589-26-001170](https://www.sec.gov/Archives/edgar/data/1233087/000165558926001170/0001655589-26-001170-index.html) — published 2026-08-24; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [N-PX 0001193125-26-360509](https://www.sec.gov/Archives/edgar/data/1233087/000119312526360509/0001193125-26-360509-index.html) — published 2026-08-21; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261026-40356450615-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/6ec0c5a139b27efe3be9111dc20cf938bd839c1e/brain/companies/FTF/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
