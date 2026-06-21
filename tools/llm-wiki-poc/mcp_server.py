#!/usr/bin/env python3
"""Phase 1 — coastal-wiki MCP server (L3 bridge over FTS5 / L1).

Pure-stdlib, READ-ONLY, newline-delimited JSON-RPC 2.0 over stdio (MCP).
No pip install needed on reader machines (방식 1: git pull → run). Tools:
  - wiki_search(query, status?, path_class?, k?)  BM25 + frontmatter filter
  - wiki_read(path, mode=section|grep|full, pattern?, max_lines?)  realpath-sandboxed
  - wiki_manifest()  git sha/dirty/timestamp + doc count + citation_status histogram

Reflects codex 1차: F3 (manifest exposes committed sha + dirty), F4 (corpus
allowlist + citation_status), F5 (read-only, realpath sandbox, denylist).
Run:  python3 mcp_server.py        (stdio)
"""
import contextlib, json, os, re, subprocess, sys, time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import fts5_index as fx  # noqa: E402

PROTOCOL = "2024-11-05"
WIKI, ALLOW, DENY = fx.WIKI, fx.ALLOW, fx.DENY_PARTS


def log(*a):
    print(*a, file=sys.stderr, flush=True)


# ---- read-only path sandbox (F5) ------------------------------------------
def safe_path(p: str) -> Path:
    if p.startswith("/") or ".." in Path(p).parts:
        raise ValueError("absolute paths and '..' are not allowed")
    target = (WIKI / p).resolve()
    if not (target == WIKI or str(target).startswith(str(WIKI) + os.sep)):
        raise ValueError("path escapes the wiki root")
    rel = target.relative_to(WIKI)
    if any(part in DENY for part in rel.parts):
        raise ValueError(f"denied corpus zone: {rel.parts[0] if rel.parts else p}")
    if not rel.parts or rel.parts[0] not in ALLOW:
        raise ValueError(f"outside canonical allowlist {sorted(ALLOW)}")
    if not target.is_file():
        raise ValueError("not a file")
    return target


# ---- git / freshness metadata (F3) ----------------------------------------
def git_meta() -> dict:
    def g(*args):
        try:
            return subprocess.run(["git", "-C", str(WIKI), *args],
                                  capture_output=True, text=True, timeout=5).stdout.strip()
        except Exception:
            return ""
    sha = g("rev-parse", "HEAD")
    dirty = bool(g("status", "--porcelain"))
    return {"git_sha": sha, "dirty_working_tree": dirty,
            "index_built_unix": int(fx.DB.stat().st_mtime) if fx.DB.exists() else None}


# ---- tools -----------------------------------------------------------------
def t_search(args):
    rows = fx.query(args["query"], status=args.get("status"),
                    path_class=args.get("path_class"), k=int(args.get("k", 8)))
    lines = [f"{len(rows)} hits for {args['query']!r} "
             f"(status={args.get('status') or 'any'})"]
    for r in rows:
        lines.append(f"[{r['score']}] ({r['citation_status'] or '—'}) {r['path']}\n"
                     f"    {r['title']}\n    …{r['snippet'][:160]}…")
    return "\n".join(lines)


def t_read(args):
    target = safe_path(args["path"])
    text = target.read_text(encoding="utf-8", errors="ignore")
    mode = args.get("mode", "section")
    if mode == "full":
        out = text[:20000]
    elif mode == "grep":
        pat = re.compile(args.get("pattern", ""), re.I)
        hits = [f"{i+1}: {ln}" for i, ln in enumerate(text.splitlines()) if pat.search(ln)]
        out = "\n".join(hits[:200]) or "(no match)"
    else:  # section: from a heading matching pattern to the next heading of same/higher level
        pat = args.get("pattern")
        lines = text.splitlines()
        if not pat:
            out = "\n".join(lines[:int(args.get("max_lines", 60))])
        else:
            rx = re.compile(pat, re.I)
            start = next((i for i, ln in enumerate(lines)
                          if ln.lstrip().startswith("#") and rx.search(ln)), None)
            if start is None:
                out = f"(no heading matching {pat!r})"
            else:
                lvl = len(lines[start]) - len(lines[start].lstrip("#"))
                end = start + 1
                while end < len(lines):
                    s = lines[end]
                    if s.lstrip().startswith("#") and (len(s) - len(s.lstrip("#"))) <= lvl:
                        break
                    end += 1
                out = "\n".join(lines[start:end])
    return f"# {args['path']} (mode={mode})\n\n{out}"


def t_manifest(_args):
    with contextlib.redirect_stdout(sys.stderr):   # never leak build() prints to JSON-RPC stdout
        fx.ensure_index()
    meta = {**git_meta(), **fx.manifest_stats(),
            "corpus_allowlist": sorted(ALLOW),
            "note": "read-only; results carry citation_status; default search returns any status — pass status='verified' to filter"}
    return json.dumps(meta, ensure_ascii=False, indent=2)


TOOLS = {
    "wiki_search": {
        "fn": t_search,
        "description": "BM25 full-text search over canonical coastal-wiki (concepts/models/textbook/experience). Filter by citation_status (verified/source-needed) and path_class. research/_archive/raw are excluded from the index.",
        "schema": {"type": "object", "properties": {
            "query": {"type": "string"},
            "status": {"type": "string", "enum": ["verified", "source-needed", "draft-unsourced"]},
            "path_class": {"type": "string", "enum": ["concepts", "models", "textbook", "experience"]},
            "k": {"type": "integer", "default": 8}}, "required": ["query"]},
    },
    "wiki_read": {
        "fn": t_read,
        "description": "Read a canonical wiki file (read-only, sandboxed to repo). mode=section (heading via pattern), grep (regex lines), full.",
        "schema": {"type": "object", "properties": {
            "path": {"type": "string"},
            "mode": {"type": "string", "enum": ["section", "grep", "full"], "default": "section"},
            "pattern": {"type": "string"},
            "max_lines": {"type": "integer", "default": 60}}, "required": ["path"]},
    },
    "wiki_manifest": {
        "fn": t_manifest,
        "description": "Index/freshness metadata: git sha, dirty working tree flag, index build time, doc count, citation_status histogram, corpus allowlist.",
        "schema": {"type": "object", "properties": {}},
    },
}


# ---- JSON-RPC stdio loop ---------------------------------------------------
def handle(msg):
    mid, method, params = msg.get("id"), msg.get("method"), msg.get("params", {})
    if method == "initialize":
        return {"protocolVersion": PROTOCOL, "capabilities": {"tools": {}},
                "serverInfo": {"name": "coastal-wiki", "version": "0.1.0"}}
    if method == "tools/list":
        return {"tools": [{"name": n, "description": t["description"],
                           "inputSchema": t["schema"]} for n, t in TOOLS.items()]}
    if method == "tools/call":
        name = params.get("name")
        t = TOOLS.get(name)
        if not t:
            return {"isError": True, "content": [{"type": "text", "text": f"unknown tool {name}"}]}
        try:
            text = t["fn"](params.get("arguments", {}))
            return {"content": [{"type": "text", "text": text}]}
        except Exception as e:
            return {"isError": True, "content": [{"type": "text", "text": f"error: {e}"}]}
    if method in ("ping",):
        return {}
    return None  # unknown / notification


def main():
    # CRITICAL: build()/ensure_index() print to stdout; that would corrupt the
    # JSON-RPC stream. Redirect any startup stdout to stderr.
    with contextlib.redirect_stdout(sys.stderr):
        fx.ensure_index()
    log(f"coastal-wiki MCP ready (docs indexed, root={WIKI})")
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except json.JSONDecodeError:
            continue
        if "id" not in msg:  # notification → no response
            continue
        result = handle(msg)
        if result is None:
            resp = {"jsonrpc": "2.0", "id": msg["id"],
                    "error": {"code": -32601, "message": "method not found"}}
        else:
            resp = {"jsonrpc": "2.0", "id": msg["id"], "result": result}
        sys.stdout.write(json.dumps(resp, ensure_ascii=False) + "\n")
        sys.stdout.flush()


if __name__ == "__main__":
    main()
