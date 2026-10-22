"""Public Stock Brain web app, with a bounded in-process collection supervisor."""
from datetime import datetime, timedelta, timezone
import gzip
import hashlib
import json
import logging
import os
from pathlib import Path
import signal
import subprocess
import sys
import threading

import runtime_data as data

LOG = logging.getLogger('stock-brain')
ASSETS = {'/': ('index.html', 'text/html'), '/app.mjs': ('app.mjs', 'text/javascript'),
          '/engine.mjs': ('engine.mjs', 'text/javascript'), '/style.css': ('style.css', 'text/css'),
          '/favicon.svg': ('favicon.svg', 'image/svg+xml')}


class Application:
    def __init__(self, root, store, zone='Asia/Jerusalem', clock='08:30', scheduler_enabled=True):
        self.root, self.store = Path(root), store
        self.zone, self.clock, self.scheduler_enabled = zone, clock, scheduler_enabled
        self.lock = threading.Lock()
        self.signature = None
        self.cached = {}
        self._load()

    def _load(self):
        stat = self.store.path.stat()
        signature = (stat.st_ino, stat.st_mtime_ns, stat.st_size)
        with self.lock:
            if signature != self.signature:
                raw = self.store.path.read_bytes()
                bundle = data.validate_bundle(json.loads(raw))
                snapshot = data.encode(bundle['files']['desk.json'])
                self.cached = {'bundle': bundle, 'state': raw, 'snapshot': snapshot,
                               'state_gzip': gzip.compress(raw), 'snapshot_gzip': gzip.compress(snapshot),
                               'generation': hashlib.sha256(raw).hexdigest()}
                self.signature = signature
            return self.cached

    def status(self, cached=None):
        cached = cached or self._load()
        run = cached['bundle']['files']['run-status.json']
        attempt_path = self.store.directory / 'attempt.json'
        attempt = data.p.read_json(attempt_path) if attempt_path.exists() else None
        return {'service': 'stock-brain', 'generation': cached['generation'],
                'built_at': cached['bundle']['files']['desk.json']['built_at'],
                'company_count': len(cached['bundle']['files']['desk.json']['companies']),
                'refresh': run, 'last_attempt': attempt,
                'scheduler': {'enabled': self.scheduler_enabled, 'timezone': self.zone, 'time': self.clock,
                              'next_due': data.next_refresh(datetime.now(timezone.utc), run.get('completed_at'),
                                                            self.zone, self.clock).isoformat()},
                'persistence': 'local checkpoint; GitHub Actions backup; latest backup restored on cold start',
                'model_api_required': False}

    def __call__(self, environ, start_response):
        path, method = environ.get('PATH_INFO', '/'), environ.get('REQUEST_METHOD', 'GET')
        status, mime, raw = '200 OK', 'application/json', b''
        headers = [('X-Content-Type-Options', 'nosniff'), ('Referrer-Policy', 'strict-origin-when-cross-origin'),
                   ('Content-Security-Policy', "default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:; connect-src 'self'; frame-ancestors 'none'; base-uri 'self'; form-action 'self'"),
                   ('Cache-Control', 'no-cache'), ('Vary', 'Accept-Encoding')]
        try:
            if method not in {'GET', 'HEAD'}:
                status, raw = '405 Method Not Allowed', data.encode({'error': 'read_only'})
                headers.append(('Allow', 'GET, HEAD'))
            elif path in ASSETS:
                filename, mime = ASSETS[path]
                raw = (self.root / 'site' / filename).read_bytes()
            elif path in {'/api/snapshot', '/snapshot.json', '/api/state', '/api/status', '/healthz'}:
                cached = self._load()
                if path == '/healthz':
                    raw = data.encode({'status': 'ok', 'service': 'stock-brain'})
                elif path == '/api/status':
                    raw = data.encode(self.status(cached))
                else:
                    key = 'state' if path == '/api/state' else 'snapshot'
                    etag = 'W/"' + hashlib.sha256(cached[key]).hexdigest() + '"'
                    headers.append(('ETag', etag))
                    if environ.get('HTTP_IF_NONE_MATCH') == etag:
                        status = '304 Not Modified'
                    elif 'gzip' in environ.get('HTTP_ACCEPT_ENCODING', ''):
                        raw = cached[key + '_gzip']
                        headers.append(('Content-Encoding', 'gzip'))
                    else:
                        raw = cached[key]
            else:
                status, raw = '404 Not Found', data.encode({'error': 'not_found'})
        except (OSError, ValueError, KeyError, TypeError):
            LOG.exception('Request could not read a valid checkpoint')
            status, raw = '503 Service Unavailable', data.encode({'error': 'data_unavailable'})
        headers.extend([('Content-Type', mime + '; charset=utf-8'), ('Content-Length', str(len(raw)))])
        start_response(status, headers)
        return [b'' if method == 'HEAD' else raw]


class Collector:
    def __init__(self, app, refresh_on_start=True):
        self.app, self.first = app, refresh_on_start
        self.stop_event = threading.Event()
        self.process = None
        self.thread = threading.Thread(target=self.run, name='stock-brain-collector', daemon=True)

    def run(self):
        retry_at = datetime.min.replace(tzinfo=timezone.utc)
        while not self.stop_event.is_set():
            try:
                run = self.app._load()['bundle']['files']['run-status.json']
                now = datetime.now(timezone.utc)
                due = data.next_refresh(now, run.get('completed_at'), self.app.zone, self.app.clock)
                if self.first or (now >= due and now >= retry_at):
                    self.first = False
                    LOG.info('Starting data collection')
                    self.process = subprocess.Popen([sys.executable, str(self.app.root / 'scripts/runtime_data.py'),
                        'refresh', '--root', str(self.app.root), '--state-dir', str(self.app.store.directory)])
                    try:
                        code = self.process.wait(timeout=1200)
                    except subprocess.TimeoutExpired:
                        self.process.kill()
                        self.process.wait()
                        code = -1
                    if code:
                        self.app.store.attempt({'status': 'failed', 'completed_at': datetime.now(timezone.utc).isoformat(),
                                                'previous_data_retained': True})
                        LOG.error('Collection failed; retaining prior checkpoint (exit %s)', code)
                    else:
                        LOG.info('Collection checkpoint committed')
                    retry_at = datetime.now(timezone.utc) + timedelta(hours=1)
                    self.process = None
            except Exception:
                LOG.exception('Collector supervisor failed; retrying later')
                retry_at = datetime.now(timezone.utc) + timedelta(hours=1)
            self.stop_event.wait(30)

    def stop(self):
        self.stop_event.set()
        if self.process is not None and self.process.poll() is None:
            self.process.terminate()
        self.thread.join(timeout=5)


def main():
    from waitress import create_server
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s: %(message)s')
    root = Path(__file__).resolve().parents[1]
    store = data.StateStore(os.environ.get('STOCK_BRAIN_STATE_DIR', str(root / 'build/runtime')))
    data.initialize(root, store, bootstrap=os.environ.get('STOCK_BRAIN_BOOTSTRAP_GITHUB', '0') == '1')
    app = Application(root, store, os.environ.get('STOCK_BRAIN_TIMEZONE', 'Asia/Jerusalem'),
                      os.environ.get('STOCK_BRAIN_REFRESH_TIME', '08:30'),
                      os.environ.get('STOCK_BRAIN_REFRESH_ENABLED', '1') == '1')
    # Validate timezone/time before claiming readiness.
    app.status()
    collector = Collector(app, os.environ.get('STOCK_BRAIN_REFRESH_ON_START', '1') == '1')
    server = create_server(app, host='0.0.0.0', port=int(os.environ.get('PORT', '10000')),
                           threads=4, connection_limit=100, channel_timeout=30, max_request_body_size=8192)
    if app.scheduler_enabled: collector.thread.start()
    def terminate(*_):
        raise SystemExit(0)
    signal.signal(signal.SIGTERM, terminate)
    try:
        LOG.info('Public Stock Brain ready on port %s', os.environ.get('PORT', '10000'))
        server.run()
    finally:
        if app.scheduler_enabled: collector.stop()
        server.close()


if __name__ == '__main__': main()
