# Contributor instructions

- Keep canonical research, documentation, code, and comments in English. The user explicitly requested Hebrew questions and answers; query aliases, localized evidence, UI labels, and answer output may therefore use Hebrew.
- Markdown company profiles are the source of truth; preserve the ordered sections in `config/sections.json`.
- Keep company IDs stable across ticker, company-name, and sector changes.
- Never fabricate company facts, sources, financial numbers, or research review status.
- New profiles start as stubs. Review must be based on actual evidence, not passing format validation.
- Update source dates and distinguish reported facts, guidance, estimates, and interpretation.
- Do not hand-edit generated indexes or `data/catalog.json`; use the build command.
- Do not include stubs, drafts, templates, indexes, or archives in retrieval exports.
- After changes, run the validator and the tests relevant to changed behavior.
- Keep credentials and generated embeddings out of Git.
