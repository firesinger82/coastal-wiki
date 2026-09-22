"""TREE-STATE 회귀 게이트 (DESIGN failure mode 35).

실패 시 TREE_STATE_GATE_FAILED. 실행: python3 test_tree_state.py

합성 저장소로 세 분류를 모두 만들고, 실측 저장소(adcirc-testsuite)로 규모를 고정한다.
"""
import os
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import tree_state as ts

REAL = Path.home()/"coastal-wiki/models/ADCIRC/raw/source_code/adcirc-testsuite"


def sh(repo, *a):
    subprocess.run(["git", "-C", str(repo), *a], check=True,
                   capture_output=True, env={**os.environ,
                                             "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t",
                                             "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@t"})


def build(tmp):
    """LFS 포인터·LF 텍스트·정상 파일을 커밋한 뒤 작업트리를 필터 적용 상태로 만든다."""
    r = Path(tmp)
    sh(r, "init", "-q")
    (r/"ptr.nc").write_bytes(ts.LFS_MAGIC + b"\noid sha256:deadbeef\nsize 100\n")
    (r/"text.md").write_bytes(b"line one\nline two\n")
    (r/"same.txt").write_bytes(b"unchanged\n")
    (r/"edited.f90").write_bytes(b"      x = 1\n")
    sh(r, "add", "-A")
    sh(r, "commit", "-qm", "base")
    # 커밋 후: LFS smudge(포인터→실체) · EOL(LF→CRLF) · 실제 수정
    (r/"ptr.nc").write_bytes(b"\x89REALBINARYCONTENT" * 20)
    (r/"text.md").write_bytes(b"line one\r\nline two\r\n")
    (r/"edited.f90").write_bytes(b"      x = 2\n")
    return r


def main():
    fails = []
    with tempfile.TemporaryDirectory() as tmp:
        r = build(tmp)
        got = {p: ts.classify(r, p) for p in ts.modified_paths(r)}
        want = {"ptr.nc": "LFS_SMUDGED", "text.md": "EOL_NORMALIZED",
                "edited.f90": "REAL_MODIFICATION"}
        for p, w in want.items():
            if got.get(p) != w:
                fails.append(f"{p}: {got.get(p)} != {w}")
        if "same.txt" in got:
            fails.append("변경 없는 파일이 modified 로 잡힘")
        # 실제 수정이 하나라도 있으면 막아야 한다
        if ts.check(r) == 0:
            fails.append("REAL_MODIFICATION 이 있는데 통과시킴")

    # 실측 — adcirc-testsuite 는 필터로만 dirty 하다(사람 수정 0)
    if REAL.is_dir():
        counts = {}
        for p in ts.modified_paths(REAL):
            c = ts.classify(REAL, p)
            counts[c] = counts.get(c, 0) + 1
        if counts.get("REAL_MODIFICATION"):
            fails.append(f"adcirc-testsuite 에 실제 수정 {counts['REAL_MODIFICATION']}건 — "
                         "트리가 오염됐거나 판별이 틀렸다")
        if not counts.get("LFS_SMUDGED"):
            fails.append("adcirc-testsuite 에서 LFS_SMUDGED 를 하나도 찾지 못함")
        skipped = ""
    else:
        skipped = ", 실측 건너뜀"

    print(f"fixtures 4(합성) + 실측 1{skipped} | 실패 {len(fails)}")
    for f in fails:
        print("  FAIL:", f)
    if fails:
        print("\nTREE_STATE_GATE_FAILED")
        return 1
    print("\nTREE_STATE_GATE_PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
