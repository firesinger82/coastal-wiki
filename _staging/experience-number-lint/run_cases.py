#!/usr/bin/env python3
"""cases.json 재현 — 기준 리비전 트리를 임시 디렉터리에 풀고 현재 validator 로 판정."""
import json, shutil, subprocess, sys, tempfile
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
cases = json.loads((ROOT / "_staging/experience-number-lint/cases.json").read_text())
rev = cases["source_revision"]
tmp = Path(tempfile.mkdtemp(prefix="expnum-cases-"))
try:
    subprocess.run(["git", "-C", str(ROOT), "worktree", "add", "--detach", "-q", str(tmp / "wt"), rev], check=True)
    wt = tmp / "wt"
    shutil.copy(ROOT / "tools/validate-experience-numbers.py", wt / "tools/validate-experience-numbers.py")
    out = subprocess.run([sys.executable, str(wt / "tools/validate-experience-numbers.py")], cwd=wt, capture_output=True, text=True).stdout
    hits = {}
    for line in out.splitlines():
        p, _, rest = line.partition(":")
        ln = rest.split(":", 1)[0]
        if ln.isdigit():
            hits.setdefault(p, set()).add(int(ln))
    bad = 0; det = 0
    for c in cases["body_cases"]:
        lines = hits.get(c["path"], set())
        # 블록 시작 행 기준 보고이므로 case 행 ±6 이내 경고를 같은 블록으로 본다
        actual = "detect" if any(abs(l - c["line"]) <= 6 for l in lines) else "miss"
        det += actual == "detect"
        ok = actual == c["expected"]; bad += not ok
        print(f'{c["id"]:22s} expected={c["expected"]:6s} actual={actual:6s} {"OK" if ok else "MISMATCH"}')
    print(f"detected {det}/{len(cases['body_cases'])}, mismatches {bad}")
finally:
    subprocess.run(["git", "-C", str(ROOT), "worktree", "remove", "--force", str(tmp / "wt")])
    shutil.rmtree(tmp, ignore_errors=True)
sys.exit(1 if bad else 0)
