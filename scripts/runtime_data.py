"""Standalone collection and atomic checkpoints; no ChatGPT or model API calls."""
import argparse
from contextlib import contextmanager
from datetime import datetime, timedelta, timezone
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import tempfile
import urllib.request
from zoneinfo import ZoneInfo

import build_desk
import refresh_desk
import research_pipeline as p
import stock_brain as kb

FILES = ('desk.json', 'latest.json', 'triage.json', 'run-status.json')
MAX_BYTES = 40 * 1024 * 1024
REPOSITORY = 'eladyesh/stock-brain'


def encode(value):
    return (json.dumps(value, ensure_ascii=False, allow_nan=False, separators=(',', ':')) + '\n').encode()


def validate_bundle(bundle):
    kb.need(bundle.get('schema_version') == 1 and set(bundle.get('files', {})) == set(FILES),
            'incomplete checkpoint')
    files = bundle['files']
    desk = files['desk.json']
    kb.need(desk.get('schema_version') == 1 and desk.get('answer_contract_version') == 2,
            'incompatible answer contract')
    kb.need(isinstance(desk.get('companies'), list) and bool(desk['companies']), 'missing companies')
    tickers = [c['ticker'] for c in desk['companies']]
    kb.need(len(set(tickers)) == len(tickers), 'duplicate companies')
    kb.need(all(isinstance(c.get('historical_index'), list) for c in desk['companies']), 'missing history index')
    kb.need(isinstance(files['latest.json'].get('queue'), list), 'missing disclosure queue')
    kb.need(isinstance(files['triage.json'].get('reviews'), list), 'missing review history')
    kb.need(files['run-status.json'].get('status') in {'partial', 'complete'}, 'invalid refresh outcome')
    kb.need(desk.get('refresh_status') == files['run-status.json'], 'mixed checkpoint generations')
    kb.need(desk.get('queue') == files['latest.json']['queue'], 'mixed disclosure generations')
    kb.need(desk.get('triage') == files['triage.json'], 'mixed triage generations')
    for value in [desk['built_at'], files['run-status.json']['completed_at']]:
        kb.need(datetime.fromisoformat(value).tzinfo is not None, 'checkpoint timestamps require timezone')
    return bundle


def fetch_json(url):
    request = urllib.request.Request(url, headers={'User-Agent': refresh_desk.USER_AGENT,
                                                   'Accept': 'application/json'})
    with urllib.request.urlopen(request, timeout=45) as response:
        raw = response.read(MAX_BYTES + 1)
    kb.need(len(raw) <= MAX_BYTES, 'checkpoint exceeds size limit')
    return json.loads(raw)


def github_checkpoint():
    # Resolve once, then read immutable paths to avoid mixing concurrent commits.
    ref = fetch_json('https://api.github.com/repos/' + REPOSITORY + '/git/ref/heads/automation/research-data')
    sha = ref['object']['sha']
    kb.need(bool(re.fullmatch(r'[0-9a-f]{40}', sha)), 'invalid GitHub checkpoint revision')
    base = 'https://raw.githubusercontent.com/' + REPOSITORY + '/' + sha + '/'
    return validate_bundle({'schema_version': 1, 'files': {name: fetch_json(base + name) for name in FILES}})


class StateStore:
    def __init__(self, directory):
        self.directory = Path(directory).resolve()
        self.directory.mkdir(parents=True, exist_ok=True)
        self.path = self.directory / 'state.json'

    @contextmanager
    def writer(self):
        with (self.directory / 'writer.lock').open('a') as lock:
            fcntl.flock(lock, fcntl.LOCK_EX)
            yield

    def read(self):
        return validate_bundle(p.read_json(self.path)) if self.path.exists() else None

    def commit(self, bundle):
        raw = encode(validate_bundle(bundle))
        # One rename publishes all four payloads together. Readers see old or new.
        fd, temporary = tempfile.mkstemp(prefix='checkpoint-', dir=self.directory)
        try:
            with os.fdopen(fd, 'wb') as handle:
                handle.write(raw)
                handle.flush()
                os.fsync(handle.fileno())
            os.replace(temporary, self.path)
        finally:
            if os.path.exists(temporary): os.unlink(temporary)
        return hashlib.sha256(raw).hexdigest()

    def attempt(self, value):
        p.write_json(self.directory / 'attempt.json', value)


@contextmanager
def workspace(root, store, saved):
    with tempfile.TemporaryDirectory(prefix='collection-', dir=store.directory) as directory:
        working = Path(directory)
        for name in ['config', 'research', 'sectors', 'data', 'templates']:
            shutil.copytree(root / name, working / name)
        if saved:
            refresh_desk.restore_payloads(working, saved['files'])
        yield working


def checkpoint_from_root(root):
    desk = build_desk.build(root)
    return {'schema_version': 1, 'files': {
        'desk.json': desk,
        'latest.json': p.read_json(root / 'research/monitoring/latest.json'),
        'triage.json': p.read_json(root / 'research/monitoring/triage.json'),
        'run-status.json': p.read_json(root / 'research/monitoring/refresh-status.json')}}


def initialize(root, store, bootstrap=False):
    with store.writer():
        saved = store.read()
        if saved is None and bootstrap:
            saved = github_checkpoint()  # An expected checkpoint must not silently become an empty queue.
        with workspace(root, store, saved) as working:
            # Rebuild against this release's reviewed research, retaining dated data.
            return store.commit(checkpoint_from_root(working))


def collect(root, store):
    started = datetime.now(timezone.utc).isoformat()
    with store.writer():
        store.attempt({'status': 'running', 'started_at': started})
        try:
            saved = store.read()
            kb.need(saved is not None, 'initialize checkpoint before collection')
            with workspace(root, store, saved) as working:
                output = working / 'build/publish'
                run = refresh_desk.refresh(working, output, saved['files']['run-status.json'])
                manifest = p.read_json(output / 'publish-manifest.json')
                kb.need(manifest.get('publication_safe'), 'unsafe collection')
                for entry in manifest['files']:
                    kb.need(entry['path'] in FILES, 'unexpected publication file')
                    kb.need(p.digest((output / entry['path']).read_bytes()) == entry['sha256'], 'payload hash mismatch')
                bundle = {'schema_version': 1, 'files': {name: p.read_json(output / name) for name in FILES}}
                generation = store.commit(bundle)
            store.attempt({'status': run['status'], 'started_at': started,
                           'completed_at': run['completed_at'], 'generation': generation})
            return run
        except Exception:
            store.attempt({'status': 'failed', 'started_at': started,
                           'completed_at': datetime.now(timezone.utc).isoformat(),
                           'previous_data_retained': True})
            raise


def next_refresh(now, completed_at, zone='Asia/Jerusalem', clock='08:30'):
    local = now.astimezone(ZoneInfo(zone))
    hour, minute = map(int, clock.split(':'))
    target = local.replace(hour=hour, minute=minute, second=0, microsecond=0)
    completed = datetime.fromisoformat(completed_at).astimezone(ZoneInfo(zone)) if completed_at else None
    if completed and completed.date() >= local.date():
        target += timedelta(days=1)
    return max(now, target).astimezone(timezone.utc)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['initialize', 'refresh'])
    parser.add_argument('--root', type=Path, default=kb.ROOT)
    parser.add_argument('--state-dir', type=Path, default=Path(os.environ.get('STOCK_BRAIN_STATE_DIR', 'build/runtime')))
    parser.add_argument('--bootstrap-github', action='store_true')
    args = parser.parse_args()
    store = StateStore(args.state_dir)
    if args.command == 'initialize':
        print(json.dumps({'generation': initialize(args.root, store, args.bootstrap_github)}))
    else:
        result = collect(args.root, store)
        print(json.dumps({'status': result['status'], 'pending_count': result['pending_count']}))


if __name__ == '__main__': main()
