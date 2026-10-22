"""Bounded multi-asset coverage releases. Version 1 snapshots remain readable."""
import gzip
import hashlib
from pathlib import Path
import re

import coverage_backup as backup
import coverage_storage as capacity
from coverage_store import require


PART_NAME = re.compile(r'coverage\.part-[0-9]{4}\.sqlite3\.gz\Z')


def pack(raw_path, destination):
    raw_path, destination = Path(raw_path), Path(destination)
    parts = []
    with raw_path.open('rb') as source:
        while source.tell() < raw_path.stat().st_size:
            name = f'coverage.part-{len(parts):04d}.sqlite3.gz'
            path = destination / name
            offset, size, digest = source.tell(), 0, hashlib.sha256()
            with path.open('xb') as target, gzip.GzipFile(fileobj=target, mode='wb', mtime=0) as encoded:
                while size < capacity.CHUNK_RAW_SIZE:
                    block = source.read(min(1024 * 1024, capacity.CHUNK_RAW_SIZE - size))
                    if not block:
                        break
                    encoded.write(block)
                    digest.update(block)
                    size += len(block)
            parts.append({'file_name': name, 'size_bytes': path.stat().st_size, 'sha256': backup._hash(path),
                          'raw_offset': offset, 'raw_size_bytes': size, 'raw_sha256': digest.hexdigest()})
    return parts


def parts(manifest, database_size):
    """Validate all filenames, order, offsets and resource limits before acquisition."""
    version = manifest.get('version')
    require(type(version) is int, 'invalid release format version')
    if version == 1:
        item = manifest['compressed']
        require(item['file_name'] == 'coverage.sqlite3.gz', 'unexpected legacy asset name')
        entries = [{**item, 'raw_offset': 0, 'raw_size_bytes': database_size,
                    'raw_sha256': manifest['database_manifest']['snapshot']['sha256']}]
        limit = capacity.MAX_COMPRESSED
    else:
        require(version == 2, 'unsupported release format')
        entries = manifest.get('parts')
        require(isinstance(entries, list) and 1 <= len(entries) <= 16, 'invalid release part count')
        limit = capacity.MAX_CHUNK_COMPRESSED
    offset, total = 0, 0
    for index, item in enumerate(entries):
        if version == 2:
            require(item['file_name'] == f'coverage.part-{index:04d}.sqlite3.gz', 'invalid release part name/order')
            require(type(item['raw_size_bytes']) is int and 0 < item['raw_size_bytes'] <= capacity.CHUNK_RAW_SIZE,
                    'release part exceeds raw capacity')
        require(type(item['size_bytes']) is int and 0 < item['size_bytes'] <= limit, 'invalid compressed part size')
        require(type(item['raw_offset']) is int and item['raw_offset'] == offset, 'release part offset mismatch')
        require(all(isinstance(item[k], str) and re.fullmatch('[0-9a-f]{64}', item[k]) for k in ('sha256', 'raw_sha256')),
                'invalid release part digest')
        offset += item['raw_size_bytes']
        total += item['size_bytes']
    require(offset == database_size and total <= capacity.MAX_TOTAL_COMPRESSED, 'release size mismatch or capacity exceeded')
    return entries


def assemble(directory, entries, raw_path):
    """Stream-decode each verified part in order; never load a whole database."""
    with Path(raw_path).open('xb') as output:
        for item in entries:
            path = Path(directory) / item['file_name']
            require(not path.is_symlink() and path.stat().st_size == item['size_bytes']
                    and backup._hash(path) == item['sha256'], 'compressed digest mismatch')
            total, digest = 0, hashlib.sha256()
            with gzip.open(path, 'rb') as source:
                while block := source.read(1024 * 1024):
                    total += len(block)
                    require(total <= item['raw_size_bytes'], 'decompressed part exceeds manifest size')
                    digest.update(block)
                    output.write(block)
            require(total == item['raw_size_bytes'] and digest.hexdigest() == item['raw_sha256'],
                    'decompressed part size/digest mismatch')
