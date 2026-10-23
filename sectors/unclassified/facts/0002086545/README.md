---
schema_version: 1
document_type: company_facts
company_id: company-cik-0002086545
cik: 0002086545
company_name: Art Technology Acquisition Corp.
tickers:
- ARTC
status: stub
canonical_reviewed: false
as_of: '2026-10-23'
updated_at: '2026-10-23T08:47:59.341415+00:00'
reviewed_at: null
coverage_release: coverage-20261023-39925380279-1
source_commit: 78606fb159189686ce54eb7bc0fa1098e51dc3ab
financial_history_available: true
curated_research: null
financial_gap:
  reason: available
  next_action: Retain dated financial evidence and review blocked metrics before analytical
    use.
  observed_forms:
  - 10-K
  - 10-Q
  - '3'
  - 424B4
  - 8-A12B
  - 8-K
  - CERT
  - DRS
  - EFFECT
  - S-1
  - S-1/A
  - SCHEDULE 13D
  - SCHEDULE 13G
input_sources:
  history:
    url: https://data.sec.gov/api/xbrl/companyfacts/CIK0002086545.json
    sha256: 0b0bb2c69713c3681face293fe03a7717cf5e6cba15bd07f074f837e67aa6c4e
    retrieved_at: '2026-10-22T17:39:41.848518+00:00'
    archive:
      member: CIK0002086545.json
      sha256: 7457a528288f1e3425cba6ffd7370c6c205845aba12761763aa5ae3683c0fdc2
      url: https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip
    acquisition: operator_supplied_sec_bulk_archive
  submissions:
    url: https://data.sec.gov/submissions/CIK0002086545.json
    sha256: 5f946d11cc8c30ee2b8385362d1c43452021082dd4b332f5cce24bf4c4be0973
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0002086545.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: nasdaqlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt
  published_at: null
  retrieved_at: '2026-10-23T08:33:47.264469+00:00'
  sha256: fad79ccb3b53d16a6ace32a9f72f13d4f6009c72a4f1a15821e46e6008e68e75
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0002086545.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 5f946d11cc8c30ee2b8385362d1c43452021082dd4b332f5cce24bf4c4be0973
- id: S03
  title: SEC CompanyFacts source
  url: https://data.sec.gov/api/xbrl/companyfacts/CIK0002086545.json
  published_at: null
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: 0b0bb2c69713c3681face293fe03a7717cf5e6cba15bd07f074f837e67aa6c4e
- id: S04
  title: 10-Q 0001213900-26-086724
  url: https://www.sec.gov/Archives/edgar/data/2086545/000121390026086724/0001213900-26-086724-index.html
  published_at: '2026-08-07'
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: null
- id: S06
  title: 10-Q 0001213900-26-086724
  url: https://www.sec.gov/Archives/edgar/data/2086545/000121390026086724/0001213900-26-086724-index.html
  published_at: '2026-08-07'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 3 0001213900-26-078041
  url: https://www.sec.gov/Archives/edgar/data/2086545/000121390026078041/0001213900-26-078041-index.html
  published_at: '2026-07-14'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S08
  title: SCHEDULE 13G 0002048251-26-003765
  url: https://www.sec.gov/Archives/edgar/data/2086545/000204825126003765/0002048251-26-003765-index.html
  published_at: '2026-05-15'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S09
  title: SCHEDULE 13G 0000919574-26-003194
  url: https://www.sec.gov/Archives/edgar/data/2086545/000091957426003194/0000919574-26-003194-index.html
  published_at: '2026-05-15'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S10
  title: SCHEDULE 13G 0001172661-26-001872
  url: https://www.sec.gov/Archives/edgar/data/2086545/000117266126001872/0001172661-26-001872-index.html
  published_at: '2026-05-14'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0002086545
  classification_status: reported_sic
  entity_type: operating
  name: Art Technology Acquisition Corp.
  sic: '6770'
  sic_description: Blank Checks
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 5f946d11cc8c30ee2b8385362d1c43452021082dd4b332f5cce24bf4c4be0973
  url: https://data.sec.gov/submissions/CIK0002086545.json
sector_assignment:
  sector: unclassified
  method: unresolved
  sic: '6770'
  sic_description: Blank Checks
  rule_version: 1
  reason: Missing, ambiguous or unmapped reported industry; company-specific review
    is required.
full_history_url: https://github.com/eladyesh/stock-brain/blob/ffcaf17e05894e3d5a5cf6f414562c7c11a15184/brain/companies/0002086545/README.md
full_history_commit: ffcaf17e05894e3d5a5cf6f414562c7c11a15184
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# Art Technology Acquisition Corp. — ARTC

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/ffcaf17e05894e3d5a5cf6f414562c7c11a15184/brain/companies/0002086545/README.md)

## Business overview

Reported issuer name: **Art Technology Acquisition Corp.**. Stable SEC CIK: **0002086545**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| ARTC | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **6770**: Blank Checks. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **unclassified**. Method: `unresolved`. Missing, ambiguous or unmapped reported industry; company-specific review is required.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

## Financial performance

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:39:41.848518+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| free_cash_flow | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| gross_profit | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| net_income | Unavailable / blocked | USD | US GAAP / reported / not model usable | NetIncomeLoss; missing_annual_anchor | [S04] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| net_income_including_noncontrolling_interests | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| operating_cash_flow | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| operating_income | Unavailable / blocked | USD | US GAAP / reported / not model usable | OperatingIncomeLoss; missing_annual_anchor | [S04] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| revenue | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| shares_basic | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| shares_diluted | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| stock_based_compensation | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |



## Balance sheet and capital allocation

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:39:41.848518+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | Unavailable / blocked | USD | US GAAP / reported / not model usable | CashAndCashEquivalentsAtCarryingValue; missing_annual_anchor | [S04] |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |



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
- Collector status: quality_review_required; last action: new_financial_filing; last checked: 2026-10-23T08:47:22.583772+00:00.

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest five available filing metadata records; document bodies have not been analyzed here.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-08-07 | 10-Q | 0001213900-26-086724 | — | [S06] |
| 2026-07-14 | 3 | 0001213900-26-078041 | — | [S07] |
| 2026-05-15 | SCHEDULE 13G | 0002048251-26-003765 | — | [S08] |
| 2026-05-15 | SCHEDULE 13G | 0000919574-26-003194 | — | [S09] |
| 2026-05-14 | SCHEDULE 13G | 0001172661-26-001872 | — | [S10] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-23T08:33:47.264469+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0002086545.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [SEC CompanyFacts source](https://data.sec.gov/api/xbrl/companyfacts/CIK0002086545.json) — published not supplied; retrieved 2026-10-22T17:39:41.848518+00:00.

[S04] [10-Q 0001213900-26-086724](https://www.sec.gov/Archives/edgar/data/2086545/000121390026086724/0001213900-26-086724-index.html) — published 2026-08-07; retrieved 2026-10-22T17:39:41.848518+00:00.

[S06] [10-Q 0001213900-26-086724](https://www.sec.gov/Archives/edgar/data/2086545/000121390026086724/0001213900-26-086724-index.html) — published 2026-08-07; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [3 0001213900-26-078041](https://www.sec.gov/Archives/edgar/data/2086545/000121390026078041/0001213900-26-078041-index.html) — published 2026-07-14; retrieved 2026-10-23T08:33:02.691743+00:00.

[S08] [SCHEDULE 13G 0002048251-26-003765](https://www.sec.gov/Archives/edgar/data/2086545/000204825126003765/0002048251-26-003765-index.html) — published 2026-05-15; retrieved 2026-10-23T08:33:02.691743+00:00.

[S09] [SCHEDULE 13G 0000919574-26-003194](https://www.sec.gov/Archives/edgar/data/2086545/000091957426003194/0000919574-26-003194-index.html) — published 2026-05-15; retrieved 2026-10-23T08:33:02.691743+00:00.

[S10] [SCHEDULE 13G 0001172661-26-001872](https://www.sec.gov/Archives/edgar/data/2086545/000117266126001872/0001172661-26-001872-index.html) — published 2026-05-14; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261023-39925380279-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/ffcaf17e05894e3d5a5cf6f414562c7c11a15184/brain/companies/0002086545/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
