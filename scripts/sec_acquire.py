"""Acquire the two official nightly SEC archives with a declared identity.

Streaming, fixed destinations, one request per archive, no redirects or retries.
A denial stops the acquisition. The offline importer independently verifies each
hash and ZIP inventory before processing any issuer.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import time
from urllib.error import HTTPError
from urllib.request import Request, HTTPRedirectHandler, build_opener

from coverage_store import require
from research_pipeline import validate_sec_user_agent
from sec_bulk import MAX_ARCHIVE, URLS


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


def acquire(destination, *, environ=None, opener=None, clock=time.monotonic):
    env = os.environ if environ is None else environ
    require(env.get('STOCK_BRAIN_SEC_ENABLED') == '1', 'SEC acquisition is paused')
    identity = env.get('SEC_USER_AGENT', '')
    validate_sec_user_agent(identity)
    out = Path(destination)
    out.mkdir(parents=True, exist_ok=False)
    opener = opener or build_opener(NoRedirect)
    manifest = {'format': 'stock-brain-sec-bulk-v1', 'network_requests': 0}
    for kind, url in URLS.items():
        path = out / (kind + '.zip')
        partial = out / (kind + '.partial')
        started = clock()
        try:
            request = Request(url, headers={'User-Agent': identity, 'Accept-Encoding': 'identity'})
            manifest['network_requests'] += 1
            with opener.open(request, timeout=120) as response:
                require(response.status == 200 and response.url == url, 'unexpected SEC archive response')
                length = int(response.headers.get('Content-Length', '0'))
                require(0 < length <= MAX_ARCHIVE, 'SEC archive length missing or exceeds limit')
                require(shutil.disk_usage(out).free >= length + 1024**3, 'insufficient archive disk headroom')
                digest, count, signature = hashlib.sha256(), 0, b''
                with partial.open('xb') as stream:
                    while block := response.read(1024 * 1024):
                        require(clock() - started < 1800, 'SEC archive download deadline exceeded')
                        count += len(block)
                        require(count <= length, 'SEC archive exceeds declared length')
                        signature = (signature + block[:4])[:4]
                        digest.update(block)
                        stream.write(block)
                require(count == length and signature == b'PK\x03\x04', 'incomplete or invalid SEC ZIP response')
                manifest[kind] = {'file': path.name, 'url': url, 'sha256': digest.hexdigest(),
                    'retrieved_at': datetime.now(timezone.utc).isoformat(), 'size_bytes': count,
                    'last_modified': response.headers.get('Last-Modified'), 'etag': response.headers.get('ETag')}
            partial.replace(path)
        except HTTPError as error:
            # Never emit response bodies, headers, or the private request identity.
            raise ValueError(f'SEC archive request denied or unavailable (HTTP {error.code}); no retry or fallback') from None
        finally:
            partial.unlink(missing_ok=True)
        print(json.dumps({'archive': kind, 'bytes': count, 'sha256': digest.hexdigest(), 'status': 'downloaded'}), flush=True)
        if kind != 'companyfacts':
            time.sleep(1)
    target = out / 'acquisition.json'
    target.write_text(json.dumps(manifest, indent=2) + '\n')
    return target


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    try:
        print(json.dumps({'manifest': str(acquire(args.output)), 'status': 'acquired'}))
    except (ValueError, OSError) as error:
        print(json.dumps({'status': 'stopped', 'error': str(error), 'prior_release_retained': True}))
        raise SystemExit(1)


if __name__ == '__main__':
    main()
