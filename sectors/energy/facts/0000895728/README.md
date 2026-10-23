---
schema_version: 1
document_type: company_facts
company_id: company-cik-0000895728
cik: 0000895728
company_name: ENBRIDGE INC
tickers:
- ENB
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
  reason: latest_filing_incomplete
  next_action: Resolve the latest financial filing/CompanyFacts mismatch; any historical
    bootstrap must keep the latest-period gap explicit.
  observed_forms:
  - 10-K
  - 10-K/A
  - 10-Q
  - 11-K
  - 11-K/A
  - '144'
  - 15-12B
  - 25-NSE
  - '3'
  - 3/A
  - '4'
  - 4/A
  - 40-F
  - 40-F/A
  - 424B2
  - 424B3
  - 424B5
  - '425'
  - '5'
  - 6-K
  - 6-K/A
  - 8-A12B
  - 8-K
  - 8-K/A
  - ARS
  - CB
  - CB/A
  - CERT
  - CORRESP
  - D
  - DEF 14A
  - DEFA14A
  - EFFECT
  - F-10
  - F-3
  - F-3/A
  - F-4
  - F-4/A
  - F-X
  - FWP
  - S-3ASR
  - S-3D
  - S-4
  - S-4/A
  - S-8
  - S-8 POS
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - SD
  - SUPPL
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0000895728.json
    sha256: 38136ee77e4b99adde85e7a1fce6d1d18e20e2f8d9d3e2f1bb223bc13dc3c8db
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0000895728.json
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
  url: https://data.sec.gov/submissions/CIK0000895728.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 38136ee77e4b99adde85e7a1fce6d1d18e20e2f8d9d3e2f1bb223bc13dc3c8db
- id: S03
  title: SD 0001193125-26-398771
  url: https://www.sec.gov/Archives/edgar/data/895728/000119312526398771/0001193125-26-398771-index.html
  published_at: '2026-09-23'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 8-K 0001104659-26-107292
  url: https://www.sec.gov/Archives/edgar/data/895728/000110465926107292/0001104659-26-107292-index.html
  published_at: '2026-09-14'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 424B5 0001104659-26-106571
  url: https://www.sec.gov/Archives/edgar/data/895728/000110465926106571/0001104659-26-106571-index.html
  published_at: '2026-09-10'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: FWP 0001104659-26-106430
  url: https://www.sec.gov/Archives/edgar/data/895728/000110465926106430/0001104659-26-106430-index.html
  published_at: '2026-09-10'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 8-K 0001104659-26-106404
  url: https://www.sec.gov/Archives/edgar/data/895728/000110465926106404/0001104659-26-106404-index.html
  published_at: '2026-09-09'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0000895728
  classification_status: reported_sic
  entity_type: operating
  name: ENBRIDGE INC
  sic: '4610'
  sic_description: Pipe Lines (No Natural Gas)
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 38136ee77e4b99adde85e7a1fce6d1d18e20e2f8d9d3e2f1bb223bc13dc3c8db
  url: https://data.sec.gov/submissions/CIK0000895728.json
sector_assignment:
  sector: energy
  method: project_sic_rule
  sic: '4610'
  sic_description: Pipe Lines (No Natural Gas)
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0000895728.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/ffcaf17e05894e3d5a5cf6f414562c7c11a15184/brain/companies/0000895728/README.md
full_history_commit: ffcaf17e05894e3d5a5cf6f414562c7c11a15184
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# ENBRIDGE INC — ENB

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/ffcaf17e05894e3d5a5cf6f414562c7c11a15184/brain/companies/0000895728/README.md)

## Business overview

Reported issuer name: **ENBRIDGE INC**. Stable SEC CIK: **0000895728**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| ENB | NYSE | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **4610**: Pipe Lines (No Natural Gas). [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **energy**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

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
- Next collection task: Resolve the latest financial filing/CompanyFacts mismatch; any historical bootstrap must keep the latest-period gap explicit.
- Forms observed in the retained filing inventory: 10-K, 10-K/A, 10-Q, 11-K, 11-K/A, 144, 15-12B, 25-NSE, 3, 3/A, 4, 4/A, 40-F, 40-F/A, 424B2, 424B3, 424B5, 425, 5, 6-K, 6-K/A, 8-A12B, 8-K, 8-K/A, ARS, CB, CB/A, CERT, CORRESP, D, DEF 14A, DEFA14A, EFFECT, F-10, F-3, F-3/A, F-4, F-4/A, F-X, FWP, S-3ASR, S-3D, S-4, S-4/A, S-8, S-8 POS, SC 13D, SC 13D/A, SC 13G, SC 13G/A, SCHEDULE 13G, SCHEDULE 13G/A, SD, SUPPL, UPLOAD
- Collector status: quality_review_required; last action: filings_only_financials_incomplete; last checked: 2026-10-23T08:40:26.163199+00:00.

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest five available filing metadata records; document bodies have not been analyzed here.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-09-23 | SD | 0001193125-26-398771 | — | [S03] |
| 2026-09-14 | 8-K | 0001104659-26-107292 | — | [S04] |
| 2026-09-10 | 424B5 | 0001104659-26-106571 | — | [S05] |
| 2026-09-10 | FWP | 0001104659-26-106430 | — | [S06] |
| 2026-09-09 | 8-K | 0001104659-26-106404 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-23T08:33:49.304929+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0000895728.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [SD 0001193125-26-398771](https://www.sec.gov/Archives/edgar/data/895728/000119312526398771/0001193125-26-398771-index.html) — published 2026-09-23; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [8-K 0001104659-26-107292](https://www.sec.gov/Archives/edgar/data/895728/000110465926107292/0001104659-26-107292-index.html) — published 2026-09-14; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [424B5 0001104659-26-106571](https://www.sec.gov/Archives/edgar/data/895728/000110465926106571/0001104659-26-106571-index.html) — published 2026-09-10; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [FWP 0001104659-26-106430](https://www.sec.gov/Archives/edgar/data/895728/000110465926106430/0001104659-26-106430-index.html) — published 2026-09-10; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [8-K 0001104659-26-106404](https://www.sec.gov/Archives/edgar/data/895728/000110465926106404/0001104659-26-106404-index.html) — published 2026-09-09; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261023-39925380279-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/ffcaf17e05894e3d5a5cf6f414562c7c11a15184/brain/companies/0000895728/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
