#!/usr/bin/env python3
"""Maintain a Markdown knowledge base without calling any external service."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import date
import hashlib
import json
from pathlib import Path
import re
import sys
import textwrap
from urllib.parse import urlparse
import uuid

import yaml


ROOT = Path(__file__).resolve().parents[1]
TICKER = re.compile(r"[A-Z][A-Z0-9]*(?:[.-][A-Z0-9]+)*\Z")
SLUG = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
CITATION = re.compile(r"\[(S[0-9]{2,})\]")
STATUSES = {"stub", "draft", "reviewed", "archived"}
EXCHANGES = {"NASDAQ", "NYSE", "NYSE_AMERICAN"}
FIELDS = {
    "schema_version", "document_type", "company_id", "ticker", "ticker_aliases",
    "company_name", "exchange", "security_type", "domicile_country", "cik",
    "sector", "industry", "tags", "status", "as_of", "updated_at", "reviewed_at", "sources",
}


class Invalid(ValueError):
    """An actionable knowledge-base validation error."""


class UniqueSafeLoader(yaml.SafeLoader):
    """Reject ambiguous YAML instead of silently discarding duplicate keys."""


def unique_mapping(loader: UniqueSafeLoader, node: yaml.MappingNode, deep: bool = False) -> dict:
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        need(isinstance(key, str), "YAML mapping keys must be strings")
        need(key not in result, f"duplicate YAML key: {key}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueSafeLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


@dataclass
class Document:
    path: Path
    metadata: dict
    sections: dict[str, str]


def config(root: Path) -> tuple[list[dict], list[dict]]:
    return tuple(json.loads((root / "config" / f"{name}.json").read_text())
                 for name in ("sectors", "sections"))


def need(condition: bool, message: str) -> None:
    if not condition:
        raise Invalid(message)


def scalar(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip()) and "\n" not in value and "\r" not in value


def iso_date(value: object, name: str, required: bool = False) -> str | None:
    if value is None:
        need(not required, f"{name} is required")
        return None
    if type(value) is date:
        value = value.isoformat()
    need(isinstance(value, str) and bool(re.fullmatch(r"\d{4}-\d{2}-\d{2}", value)),
         f"{name} must be YYYY-MM-DD or null")
    try:
        parsed = date.fromisoformat(value)
    except ValueError as error:
        raise Invalid(f"{name} is not a valid date") from error
    need(parsed <= date.today(), f"{name} cannot be in the future")
    return value


def split_document(text: str) -> tuple[dict, str]:
    match = re.match(r"\A---\n(.*?)\n---\n(.*)\Z", text, flags=re.S)
    need(match is not None, "expected YAML frontmatter enclosed in ---")
    try:
        metadata = yaml.load(match[1], Loader=UniqueSafeLoader)
    except yaml.YAMLError as error:
        raise Invalid(f"invalid YAML: {error}") from error
    need(isinstance(metadata, dict), "frontmatter must be a mapping")
    return metadata, match[2]


def sections_from(body: str, definitions: list[dict]) -> dict[str, str]:
    headings, chunks = [], []
    current = None
    fence_char, fence_size = "", 0
    for line in body.splitlines():
        fence = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if fence:
            marker = fence[1]
            if not fence_char:
                fence_char, fence_size = marker[0], len(marker)
            elif marker[0] == fence_char and len(marker) >= fence_size:
                fence_char = ""
        if not fence_char and line.startswith("## "):
            headings.append(line[3:].strip())
            chunks.append([])
            current = chunks[-1]
        elif current is not None:
            current.append(line)
    need(headings == [entry["title"] for entry in definitions],
         "H2 headings must exactly match config/sections.json in order")
    return {entry["id"]: "\n".join(lines).strip()
            for entry, lines in zip(definitions, chunks)}


def unavailable(text: str) -> bool:
    return bool(re.fullmatch(r"Not (?:available|applicable):[^\n]+", text.strip()))


def validate_metadata(meta: dict, sectors: list[dict]) -> None:
    need(set(meta) == FIELDS, f"metadata keys differ: {sorted(set(meta) ^ FIELDS)}")
    need(type(meta["schema_version"]) is int and meta["schema_version"] == 1,
         "schema_version must be integer 1")
    need(meta["document_type"] == "company", "document_type must be company")
    for field in ("company_id", "ticker", "company_name", "exchange", "sector", "status", "security_type"):
        need(scalar(meta[field]), f"{field} must be a nonempty single-line string")
    need(bool(SLUG.fullmatch(meta["company_id"])), "company_id must be a lowercase hyphenated identifier")
    need(len(meta["ticker"]) <= 12 and bool(TICKER.fullmatch(meta["ticker"])), "invalid ticker")
    need(meta["exchange"] in EXCHANGES, "exchange is outside the initial U.S. listing scope")
    need(meta["security_type"] in {"common_stock", "adr"}, "security_type must be common_stock or adr")
    need(meta["sector"] in {s["id"] for s in sectors}, "unknown sector")
    need(meta["status"] in STATUSES, "unknown research status")
    need(meta["industry"] is None or scalar(meta["industry"]), "industry must be a string or null")
    need(meta["domicile_country"] is None or (
        isinstance(meta["domicile_country"], str) and bool(re.fullmatch(r"[A-Z]{2}", meta["domicile_country"]))),
        "domicile_country must be a two-letter uppercase code or null")
    need(meta["cik"] is None or (
        isinstance(meta["cik"], str) and bool(re.fullmatch(r"[0-9]{10}", meta["cik"]))),
        "cik must be a quoted ten-digit string or null")
    for field, pattern in (("tags", SLUG), ("ticker_aliases", TICKER)):
        values = meta[field]
        need(isinstance(values, list), f"{field} must be a list")
        need(all(isinstance(value, str) and bool(pattern.fullmatch(value)) for value in values),
             f"{field} contains an invalid value")
        need(len(values) == len(set(values)), f"{field} contains duplicates")
    need(all(len(value) <= 12 for value in meta["ticker_aliases"]), "ticker alias is too long")
    need(meta["ticker"] not in meta["ticker_aliases"], "ticker cannot also be its own alias")
    reviewed = meta["status"] == "reviewed"
    for field in ("as_of", "updated_at", "reviewed_at"):
        meta[field] = iso_date(meta[field], field, required=reviewed or field == "updated_at")
    if meta["as_of"]:
        need(meta["as_of"] <= meta["updated_at"], "as_of cannot follow updated_at")
    if meta["reviewed_at"]:
        need(meta["reviewed_at"] <= meta["updated_at"], "reviewed_at cannot follow updated_at")
        need(meta["as_of"] is not None and meta["as_of"] <= meta["reviewed_at"],
             "reviewed_at requires an as_of date no later than review")
    need(isinstance(meta["sources"], list), "sources must be a list")
    seen = set()
    for source in meta["sources"]:
        need(isinstance(source, dict) and set(source) == {
            "id", "title", "publisher", "url", "published_at", "accessed_at"},
            "each source needs id, title, publisher, url, published_at, accessed_at")
        for field in ("id", "title", "publisher", "url"):
            need(scalar(source[field]), f"source {field} must be a nonempty single-line string")
        need(bool(re.fullmatch(r"S[0-9]{2,}", source["id"])), "source ID must look like S01")
        need(source["id"] not in seen, "duplicate source ID")
        seen.add(source["id"])
        try:
            url = urlparse(source["url"])
            need(url.scheme in {"http", "https"} and bool(url.hostname)
                 and not re.search(r"\s", source["url"]), "source URL must be HTTP or HTTPS")
        except ValueError as error:
            raise Invalid("invalid source URL") from error
        source["published_at"] = iso_date(source["published_at"], "source published_at")
        source["accessed_at"] = iso_date(source["accessed_at"], "source accessed_at", required=True)
        need(source["accessed_at"] <= meta["updated_at"], "source access cannot follow updated_at")
        if source["published_at"]:
            need(source["published_at"] <= source["accessed_at"], "source publication cannot follow access")
        if reviewed:
            need(source["accessed_at"] <= meta["reviewed_at"], "review must include all source access dates")
    need(not reviewed or bool(seen), "reviewed profiles require sources")


def documents(root: Path) -> list[Document]:
    sectors, definitions = config(root)
    result, identities, symbols, ciks = [], set(), set(), set()
    paths = sorted(path for path in (root / "sectors").rglob("*.md") if "companies" in path.relative_to(root).parts)
    for path in paths:
        try:
            meta, body = split_document(path.read_text(encoding="utf-8"))
            validate_metadata(meta, sectors)
            expected = Path("sectors") / meta["sector"] / "companies" / meta["ticker"] / "README.md"
            need(path.relative_to(root) == expected, f"company profile must be stored at {expected}")
            need(body.startswith(f"# {meta['ticker']} — {meta['company_name']}\n"), "H1 must match ticker and company name")
            need(meta["company_id"] not in identities, "duplicate company_id")
            all_symbols = {meta["ticker"], *meta["ticker_aliases"]}
            need(not symbols.intersection(all_symbols), "duplicate ticker or alias across companies")
            if meta["cik"]:
                need(meta["cik"] not in ciks, "duplicate CIK: keep share classes in one company profile")
                ciks.add(meta["cik"])
            identities.add(meta["company_id"])
            symbols.update(all_symbols)
            sections = sections_from(body, definitions)
            known_sources = {s["id"] for s in meta["sources"]}
            need(set(CITATION.findall(body)) <= known_sources, "text cites an unregistered source ID")
            if meta["status"] == "reviewed":
                need(not re.search(r"\b(?:TODO|TBD|FIXME)\b|\{\{.*?\}\}", body, flags=re.I),
                     "reviewed profile still contains placeholders")
                for key, content in sections.items():
                    need(bool(content), f"reviewed section {key} is empty")
                    if key != "sources-and-change-log":
                        need(bool(CITATION.search(content)) or unavailable(content),
                             f"reviewed section {key} needs evidence or an explicit unavailable reason")
                for key in ("business-overview", "revenue-model-and-segments"):
                    need(bool(CITATION.search(sections[key])) and not unavailable(sections[key]),
                         f"reviewed {key} requires substantive sourced content")
            result.append(Document(path, meta, sections))
        except Invalid as error:
            raise Invalid(f"{path.relative_to(root)}: {error}") from error
    return sorted(result, key=lambda doc: doc.metadata["ticker"])


def validate_sector_guides(root: Path) -> None:
    sectors, _ = config(root)
    template = (root / "templates/sector/README.md").read_text(encoding="utf-8")
    titles = re.findall(r"^## (.+)$", template, flags=re.M)
    definitions = [{"id": str(index), "title": title} for index, title in enumerate(titles)]
    need(bool(definitions), "sector template has no section headings")
    for sector in sectors:
        path = root / "sectors" / sector["id"] / "README.md"
        need(path.exists(), f"missing sector guide: {path.relative_to(root)}")
        body = path.read_text(encoding="utf-8")
        need(body.startswith(f"# {sector['name']}\n"), f"wrong title: {path.relative_to(root)}")
        try:
            sections_from(body, definitions)
        except Invalid as error:
            raise Invalid(f"{path.relative_to(root)}: sector headings must match the sector template") from error


def cell(value: object) -> str:
    if value is None:
        return "—"
    return str(value).replace("\\", "\\\\").replace("|", "\\|").replace("[", "\\[").replace("]", "\\]").replace("<", "&lt;").replace(">", "&gt;")


def company_table(docs: list[Document], root: Path, sector: bool = False) -> str:
    rows = ["| Ticker | Company | Status | Research as of |", "| --- | --- | --- | --- |"]
    for doc in docs:
        meta = doc.metadata
        link = f"companies/{meta['ticker']}/README.md" if sector else doc.path.relative_to(root).as_posix()
        rows.append(f"| [{meta['ticker']}]({link}) | {cell(meta['company_name'])} | {meta['status']} | {cell(meta['as_of'])} |")
    return "\n".join(rows) if docs else "No company profiles yet. Coverage has not started."


def generated(root: Path, docs: list[Document]) -> dict[Path, str]:
    sectors, _ = config(root)
    banner = "<!-- Generated by scripts/stock_brain.py build. Do not edit by hand. -->\n\n"
    output = {}
    facts_path = root / 'data/sector-facts.json'
    facts = json.loads(facts_path.read_text()) if facts_path.exists() else None
    fact_rows = (facts or {}).get('companies', [])
    main = [banner + "# Stock Brain — Master index\n", "[Project overview](README.md) · [Company template](templates/company/README.md)\n",
            "## Curated research coverage\n", f"Curated profiles: **{len(docs)}**. Reviewed: **{sum(d.metadata['status'] == 'reviewed' for d in docs)}**. These counts describe curated research, not automatic factual coverage or the entire U.S. market.\n",
            "## Sectors\n", "| Sector | Profiles | Reviewed | Index |", "| --- | ---: | ---: | --- |"]
    for sector in sectors:
        subset = [doc for doc in docs if doc.metadata["sector"] == sector["id"]]
        reviewed = sum(doc.metadata["status"] == "reviewed" for doc in subset)
        base = f"sectors/{sector['id']}"
        main.append(f"| [{sector['name']}]({base}/README.md) | {len(subset)} | {reviewed} | [Browse]({base}/INDEX.md) |")
        output[Path(base) / "INDEX.md"] = banner + f"# {sector['name']} — Company index\n\n[Sector overview](README.md) · [Master index](../../INDEX.md)\n\n## Coverage\n\nProfiles: **{len(subset)}**. Reviewed: **{reviewed}**.\n\n## Companies\n\n" + company_table(subset, root, sector=True) + "\n"
    if facts:
        counts = facts['sector_counts']
        overview = [banner + '# Stock Brain — Sectors\n', '[Master index](../INDEX.md) · [Coverage policy](../docs/BRAIN_MARKDOWN.md)\n',
                    f"Factual Markdown files in this branch: **{facts['company_profiles']}**; financial history available: **{facts['financial_profiles']}**. "
                    f"Source release: `{facts['release_tag']}`, created {facts['created_at']}.\n",
                    'Factual files are not completed research. Sector assignments from SIC are provisional project navigation rules; ambiguous industries and fund signals stay unclassified.\n',
                    '| Sector | Factual files | Curated profiles | Reviewed research |', '| --- | ---: | ---: | ---: |']
        for sector in [*sectors, {'id': 'unclassified', 'name': 'Unclassified — needs evidence review'}]:
            sid = sector['id']
            subset = [d for d in docs if d.metadata['sector'] == sid]
            rows = sorted((r for r in fact_rows if r['sector'] == sid), key=lambda r: (r['company_name'].casefold(), r['cik']))
            reviewed = sum(d.metadata['status'] == 'reviewed' for d in subset)
            overview.append(f"| [{sector['name']}]({sid}/INDEX.md) | {len(rows)} | {len(subset)} | {reviewed} |")
            heading = (banner + f"# {sector['name']} — Company index\n\n[All sectors](../README.md) · [Master index](../../INDEX.md)\n\n"
                       f"Factual files: **{len(rows)}**. Curated profiles: **{len(subset)}**. Reviewed research: **{reviewed}**.\n\n"
                       f"Data release: `{facts['release_tag']}`. Provisional SIC groupings are not official GICS classifications. "
                       'Factual profiles remain stubs and do not enter reviewed retrieval. Counts can overlap: a researched company also has a separate factual file.\n\n'
                       '## Factual company files\n\n| Company | Current symbols | Financial history | Classification basis |\n| --- | --- | --- | --- |\n')
            heading += '\n'.join(f"| [{cell(r['company_name'])}](facts/{r['cik']}/README.md) | {cell(', '.join(r['tickers']))} | "
                                 f"{'available; quality gates apply' if r['financial_history_available'] else 'missing'} | {r['classification_method']} |" for r in rows)
            heading += '\n\n## Curated research\n\n' + (company_table(subset, root, sector=True) if subset else 'No completed company research in this sector yet.') + '\n'
            output[Path('sectors') / sid / 'INDEX.md'] = heading
        output[Path('sectors/README.md')] = '\n'.join(overview) + '\n'
        main[2:2] = ['## Broad factual coverage\n', f"**{facts['company_profiles']} actual company Markdown files** are stored inside `sectors/*/facts/`. "
                    f"[Browse all sectors and classification gaps](sectors/README.md). **{facts['financial_profiles']}** have financial history. "
                    'The curated research counts below are separate and must not be presented as broad research completion.\n']
    else:
        output[Path('sectors/README.md')] = (banner + '# Stock Brain — Sectors\n\n'
            'The sector factual-file synchronization has not published a snapshot in this branch yet. '
            'The current curated research contains ' + str(len(docs)) + ' company profiles. '
            'A broad data inventory does not mean all sector research is complete.\n\n'
            + '\n'.join(f"- [{s['name']}]({s['id']}/INDEX.md)" for s in sectors) + '\n')
    main += ["\n## All companies\n", company_table(docs, root), "\n## Cross-sector themes\n"]
    tags = sorted({tag for doc in docs for tag in doc.metadata["tags"]})
    if not tags:
        main.append("No company tags yet. Themes appear here automatically when profiles are tagged.")
    for tag in tags:
        links = [f"[{doc.metadata['ticker']}]({doc.path.relative_to(root).as_posix()})" for doc in docs if tag in doc.metadata["tags"]]
        main.append(f"- **{tag}**: {', '.join(links)}")
    output[Path("INDEX.md")] = "\n".join(main) + "\n"
    catalog = {"schema_version": 1, "companies": [
        {**doc.metadata, "source_path": doc.path.relative_to(root).as_posix()} for doc in docs]}
    output[Path("data/catalog.json")] = json.dumps(catalog, indent=2, ensure_ascii=False, sort_keys=True) + "\n"
    return output


def build(root: Path, check: bool = False) -> int:
    validate_sector_guides(root)
    docs = documents(root)
    from review_gates import check_managed_reviews
    try:
        check_managed_reviews(root, docs)
    except ValueError as error:
        raise Invalid(str(error)) from error
    from sector_corpus import sector_records
    sector_records(root)
    from sector_facts import verify as verify_sector_facts
    verify_sector_facts(root, root=root, allow_absent=True)
    for relative, content in generated(root, docs).items():
        path = root / relative
        if check:
            need(path.exists() and path.read_text(encoding="utf-8") == content,
                 f"{relative} is missing or stale; run the build command")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
    return len(docs)


def add(root: Path, ticker: str, name: str, sector: str, exchange: str, security_type: str) -> Path:
    # Validate first so a failed command cannot leave a partial or duplicate record.
    existing = documents(root)
    sectors, _ = config(root)
    meta, body = split_document((root / "templates/company/README.md").read_text(encoding="utf-8"))
    meta.update(company_id=f"company-{uuid.uuid4().hex}", ticker=ticker.upper(), company_name=name,
                sector=sector, exchange=exchange, security_type=security_type, updated_at=date.today().isoformat())
    validate_metadata(meta, sectors)
    need(not any(meta["ticker"] in {doc.metadata["ticker"], *doc.metadata["ticker_aliases"]} for doc in existing),
         "ticker is already covered, including aliases")
    path = root / "sectors" / sector / "companies" / meta["ticker"] / "README.md"
    need(not path.exists(), f"{path.relative_to(root)} already exists")
    title = f"# {meta['ticker']} — {name}"
    body = body.replace("# {{ticker}} — {{company_name}}", title, 1)
    body = body.replace(title + "\n", title + "\n\n[Sector](../../README.md) · [Master index](../../../../INDEX.md)\n", 1)
    content = "---\n" + yaml.safe_dump(meta, sort_keys=False, allow_unicode=True) + "---\n" + body
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    try:
        build(root)
    except Exception:
        path.unlink()
        raise
    return path


def table_parts(block: str, limit: int) -> list[str]:
    lines = block.splitlines()
    header = "\n".join(lines[:2])
    parts, current = [], header
    for row in lines[2:]:
        if len(current) + len(row) + 1 > limit and current != header:
            parts.append(current)
            current = header
        current += "\n" + row
    if current != header or len(lines) == 2:
        parts.append(current)
    return parts


def chunk_body(content: str, limit: int) -> list[str]:
    need(limit >= 500, "max-chars must be at least 500")
    blocks = []
    for block in re.split(r"\n\s*\n", content.strip()):
        if len(block) <= limit:
            blocks.append(block)
        elif re.match(r"^\|.*\n\|[\s:|\-]+\|", block):
            blocks.extend(table_parts(block, limit))
        else:
            # Keep ordinary lines intact; only split a line that exceeds the limit.
            for line in block.splitlines():
                blocks.extend(textwrap.wrap(line, width=limit, break_long_words=True,
                                            break_on_hyphens=False, replace_whitespace=False) or [""])
    chunks, current = [], ""
    for block in blocks:
        combined = current + "\n\n" + block if current else block
        if current and len(combined) > limit:
            chunks.append(current)
            current = block
        else:
            current = combined
    if current:
        chunks.append(current)
    return chunks


def export_records(root: Path, max_chars: int = 3000) -> list[dict]:
    _, definitions = config(root)
    titles = {entry["id"]: entry["title"] for entry in definitions}
    records = []
    docs = documents(root)
    from review_gates import check_managed_reviews
    try:
        check_managed_reviews(root, docs)
    except ValueError as error:
        raise Invalid(str(error)) from error
    for doc in docs:
        meta = doc.metadata
        if meta["status"] != "reviewed":
            continue
        for section_id, content in doc.sections.items():
            if section_id == "sources-and-change-log" or unavailable(content):
                continue
            source_ids = set(CITATION.findall(content))
            for part, text in enumerate(chunk_body(content, max_chars), 1):
                record = {**meta, "id": f"{meta['company_id']}:{section_id}:{part:03d}",
                          "document_id": meta["company_id"], "section_id": section_id,
                          "section_title": titles[section_id], "part": part,
                          "source_path": doc.path.relative_to(root).as_posix(),
                          "sources": [source for source in meta["sources"] if source["id"] in source_ids],
                          "text": f"Company: {meta['company_name']} ({meta['ticker']})\nSection: {titles[section_id]}\nResearch as of: {meta['as_of']}\n\n{text}"}
                payload = json.dumps(record, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
                record["content_sha256"] = hashlib.sha256(payload.encode()).hexdigest()
                records.append(record)
    from sector_corpus import sector_records
    records.extend(sector_records(root, max_chars))
    return records


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="knowledge-base root directory")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("build", help="validate profiles and rebuild navigation")
    commands.add_parser("check", help="validate profiles and check generated navigation")
    create = commands.add_parser("add", help="add a new unresearched company stub")
    create.add_argument("--ticker", required=True)
    create.add_argument("--name", required=True)
    create.add_argument("--sector", required=True)
    create.add_argument("--exchange", required=True, choices=sorted(EXCHANGES))
    create.add_argument("--security-type", default="common_stock", choices=["common_stock", "adr"])
    out = commands.add_parser("export", help="export reviewed company sections to JSONL")
    out.add_argument("--output", type=Path, default=Path("build/chunks.jsonl"))
    out.add_argument("--max-chars", type=int, default=3000)
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        if args.command in {"build", "check"}:
            count = build(root, check=args.command == "check")
            print(f"{'Checked' if args.command == 'check' else 'Built'} indexes: {count} company profiles.")
        elif args.command == "add":
            path = add(root, args.ticker, args.name, args.sector, args.exchange, args.security_type)
            print(f"Created unresearched stub: {path.relative_to(root)}")
        else:
            need(args.max_chars >= 500, "max-chars must be at least 500")
            records = export_records(root, args.max_chars)
            output = args.output if args.output.is_absolute() else root / args.output
            # Generated output must not overwrite source files or navigation.
            need(output.suffix == ".jsonl", "export output must end in .jsonl")
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_text("".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in records), encoding="utf-8")
            print(f"Exported {len(records)} chunks from reviewed research to {output}.")
        return 0
    except (Invalid, OSError, json.JSONDecodeError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
