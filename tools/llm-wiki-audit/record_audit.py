#!/usr/bin/env python3
"""L4 자가 감사 루프 — Recorder (결정론적 verdict + 리포트 + ledger).

AI Auditor/Adversary 가 내놓은 findings(JSON)를 받아:
  1) verdict 매트릭스(현재 citation_status × 미출처 단언 수)를 *결정론적으로* 적용
  2) _staging/audit/L4-<date>.md 리포트 작성 (file:line·단언·사유·verdict)
  3) ledger 갱신(파일별 blob_sha·verdict·date) → 다음 run 이 변경분만 재감사

판단(어느 단언이 미출처인가)은 AI 몫.  여기서는 *분류 결과를 규칙에 대입*만 한다.
auto-edit 없음: canonical 파일은 손대지 않는다(report-only, 사람이 게이트).

입력 findings JSON (stdin 또는 --in <file>):
  { "date": "YYYY-MM-DD",            # 선택; 없으면 오늘
    "findings": [
      { "path": "concepts/waves/02-theory.md",
        "blob_sha": "<HEAD blob from selector>",
        "citation_status": "verified",
        "has_real_claims": true,
        "sourced": 12, "opinion": 1,
        "unsourced": [ {"line": 42, "text": "...", "reason": "...",
                        "adversary": "refute 실패 → confirmed"} ] } ] }
"""
import difflib, json, subprocess, sys
from datetime import datetime
from pathlib import Path

WIKI = Path(__file__).resolve().parents[2]
AUDIT = WIKI / "_staging" / "audit"
LEDGER = AUDIT / "ledger.json"
PROPOSALS = AUDIT / "proposals"


def git_show(path):
    """HEAD blob 의 committed 내용 (제안 패치의 base = SSOT, 워킹트리 아님)."""
    return subprocess.run(["git", "-C", str(WIKI), "show", f"HEAD:{path}"],
                          capture_output=True, text=True).stdout


def build_patch(path, proposals):
    """findings 의 proposals(Edit식 old_string/new_string)를 committed 본문 대비
    git-apply 가능한 unified diff 로 렌더. *생성만* 하고 적용하지 않는다(report-only).
    old_string 이 정확히 1회 매치될 때만 패치화 — 0/다중 매치는 manual 로 표기해
    깨진 패치를 만들지 않는다. 반환: (patch_text or '', [note...])."""
    committed = git_show(path)
    chunks, notes = [], []
    for pr in proposals:
        old, new = pr.get("old_string", ""), pr.get("new_string", "")
        cnt = committed.count(old) if old else 0
        if cnt != 1:
            notes.append({"status": "MANUAL", "rationale": pr.get("rationale", ""),
                          "why": f"old_string {cnt}회 매치 — 자동 패치 불가(수동 처리)"})
            continue
        new_full = committed.replace(old, new)
        diff = "".join(difflib.unified_diff(
            committed.splitlines(keepends=True), new_full.splitlines(keepends=True),
            fromfile=f"a/{path}", tofile=f"b/{path}"))
        chunks.append(f"diff --git a/{path} b/{path}\n{diff}")
        notes.append({"status": "PATCH", "rationale": pr.get("rationale", "")})
    return "".join(chunks), notes

# verdict 매트릭스 (plan.md "L4 자가 감사 루프 PoC 설계")
V_VIOLATION = "INTEGRITY-VIOLATION"   # verified 인데 미출처 → 강등 or 출처 보강
V_CONFIRMED = "verified-confirmed"
V_PROMOTE = "promote-candidate"       # 빈/source-needed 인데 미출처 0 → verified 후보
V_NEEDS_WORK = "needs-work"           # 빈/source-needed + 미출처 → 작업목록
V_SCAFFOLD = "scaffolding-exempt"
V_NONSTD = "status-nonstandard"       # reference/partial(ly)-verified 등 → 정규화 대상

SEVERITY = {V_VIOLATION: 0, V_NEEDS_WORK: 1, V_NONSTD: 2,
            V_PROMOTE: 3, V_CONFIRMED: 4, V_SCAFFOLD: 5}


def verdict_for(cs, n_unsourced, has_claims):
    if not has_claims:
        return V_SCAFFOLD
    if cs == "verified":
        return V_VIOLATION if n_unsourced > 0 else V_CONFIRMED
    if cs in ("source-needed", ""):
        return V_PROMOTE if n_unsourced == 0 else V_NEEDS_WORK
    return V_NONSTD       # 표준 외 상태값 — 별도 정규화 필요


def main():
    raw = sys.stdin.read()
    if "--in" in sys.argv:
        raw = Path(sys.argv[sys.argv.index("--in") + 1]).read_text()
    data = json.loads(raw)
    now = datetime.now()
    today = data.get("date") or now.strftime("%Y-%m-%d")
    # 슬라이스를 같은 날 반복 감사하므로(설계 의도) 리포트는 시각 suffix 로
    # 고유화 — 고정 L4-<date>.md 면 이전 슬라이스 findings 가 human gate 전에
    # 덮여 소실됨(Codex review #1). ledger 는 누적 상태라 고정 파일 유지.
    stamp = now.strftime("%H%M%S")
    findings = data["findings"]

    AUDIT.mkdir(parents=True, exist_ok=True)
    ledger = json.loads(LEDGER.read_text()) if LEDGER.exists() else {}

    rows = []
    all_patch = []          # 누적 패치 텍스트 (한 .patch 파일로)
    for f in findings:
        cs = f.get("citation_status", "")
        unsourced = f.get("unsourced", [])
        v = verdict_for(cs, len(unsourced), f.get("has_real_claims", True))
        # V1: actionable finding 의 제안 패치 렌더(미적용). proposals 없으면 [].
        patch_text, notes = build_patch(f["path"], f.get("proposals", [])) \
            if f.get("proposals") else ("", [])
        if patch_text:
            all_patch.append(patch_text)
        rows.append({**f, "verdict": v, "proposal_notes": notes})
        ledger[f["path"]] = {
            "blob_sha": f.get("blob_sha"),
            "verdict": v,
            "audited_date": today,
            "n_unsourced": len(unsourced),
        }
    rows.sort(key=lambda r: (SEVERITY.get(r["verdict"], 9), r["path"]))

    # ── 리포트 ──
    out = [f"# L4 자가 감사 리포트 — {today}", "",
           f"감사 {len(rows)}파일.  **report-only — canonical 미수정, 사람이 게이트.**", ""]
    tally = {}
    for r in rows:
        tally[r["verdict"]] = tally.get(r["verdict"], 0) + 1
    out.append("| verdict | 수 |")
    out.append("|---|---|")
    for v, c in sorted(tally.items(), key=lambda kv: SEVERITY.get(kv[0], 9)):
        out.append(f"| {v} | {c} |")
    out.append("")

    for r in rows:
        flag = " ⚠" if r["verdict"] == V_VIOLATION else ""
        out.append(f"## {r['verdict']}{flag} — `{r['path']}`")
        out.append(f"- citation_status: `{r.get('citation_status','') or '(빈)'}` · "
                   f"sourced {r.get('sourced','?')} · opinion {r.get('opinion','?')} · "
                   f"미출처 {len(r.get('unsourced', []))}"
                   + ("  · ⚠ dirty(미커밋)" if r.get("dirty") else ""))
        for u in r.get("unsourced", []):
            out.append(f"  - L{u.get('line','?')}: {u.get('text','').strip()}")
            out.append(f"    - 사유: {u.get('reason','')}")
            if u.get("adversary"):
                out.append(f"    - adversary: {u['adversary']}")
        for pn in r.get("proposal_notes", []):
            tag = "🩹 제안 패치(미적용)" if pn["status"] == "PATCH" else "✍ 수동 처리 필요"
            out.append(f"  - {tag}: {pn.get('rationale','')}"
                       + (f" — {pn['why']}" if pn.get("why") else ""))
        out.append("")

    # ── 제안 패치 파일(미적용) ──
    patch_rel = None
    if all_patch:
        PROPOSALS.mkdir(parents=True, exist_ok=True)
        patch_path = PROPOSALS / f"L4-{today}-{stamp}.patch"
        patch_path.write_text("".join(all_patch), encoding="utf-8")
        patch_rel = patch_path.relative_to(WIKI)
        out.insert(3, f"제안 패치(미적용): `{patch_rel}` — 검토 후 적용은 "
                      f"`git apply {patch_rel}` (사람 결정). 자동 적용 안 함.\n")

    report = AUDIT / f"L4-{today}-{stamp}.md"
    report.write_text("\n".join(out), encoding="utf-8")
    LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2), encoding="utf-8")

    violations = tally.get(V_VIOLATION, 0)
    print(f"리포트: {report.relative_to(WIKI)}")
    print(f"ledger: {LEDGER.relative_to(WIKI)} ({len(ledger)} 파일 누적)")
    print(f"verdict 집계: {tally}")
    if patch_rel:
        print(f"제안 패치(미적용): {patch_rel}  — git apply 는 사람 검토 후.")
    if violations:
        print(f"⚠ 무결성 위반 {violations}건 — 사람 검토 필요(verified 강등 or 출처 보강).")


if __name__ == "__main__":
    main()
