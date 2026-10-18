#!/usr/bin/env python3
"""Select an exact reported XBRL fact; never silently mix quarter/YTD or GAAP/adjusted."""
import argparse
import json
from pathlib import Path
import sys

import stock_brain as kb


def select_fact(data, taxonomy, concept, unit, start, end, cutoff, accession=None):
    kb.iso_date(cutoff, "cutoff", required=True)
    kb.iso_date(start, "period start")
    kb.iso_date(end, "period end", required=True)
    kb.need(end <= cutoff and (start is None or start <= end), "invalid period for cutoff")
    facts = data.get("facts", {}).get(taxonomy, {}).get(concept, {}).get("units", {}).get(unit, [])
    matches = [f for f in facts if f.get("start") == start and f.get("end") == end
               and f.get("filed", "9999") <= cutoff and (not accession or f.get("accn") == accession)]
    kb.need(bool(matches), "no exact fact: check taxonomy, concept, currency/unit, period and accession; missing is not zero")
    latest = max(f["filed"] for f in matches)
    matches = [f for f in matches if f["filed"] == latest]
    kb.need(len({f["val"] for f in matches}) == 1, "conflicting values on the latest filing date; resolve the accession explicitly")
    fact = sorted(matches, key=lambda f: (f.get("accn", ""), f.get("form", "")))[-1]
    return {"value": fact["val"], "unit": unit, "taxonomy": taxonomy, "concept": concept,
            "period_start": start, "period_end": end, "filed": fact["filed"],
            "accession": fact.get("accn"), "form": fact.get("form"),
            "basis": "US GAAP" if taxonomy == "us-gaap" else taxonomy,
            "selection": "Latest filed exact-period fact available by cutoff; revisions are retained in raw cache."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument("--taxonomy", default="us-gaap")
    parser.add_argument("--concept", required=True)
    parser.add_argument("--unit", default="USD")
    parser.add_argument("--start")
    parser.add_argument("--end", required=True)
    parser.add_argument("--as-of", required=True)
    parser.add_argument("--accession")
    args = parser.parse_args()
    try:
        result = select_fact(json.loads(args.path.read_text()), args.taxonomy, args.concept, args.unit,
                             args.start, args.end, args.as_of, args.accession)
        print(json.dumps(result, indent=2))
        return 0
    except (OSError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
