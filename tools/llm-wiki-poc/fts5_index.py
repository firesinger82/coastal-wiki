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
import os, re, sqlite3, subprocess, sys, time
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

def _git_head():
    """HEAD sha of the wiki repo; "" when git/repo is unavailable (freshness
    check then degrades to schema-only — never blocks search)."""
    try:
        r = subprocess.run(["git", "-C", str(WIKI), "rev-parse", "HEAD"],
                           capture_output=True, text=True, timeout=5)
        return r.stdout.strip() if r.returncode == 0 else ""
    except Exception:
        return ""

def _indexed_sha():
    """indexed_git_sha recorded at build time; "" on any error (→ rebuild)."""
    try:
        con = sqlite3.connect(DB)
        row = con.execute(
            "SELECT value FROM meta WHERE key='indexed_git_sha'").fetchone()
        con.close()
        return row[0] if row else ""
    except sqlite3.Error:
        return ""

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
    # has_source_needed: G9 disclosed-gap 트라이스테이트 (true/false/'' 부재).
    # 마지막 컬럼에 추가 → snippet(idx,4)=body·bm25 tier(col5) 인덱스 불변.
    con.execute("""CREATE VIRTUAL TABLE idx USING fts5(
        path UNINDEXED, path_class UNINDEXED, citation_status UNINDEXED,
        title, body, tier UNINDEXED, has_source_needed UNINDEXED,
        tokenize='unicode61')""")
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
        # 부재='' = 미감사(unknown). 'true'/'false' = 감사됨(G9e). 그 외 값은 ''로.
        hsn = fm.get("has_source_needed", "").strip().lower()
        if hsn not in ("true", "false"):
            hsn = ""
        con.execute("INSERT INTO idx VALUES (?,?,?,?,?,?,?)",
                    (str(rel), path_class(rel), cs, title, body, tier, hsn))
        n += 1
    # freshness metadata (Codex 22회차): HEAD sha at build time → ensure_index()
    # rebuilds when HEAD moves without a reindex hook firing (e.g. hook-less
    # clone, long-lived MCP server across a git pull). Plain table, not fts5.
    con.execute("CREATE TABLE meta(key TEXT PRIMARY KEY, value TEXT)")
    con.execute("INSERT INTO meta VALUES ('indexed_git_sha', ?)", (_git_head(),))
    con.commit()
    dt = time.time() - t0
    size = DB.stat().st_size / 1024
    # status histogram
    hist = dict(con.execute(
        "SELECT citation_status, count(*) FROM idx GROUP BY citation_status").fetchall())
    con.close()
    print(f"indexed {n} docs in {dt:.2f}s  | db {size:.0f} KB")
    print("citation_status histogram:", hist)

def _schema_current():
    """True iff the existing DB has the current schema (newest column present).
    Guards against stale DBs built before a schema change — otherwise queries
    referencing the new column raise OperationalError on every search.
    has_source_needed is the newest column; meta table is the newest schema
    element overall (freshness metadata, Codex 22회차)."""
    try:
        con = sqlite3.connect(DB)
        cols = [r[1] for r in con.execute("PRAGMA table_info(idx)").fetchall()]
        has_meta = con.execute(
            "SELECT count(*) FROM sqlite_master WHERE type='table' AND name='meta'"
        ).fetchone()[0] == 1
        con.close()
        return "has_source_needed" in cols and has_meta
    except sqlite3.Error:
        return False

def ensure_index():
    """Build the index if missing, schema-stale, OR HEAD moved since the last
    build (indexed_git_sha mismatch — Codex 22회차: sha 최신인데 검색은 구인덱스
    방지). Cheap (~0.5s rebuild, ~ms when fresh) so callers can run it on
    startup and per tools/call. Rebuild-on-stale lets old DBs self-heal
    without requiring the reindex hooks (multi-machine 방식1). Dirty working
    tree is NOT detectable here (same HEAD) — hooks/manifest dirty flag cover
    that axis."""
    if not DB.exists() or not _schema_current():
        build()
        return
    head = _git_head()
    if head and head != _indexed_sha():
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
           f"snippet(idx,4,'[',']','…',12), bm25(idx), has_source_needed, "
           f"bm25(idx) + tier AS rank "
           f"FROM idx WHERE {' AND '.join(where)} ORDER BY rank LIMIT ?")
    rows = con.execute(sql, args + [k]).fetchall()
    con.close()
    # has_source_needed (G9): 'true'/'false'/None(부재=미감사). 소비자가 verified 의
    # 완전sourced vs disclosed-갭 vs 미감사를 기계 구별.
    def _hsn(v):
        return v if v in ("true", "false") else None
    return [dict(path=r[0], path_class=r[1], citation_status=r[2],
                 title=r[3], snippet=r[4].strip(), score=round(r[5], 3),
                 has_source_needed=_hsn(r[6])) for r in rows]

def manifest_stats():
    """Index-level metadata for wiki_manifest (doc count, status histogram)."""
    con = sqlite3.connect(DB)
    n = con.execute("SELECT count(*) FROM idx").fetchone()[0]
    hist = dict(con.execute(
        "SELECT citation_status, count(*) FROM idx GROUP BY citation_status").fetchall())
    by_class = dict(con.execute(
        "SELECT path_class, count(*) FROM idx GROUP BY path_class").fetchall())
    # G9f: verified 의 disclosed-gap 감사 커버리지 (true/false/미감사 3분).
    vrows = con.execute(
        "SELECT has_source_needed, count(*) FROM idx WHERE citation_status='verified' "
        "GROUP BY has_source_needed").fetchall()
    cov = {"true": 0, "false": 0, "unaudited": 0}
    for hsn, c in vrows:
        cov["true" if hsn == "true" else "false" if hsn == "false" else "unaudited"] += c
    con.close()
    return {"doc_count": n, "citation_status": hist, "path_class": by_class,
            "verified_gap_coverage": cov, "indexed_git_sha": _indexed_sha()}

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
