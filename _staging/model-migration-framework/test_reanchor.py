"""REANCHOR 회귀 게이트 (DESIGN v2.0 §REANCHOR — 주석 함정).

실패 시 REANCHOR_GATE_FAILED. 실행: python3 test_reanchor.py
파일럿 실측 사례를 fixture 로 고정한다.
"""
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import reanchor as ra

CEL = Path.home()/".cache/coastal-snapshots/celeris-upstream"
CEL_OLD = "f6fd78bd12af3aeeef11774a850b6b3d52be65b3"
CEL_NEW = "ebca435d02b258768e0352fbaf27404f2f135799"

# Celeris 실측: (파일, old 줄, 기대 new 줄) — 각 지점 2줄 위에 주석화된 옛 코드가 있다
CELERIS = [("js/Handler_BoundaryPass.js", 100, 140),
           ("js/main.js", 1881, 2624),
           ("js/Time_Series.js", 58, 60)]

UNIT = [
    # (설명, 줄, 경로, 주석인가)
    ("JS 주석",        "// export function foo(a, b) {", "x.js",     True),
    ("JS 실행",        "  export function foo(a, b) {",  "x.js",     False),
    ("WGSL 주석",      "  // let x = 1;",                "x.wgsl",   True),
    ("Fortran 자유 주석", "!     call SWTSTA(112)",       "x.f90",    True),
    ("Fortran 고정 C",  "C     OLD CODE",                 "x.f",      True),
    ("Fortran 실행",    "      call CALTRAN(...)",        "x.f90",    False),
    ("꼬리 주석은 아님", "  total_time = a * b;  // note",  "x.js",     False),
    ("빈 줄",           "   ",                            "x.js",     False),
]


def git(*a):
    r = subprocess.run(["git", "-c", "safe.directory=*", "-C", str(CEL), *a],
                       capture_output=True)
    return r.stdout.decode("utf-8", "replace").splitlines()


def main():
    fails = []
    for name, line, path, want in UNIT:
        if ra.is_commented(line, path) != want:
            fails.append(f"is_commented {name}: {not want} != {want}")

    if CEL.exists():
        for path, old_ln, want in CELERIS:
            o = git("show", f"{CEL_OLD}:{path}")
            n = git("show", f"{CEL_NEW}:{path}")
            if not o or not n:
                fails.append(f"{path}: blob 없음")
                continue
            r = ra.find_anchor(o[old_ln - 1], n, path, hint=old_ln)
            if r["line"] != want:
                fails.append(f"{path}:{old_ln} → {r['line']} != {want} ({r['status']})")
            elif r["status"] not in ("RESOLVED_SKIPPED_COMMENT","RESOLVED_VIA_COMMENT_NEIGHBOR"):
                fails.append(f"{path}:{old_ln} 주석 회피가 기록되지 않음: {r['status']}")
        skipped = 0
    else:
        skipped = len(CELERIS)

    # Fortran 선언 문법 변경: 심볼명이 앵커 (Delft3D 실측)
    old_decl = "   real(kind=dp), allocatable, target :: s1max(:) !< [m] maximum waterlevel"
    new_file = ["   real(kind=dp), allocatable, target, dimension(:) :: s0 !< [m] waterlevel",
                "   real(kind=dp), allocatable, target, dimension(:) :: s1max !< [m] maximum waterlevel"]
    r = ra.find_anchor(old_decl, new_file, "m_flow.f90", hint=1)
    if r["line"] != 2 or r["status"] != "RESOLVED_BY_SIGNATURE":
        fails.append(f"선언 문법 변경 재앵커 실패: {r}")
    # 선언 signature 는 :: 뒤 심볼이다 (타입 표기의 괄호·등호에 속지 않는다)
    if ra._signature("real(kind=dp), allocatable :: foo") != "::foo":
        fails.append(f"선언 signature 오류: {ra._signature('real(kind=dp), allocatable :: foo')}")
    # 심볼이 그 파일에서 사라졌으면 찾지 않는다
    if ra.find_anchor("   integer :: md_ptr", ["   integer :: other"], "x.f90")["status"] != "NOT_FOUND":
        fails.append("사라진 심볼을 잘못 정박")
    # 옛 줄 자체가 주석이면(Fortran 섹션 표제 등) 주석 일치가 정상이다
    fort = ["      subroutine X", "! loop over sweeps", "      do i=1,n"]
    r = ra.find_anchor("! loop over sweeps", fort, "x.ftn90", hint=2)
    if r["line"] != 2 or r["status"] != "RESOLVED":
        fails.append(f"주석 앵커(정상) 오판: {r}")
    # 전부 주석이면 고르지 않는다
    r = ra.find_anchor("let x = 1;", ["// let x = 1;", "  // let x = 1;"], "a.wgsl")
    if r["status"] != "ALL_COMMENTED" or r["line"] is not None:
        fails.append(f"ALL_COMMENTED 미처리: {r}")
    # 없는 내용
    if ra.find_anchor("nope();", ["a", "b"], "a.js")["status"] != "NOT_FOUND":
        fails.append("NOT_FOUND 미처리")

    n = len(UNIT) + len(CELERIS)
    print(f"fixtures {n} (Celeris 실측 {len(CELERIS)}{', 건너뜀' if skipped else ''})"
          f" + 규칙검사 6 | 실패 {len(fails)}")
    for f in fails:
        print("  FAIL:", f)
    if fails:
        print("\nREANCHOR_GATE_FAILED")
        return 1
    print("\nREANCHOR_GATE_PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
