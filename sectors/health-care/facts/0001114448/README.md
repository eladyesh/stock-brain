---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001114448
cik: 0001114448
company_name: NOVARTIS AG
tickers:
- NVS
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
  reason: foreign_reporting_adapter
  next_action: Add support for the observed 20-F, 40-F or 6-K reporting forms and
    verify the actual accounting taxonomy before normalization.
  observed_forms:
  - '144'
  - 20-F
  - 20-F/A
  - '3'
  - 3/A
  - '4'
  - 4/A
  - 424B3
  - 424B5
  - '425'
  - '5'
  - 6-K
  - 6-K/A
  - CORRESP
  - CT ORDER
  - DFAN14A
  - EFFECT
  - F-3ASR
  - F-4
  - F-4/A
  - F-6 POS
  - F-6EF
  - FWP
  - IRANNOTICE
  - POSASR
  - S-8
  - S-8 POS
  - SC 13D
  - SC 13D/A
  - SC 13E3
  - SC 13E3/A
  - SC 13G
  - SC 13G/A
  - SC TO-C
  - SC TO-T
  - SC TO-T/A
  - SCHEDULE 13G
  - SD
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001114448.json
    sha256: 2028f5dcea889a345e54cc9036938ffb501cb5d626c79604a4e10ef3332efb76
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001114448.json
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
  url: https://data.sec.gov/submissions/CIK0001114448.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 2028f5dcea889a345e54cc9036938ffb501cb5d626c79604a4e10ef3332efb76
- id: S03
  title: 6-K 0001171843-26-005908
  url: https://www.sec.gov/Archives/edgar/data/1114448/000117184326005908/0001171843-26-005908-index.html
  published_at: '2026-09-08'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 6-K 0001171843-26-005896
  url: https://www.sec.gov/Archives/edgar/data/1114448/000117184326005896/0001171843-26-005896-index.html
  published_at: '2026-09-04'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 6-K 0001171843-26-005824
  url: https://www.sec.gov/Archives/edgar/data/1114448/000117184326005824/0001171843-26-005824-index.html
  published_at: '2026-09-01'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 6-K 0001114448-26-000012
  url: https://www.sec.gov/Archives/edgar/data/1114448/000111444826000012/0001114448-26-000012-index.html
  published_at: '2026-07-21'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 6-K 0001171843-26-004052
  url: https://www.sec.gov/Archives/edgar/data/1114448/000117184326004052/0001171843-26-004052-index.html
  published_at: '2026-06-11'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0001114448
  classification_status: reported_sic
  entity_type: other
  name: NOVARTIS AG
  sic: '2834'
  sic_description: Pharmaceutical Preparations
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 2028f5dcea889a345e54cc9036938ffb501cb5d626c79604a4e10ef3332efb76
  url: https://data.sec.gov/submissions/CIK0001114448.json
sector_assignment:
  sector: health-care
  method: project_sic_rule
  sic: '2834'
  sic_description: Pharmaceutical Preparations
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001114448.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/ffcaf17e05894e3d5a5cf6f414562c7c11a15184/brain/companies/0001114448/README.md
full_history_commit: ffcaf17e05894e3d5a5cf6f414562c7c11a15184
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# NOVARTIS AG — NVS

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/ffcaf17e05894e3d5a5cf6f414562c7c11a15184/brain/companies/0001114448/README.md)

## Business overview

Reported issuer name: **NOVARTIS AG**. Stable SEC CIK: **0001114448**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| NVS | NYSE | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **2834**: Pharmaceutical Preparations. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **health-care**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

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
- Forms observed in the retained filing inventory: 144, 20-F, 20-F/A, 3, 3/A, 4, 4/A, 424B3, 424B5, 425, 5, 6-K, 6-K/A, CORRESP, CT ORDER, DFAN14A, EFFECT, F-3ASR, F-4, F-4/A, F-6 POS, F-6EF, FWP, IRANNOTICE, POSASR, S-8, S-8 POS, SC 13D, SC 13D/A, SC 13E3, SC 13E3/A, SC 13G, SC 13G/A, SC TO-C, SC TO-T, SC TO-T/A, SCHEDULE 13G, SD, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-23T08:42:01.277005+00:00.

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest five available filing metadata records; document bodies have not been analyzed here.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-09-08 | 6-K | 0001171843-26-005908 | — | [S03] |
| 2026-09-04 | 6-K | 0001171843-26-005896 | — | [S04] |
| 2026-09-01 | 6-K | 0001171843-26-005824 | — | [S05] |
| 2026-07-21 | 6-K | 0001114448-26-000012 | — | [S06] |
| 2026-06-11 | 6-K | 0001171843-26-004052 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-23T08:33:49.304929+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001114448.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [6-K 0001171843-26-005908](https://www.sec.gov/Archives/edgar/data/1114448/000117184326005908/0001171843-26-005908-index.html) — published 2026-09-08; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [6-K 0001171843-26-005896](https://www.sec.gov/Archives/edgar/data/1114448/000117184326005896/0001171843-26-005896-index.html) — published 2026-09-04; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [6-K 0001171843-26-005824](https://www.sec.gov/Archives/edgar/data/1114448/000117184326005824/0001171843-26-005824-index.html) — published 2026-09-01; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [6-K 0001114448-26-000012](https://www.sec.gov/Archives/edgar/data/1114448/000111444826000012/0001114448-26-000012-index.html) — published 2026-07-21; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [6-K 0001171843-26-004052](https://www.sec.gov/Archives/edgar/data/1114448/000117184326004052/0001171843-26-004052-index.html) — published 2026-06-11; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261023-39925380279-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/ffcaf17e05894e3d5a5cf6f414562c7c11a15184/brain/companies/0001114448/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
