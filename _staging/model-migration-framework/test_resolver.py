"""RESOLVER 회귀 게이트 (DESIGN v2.0 §CROSS-MODEL RESOLUTION).

실패 시 RESOLVER_GATE_FAILED. 실행: python3 test_resolver.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import resolver as rv

W = Path.home()/"coastal-wiki"

# (참조, 소유 노트, max_line, 기대 status, 기대 model)
FIX = [
    ("src/SwanCompUnstruc.ftn90", "models/SWAN/source-analysis/x.md", 900, "RESOLVED", "SWAN"),
    ("calexp.f90",                "models/EFDC/source-analysis/x.md", 1200, "RESOLVED", "EFDC"),
    # switch.pl 생성물 인용 (.ftn90 → .f90, .ftn → .f)
    ("SwanIEM.f90",   "models/SWAN/source-analysis/x.md", None, "RESOLVED_GENERATED", "SWAN"),
    ("SwanQCM.f90",   "models/SWAN/source-analysis/x.md", None, "RESOLVED_GENERATED", "SWAN"),
    ("swmod1.f",      "models/SWAN/source-analysis/x.md", None, "RESOLVED_GENERATED", "SWAN"),
    ("SwanSpectPart.f90", "models/SWAN/source-analysis/x.md", None,
     "RESOLVED_GENERATED_EXT_MISMATCH", "SWAN"),
    # cross-model — SWAN 노트가 ADCIRC 결합 코드를 인용
    ("couple2swan.F", "models/SWAN/source-analysis/x.md", None, "RESOLVED_CROSS_MODEL", "ADCIRC"),
    ("macros.inc",    "models/SWAN/source-analysis/x.md", None, "RESOLVED_CROSS_MODEL", "ADCIRC"),
    # 번들 사본 — 복수 모델 보유는 임의 귀속 금지
    ("metis.h",       "models/SWAN/source-analysis/x.md", None, "AMBIGUOUS_CROSS_MODEL", None),
    # 같은 모델 안 동명 2개(adcirc/src vs asgs/output): 줄 번호 배제 + 주 저장소 우선
    ("wind.F",        "models/ADCIRC/source-analysis/x.md", 8288, "RESOLVED_NARROWED", "ADCIRC"),
    ("wind.F",        "models/ADCIRC/source-analysis/x.md", 100,  "RESOLVED_NARROWED", "ADCIRC"),
    # 이중 배치(배포본 vs 사용자 템플릿): 노트 선언 component 로 귀속
    ("ana_initial.h", "models/ROMS/source-analysis/roms_analytical_functionals.md", 53,
     "RESOLVED_BY_COMPONENT", "ROMS"),
    ("ana_grid.h", "models/ROMS/source-analysis/roms_analytical_functionals.md", 200,
     "RESOLVED_BY_COMPONENT", "ROMS"),
    # 부분 이름은 추측으로 해소하지 않는다
    ("Compdata.f90",  "models/SWAN/source-analysis/x.md", None, "UNRESOLVED", None),
    ("PDataSets.ftn90", "models/SWAN/source-analysis/x.md", None, "UNRESOLVED", None),
]


def main():
    idx = rv.build_index(W)
    fails = []
    for ref, note, ml, want_s, want_m in FIX:
        r = rv.resolve(ref, note, idx, max_line=ml, wiki=W)
        if r["status"] != want_s or (want_m and r["model"] != want_m):
            fails.append(f"{ref} ({note}): {r['status']}/{r['model']} != {want_s}/{want_m}")
    # 롤백 자산은 색인에서 제외돼야 한다
    for m, d in idx.items():
        for paths in d.values():
            if any(".old-" in p for p in paths):
                fails.append(f"롤백 자산이 색인에 포함됨: {paths[0]}")
                break
    # wind.F 는 adcirc/src 로 귀속돼야 한다(asgs 사본 아님)
    r = rv.resolve("wind.F", "models/ADCIRC/source-analysis/x.md", idx, max_line=8288, wiki=W)
    if not (len(r["paths"]) == 1 and "/adcirc/src/" in r["paths"][0]):
        fails.append(f"wind.F 귀속 오류: {r['paths']}")
    # component 귀속은 ROMS/Functionals 를 고른다(User/Functionals 아님)
    r = rv.resolve("ana_initial.h", "models/ROMS/source-analysis/roms_analytical_functionals.md",
                   idx, max_line=53, wiki=W)
    if not (len(r["paths"]) == 1 and "/ROMS/Functionals/" in r["paths"][0]):
        fails.append(f"component 귀속 오류: {r['paths']}")
    # 모양 기반 억제 금지: 짧은 stem 이어도 실재하면 참조다 (io.F·bc.F 19건 선례)
    for probe in ("io.F", "bc.F"):
        if rv.resolve(probe, "models/ROMS/source-analysis/x.md", idx, wiki=W)["status"] == "UNRESOLVED":
            fails.append(f"짧은 stem 실재 파일이 미해소: {probe}")

    print(f"fixtures {len(FIX)} + 규칙검사 4 | 실패 {len(fails)}")
    for f in fails:
        print("  FAIL:", f)
    if fails:
        print("\nRESOLVER_GATE_FAILED")
        return 1
    print("\nRESOLVER_GATE_PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
