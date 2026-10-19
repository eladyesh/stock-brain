# Critical disclosure updates — 2026-10-19

Reviewer: OpenAI Codex agent `/root/critical_disclosures`, **AI**. This is not independent human approval. The incremental review date is October 19; both companies retain their **October 18 evidence cutoff**, because other announcements remain unreviewed.

## Sources and scope

Read both queued earnings Form 8-Ks and their earnings releases and supplementary exhibits in full:

- AMD: [August 4 filing](https://www.sec.gov/Archives/edgar/data/2488/000000248826000121/amd-20260804.htm), [earnings release](https://www.sec.gov/Archives/edgar/data/2488/000000248826000121/q22026991.htm), and [presentation, now S08](https://www.sec.gov/Archives/edgar/data/2488/000000248826000121/amdq22026earningsslidesf.htm).
- NVIDIA: [August 26 filing](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/nvda-20260826.htm), [earnings release](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27pr.htm), and [CFO commentary, now S05](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27cfocommentary.htm).

Reopened the existing annual, quarterly, amendment and subsequent-event sources at the retained claims' cited locations. SEC submission inventories showed no later quarterly results; the inspected subsequent filings did not replace the earnings guidance. This does not establish exhaustive announcement coverage. Retrieval hashes, actual read scope, claim checks and approved packet/profile bindings are in `AMD.json` and `NVDA.json` in this directory. Full documents remain outside tracked research.

## Research changes

- **AMD:** added the dated Q3 revenue, margin, expense, other-income and tax guidance; preserved non-GAAP labels. Added the detailed diluted-share estimate and its historical price assumption, explicitly excluding its use as a current quote. Added investment-gain context and quantified commitments/lease guarantees. The Q3 period dates are explicitly identified as fiscal-calendar mapping. Monitoring now connects outlook misses, delayed deployments, cash generation and purchase obligations.
- **NVIDIA:** reconciled exact quarterly operating cash flow and receivables with the CFO's rounded discussion; retained DSO units. Added supply commitments and subsequent-event guarantee caps, with tenant-default/lease-commencement conditions. Maximum exposure is not debt, expected loss or revenue. Preserved the FY2029 expectation and the changed non-GAAP stock-compensation convention. Monitoring now tracks collections, cash-flow recovery, deployment delays, unused commitments and guarantee calls.
- Added ten claims and 24 typed metrics across the two packets; refreshed both canonical profiles and all corresponding Hebrew translations. No market forecast, valuation, default probability or independent product benchmark was invented.

## Queue decisions

The two P0 events resolve through their new **hash-bound reviewed evidence and SEC accessions**, not through a nonmaterial disposition:

| Event | Result |
| --- | --- |
| AMD `3b97f5980575158e811e4534` | Presentation incorporated and reviewed |
| NVDA `36233869aa3d76f8787af342` | CFO commentary incorporated and reviewed |

Inspected the 25 P1 entries for likely overlaps. Fully read the AMD board announcement and its existing reviewed filing, then recorded one verified `no_material_change` decision for `a4d847e532c7b32cec9d73c7` (record `b1bb8a301d0aa11aab32ade1`). Both original sources were refetched and bound before recording. The announcement repeats the same appointment, retirement and committee changes; added biography does not change the reviewed governance claims.

Read the NVIDIA August 17 guarantee wrapper, Micron August 26 leadership wrapper and RTX conference notice, but made no closure for them. The first two require additional exhibit/legal or leadership coverage; the conference notice was outside this bounded overlap closure. Other downloaded P1 documents were not substantively reviewed and remain pending. Downloads alone are not reviews.

Immediately after these decisions, the existing snapshot contained **147 events, 137 pending: P0 0, P1 24, P2 104, P3 9**. These are pre-refresh counts, not a claim about future discovery.

## Validation and limits

`research_company.py audit` passed: ten reviewed profiles, zero drafts. All 42 AMD/NVDA Hebrew claims passed source-hash, translated-text-hash and numeric-token checks. The catalog validator correctly requested rebuilding generated artifacts after canonical changes; the integration lead owns that rebuild. Source review and translation judgment are AI work; these mechanical checks do not prove financial truth or independent human approval. Remaining announcements, valuation, ownership and counterparty economics still require research.
