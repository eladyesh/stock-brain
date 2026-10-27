---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001951089
cik: 0001951089
company_name: Critical Metals Corp.
tickers:
- CRML
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
  - 424B3
  - '425'
  - 6-K
  - 6-K/A
  - 8-A12B
  - CERT
  - CORRESP
  - D
  - EFFECT
  - F-1
  - F-1/A
  - F-3
  - F-3/A
  - F-4
  - F-4/A
  - POS AM
  - S-8
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SCHEDULE 13D
  - SCHEDULE 13D/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001951089.json
    sha256: b813658ff2ac398302442487af6327122604dc730da4777b3f9ceffd6bd718be
    retrieved_at: '2026-10-24T13:22:51.759433+00:00'
    archive: &id001
      member: CIK0001951089.json
      sha256: 593fbbea6512ef5ec729a5e513c465fbedaac8a66602c0abe00d0ba5a4d18732
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: nasdaqlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt
  published_at: null
  retrieved_at: '2026-10-27T15:25:33.739265+00:00'
  sha256: 29c7cedde394d9fb806c731f8be32ec8c78cad2668852342db80ae28619465f0
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001951089.json
  published_at: null
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: b813658ff2ac398302442487af6327122604dc730da4777b3f9ceffd6bd718be
- id: S03
  title: 6-K 0001213900-26-111777
  url: https://www.sec.gov/Archives/edgar/data/1951089/000121390026111777/0001213900-26-111777-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S04
  title: F-3 0001213900-26-111485
  url: https://www.sec.gov/Archives/edgar/data/1951089/000121390026111485/0001213900-26-111485-index.html
  published_at: '2026-10-22'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S05
  title: 6-K 0001213900-26-111477
  url: https://www.sec.gov/Archives/edgar/data/1951089/000121390026111477/0001213900-26-111477-index.html
  published_at: '2026-10-22'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S06
  title: 6-K 0001213900-26-111467
  url: https://www.sec.gov/Archives/edgar/data/1951089/000121390026111467/0001213900-26-111467-index.html
  published_at: '2026-10-22'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S07
  title: 6-K 0001213900-26-106323
  url: https://www.sec.gov/Archives/edgar/data/1951089/000121390026106323/0001213900-26-106323-index.html
  published_at: '2026-10-02'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S53
  url: https://www.sec.gov/Archives/edgar/data/1951089/000121390026111777/ea0309427-6k_critical.htm
  title: 6-K 0001213900-26-111777
  published_at: '2026-10-23'
  retrieved_at: '2026-10-26T16:24:00.300636+00:00'
  sha256: 2d875a86e2e8447db6f0a642d0b1222b3181e2d11698d72ee26f154ce7cac18f
- id: S54
  url: https://www.sec.gov/Archives/edgar/data/1951089/000121390026103607/ea0302128-20f_critical.htm
  title: 20-F 0001213900-26-103607
  published_at: '2026-09-25'
  retrieved_at: '2026-10-26T16:23:58.500225+00:00'
  sha256: 30cfcd376a2770f65aa4461385868cd6757ba4e029320777f016e86068d2949d
issuer_classification:
  cik: 0001951089
  classification_status: reported_sic
  entity_type: other
  name: Critical Metals Corp.
  sic: '1000'
  sic_description: Metal Mining
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: b813658ff2ac398302442487af6327122604dc730da4777b3f9ceffd6bd718be
  url: https://data.sec.gov/submissions/CIK0001951089.json
listings:
- ticker: CRML
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001213900-26-103607
  filed: '2026-09-25'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1951089/000121390026103607/0001213900-26-103607-index.html
- accession: 0001213900-26-059770
  filed: '2026-05-21'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1951089/000121390026059770/0001213900-26-059770-index.html
- accession: 0001213900-25-098919
  filed: '2025-10-15'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1951089/000121390025098919/0001213900-25-098919-index.html
- accession: 0001213900-25-096245
  filed: '2025-10-06'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1951089/000121390025096245/0001213900-25-096245-index.html
- accession: 0001213900-26-111777
  filed: '2026-10-23'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1951089/000121390026111777/0001213900-26-111777-index.html
- accession: 0001213900-26-056690
  filed: '2026-05-14'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1951089/000121390026056690/0001213900-26-056690-index.html
- accession: 0001213900-25-096252
  filed: '2025-10-06'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1951089/000121390025096252/0001213900-25-096252-index.html
- accession: 0001213900-25-025156
  filed: '2025-03-19'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1951089/000121390025025156/0001213900-25-025156-index.html
research_progress:
  stage: evidence_collected
  input_sha256: eebaddd2df698f3d0858b7f2475711f426583930fb41876eec249cfb0cadca7a
  last_attempt_at: '2026-10-26T16:22:31.694168+00:00'
  last_success_at: '2026-10-26T16:22:31.694168+00:00'
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
  sector: materials
  method: project_sic_rule
  sic: '1000'
  sic_description: Metal Mining
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001951089.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/ea9dd09e5d047ff0620d4500849876915bb10e87/brain/companies/CRML/README.md
full_history_commit: ea9dd09e5d047ff0620d4500849876915bb10e87
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# CRML — Critical Metals Corp.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/ea9dd09e5d047ff0620d4500849876915bb10e87/brain/companies/CRML/README.md)

## Business overview

Reported issuer name: **Critical Metals Corp.**. Stable SEC CIK: **0001951089**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| CRML | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 20-F, filed 2026-09-25, L156:

> Except where the context otherwise requires or where otherwise indicated in this annual report (this “Annual Report”), the terms “Critical Metals,” the “Company,” “we,” “us,” “our,” “our company” and “our business” refer to the businesses of Critical Metals Corp., together with its consolidated subsidiaries as a consolidated entity. [S54]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 20-F, filed 2026-09-25, L3128:

> Accordingly, the Group has only one reportable segment and the results are the same as the Group results. [S54]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 20-F, filed 2026-09-25, L297:

> We anticipate that in some cases our products will be delivered to certain customers on an early trial deployment basis, where such customers have the ability to evaluate whether our products meet their performance requirements before they commit to meaningful orders. If our targeted customers do not commit to make meaningful orders, or at all, it could adversely affect our business, prospects and results of operations. Our customers may require protections in the form of price reductions and similar arrangements that allow them to require us to deliver additional product or reimburse them for losses they suffer as a result of our late delivery or failure to meet agreed upon performance specification. Delays in delivery of our products, unexpected performance problems or other events could cause us to fail to meet these contractual commitments, resulting in delays in obtaining necessary materials used in our production process, defects in material or workmanship or unexpected problems in our manufacturing process, which could lead to unanticipated revenue and earnings losses and financial penalties. The occurrence of any of these events could harm our business, prospects, results of operations and financial results. [S54]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 20-F, filed 2026-09-25, L297:

> We anticipate that in some cases our products will be delivered to certain customers on an early trial deployment basis, where such customers have the ability to evaluate whether our products meet their performance requirements before they commit to meaningful orders. If our targeted customers do not commit to make meaningful orders, or at all, it could adversely affect our business, prospects and results of operations. Our customers may require protections in the form of price reductions and similar arrangements that allow them to require us to deliver additional product or reimburse them for losses they suffer as a result of our late delivery or failure to meet agreed upon performance specification. Delays in delivery of our products, unexpected performance problems or other events could cause us to fail to meet these contractual commitments, resulting in delays in obtaining necessary materials used in our production process, defects in material or workmanship or unexpected problems in our manufacturing process, which could lead to unanticipated revenue and earnings losses and financial penalties. The occurrence of any of these events could harm our business, prospects, results of operations and financial results. [S54]

## Industry and value chain

SEC-reported SIC **1000**: Metal Mining. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 20-F, filed 2026-09-25, L199:

> \| \| ● \| We intend to seek to raise funds through equity or debt financing transactions, and we may also pursue joint ventures, production sharing arrangements or other transactions. We may also pursue grants or facilities under the Defense Production Act, as well as financing opportunities from the U.S Export-Import Bank (“U.S. Ex-Im”), which includes but is not limited to loans in direct support of the recently created Supply Chain Resiliency Initiative and/or under the Make More in America rubric, and the European Investment Bank, among other means. Any inability to raise additional capital may limit our ability to fund our ongoing operations, execute our business plan or pursue investments that we may rely on for future growth. [S54]

Navigation sector: **materials**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 20-F, filed 2026-09-25, L172:

> \| \| ● \| competition in the mining industry, including risks associated with pricing pressures from and loss of market share to competitors with greater resources than we have and increasing competition as a result of consolidation in the industry; [S54]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 20-F, filed 2026-09-25, L420:

> If our information or cyber security systems or data are compromised in a material way, our ability to conduct our business may be impaired, we may lose profitable opportunities or the value of those opportunities may be diminished and, as described above, we may lose revenue as a result of unlicensed use of our intellectual property. If personal information of our customers or employees is misappropriated, our reputation with our customers and employees may be damaged, resulting in loss of business or morale, and we may incur costs to remediate possible harm to our customers and employees or damages arising from litigation and/or to pay fines or take other action with respect to judicial or regulatory actions arising out of the incident. Insurance we obtain may not cover losses or damages associated with such attacks or events. [S54]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 20-F, filed 2026-09-25, L165:

> This Annual Report contains estimates and forward-looking statements, principally in the sections entitled Item 3.D. “Key Information-Risk Factors,” Item 4. “Information on the Company,” and Item 5. “Operating and Financial Review and Prospects.” In some cases, these forward-looking statements can be identified by words or phrases such as “may,” “might,” “will,” “could,” “would,” “should,” “expect,” “plan,” “anticipate,” “intend,” “seek,” “believe,” “estimate,” “predict,” “potential,” “continue,” “contemplate,” “possible” or similar words. Statements regarding our future results of operations and financial position, growth strategy and plans and objectives of management for future operations, including, among others, expansion in new and existing markets, are forward-looking statements. [S54]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 20-F, filed 2026-09-25, L64:

> Indicate by check mark whether any of those error corrections are restatements that required a recovery analysis of incentive-based compensation received by any of the registrant’s executive officers during the relevant recovery period pursuant to §240.10D-1(b). ☐ [S54]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 6-K, filed 2026-10-23, L57:

> statements for many reasons, including the factors discussed under the “Risk Factors” section in the Company’s Annual [S53]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 144, 20-F, 20-F/A, 3, 4, 424B3, 425, 6-K, 6-K/A, 8-A12B, CERT, CORRESP, D, EFFECT, F-1, F-1/A, F-3, F-3/A, F-4, F-4/A, POS AM, S-8, SC 13D, SC 13D/A, SC 13G, SCHEDULE 13D, SCHEDULE 13D/A, SCHEDULE 13G, SCHEDULE 13G/A, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:36:25.949716+00:00.

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
| 2026-10-23 | 6-K | 0001213900-26-111777 | — | [S03] |
| 2026-10-22 | F-3 | 0001213900-26-111485 | — | [S04] |
| 2026-10-22 | 6-K | 0001213900-26-111477 | — | [S05] |
| 2026-10-22 | 6-K | 0001213900-26-111467 | — | [S06] |
| 2026-10-02 | 6-K | 0001213900-26-106323 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-27T15:25:33.739265+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001951089.json) — published not supplied; retrieved 2026-10-24T13:22:51.759433+00:00.

[S03] [6-K 0001213900-26-111777](https://www.sec.gov/Archives/edgar/data/1951089/000121390026111777/0001213900-26-111777-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S04] [F-3 0001213900-26-111485](https://www.sec.gov/Archives/edgar/data/1951089/000121390026111485/0001213900-26-111485-index.html) — published 2026-10-22; retrieved 2026-10-24T13:22:51.759433+00:00.

[S05] [6-K 0001213900-26-111477](https://www.sec.gov/Archives/edgar/data/1951089/000121390026111477/0001213900-26-111477-index.html) — published 2026-10-22; retrieved 2026-10-24T13:22:51.759433+00:00.

[S06] [6-K 0001213900-26-111467](https://www.sec.gov/Archives/edgar/data/1951089/000121390026111467/0001213900-26-111467-index.html) — published 2026-10-22; retrieved 2026-10-24T13:22:51.759433+00:00.

[S07] [6-K 0001213900-26-106323](https://www.sec.gov/Archives/edgar/data/1951089/000121390026106323/0001213900-26-106323-index.html) — published 2026-10-02; retrieved 2026-10-24T13:22:51.759433+00:00.

[S53] [6-K 0001213900-26-111777](https://www.sec.gov/Archives/edgar/data/1951089/000121390026111777/ea0309427-6k_critical.htm) — published 2026-10-23; retrieved 2026-10-26T16:24:00.300636+00:00.

[S54] [20-F 0001213900-26-103607](https://www.sec.gov/Archives/edgar/data/1951089/000121390026103607/ea0302128-20f_critical.htm) — published 2026-09-25; retrieved 2026-10-26T16:23:58.500225+00:00.

Source release: `coverage-20261027-40530587641-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/ea9dd09e5d047ff0620d4500849876915bb10e87/brain/companies/CRML/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
