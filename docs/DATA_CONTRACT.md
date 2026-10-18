# Data contract

## Company records

A record lives at `sectors/<sector>/companies/<TICKER>/README.md`. YAML frontmatter is followed by an H1 title and exactly the ordered H2 headings in [sections.json](../config/sections.json). H3 headings are allowed inside a section. The [company template](../templates/company/README.md) documents the format.

| Field | Meaning |
| --- | --- |
| `schema_version` | Integer `1` |
| `document_type` | `company` |
| `company_id` | Immutable internal ID; independent of ticker and sector |
| `ticker` | Canonical uppercase U.S. listing symbol matching the directory |
| `ticker_aliases` | Other share classes or historical ticker strings; must be unique across records |
| `company_name` | Display name |
| `exchange` | `NASDAQ`, `NYSE`, or `NYSE_AMERICAN` |
| `security_type` | `common_stock` or `adr` |
| `domicile_country` | ISO-style two-letter country code, or `null` while unknown |
| `cik` | Ten-digit SEC CIK as a quoted string, or `null` |
| `sector` | ID from [sectors.json](../config/sectors.json), matching the directory |
| `industry` | Authored industry label, or `null` while unknown |
| `tags` | Unique lowercase hyphenated themes; not a replacement for the primary sector |
| `status` | `stub`, `draft`, `reviewed`, or `archived` |
| `as_of` | Date through which the research was reviewed, or `null` for unreviewed content |
| `updated_at` | Date the document was changed |
| `reviewed_at` | Date review was completed, or `null` |
| `sources` | Source registry described below |

Dates use `YYYY-MM-DD`. `as_of` must not follow `reviewed_at`, and review cannot follow `updated_at`. Future metadata dates are rejected. Reviewed records require non-null research and review dates. `company_id` and ticker/aliases must be globally unique. A non-null CIK must also be unique; keep multiple share classes in a single company profile.

## Source registry

```yaml
sources:
  - id: S01
    title: Replace with the actual document title
    publisher: Replace with the issuer or publisher
    url: https://example.com/actual-source
    published_at: null
    accessed_at: '2026-10-18'
```

The URL above is illustrative, not evidence. Use real sources in company profiles. Cite sources in prose as `[S01]`, `[S02]`, and so on. Source IDs must be unique within a profile, and every cited ID must be registered. URLs must be HTTP or HTTPS. Publication may be unknown; access date is required and cannot predate a known publication date.

## Generated outputs

`INDEX.md`, the eleven sector `INDEX.md` files, and `data/catalog.json` are deterministic outputs of the `build` command. The catalog records all profiles, including unreviewed and archived records, with their status. It is a navigation catalog, not a retrieval corpus. `check` rejects stale generated files as well as invalid profiles.

`export` writes a separate JSONL retrieval corpus, containing only eligible sections of reviewed company records. The Sources and change log section is provenance rather than research content, so it is not a searchable chunk. See [RAG design](RAG.md) for the output fields and ingestion rules.
