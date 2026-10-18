#!/usr/bin/env python3
"""Evaluate evidence retrieval and abstention separately; no answer generation or API calls."""
import argparse
from collections import Counter
import json
import hashlib
import math
from pathlib import Path
import re
import sys

import stock_brain as kb


STOP = {"a", "an", "the", "is", "are", "was", "were", "of", "for", "in", "and", "to", "what", "which", "how", "does", "do", "its", "by", "as", "on", "with", "from"}


def tokens(text):
    return [w for w in re.findall(r"[a-z0-9]+", text.lower()) if w not in STOP]


def lexical_retrieve(question, records, universe, top_k=6):
    """Small English-only BM25 baseline with explicit entity and freshness guards."""
    covered = {r.get("ticker") for r in records if r.get("document_type") == "company"}
    mentions = set()
    for company in universe:
        if re.search(r"\b" + re.escape(company["ticker"]) + r"\b", question):
            mentions.add(company["ticker"])
        name = re.sub(r"\b(?:Corporation|Technologies|Technology|Inc|Corp)\.?", "", company["company_name"]).strip(" ,.")
        if name and name.lower() in question.lower():
            mentions.add(company["ticker"])
    unknown_symbols = set(re.findall(r"\b[A-Z]{2,5}\b", question)) - {c["ticker"] for c in universe} - {"AI", "GAAP", "EPS", "USD", "HBM", "CPU", "GPU", "ADR", "NYSE", "SEC"}
    relation_question = bool(re.search(r"\b(?:relationship|collaboration|partnership|supplier|customer)\b", question, re.I))
    missing_issuer = bool(mentions - covered) and not (relation_question and mentions & covered)
    # Uppercase product/program acronyms are common inside an identified issuer's
    # question. They are not automatically additional tickers.
    unresolved = bool(unknown_symbols) and (not mentions or bool(re.search(r"\bcompare\b|\bversus\b|\bvs\b", question, re.I)))
    if missing_issuer or unresolved:
        return {"abstain": True, "reason": "Requested issuer lacks reviewed coverage or the symbol needs disambiguation.", "chunk_ids": []}
    if re.search(r"(?:today|current|live|right now).*(?:price|multiple|market cap)|(?:price|multiple).*(?:today|right now)|consensus|price target|fair value", question, re.I):
        return {"abstain": True, "reason": "This corpus has no live market-data or consensus feed.", "chunk_ids": []}
    candidates = [r for r in records if not mentions or r.get("ticker") in mentions]
    if not candidates:
        return {"abstain": True, "reason": "No eligible evidence.", "chunk_ids": []}
    documents = [tokens(r["text"]) for r in candidates]
    frequencies = Counter(word for document in documents for word in set(document))
    avg = sum(map(len, documents)) / len(documents)
    query = tokens(question)
    scored = []
    for record, document in zip(candidates, documents):
        counts = Counter(document)
        score = 0.0
        for term in query:
            tf = counts[term]
            if tf:
                idf = math.log(1 + (len(documents) - frequencies[term] + .5) / (frequencies[term] + .5))
                score += idf * tf * 2.2 / (tf + 1.2 * (.25 + .75 * len(document) / avg))
        if score > 0:
            scored.append((score, record["id"]))
    ids = [cid for _, cid in sorted(scored, key=lambda x: (-x[0], x[1]))[:top_k]]
    return {"abstain": not bool(ids), "reason": None if ids else "No lexical evidence match.", "chunk_ids": ids}


def evaluate(cases, predictions, records):
    corpus = {r["id"]: r for r in records}
    results = []
    for case in cases:
        pred = predictions.get(case["id"], {"abstain": False, "chunk_ids": []})
        ids = pred.get("chunk_ids", [])
        kb.need(len(ids) == len(set(ids)) and all(cid in corpus for cid in ids), "prediction contains unknown or duplicate chunk IDs")
        if case["expected_behavior"] == "abstain":
            passed = pred.get("abstain") is True
            results.append({"id": case["id"], "kind": "abstention", "passed": passed})
        else:
            hits = []
            for expected in case["evidence"]:
                hits.append(any(corpus[cid]["document_id"] == expected["document_id"] and corpus[cid]["section_id"] == expected["section_id"]
                                and set(expected["source_ids"]) <= {s["id"] for s in corpus[cid]["sources"]} for cid in ids))
            results.append({"id": case["id"], "kind": "retrieval", "passed": bool(hits) and all(hits) and not pred.get("abstain"),
                            "evidence_recall": sum(hits) / len(hits), "retrieved": ids})
    retrieval = [r for r in results if r["kind"] == "retrieval"]
    negative = [r for r in results if r["kind"] == "abstention"]
    return {"cases": len(results), "retrieval_case_pass_rate": sum(r["passed"] for r in retrieval) / len(retrieval) if retrieval else None,
            "mean_evidence_recall": sum(r["evidence_recall"] for r in retrieval) / len(retrieval) if retrieval else None,
            "abstention_pass_rate": sum(r["passed"] for r in negative) / len(negative) if negative else None,
            "answer_factuality": "Not evaluated: this command retrieves evidence but does not generate answers.", "results": results}


def validate_cases(cases, records):
    kb.need(len({c["id"] for c in cases}) == len(cases), "duplicate evaluation case IDs")
    for case in cases:
        kb.need(kb.scalar(case.get("question")) and kb.scalar(case.get("expected_answer")), "question and gold answer/rationale required")
        kb.need(case["expected_behavior"] in {"answer", "abstain"}, "invalid expected behavior")
        if case["expected_behavior"] == "answer":
            kb.need(bool(case.get("evidence")), "answerable case requires gold evidence")
            for expected in case["evidence"]:
                kb.need(any(r["document_id"] == expected["document_id"] and r["section_id"] == expected["section_id"]
                            and set(expected["source_ids"]) <= {s["id"] for s in r["sources"]} for r in records),
                        f"{case['id']}: gold evidence not present in reviewed export")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=kb.ROOT)
    parser.add_argument("--cases", type=Path, default=Path("eval/questions.json"))
    parser.add_argument("--predictions", type=Path, help="Optional JSON mapping case ID to abstain/chunk_ids from another retriever")
    parser.add_argument("--output", type=Path, default=Path("build/evaluation.json"))
    parser.add_argument("--top-k", type=int, default=6)
    args = parser.parse_args()
    try:
        root = args.root.resolve()
        cases_path = args.cases if args.cases.is_absolute() else root / args.cases
        cases = json.loads(cases_path.read_text())["cases"]
        records = kb.export_records(root)
        validate_cases(cases, records)
        kb.need(args.top_k > 0, "top-k must be positive")
        universe = json.loads((root / "config/universe.json").read_text())["companies"]
        if args.predictions:
            predictions = json.loads(args.predictions.read_text())
        else:
            predictions = {c["id"]: lexical_retrieve(c["question"], records, universe, args.top_k) for c in cases}
        report = {"retriever": "external" if args.predictions else "English BM25 baseline", "top_k": args.top_k,
                  "corpus_chunks": len(records), "corpus_sha256": hashlib.sha256(json.dumps(records, sort_keys=True).encode()).hexdigest(),
                  "cases_sha256": hashlib.sha256(cases_path.read_bytes()).hexdigest(), **evaluate(cases, predictions, records)}
        output = args.output if args.output.is_absolute() else root / args.output
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(report, indent=2) + "\n")
        print(json.dumps({k: v for k, v in report.items() if k != "results"}, indent=2))
        return 0
    except (OSError, ValueError, KeyError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
