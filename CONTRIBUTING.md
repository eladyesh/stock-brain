# Contributing

## Add a company

Run `python scripts/stock_brain.py add --ticker SYMBOL --name "Company name" --sector SECTOR_ID --exchange NASDAQ` with verified issuer details. Choose the primary sector from [the master index](INDEX.md). The command creates a stub and refreshes all indexes. Tickers are normalized to uppercase; duplicate tickers, aliases, and company IDs are rejected. For source collection, also add the verified ten-digit SEC CIK and cohort to `config/universe.json`; see [the pipeline guide](docs/PIPELINE.md).

The generated `company_id` is an immutable identifier. Keep it when a company changes its name, ticker, or sector. For a ticker change, rename the ticker directory, update `ticker`, and retain the old symbol in `ticker_aliases` with an explanation in the change log. For a sector change, move the existing directory and update `sector`. Do not create a second profile for another share class; record alternative traded symbols in `ticker_aliases` and explain the classes in the text.

## Research and review

1. Set `status: draft` when research begins.
2. Read primary sources and register them in frontmatter `sources` with stable IDs such as `S01`.
3. Replace each TODO with sourced content or an explicit reason information is unavailable or inapplicable.
4. Cite source IDs inline, for example `Revenue is recognized as the service is delivered. [S01]`.
5. Keep facts, management guidance, estimates, and your interpretation separate.
6. Complete the [research review](docs/RESEARCH.md). For pipeline-managed profiles, use the `review` command with a claim-by-claim attestation; directly changing status will fail the review gate. Manually authored profiles outside the pipeline retain the original editorial workflow.
7. Rebuild and validate before committing.

```bash
python scripts/stock_brain.py build
python scripts/stock_brain.py check
python -m unittest discover -s tests -v
```

`reviewed` is a deliberate editorial judgment. Passing validation checks format and evidence references; it cannot verify that a claim is true or that its source actually supports it.

## Maintain existing research

Update `updated_at` for document changes. Change `as_of` and `reviewed_at` only after reviewing the relevant evidence; touching a file must not make old research appear current. Return the profile to `draft` if new material is not yet reviewed. Archive delisted or out-of-scope profiles instead of presenting them as currently covered listings.

Indexes and `data/catalog.json` are generated. Edit company READMEs and configuration, then run `build`; do not hand-edit generated files. Changes to a managed reviewed profile or packet invalidate its review binding. Return it to draft before editing, and review the changed evidence again. Sector READMEs are authored guides. Only sectors explicitly registered as reviewed in `config/sector_research.json`, with sources and an exact content hash, enter retrieval. Changing those guides also requires a new review.

Do not commit secrets, private communications, or entire copyrighted filings. Prefer concise original summaries and links to evidence. The repository's current visibility is public.
