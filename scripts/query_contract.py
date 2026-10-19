"""Match numeric questions to explicit metric, period, basis and issuer evidence.

This gate never substitutes a whole-year figure for a quarter or computes a
missing measure from a nearby narrative. Unknown qualifiers fail closed.
"""
from datetime import date
import calendar
import json
import re

METRICS = {
    "gross_margin": (r"gross margin|שיעור (?:ה)?רווח (?:ה)?גולמי|רווחיות גולמית", r"gross margin"),
    "gross_profit": (r"gross profit|רווח (?:ה)?גולמי", r"gross profit"),
    "operating_margin": (r"operating margin|שיעור (?:ה)?רווח (?:ה)?תפעולי", r"operating margin"),
    "net_margin": (r"net margin|שיעור (?:ה)?רווח (?:ה)?נקי", r"net margin"),
    "free_cash_flow": (r"free cash flow|\bfcf\b|תזרים (?:ה)?מזומנים (?:ה)?חופשי", r"free cash flow"),
    "operating_cash_flow": (r"operating cash flow|cash (?:from|provided by) operations|\bocf\b|תזרים.*(?:מפעילות שוטפת|תפעולי)", r"operating cash flow"),
    "capex": (r"capex|capital expenditures|השקעות הוניות", r"capital expenditures|additions to property"),
    "sbc": (r"stock.based compensation|\bsbc\b|תגמול מבוסס מניות", r"stock.based compensation"),
    "eps": (r"\beps\b|earnings per share|רווח (?:ה)?(?:מדולל )?למניה", r"eps"),
    "ebitda": (r"\bebitda\b", r"ebitda"),
    "revenue_growth": (r"revenue growth|צמיחת (?:ה)?הכנסות|שיעור צמיחה", r"revenue growth"),
    "revenue": (r"\brevenue\b|\bsales\b|הכנסות|מכירות", r"revenue|sales"),
    "operating_income": (r"operating (?:income|profit)|רווח (?:ה)?תפעולי", r"operating income|operating profit"),
    "net_income": (r"net (?:income|earnings|profit)|gaap loss|\bprofit(?:able)?\b|רווח (?:ה)?נקי|הפסד", r"net income|net earnings"),
    "cash": (r"\bcash\b|מזומנים|מזומן", r"^cash"),
    "debt": (r"\bdebt\b|חוב", r"debt"),
}
QUARTER_WORDS = {1: "first|1st|ראשון", 2: "second|2nd|שני", 3: "third|3rd|שלישי", 4: "fourth|4th|רביעי"}


def parse(question):
    q = question.casefold()
    remainder = q
    metrics = []
    for key, (pattern, _) in METRICS.items():
        if re.search(pattern, remainder):
            metrics.append(key)
            remainder = re.sub(pattern, " ", remainder)
    # Earnings alone is broad; a question about a date is not a numeric question.
    if re.search(r"\bearnings\b", remainder) and not re.search(r"date|release|next results", q):
        metrics.append("net_income")
    quarters = set(int(n) for n in re.findall(r"\bq([1-4])\b", q) if n)
    for number, words in QUARTER_WORDS.items():
        if re.search(r"(?:" + words + r")[- ]quarter|quarter\s*" + str(number) + r"|רבעון\s+(?:(?:ה)?(?:קלנדרי|פיסקלי)\s+)?(?:ה)?(?:" + words + r")|רבעון\s*" + str(number), q):
            quarters.add(number)
    explicit_fiscal = bool(re.search(r"\bfy\s*\d{4}|fiscal|שנת (?:ה)?כספים|פיסקלי", q))
    explicit_calendar = bool(re.search(r"\bcalendar\b|\bcy\s*\d{4}|קלנדרי|אזרחי", q))
    years = set(int(y) for y in re.findall(r"(?<!\d)(?:19|20)\d{2}(?!\d)", q))
    non_gaap = bool(re.search(r"non[ -]?gaap|adjusted|מתואמ", q))
    gaap = bool(re.search(r"(?<!non-)(?<!non )\bgaap\b", q))
    basis = None if gaap and non_gaap else "non-GAAP" if non_gaap else "GAAP" if gaap else None
    qualifier = None
    if re.search(r"\broic\b|\broe\b|\broa\b|ebit margin|return on (?:capital|equity|assets)|תשואה על (?:ההון|נכסים)", q):
        qualifier = "unsupported_metric"
    if re.search(r"excluding|except for|without|ללא|בניכוי|למעט", q):
        qualifier = "unsupported_qualifier"
    if metrics and re.search(r"per employee|per customer|per user|לעובד|ללקוח|למשתמש|inflation.adjusted|constant.currency|במטבע קבוע|בנטרול", q):
        qualifier = "unsupported_qualifier"
    if metrics and re.search(r"azure|copilot|data cent(?:er|re)|aws|cloud revenue|revenue.*cloud|הכנסות.*ענן|הכנסות.*אזור|הכנסות.*(?:סין|ארה״ב)", q):
        qualifier = "unsupported_qualifier"
    # Relative/rolling periods need their own sourced calculation. They must
    # never fall through to a nearby annual or quarterly narrative claim.
    relative_period = bool(re.search(
        r"\b(?:ttm|ltm|ytd)\b|(?:last|past|trailing)\s+(?:12|twelve)\s+months|"
        r"(?:last|past|trailing)\s+(?:4|four)\s+quarters|year.to.date|"
        r"(?:last|previous|next|current)\s+(?:fiscal\s+)?(?:year|quarter)|"
        r"(?:12|שנים[ -]עשר)\s+(?:ה)?חודשים|ארבעת\s+(?:ה)?רבעונים|"
        r"מתחילת השנה|השנה שעברה|בשנה שעברה|השנה הנוכחית|הרבעון (?:הקודם|הנוכחי|הבא)|"
        r"\bh[12]\b|(?:first|second) half|מחצית|\bq(?:[05-9]|\d{2,})\b|"
        r"\b(?:january|february|march|april|may|june|july|august|september|october|november|december)\b|"
        r"ינואר|פברואר|מרץ|אפריל|יוני|יולי|אוגוסט|ספטמבר|אוקטובר|נובמבר|דצמבר", q))
    period_error = "unsupported_period" if relative_period or (explicit_fiscal and explicit_calendar) or (quarters and not years) else None
    return {"metrics": metrics, "years": sorted(years), "quarters": sorted(quarters),
            "fiscal": explicit_fiscal, "annual": bool(years and not quarters), "basis": basis, "both_bases": gaap and non_gaap,
            "calendar": explicit_calendar, "period_error": period_error,
            "guidance": bool(re.search(r"guidance|outlook|forecast|תחזית|צפי", q)),
            "comparison": bool(re.search(r"\bcompare|versus|\bvs\b|השוו|השוה|השוואה|לעומת", q)),
            "qualifier_error": qualifier}


def period_identity(metric, claim, context=None):
    """Only use explicit claim/locator fiscal labels, never a calendar-quarter guess."""
    start, end = metric.get("period_start"), metric.get("period_end")
    days = (date.fromisoformat(end) - date.fromisoformat(start)).days + 1 if start and end else None
    text = claim["text"] + " " + metric.get("locator", "")
    pairs = re.findall(r"(?:fiscal\s+)?Q([1-4])\s*(?:FY\s*)?((?:19|20)\d{2})", text, re.I)
    pairs += [(q, y) for y, q in re.findall(r"FY\s*((?:19|20)\d{2})\s+Q([1-4])", text, re.I)]
    for number, words in QUARTER_WORDS.items():
        pairs += [(str(number), year) for year in re.findall(r"fiscal\s*((?:19|20)\d{2})\s+(?:" + words + r")[ -]quarter", text, re.I)]
    fiscal_years = set(int(y) for y in re.findall(r"(?:FY|fiscal(?: year)?|full[ -]year)\s*((?:19|20)\d{2})", text, re.I))
    # Some releases say "fiscal Q4 ended September 3, 2026" then state FY2026.
    bare_quarters = set(int(n) for n in re.findall(r"fiscal Q([1-4])\b", text, re.I))
    if not pairs and len(bare_quarters) == 1 and len(fiscal_years) == 1:
        pairs = [(str(next(iter(bare_quarters))), str(next(iter(fiscal_years))))]
    if days is not None and 330 <= days <= 380:
        end_year = date.fromisoformat(end).year
        return {"type": "annual", "year": end_year if end_year in fiscal_years else None, "quarter": None}
    if days is not None and 70 <= days <= 105:
        unique = {(int(q), int(y)) for q, y in pairs}
        if len(unique) == 1:
            quarter, year = next(iter(unique))
            if "prior-year" in metric.get("name", "").lower():
                year -= 1
            return {"type": "quarterly", "year": year, "quarter": quarter}
        # A fiscal label elsewhere in the reviewed packet can identify the exact
        # same company duration. It cannot identify a nearby or prior-year date.
        shared = (context or {}).get((start, end), set())
        if not unique and len(shared) == 1:
            quarter, year = next(iter(shared))
            return {"type": "quarterly", "year": year, "quarter": quarter}
    return {"type": "instant" if days is None else "duration", "year": date.fromisoformat(end).year if end else None, "quarter": None}


def metric_matches(metric, key):
    name = metric["name"].casefold()
    if key == "revenue" and ("growth" in name or "guidance" in name):
        return "guidance" in name and "revenue" in name
    return bool(re.search(METRICS[key][1], name))


def period_context(packet):
    claims = {c['id']: c for section in packet['sections'].values() for c in section.get('claims', [])}
    result = {}
    for metric in packet.get('metrics', []):
        identity = period_identity(metric, claims[metric['claim_id']])
        if identity['type'] == 'quarterly' and identity['year'] is not None:
            result.setdefault((metric.get('period_start'), metric.get('period_end')), set()).add((identity['quarter'], identity['year']))
    return result


def match_identity(identity, start, end, request):
    """Exact fiscal identity, or exact calendar boundaries for unqualified years."""
    if request.get("period_error"):
        return False
    if request["quarters"] and identity["type"] != "quarterly":
        return False
    if request["annual"] and identity["type"] != "annual":
        return False
    if request["years"] and not request["fiscal"]:
        year = request["years"][0]
        quarter = request["quarters"][0] if request["quarters"] else None
        first_month = (quarter - 1) * 3 + 1 if quarter else 1
        last_month = first_month + 2 if quarter else 12
        expected_start = date(year, first_month, 1).isoformat()
        expected_end = date(year, last_month, calendar.monthrange(year, last_month)[1]).isoformat()
        if (start, end) != (expected_start, expected_end):
            return False
    else:
        if request["quarters"] and identity["quarter"] not in request["quarters"]:
            return False
        if request["years"] and identity["year"] not in request["years"]:
            return False
    return True


def match_period(metric, claim, request, context=None):
    identity = period_identity(metric, claim, context)
    if not match_identity(identity, metric.get("period_start"), metric.get("period_end"), request):
        return False
    if request["basis"] and metric.get("basis") != request["basis"]:
        return False
    guided = claim.get("kind") == "management_guidance"
    return guided == request["guidance"]


def constrain(question, candidates, entities, hints, root):
    """Return eligible records, explicit claim allowlists, and a refusal if incomplete."""
    request = parse(question)
    financial = bool(request["metrics"] or request["qualifier_error"] or set(hints) & {"financial-performance", "balance-sheet-and-capital-allocation"})
    descriptive = bool(set(hints) & {"business-overview", "revenue-model-and-segments", "products-and-services", "growth-drivers", "catalysts"}) and not re.search(r"how much|how many|what was|what were|כמה|מה היו|שיעור|\b(?:FY|Q[1-4])", question, re.I)
    if not financial or descriptive:
        return candidates, {}, None
    if request["qualifier_error"]:
        return [], {}, {"code": request["qualifier_error"], "missing": []}
    if request["period_error"]:
        return [], {}, {"code": request["period_error"], "missing": []}
    if len(request["quarters"]) > 1 or len(request["years"]) > 1:
        return [], {}, {"code": "unsupported_period", "missing": []}
    # Broad financial summaries without a metric or period use their whole reviewed section.
    if not request["metrics"] and not request["years"] and not request["quarters"] and not request["basis"]:
        return candidates, {}, None
    allowed, matched_sections, missing = {}, {}, []
    tickers = sorted({r["ticker"] for r in candidates if r.get("ticker")})
    for ticker in tickers:
        path = root / "research/pilot" / (ticker + ".json")
        if not path.exists():
            missing.append({"ticker": ticker, "reason": "missing_metric_packet"})
            continue
        packet = json.loads(path.read_text())
        context = period_context(packet)
        claims = {c["id"]: (section, c) for section, data in packet["sections"].items() for c in data.get("claims", [])}
        keys = request["metrics"] or [None]
        selected = set()
        for key in keys:
            matching = [m for m in packet.get("metrics", []) if m.get("claim_id") in claims
                        and (key is None or metric_matches(m, key))
                        and match_period(m, claims[m["claim_id"]][1], request, context)]
            if request['both_bases'] and len(keys) == 1 and not {'GAAP', 'non-GAAP'} <= {m.get('basis') for m in matching}:
                matching = []
            if not matching:
                missing.append({"ticker": ticker, "metric": key, "reason": "unsupported_metric_or_period"})
            selected.update(m["claim_id"] for m in matching)
        allowed[ticker] = sorted(selected)
        matched_sections[ticker] = {claims[c][0] for c in selected}
    if missing:
        code = "unsupported_period" if request["years"] or request["quarters"] else "unsupported_metric"
        return [], {}, {"code": code, "missing": missing}
    eligible = [r for r in candidates if r.get("section_id") in matched_sections.get(r.get("ticker"), set())]
    return eligible, allowed, None
