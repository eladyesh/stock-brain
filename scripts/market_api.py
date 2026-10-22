"""Read-only, bounded security directory routes and explicit dataset gaps."""
import re
import sqlite3
from urllib.parse import parse_qs, urlencode

import coverage_api
import market_directory as directory


def serve_market(store, path, query_string=''):
    if path != '/api/securities' and not path.startswith('/api/securities/'):
        return None
    if store is None:
        return '503 Service Unavailable', {'error': 'directory_unavailable'}
    try:
        if len(query_string) > 4096 or re.search(r'%(?![0-9A-Fa-f]{2})', query_string):
            raise ValueError('invalid query')
        params = parse_qs(query_string, keep_blank_values=True, max_num_fields=8, errors='strict')
        if any(len(v) != 1 for v in params.values()): raise ValueError('duplicate parameter')
        if path == '/api/securities':
            if set(params) - {'q', 'limit', 'offset', 'instrument', 'exchange', 'status'}: raise ValueError('unknown parameter')
            q, limit, offset = coverage_api._query(urlencode({k: v[0] for k, v in params.items() if k in {'q', 'limit', 'offset'}}), listing=True)
            exchange = params.get('exchange', [''])[0]
            if exchange and not re.fullmatch(r'[A-Z_]{1,40}', exchange): raise ValueError('invalid exchange')
            page = directory.list_securities(store, query=q, limit=limit, offset=offset,
                instrument=params.get('instrument', ['equities'])[0], exchange=exchange, status=params.get('status', ['present'])[0])
            return '200 OK', {**page, 'directory': directory.directory_status(store)}
        if params: raise ValueError('detail has no parameters')
        key = path.removeprefix('/api/securities/')
        if not re.fullmatch(r'[0-9a-f]{32}', key): return '404 Not Found', {'error': 'security_not_found'}
        security = directory.security_detail(store, key)
        if security is None: return '404 Not Found', {'error': 'security_not_found'}
        return '200 OK', {'security': security,
                         'company_detail_path': '/api/companies/' + security['cik'] if security['cik'] else None,
                         'scope_note': 'Listing identity is separate from issuer identity, collected datasets and reviewed research.'}
    except (ValueError, UnicodeError):
        return '400 Bad Request', {'error': 'invalid_query'}
    except (sqlite3.Error, OSError):
        return '503 Service Unavailable', {'error': 'directory_unavailable'}
