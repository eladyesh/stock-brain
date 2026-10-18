# Pilot results — 2026-10-18

Ten issuers are populated with sourced English research. The scope is an initial knowledge base, not a complete market screen, valuation service or deployed investment assistant.

## Coverage and review

| Cohort | Reviewed reference snapshots | Drafts awaiting separate review |
| --- | --- | --- |
| Software/cloud | MSFT | ORCL, PLTR |
| Semiconductors | MU | NVDA, AMD, AVGO |
| Defense | AVAV | LMT, RTX |

The three reference packets contain 54 claims and 28 metrics. A separate evidence-checking agent read the supporting primary-source passages, raised three wording corrections, and reread the fixes. Microsoft consumer-segment scope and M365-specific growth attribution were narrowed; Micron production versus shipment wording was corrected. See [the independent audit](../research/reviews/reference-audit.md) and the hash-bound review records. These are AI research reviews, not human sign-off or financial-statement audit opinions.

Two reviewed sector guides cover a deliberately limited software/cloud-and-memory view of technology and an AeroVironment-based defense view of industrials. Nine other sector guides remain planning material and are excluded from retrieval. Every company profile has the standard 18 headings, dated sources and explicit research gaps.

## Verification

- 34 behavior/failure-mode tests pass, including original knowledge-base tests, exact-period facts, calculation compatibility, stale review rejection, source-ID preservation, pending update persistence, PDF handling, runner failures and retrieval guards.
- Metadata, indexes, evidence packets and review bindings validate.
- Reviewed export contains 59 chunks: 49 company chunks and 10 sector chunks. Seven drafts are excluded.
- The English lexical baseline passes all 15 answerable retrieval cases and all five abstention cases. [Gold questions](../eval/questions.json) and [the reproducible baseline result](../eval/baseline.json) are committed. This is a visible development set, not a held-out accuracy claim. Answer generation, factuality and citation entailment are not evaluated by that script.
- Live SEC/curated-source collection completed without unresolved fetch errors for all ten issuers. The Oracle IR release was unreadable to the collector; the same release was verified and collected from its filed SEC exhibit.
- A repeated AVAV run detected no source change, skipped generation, and preserved the exact packet/profile hashes and review dates. Regression coverage verifies that collecting an unapplied new disclosure repeatedly cannot erase the pending change.

## Collection measurements

These are each issuer's most recent successful collection after adding curated sources, with an already populated SEC cache. They include network/extraction time; they exclude research, source selection, drafting and review. They are not a cold-start benchmark or a runtime guarantee.

| Issuer | Collected documents | Seconds | Downloads | Cache hits |
| --- | ---: | ---: | ---: | ---: |
| MSFT | 10 | 39.250 | 8 | 4 |
| ORCL | 6 | 14.324 | 3 | 5 |
| PLTR | 7 | 19.516 | 4 | 5 |
| MU | 5 | 12.571 | 5 | 2 |
| NVDA | 6 | 7.632 | 3 | 5 |
| AMD | 7 | 6.968 | 3 | 6 |
| AVGO | 7 | 7.623 | 3 | 6 |
| AVAV | 7 | 19.724 | 4 | 5 |
| LMT | 6 | 14.574 | 3 | 5 |
| RTX | 6 | 14.698 | 3 | 5 |

The sum of these per-issuer measurements is 156.880 seconds; median 14.449 seconds. This sum is not total project duration. The later AVAV no-change run took 11.233 seconds with 7 cached documents. Details: [pilot-run.json](../research/pilot-run.json).

## Costs and remaining limits

No paid model API call was made. The optional adapter was validated with local protocol/failure tests; live paid generation still requires a user-supplied key and model. ChatGPT's research/review token usage, monetary cost and per-company review duration were not exposed, so they are recorded as unknown rather than zero. Future runner jobs record reported tokens, elapsed time and an estimate only if explicit prices are configured.

The collector samples event filings and requires curated earnings/call/product sources. It does not promise exhaustive news, insider, litigation or contract coverage. Review the manifest gaps. Historical prices, current valuation, analyst consensus, normalized-cycle forecasts and several detailed governance/operating questions remain unresearched where the profiles say so. Large excerpts can omit important evidence; local validation does not prove source support.

Expand by reviewing the seven drafts, then adding cohorts of three to five. Track actual review minutes and correction rates alongside collection/model cost. Add a held-out set with conflicting-source, sector and Hebrew questions before selecting an embedding service or production answering stack.
