#!/usr/bin/env python3
"""Local-only research interface; no external services or credentials required."""
import argparse
from functools import partial
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
from urllib.parse import urlsplit

import answering
import research_pipeline as pipeline
import stock_brain as kb

WEB = Path(__file__).resolve().parents[1] / 'web'


class Handler(BaseHTTPRequestHandler):
    def __init__(self, *args, root=kb.ROOT, **kwargs):
        self.root = root
        super().__init__(*args, **kwargs)

    def send(self, status, body, content_type='application/json; charset=utf-8'):
        raw = body.encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', str(len(raw)))
        self.send_header('Cache-Control', 'no-store')
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('Content-Security-Policy', "default-src 'self'; script-src 'self'; style-src 'self'; connect-src 'self'; frame-ancestors 'none'; base-uri 'none'")
        self.end_headers()
        self.wfile.write(raw)

    def do_GET(self):
        path = urlsplit(self.path).path
        if path in {'/', '/app.js', '/style.css'}:
            name = {'/': 'index.html', '/app.js': 'app.js', '/style.css': 'style.css'}[path]
            mime = {'/': 'text/html', '/app.js': 'text/javascript', '/style.css': 'text/css'}[path]
            return self.send(200, (WEB / name).read_text(), mime + '; charset=utf-8')
        if path == '/api/status':
            report_path = self.root / 'build/monitoring/latest.json'
            if not report_path.exists():
                report_path = self.root / 'research/monitoring/latest.json'
            report = pipeline.read_json(report_path) if report_path.exists() else None
            docs = kb.documents(self.root)
            from review_gates import check_managed_reviews
            check_managed_reviews(self.root, docs)
            data = {'companies': [{'ticker': d.metadata['ticker'], 'status': d.metadata['status'],
                                  'as_of': d.metadata.get('as_of'), 'freshness': answering.disclosure_monitor.freshness(self.root, d.metadata['ticker'], report)} for d in docs],
                    'queue': [e for e in (report or {}).get('queue', []) if e['status'] == 'pending_review']}
            return self.send(200, json.dumps(data, ensure_ascii=False))
        self.send(404, '{"error":"not_found"}')

    def do_POST(self):
        if self.path != '/api/ask':
            return self.send(404, '{"error":"not_found"}')
        # No cross-origin browser clients or form submissions; this is a localhost tool.
        origin = self.headers.get('Origin')
        if origin and origin != 'http://' + self.headers.get('Host', ''):
            return self.send(403, '{"error":"origin_not_allowed"}')
        if self.headers.get('Content-Type', '').split(';')[0] != 'application/json':
            return self.send(415, '{"error":"json_required"}')
        try:
            size = int(self.headers.get('Content-Length', '0'))
            if not 1 <= size <= 20000:
                return self.send(413, '{"error":"invalid_size"}')
            payload = json.loads(self.rfile.read(size))
            if not isinstance(payload, dict) or not isinstance(payload.get('question'), str):
                return self.send(400, '{"error":"question_required"}')
            output = answering.answer(payload['question'], self.root, payload.get('language', 'auto'))
            self.send(200, json.dumps(output, ensure_ascii=False))
        except (ValueError, KeyError, TypeError, OSError):
            self.send(400, json.dumps({'error': 'הבקשה או הראיות אינן תקינות. יש לבדוק את המאגר.'}, ensure_ascii=False))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port', type=int, default=8765)
    parser.add_argument('--root', type=Path, default=kb.ROOT)
    args = parser.parse_args()
    server = ThreadingHTTPServer(('127.0.0.1', args.port), partial(Handler, root=args.root.resolve()))
    print(f'Stock Brain: http://127.0.0.1:{server.server_port}', flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == '__main__':
    main()
