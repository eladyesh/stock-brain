---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001001290
cik: 0001001290
company_name: CREDICORP LTD
tickers:
- BAP
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
  - 20-F
  - 20-F/A
  - '3'
  - 3/A
  - '4'
  - 6-K
  - 6-K/A
  - CORRESP
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001001290.json
    sha256: fc70d4ebec3b8796b9bdee091a0dce2c7441605d90c6832d8bac442207ff837d
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001001290.json
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
  url: https://data.sec.gov/submissions/CIK0001001290.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: fc70d4ebec3b8796b9bdee091a0dce2c7441605d90c6832d8bac442207ff837d
- id: S03
  title: 6-K 0001140361-26-036806
  url: https://www.sec.gov/Archives/edgar/data/1001290/000114036126036806/0001140361-26-036806-index.html
  published_at: '2026-09-17'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 6-K 0001140361-26-033379
  url: https://www.sec.gov/Archives/edgar/data/1001290/000114036126033379/0001140361-26-033379-index.html
  published_at: '2026-08-17'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: SCHEDULE 13G 0001422849-26-000114
  url: https://www.sec.gov/Archives/edgar/data/1001290/000142284926000114/0001422849-26-000114-index.html
  published_at: '2026-08-12'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: SCHEDULE 13G/A 0002012383-26-003202
  url: https://www.sec.gov/Archives/edgar/data/1001290/000201238326003202/0002012383-26-003202-index.html
  published_at: '2026-08-03'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: SCHEDULE 13G 0002012383-26-002139
  url: https://www.sec.gov/Archives/edgar/data/1001290/000201238326002139/0002012383-26-002139-index.html
  published_at: '2026-07-27'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S54
  url: https://www.sec.gov/Archives/edgar/data/1001290/000100129026000008/bap-20251231.htm
  title: 20-F 0001001290-26-000008
  published_at: '2026-04-27'
  retrieved_at: '2026-11-19T21:13:46.710960+00:00'
  sha256: 50c60e31b68820657b24dfcf312a6e10e4ae9cef651678a39fbe6a94268c7a1f
issuer_classification:
  cik: 0001001290
  classification_status: reported_sic
  entity_type: other
  name: CREDICORP LTD
  sic: '6029'
  sic_description: Commercial Banks, NEC
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: fc70d4ebec3b8796b9bdee091a0dce2c7441605d90c6832d8bac442207ff837d
  url: https://data.sec.gov/submissions/CIK0001001290.json
listings:
- ticker: BAP
  exchange: NYSE
  instrument_type: common_stock
research_filings:
- accession: 0001001290-26-000008
  filed: '2026-04-27'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1001290/000100129026000008/0001001290-26-000008-index.html
- accession: 0001140361-25-026765
  filed: '2025-07-22'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1001290/000114036125026765/0001140361-25-026765-index.html
- accession: 0001140361-22-019956
  filed: '2022-05-19'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1001290/000114036122019956/0001140361-22-019956-index.html
- accession: 0001144204-12-060174
  filed: '2012-11-08'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1001290/000114420412060174/0001144204-12-060174-index.html
- accession: 0001144204-11-010517
  filed: '2011-02-23'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1001290/000114420411010517/0001144204-11-010517-index.html
- accession: 0001144204-08-056081
  filed: '2008-10-03'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1001290/000114420408056081/0001144204-08-056081-index.html
- accession: 0001144204-07-038288
  filed: '2007-07-25'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1001290/000114420407038288/0001144204-07-038288-index.html
- accession: 0001144204-07-034872
  filed: '2007-07-02'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1001290/000114420407034872/0001144204-07-034872-index.html
- accession: 0001292814-06-000118
  filed: '2006-01-23'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1001290/000129281406000118/0001292814-06-000118-index.html
- accession: 0001140361-26-036806
  filed: '2026-09-17'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1001290/000114036126036806/0001140361-26-036806-index.html
- accession: 0001140361-24-003938
  filed: '2024-01-26'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1001290/000114036124003938/0001140361-24-003938-index.html
- accession: 0001140361-23-010117
  filed: '2023-03-03'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1001290/000114036123010117/0001140361-23-010117-index.html
research_progress:
  stage: evidence_collected
  input_sha256: 6f99624feca2b180f8b55f4c59cc0b1c3e0fcd8d33b70060d7afad8906697710
  last_attempt_at: '2026-11-19T21:08:42.711300+00:00'
  last_success_at: '2026-11-19T21:08:42.711300+00:00'
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
  source_url: https://data.sec.gov/submissions/CIK0001001290.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/0f49b319f95dcee8e757e592a38a028a04a7bc3c/brain/companies/BAP/README.md
full_history_commit: 0f49b319f95dcee8e757e592a38a028a04a7bc3c
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# BAP — CREDICORP LTD

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/0f49b319f95dcee8e757e592a38a028a04a7bc3c/brain/companies/BAP/README.md)

## Business overview

Reported issuer name: **CREDICORP LTD**. Stable SEC CIK: **0001001290**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| BAP | NYSE | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 20-F, filed 2026-04-27, L853:

> We operate primarily through our four lines of business (LoBs): Universal Banking, Microfinance, Insurance & Pensions, and Investment Management & Advisory. Additionally, we complement the operations of our LoBs through our innovation portfolio which is managed by the Innovation Committee at a corporate level. For more information about our innovation portfolio and strategy, please review “ITEM 4. INFORMATION ON THE COMPANY – 4.B Business Overview – (1) Credicorp Overview – Our Innovation Strategy”. [S54]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 20-F, filed 2026-04-27, L1459:

> During 2022, we implemented our corporate innovation system at Credicorp Ltd. level. This system is focused on disruptive initiatives; that is, those that (i) are aimed at achieving new revenue streams through new business models, (ii) may compete with our own traditional businesses, and (iii) may require building new and critical capabilities, either operational, digital, or technological. The system is steered by the Chief Innovation Officer (CINO), with the support of the Innovation Management Office (IMO). The CINO and the IMO oversee (i) the definition of an innovation strategy at a corporate level, (ii) the management of the disruptive initiative portfolio, (iii) the development of the necessary innovation enablers; and (iv) the execution of activities and transversal projects to foster and improve innovation efforts. We periodically review potential disruptive initiatives so that we can manage them within funds, financial limits, and metrics structured as a portfolio. The CINO steers this process, which is performed alongside the Finance Department and validated by the Innovation Committee. [S54]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 20-F, filed 2026-04-27, L1153:

> We also face increasing competition from non-banking and digital bank competitors in markets for some of our products and services. These non-banking competitors, including fintech and startup companies and other technology companies, have emerged in recent years with increasing digitalization, and these competitors may adversely affect our results of operations. Some of these competitors operate under different or reduced levels of regulation in comparison to the regular banking supervision that applies to BCP Stand-alone and Mibanco. Therefore, these non-banking competitors are not subject to the same specific solvency or liquidity requirements as banks. [S54]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 20-F, filed 2026-04-27, L1189:

> The Group benefits from short-term funding sources, including primarily demand deposits, securities lending and time deposits. The Group's ability to generate deposits depends on its reputation, customer service and competitive pricing. Our access to deposits may also be adversely affected by the liquidity needs of our depositors, which may increase in an inflationary environment where they may be compelled to withdraw deposits in order to cover rising expenses. As a part of our liquidity management, we must ensure we can respond effectively to potential volatility in our customers’ deposit balances. [S54]

## Industry and value chain

SEC-reported SIC **6029**: Commercial Banks, NEC. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 20-F, filed 2026-04-27, L952:

> Between December 2022, when Boluarte took office, and the first months of 2023, social unrest increased, mainly in southern regions of Peru which represent around 15% of Peru’s GDP, where Castillo had more support. Protesters demanded the release of former President Castillo and the holding of new general elections. Protests were violent and resulted in supply chain disruptions due to road blockages, and some regional airports suspended operations temporarily as infrastructure was damaged. Additionally, some mining operations were also disrupted as they faced road blockages and supply shortages. Furthermore, the protest negatively affected the tourism, hospitality, transportation, construction, and retail sectors. [S54]

Navigation sector: **financials**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 20-F, filed 2026-04-27, L763:

> Instituto Nacional de Defensa de la Competencia y de la Protección de la Propiedad Intelectual del Peru or National Institute for the Defense of Competition and the Protection of Intellectual Property of Peru [S54]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 20-F, filed 2026-04-27, L763:

> Instituto Nacional de Defensa de la Competencia y de la Protección de la Propiedad Intelectual del Peru or National Institute for the Defense of Competition and the Protection of Intellectual Property of Peru [S54]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 20-F, filed 2026-04-27, L1186:

> Our ability to borrow on a secured or unsecured basis, and the cost of doing so, can be affected by increases in interest rates or credit spreads, a downturn in the geographic markets in which our loans are concentrated, the availability of credit, regulatory requirements relating to liquidity or the market perceptions of risk relating to us, certain of our counterparties or the banking sector or the financial services sector as a whole, including our perceived or actual creditworthiness, as well as other factors that may be outside our control. An inability to obtain financing in the unsecured long-term or short-term debt capital markets, or to access the secured lending markets, could have a substantial adverse effect on our liquidity. In challenging credit markets, our funding costs may increase, or we may be unable to raise funds to support or expand our businesses, adversely affecting our results of operations. [S54]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 20-F, filed 2026-04-27, L84:

> Indicate by check mark whether any of those error corrections are restatements that required a recovery analysis of incentive based compensation received by any of the registrant’s executive officers during the relevant recovery period pursuant to §240.10D-1(b). o [S54]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 20-F, filed 2026-04-27, L892:

> See “ITEM 3. KEY INFORMATION - 3.D Risk Factors” and “ITEM 5. OPERATING AND FINANCIAL REVIEW AND PROSPECTS” for additional information and other such factors. [S54]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 20-F, 20-F/A, 3, 3/A, 4, 6-K, 6-K/A, CORRESP, SC 13G, SC 13G/A, SCHEDULE 13G, SCHEDULE 13G/A, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:30:43.794680+00:00.

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
| 2026-09-17 | 6-K | 0001140361-26-036806 | — | [S03] |
| 2026-08-17 | 6-K | 0001140361-26-033379 | — | [S04] |
| 2026-08-12 | SCHEDULE 13G | 0001422849-26-000114 | — | [S05] |
| 2026-08-03 | SCHEDULE 13G/A | 0002012383-26-003202 | — | [S06] |
| 2026-07-27 | SCHEDULE 13G | 0002012383-26-002139 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-11-01T16:07:03.340031+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001001290.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [6-K 0001140361-26-036806](https://www.sec.gov/Archives/edgar/data/1001290/000114036126036806/0001140361-26-036806-index.html) — published 2026-09-17; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [6-K 0001140361-26-033379](https://www.sec.gov/Archives/edgar/data/1001290/000114036126033379/0001140361-26-033379-index.html) — published 2026-08-17; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [SCHEDULE 13G 0001422849-26-000114](https://www.sec.gov/Archives/edgar/data/1001290/000142284926000114/0001422849-26-000114-index.html) — published 2026-08-12; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [SCHEDULE 13G/A 0002012383-26-003202](https://www.sec.gov/Archives/edgar/data/1001290/000201238326003202/0002012383-26-003202-index.html) — published 2026-08-03; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [SCHEDULE 13G 0002012383-26-002139](https://www.sec.gov/Archives/edgar/data/1001290/000201238326002139/0002012383-26-002139-index.html) — published 2026-07-27; retrieved 2026-10-23T08:33:02.691743+00:00.

[S54] [20-F 0001001290-26-000008](https://www.sec.gov/Archives/edgar/data/1001290/000100129026000008/bap-20251231.htm) — published 2026-04-27; retrieved 2026-11-19T21:13:46.710960+00:00.

Source release: `coverage-20261101-41324509967-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/0f49b319f95dcee8e757e592a38a028a04a7bc3c/brain/companies/BAP/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
