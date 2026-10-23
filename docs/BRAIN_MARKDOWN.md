# Company Markdown at market scale

The `brain-data` branch holds real, versioned Markdown files for each distinct
CIK linked to a current stock candidate in the verified coverage database.
[Browse the files](https://github.com/eladyesh/stock-brain/blob/brain-data/brain/INDEX.md).
The generated factual profiles complement the curated company research on
`main`; they do not replace its review status or join reviewed retrieval exports.

## Content and identity

- `brain/companies/{ten-digit-cik}/README.md`: stable company ID, current mapped
  listings, all headings from `config/sections.json`, every retained normalized
  financial period and metric, recent filing metadata, source URLs, original
  acquisition dates, hashes and SEC bulk archive provenance.
- `brain/unmapped/{listing_key}.md`: directory evidence for a stock candidate
  without a verified CIK. This is a listing slot, not an identified company.
- `brain/INDEX.md` and `brain/index/*.md`: bounded pages with 100 entries each.
- `brain/publication.json`: source data release, database hash, source code
  commit, exact issuer inventory and separate financial/identity-gap counts.
- `brain/files.json`: SHA-256 and byte size of every published content file.

Generated company files have `document_type: company_facts`, `status: stub`,
`canonical_reviewed: false`, and no review date. This separate contract permits
unknown sector/domicile and preferred or partnership listings without inventing
facts or weakening the curated profile schema. All ordered research sections
are present; unanswered qualitative questions remain explicitly unavailable.

Financial histories pass the existing provenance/schema validator before export.
Each value carries its period, unit, accounting basis, reported/derived status,
definition and filing references. Missing, conflicting, non-model-usable and
period-ambiguous values stay blocked, including derived cells whose inputs are
blocked. Source retrieval dates are not refreshed merely by publishing new files.
Filing metadata is limited to the latest 50 of the retained inventory and does
not claim the underlying documents were analyzed.

Curated profiles are linked at the exact generator source commit with their
original research date/status. Their contents are never rewritten by this job.
The existing `stock_brain.py export` still exports only reviewed company research.

## Daily publication

`.github/workflows/brain-markdown.yml` follows successful main-branch runs of
`Refresh US stock coverage`. It also runs on generator/curated-profile changes
and supports manual dispatch. A separate concurrency group serializes publication.

1. Restore the latest complete coverage release, checking its bounded chunks,
   hashes and cold-restore contract. Never acquire SEC data again for Markdown.
2. Render one issuer at a time into a fresh output directory. Fail if a financial
   history is invalid or identities, source citations, section order or counts
   disagree. Files and the complete export have explicit capacity bounds.
3. Verify every persisted byte against its manifest before publication.
4. In an isolated Git checkout, verify the previous branch against its manifest.
   A manual edit, added file or missing file stops the publisher without replacing
   it. Put curated research on main, not in the generated branch.
5. Commit to `brain-data` and push a normal fast-forward. Never force-push, change
   main, discard Git history, or store the workflow token in a Git config/file.
   Verify the remote ref equals the checked commit. Identical reruns do not commit.

Current listings determine this snapshot. A disappeared listing/profile remains
in Git history; disappearance is not a proven delisting. CIK-based paths survive
symbol changes and consolidate multiple share classes into one issuer profile.

## Website

The Render mirror checks the small publication index outside HTTP request handling.
`/api/coverage` and registry searches expose publication counts/date and an archive
download. Company/security detail links point to the exact published Git commit,
including a raw Markdown link. Only identities in the published inventory receive
links. A newer database than the Markdown snapshot is explicitly indicated.

Publication failure leaves the last published Markdown and previous website
links usable; it does not block the data collector or promote incomplete output.
The large Markdown corpus is not downloaded into Render memory or the browser.

## Commands

```bash
python scripts/brain_markdown.py export --source-commit <verified-main-commit> --output build/brain-data
python scripts/brain_markdown.py verify --output build/brain-data
# Authorized workflow only; GH_TOKEN is injected through its private environment.
python scripts/brain_markdown.py publish --output build/brain-data
```

For an offline reproduction, supply `--database` and `--manifest`; the entire
SQLite hash must match the verified release manifest before export starts.
