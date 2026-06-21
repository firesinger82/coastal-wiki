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
import json, sys
from datetime import date
from pathlib import Path

WIKI = Path(__file__).resolve().parents[2]
AUDIT = WIKI / "_staging" / "audit"
LEDGER = AUDIT / "ledger.json"

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
    today = data.get("date") or date.today().isoformat()
    findings = data["findings"]

    AUDIT.mkdir(parents=True, exist_ok=True)
    ledger = json.loads(LEDGER.read_text()) if LEDGER.exists() else {}

    rows = []
    for f in findings:
        cs = f.get("citation_status", "")
        unsourced = f.get("unsourced", [])
        v = verdict_for(cs, len(unsourced), f.get("has_real_claims", True))
        rows.append({**f, "verdict": v})
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
        out.append("")

    report = AUDIT / f"L4-{today}.md"
    report.write_text("\n".join(out), encoding="utf-8")
    LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2), encoding="utf-8")

    violations = tally.get(V_VIOLATION, 0)
    print(f"리포트: {report.relative_to(WIKI)}")
    print(f"ledger: {LEDGER.relative_to(WIKI)} ({len(ledger)} 파일 누적)")
    print(f"verdict 집계: {tally}")
    if violations:
        print(f"⚠ 무결성 위반 {violations}건 — 사람 검토 필요(verified 강등 or 출처 보강).")


if __name__ == "__main__":
    main()
