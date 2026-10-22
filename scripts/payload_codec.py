"""Bounded, content-addressed company payloads stored inside the SQLite snapshot.

Compression changes storage only. The SHA-256 identifies the original canonical
UTF-8 JSON; each version retains its own original source evidence and timestamp.
"""
import hashlib
import json
import re
import zlib


MAX_PAYLOAD = 64 * 1024 * 1024
COMPRESS_AT = 4096
CODEC = 'zlib-json-v1'


class PayloadIntegrityError(ValueError):
    """Stored content is missing, inconsistent or cannot be decoded within bounds."""


def _reject_constant(_):
    raise ValueError('nonfinite JSON')


def pack(encoded):
    raw = encoded.encode('utf-8')
    if len(raw) > MAX_PAYLOAD:
        raise ValueError('company payload exceeds 64 MiB')
    if len(raw) < COMPRESS_AT:
        return None
    return {'codec': CODEC, 'raw_size': len(raw), 'data': zlib.compress(raw, level=6)}


def unpack(sha256, codec, raw_size, data):
    if (not isinstance(sha256, str) or not re.fullmatch('[0-9a-f]{64}', sha256)
            or codec != CODEC or type(raw_size) is not int or not 1 <= raw_size <= MAX_PAYLOAD
            or not isinstance(data, bytes) or not 0 < len(data) <= MAX_PAYLOAD + 65536):
        raise PayloadIntegrityError('invalid payload object metadata')
    try:
        inflater = zlib.decompressobj()
        raw = inflater.decompress(data, raw_size + 1)
        if (len(raw) != raw_size or not inflater.eof or inflater.unused_data or inflater.unconsumed_tail
                or hashlib.sha256(raw).hexdigest() != sha256):
            raise PayloadIntegrityError('payload object size or digest mismatch')
        value = json.loads(raw.decode('utf-8'), parse_constant=_reject_constant)
        if not isinstance(value, dict):
            raise PayloadIntegrityError('payload object must be a JSON object')
        return value
    except (zlib.error, UnicodeError, ValueError, RecursionError) as error:
        raise PayloadIntegrityError('payload object failed integrity validation') from error


def validate_snapshot(connection):
    """Stream validation of objects and references before backup/restore publication.

    Older standalone databases have no object table and remain recoverable.
    This does not hold the entire corpus or all decoded histories in memory.
    """
    if not connection.execute("SELECT 1 FROM sqlite_schema WHERE type='table' AND name='payload_objects'").fetchone():
        return
    bad = connection.execute('''SELECT 1 FROM company_payloads p LEFT JOIN payload_objects o
        ON o.sha256=p.object_sha256 WHERE p.object_sha256 IS NOT NULL AND
        (o.sha256 IS NULL OR p.sha256!=p.object_sha256 OR p.value_json!='') LIMIT 1''').fetchone()
    if bad:
        raise PayloadIntegrityError('invalid payload object reference')
    for row in connection.execute('SELECT sha256,codec,raw_size,data FROM payload_objects'):
        unpack(*row)
