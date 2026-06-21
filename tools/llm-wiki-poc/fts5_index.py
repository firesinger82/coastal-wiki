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
        title, body, tokenize='unicode61')""")
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
        con.execute("INSERT INTO idx VALUES (?,?,?,?,?)",
                    (str(rel), path_class(rel), cs, title, body))
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

def search(q, status=None, allow_only=True, k=8):
    con = sqlite3.connect(DB)
    where = ["idx MATCH ?"]; args = [q]
    if status:
        where.append("citation_status = ?"); args.append(status)
    sql = (f"SELECT path, citation_status, snippet(idx,4,'[',']','…',8), bm25(idx) "
           f"FROM idx WHERE {' AND '.join(where)} ORDER BY bm25(idx) LIMIT {k}")
    rows = con.execute(sql, args).fetchall()
    con.close()
    print(f"\nQ: {q!r}  status={status or 'any'}  → {len(rows)} hits")
    for path, cs, snip, score in rows:
        print(f"  [{score:6.2f}] ({cs or '—':>13}) {path}")
        print(f"            …{snip.strip()[:90]}…")

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
