---
schema_version: 1
document_type: company_facts
company_id: company-cik-0002089271
cik: 0002089271
company_name: Honeywell Aerospace Inc.
tickers:
- HONA
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
  - 10-12B
  - 10-12B/A
  - 10-Q
  - '3'
  - '4'
  - 424B3
  - 8-K
  - CERT
  - DRS
  - DRS/A
  - EFFECT
  - S-4
  - S-8
  - SCHEDULE 13G
  - SEC STAFF ACTION
input_sources:
  history:
    url: https://data.sec.gov/api/xbrl/companyfacts/CIK0002089271.json
    sha256: ec4ab25b4219f40e64811d5d2aded693e11085aaa66b6475971d8b20f947c12b
    retrieved_at: '2026-10-22T17:39:41.848518+00:00'
    archive:
      member: CIK0002089271.json
      sha256: 7457a528288f1e3425cba6ffd7370c6c205845aba12761763aa5ae3683c0fdc2
      url: https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip
    acquisition: operator_supplied_sec_bulk_archive
  submissions:
    url: https://data.sec.gov/submissions/CIK0002089271.json
    sha256: 4134dcd8318e38863694639c025c70d56dbb568cfc1d58301866830ce2ffd5b9
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0002089271.json
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
  url: https://data.sec.gov/submissions/CIK0002089271.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 4134dcd8318e38863694639c025c70d56dbb568cfc1d58301866830ce2ffd5b9
- id: S03
  title: SEC CompanyFacts source
  url: https://data.sec.gov/api/xbrl/companyfacts/CIK0002089271.json
  published_at: null
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: ec4ab25b4219f40e64811d5d2aded693e11085aaa66b6475971d8b20f947c12b
- id: S04
  title: 10-Q 0002089271-26-000021
  url: https://www.sec.gov/Archives/edgar/data/2089271/000208927126000021/0002089271-26-000021-index.html
  published_at: '2026-08-05'
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: null
- id: S05
  title: 4 0001628280-26-060444
  url: https://www.sec.gov/Archives/edgar/data/2089271/000162828026060444/0001628280-26-060444-index.html
  published_at: '2026-09-03'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 4 0001628280-26-054956
  url: https://www.sec.gov/Archives/edgar/data/2089271/000162828026054956/0001628280-26-054956-index.html
  published_at: '2026-08-07'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 10-Q 0002089271-26-000021
  url: https://www.sec.gov/Archives/edgar/data/2089271/000208927126000021/0002089271-26-000021-index.html
  published_at: '2026-08-05'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S08
  title: 8-K 0002089271-26-000020
  url: https://www.sec.gov/Archives/edgar/data/2089271/000208927126000020/0002089271-26-000020-index.html
  published_at: '2026-08-05'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S09
  title: 4 0001628280-26-053731
  url: https://www.sec.gov/Archives/edgar/data/2089271/000162828026053731/0001628280-26-053731-index.html
  published_at: '2026-08-05'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0002089271
  classification_status: reported_sic
  entity_type: operating
  name: Honeywell Aerospace Inc.
  sic: '3724'
  sic_description: Aircraft Engines & Engine Parts
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 4134dcd8318e38863694639c025c70d56dbb568cfc1d58301866830ce2ffd5b9
  url: https://data.sec.gov/submissions/CIK0002089271.json
sector_assignment:
  sector: industrials
  method: project_sic_rule
  sic: '3724'
  sic_description: Aircraft Engines & Engine Parts
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0002089271.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/ffcaf17e05894e3d5a5cf6f414562c7c11a15184/brain/companies/0002089271/README.md
full_history_commit: ffcaf17e05894e3d5a5cf6f414562c7c11a15184
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# Honeywell Aerospace Inc. — HONA

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/ffcaf17e05894e3d5a5cf6f414562c7c11a15184/brain/companies/0002089271/README.md)

## Business overview

Reported issuer name: **Honeywell Aerospace Inc.**. Stable SEC CIK: **0002089271**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| HONA | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **3724**: Aircraft Engines & Engine Parts. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **industrials**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

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

### quarterly: 2026-03-29 to 2026-06-27

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | CostOfGoodsAndServicesSold; missing_annual_anchor | [S04] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| free_cash_flow | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| gross_profit | Unavailable / blocked | USD | US GAAP / derived / not model usable | CostOfGoodsAndServicesSold + RevenueFromContractWithCustomerExcludingAssessedTax; missing_annual_anchor | [S04] |
| net_income | Unavailable / blocked | USD | US GAAP / reported / not model usable | NetIncomeLoss; missing_annual_anchor | [S04] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| net_income_including_noncontrolling_interests | Unavailable / blocked | USD | US GAAP / reported / not model usable | ProfitLoss; missing_annual_anchor | [S04] |
| operating_cash_flow | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| operating_income | Unavailable / blocked | USD | US GAAP / reported / not model usable | OperatingIncomeLoss; missing_annual_anchor | [S04] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | RevenueFromContractWithCustomerExcludingAssessedTax; missing_annual_anchor | [S04] |
| shares_basic | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| shares_diluted | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| stock_based_compensation | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |

## Balance sheet and capital allocation

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:39:41.848518+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### quarterly: 2026-03-29 to 2026-06-27

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | Unavailable / blocked | USD | US GAAP / reported / not model usable | CashAndCashEquivalentsAtCarryingValue; missing_annual_anchor | [S04] |
| debt_current | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtCurrent; debt_scope_requires_filing_review, missing_annual_anchor | [S04] |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtNoncurrent; debt_scope_requires_filing_review, missing_annual_anchor | [S04] |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebt; debt_scope_requires_filing_review, missing_annual_anchor | [S04] |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |

Not available: reviewed debt maturity, acquisition, dividend and repurchase analysis.

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
- Collector status: quality_review_required; last action: new_financial_filing; last checked: 2026-10-23T08:47:22.866334+00:00.

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest five available filing metadata records; document bodies have not been analyzed here.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-09-03 | 4 | 0001628280-26-060444 | — | [S05] |
| 2026-08-07 | 4 | 0001628280-26-054956 | — | [S06] |
| 2026-08-05 | 10-Q | 0002089271-26-000021 | — | [S07] |
| 2026-08-05 | 8-K | 0002089271-26-000020 | — | [S08] |
| 2026-08-05 | 4 | 0001628280-26-053731 | — | [S09] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-23T08:33:47.264469+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0002089271.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [SEC CompanyFacts source](https://data.sec.gov/api/xbrl/companyfacts/CIK0002089271.json) — published not supplied; retrieved 2026-10-22T17:39:41.848518+00:00.

[S04] [10-Q 0002089271-26-000021](https://www.sec.gov/Archives/edgar/data/2089271/000208927126000021/0002089271-26-000021-index.html) — published 2026-08-05; retrieved 2026-10-22T17:39:41.848518+00:00.

[S05] [4 0001628280-26-060444](https://www.sec.gov/Archives/edgar/data/2089271/000162828026060444/0001628280-26-060444-index.html) — published 2026-09-03; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [4 0001628280-26-054956](https://www.sec.gov/Archives/edgar/data/2089271/000162828026054956/0001628280-26-054956-index.html) — published 2026-08-07; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [10-Q 0002089271-26-000021](https://www.sec.gov/Archives/edgar/data/2089271/000208927126000021/0002089271-26-000021-index.html) — published 2026-08-05; retrieved 2026-10-23T08:33:02.691743+00:00.

[S08] [8-K 0002089271-26-000020](https://www.sec.gov/Archives/edgar/data/2089271/000208927126000020/0002089271-26-000020-index.html) — published 2026-08-05; retrieved 2026-10-23T08:33:02.691743+00:00.

[S09] [4 0001628280-26-053731](https://www.sec.gov/Archives/edgar/data/2089271/000162828026053731/0001628280-26-053731-index.html) — published 2026-08-05; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261023-39925380279-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/ffcaf17e05894e3d5a5cf6f414562c7c11a15184/brain/companies/0002089271/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
