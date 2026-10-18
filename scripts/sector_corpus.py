"""Opt-in, hash-bound retrieval export for genuinely researched sector guides."""
import hashlib
import json
import re

import stock_brain as kb


def sector_records(root, max_chars=3000):
    path = root / "config/sector_research.json"
    if not path.exists():
        return []
    data = json.loads(path.read_text())
    kb.need(data.get("schema_version") == 1, "unsupported sector research version")
    sectors = {s["id"]: s for s in kb.config(root)[0]}
    titles = re.findall(r"^## (.+)$", (root / "templates/sector/README.md").read_text(), flags=re.M)
    definitions = [{"id": re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-"), "title": title} for title in titles]
    output, seen = [], set()
    for entry in data["sectors"]:
        sector = entry["sector"]
        kb.need(sector in sectors and sector not in seen, "unknown or duplicate researched sector")
        seen.add(sector)
        kb.need(entry["status"] in kb.STATUSES, "invalid sector research status")
        if entry["status"] != "reviewed":
            continue
        guide = root / "sectors" / sector / "README.md"
        raw = guide.read_bytes()
        kb.need(hashlib.sha256(raw).hexdigest() == entry["content_sha256"], f"{sector}: sector guide changed after review")
        text = raw.decode()
        kb.need(not re.search(r"\b(?:TODO|TBD|FIXME)\b", text, re.I), "reviewed sector still has placeholders")
        meta, _ = kb.split_document((root / "templates/company/README.md").read_text())
        meta.update(company_id="sector-" + sector, ticker="SECTOR", company_name=sectors[sector]["name"], sector=sector,
                    status="reviewed", as_of=entry["as_of"], updated_at=entry["updated_at"], reviewed_at=entry["reviewed_at"], sources=entry["sources"])
        kb.validate_metadata(meta, kb.config(root)[0])
        sources = {s["id"]: s for s in entry["sources"]}
        sections = kb.sections_from(text, definitions)
        kb.need(set(kb.CITATION.findall(text)) <= set(sources), "unknown sector citation")
        for section in definitions:
            sid = section["id"]
            if sid in {"company-index", "sources-and-updates"}:
                continue
            content = sections[sid]
            if kb.unavailable(content):
                continue
            ids = set(kb.CITATION.findall(content))
            kb.need(bool(ids), f"{sector}/{sid}: reviewed research has no source")
            for part, body in enumerate(kb.chunk_body(content, max_chars), 1):
                record = {"schema_version": 1, "document_type": "sector", "document_id": "sector-" + sector,
                          "id": f"sector-{sector}:{sid}:{part:03d}", "sector": sector,
                          "section_id": sid, "section_title": section["title"], "part": part,
                          "as_of": entry["as_of"], "updated_at": entry["updated_at"], "reviewed_at": entry["reviewed_at"],
                          "status": "reviewed", "source_path": guide.relative_to(root).as_posix(),
                          "sources": [sources[s] for s in sorted(ids)],
                          "text": f"Sector: {sectors[sector]['name']}\nSection: {section['title']}\nResearch as of: {entry['as_of']}\n\n{body}"}
                payload = json.dumps(record, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
                record["content_sha256"] = hashlib.sha256(payload.encode()).hexdigest()
                output.append(record)
    return output
