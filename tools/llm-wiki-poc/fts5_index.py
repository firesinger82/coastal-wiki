#!/usr/bin/env python3
"""Phase 0 PoC — SQLite FTS5 index over coastal-wiki (L1 candidate b).

Demonstrates the 4 Phase-0 decision criteria for a headless serving layer:
  (a) headless     — pure stdlib sqlite3, no GUI/daemon
  (b) frontmatter  — citation_status parsed into a filterable column
  (c) corpus scope — allowlist/denylist by path-class; research/_staging/_archive/raw excluded
  (d) transport    — FTS5 is a library; an MCP wrapper can expose it over stdio OR http (transport-agnostic)

Usage:
  python3 fts5_index.py build               # build index
  python3 fts5_index.py search "<query>" [--all] [--status verified]
"""
import os, re, sqlite3, sys, time
from pathlib import Path

WIKI = Path(__file__).resolve().parents[2]          # repo root
DB = Path(__file__).resolve().parent / "wiki_fts.db"
ALLOW = {"concepts", "models", "textbook", "experience"}
DENY_PARTS = {"_archive", "_staging", "raw", "research", ".git", ".obsidian", "node_modules"}

# Raw full-text dumps (textbook/md/<file>.md): indexed for page-lookup / AI
# cross-reference, but demoted below every curated note so a refined excerpt
# (textbook/notes, models/*/source-analysis, manual-notes, concepts) always
# outranks the raw OCR. BM25 in FTS5 is negative (lower = better); adding a
# large positive constant pushes raw dumps into a strict lower tier while
# preserving BM25 order within each tier.
RAW_DEMOTE = 1000.0

def is_raw_dump(rel: Path):
    return len(rel.parts) >= 2 and rel.parts[0] == "textbook" and rel.parts[1] == "md"

FM = re.compile(r"^---\n(.*?)\n---\n", re.S)

def frontmatter(text):
    m = FM.match(text)
    if not m:
        return {}, text
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm, text[m.end():]

def path_class(rel: Path):
    return rel.parts[0] if rel.parts else ""

def included(rel: Path):
    if any(p in DENY_PARTS for p in rel.parts):
        return False
    return path_class(rel) in ALLOW

def build():
    if DB.exists():
        DB.unlink()
    con = sqlite3.connect(DB)
    con.execute("""CREATE VIRTUAL TABLE idx USING fts5(
        path UNINDEXED, path_class UNINDEXED, citation_status UNINDEXED,
        title, body, tier UNINDEXED, tokenize='unicode61')""")
    t0 = time.time(); n = 0
    for md in WIKI.rglob("*.md"):
        rel = md.relative_to(WIKI)
        if not included(rel):
            continue
        try:
            text = md.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        fm, body = frontmatter(text)
        title = fm.get("title") or md.stem
        cs = fm.get("citation_status", "")
        tier = RAW_DEMOTE if is_raw_dump(rel) else 0.0
        con.execute("INSERT INTO idx VALUES (?,?,?,?,?,?)",
                    (str(rel), path_class(rel), cs, title, body, tier))
        n += 1
    con.commit()
    dt = time.time() - t0
    size = DB.stat().st_size / 1024
    # status histogram
    hist = dict(con.execute(
        "SELECT citation_status, count(*) FROM idx GROUP BY citation_status").fetchall())
    con.close()
    print(f"indexed {n} docs in {dt:.2f}s  | db {size:.0f} KB")
    print("citation_status histogram:", hist)

def ensure_index():
    """Build the index if missing. Cheap (~0.5s) so callers can rebuild on startup."""
    if not DB.exists():
        build()

def query(q, status=None, path_class=None, k=8):
    """Return BM25-ranked hits as a list of dicts (data, not print)."""
    con = sqlite3.connect(DB)
    where = ["idx MATCH ?"]; args = [q]
    if status:
        where.append("citation_status = ?"); args.append(status)
    if path_class:
        where.append("path_class = ?"); args.append(path_class)
    # tier demotes raw textbook dumps below curated notes (see RAW_DEMOTE);
    # bm25(idx) is negative (lower = better), so adding tier sorts dumps last.
    sql = (f"SELECT path, path_class, citation_status, title, "
           f"snippet(idx,4,'[',']','…',12), bm25(idx), bm25(idx) + tier AS rank "
           f"FROM idx WHERE {' AND '.join(where)} ORDER BY rank LIMIT ?")
    rows = con.execute(sql, args + [k]).fetchall()
    con.close()
    return [dict(path=r[0], path_class=r[1], citation_status=r[2],
                 title=r[3], snippet=r[4].strip(), score=round(r[5], 3)) for r in rows]

def manifest_stats():
    """Index-level metadata for wiki_manifest (doc count, status histogram)."""
    con = sqlite3.connect(DB)
    n = con.execute("SELECT count(*) FROM idx").fetchone()[0]
    hist = dict(con.execute(
        "SELECT citation_status, count(*) FROM idx GROUP BY citation_status").fetchall())
    by_class = dict(con.execute(
        "SELECT path_class, count(*) FROM idx GROUP BY path_class").fetchall())
    con.close()
    return {"doc_count": n, "citation_status": hist, "path_class": by_class}

def search(q, status=None, allow_only=True, k=8):
    rows = query(q, status=status, k=k)
    print(f"\nQ: {q!r}  status={status or 'any'}  → {len(rows)} hits")
    for r in rows:
        print(f"  [{r['score']:6.2f}] ({r['citation_status'] or '—':>13}) {r['path']}")
        print(f"            …{r['snippet'][:90]}…")

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "build"
    if cmd == "build":
        build()
    elif cmd == "search":
        q = sys.argv[2]
        status = None
        if "--status" in sys.argv:
            status = sys.argv[sys.argv.index("--status") + 1]
        search(q, status=status)
