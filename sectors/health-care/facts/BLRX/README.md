---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001498403
cik: 0001498403
company_name: BioLineRx Ltd.
tickers:
- BLRX
status: stub
canonical_reviewed: false
as_of: '2026-10-28'
updated_at: '2026-10-28T16:13:42.115634+00:00'
reviewed_at: null
coverage_release: coverage-20261028-40722802424-1
source_commit: 8a30d18f29f6ce6c61cbe955ca3f23f6f12ef180
financial_history_available: false
curated_research: null
financial_gap:
  reason: foreign_reporting_adapter
  next_action: Add support for the observed 20-F, 40-F or 6-K reporting forms and
    verify the actual accounting taxonomy before normalization.
  observed_forms:
  - 20-F
  - 20-F/A
  - 20FR12B
  - 20FR12B/A
  - '3'
  - 424B2
  - 424B3
  - 424B5
  - 6-K
  - 6-K/A
  - AW
  - CERTNAS
  - CORRESP
  - CT ORDER
  - D
  - EFFECT
  - F-1
  - F-1/A
  - F-3
  - F-3/A
  - F-6
  - FWP
  - POS AM
  - RW
  - S-8
  - S-8 POS
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13G
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001498403.json
    sha256: 2caf587fb6162049497f44b49b27ec547123d5000db40b19c18fcea2a9618502
    retrieved_at: '2026-10-24T13:22:51.759433+00:00'
    archive: &id001
      member: CIK0001498403.json
      sha256: 593fbbea6512ef5ec729a5e513c465fbedaac8a66602c0abe00d0ba5a4d18732
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: nasdaqlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt
  published_at: null
  retrieved_at: '2026-10-28T16:09:01.738588+00:00'
  sha256: b555e192b928396dc88877226e82c2c8e9470c389cf2def559495683c673510d
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001498403.json
  published_at: null
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 2caf587fb6162049497f44b49b27ec547123d5000db40b19c18fcea2a9618502
- id: S03
  title: 6-K 0001178913-26-004823
  url: https://www.sec.gov/Archives/edgar/data/1498403/000117891326004823/0001178913-26-004823-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S04
  title: EFFECT 9999999995-26-003144
  url: https://www.sec.gov/Archives/edgar/data/1498403/999999999526003144/9999999995-26-003144-index.html
  published_at: '2026-10-02'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S05
  title: 424B3 0001178913-26-004697
  url: https://www.sec.gov/Archives/edgar/data/1498403/000117891326004697/0001178913-26-004697-index.html
  published_at: '2026-10-02'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S06
  title: F-1 0001178913-26-004612
  url: https://www.sec.gov/Archives/edgar/data/1498403/000117891326004612/0001178913-26-004612-index.html
  published_at: '2026-09-25'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S07
  title: 6-K 0001178913-26-004591
  url: https://www.sec.gov/Archives/edgar/data/1498403/000117891326004591/0001178913-26-004591-index.html
  published_at: '2026-09-24'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S53
  url: https://www.sec.gov/Archives/edgar/data/1498403/000117891326001807/zk2634966.htm
  title: 20-F/A 0001178913-26-001807
  published_at: '2026-03-27'
  retrieved_at: '2026-10-25T13:59:09.609139+00:00'
  sha256: d6c8b75e67a013388b017c7705363dab7b30e0a246683185769c8f38ac85490e
- id: S54
  url: https://www.sec.gov/Archives/edgar/data/1498403/000117891326001581/zk2634707.htm
  title: 20-F 0001178913-26-001581
  published_at: '2026-03-23'
  retrieved_at: '2026-10-25T13:59:07.720185+00:00'
  sha256: 67951ce0bf5c741387199b7412e8db7750c83cbe9d9be6b407fd864e1229260d
issuer_classification:
  cik: 0001498403
  classification_status: reported_sic
  entity_type: other
  name: BioLineRx Ltd.
  sic: '2834'
  sic_description: Pharmaceutical Preparations
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 2caf587fb6162049497f44b49b27ec547123d5000db40b19c18fcea2a9618502
  url: https://data.sec.gov/submissions/CIK0001498403.json
listings:
- ticker: BLRX
  exchange: NASDAQ
  instrument_type: depositary_receipt
research_filings:
- accession: 0001178913-26-001581
  filed: '2026-03-23'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1498403/000117891326001581/0001178913-26-001581-index.html
- accession: 0001178913-26-001807
  filed: '2026-03-27'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1498403/000117891326001807/0001178913-26-001807-index.html
- accession: 0001178913-24-001095
  filed: '2024-03-26'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1498403/000117891324001095/0001178913-24-001095-index.html
- accession: 0001178913-22-003376
  filed: '2022-09-09'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1498403/000117891322003376/0001178913-22-003376-index.html
- accession: 0001178913-19-001988
  filed: '2019-07-30'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1498403/000117891319001988/0001178913-19-001988-index.html
- accession: 0001178913-19-001666
  filed: '2019-06-05'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1498403/000117891319001666/0001178913-19-001666-index.html
- accession: 0001178913-16-005577
  filed: '2016-05-31'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1498403/000117891316005577/0001178913-16-005577-index.html
- accession: 0001178913-15-002925
  filed: '2015-09-22'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1498403/000117891315002925/0001178913-15-002925-index.html
- accession: 0001178913-15-000973
  filed: '2015-03-23'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1498403/000117891315000973/0001178913-15-000973-index.html
- accession: 0001178913-14-001699
  filed: '2014-05-15'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1498403/000117891314001699/0001178913-14-001699-index.html
- accession: 0001178913-12-000797
  filed: '2012-03-26'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1498403/000117891312000797/0001178913-12-000797-index.html
- accession: 0001178913-26-004823
  filed: '2026-10-23'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1498403/000117891326004823/0001178913-26-004823-index.html
research_progress:
  stage: retry
  input_sha256: c353802d965cb70a340a90e487c61b303014174d9141a3ee096afb945d2ffdad
  last_attempt_at: '2026-10-25T13:56:40.792803+00:00'
  last_success_at: null
  next_retry_at: '2026-10-26T13:56:40.792803+00:00'
  source_set_current: false
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
  - risks-and-thesis-breakers
  derived_observations: 0
  model_draft: false
  reviewed: false
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
  source_url: https://data.sec.gov/submissions/CIK0001498403.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/5da532c3abee5b40a5400c5864c6f3f4593276d7/brain/companies/BLRX/README.md
full_history_commit: 5da532c3abee5b40a5400c5864c6f3f4593276d7
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# BLRX — BioLineRx Ltd.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/5da532c3abee5b40a5400c5864c6f3f4593276d7/brain/companies/BLRX/README.md)

## Business overview

Reported issuer name: **BioLineRx Ltd.**. Stable SEC CIK: **0001498403**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| BLRX | NASDAQ | depositary_receipt | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 20-F, filed 2026-03-23, L428; prior source set, update pending:

> statements as to the impact of the political and security situation in Israel on our business which may exacerbate the magnitude [S54]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 20-F, filed 2026-03-23, L771; prior source set, update pending:

> may receive from our licensees, as well as the commercial success of our products will depend on, among other things, the efforts, allocation [S54]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 20-F, filed 2026-03-23, L1603; prior source set, update pending:

> purchasers, including the impact of consolidation of our customers. In 2022, the IRA, established the Medicare Drug Price Negotiation [S54]

## Industry and value chain

SEC-reported SIC **2834**: Pharmaceutical Preparations. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 20-F, filed 2026-03-23, L1928; prior source set, update pending:

> and global supply chain disruptions, have caused, and may in the future cause, global economic uncertainty and uncertainty about the interest [S54]

Navigation sector: **health-care**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 20-F, filed 2026-03-23, L784; prior source set, update pending:

> on the benefits of APHEXDA over its competition have required significant resources and may not ultimately be successful. If GLIX1, motixafortide, [S54]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 20-F, filed 2026-03-23, L407; prior source set, update pending:

> the scope of protection that we are able to establish and maintain for intellectual property rights covering our therapeutic candidates [S54]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 20-F, filed 2026-03-23, L1937; prior source set, update pending:

> terms could have a material adverse effect on our growth strategy, financial performance and market price of our ordinary shares and ADSs [S54]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 20-F/A, filed 2026-03-27, L92; prior source set, update pending:

> Indicate by check mark whether any of those error corrections are restatements that required a recovery analysis of incentive-based compensation received by any of the registrant’s executive officers during the relevant recovery period pursuant to §240.10D-1(b). ☐ [S53]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 20-F, filed 2026-03-23, L336; prior source set, update pending:

> 3. Key Information - Risk Factors,” “Item 4. Information on the Company” and “Item 5. Operating and Financial [S54]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 20-F, 20-F/A, 20FR12B, 20FR12B/A, 3, 424B2, 424B3, 424B5, 6-K, 6-K/A, AW, CERTNAS, CORRESP, CT ORDER, D, EFFECT, F-1, F-1/A, F-3, F-3/A, F-6, FWP, POS AM, RW, S-8, S-8 POS, SC 13D, SC 13D/A, SC 13G, SC 13G/A, SCHEDULE 13G, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:33:42.253413+00:00.

### Research work queue

Collection stage: **retry**. Extracted evidence is not a reviewed conclusion. Daily collection resumes from durable state; unchanged accessions are reused.

- **Business overview** (source excerpts available; assess the claim): Explain what the company does, who pays it, and why the business exists. Cite primary sources.
- **Revenue model and segments** (evidence or analysis still needed): Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.
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
| 2026-10-23 | 6-K | 0001178913-26-004823 | — | [S03] |
| 2026-10-02 | EFFECT | 9999999995-26-003144 | — | [S04] |
| 2026-10-02 | 424B3 | 0001178913-26-004697 | — | [S05] |
| 2026-09-25 | F-1 | 0001178913-26-004612 | — | [S06] |
| 2026-09-24 | 6-K | 0001178913-26-004591 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-28T16:09:01.738588+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001498403.json) — published not supplied; retrieved 2026-10-24T13:22:51.759433+00:00.

[S03] [6-K 0001178913-26-004823](https://www.sec.gov/Archives/edgar/data/1498403/000117891326004823/0001178913-26-004823-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S04] [EFFECT 9999999995-26-003144](https://www.sec.gov/Archives/edgar/data/1498403/999999999526003144/9999999995-26-003144-index.html) — published 2026-10-02; retrieved 2026-10-24T13:22:51.759433+00:00.

[S05] [424B3 0001178913-26-004697](https://www.sec.gov/Archives/edgar/data/1498403/000117891326004697/0001178913-26-004697-index.html) — published 2026-10-02; retrieved 2026-10-24T13:22:51.759433+00:00.

[S06] [F-1 0001178913-26-004612](https://www.sec.gov/Archives/edgar/data/1498403/000117891326004612/0001178913-26-004612-index.html) — published 2026-09-25; retrieved 2026-10-24T13:22:51.759433+00:00.

[S07] [6-K 0001178913-26-004591](https://www.sec.gov/Archives/edgar/data/1498403/000117891326004591/0001178913-26-004591-index.html) — published 2026-09-24; retrieved 2026-10-24T13:22:51.759433+00:00.

[S53] [20-F/A 0001178913-26-001807](https://www.sec.gov/Archives/edgar/data/1498403/000117891326001807/zk2634966.htm) — published 2026-03-27; retrieved 2026-10-25T13:59:09.609139+00:00.

[S54] [20-F 0001178913-26-001581](https://www.sec.gov/Archives/edgar/data/1498403/000117891326001581/zk2634707.htm) — published 2026-03-23; retrieved 2026-10-25T13:59:07.720185+00:00.

Source release: `coverage-20261028-40722802424-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/5da532c3abee5b40a5400c5864c6f3f4593276d7/brain/companies/BLRX/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
