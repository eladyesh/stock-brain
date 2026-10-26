---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001571776
cik: '0001571776'
company_name: Cherry Hill Mortgage Investment Corp
tickers:
- CHMI
status: stub
canonical_reviewed: false
as_of: '2026-10-26'
updated_at: '2026-10-26T16:16:21.148680+00:00'
reviewed_at: null
coverage_release: coverage-20261026-40356450615-1
source_commit: 1a2786cc3cffc8c9981965ab9c208315321385f6
financial_history_available: false
curated_research: null
financial_gap:
  reason: latest_filing_incomplete
  next_action: Resolve the latest financial filing/CompanyFacts mismatch; any historical
    bootstrap must keep the latest-period gap explicit.
  observed_forms:
  - 10-K
  - 10-Q
  - 10-Q/A
  - '144'
  - '3'
  - '4'
  - 4/A
  - 424B1
  - 424B3
  - 424B5
  - '425'
  - '5'
  - 8-A12B
  - 8-K
  - ARS
  - CERT
  - CERTNYS
  - CORRESP
  - D
  - DEF 14A
  - DEFA14A
  - DEFM14A
  - DRS
  - EFFECT
  - FWP
  - NT 10-Q
  - PRE 14A
  - S-11
  - S-11/A
  - S-3
  - S-3/A
  - S-8
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001571776.json
    sha256: 7d3180e517f979211770e0e620b89c424eaa62869e5fbfbd1a9f3bc172f6fd6e
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001571776.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: otherlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt
  published_at: null
  retrieved_at: '2026-10-26T16:11:31.806354+00:00'
  sha256: 13932af456c860d259c16604472ab685dab69d880fb71eb6d5b53159497eb520
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001571776.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 7d3180e517f979211770e0e620b89c424eaa62869e5fbfbd1a9f3bc172f6fd6e
- id: S03
  title: DEFM14A 0001104659-26-114707
  url: https://www.sec.gov/Archives/edgar/data/1571776/000110465926114707/0001104659-26-114707-index.html
  published_at: '2026-10-08'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 425 0001628280-26-055337
  url: https://www.sec.gov/Archives/edgar/data/1571776/000162828026055337/0001628280-26-055337-index.html
  published_at: '2026-08-10'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 425 0001628280-26-054991
  url: https://www.sec.gov/Archives/edgar/data/1571776/000162828026054991/0001628280-26-054991-index.html
  published_at: '2026-08-10'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 425 0001628280-26-054987
  url: https://www.sec.gov/Archives/edgar/data/1571776/000162828026054987/0001628280-26-054987-index.html
  published_at: '2026-08-10'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 10-Q 0001140361-26-032050
  url: https://www.sec.gov/Archives/edgar/data/1571776/000114036126032050/0001140361-26-032050-index.html
  published_at: '2026-08-10'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: '0001571776'
  classification_status: reported_sic
  entity_type: operating
  name: Cherry Hill Mortgage Investment Corp
  sic: '6798'
  sic_description: Real Estate Investment Trusts
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 7d3180e517f979211770e0e620b89c424eaa62869e5fbfbd1a9f3bc172f6fd6e
  url: https://data.sec.gov/submissions/CIK0001571776.json
listings:
- ticker: CHMI
  exchange: NYSE
  instrument_type: common_stock
research_filings:
- accession: 0001140361-26-008094
  filed: '2026-03-05'
  form: 10-K
  period_end: '2025-12-31'
  url: https://www.sec.gov/Archives/edgar/data/1571776/000114036126008094/0001140361-26-008094-index.html
- accession: 0001140361-26-032050
  filed: '2026-08-10'
  form: 10-Q
  period_end: '2026-06-30'
  url: https://www.sec.gov/Archives/edgar/data/1571776/000114036126032050/0001140361-26-032050-index.html
- accession: 0001140361-26-015895
  filed: '2026-04-21'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/1571776/000114036126015895/0001140361-26-015895-index.html
- accession: 0001140361-26-031932
  filed: '2026-08-10'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/1571776/000114036126031932/0001140361-26-031932-index.html
research_progress:
  stage: pending
  input_sha256: f54a3a735eaedf178a7cd4fec5059b72663219f39cd281e85ecfd3d8dfe42b2e
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
  derived_observations: 0
  model_draft: false
  reviewed: false
sector_assignment:
  sector: unclassified
  method: unresolved
  sic: '6798'
  sic_description: Real Estate Investment Trusts
  rule_version: 1
  reason: Missing, ambiguous or unmapped reported industry; company-specific review
    is required.
full_history_url: https://github.com/eladyesh/stock-brain/blob/30a5d1cd40fce8d4a64ca29ee815b726555957d3/brain/companies/CHMI/README.md
full_history_commit: 30a5d1cd40fce8d4a64ca29ee815b726555957d3
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# CHMI — Cherry Hill Mortgage Investment Corp

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/30a5d1cd40fce8d4a64ca29ee815b726555957d3/brain/companies/CHMI/README.md)

## Business overview

Reported issuer name: **Cherry Hill Mortgage Investment Corp**. Stable SEC CIK: **0001571776**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| CHMI | NYSE | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **6798**: Real Estate Investment Trusts. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **unclassified**. Method: `unresolved`. Missing, ambiguous or unmapped reported industry; company-specific review is required.

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
- Forms observed in the retained filing inventory: 10-K, 10-Q, 10-Q/A, 144, 3, 4, 4/A, 424B1, 424B3, 424B5, 425, 5, 8-A12B, 8-K, ARS, CERT, CERTNYS, CORRESP, D, DEF 14A, DEFA14A, DEFM14A, DRS, EFFECT, FWP, NT 10-Q, PRE 14A, S-11, S-11/A, S-3, S-3/A, S-8, SC 13D, SC 13D/A, SC 13G, SC 13G/A, UPLOAD
- Collector status: quality_review_required; last action: filings_only_financials_incomplete; last checked: 2026-10-24T13:34:13.255705+00:00.

### Research work queue

Collection stage: **pending**. Extracted evidence is not a reviewed conclusion. Daily collection resumes from durable state; unchanged accessions are reused.

- **Business overview** (evidence or analysis still needed): Explain what the company does, who pays it, and why the business exists. Cite primary sources.
- **Revenue model and segments** (evidence or analysis still needed): Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.
- **Products and services** (evidence or analysis still needed): Describe the main products, customer problems solved, distribution, and product dependencies.
- **Customers and end markets** (evidence or analysis still needed): Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.
- **Industry and value chain** (evidence or analysis still needed): Place the company among suppliers, distribution channels, customers, and substitutes. Explain cyclicality and supply constraints.
- **Competitive landscape** (evidence or analysis still needed): Identify direct competitors and alternatives. Compare specific products or business segments, with sources.
- **Moat and differentiation** (evidence or analysis still needed): Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.
- **Growth drivers** (evidence or analysis still needed): Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.
- **Financial performance** (evidence or analysis still needed): Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.
- **Balance sheet and capital allocation** (evidence or analysis still needed): Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.
- **Management and governance** (evidence or analysis still needed): Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.
- **Valuation context** (evidence or analysis still needed): Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.
- **Catalysts** (evidence or analysis still needed): List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.
- **Risks and thesis breakers** (evidence or analysis still needed): Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.
- **Scenarios and open questions** (evidence or analysis still needed): Separate bull, base, and bear assumptions from facts. Record missing data, disputed evidence, and research questions without inventing answers.
- **Relationships and themes** (evidence or analysis still needed): Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.
- **Recent developments** (evidence or analysis still needed): Keep a dated, source-backed log of material changes. Distinguish the event date from the article date and explain what changed in the profile.

Calculation gaps: Validated financial history is missing.

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest five available filing metadata records; document bodies have not been analyzed here.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-10-08 | DEFM14A | 0001104659-26-114707 | — | [S03] |
| 2026-08-10 | 425 | 0001628280-26-055337 | — | [S04] |
| 2026-08-10 | 425 | 0001628280-26-054991 | — | [S05] |
| 2026-08-10 | 425 | 0001628280-26-054987 | — | [S06] |
| 2026-08-10 | 10-Q | 0001140361-26-032050 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-26T16:11:31.806354+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001571776.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [DEFM14A 0001104659-26-114707](https://www.sec.gov/Archives/edgar/data/1571776/000110465926114707/0001104659-26-114707-index.html) — published 2026-10-08; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [425 0001628280-26-055337](https://www.sec.gov/Archives/edgar/data/1571776/000162828026055337/0001628280-26-055337-index.html) — published 2026-08-10; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [425 0001628280-26-054991](https://www.sec.gov/Archives/edgar/data/1571776/000162828026054991/0001628280-26-054991-index.html) — published 2026-08-10; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [425 0001628280-26-054987](https://www.sec.gov/Archives/edgar/data/1571776/000162828026054987/0001628280-26-054987-index.html) — published 2026-08-10; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [10-Q 0001140361-26-032050](https://www.sec.gov/Archives/edgar/data/1571776/000114036126032050/0001140361-26-032050-index.html) — published 2026-08-10; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261026-40356450615-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/30a5d1cd40fce8d4a64ca29ee815b726555957d3/brain/companies/CHMI/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
