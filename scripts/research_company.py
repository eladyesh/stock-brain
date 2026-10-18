#!/usr/bin/env python3
"""Collect, prepare, draft, review, and audit a source-backed research job."""
import argparse
from datetime import date
import json
import os
from pathlib import Path
import sys
import subprocess
import time

import research_pipeline as pipeline
import stock_brain as kb


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=kb.ROOT)
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("collect", "prepare", "run"):
        p = commands.add_parser(name)
        p.add_argument("--ticker", required=True)
        if name in {"collect", "run"}:
            p.add_argument("--as-of", default=date.today().isoformat())
            p.add_argument("--max-events", type=int, default=3)
        if name in {"prepare", "run"}:
            p.add_argument("--max-chars", type=int, default=100000)
        if name == "run":
            p.add_argument("--runner", type=Path, help="Explicit JSON config with model program argv; omit to prepare only")
            p.add_argument("--apply", action="store_true")
            p.add_argument("--force", action="store_true", help="Prepare or rerun even when collected disclosures are unchanged")
    draft = commands.add_parser("draft")
    draft.add_argument("--packet", type=Path, required=True)
    draft.add_argument("--apply", action="store_true")
    review = commands.add_parser("review")
    review.add_argument("--packet", type=Path, required=True)
    review.add_argument("--attestation", type=Path, required=True)
    commands.add_parser("audit")
    batch = commands.add_parser("batch")
    batch.add_argument("--group", required=True, help="A universe cohort such as software")
    batch.add_argument("--limit", type=int, default=5)
    batch.add_argument("--as-of", default=date.today().isoformat())
    args = parser.parse_args()
    root = args.root.resolve()
    started = time.monotonic()
    try:
        if args.command == "audit":
            result = pipeline.audit(root)
        elif args.command == "draft":
            packet = pipeline.read_json(args.packet)
            path = pipeline.apply_packet(root, packet, args.apply)
            if args.apply:
                kb.build(root)
            result = {"path": str(path), "status": "draft", "metrics": pipeline.computed_metrics(packet)}
        elif args.command == "review":
            path = pipeline.review_packet(root, args.packet, args.attestation)
            kb.build(root)
            result = {"path": str(path), "status": "reviewed"}
        elif args.command == "batch":
            kb.need(1 <= args.limit <= 5, "batch limit must be between one and five")
            chosen = [c for c in pipeline.universe(root) if c["group"] == args.group][:args.limit]
            kb.need(bool(chosen), "empty batch: unknown group")
            result = {"jobs": []}
            for company in chosen:
                try:
                    manifest = pipeline.collect(root, company, args.as_of, os.environ.get("SEC_USER_AGENT", ""))
                    request = pipeline.prepare_request(root, company["ticker"])
                    pipeline.write_json(root / "build/research" / company["ticker"] / "request.json", request)
                    result["jobs"].append({"ticker": company["ticker"], "errors": manifest["errors"], "metrics": manifest["metrics"]})
                except (OSError, ValueError) as error:
                    result["jobs"].append({"ticker": company["ticker"], "error": str(error)})
            pipeline.write_json(root / "build/research" / (args.group + "-batch.json"), result)
            if any(job.get("error") or job.get("errors") for job in result["jobs"]):
                print(json.dumps(result, indent=2))
                return 1
        else:
            ticker = args.ticker.upper()
            company = pipeline.issuer(root, ticker)
            result = {}
            if args.command in {"collect", "run"}:
                manifest = pipeline.collect(root, company, args.as_of, os.environ.get("SEC_USER_AGENT", ""), args.max_events)
                result = {"manifest": str(root / "build/research" / ticker / "manifest.json"), "errors": manifest["errors"], "metrics": manifest["metrics"]}
                if manifest["errors"]:
                    print(json.dumps(result, indent=2))
                    return 1
                plan = pipeline.read_json(root / "build/research" / ticker / "update-plan.json")
                if args.command == "run" and not args.force and not plan["requires_review"] and pipeline.managed_packet_path(root, ticker).exists() and pipeline.profile_path(root, company).exists():
                    result["skipped"] = "No disclosure changes; existing research and review dates preserved."
                    print(json.dumps(result, indent=2))
                    return 0
            if args.command in {"prepare", "run"}:
                request = pipeline.prepare_request(root, ticker, args.max_chars)
                request_path = root / "build/research" / ticker / "request.json"
                pipeline.write_json(request_path, request)
                result["request"] = str(request_path)
                if args.command == "run" and args.runner:
                    packet, model_metrics = pipeline.run_model(root, request, args.runner.resolve())
                    packet_path = root / "build/research" / ticker / "packet.json"
                    pipeline.write_json(packet_path, packet)
                    result["draft"] = str(pipeline.apply_packet(root, packet, args.apply))
                    result["model_metrics"] = model_metrics
                    pipeline.write_json(root / "build/research" / ticker / "run-metrics.json", model_metrics)
                    if args.apply:
                        kb.build(root)
            if result.get("errors"):
                print(json.dumps(result, indent=2))
                return 1
        result["elapsed_seconds"] = round(time.monotonic() - started, 3)
        print(json.dumps(result, indent=2))
        return 0
    except (OSError, ValueError, KeyError, TypeError, TimeoutError, subprocess.SubprocessError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
