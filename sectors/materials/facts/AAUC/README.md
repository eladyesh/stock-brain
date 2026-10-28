---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001993344
cik: 0001993344
company_name: Allied Gold Corp
tickers:
- AAUC
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
  - 40-F
  - 40FR12B
  - 6-K
  - CERT
  - D
  - F-X
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - SD
  - SEC STAFF ACTION
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001993344.json
    sha256: 1b689ebf709fd8c7bf4cf0bc71760744f1315997446fbe81821de9de8b9a054b
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001993344.json
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
  url: https://data.sec.gov/submissions/CIK0001993344.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 1b689ebf709fd8c7bf4cf0bc71760744f1315997446fbe81821de9de8b9a054b
- id: S03
  title: 6-K 0001171843-26-006439
  url: https://www.sec.gov/Archives/edgar/data/1993344/000117184326006439/0001171843-26-006439-index.html
  published_at: '2026-10-06'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 6-K 0001171843-26-006097
  url: https://www.sec.gov/Archives/edgar/data/1993344/000117184326006097/0001171843-26-006097-index.html
  published_at: '2026-09-17'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: SCHEDULE 13G/A 0001172661-26-004335
  url: https://www.sec.gov/Archives/edgar/data/1993344/000117266126004335/0001172661-26-004335-index.html
  published_at: '2026-09-03'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 6-K 0001171843-26-005634
  url: https://www.sec.gov/Archives/edgar/data/1993344/000117184326005634/0001171843-26-005634-index.html
  published_at: '2026-08-18'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 6-K 0001104659-26-098393
  url: https://www.sec.gov/Archives/edgar/data/1993344/000110465926098393/0001104659-26-098393-index.html
  published_at: '2026-08-18'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S54
  url: https://www.sec.gov/Archives/edgar/data/1993344/000162828026022512/aaue-20251231.htm
  title: 40-F 0001628280-26-022512
  published_at: '2026-04-01'
  retrieved_at: '2026-10-23T18:24:30.680528+00:00'
  sha256: 919271f12c81d505bc133ebfda0d6d42a0e27437e57e4b20c86b88fa4654c0e7
issuer_classification:
  cik: 0001993344
  classification_status: reported_sic
  entity_type: other
  name: Allied Gold Corp
  sic: '1040'
  sic_description: Gold and Silver Ores
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 1b689ebf709fd8c7bf4cf0bc71760744f1315997446fbe81821de9de8b9a054b
  url: https://data.sec.gov/submissions/CIK0001993344.json
listings:
- ticker: AAUC
  exchange: NYSE
  instrument_type: common_stock
research_filings:
- accession: 0001628280-26-022512
  filed: '2026-04-01'
  form: 40-F
  url: https://www.sec.gov/Archives/edgar/data/1993344/000162828026022512/0001628280-26-022512-index.html
- accession: 0001171843-26-006439
  filed: '2026-10-06'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1993344/000117184326006439/0001171843-26-006439-index.html
research_progress:
  stage: evidence_collected
  input_sha256: 02fbc420182418061ba7897d08447a14aca0a55cf49bf2552cfc16a06d861b65
  last_attempt_at: '2026-10-23T18:20:50.371071+00:00'
  last_success_at: '2026-10-23T18:20:50.371071+00:00'
  next_retry_at: null
  source_set_current: true
  evidence_topics:
  - management-and-governance
  - risks-and-thesis-breakers
  derived_observations: 0
  model_draft: false
  reviewed: false
sector_assignment:
  sector: materials
  method: project_sic_rule
  sic: '1040'
  sic_description: Gold and Silver Ores
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001993344.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/d9e673c37aaa38580be4e36b4880e8ab015a9390/brain/companies/AAUC/README.md
full_history_commit: d9e673c37aaa38580be4e36b4880e8ab015a9390
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# AAUC — Allied Gold Corp

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/d9e673c37aaa38580be4e36b4880e8ab015a9390/brain/companies/AAUC/README.md)

## Business overview

Reported issuer name: **Allied Gold Corp**. Stable SEC CIK: **0001993344**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| AAUC | NYSE | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **1040**: Gold and Silver Ores. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **materials**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

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

Source excerpt — 40-F, filed 2026-04-01, L79:

> Indicate by check mark whether any of those error corrections are restatements that required a recovery analysis of incentive-based compensation received by any of the registrant’s executive officers during the relevant recovery period pursuant to §240.10D-1(b). [S54]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 40-F, filed 2026-04-01, L82:

> Certain statements in this annual report on Form 40-F of Allied Gold Corporation (the “Company”) constitute forward-looking information and forward-looking statements (collectively, “forward-looking information”). Except for statements of historical fact relating to the Company, information contained herein constitutes forward-looking information, including, but not limited to, any information as to the Company’s strategy, objectives, plans or future financial or operating performance. Forward-looking statements are characterized by words such as “plan”, “expect”, “budget”, “target”, “project”, “intend”, “believe”, “anticipate”, “estimate” and other similar words or negative versions thereof, or statements that certain events or conditions “may”, “will”, “should”, “would” or “could” occur. In particular, forward-looking information included in this annual report on Form 40-F includes, without limitation, statements with respect to the Company’s expectations in connection with the production and exploration, development and expansion plans at the Company’s projects discussed herein being met, the Company’s plans to continue building on its base of significant gold production, development-stage properties, exploration properties and land positions in Mali, Côte d’Ivoire and Ethiopia through optimization initiatives at existing operating mines, development of new mines, the … [S54]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 40-F, 40FR12B, 6-K, CERT, D, F-X, SCHEDULE 13G, SCHEDULE 13G/A, SD, SEC STAFF ACTION
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:36:30.424268+00:00.

### Research work queue

Collection stage: **evidence_collected**. Extracted evidence is not a reviewed conclusion. Daily collection resumes from durable state; unchanged accessions are reused.

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
- **Management and governance** (source excerpts available; assess the claim): Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.
- **Valuation context** (evidence or analysis still needed): Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.
- **Catalysts** (evidence or analysis still needed): List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.
- **Risks and thesis breakers** (source excerpts available; assess the claim): Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.
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
| 2026-10-06 | 6-K | 0001171843-26-006439 | — | [S03] |
| 2026-09-17 | 6-K | 0001171843-26-006097 | — | [S04] |
| 2026-09-03 | SCHEDULE 13G/A | 0001172661-26-004335 | — | [S05] |
| 2026-08-18 | 6-K | 0001171843-26-005634 | — | [S06] |
| 2026-08-18 | 6-K | 0001104659-26-098393 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-28T16:09:02.154543+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001993344.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [6-K 0001171843-26-006439](https://www.sec.gov/Archives/edgar/data/1993344/000117184326006439/0001171843-26-006439-index.html) — published 2026-10-06; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [6-K 0001171843-26-006097](https://www.sec.gov/Archives/edgar/data/1993344/000117184326006097/0001171843-26-006097-index.html) — published 2026-09-17; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [SCHEDULE 13G/A 0001172661-26-004335](https://www.sec.gov/Archives/edgar/data/1993344/000117266126004335/0001172661-26-004335-index.html) — published 2026-09-03; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [6-K 0001171843-26-005634](https://www.sec.gov/Archives/edgar/data/1993344/000117184326005634/0001171843-26-005634-index.html) — published 2026-08-18; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [6-K 0001104659-26-098393](https://www.sec.gov/Archives/edgar/data/1993344/000110465926098393/0001104659-26-098393-index.html) — published 2026-08-18; retrieved 2026-10-23T08:33:02.691743+00:00.

[S54] [40-F 0001628280-26-022512](https://www.sec.gov/Archives/edgar/data/1993344/000162828026022512/aaue-20251231.htm) — published 2026-04-01; retrieved 2026-10-23T18:24:30.680528+00:00.

Source release: `coverage-20261028-40722802424-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/d9e673c37aaa38580be4e36b4880e8ab015a9390/brain/companies/AAUC/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
