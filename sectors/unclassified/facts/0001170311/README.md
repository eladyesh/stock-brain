---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001170311
cik: '0001170311'
company_name: PIMCO NEW YORK MUNICIPAL INCOME FUND II
tickers:
- PNI
status: stub
canonical_reviewed: false
as_of: '2026-10-23'
updated_at: '2026-10-23T08:47:59.341415+00:00'
reviewed_at: null
coverage_release: coverage-20261023-39925380279-1
source_commit: 78606fb159189686ce54eb7bc0fa1098e51dc3ab
financial_history_available: false
curated_research: null
financial_gap:
  reason: fund_reporting_review
  next_action: Review the instrument against its N-CSR/N-CSRS reporting evidence before
    applying an operating-company model. This signal alone is not a final fund classification.
  observed_forms:
  - '3'
  - 3/A
  - '4'
  - 40-17G
  - 40-17G/A
  - 40-6C
  - 40-APP
  - 40-APP/A
  - 424B3
  - '497'
  - 8-A12B
  - 8-K
  - CERTNYS
  - CORRESP
  - DEF 14A
  - DEFA14A
  - DEFC14A
  - DFAN14A
  - EFFECT
  - N-14 8C
  - N-14 8C/A
  - N-2
  - N-2/A
  - N-23C-2
  - N-2MEF
  - N-30D
  - N-8A
  - N-CEN
  - N-CSR
  - N-CSR/A
  - N-CSRS
  - N-CSRS/A
  - N-PX
  - N-Q
  - N-Q/A
  - NPORT-EX
  - NPORT-P
  - NPORT-P/A
  - NSAR-A
  - NSAR-B
  - NSAR-B/A
  - NSAR-BT
  - NT-NCSR
  - NT-NSAR
  - POS EX
  - PRE 14A
  - PREC14A
  - PRER14A
  - PRRN14A
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SC TO-C
  - SC TO-I
  - SC TO-I/A
  - SCHEDULE 13D/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001170311.json
    sha256: 1cf53ea6d3d3f7ce10f82ed6adf73dc4c2fd13fc6f546fb3510a5be40541ea7e
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001170311.json
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
  url: https://data.sec.gov/submissions/CIK0001170311.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 1cf53ea6d3d3f7ce10f82ed6adf73dc4c2fd13fc6f546fb3510a5be40541ea7e
- id: S03
  title: N-23C-2 0001193125-26-391878
  url: https://www.sec.gov/Archives/edgar/data/1170311/000119312526391878/0001193125-26-391878-index.html
  published_at: '2026-09-15'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: NPORT-P/A 0001410368-26-091283
  url: https://www.sec.gov/Archives/edgar/data/1170311/000141036826091283/0001410368-26-091283-index.html
  published_at: '2026-09-11'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: N-CSRS 0001193125-26-382373
  url: https://www.sec.gov/Archives/edgar/data/1170311/000119312526382373/0001193125-26-382373-index.html
  published_at: '2026-09-04'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: NPORT-P 0001410368-26-090100
  url: https://www.sec.gov/Archives/edgar/data/1170311/000141036826090100/0001410368-26-090100-index.html
  published_at: '2026-08-31'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: N-PX 0001050269-26-000079
  url: https://www.sec.gov/Archives/edgar/data/1170311/000105026926000079/0001050269-26-000079-index.html
  published_at: '2026-08-27'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: '0001170311'
  classification_status: missing_or_invalid_sic
  entity_type: other
  name: PIMCO NEW YORK MUNICIPAL INCOME FUND II
  sic: null
  sic_description: ''
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 1cf53ea6d3d3f7ce10f82ed6adf73dc4c2fd13fc6f546fb3510a5be40541ea7e
  url: https://data.sec.gov/submissions/CIK0001170311.json
sector_assignment:
  sector: unclassified
  method: unresolved
  sic: null
  sic_description: ''
  rule_version: 1
  reason: Fund reporting signal requires instrument review before operating-sector
    classification.
full_history_url: https://github.com/eladyesh/stock-brain/blob/ffcaf17e05894e3d5a5cf6f414562c7c11a15184/brain/companies/0001170311/README.md
full_history_commit: ffcaf17e05894e3d5a5cf6f414562c7c11a15184
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# PIMCO NEW YORK MUNICIPAL INCOME FUND II — PNI

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/ffcaf17e05894e3d5a5cf6f414562c7c11a15184/brain/companies/0001170311/README.md)

## Business overview

Reported issuer name: **PIMCO NEW YORK MUNICIPAL INCOME FUND II**. Stable SEC CIK: **0001170311**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| PNI | NYSE | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

Not available: substantive research has not been completed. Place the company among suppliers, distribution channels, customers, and substitutes. Explain cyclicality and supply constraints.

Navigation sector: **unclassified**. Method: `unresolved`. Fund reporting signal requires instrument review before operating-sector classification.

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
- Next collection task: Review the instrument against its N-CSR/N-CSRS reporting evidence before applying an operating-company model. This signal alone is not a final fund classification.
- Forms observed in the retained filing inventory: 3, 3/A, 4, 40-17G, 40-17G/A, 40-6C, 40-APP, 40-APP/A, 424B3, 497, 8-A12B, 8-K, CERTNYS, CORRESP, DEF 14A, DEFA14A, DEFC14A, DFAN14A, EFFECT, N-14 8C, N-14 8C/A, N-2, N-2/A, N-23C-2, N-2MEF, N-30D, N-8A, N-CEN, N-CSR, N-CSR/A, N-CSRS, N-CSRS/A, N-PX, N-Q, N-Q/A, NPORT-EX, NPORT-P, NPORT-P/A, NSAR-A, NSAR-B, NSAR-B/A, NSAR-BT, NT-NCSR, NT-NSAR, POS EX, PRE 14A, PREC14A, PRER14A, PRRN14A, SC 13D, SC 13D/A, SC 13G, SC 13G/A, SC TO-C, SC TO-I, SC TO-I/A, SCHEDULE 13D/A, SCHEDULE 13G, SCHEDULE 13G/A
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-23T08:42:21.129446+00:00.

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest five available filing metadata records; document bodies have not been analyzed here.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-09-15 | N-23C-2 | 0001193125-26-391878 | — | [S03] |
| 2026-09-11 | NPORT-P/A | 0001410368-26-091283 | — | [S04] |
| 2026-09-04 | N-CSRS | 0001193125-26-382373 | — | [S05] |
| 2026-08-31 | NPORT-P | 0001410368-26-090100 | — | [S06] |
| 2026-08-27 | N-PX | 0001050269-26-000079 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-23T08:33:49.304929+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001170311.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [N-23C-2 0001193125-26-391878](https://www.sec.gov/Archives/edgar/data/1170311/000119312526391878/0001193125-26-391878-index.html) — published 2026-09-15; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [NPORT-P/A 0001410368-26-091283](https://www.sec.gov/Archives/edgar/data/1170311/000141036826091283/0001410368-26-091283-index.html) — published 2026-09-11; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [N-CSRS 0001193125-26-382373](https://www.sec.gov/Archives/edgar/data/1170311/000119312526382373/0001193125-26-382373-index.html) — published 2026-09-04; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [NPORT-P 0001410368-26-090100](https://www.sec.gov/Archives/edgar/data/1170311/000141036826090100/0001410368-26-090100-index.html) — published 2026-08-31; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [N-PX 0001050269-26-000079](https://www.sec.gov/Archives/edgar/data/1170311/000105026926000079/0001050269-26-000079-index.html) — published 2026-08-27; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261023-39925380279-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/ffcaf17e05894e3d5a5cf6f414562c7c11a15184/brain/companies/0001170311/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
