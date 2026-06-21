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
    # V1 default = 라운드로빈(변경분 우선 + 정적 파일 오래된순 순환). --changed-only
    # = V0 동작(변경분만). 정적 verified(대다수)가 1회 감사 후 영영 안 도는 맹점 해소.
    changed_only = "--changed-only" in sys.argv

    ledger = json.loads(LEDGER.read_text()) if LEDGER.exists() else {}
    blobs = head_blobs()
    dirty = dirty_paths()

    changed, rotation = [], []
    total_content = 0
    for md in sorted(WIKI.rglob("*.md")):
        rel = md.relative_to(WIKI)
        if not is_content(rel):
            continue
        total_content += 1
        relstr = str(rel)
        blob = blobs.get(relstr)
        if blob is None:        # 미커밋 신규 파일 — committed SSOT 없음, skip(경고)
            continue
        entry = ledger.get(relstr, {})
        prev = entry.get("blob_sha")
        is_dirty = relstr in dirty
        # SSOT = committed(HEAD blob). dirty 파일은 워킹트리 frontmatter 가
        # blob_sha 와 어긋날 수 있으므로 citation_status 도 committed 에서 읽어
        # blob_sha 와 일관 유지(Codex review #2). clean 파일은 워킹트리==HEAD 라
        # 그대로 read(빠름).
        content = git("show", f"HEAD:{relstr}") if is_dirty \
            else md.read_text(encoding="utf-8", errors="ignore")
        item = {
            "path": relstr,
            "citation_status": citation_status(content),
            "blob_sha": blob,
            "dirty": is_dirty,
        }
        if prev != blob:        # 신규(미감사) 또는 내용 변경 → 최우선
            item["reason"] = "new" if prev is None else "changed"
            changed.append(item)
        else:                   # 내용 불변·이미 감사됨 → 라운드로빈 풀
            item["reason"] = "rotation"
            item["audited_date"] = entry.get("audited_date", "")
            # 정렬 키 = 마이크로초 타임스탬프(없으면 구 날짜·미상 fallback). 같은 날
            # 반복 run 에도 방금 감사한 파일이 뒤로 밀려 순환 진행(Codex review #1).
            item["audited_at"] = entry.get("audited_at") or entry.get("audited_date", "")
            rotation.append(item)

    # 변경분: 무결성 위험 큰 verified 우선. 회전분: 가장 오래 감사 안 된 순(미상→최우선).
    changed.sort(key=lambda c: (PRIORITY.get(c["citation_status"], 3), c["path"]))
    rotation.sort(key=lambda c: (c["audited_at"], c["path"]))

    pool = changed if changed_only else changed + rotation
    slice_ = pool[:n]

    stats = {
        "total_content": total_content,
        "changed": len(changed),
        "rotation_pool": len(rotation),
        "never_audited": sum(1 for c in changed if c["reason"] == "new"),
        "mode": "changed-only" if changed_only else "round-robin",
        "slice": len(slice_),
        "slice_reasons": {r: sum(1 for c in slice_ if c["reason"] == r)
                          for r in ("new", "changed", "rotation")},
        "dirty_in_slice": [c["path"] for c in slice_ if c["dirty"]],
    }
    print(json.dumps({"slice": slice_, "stats": stats}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
