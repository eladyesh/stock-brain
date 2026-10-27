---
schema_version: 1
document_type: company_facts
company_id: company-cik-0000313838
cik: 0000313838
company_name: Sony Group Corp
tickers:
- SONY
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
  reason: foreign_reporting_adapter
  next_action: Add support for the observed 20-F, 40-F or 6-K reporting forms and
    verify the actual accounting taxonomy before normalization.
  observed_forms:
  - '144'
  - 20-F
  - 20-F/A
  - '3'
  - '4'
  - 424B2
  - 424B3
  - 424B5
  - '425'
  - 6-K
  - 6-K/A
  - CORRESP
  - EFFECT
  - F-3ASR
  - F-6
  - F-6EF
  - FWP
  - IRANNOTICE
  - S-8
  - S-8 POS
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SD
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0000313838.json
    sha256: e337c473c42ee5d8d7f872443f025b8efed23407be1385698e1f97299e922b0c
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0000313838.json
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
  url: https://data.sec.gov/submissions/CIK0000313838.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: e337c473c42ee5d8d7f872443f025b8efed23407be1385698e1f97299e922b0c
- id: S03
  title: 6-K 0001104659-26-115761
  url: https://www.sec.gov/Archives/edgar/data/313838/000110465926115761/0001104659-26-115761-index.html
  published_at: '2026-10-14'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 6-K 0001104659-26-113566
  url: https://www.sec.gov/Archives/edgar/data/313838/000110465926113566/0001104659-26-113566-index.html
  published_at: '2026-10-05'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 4 0001193125-26-395188
  url: https://www.sec.gov/Archives/edgar/data/313838/000119312526395188/0001193125-26-395188-index.html
  published_at: '2026-09-18'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 4 0001193125-26-391724
  url: https://www.sec.gov/Archives/edgar/data/313838/000119312526391724/0001193125-26-391724-index.html
  published_at: '2026-09-15'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 6-K 0001104659-26-107340
  url: https://www.sec.gov/Archives/edgar/data/313838/000110465926107340/0001104659-26-107340-index.html
  published_at: '2026-09-14'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0000313838
  classification_status: reported_sic
  entity_type: other
  name: Sony Group Corp
  sic: '3651'
  sic_description: Household Audio & Video Equipment
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: e337c473c42ee5d8d7f872443f025b8efed23407be1385698e1f97299e922b0c
  url: https://data.sec.gov/submissions/CIK0000313838.json
listings:
- ticker: SONY
  exchange: NYSE
  instrument_type: depositary_receipt
research_filings:
- accession: 0001193125-26-274893
  filed: '2026-06-18'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/313838/000119312526274893/0001193125-26-274893-index.html
- accession: 0001193125-12-308053
  filed: '2012-07-20'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/313838/000119312512308053/0001193125-12-308053-index.html
- accession: 0001104659-26-115761
  filed: '2026-10-14'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/313838/000110465926115761/0001104659-26-115761-index.html
- accession: 0001157523-18-001184
  filed: '2018-05-23'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/313838/000115752318001184/0001157523-18-001184-index.html
- accession: 0000903423-17-000489
  filed: '2017-08-11'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/313838/000090342317000489/0000903423-17-000489-index.html
- accession: 0000903423-17-000392
  filed: '2017-05-26'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/313838/000090342317000392/0000903423-17-000392-index.html
research_progress:
  stage: pending
  input_sha256: 702b7f0c5fda34dfab3a9b6aa1d6b5d40e94463601b8e71cc600928ea2c25914
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
  derived_observations: 0
  model_draft: false
  reviewed: false
sector_assignment:
  sector: consumer-discretionary
  method: project_sic_rule
  sic: '3651'
  sic_description: Household Audio & Video Equipment
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0000313838.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/ea9dd09e5d047ff0620d4500849876915bb10e87/brain/companies/SONY/README.md
full_history_commit: ea9dd09e5d047ff0620d4500849876915bb10e87
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# SONY — Sony Group Corp

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/ea9dd09e5d047ff0620d4500849876915bb10e87/brain/companies/SONY/README.md)

## Business overview

Reported issuer name: **Sony Group Corp**. Stable SEC CIK: **0000313838**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| SONY | NYSE | depositary_receipt | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **3651**: Household Audio & Video Equipment. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **consumer-discretionary**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

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
- Forms observed in the retained filing inventory: 144, 20-F, 20-F/A, 3, 4, 424B2, 424B3, 424B5, 425, 6-K, 6-K/A, CORRESP, EFFECT, F-3ASR, F-6, F-6EF, FWP, IRANNOTICE, S-8, S-8 POS, SC 13D, SC 13D/A, SC 13G, SC 13G/A, SD, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:28:27.209138+00:00.

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
| 2026-10-14 | 6-K | 0001104659-26-115761 | — | [S03] |
| 2026-10-05 | 6-K | 0001104659-26-113566 | — | [S04] |
| 2026-09-18 | 4 | 0001193125-26-395188 | — | [S05] |
| 2026-09-15 | 4 | 0001193125-26-391724 | — | [S06] |
| 2026-09-14 | 6-K | 0001104659-26-107340 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-27T15:25:35.250901+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0000313838.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [6-K 0001104659-26-115761](https://www.sec.gov/Archives/edgar/data/313838/000110465926115761/0001104659-26-115761-index.html) — published 2026-10-14; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [6-K 0001104659-26-113566](https://www.sec.gov/Archives/edgar/data/313838/000110465926113566/0001104659-26-113566-index.html) — published 2026-10-05; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [4 0001193125-26-395188](https://www.sec.gov/Archives/edgar/data/313838/000119312526395188/0001193125-26-395188-index.html) — published 2026-09-18; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [4 0001193125-26-391724](https://www.sec.gov/Archives/edgar/data/313838/000119312526391724/0001193125-26-391724-index.html) — published 2026-09-15; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [6-K 0001104659-26-107340](https://www.sec.gov/Archives/edgar/data/313838/000110465926107340/0001104659-26-107340-index.html) — published 2026-09-14; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261027-40530587641-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/ea9dd09e5d047ff0620d4500849876915bb10e87/brain/companies/SONY/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
