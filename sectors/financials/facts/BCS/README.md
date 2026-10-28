---
schema_version: 1
document_type: company_facts
company_id: company-cik-0000312069
cik: 0000312069
company_name: BARCLAYS PLC
tickers:
- BCS
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
  - 13F-HR
  - 13F-HR/A
  - 13F-NT
  - '144'
  - 20-F
  - 20-F/A
  - 25-NSE
  - '3'
  - 3/A
  - '4'
  - 424B2
  - 6-K
  - 8-A12B
  - CERT
  - CORRESP
  - EFFECT
  - F-3ASR
  - F-6
  - F-6EF
  - F-N
  - FWP
  - IRANNOTICE
  - N-PX
  - S-8
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0000312069.json
    sha256: 0973a2b76dfda82ca9cfa46a88c40d5e77359beaf067e4731e839c4949dcdbd1
    retrieved_at: '2026-10-24T13:22:51.759433+00:00'
    archive: &id001
      member: CIK0000312069.json
      sha256: 593fbbea6512ef5ec729a5e513c465fbedaac8a66602c0abe00d0ba5a4d18732
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
  url: https://data.sec.gov/submissions/CIK0000312069.json
  published_at: null
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 0973a2b76dfda82ca9cfa46a88c40d5e77359beaf067e4731e839c4949dcdbd1
- id: S03
  title: 6-K 0001654954-26-009117
  url: https://www.sec.gov/Archives/edgar/data/312069/000165495426009117/0001654954-26-009117-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S04
  title: 6-K 0001654954-26-009079
  url: https://www.sec.gov/Archives/edgar/data/312069/000165495426009079/0001654954-26-009079-index.html
  published_at: '2026-10-22'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S05
  title: 6-K 0000312069-26-000240
  url: https://www.sec.gov/Archives/edgar/data/312069/000031206926000240/0000312069-26-000240-index.html
  published_at: '2026-10-22'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S06
  title: 6-K 0001654954-26-008864
  url: https://www.sec.gov/Archives/edgar/data/312069/000165495426008864/0001654954-26-008864-index.html
  published_at: '2026-10-09'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S07
  title: 144 0002157144-26-000001
  url: https://www.sec.gov/Archives/edgar/data/312069/000215714426000001/0002157144-26-000001-index.html
  published_at: '2026-10-01'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S53
  url: https://www.sec.gov/Archives/edgar/data/312069/000031206922000085/bcs-20211231.htm
  title: 20-F/A 0000312069-22-000085
  published_at: '2022-05-23'
  retrieved_at: '2026-10-25T13:57:35.375433+00:00'
  sha256: 2367dd8f8f2188d9a2272908f3e733022131a2315089ff7d24a3e5161033f8a3
issuer_classification:
  cik: 0000312069
  classification_status: reported_sic
  entity_type: other
  name: BARCLAYS PLC
  sic: '6029'
  sic_description: Commercial Banks, NEC
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 0973a2b76dfda82ca9cfa46a88c40d5e77359beaf067e4731e839c4949dcdbd1
  url: https://data.sec.gov/submissions/CIK0000312069.json
listings:
- ticker: BCS
  exchange: NYSE
  instrument_type: common_stock
research_filings:
- accession: 0000312069-26-000004
  filed: '2026-02-10'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/312069/000031206926000004/0000312069-26-000004-index.html
- accession: 0000312069-22-000085
  filed: '2022-05-23'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/312069/000031206922000085/0000312069-22-000085-index.html
- accession: 0001654954-26-009117
  filed: '2026-10-23'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/312069/000165495426009117/0001654954-26-009117-index.html
research_progress:
  stage: retry
  input_sha256: d4f072669e3114c9f52662bd2dc62d74523662dd17c1790effe8e18bbea0a4f3
  last_attempt_at: '2026-10-25T13:56:40.792803+00:00'
  last_success_at: null
  next_retry_at: '2026-10-26T13:56:40.792803+00:00'
  source_set_current: false
  evidence_topics:
  - business-overview
  - competitive-landscape
  - customers-and-end-markets
  - growth-drivers
  - industry-and-value-chain
  - management-and-governance
  - moat-and-differentiation
  - recent-developments
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
  source_url: https://data.sec.gov/submissions/CIK0000312069.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/d9e673c37aaa38580be4e36b4880e8ab015a9390/brain/companies/BCS/README.md
full_history_commit: d9e673c37aaa38580be4e36b4880e8ab015a9390
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# BCS — BARCLAYS PLC

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/d9e673c37aaa38580be4e36b4880e8ab015a9390/brain/companies/BCS/README.md)

## Business overview

Reported issuer name: **BARCLAYS PLC**. Stable SEC CIK: **0000312069**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| BCS | NYSE | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 20-F/A, filed 2022-05-23, L186; prior source set, update pending:

> \| \| B. Business overview** \| ii (Market and other data), 104 – 105, 187 – 192, 230 – 231 (Note 2) [S53]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 20-F/A, filed 2022-05-23, L737; prior source set, update pending:

> We believe that an effective Board is one which delivers value for our four priority stakeholder groups – our customers and clients, colleagues, society and investors. We assess the effectiveness of our Board, its Committees and Board members annually. You can read about the 2021 effectiveness review, and progress against the 2020 review and recommendations carried forward, in the report of the Board Nominations Committee on pages 15 to 21. [S53]

## Industry and value chain

SEC-reported SIC **6029**: Commercial Banks, NEC. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 20-F/A, filed 2022-05-23, L1436; prior source set, update pending:

> The Committee considered a broad range of potential impacts including evolving inflation expectations, unemployment rates, delayed defaults as support measures were withdrawn, and longer- term structural risks, including the significant increase in global indebtedness in response to the COVID-19 pandemic. During the second half of the year, the Committee focused on the continued improvement in the global economic outlook while considering the risks to the recovery from supply chain constraints and bouts of rising infection rates amid new strains of the virus. The Committee reviewed and approved the Group’s Internal Capital Adequacy Assessment Process (ICAAP) and Internal Liquidity Adequacy Assessment Process (ILAAP) during the course of 2021, concluding that the Group was appropriately capitalised and had adequate liquidity resources. Economic conditions were such that no out-of-cycle refresh of either the ICAAP or the ILAAP was required. [S53]

Navigation sector: **financials**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 20-F/A, filed 2022-05-23, L1295; prior source set, update pending:

> Barclays is engaged in various legal, competition and regulatory matters which may give rise to provisioning based on the facts. [S53]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 20-F/A, filed 2022-05-23, L1026; prior source set, update pending:

> Both the Committee and the Board recognise and embrace the benefits of diversity – of gender, ethnicity, cognitive and personal strengths and social backgrounds – at Board, ExCo and senior management level, and consider this an essential element of maintaining a competitive advantage and effective governance, as well as mitigating the risk of ‘group think’. [S53]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 20-F/A, filed 2022-05-23, L812; prior source set, update pending:

> Against this backdrop, the Board retained its focus on our strategy, including in the context of our refreshed Purpose and newly launched Barclays Mindset. In November, the Board appointed Venkat to take on the role of Group Chief Executive. Venkat is now driving forwards the implementation of the clear strategy that the Board has established. [S53]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 20-F/A, filed 2022-05-23, L290; prior source set, update pending:

> The information in this document, which was approved by the Board of Directors on 22 February 2022 (save for the information expressly revised pursuant to this Amendment No. 1, which was approved by the Board of Directors on 22 May 2022), does not comprise statutory accounts within the meaning of Section 434 of the Companies Act 2006. Statutory accounts for the year ended 31 December 2021, which contain an unmodified audit report under Section 495 of the Companies Act 2006 (which does not make any statements under Section 498 of the Companies Act 2006), will be delivered to the Registrar of Companies in accordance with Section 441 of the Companies Act 2006. [S53]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 20-F/A, filed 2022-05-23, L1632; prior source set, update pending:

> ▪To debate the Risk function’s view of performance, making a recommendation to the Board Remuneration Committee on the financial and operational risk factors to be taken into account in remuneration decisions for 2021. [S53]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 13F-HR, 13F-HR/A, 13F-NT, 144, 20-F, 20-F/A, 25-NSE, 3, 3/A, 4, 424B2, 6-K, 8-A12B, CERT, CORRESP, EFFECT, F-3ASR, F-6, F-6EF, F-N, FWP, IRANNOTICE, N-PX, S-8, SC 13D/A, SC 13G, SC 13G/A, SCHEDULE 13G, SCHEDULE 13G/A, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:28:26.711630+00:00.

### Research work queue

Collection stage: **retry**. Extracted evidence is not a reviewed conclusion. Daily collection resumes from durable state; unchanged accessions are reused.

- **Business overview** (source excerpts available; assess the claim): Explain what the company does, who pays it, and why the business exists. Cite primary sources.
- **Revenue model and segments** (evidence or analysis still needed): Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.
- **Products and services** (evidence or analysis still needed): Describe the main products, customer problems solved, distribution, and product dependencies.
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
| 2026-10-23 | 6-K | 0001654954-26-009117 | — | [S03] |
| 2026-10-22 | 6-K | 0001654954-26-009079 | — | [S04] |
| 2026-10-22 | 6-K | 0000312069-26-000240 | — | [S05] |
| 2026-10-09 | 6-K | 0001654954-26-008864 | — | [S06] |
| 2026-10-01 | 144 | 0002157144-26-000001 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-28T16:09:02.154543+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0000312069.json) — published not supplied; retrieved 2026-10-24T13:22:51.759433+00:00.

[S03] [6-K 0001654954-26-009117](https://www.sec.gov/Archives/edgar/data/312069/000165495426009117/0001654954-26-009117-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S04] [6-K 0001654954-26-009079](https://www.sec.gov/Archives/edgar/data/312069/000165495426009079/0001654954-26-009079-index.html) — published 2026-10-22; retrieved 2026-10-24T13:22:51.759433+00:00.

[S05] [6-K 0000312069-26-000240](https://www.sec.gov/Archives/edgar/data/312069/000031206926000240/0000312069-26-000240-index.html) — published 2026-10-22; retrieved 2026-10-24T13:22:51.759433+00:00.

[S06] [6-K 0001654954-26-008864](https://www.sec.gov/Archives/edgar/data/312069/000165495426008864/0001654954-26-008864-index.html) — published 2026-10-09; retrieved 2026-10-24T13:22:51.759433+00:00.

[S07] [144 0002157144-26-000001](https://www.sec.gov/Archives/edgar/data/312069/000215714426000001/0002157144-26-000001-index.html) — published 2026-10-01; retrieved 2026-10-24T13:22:51.759433+00:00.

[S53] [20-F/A 0000312069-22-000085](https://www.sec.gov/Archives/edgar/data/312069/000031206922000085/bcs-20211231.htm) — published 2022-05-23; retrieved 2026-10-25T13:57:35.375433+00:00.

Source release: `coverage-20261028-40722802424-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/d9e673c37aaa38580be4e36b4880e8ab015a9390/brain/companies/BCS/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
