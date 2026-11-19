---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001379785
cik: 0001379785
company_name: Barings BDC, Inc.
tickers:
- BBDC
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
  reason: latest_filing_incomplete
  next_action: Resolve the latest financial filing/CompanyFacts mismatch; any historical
    bootstrap must keep the latest-period gap explicit.
  observed_forms:
  - 10-K
  - 10-K/A
  - 10-Q
  - '144'
  - '25'
  - 25-NSE
  - '3'
  - 3/A
  - 305B2
  - '4'
  - 4/A
  - 40-17G
  - 40-33
  - 40-APP
  - 40-APP/A
  - 424B2
  - 424B3
  - '425'
  - '497'
  - 497AD
  - '5'
  - 8-A12B
  - 8-K
  - 8-K/A
  - APP NTC
  - APP ORDR
  - CERTNYS
  - CORRESP
  - D
  - D/A
  - DEF 14A
  - DEFA14A
  - DEFM14A
  - DEFR14A
  - EFFECT
  - FWP
  - N-14 8C
  - N-14 8C/A
  - N-14MEF
  - N-2
  - N-2/A
  - N-23C-2
  - N-2ASR
  - POS 8C
  - POS EX
  - PRE 14A
  - PREM14A
  - PRER14A
  - S-8
  - S-8 POS
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SC TO-I
  - SC TO-I/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001379785.json
    sha256: 166ca25128e3a56a2dce266d07091144d717ae329d608cb7e4639e9efe3e6b9b
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001379785.json
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
  url: https://data.sec.gov/submissions/CIK0001379785.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 166ca25128e3a56a2dce266d07091144d717ae329d608cb7e4639e9efe3e6b9b
- id: S03
  title: 40-17G 0001072613-26-000710
  url: https://www.sec.gov/Archives/edgar/data/1379785/000107261326000710/0001072613-26-000710-index.html
  published_at: '2026-08-21'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 8-K 0001379785-26-000031
  url: https://www.sec.gov/Archives/edgar/data/1379785/000137978526000031/0001379785-26-000031-index.html
  published_at: '2026-08-05'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 10-Q 0001379785-26-000030
  url: https://www.sec.gov/Archives/edgar/data/1379785/000137978526000030/0001379785-26-000030-index.html
  published_at: '2026-08-05'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 4 0001225208-26-005818
  url: https://www.sec.gov/Archives/edgar/data/1379785/000122520826005818/0001225208-26-005818-index.html
  published_at: '2026-06-05'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 8-K 0001379785-26-000024
  url: https://www.sec.gov/Archives/edgar/data/1379785/000137978526000024/0001379785-26-000024-index.html
  published_at: '2026-06-01'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S53
  url: https://www.sec.gov/Archives/edgar/data/1379785/000137978526000030/bbdc-20260630.htm
  title: 10-Q 0001379785-26-000030
  published_at: '2026-08-05'
  retrieved_at: '2026-11-19T21:15:17.057332+00:00'
  sha256: 0ef8a466cf1510041f00f24b652a65f55c006d9f7da84247d91833902be8c87d
- id: S56
  url: https://www.sec.gov/Archives/edgar/data/1379785/000137978526000009/bbdc-20251231.htm
  title: 10-K 0001379785-26-000009
  published_at: '2026-02-19'
  retrieved_at: '2026-11-19T21:15:12.099770+00:00'
  sha256: ea2f4e8be68dda3de826afee9bbf04cfe0f8b2f7fef25224aabcf0bd049a5bf1
issuer_classification:
  cik: 0001379785
  classification_status: missing_or_invalid_sic
  entity_type: operating
  name: Barings BDC, Inc.
  sic: null
  sic_description: ''
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 166ca25128e3a56a2dce266d07091144d717ae329d608cb7e4639e9efe3e6b9b
  url: https://data.sec.gov/submissions/CIK0001379785.json
listings:
- ticker: BBDC
  exchange: NYSE
  instrument_type: common_stock
research_filings:
- accession: 0001379785-26-000009
  filed: '2026-02-19'
  form: 10-K
  period_end: '2025-12-31'
  url: https://www.sec.gov/Archives/edgar/data/1379785/000137978526000009/0001379785-26-000009-index.html
- accession: 0001379785-26-000030
  filed: '2026-08-05'
  form: 10-Q
  period_end: '2026-06-30'
  url: https://www.sec.gov/Archives/edgar/data/1379785/000137978526000030/0001379785-26-000030-index.html
- accession: 0001379785-26-000012
  filed: '2026-03-10'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/1379785/000137978526000012/0001379785-26-000012-index.html
- accession: 0001379785-26-000031
  filed: '2026-08-05'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/1379785/000137978526000031/0001379785-26-000031-index.html
- accession: 0001379785-24-000057
  filed: '2024-09-25'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1379785/000137978524000057/0001379785-24-000057-index.html
- accession: 0001140361-22-014385
  filed: '2022-04-13'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1379785/000114036122014385/0001140361-22-014385-index.html
- accession: 0001379785-13-000041
  filed: '2013-08-30'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1379785/000137978513000041/0001379785-13-000041-index.html
- accession: 0001193125-11-165790
  filed: '2011-06-15'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1379785/000119312511165790/0001193125-11-165790-index.html
research_progress:
  stage: evidence_collected
  input_sha256: 24bd9babb9210e20e11d666496265bdf592a34a477f5b1a0ff40c0462ebe3dce
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
  - recent-developments
  - revenue-model-and-segments
  - risks-and-thesis-breakers
  derived_observations: 0
  model_draft: false
  reviewed: false
sector_assignment:
  sector: unclassified
  method: unresolved
  sic: null
  sic_description: ''
  rule_version: 1
  reason: Missing, ambiguous or unmapped reported industry; company-specific review
    is required.
full_history_url: https://github.com/eladyesh/stock-brain/blob/0f49b319f95dcee8e757e592a38a028a04a7bc3c/brain/companies/BBDC/README.md
full_history_commit: 0f49b319f95dcee8e757e592a38a028a04a7bc3c
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# BBDC — Barings BDC, Inc.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/0f49b319f95dcee8e757e592a38a028a04a7bc3c/brain/companies/BBDC/README.md)

## Business overview

Reported issuer name: **Barings BDC, Inc.**. Stable SEC CIK: **0001379785**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| BBDC | NYSE | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 10-Q, filed 2026-08-05, L8755:

> The following discussion is designed to provide a better understanding of our Unaudited Consolidated Financial Statements for the three and six months ended June 30, 2026, including a brief discussion of our business, key factors that impacted our performance and a summary of our operating results. The following discussion should be read in conjunction with the Unaudited Consolidated Financial Statements and the notes thereto included in Item 1 of this Quarterly Report on Form 10-Q, and the Consolidated Financial Statements and notes thereto and Management’s Discussion and Analysis of Financial Condition and Results of Operations contained in our Annual Report on Form 10-K for the year ended December 31, 2025. Historical results and percentage relationships among any amounts in the financial statements are not necessarily indicative of trends in operating results for any future periods. [S53]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 10-Q, filed 2026-08-05, L8103:

> The Company lends to and invests in portfolio companies in various industries. The Company operates as a single operating and reporting segment: lending and investment. The segment generates revenues through debt investments, and on a limited basis, may acquire equity investments in portfolio companies. The accounting policies of the lending and investment segment are the same as those described herein and in the Company’s most recent Annual Report on Form 10-K. The Company has identified the Chief Executive Officer, its President, and Chief Financial Officer as the chief operating decision maker (the “CODM”), who evaluates the performance of the lending and investment segment. The CODM uses segment net investment income before taxes and net increase in net assets resulting from operations to determine the capital allocation of the Company, the dividend policy, and the Company’s investment strategy, which is outlined in “Business–Investment Criteria” in Part I, Item 1 of the Company’s most recent Annual Report on Form 10-K. As the Company operates as a single reportable segment, the segment assets are presented on the accompanying Unaudited and Audited Consolidated Balance Sheets as “total assets” and the net investment income before taxes, significant segment expenses, and net increase in net assets resulting from operations are presented on the accompanying Unaudited … [S53]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 10-K, filed 2026-02-19, L671:

> •may have shorter operating histories, narrower product lines, smaller market shares and/or more significant customer concentration than larger businesses, which tend to render them more vulnerable to competitors’ actions and market conditions, as well as general economic downturns; [S56]

## Industry and value chain

Not available: substantive research has not been completed. Place the company among suppliers, distribution channels, customers, and substitutes. Explain cyclicality and supply constraints.

Source excerpt — 10-K, filed 2026-02-19, L839:

> The extent to which any disease outbreaks or health pandemics may negatively affect our and our portfolio companies’ operating results, or the duration of any potential business or supply chain disruption, is uncertain. These potential impacts, while uncertain, could adversely affect our operating results and the operating results of the portfolio companies in which we invest. There is a risk that any future disease outbreaks or health pandemics (including a recurrence of COVID-19) would impact our ability to achieve our investment objectives. Further, if a future pandemic occurs during a period when our investments are maturing, we may not be able to realize our investments within the Company’s term, or at all. In addition, future terrorist activities, military or security operations, natural disasters, disease outbreaks, pandemics or other similar events could weaken the domestic/global economies and create additional uncertainties, which may negatively impact our portfolio companies and, in turn, could have a material effect on our business, operating results and financial condition. [S56]

Navigation sector: **unclassified**. Method: `unresolved`. Missing, ambiguous or unmapped reported industry; company-specific review is required.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 10-K, filed 2026-02-19, L298:

> We compete for investments with a number of investment funds including public funds, private debt funds and private equity funds, other BDCs, as well as traditional financial services companies such as commercial banks and other sources of financing. Some of these entities have greater financial and managerial resources than we do. In addition, some of our competitors may have higher risk tolerances or different risk assessments, which could allow them to consider more investments and establish more relationships than we do. Furthermore, many of our competitors are not subject to the regulatory restrictions that the 1940 Act imposes on us as a BDC. [S56]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 10-K, filed 2026-02-19, L238:

> •Strong Competitive Position. We seek to invest in companies that have developed strong positions within their respective markets, are well positioned to capitalize on growth opportunities and compete in industries with barriers to entry. We also seek to invest in companies that exhibit a competitive advantage, which may help to protect their market position and profitability. [S56]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 10-K, filed 2026-02-19, L217:

> We seek attractive returns by generating current income primarily from directly-originated debt investments in middle-market companies located primarily in the United States. We also have investments in middle-market companies located outside the United States. Our strategy includes the following components: [S56]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 10-Q, filed 2026-08-05, L3721:

> (1)All debt investments are income producing, unless otherwise noted. The Adviser determines in good faith the fair value of the Company’s investments in accordance with a valuation policy and processes established by the Adviser, which have been approved by the Company’s board of directors (the “Board”), and the Investment Company Act of 1940, as amended (the “1940 Act”). In addition, all debt investments are variable rate investments unless otherwise noted. Index-based floating interest rates are generally subject to a contractual minimum interest rate. Variable rate loans to the Company’s portfolio companies bear interest at a rate that may be determined by reference to the Secured Overnight Financing Rate (“SOFR”), the Euro Interbank Offered Rate (“EURIBOR”), the Bank Bill Swap Bid Rate (“BBSY”), the Stockholm Interbank Offered Rate (“STIBOR”), the Canadian Overnight Repo Rate Average (“CORRA”), the Sterling Overnight Index Average (“SONIA”), the Swiss Average Rate Overnight (“SARON”), the Norwegian Interbank Offered Rate (“NIBOR”), the Bank Bill Market rate (“BKBM”) or an alternate base rate (commonly based on the Federal Funds Rate or the Prime Rate), at the borrower’s option, which reset annually, semi-annually, quarterly or monthly. For each such loan, the Company has provided the interest rate in effect on the date presented. SOFR based contracts may include a credit … [S53]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 10-Q, filed 2026-08-05, L8177:

> The February 2019 Credit Facility contains certain affirmative and negative covenants, including but not limited to (i) maintaining minimum stockholders’ equity, (ii) maintaining a minimum asset coverage ratio, and (iii) maintaining the Company’s status as a regulated investment company and as a business development company. The February 2019 Credit Facility also contains customary events of default with customary cure and notice provisions, including, without limitation, nonpayment, material misrepresentation of representations and warranties, breach of covenant, cross-default to other indebtedness, bankruptcy, change of control, and material adverse effect. The February 2019 Credit Facility also permits the administrative agent to select an independent third-party valuation firm to determine valuations of certain portfolio investments for purposes of borrowing base provisions. As of June 30, 2026, the Company was in compliance with all covenants under the February 2019 Credit Facility. [S53]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Resolve the latest financial filing/CompanyFacts mismatch; any historical bootstrap must keep the latest-period gap explicit.
- Forms observed in the retained filing inventory: 10-K, 10-K/A, 10-Q, 144, 25, 25-NSE, 3, 3/A, 305B2, 4, 4/A, 40-17G, 40-33, 40-APP, 40-APP/A, 424B2, 424B3, 425, 497, 497AD, 5, 8-A12B, 8-K, 8-K/A, APP NTC, APP ORDR, CERTNYS, CORRESP, D, D/A, DEF 14A, DEFA14A, DEFM14A, DEFR14A, EFFECT, FWP, N-14 8C, N-14 8C/A, N-14MEF, N-2, N-2/A, N-23C-2, N-2ASR, POS 8C, POS EX, PRE 14A, PREM14A, PRER14A, S-8, S-8 POS, SC 13D, SC 13D/A, SC 13G, SC 13G/A, SC TO-I, SC TO-I/A, UPLOAD
- Collector status: quality_review_required; last action: filings_only_financials_incomplete; last checked: 2026-10-24T13:32:57.121339+00:00.

### Research work queue

Collection stage: **evidence_collected**. Extracted evidence is not a reviewed conclusion. Daily collection resumes from durable state; unchanged accessions are reused.

- **Business overview** (source excerpts available; assess the claim): Explain what the company does, who pays it, and why the business exists. Cite primary sources.
- **Revenue model and segments** (source excerpts available; assess the claim): Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.
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
| 2026-08-21 | 40-17G | 0001072613-26-000710 | — | [S03] |
| 2026-08-05 | 8-K | 0001379785-26-000031 | — | [S04] |
| 2026-08-05 | 10-Q | 0001379785-26-000030 | — | [S05] |
| 2026-06-05 | 4 | 0001225208-26-005818 | — | [S06] |
| 2026-06-01 | 8-K | 0001379785-26-000024 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-11-01T16:07:03.340031+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001379785.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [40-17G 0001072613-26-000710](https://www.sec.gov/Archives/edgar/data/1379785/000107261326000710/0001072613-26-000710-index.html) — published 2026-08-21; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [8-K 0001379785-26-000031](https://www.sec.gov/Archives/edgar/data/1379785/000137978526000031/0001379785-26-000031-index.html) — published 2026-08-05; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [10-Q 0001379785-26-000030](https://www.sec.gov/Archives/edgar/data/1379785/000137978526000030/0001379785-26-000030-index.html) — published 2026-08-05; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [4 0001225208-26-005818](https://www.sec.gov/Archives/edgar/data/1379785/000122520826005818/0001225208-26-005818-index.html) — published 2026-06-05; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [8-K 0001379785-26-000024](https://www.sec.gov/Archives/edgar/data/1379785/000137978526000024/0001379785-26-000024-index.html) — published 2026-06-01; retrieved 2026-10-23T08:33:02.691743+00:00.

[S53] [10-Q 0001379785-26-000030](https://www.sec.gov/Archives/edgar/data/1379785/000137978526000030/bbdc-20260630.htm) — published 2026-08-05; retrieved 2026-11-19T21:15:17.057332+00:00.

[S56] [10-K 0001379785-26-000009](https://www.sec.gov/Archives/edgar/data/1379785/000137978526000009/bbdc-20251231.htm) — published 2026-02-19; retrieved 2026-11-19T21:15:12.099770+00:00.

Source release: `coverage-20261101-41324509967-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/0f49b319f95dcee8e757e592a38a028a04a7bc3c/brain/companies/BBDC/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
