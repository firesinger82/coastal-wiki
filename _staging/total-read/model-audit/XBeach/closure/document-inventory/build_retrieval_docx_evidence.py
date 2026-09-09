#!/usr/bin/env python3
"""Freeze original-DOCX block evidence for non-page-aligned/partial X00 rows.

This script does not infer PDF pages.  It locates the reported converted-text
lines in the original DOCX package and records stable document-order block
positions plus short quotations.
"""

from __future__ import annotations

import hashlib
import json
import re
from difflib import SequenceMatcher
from pathlib import Path

from docx import Document
from docx.document import Document as _Document
from docx.table import Table
from docx.text.paragraph import Paragraph
from docx.oxml.table import CT_Tbl
from docx.oxml.text.paragraph import CT_P


ROOT = Path(__file__).resolve().parents[6]
HERE = Path(__file__).resolve().parent
ROWS = HERE / "all-207-disposition.jsonl"
CONVERTED = ROOT / "_staging/total-read/model-audit/XBeach/bindoc-converted"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def norm(text: str) -> str:
    text = text.replace("−", "-").replace("–", "-").replace("²", "2")
    return re.sub(r"[^a-z0-9.+_=-]+", " ", text.lower()).strip()


def iter_blocks(doc: _Document):
    block_index = 0
    paragraph_index = 0
    table_index = 0
    for child in doc.element.body.iterchildren():
        if isinstance(child, CT_P):
            paragraph_index += 1
            text = Paragraph(child, doc).text.strip()
            if text:
                block_index += 1
                yield {
                    "block_index": block_index,
                    "kind": "paragraph",
                    "paragraph_index": paragraph_index,
                    "text": text,
                }
        elif isinstance(child, CT_Tbl):
            table_index += 1
            table = Table(child, doc)
            for row_index, row in enumerate(table.rows, 1):
                cells = [re.sub(r"\s+", " ", c.text).strip() for c in row.cells]
                text = " | ".join(cells).strip(" |")
                if text:
                    block_index += 1
                    yield {
                        "block_index": block_index,
                        "kind": "table-row",
                        "table_index": table_index,
                        "row_index": row_index,
                        "text": text,
                    }


def parse_ranges(spec: str):
    out = []
    for part in spec.split(","):
        if "-" in part:
            a, b = map(int, part.split("-"))
        else:
            a = b = int(part)
        out.extend(range(a, b + 1))
    return out


def short_quote(text: str, query: str, limit_words: int = 24) -> str:
    words = re.findall(r"\S+", text)
    if len(words) <= limit_words:
        return text
    qwords = [w for w in re.findall(r"[A-Za-z0-9_.=-]+", query.lower()) if len(w) >= 3]
    low = [re.sub(r"\W", "", w.lower()) for w in words]
    positions = [i for i, w in enumerate(low) if any(q in w or w in q for q in qwords)]
    center = positions[len(positions) // 2] if positions else 0
    start = max(0, min(center - limit_words // 2, len(words) - limit_words))
    excerpt = " ".join(words[start : start + limit_words])
    return ("… " if start else "") + excerpt + (" …" if start + limit_words < len(words) else "")


def main():
    rows = [json.loads(line) for line in ROWS.read_text(encoding="utf-8").splitlines()]
    rows = [r for r in rows if (
        r["page_map"]["status"] == "cross-format-retrieval-candidate"
        or (r["page_map"]["status"] == "cross-format-partial" and r["representation_kind"] == "docx-text")
    )]
    cache = {}
    output = []
    for row in rows:
        original = ROOT / row["original_path"]
        converted = CONVERTED / row["representation_path"]
        if original not in cache:
            cache[original] = list(iter_blocks(Document(original)))
        blocks = cache[original]
        source_lines = converted.read_text(encoding="utf-8", errors="replace").splitlines()
        queries = []
        for lineno in parse_ranges(row["reported_lines"]):
            if 1 <= lineno <= len(source_lines):
                text = source_lines[lineno - 1].strip()
            if len(norm(text)) >= 5:
                queries.append((lineno, text))

        scored = {}
        for lineno, query in queries:
            nq = norm(query)
            qtokens = set(nq.split())
            for block in blocks:
                nb = norm(block["text"])
                if not nb:
                    continue
                if nq in nb or nb in nq:
                    score = min(len(nq), len(nb)) / max(len(nq), len(nb))
                    score = max(score, 0.96 if nq == nb else 0.90)
                else:
                    btokens = set(nb.split())
                    overlap = len(qtokens & btokens) / max(1, min(len(qtokens), len(btokens)))
                    if overlap < 0.34:
                        continue
                    score = 0.45 * overlap + 0.55 * SequenceMatcher(None, nq, nb).ratio()
                key = (lineno, block["block_index"])
                prior = scored.get(key)
                if prior is None or score > prior[0]:
                    scored[key] = (score, lineno, query, block)

        # Keep the best original block for every non-empty reported source line.
        # This preserves compound default-table findings instead of truncating
        # them to an arbitrary number of rows.
        ranked = sorted(scored.values(), key=lambda x: (x[1], -x[0], x[3]["block_index"]))
        chosen = []
        used_lines = set()
        for score, lineno, query, block in ranked:
            if score < 0.58:
                continue
            if lineno in used_lines:
                continue
            used_lines.add(lineno)
            if len(norm(block["text"])) < 5:
                continue
            item = {k: v for k, v in block.items() if k != "text"}
            item.update({
                "converted_line": lineno,
                "match_score": round(score, 4),
                "quote": short_quote(block["text"], query),
            })
            chosen.append(item)
        output.append({
            "finding_id": row["finding_id"],
            "finding": row["finding"],
            "original_docx": row["original_path"],
            "original_sha256": sha256(original),
            "reported_converted_text": row["representation_path"],
            "reported_lines": row["reported_lines"],
            "pdf_page_claim": None,
            "locator_basis": "original DOCX document-order block; no PDF page equivalence asserted",
            "alignment_category": row["page_map"]["status"],
            "evidence_blocks": chosen,
            "status": "original-docx-block-verified" if chosen else "no-original-block-match",
        })

    out = HERE / "retrieval-docx-evidence.json"
    out.write_text(json.dumps({
        "schema": "xbeach-retrieval-docx-evidence/v1",
        "count": len(output),
        "retrieval_candidate_count": sum(x["alignment_category"] == "cross-format-retrieval-candidate" for x in output),
        "partial_alignment_count": sum(x["alignment_category"] == "cross-format-partial" for x in output),
        "method": "python-docx 1.2.0 document-order paragraph/table-row extraction; normalized exact/fuzzy alignment to frozen converted-text line ranges",
        "warning": "These records deliberately make no PDF-page claim.",
        "items": output,
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(out)
    for item in output:
        scores = [b["match_score"] for b in item["evidence_blocks"]]
        print(item["finding_id"], item["status"], scores)


if __name__ == "__main__":
    main()
