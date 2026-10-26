---
schema_version: 1
document_type: company_facts
company_id: company-cik-0000718940
cik: 0000718940
company_name: BCE INC
tickers:
- BCE
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
  - '3'
  - '4'
  - 40-F
  - 424B3
  - '425'
  - 6-K
  - 6-K/A
  - CB
  - CB/A
  - CORRESP
  - EFFECT
  - F-10
  - F-10/A
  - F-3D
  - F-8
  - F-8 POS
  - F-9
  - F-9/A
  - F-X
  - FWP
  - POS AM
  - S-8
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SUPPL
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0000718940.json
    sha256: 93a5f5cce4cb18fec144820864e9aff7c2063a76dfb595ef8af880ba1298c756
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0000718940.json
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
  url: https://data.sec.gov/submissions/CIK0000718940.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 93a5f5cce4cb18fec144820864e9aff7c2063a76dfb595ef8af880ba1298c756
- id: S03
  title: 6-K 0001193125-26-426072
  url: https://www.sec.gov/Archives/edgar/data/718940/000119312526426072/0001193125-26-426072-index.html
  published_at: '2026-10-20'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 6-K 0000718940-26-000011
  url: https://www.sec.gov/Archives/edgar/data/718940/000071894026000011/0000718940-26-000011-index.html
  published_at: '2026-08-10'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 6-K 0000718940-26-000009
  url: https://www.sec.gov/Archives/edgar/data/718940/000071894026000009/0000718940-26-000009-index.html
  published_at: '2026-08-06'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 6-K 0001193125-26-313748
  url: https://www.sec.gov/Archives/edgar/data/718940/000119312526313748/0001193125-26-313748-index.html
  published_at: '2026-07-23'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 6-K 0001193125-26-259463
  url: https://www.sec.gov/Archives/edgar/data/718940/000119312526259463/0001193125-26-259463-index.html
  published_at: '2026-06-05'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0000718940
  classification_status: reported_sic
  entity_type: other
  name: BCE INC
  sic: '4813'
  sic_description: Telephone Communications (No Radiotelephone)
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 93a5f5cce4cb18fec144820864e9aff7c2063a76dfb595ef8af880ba1298c756
  url: https://data.sec.gov/submissions/CIK0000718940.json
listings:
- ticker: BCE
  exchange: NYSE
  instrument_type: common_stock
research_filings:
- accession: 0001193125-26-095004
  filed: '2026-03-06'
  form: 40-F
  url: https://www.sec.gov/Archives/edgar/data/718940/000119312526095004/0001193125-26-095004-index.html
- accession: 0001193125-26-426072
  filed: '2026-10-20'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/718940/000119312526426072/0001193125-26-426072-index.html
- accession: 0001309014-17-000716
  filed: '2017-08-23'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/718940/000130901417000716/0001309014-17-000716-index.html
- accession: 0001309014-17-000205
  filed: '2017-03-10'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/718940/000130901417000205/0001309014-17-000205-index.html
- accession: 0001309014-08-000340
  filed: '2008-06-06'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/718940/000130901408000340/0001309014-08-000340-index.html
- accession: 0001277645-07-000014
  filed: '2007-05-10'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/718940/000127764507000014/0001277645-07-000014-index.html
- accession: 0000718940-05-000030
  filed: '2005-08-04'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/718940/000071894005000030/0000718940-05-000030-index.html
- accession: 0000718940-05-000029
  filed: '2005-08-04'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/718940/000071894005000029/0000718940-05-000029-index.html
- accession: 0000718940-02-000025
  filed: '2002-12-23'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/718940/000071894002000025/0000718940-02-000025-index.html
- accession: 9999999997-02-036304
  filed: '2002-06-14'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/718940/999999999702036304/9999999997-02-036304-index.html
research_progress:
  stage: pending
  input_sha256: 66197d613955a06a95a907e1ab47d8daf501662855c32154f47dc4259bb18f33
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
  derived_observations: 0
  model_draft: false
  reviewed: false
sector_assignment:
  sector: communication-services
  method: project_sic_rule
  sic: '4813'
  sic_description: Telephone Communications (No Radiotelephone)
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0000718940.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/6ec0c5a139b27efe3be9111dc20cf938bd839c1e/brain/companies/BCE/README.md
full_history_commit: 6ec0c5a139b27efe3be9111dc20cf938bd839c1e
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# BCE — BCE INC

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/6ec0c5a139b27efe3be9111dc20cf938bd839c1e/brain/companies/BCE/README.md)

## Business overview

Reported issuer name: **BCE INC**. Stable SEC CIK: **0000718940**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| BCE | NYSE | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **4813**: Telephone Communications (No Radiotelephone). [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **communication-services**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

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
- Forms observed in the retained filing inventory: 3, 4, 40-F, 424B3, 425, 6-K, 6-K/A, CB, CB/A, CORRESP, EFFECT, F-10, F-10/A, F-3D, F-8, F-8 POS, F-9, F-9/A, F-X, FWP, POS AM, S-8, SC 13D, SC 13D/A, SC 13G, SC 13G/A, SUPPL, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:28:46.156849+00:00.

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
| 2026-10-20 | 6-K | 0001193125-26-426072 | — | [S03] |
| 2026-08-10 | 6-K | 0000718940-26-000011 | — | [S04] |
| 2026-08-06 | 6-K | 0000718940-26-000009 | — | [S05] |
| 2026-07-23 | 6-K | 0001193125-26-313748 | — | [S06] |
| 2026-06-05 | 6-K | 0001193125-26-259463 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-26T16:11:31.806354+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0000718940.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [6-K 0001193125-26-426072](https://www.sec.gov/Archives/edgar/data/718940/000119312526426072/0001193125-26-426072-index.html) — published 2026-10-20; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [6-K 0000718940-26-000011](https://www.sec.gov/Archives/edgar/data/718940/000071894026000011/0000718940-26-000011-index.html) — published 2026-08-10; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [6-K 0000718940-26-000009](https://www.sec.gov/Archives/edgar/data/718940/000071894026000009/0000718940-26-000009-index.html) — published 2026-08-06; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [6-K 0001193125-26-313748](https://www.sec.gov/Archives/edgar/data/718940/000119312526313748/0001193125-26-313748-index.html) — published 2026-07-23; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [6-K 0001193125-26-259463](https://www.sec.gov/Archives/edgar/data/718940/000119312526259463/0001193125-26-259463-index.html) — published 2026-06-05; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261026-40356450615-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/6ec0c5a139b27efe3be9111dc20cf938bd839c1e/brain/companies/BCE/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
