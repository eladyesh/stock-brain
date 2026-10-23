---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001341439
cik: 0001341439
company_name: ORACLE CORP
tickers:
- ORCL
- ORCL$D
status: stub
canonical_reviewed: false
as_of: '2026-10-23'
updated_at: '2026-10-23T08:47:59.341415+00:00'
reviewed_at: null
coverage_release: coverage-20261023-39925380279-1
source_commit: 78606fb159189686ce54eb7bc0fa1098e51dc3ab
financial_history_available: true
curated_research:
  url: https://github.com/eladyesh/stock-brain/blob/78606fb159189686ce54eb7bc0fa1098e51dc3ab/sectors/information-technology/companies/ORCL/README.md
  status: reviewed
  as_of: '2026-10-18'
  sector: information-technology
financial_gap:
  reason: available
  next_action: Retain dated financial evidence and review blocked metrics before analytical
    use.
  observed_forms:
  - 10-K
  - 10-Q
  - 11-K
  - '144'
  - 25-NSE
  - '3'
  - '4'
  - 4/A
  - 424B2
  - 424B5
  - 8-A12B
  - 8-K
  - 8-K/A
  - CERT
  - CORRESP
  - DEF 14A
  - DEFA14A
  - FWP
  - NO ACT
  - POSASR
  - PX14A6G
  - S-3ASR
  - S-8
  - S-8 POS
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SC TO-C
  - SC TO-T
  - SC TO-T/A
  - SCHEDULE 13G/A
  - SD
  - UPLOAD
input_sources:
  history:
    url: https://data.sec.gov/api/xbrl/companyfacts/CIK0001341439.json
    sha256: 65523545f040abaea1dfcf321da2a5aec85e7f34387244b0ffcb26e4c8707f7d
    retrieved_at: '2026-10-22T18:50:05.571155+00:00'
  submissions:
    url: https://data.sec.gov/submissions/CIK0001341439.json
    sha256: c41260def74f2052a1bfc9088a063688e772e5f1e4a7007ecb46c30312c84719
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001341439.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: otherlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt
  published_at: null
  retrieved_at: '2026-10-23T08:33:49.304929+00:00'
  sha256: 6b752ea8975cd8cfe39564769459d8cea3289453fb9454cc2eb02663466ddb67
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001341439.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: c41260def74f2052a1bfc9088a063688e772e5f1e4a7007ecb46c30312c84719
- id: S03
  title: SEC CompanyFacts source
  url: https://data.sec.gov/api/xbrl/companyfacts/CIK0001341439.json
  published_at: null
  retrieved_at: '2026-10-22T18:50:05.571155+00:00'
  sha256: 65523545f040abaea1dfcf321da2a5aec85e7f34387244b0ffcb26e4c8707f7d
- id: S04
  title: 10-K 0001193125-26-277521
  url: https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.html
  published_at: '2026-06-22'
  retrieved_at: '2026-10-22T18:50:05.571155+00:00'
  sha256: null
- id: S05
  title: 10-Q 0001193125-26-389274
  url: https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.html
  published_at: '2026-09-11'
  retrieved_at: '2026-10-22T18:50:05.571155+00:00'
  sha256: null
- id: S18
  title: 4 0001341439-26-000117
  url: https://www.sec.gov/Archives/edgar/data/1341439/000134143926000117/0001341439-26-000117-index.html
  published_at: '2026-10-19'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S19
  title: 4 0001341439-26-000116
  url: https://www.sec.gov/Archives/edgar/data/1341439/000134143926000116/0001341439-26-000116-index.html
  published_at: '2026-10-19'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S20
  title: 4 0001341439-26-000113
  url: https://www.sec.gov/Archives/edgar/data/1341439/000134143926000113/0001341439-26-000113-index.html
  published_at: '2026-10-19'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S21
  title: 4 0001341439-26-000111
  url: https://www.sec.gov/Archives/edgar/data/1341439/000134143926000111/0001341439-26-000111-index.html
  published_at: '2026-10-19'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S22
  title: 4 0001341439-26-000109
  url: https://www.sec.gov/Archives/edgar/data/1341439/000134143926000109/0001341439-26-000109-index.html
  published_at: '2026-10-19'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0001341439
  classification_status: reported_sic
  entity_type: operating
  name: ORACLE CORP
  sic: '7372'
  sic_description: Services-Prepackaged Software
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: c41260def74f2052a1bfc9088a063688e772e5f1e4a7007ecb46c30312c84719
  url: https://data.sec.gov/submissions/CIK0001341439.json
sector_assignment:
  sector: information-technology
  method: curated_profile
  sic: '7372'
  sic_description: Services-Prepackaged Software
  rule_version: 1
  reason: Uses the dated curated profile assignment; automatic data does not renew
    its review.
  source_url: https://github.com/eladyesh/stock-brain/blob/78606fb159189686ce54eb7bc0fa1098e51dc3ab/sectors/information-technology/companies/ORCL/README.md
full_history_url: https://github.com/eladyesh/stock-brain/blob/ffcaf17e05894e3d5a5cf6f414562c7c11a15184/brain/companies/0001341439/README.md
full_history_commit: ffcaf17e05894e3d5a5cf6f414562c7c11a15184
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# ORACLE CORP — ORCL, ORCL$D

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/ffcaf17e05894e3d5a5cf6f414562c7c11a15184/brain/companies/0001341439/README.md)

## Business overview

Reported issuer name: **ORACLE CORP**. Stable SEC CIK: **0001341439**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| ORCL | NYSE | common_stock | 1 | [S01] |
| ORCL$D | NYSE | preferred | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **7372**: Services-Prepackaged Software. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **information-technology**. Method: `curated_profile`. Uses the dated curated profile assignment; automatic data does not renew its review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

## Financial performance

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T18:50:05.571155+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-06-01 to 2026-05-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -55,663,000,000 | USD | US GAAP / reported | PaymentsToAcquirePropertyPlantAndEquipment; Cash outflow = negative of reported PaymentsToAcquirePropertyPlantAndEquipment; source value retained. | [S04] |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S04] |
| free_cash_flow | -23,686,000,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment | [S04] |
| gross_profit | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income | 17,087,000,000 | USD | US GAAP / reported | NetIncomeLoss | [S04] |
| net_income_common | 16,984,000,000 | USD | US GAAP / reported | NetIncomeLossAvailableToCommonStockholdersBasic | [S04] |
| net_income_including_noncontrolling_interests | 17,309,000,000 | USD | US GAAP / reported | ProfitLoss | [S04] |
| operating_cash_flow | 31,977,000,000 | USD | US GAAP / reported | NetCashProvidedByUsedInOperatingActivities | [S04] |
| operating_income | 20,606,000,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S04] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | 67,357,000,000 | USD | US GAAP / reported | RevenueFromContractWithCustomerExcludingAssessedTax | [S04] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S04] |
| stock_based_compensation | 4,811,000,000 | USD | US GAAP / reported | ShareBasedCompensation | [S04] |


### quarterly: 2026-06-01 to 2026-08-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | Unavailable / blocked | USD | US GAAP / reported / not model usable | PaymentsToAcquirePropertyPlantAndEquipment; Cash outflow = negative of reported PaymentsToAcquirePropertyPlantAndEquipment; source value retained.; conflicting_fiscal_year | [S05] |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; conflicting_fiscal_year | No eligible evidence |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; conflicting_fiscal_year, share_split_and_corporate_action_basis_unverified | [S05] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; conflicting_fiscal_year, share_split_and_corporate_action_basis_unverified | [S05] |
| free_cash_flow | Unavailable / blocked | USD | US GAAP / derived / not model usable | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment; conflicting_fiscal_year | [S05] |
| gross_profit | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; conflicting_fiscal_year | No eligible evidence |
| net_income | Unavailable / blocked | USD | US GAAP / reported / not model usable | NetIncomeLoss; conflicting_fiscal_year | [S05] |
| net_income_common | Unavailable / blocked | USD | US GAAP / reported / not model usable | NetIncomeLossAvailableToCommonStockholdersBasic; conflicting_fiscal_year | [S05] |
| net_income_including_noncontrolling_interests | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; conflicting_fiscal_year | No eligible evidence |
| operating_cash_flow | Unavailable / blocked | USD | US GAAP / reported / not model usable | NetCashProvidedByUsedInOperatingActivities; conflicting_fiscal_year | [S05] |
| operating_income | Unavailable / blocked | USD | US GAAP / reported / not model usable | OperatingIncomeLoss; conflicting_fiscal_year | [S05] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; conflicting_fiscal_year | No eligible evidence |
| revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | RevenueFromContractWithCustomerExcludingAssessedTax; conflicting_fiscal_year | [S05] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; conflicting_fiscal_year, share_split_and_corporate_action_basis_unverified | [S05] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; conflicting_fiscal_year, share_split_and_corporate_action_basis_unverified | [S05] |
| stock_based_compensation | Unavailable / blocked | USD | US GAAP / reported / not model usable | ShareBasedCompensation; conflicting_fiscal_year | [S05] |



## Balance sheet and capital allocation

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T18:50:05.571155+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-06-01 to 2026-05-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 31,289,000,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S05] |
| debt_current | Unavailable / blocked | USD | US GAAP / reported / not model usable | NotesPayableCurrent; debt_scope_requires_filing_review, definition_changed_across_series | [S05] |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermNotesPayable; debt_scope_requires_filing_review | [S04] |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S05] |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |


### quarterly: 2026-06-01 to 2026-08-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | Unavailable / blocked | USD | US GAAP / reported / not model usable | CashAndCashEquivalentsAtCarryingValue; conflicting_fiscal_year | [S05] |
| debt_current | Unavailable / blocked | USD | US GAAP / reported / not model usable | NotesPayableCurrent; conflicting_fiscal_year, debt_scope_requires_filing_review, definition_changed_across_series | [S05] |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; conflicting_fiscal_year | No eligible evidence |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; conflicting_fiscal_year | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; conflicting_fiscal_year | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; conflicting_fiscal_year, share_split_and_corporate_action_basis_unverified | [S05] |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; conflicting_fiscal_year | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; conflicting_fiscal_year | No eligible evidence |



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
- Collector status: quality_review_required; last action: new_financial_filing; last checked: 2026-10-23T08:43:01.795856+00:00.

Dated curated research is maintained separately: [profile at source commit](https://github.com/eladyesh/stock-brain/blob/78606fb159189686ce54eb7bc0fa1098e51dc3ab/sectors/information-technology/companies/ORCL/README.md) (status reviewed, as of 2026-10-18). Automatic facts never change its review date.

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest five available filing metadata records; document bodies have not been analyzed here.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-10-19 | 4 | 0001341439-26-000117 | — | [S18] |
| 2026-10-19 | 4 | 0001341439-26-000116 | — | [S19] |
| 2026-10-19 | 4 | 0001341439-26-000113 | — | [S20] |
| 2026-10-19 | 4 | 0001341439-26-000111 | — | [S21] |
| 2026-10-19 | 4 | 0001341439-26-000109 | — | [S22] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-23T08:33:49.304929+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001341439.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [SEC CompanyFacts source](https://data.sec.gov/api/xbrl/companyfacts/CIK0001341439.json) — published not supplied; retrieved 2026-10-22T18:50:05.571155+00:00.

[S04] [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.html) — published 2026-06-22; retrieved 2026-10-22T18:50:05.571155+00:00.

[S05] [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.html) — published 2026-09-11; retrieved 2026-10-22T18:50:05.571155+00:00.

[S18] [4 0001341439-26-000117](https://www.sec.gov/Archives/edgar/data/1341439/000134143926000117/0001341439-26-000117-index.html) — published 2026-10-19; retrieved 2026-10-23T08:33:02.691743+00:00.

[S19] [4 0001341439-26-000116](https://www.sec.gov/Archives/edgar/data/1341439/000134143926000116/0001341439-26-000116-index.html) — published 2026-10-19; retrieved 2026-10-23T08:33:02.691743+00:00.

[S20] [4 0001341439-26-000113](https://www.sec.gov/Archives/edgar/data/1341439/000134143926000113/0001341439-26-000113-index.html) — published 2026-10-19; retrieved 2026-10-23T08:33:02.691743+00:00.

[S21] [4 0001341439-26-000111](https://www.sec.gov/Archives/edgar/data/1341439/000134143926000111/0001341439-26-000111-index.html) — published 2026-10-19; retrieved 2026-10-23T08:33:02.691743+00:00.

[S22] [4 0001341439-26-000109](https://www.sec.gov/Archives/edgar/data/1341439/000134143926000109/0001341439-26-000109-index.html) — published 2026-10-19; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261023-39925380279-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/ffcaf17e05894e3d5a5cf6f414562c7c11a15184/brain/companies/0001341439/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
