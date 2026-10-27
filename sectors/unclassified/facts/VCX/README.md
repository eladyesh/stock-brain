---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001867090
cik: 0001867090
company_name: Fundrise Innovation Fund, LLC
tickers:
- VCX
status: stub
canonical_reviewed: false
as_of: '2026-10-27'
updated_at: '2026-10-27T15:30:18.641431+00:00'
reviewed_at: null
coverage_release: coverage-20261027-40530587641-1
source_commit: 79ea404d09f86d838fefd71cf88a566d57bc57a2
financial_history_available: false
curated_research: null
financial_gap:
  reason: fund_reporting_review
  next_action: Review the instrument against its N-CSR/N-CSRS reporting evidence before
    applying an operating-company model. This signal alone is not a final fund classification.
  observed_forms:
  - '144'
  - 144/A
  - '3'
  - '4'
  - 40-17F2
  - 40-17G
  - 424B2
  - 424B3
  - 486APOS
  - 486BPOS
  - 497AD
  - 8-A12B
  - 8-K
  - CERT
  - CORRESP
  - DEF 14A
  - DEF 14C
  - DEFA14A
  - DEFR14A
  - DEL AM
  - EFFECT
  - N-2
  - N-2/A
  - N-2ASR
  - N-8A
  - N-8A/A
  - N-CEN
  - N-CSR
  - N-CSR/A
  - N-CSRS
  - N-PX
  - NPORT-P
  - PRE 14A
  - SC TO-I
  - SC TO-I/A
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001867090.json
    sha256: 57d484ef63537d7d02b57d859963b52fd919d9b43f0f7c56c4319dd64fcc2918
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001867090.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: otherlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt
  published_at: null
  retrieved_at: '2026-10-27T15:25:35.250901+00:00'
  sha256: 3e845dbd702671bbfbbc700f50d314d4d4cb439640ee0fe6fbf22fc3344c7f42
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001867090.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 57d484ef63537d7d02b57d859963b52fd919d9b43f0f7c56c4319dd64fcc2918
- id: S03
  title: 424B2 0001213900-26-098534
  url: https://www.sec.gov/Archives/edgar/data/1867090/000121390026098534/0001213900-26-098534-index.html
  published_at: '2026-09-10'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: N-2ASR 0001213900-26-098443
  url: https://www.sec.gov/Archives/edgar/data/1867090/000121390026098443/0001213900-26-098443-index.html
  published_at: '2026-09-09'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: NPORT-P 0001867090-26-000109
  url: https://www.sec.gov/Archives/edgar/data/1867090/000186709026000109/0001867090-26-000109-index.html
  published_at: '2026-08-28'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 144 0001974158-26-000098
  url: https://www.sec.gov/Archives/edgar/data/1867090/000197415826000098/0001974158-26-000098-index.html
  published_at: '2026-08-12'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 144 0001974158-26-000094
  url: https://www.sec.gov/Archives/edgar/data/1867090/000197415826000094/0001974158-26-000094-index.html
  published_at: '2026-08-03'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0001867090
  classification_status: missing_or_invalid_sic
  entity_type: other
  name: Fundrise Innovation Fund, LLC
  sic: null
  sic_description: ''
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 57d484ef63537d7d02b57d859963b52fd919d9b43f0f7c56c4319dd64fcc2918
  url: https://data.sec.gov/submissions/CIK0001867090.json
listings:
- ticker: VCX
  exchange: NYSE
  instrument_type: common_stock
research_filings:
- accession: 0002071844-26-000143
  filed: '2026-02-03'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/1867090/000207184426000143/0002071844-26-000143-index.html
- accession: 0001213900-26-081869
  filed: '2026-07-27'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/1867090/000121390026081869/0001213900-26-081869-index.html
research_progress:
  stage: pending
  input_sha256: 7196b67f741cbf160023c96d7c671c5c4b7ffc602be794cde8e158eda909294f
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
full_history_url: https://github.com/eladyesh/stock-brain/blob/ea9dd09e5d047ff0620d4500849876915bb10e87/brain/companies/VCX/README.md
full_history_commit: ea9dd09e5d047ff0620d4500849876915bb10e87
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# VCX — Fundrise Innovation Fund, LLC

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/ea9dd09e5d047ff0620d4500849876915bb10e87/brain/companies/VCX/README.md)

## Business overview

Reported issuer name: **Fundrise Innovation Fund, LLC**. Stable SEC CIK: **0001867090**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| VCX | NYSE | common_stock | 1 | [S01] |

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
- Forms observed in the retained filing inventory: 144, 144/A, 3, 4, 40-17F2, 40-17G, 424B2, 424B3, 486APOS, 486BPOS, 497AD, 8-A12B, 8-K, CERT, CORRESP, DEF 14A, DEF 14C, DEFA14A, DEFR14A, DEL AM, EFFECT, N-2, N-2/A, N-2ASR, N-8A, N-8A/A, N-CEN, N-CSR, N-CSR/A, N-CSRS, N-PX, NPORT-P, PRE 14A, SC TO-I, SC TO-I/A
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:36:14.429842+00:00.

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
| 2026-09-10 | 424B2 | 0001213900-26-098534 | — | [S03] |
| 2026-09-09 | N-2ASR | 0001213900-26-098443 | — | [S04] |
| 2026-08-28 | NPORT-P | 0001867090-26-000109 | — | [S05] |
| 2026-08-12 | 144 | 0001974158-26-000098 | — | [S06] |
| 2026-08-03 | 144 | 0001974158-26-000094 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-27T15:25:35.250901+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001867090.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [424B2 0001213900-26-098534](https://www.sec.gov/Archives/edgar/data/1867090/000121390026098534/0001213900-26-098534-index.html) — published 2026-09-10; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [N-2ASR 0001213900-26-098443](https://www.sec.gov/Archives/edgar/data/1867090/000121390026098443/0001213900-26-098443-index.html) — published 2026-09-09; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [NPORT-P 0001867090-26-000109](https://www.sec.gov/Archives/edgar/data/1867090/000186709026000109/0001867090-26-000109-index.html) — published 2026-08-28; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [144 0001974158-26-000098](https://www.sec.gov/Archives/edgar/data/1867090/000197415826000098/0001974158-26-000098-index.html) — published 2026-08-12; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [144 0001974158-26-000094](https://www.sec.gov/Archives/edgar/data/1867090/000197415826000094/0001974158-26-000094-index.html) — published 2026-08-03; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261027-40530587641-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/ea9dd09e5d047ff0620d4500849876915bb10e87/brain/companies/VCX/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
