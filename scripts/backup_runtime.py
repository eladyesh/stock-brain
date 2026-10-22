"""Back up a public Render checkpoint using GitHub Actions' own Git credentials."""
import argparse
from datetime import datetime
import json
import os
from pathlib import Path
import subprocess
import tempfile
from urllib.parse import urlsplit

import runtime_data as data


def git(*args, cwd=None):
    return subprocess.run(['git', *args], cwd=cwd, check=True, text=True, capture_output=True).stdout.strip()


def newer(incoming, existing):
    new_run = datetime.fromisoformat(incoming['run-status.json']['completed_at'])
    old_run = datetime.fromisoformat(existing['run-status.json']['completed_at'])
    if new_run != old_run:
        return new_run > old_run
    return datetime.fromisoformat(incoming['desk.json']['built_at']) > datetime.fromisoformat(existing['desk.json']['built_at'])


def backup(root, base_url):
    parsed = urlsplit(base_url)
    data.kb.need(parsed.scheme == 'https' and bool(parsed.hostname) and not parsed.username and not parsed.password,
                 'a public HTTPS app URL is required')
    branch = 'automation/research-data'
    git('fetch', '--no-tags', 'origin', 'refs/heads/' + branch, cwd=root)
    parent = git('rev-parse', 'FETCH_HEAD', cwd=root)
    existing = {name: json.loads(git('show', parent + ':' + name, cwd=root)) for name in data.FILES}
    status = data.fetch_json(base_url.rstrip('/') + '/api/status')
    data.kb.need(status.get('service') == 'stock-brain', 'URL is not a Stock Brain application')
    remote_run = status.get('refresh', {}).get('completed_at')
    # Fetch the bundle only when it can contain a new data run or research build.
    if remote_run and datetime.fromisoformat(remote_run) < datetime.fromisoformat(existing['run-status.json']['completed_at']):
        return {'result': 'skipped_older_server'}
    if remote_run == existing['run-status.json']['completed_at'] and status.get('built_at') == existing['desk.json']['built_at']:
        return {'result': 'unchanged'}
    bundle = data.validate_bundle(data.fetch_json(base_url.rstrip('/') + '/api/state'))
    if not newer(bundle['files'], existing):
        return {'result': 'unchanged'}
    with tempfile.TemporaryDirectory(prefix='stock-brain-backup-') as directory:
        scratch = Path(directory)
        store = data.StateStore(scratch / 'validation')
        with data.workspace(root, store, bundle) as working:
            data.kb.export_records(working)
        checkout = scratch / 'data'
        git('worktree', 'add', '--detach', str(checkout), parent, cwd=root)
        try:
            data.kb.need(set(git('ls-tree', '--name-only', 'HEAD', cwd=checkout).splitlines()) == set(data.FILES),
                         'data branch contains unexpected files')
            for name in data.FILES:
                (checkout / name).write_bytes(data.encode(bundle['files'][name]))
            git('add', '--', *data.FILES, cwd=checkout)
            if not git('diff', '--cached', '--name-only', cwd=checkout):
                return {'result': 'unchanged'}
            git('-c', 'user.name=github-actions[bot]', '-c', 'user.email=41898282+github-actions[bot]@users.noreply.github.com',
                'commit', '-m', 'Back up standalone Stock Brain data ' + bundle['files']['run-status.json']['cutoff'], cwd=checkout)
            commit = git('rev-parse', 'HEAD', cwd=checkout)
            # Normal fast-forward push rejects a competing writer. Never force.
            git('push', 'origin', 'HEAD:refs/heads/' + branch, cwd=checkout)
            actual = git('ls-remote', 'origin', 'refs/heads/' + branch, cwd=checkout).split()[0]
            data.kb.need(actual == commit, 'backup ref readback mismatch')
            return {'result': 'persisted', 'commit': commit}
        finally:
            git('worktree', 'remove', '--force', str(checkout), cwd=root)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--url', default=os.environ.get('STOCK_BRAIN_URL', 'https://finlotus-1.onrender.com'))
    args = parser.parse_args()
    print(json.dumps(backup(data.kb.ROOT, args.url)))
