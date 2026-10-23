---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001001085
cik: 0001001085
company_name: BROOKFIELD Corp /ON/
tickers:
- BN
status: stub
canonical_reviewed: false
as_of: '2026-10-23'
updated_at: '2026-10-23T14:35:22.252685+00:00'
reviewed_at: null
coverage_release: coverage-20261023-39968262770-1
source_commit: c5f247f1f77b31a20ec1a66533503255600926f7
financial_history_available: false
curated_research: null
financial_gap:
  reason: foreign_reporting_adapter
  next_action: Add support for the observed 20-F, 40-F or 6-K reporting forms and
    verify the actual accounting taxonomy before normalization.
  observed_forms:
  - 13F-HR
  - 13F-HR/A
  - '3'
  - 3/A
  - '4'
  - 4/A
  - 40-F
  - 40-F/A
  - 424B3
  - '425'
  - '5'
  - 6-K
  - 6-K/A
  - 8-A12B
  - 8-A12B/A
  - CERT
  - CORRESP
  - DFAN14A
  - EFFECT
  - F-1
  - F-1/A
  - F-10
  - F-10/A
  - F-3
  - F-3/A
  - F-4
  - F-4/A
  - F-X
  - FWP
  - N-PX
  - POS AM
  - S-8
  - SC 13D
  - SC 13D/A
  - SC 13E3
  - SC 13E3/A
  - SC 13G
  - SC 13G/A
  - SC TO-C
  - SC TO-I
  - SC TO-I/A
  - SC TO-T
  - SC TO-T/A
  - SCHEDULE 13D
  - SCHEDULE 13D/A
  - SUPPL
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001001085.json
    sha256: cbdc2ab235fa7072c1f45c2711ce3d635b55c66c90b9937b2a9eb99cbf2312e2
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001001085.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: otherlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt
  published_at: null
  retrieved_at: '2026-10-23T14:17:55.298415+00:00'
  sha256: be329650ef672c0314f0e16b2e41951f6af4ae314df9a04a32dc11ddb70b194e
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001001085.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: cbdc2ab235fa7072c1f45c2711ce3d635b55c66c90b9937b2a9eb99cbf2312e2
- id: S03
  title: 4 0001193125-26-428770
  url: https://www.sec.gov/Archives/edgar/data/1001085/000119312526428770/0001193125-26-428770-index.html
  published_at: '2026-10-22'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 6-K 0001104659-26-118154
  url: https://www.sec.gov/Archives/edgar/data/1001085/000110465926118154/0001104659-26-118154-index.html
  published_at: '2026-10-22'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 6-K 0001104659-26-116314
  url: https://www.sec.gov/Archives/edgar/data/1001085/000110465926116314/0001104659-26-116314-index.html
  published_at: '2026-10-16'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 6-K 0001171843-26-006563
  url: https://www.sec.gov/Archives/edgar/data/1001085/000117184326006563/0001171843-26-006563-index.html
  published_at: '2026-10-09'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 4 0001193125-26-412131
  url: https://www.sec.gov/Archives/edgar/data/1001085/000119312526412131/0001193125-26-412131-index.html
  published_at: '2026-10-02'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0001001085
  classification_status: reported_sic
  entity_type: other
  name: BROOKFIELD Corp /ON/
  sic: '6512'
  sic_description: Opeators of  Nonresidential Buildings
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: cbdc2ab235fa7072c1f45c2711ce3d635b55c66c90b9937b2a9eb99cbf2312e2
  url: https://data.sec.gov/submissions/CIK0001001085.json
sector_assignment:
  sector: real-estate
  method: project_sic_rule
  sic: '6512'
  sic_description: Opeators of  Nonresidential Buildings
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001001085.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/8929b40d1af134561afb621de3adca71dd9577ba/brain/companies/0001001085/README.md
full_history_commit: 8929b40d1af134561afb621de3adca71dd9577ba
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# BROOKFIELD Corp /ON/ — BN

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/8929b40d1af134561afb621de3adca71dd9577ba/brain/companies/0001001085/README.md)

## Business overview

Reported issuer name: **BROOKFIELD Corp /ON/**. Stable SEC CIK: **0001001085**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| BN | NYSE | equity_candidate | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **6512**: Opeators of  Nonresidential Buildings. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **real-estate**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

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
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 13F-HR, 13F-HR/A, 3, 3/A, 4, 4/A, 40-F, 40-F/A, 424B3, 425, 5, 6-K, 6-K/A, 8-A12B, 8-A12B/A, CERT, CORRESP, DFAN14A, EFFECT, F-1, F-1/A, F-10, F-10/A, F-3, F-3/A, F-4, F-4/A, F-X, FWP, N-PX, POS AM, S-8, SC 13D, SC 13D/A, SC 13E3, SC 13E3/A, SC 13G, SC 13G/A, SC TO-C, SC TO-I, SC TO-I/A, SC TO-T, SC TO-T/A, SCHEDULE 13D, SCHEDULE 13D/A, SUPPL, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-23T14:26:47.827016+00:00.

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest five available filing metadata records; document bodies have not been analyzed here.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-10-22 | 4 | 0001193125-26-428770 | — | [S03] |
| 2026-10-22 | 6-K | 0001104659-26-118154 | — | [S04] |
| 2026-10-16 | 6-K | 0001104659-26-116314 | — | [S05] |
| 2026-10-09 | 6-K | 0001171843-26-006563 | — | [S06] |
| 2026-10-02 | 4 | 0001193125-26-412131 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-23T14:17:55.298415+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001001085.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [4 0001193125-26-428770](https://www.sec.gov/Archives/edgar/data/1001085/000119312526428770/0001193125-26-428770-index.html) — published 2026-10-22; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [6-K 0001104659-26-118154](https://www.sec.gov/Archives/edgar/data/1001085/000110465926118154/0001104659-26-118154-index.html) — published 2026-10-22; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [6-K 0001104659-26-116314](https://www.sec.gov/Archives/edgar/data/1001085/000110465926116314/0001104659-26-116314-index.html) — published 2026-10-16; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [6-K 0001171843-26-006563](https://www.sec.gov/Archives/edgar/data/1001085/000117184326006563/0001171843-26-006563-index.html) — published 2026-10-09; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [4 0001193125-26-412131](https://www.sec.gov/Archives/edgar/data/1001085/000119312526412131/0001193125-26-412131-index.html) — published 2026-10-02; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261023-39968262770-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/8929b40d1af134561afb621de3adca71dd9577ba/brain/companies/0001001085/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
