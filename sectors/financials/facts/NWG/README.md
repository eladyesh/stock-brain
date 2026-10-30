---
schema_version: 1
document_type: company_facts
company_id: company-cik-0000844150
cik: 0000844150
company_name: NatWest Group plc
tickers:
- NWG
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
  reason: foreign_reporting_adapter
  next_action: Add support for the observed 20-F, 40-F or 6-K reporting forms and
    verify the actual accounting taxonomy before normalization.
  observed_forms:
  - 13F-HR
  - '144'
  - 20-F
  - 25-NSE
  - 424B2
  - 424B5
  - 6-K
  - 6-K/A
  - 8-A12B
  - CERT
  - CT ORDER
  - F-3ASR
  - F-N
  - FWP
  - IRANNOTICE
  - S-8
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13D/A
  - SCHEDULE 13G/A
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0000844150.json
    sha256: 12b1a11fd3600c0eac819186f9c1367c501336237e8018afe80e1fe5bb46ec03
    retrieved_at: '2026-10-24T13:22:51.759433+00:00'
    archive: &id001
      member: CIK0000844150.json
      sha256: 593fbbea6512ef5ec729a5e513c465fbedaac8a66602c0abe00d0ba5a4d18732
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: otherlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt
  published_at: null
  retrieved_at: '2026-10-30T16:00:12.358089+00:00'
  sha256: a960a0bfc5439fac9e467fe07ef1f44afe893ba2afc3297648321a80ce09971e
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0000844150.json
  published_at: null
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 12b1a11fd3600c0eac819186f9c1367c501336237e8018afe80e1fe5bb46ec03
- id: S03
  title: 6-K 0001654954-26-009121
  url: https://www.sec.gov/Archives/edgar/data/844150/000165495426009121/0001654954-26-009121-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S04
  title: CERT 0000876661-26-000852
  url: https://www.sec.gov/Archives/edgar/data/844150/000087666126000852/0000876661-26-000852-index.html
  published_at: '2026-10-21'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S05
  title: 8-A12B 0000950103-26-015725
  url: https://www.sec.gov/Archives/edgar/data/844150/000095010326015725/0000950103-26-015725-index.html
  published_at: '2026-10-16'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S06
  title: 6-K 0000950103-26-015723
  url: https://www.sec.gov/Archives/edgar/data/844150/000095010326015723/0000950103-26-015723-index.html
  published_at: '2026-10-16'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S07
  title: 6-K 0001654954-26-008939
  url: https://www.sec.gov/Archives/edgar/data/844150/000165495426008939/0001654954-26-008939-index.html
  published_at: '2026-10-14'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S54
  url: https://www.sec.gov/Archives/edgar/data/844150/000110465926016245/nwg-20251231x20f.htm
  title: 20-F 0001104659-26-016245
  published_at: '2026-02-17'
  retrieved_at: '2026-10-30T16:14:13.341712+00:00'
  sha256: d57909313dd276b017bb82121756a3bdc99007d01e12d39e85a7f940a8314262
issuer_classification:
  cik: 0000844150
  classification_status: reported_sic
  entity_type: other
  name: NatWest Group plc
  sic: '6029'
  sic_description: Commercial Banks, NEC
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 12b1a11fd3600c0eac819186f9c1367c501336237e8018afe80e1fe5bb46ec03
  url: https://data.sec.gov/submissions/CIK0000844150.json
listings:
- ticker: NWG
  exchange: NYSE
  instrument_type: depositary_receipt
research_filings:
- accession: 0001104659-26-016245
  filed: '2026-02-17'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/844150/000110465926016245/0001104659-26-016245-index.html
- accession: 0001654954-26-009121
  filed: '2026-10-23'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/844150/000165495426009121/0001654954-26-009121-index.html
- accession: 0000950103-24-003381
  filed: '2024-03-04'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/844150/000095010324003381/0000950103-24-003381-index.html
- accession: 0001654954-23-003171
  filed: '2023-03-20'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/844150/000165495423003171/0001654954-23-003171-index.html
research_progress:
  stage: evidence_collected
  input_sha256: 202b19553a96598a4dd10d832b986d9fc3db8890a1fab70485c88026a1c621aa
  last_attempt_at: '2026-10-30T16:11:34.164763+00:00'
  last_success_at: '2026-10-30T16:11:34.164763+00:00'
  next_retry_at: null
  source_set_current: true
  evidence_topics:
  - business-overview
  - competitive-landscape
  - customers-and-end-markets
  - growth-drivers
  - industry-and-value-chain
  - management-and-governance
  - moat-and-differentiation
  - products-and-services
  - recent-developments
  - revenue-model-and-segments
  - risks-and-thesis-breakers
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
  source_url: https://data.sec.gov/submissions/CIK0000844150.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/79888139fa1fe8ad3404e6bc04e318eee1474f73/brain/companies/NWG/README.md
full_history_commit: 79888139fa1fe8ad3404e6bc04e318eee1474f73
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# NWG — NatWest Group plc

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/79888139fa1fe8ad3404e6bc04e318eee1474f73/brain/companies/NWG/README.md)

## Business overview

Reported issuer name: **NatWest Group plc**. Stable SEC CIK: **0000844150**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| NWG | NYSE | depositary_receipt | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 20-F, filed 2026-02-17, L63599:

> Employees may receive variable compensation in cash, in deferred cash or debt instruments of NatWest Group or in ordinary shares of NatWest Group plc subject to deferral, clawback and forfeiture criteria. We operate a number of share-based compensation schemes under which we grant awards of NatWest Group plc shares and share options to our employees. Such awards are subject to vesting conditions. [S54]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 20-F, filed 2026-02-17, L1202:

> In the Annual Report on Form 20-F, unless specified otherwise, ‘parent company’ refers to NatWest Group plc, and ‘NatWest Group’, ‘Group’ or ‘we’ refers to NatWest Group plc and its subsidiaries. The term ‘NWH Group’ refers to NatWest Holdings Limited (‘NWH Limited’) and its subsidiary and associated undertakings. The term ‘NWM Group’ refers to NatWest Markets Plc (‘NWM Plc’) and its subsidiary and associated undertakings. The term 'RBSH N.V.' refers to RBS Holdings N.V. The term ‘NWM N.V.’ refers to NatWest Markets N.V. The term ‘NWM N.V. Group’ refers to NatWest Markets N.V. and its subsidiary and associated undertakings The term ‘NWMSI’ refers to NatWest Markets Securities, Inc. The term ‘RBS plc’ refers to The Royal Bank of Scotland plc. The term ‘NWB Plc’ refers to National Westminster Bank Plc. The term ‘RBSI Ltd’ refers to The Royal Bank of Scotland International Limited. Effective from Q2 2025, the reportable segment Private Banking was renamed Private Banking & Wealth Management. This does not change the financial results of Private Banking & Wealth Management or the consolidated financial results of NatWest Group. [S54]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 20-F, filed 2026-02-17, L105484:

> \| ● \| changes to the regulatory environment and associated requirements which could lead to shifts in operating cost and regulatory capital requirements that impact NatWest Group’s product offerings and business models (see ‘NatWest Group’s businesses are subject to substantial regulation and oversight, which are constantly evolving and may adversely affect NatWest Group’ and ‘NatWest Group could incur losses or be required to maintain higher levels of capital as a result of limitations or failure of various models.) [S54]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 20-F, filed 2026-02-17, L1299:

> We continued to support our customers as net loans to customers of £418.9 billion increased by £18.6 billion in the year and net loans to customers excluding central items increased by £20.7 billion in the year. Retail Banking mortgage balances increased by £5.1 billion and Commercial & Institutional balances were up by £12.3 billion. [S54]

## Industry and value chain

SEC-reported SIC **6029**: Commercial Banks, NEC. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 20-F, filed 2026-02-17, L1111:

> We caution you that a large number of important factors could adversely affect our results or our ability to implement our strategy, cause us to fail to meet our targets, predictions, expectations and other anticipated outcomes or affect the accuracy of forward-looking statements described in this document. These factors include, but are not limited to, those set forth in the risk factors and the other uncertainties described in NatWest Group plc’s 2025 Annual Report on Form 20-F, and its other filings with the US Securities and Exchange Commission. The principal risks and uncertainties that could adversely affect NatWest Group’s future results, its financial condition and/or prospects and cause them to be materially different from what is forecast or expected, include, but are not limited to: economic and political risk (including in respect of: political and economic risks and uncertainty in the UK and global markets, including as a result of inflation and interest rates, supply chain disruption, protectionist policies, and geopolitical developments); and changes in interest rates and foreign currency exchange rates; business change and execution risk (including in respect of the implementation of NatWest Group’s strategy; future acquisitions and divestments, the competitive environment; and the transfer of its EU corporate portfolio); financial resilience risk (including in … [S54]

Navigation sector: **financials**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 20-F, filed 2026-02-17, L1137:

> \| ● \| Factors and uncertainties beyond NatWest Group’s control. The extent and pace of climate change, including the timing and manifestation of physical and transition risks and nature loss; the macroeconomic environment; the effectiveness of actions of governments, legislators, regulators and businesses; changes to government policy direction, legislation, regulation and industry and market practice; the response of wider society, including NatWest Group’s value chain, including its investors, customers, counterparties, suppliers and business partners; changes in customer and societal behaviour and demand; availability of commercially viable opportunities in the sustainable and transition finance markets, competition dynamics, capital markets appetite, investor expectations, and external credit and concentration risk appetites which may constrain the scale or risk profile of opportunities accessible to NatWest Group; developments in available technology; the rollout of low carbon infrastructure; and the availability of accurate, verifiable, reliable, auditable, consistent and comparable data. [S54]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 20-F, filed 2026-02-17, L8118:

> NatWest Group’s ability to attract and manage funding remains a critical competitive advantage. Other key competitive factors include cost management, growing digital sales focus, branch network re-shaping, and product simplification. Cost management remains a key focus, as banks seek to simplify their organisational and IT architectures while at the same time investing to ensure that they can meet customers’ evolving channel preferences. Customers have increasingly focused on the use of internet and mobile as sales and service channels for certain types of products. Therefore, competitive position and performance increasingly depends on the possession of user-friendly, diverse and efficient online solutions. [S54]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 20-F, filed 2026-02-17, L1107:

> Certain sections in this document contain ‘forward-looking statements’ as that term is defined in the United States Private Securities Litigation Reform Act of 1995, such as statements with respect to NatWest Group’s financial condition, results of operations and business, including its strategic priorities, financial, investment and capital targets, and climate and sustainability-related targets, commitments and ambitions described herein. Statements that are not historical facts, including statements about NatWest Group’s beliefs and expectations, are forward-looking statements. Words such as ‘expect’, ‘estimate’, ‘project’, ‘anticipate’, ‘commit’, ‘believe’, ‘should’, ‘intend’, ‘will’, ‘plan’, ‘could’, ‘probability’, ‘risk’, ‘target’, ‘goal’, ‘objective’, ‘may’, ‘endeavour’, ‘outlook’, ‘optimistic’, ‘prospects’ and similar expressions or variations on these expressions are intended to identify forward-looking statements. In particular, this document includes forward-looking targets and guidance relating to financial performance measures, such as income growth, operating expense, RoTE, ROE, discretionary capital distribution targets, impairment loss rates, capital generation pre distributions, customer assets and liabilities growth rate, cost: income ratio, balance sheet reduction (including the reduction of RWAs), CET1 ratio (and key drivers of the CET1 ratio including … [S54]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 20-F, filed 2026-02-17, L411:

> Indicate by check mark whether any of those error corrections are restatements that required a recovery analysis of incentive-based compensation received by any of the registrant’s executive officers during the relevant recovery period pursuant to §240.10D-1(b). ☐ [S54]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 20-F, filed 2026-02-17, L1111:

> We caution you that a large number of important factors could adversely affect our results or our ability to implement our strategy, cause us to fail to meet our targets, predictions, expectations and other anticipated outcomes or affect the accuracy of forward-looking statements described in this document. These factors include, but are not limited to, those set forth in the risk factors and the other uncertainties described in NatWest Group plc’s 2025 Annual Report on Form 20-F, and its other filings with the US Securities and Exchange Commission. The principal risks and uncertainties that could adversely affect NatWest Group’s future results, its financial condition and/or prospects and cause them to be materially different from what is forecast or expected, include, but are not limited to: economic and political risk (including in respect of: political and economic risks and uncertainty in the UK and global markets, including as a result of inflation and interest rates, supply chain disruption, protectionist policies, and geopolitical developments); and changes in interest rates and foreign currency exchange rates; business change and execution risk (including in respect of the implementation of NatWest Group’s strategy; future acquisitions and divestments, the competitive environment; and the transfer of its EU corporate portfolio); financial resilience risk (including in … [S54]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 13F-HR, 144, 20-F, 25-NSE, 424B2, 424B5, 6-K, 6-K/A, 8-A12B, CERT, CT ORDER, F-3ASR, F-N, FWP, IRANNOTICE, S-8, SC 13D/A, SC 13G, SC 13G/A, SCHEDULE 13D/A, SCHEDULE 13G/A
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:29:37.117562+00:00.

### Research work queue

Collection stage: **evidence_collected**. Extracted evidence is not a reviewed conclusion. Daily collection resumes from durable state; unchanged accessions are reused.

- **Business overview** (source excerpts available; assess the claim): Explain what the company does, who pays it, and why the business exists. Cite primary sources.
- **Revenue model and segments** (source excerpts available; assess the claim): Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.
- **Products and services** (source excerpts available; assess the claim): Describe the main products, customer problems solved, distribution, and product dependencies.
- **Customers and end markets** (source excerpts available; assess the claim): Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.
- **Industry and value chain** (source excerpts available; assess the claim): Place the company among suppliers, distribution channels, customers, and substitutes. Explain cyclicality and supply constraints.
- **Competitive landscape** (source excerpts available; assess the claim): Identify direct competitors and alternatives. Compare specific products or business segments, with sources.
- **Moat and differentiation** (source excerpts available; assess the claim): Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.
- **Growth drivers** (source excerpts available; assess the claim): Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.
- **Financial performance** (evidence or analysis still needed): Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.
- **Balance sheet and capital allocation** (evidence or analysis still needed): Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.
- **Management and governance** (source excerpts available; assess the claim): Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.
- **Valuation context** (evidence or analysis still needed): Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.
- **Catalysts** (evidence or analysis still needed): List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.
- **Risks and thesis breakers** (source excerpts available; assess the claim): Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.
- **Scenarios and open questions** (evidence or analysis still needed): Separate bull, base, and bear assumptions from facts. Record missing data, disputed evidence, and research questions without inventing answers.
- **Relationships and themes** (evidence or analysis still needed): Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.
- **Recent developments** (source excerpts available; assess the claim): Keep a dated, source-backed log of material changes. Distinguish the event date from the article date and explain what changed in the profile.

Calculation gaps: Validated financial history is missing.

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest five available filing metadata records; document bodies have not been analyzed here.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-10-23 | 6-K | 0001654954-26-009121 | — | [S03] |
| 2026-10-21 | CERT | 0000876661-26-000852 | — | [S04] |
| 2026-10-16 | 8-A12B | 0000950103-26-015725 | — | [S05] |
| 2026-10-16 | 6-K | 0000950103-26-015723 | — | [S06] |
| 2026-10-14 | 6-K | 0001654954-26-008939 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-30T16:00:12.358089+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0000844150.json) — published not supplied; retrieved 2026-10-24T13:22:51.759433+00:00.

[S03] [6-K 0001654954-26-009121](https://www.sec.gov/Archives/edgar/data/844150/000165495426009121/0001654954-26-009121-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S04] [CERT 0000876661-26-000852](https://www.sec.gov/Archives/edgar/data/844150/000087666126000852/0000876661-26-000852-index.html) — published 2026-10-21; retrieved 2026-10-24T13:22:51.759433+00:00.

[S05] [8-A12B 0000950103-26-015725](https://www.sec.gov/Archives/edgar/data/844150/000095010326015725/0000950103-26-015725-index.html) — published 2026-10-16; retrieved 2026-10-24T13:22:51.759433+00:00.

[S06] [6-K 0000950103-26-015723](https://www.sec.gov/Archives/edgar/data/844150/000095010326015723/0000950103-26-015723-index.html) — published 2026-10-16; retrieved 2026-10-24T13:22:51.759433+00:00.

[S07] [6-K 0001654954-26-008939](https://www.sec.gov/Archives/edgar/data/844150/000165495426008939/0001654954-26-008939-index.html) — published 2026-10-14; retrieved 2026-10-24T13:22:51.759433+00:00.

[S54] [20-F 0001104659-26-016245](https://www.sec.gov/Archives/edgar/data/844150/000110465926016245/nwg-20251231x20f.htm) — published 2026-02-17; retrieved 2026-10-30T16:14:13.341712+00:00.

Source release: `coverage-20261030-41085569265-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/79888139fa1fe8ad3404e6bc04e318eee1474f73/brain/companies/NWG/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
