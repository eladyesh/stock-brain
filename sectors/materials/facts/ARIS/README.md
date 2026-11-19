---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001964504
cik: 0001964504
company_name: Aris Mining Corp
tickers:
- ARIS
status: stub
canonical_reviewed: false
as_of: '2026-11-01'
updated_at: '2026-11-01T16:11:48.803754+00:00'
reviewed_at: null
coverage_release: coverage-20261101-41324509967-1
source_commit: 107777182f87f961989f84e51ee16bb872074fdf
financial_history_available: false
curated_research: null
financial_gap:
  reason: foreign_reporting_adapter
  next_action: Add support for the observed 20-F, 40-F or 6-K reporting forms and
    verify the actual accounting taxonomy before normalization.
  observed_forms:
  - '25'
  - '3'
  - 3/A
  - 40-F
  - 40FR12B
  - 40FR12B/A
  - 6-K
  - 8-A12B
  - CERT
  - F-10
  - F-10EF
  - F-X
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - SD
  - SEC STAFF ACTION
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001964504.json
    sha256: 36b3157a33b267204aa95c47d91035280a5a650d816ad7a86ddf865480df84a3
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001964504.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: otherlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt
  published_at: null
  retrieved_at: '2026-11-01T16:07:03.340031+00:00'
  sha256: ee0a872edece98430f3ba5a1ed6e9c683d7a1bb4b2980bdc9743c6995f264398
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001964504.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 36b3157a33b267204aa95c47d91035280a5a650d816ad7a86ddf865480df84a3
- id: S03
  title: 6-K 0001753926-26-001974
  url: https://www.sec.gov/Archives/edgar/data/1964504/000175392626001974/0001753926-26-001974-index.html
  published_at: '2026-10-21'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 6-K 0001753926-26-001913
  url: https://www.sec.gov/Archives/edgar/data/1964504/000175392626001913/0001753926-26-001913-index.html
  published_at: '2026-10-07'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 6-K 0001753926-26-001879
  url: https://www.sec.gov/Archives/edgar/data/1964504/000175392626001879/0001753926-26-001879-index.html
  published_at: '2026-09-30'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 6-K 0001753926-26-001877
  url: https://www.sec.gov/Archives/edgar/data/1964504/000175392626001877/0001753926-26-001877-index.html
  published_at: '2026-09-29'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: SD 0001104659-26-111490
  url: https://www.sec.gov/Archives/edgar/data/1964504/000110465926111490/0001104659-26-111490-index.html
  published_at: '2026-09-29'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S54
  url: https://www.sec.gov/Archives/edgar/data/1964504/000196450426000012/aris-20251231_d2.htm
  title: 40-F 0001964504-26-000012
  published_at: '2026-03-11'
  retrieved_at: '2026-11-14T18:41:49.897029+00:00'
  sha256: c97b73e444337133f953757646a034c3a5c8cedd7df67eb44d79cd34cf7f3eb7
issuer_classification:
  cik: 0001964504
  classification_status: reported_sic
  entity_type: other
  name: Aris Mining Corp
  sic: '1040'
  sic_description: Gold and Silver Ores
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 36b3157a33b267204aa95c47d91035280a5a650d816ad7a86ddf865480df84a3
  url: https://data.sec.gov/submissions/CIK0001964504.json
listings:
- ticker: ARIS
  exchange: NYSE
  instrument_type: common_stock
research_filings:
- accession: 0001964504-26-000012
  filed: '2026-03-11'
  form: 40-F
  url: https://www.sec.gov/Archives/edgar/data/1964504/000196450426000012/0001964504-26-000012-index.html
- accession: 0001753926-26-001974
  filed: '2026-10-21'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1964504/000175392626001974/0001753926-26-001974-index.html
research_progress:
  stage: evidence_collected
  input_sha256: 4effeec072bef4a6892fec44e541754c234f56dd18beddfade435b7f1acd17c1
  last_attempt_at: '2026-11-14T18:39:40.176158+00:00'
  last_success_at: '2026-11-14T18:39:40.176158+00:00'
  next_retry_at: null
  source_set_current: true
  evidence_topics:
  - competitive-landscape
  - industry-and-value-chain
  - management-and-governance
  - revenue-model-and-segments
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
  source_url: https://data.sec.gov/submissions/CIK0001964504.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/0f49b319f95dcee8e757e592a38a028a04a7bc3c/brain/companies/ARIS/README.md
full_history_commit: 0f49b319f95dcee8e757e592a38a028a04a7bc3c
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# ARIS — Aris Mining Corp

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/0f49b319f95dcee8e757e592a38a028a04a7bc3c/brain/companies/ARIS/README.md)

## Business overview

Reported issuer name: **Aris Mining Corp**. Stable SEC CIK: **0001964504**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| ARIS | NYSE | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 40-F, filed 2026-03-11, L208:

> This Policy applies in the event of any restatement (“Restatement”) of the Company’s financial results due to its material non-compliance with financial reporting requirements under the securities laws. This Policy does not apply to restatements that are not caused by non-compliance with financial reporting requirements, such as, but not limited to, a retrospective: (1) application of a change in accounting principles; (2) revision to reportable segment information due to a change in the structure of the Company’s internal organization; (3) reclassification due to a discontinued operation; (4) application of a change in reporting entity, such as from a reorganization of entities under common control; (5) adjustment to provision amounts in connection with a prior business combination; and (6) revision for stock splits, reverse stock splits, dividends or other changes in capital structure (collectively the “Restatement Exclusions”). [S54]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **1040**: Gold and Silver Ores. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 40-F, filed 2026-03-11, L76:

> Certain statements in this annual report on Form 40-F of Aris Mining Corporation (“the Company” or “Aris Mining”) constitute forward-looking information. Often, but not always, forward-looking statements use words or phrases such as: “anticipate”, “believe”, “continue”, “estimate”, “expect”, “future”, “goal”, “guidance”, “intend”, “likely”, “objective”, “opportunity”, “plan”, “possible”, “potential”, “probable”, “project”, “target” or state that certain actions, events or results “may”, “could”, “would”, “might” or “will” be taken, occur or be achieved. Such forward-looking statements, include but are not limited to statements with respect to local environmental and regulatory requirements and delays in obtaining required environmental and other licenses, changes in national and local government legislation, taxation, controls, regulations and political or economic developments, uncertainties and hazards associated with gold exploration, development and mining, risks associated with tailings and water management, risks associated with costs, supply chain disruptions, and financial risks due to changes in tariffs, trade policies, international trade disputes, or regulatory shifts, risks associated with operating in foreign jurisdictions, risks associated with capital and operating cost estimates, dependence of operations on construction and maintenance of adequate … [S54]

Navigation sector: **materials**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 40-F, filed 2026-03-11, L76:

> Certain statements in this annual report on Form 40-F of Aris Mining Corporation (“the Company” or “Aris Mining”) constitute forward-looking information. Often, but not always, forward-looking statements use words or phrases such as: “anticipate”, “believe”, “continue”, “estimate”, “expect”, “future”, “goal”, “guidance”, “intend”, “likely”, “objective”, “opportunity”, “plan”, “possible”, “potential”, “probable”, “project”, “target” or state that certain actions, events or results “may”, “could”, “would”, “might” or “will” be taken, occur or be achieved. Such forward-looking statements, include but are not limited to statements with respect to local environmental and regulatory requirements and delays in obtaining required environmental and other licenses, changes in national and local government legislation, taxation, controls, regulations and political or economic developments, uncertainties and hazards associated with gold exploration, development and mining, risks associated with tailings and water management, risks associated with costs, supply chain disruptions, and financial risks due to changes in tariffs, trade policies, international trade disputes, or regulatory shifts, risks associated with operating in foreign jurisdictions, risks associated with capital and operating cost estimates, dependence of operations on construction and maintenance of adequate … [S54]

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

Source excerpt — 40-F, filed 2026-03-11, L74:

> Indicate by check mark whether any of those error corrections are restatements that required a recovery analysis of incentive-based compensation received by any of the registrant’s executive officers during the relevant recovery period pursuant to §240.10D-1(b). ☐ [S54]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 40-F, filed 2026-03-11, L76:

> Certain statements in this annual report on Form 40-F of Aris Mining Corporation (“the Company” or “Aris Mining”) constitute forward-looking information. Often, but not always, forward-looking statements use words or phrases such as: “anticipate”, “believe”, “continue”, “estimate”, “expect”, “future”, “goal”, “guidance”, “intend”, “likely”, “objective”, “opportunity”, “plan”, “possible”, “potential”, “probable”, “project”, “target” or state that certain actions, events or results “may”, “could”, “would”, “might” or “will” be taken, occur or be achieved. Such forward-looking statements, include but are not limited to statements with respect to local environmental and regulatory requirements and delays in obtaining required environmental and other licenses, changes in national and local government legislation, taxation, controls, regulations and political or economic developments, uncertainties and hazards associated with gold exploration, development and mining, risks associated with tailings and water management, risks associated with costs, supply chain disruptions, and financial risks due to changes in tariffs, trade policies, international trade disputes, or regulatory shifts, risks associated with operating in foreign jurisdictions, risks associated with capital and operating cost estimates, dependence of operations on construction and maintenance of adequate … [S54]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 25, 3, 3/A, 40-F, 40FR12B, 40FR12B/A, 6-K, 8-A12B, CERT, F-10, F-10EF, F-X, SC 13D, SC 13D/A, SC 13G, SC 13G/A, SCHEDULE 13G, SCHEDULE 13G/A, SD, SEC STAFF ACTION
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:36:27.592541+00:00.

### Research work queue

Collection stage: **evidence_collected**. Extracted evidence is not a reviewed conclusion. Daily collection resumes from durable state; unchanged accessions are reused.

- **Business overview** (evidence or analysis still needed): Explain what the company does, who pays it, and why the business exists. Cite primary sources.
- **Revenue model and segments** (source excerpts available; assess the claim): Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.
- **Products and services** (evidence or analysis still needed): Describe the main products, customer problems solved, distribution, and product dependencies.
- **Customers and end markets** (evidence or analysis still needed): Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.
- **Industry and value chain** (source excerpts available; assess the claim): Place the company among suppliers, distribution channels, customers, and substitutes. Explain cyclicality and supply constraints.
- **Competitive landscape** (source excerpts available; assess the claim): Identify direct competitors and alternatives. Compare specific products or business segments, with sources.
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
| 2026-10-21 | 6-K | 0001753926-26-001974 | — | [S03] |
| 2026-10-07 | 6-K | 0001753926-26-001913 | — | [S04] |
| 2026-09-30 | 6-K | 0001753926-26-001879 | — | [S05] |
| 2026-09-29 | 6-K | 0001753926-26-001877 | — | [S06] |
| 2026-09-29 | SD | 0001104659-26-111490 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-11-01T16:07:03.340031+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001964504.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [6-K 0001753926-26-001974](https://www.sec.gov/Archives/edgar/data/1964504/000175392626001974/0001753926-26-001974-index.html) — published 2026-10-21; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [6-K 0001753926-26-001913](https://www.sec.gov/Archives/edgar/data/1964504/000175392626001913/0001753926-26-001913-index.html) — published 2026-10-07; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [6-K 0001753926-26-001879](https://www.sec.gov/Archives/edgar/data/1964504/000175392626001879/0001753926-26-001879-index.html) — published 2026-09-30; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [6-K 0001753926-26-001877](https://www.sec.gov/Archives/edgar/data/1964504/000175392626001877/0001753926-26-001877-index.html) — published 2026-09-29; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [SD 0001104659-26-111490](https://www.sec.gov/Archives/edgar/data/1964504/000110465926111490/0001104659-26-111490-index.html) — published 2026-09-29; retrieved 2026-10-23T08:33:02.691743+00:00.

[S54] [40-F 0001964504-26-000012](https://www.sec.gov/Archives/edgar/data/1964504/000196450426000012/aris-20251231_d2.htm) — published 2026-03-11; retrieved 2026-11-14T18:41:49.897029+00:00.

Source release: `coverage-20261101-41324509967-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/0f49b319f95dcee8e757e592a38a028a04a7bc3c/brain/companies/ARIS/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
