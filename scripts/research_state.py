"""Durable generated research queue, published with a checked Git lease."""
import argparse
import base64
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

import brain_markdown as brain
from coverage_store import require
import research_queue as queue


def sync(directory, publish=False):
    directory = Path(directory)
    token = os.environ.get('GH_TOKEN')
    require(bool(token), 'GH_TOKEN is required for research state continuity')
    env = dict(os.environ, GIT_TERMINAL_PROMPT='0', GIT_CONFIG_COUNT='1',
        GIT_CONFIG_KEY_0='http.https://github.com/.extraheader',
        GIT_CONFIG_VALUE_0='AUTHORIZATION: basic ' + base64.b64encode(('x-access-token:' + token).encode()).decode())
    lease_file = directory.parent / (directory.name + '.parent')
    if publish:
        queue.load_state(directory)
        require(lease_file.exists(), 'research state must be restored before publishing')
    with tempfile.TemporaryDirectory() as temporary:
        target = Path(temporary)
        def git(*args, allowed=(0,)):
            result = subprocess.run(['git', *args], cwd=target, env=env, capture_output=True, text=True, timeout=600)
            require(result.returncode in allowed, 'research state Git operation failed: ' + args[0])
            return result
        git('init', '-q')
        git('remote', 'add', 'origin', f'https://github.com/{brain.REPO}.git')
        # ls-remote patterns also match trailing path components: a short
        # research-data pattern would match automation/research-data.
        branch_ref = 'refs/heads/' + queue.BRANCH
        found = git('ls-remote', '--exit-code', '--heads', 'origin', branch_ref, allowed=(0, 2))
        parent = found.stdout.split()[0] if found.returncode == 0 else ''
        if parent:
            git('fetch', '--depth=1', 'origin', branch_ref)
            git('checkout', '-q', '-b', queue.BRANCH, 'FETCH_HEAD')
            require(git('rev-parse', 'HEAD').stdout.strip() == parent, 'research branch moved during restore')
            queue.load_state(target)
            files = git('ls-files').stdout.splitlines()
            require(all(f == 'state.json' or __import__('re').fullmatch(r'reports/[0-9]{10}\.json', f) for f in files),
                    'unexpected research files; preserve manual changes')
        else:
            git('checkout', '--orphan', queue.BRANCH)
        if not publish:
            require(not directory.exists() or not any(directory.iterdir()), 'restore requires an empty state directory')
            directory.mkdir(parents=True, exist_ok=True)
            if parent:
                shutil.copy2(target / 'state.json', directory / 'state.json')
                if (target / 'reports').exists():
                    shutil.copytree(target / 'reports', directory / 'reports')
            lease_file.write_text(parent)
            return parent
        require(lease_file.read_text() == parent, 'research branch changed; regenerate from current state')
        previous = queue.load_state(target)
        incoming = queue.load_state(directory)
        require(set(previous['reports']) <= set(incoming['reports']), 'research report history cannot disappear')
        shutil.copy2(directory / 'state.json', target / 'state.json')
        if (directory / 'reports').exists():
            shutil.copytree(directory / 'reports', target / 'reports', dirs_exist_ok=True)
        queue.load_state(target)
        git('add', '--all')
        if git('diff', '--cached', '--quiet', allowed=(0, 1)).returncode:
            git('-c', 'user.name=github-actions[bot]', '-c', 'user.email=41898282+github-actions[bot]@users.noreply.github.com',
                'commit', '-qm', 'Checkpoint daily issuer research queue')
            git('push', 'origin', 'HEAD:refs/heads/' + queue.BRANCH)
        commit = git('rev-parse', 'HEAD').stdout.strip()
        require(git('ls-remote', '--exit-code', '--heads', 'origin', branch_ref).stdout.split()[0] == commit, 'research state ref differs')
        return commit


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['restore', 'publish'])
    parser.add_argument('--state', type=Path, default=Path('build/research-state'))
    args = parser.parse_args()
    print(sync(args.state, args.command == 'publish'))
