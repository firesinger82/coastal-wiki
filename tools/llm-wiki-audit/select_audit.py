#!/usr/bin/env python3
"""L4 자가 감사 루프 — Selector (결정론적 슬라이스 선정).

CLAUDE.md 절대규칙 #1(canonical 단언 = 출처 인용 필수)의 자가 감사 PoC.
이 스크립트는 *판단하지 않는다* — 어떤 파일을 AI Auditor 에게 넘길지만 고른다.

선정 규칙:
  - 대상 = concepts/ · models/ 의 *본문* .md (README/INDEX/manifest/_template 및
    raw/_archive/_staging/research 제외).  rule #1 이 무는 곳만.
  - SSOT = committed 내용(HEAD blob sha).  dirty working tree 는 감사 대상 아님
    (Phase 1 F3 기조).  미커밋 변경은 경고만.
  - ledger(_staging/audit/ledger.json)의 blob_sha 와 다르거나 미기록인 파일만 후보
    (= 변경분만 점진 소진 → 반복 실행이 곧 루프).
  - 우선순위: verified(무결성 위반 시 가장 무거움) → source-needed/빈 → 기타 상태.
  - 한 슬라이스 = 최대 N (기본 8).  전수 1방 금지(plan.md W4).

출력: stdout 에 JSON {slice:[{path,citation_status,blob_sha,dirty}], stats:{...}}.
순수 stdlib + git.  Recorder(record_audit.py)가 결과를 받아 verdict·ledger 처리.
"""
import json, re, subprocess, sys
from pathlib import Path

WIKI = Path(__file__).resolve().parents[2]
LEDGER = WIKI / "_staging" / "audit" / "ledger.json"
ROOTS = ("concepts", "models")
DENY = {"raw", "_archive", "_staging", "research", "_template", ".git"}
SCAFFOLD = re.compile(r"/(README|INDEX|manifest)\.md$")
FM = re.compile(r"^---\n(.*?)\n---\n", re.S)
# 무결성 위반이 가장 무거우므로 verified 를 먼저 감사. 빈/source-needed 는 분류.
PRIORITY = {"verified": 0, "source-needed": 1, "": 2}


def citation_status(text):
    m = FM.match(text)
    if not m:
        return ""
    for line in m.group(1).splitlines():
        if line.startswith("citation_status:"):
            return line.split(":", 1)[1].strip().strip('"').strip("'")
    return ""


def git(*args):
    return subprocess.run(["git", "-C", str(WIKI), *args],
                          capture_output=True, text=True).stdout


def head_blobs():
    """HEAD 의 path→blob_sha (content hash).  한 번의 git 호출."""
    out = git("ls-tree", "-r", "HEAD", "--format=%(objectname) %(path)")
    blobs = {}
    for line in out.splitlines():
        sha, _, path = line.partition(" ")
        if path:
            blobs[path] = sha
    return blobs


def dirty_paths():
    out = git("status", "--porcelain", "--untracked-files=all")
    return {line[3:].strip() for line in out.splitlines() if line.strip()}


def is_content(rel: Path):
    if rel.parts and rel.parts[0] not in ROOTS:
        return False
    if any(p in DENY for p in rel.parts):
        return False
    return not SCAFFOLD.search(str(rel))


def main():
    n = 8
    if "--n" in sys.argv:
        n = int(sys.argv[sys.argv.index("--n") + 1])

    ledger = json.loads(LEDGER.read_text()) if LEDGER.exists() else {}
    blobs = head_blobs()
    dirty = dirty_paths()

    candidates = []
    for md in sorted(WIKI.rglob("*.md")):
        rel = md.relative_to(WIKI)
        if not is_content(rel):
            continue
        relstr = str(rel)
        blob = blobs.get(relstr)
        if blob is None:        # 미커밋 신규 파일 — committed SSOT 없음, skip(경고)
            continue
        prev = ledger.get(relstr, {}).get("blob_sha")
        if prev == blob:        # 마지막 감사 이후 내용 불변 → skip
            continue
        cs = citation_status(md.read_text(encoding="utf-8", errors="ignore"))
        candidates.append({
            "path": relstr,
            "citation_status": cs,
            "blob_sha": blob,
            "dirty": relstr in dirty,
        })

    candidates.sort(key=lambda c: (PRIORITY.get(c["citation_status"], 3), c["path"]))
    slice_ = candidates[:n]

    stats = {
        "total_content": sum(1 for md in WIKI.rglob("*.md")
                             if is_content(md.relative_to(WIKI))),
        "pending": len(candidates),
        "slice": len(slice_),
        "dirty_in_slice": [c["path"] for c in slice_ if c["dirty"]],
    }
    print(json.dumps({"slice": slice_, "stats": stats}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
