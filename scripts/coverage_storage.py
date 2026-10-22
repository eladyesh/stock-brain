"""Inspect storage and resume lossless payload compression without network access.

The current public-release envelope remains bounded at 512 MiB restored. Version
2 releases use independently verified 32 MiB raw chunks. This migration removes
repeated JSON values; it does not promise
unlimited historical retention within that envelope. No data versions are pruned.
"""
import argparse
import json
from pathlib import Path

import payload_codec


MAX_DATABASE = 512 * 1024 * 1024
MAX_COMPRESSED = 128 * 1024 * 1024
CHUNK_RAW_SIZE = 32 * 1024 * 1024
MAX_CHUNK_COMPRESSED = CHUNK_RAW_SIZE + 128 * 1024
MAX_TOTAL_COMPRESSED = MAX_DATABASE + 2 * 1024 * 1024


def status(store):
    with store._connection() as db:
        page_size = db.execute('PRAGMA page_size').fetchone()[0]
        allocated = db.execute('PRAGMA page_count').fetchone()[0] * page_size
        free = db.execute('PRAGMA freelist_count').fetchone()[0] * page_size
        objects = db.execute('''SELECT count(*),coalesce(sum(raw_size),0),coalesce(sum(length(data)),0)
                                FROM payload_objects''').fetchone()
        versions = db.execute('''SELECT count(*),
            coalesce(sum(CASE WHEN p.object_sha256 IS NULL THEN length(CAST(p.value_json AS BLOB)) ELSE o.raw_size END),0),
            coalesce(sum(CASE WHEN p.object_sha256 IS NULL THEN length(CAST(p.value_json AS BLOB)) ELSE 0 END),0),
            coalesce(sum(p.object_sha256 IS NOT NULL),0),
            coalesce(sum(p.object_sha256 IS NULL AND length(CAST(p.value_json AS BLOB))>=?),0)
            FROM company_payloads p LEFT JOIN payload_objects o ON o.sha256=p.object_sha256''',
            (payload_codec.COMPRESS_AT,)).fetchone()
    used = allocated - free
    return {'format': 'sqlite-content-addressed-zlib-v1', 'database_bytes': allocated,
            'reclaimable_page_bytes': free, 'used_page_bytes': used,
            'release_database_limit_bytes': MAX_DATABASE, 'legacy_compressed_limit_bytes': MAX_COMPRESSED,
            'release_chunk_raw_bytes': CHUNK_RAW_SIZE, 'release_total_compressed_limit_bytes': MAX_TOTAL_COMPRESSED,
            'capacity_status': 'limit_exceeded' if used > MAX_DATABASE else 'headroom_low' if used > MAX_DATABASE * .7 else 'within_limit',
            'payload_versions': versions[0], 'logical_version_bytes': versions[1],
            'inline_bytes': versions[2], 'object_references': versions[3], 'legacy_large_payloads': versions[4],
            'unique_objects': objects[0], 'unique_object_raw_bytes': objects[1],
            'compressed_object_bytes': objects[2], 'stored_content_bytes': objects[2] + versions[2],
            'versions_removed': 0,
            'scope': 'Observed local storage, not proof that all issuers or unlimited history fit. The restored database cap remains 512 MiB.'}


def main(argv=None):
    from coverage_store import CoverageStore
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['status', 'compact'])
    parser.add_argument('--db', required=True, type=Path)
    parser.add_argument('--limit', type=int, default=100)
    args = parser.parse_args(argv)
    if not args.db.is_file():
        parser.error('database must already exist')
    store = CoverageStore(args.db)
    result = {'compaction': store.compact_payloads(args.limit)} if args.command == 'compact' else {}
    print(json.dumps({**result, 'storage': status(store)}, indent=2))


if __name__ == '__main__':
    main()
