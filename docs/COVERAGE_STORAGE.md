# Coverage storage and recovery

## Schema 6: compressed objects, original evidence

Large company payloads (at least 4 KiB UTF-8) are stored as `zlib-json-v1` blobs in
`payload_objects`, addressed by the SHA-256 of the original canonical JSON.
`company_payloads` retains each version, original hash, stored time and source
evidence. Source-only changes reuse the same object and still create a distinct
version. Historical values are available through `get_payload_record(...,
version=N)`. Small records remain inline; there is no filesystem sidecar to lose.

Decompression validates codec, length, stream termination, JSON type and digest,
with a 64 MiB per-value bound. Snapshots validate every object and reference before
backup/restore publication. A missing or corrupt object fails closed. Compare-and-
swap and leased job commits still encompass metadata and object creation together.

Schema migration is additive. Existing inline records remain readable immediately;
compression proceeds in bounded transactions and is safe to resume:

```bash
python scripts/coverage_storage.py status --db /data/coverage.sqlite3
python scripts/coverage_storage.py compact --db /data/coverage.sqlite3 --limit 100
```

The daily release builder converts up to 1,000 legacy large records per run.
No versions are deleted and no source dates are changed. It compacts only its
private copied snapshot before publication; the live database is never vacuumed
or replaced underneath active readers.

## Version-2 releases

The immutable release manifest names ordered `coverage.part-NNNN.sqlite3.gz`
assets. Each independently compressed part represents at most 32 MiB of the
SQLite snapshot and records raw offset, raw length, raw SHA-256, compressed size
and compressed SHA-256. There are at most 16 parts. Assembly streams one MiB at a
time, validates all bounds, rejects gaps/reordering/path substitution and checks
the complete database hash, SQLite integrity and payload objects before install.

The restored database cap remains **512 MiB**. Each compressed part is capped at
32 MiB + 128 KiB, and total compressed bytes at 514 MiB. The additional bytes
allow compression overhead on incompressible input, not a larger database. This
removes the former 128 MiB single-compressed-file bottleneck. Legacy version-1
releases continue to restore with their original 128 MiB compressed cap.

The existing release workflow uploads every part, downloads the published bytes
into an empty directory and performs cold recovery. It publishes the off-host
proof only after that succeeds. Mirror readers retain the prior generation on
failure. Old application versions ignore multipart-only releases; deploy the
schema-6 reader before expecting it to consume them. No public raw vendor data is
authorized by this format: the separate bulk-export permission gate still applies.

Disk-space checks reserve room for decompression and the verified destination
before downloading/restoring. Local generation cleanup retains active and previous
copies; immutable off-host releases preserve recovery history. This continues to
use the existing repository and Render service, without adding a paid disk.

## Capacity evidence and limits

An October 22 local migration probe restored production release
`coverage-20261022-39802451522-1`. All 20 current payload values and their metadata
were exactly equal before and after conversion. Content storage fell from
3,834,793 to 244,049 bytes. The compacted full database was 15,564,800 bytes;
the multipart format and local cold restore passed. This proves lossless migration
for the ten pilot issuers, not additional financial coverage.

A separate **synthetic** 7,000-issuer experiment copied the shape of those ten
pilot histories and narrative payloads, changed fixture identities, and explicitly
marked all 14,000 records as synthetic/unreviewed. It retained 2,685,388,880 logical
JSON bytes in a 192,098,304-byte compacted database. Six release parts totaled
175,165,647 compressed bytes, exceeding the old single-file cap while remaining
inside the new envelope. Full local cold recovery passed. The experiment took
311.83 seconds in this workspace, including 133.18 seconds for writes, with peak
process RSS of 74,064 KiB. These are measured local fixture results, not production
latency guarantees or evidence of 7,000 acquired company datasets. Broader issuer
types, archive sizes, new versions and long-term growth still require observation.

`/api/coverage.storage` reports physical pages, reclaimable pages, logical version
bytes, compressed object bytes, deduplication, outstanding legacy records and the
capacity envelope. It warns at 70% of the restored database limit. The package
builder still refuses to exceed the limit; it does not delete data to make a run
pass. Monitor actual growth, particularly new historical versions and observations.
Before that envelope is exhausted, move the same content-hash contract to a
verified sharded/object store or managed database with a separate cost decision.

Synthetic capacity experiments are not source acquisition or research. Keep them
under ignored `build/` paths and never publish their databases or mark their
fixtures as reviewed. Production coverage always comes from actual source data.

## Remaining source and accounting work

SEC acquisition is still paused after an access denial. There is no real SEC bulk
archive in the production job, and the alternative connected provider returned a
zero-balance error. No key, operator contact, budget or export license is invented.
IFRS/foreign financial forms, a complete authorized OTC master and other datasets
remain independent requirements. Storage readiness alone is not complete coverage.
