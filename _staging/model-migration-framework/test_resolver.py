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
    # 변종 트리: 노트 선언 source_scope 로 거른다 (Celeris main vs transect_version)
    ("js/main.js", "models/Celeris/source-analysis/celeris-source-map.md", None,
     "RESOLVED_BY_SCOPE", "Celeris"),
    ("Pass1.wgsl", "models/Celeris/source-analysis/celeris-pipeline-graph.md", None,
     "RESOLVED_BY_SCOPE", "Celeris"),
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
    # source_scope 귀속은 main 트리를 고른다(transect_version 아님)
    r = rv.resolve("main.js", "models/Celeris/source-analysis/celeris-source-map.md", idx, wiki=W)
    if not (len(r["paths"]) == 1 and "transect_version" not in r["paths"][0]):
        fails.append(f"source_scope 귀속 오류: {r['paths']}")
    # source_scope `dir/*` = 그 디렉터리 **직속만**. 한 저장소 안에서 루트와 하위가
    # 같은 파일명을 쓰면 접두사로는 갈리지 않는다(LISFLOOD-FP 2026-09-22).
    #   output.cpp : 루트 vs swe/  |  fields.cpp : swe/ vs swe/dg2/
    r = rv.resolve("output.cpp", "models/LISFLOOD-FP/source-analysis/lisflood-fp-io-boundary.md",
                   idx, wiki=W)
    if not (len(r["paths"]) == 1 and r["paths"][0].endswith("LISFLOOD-FP/output.cpp")):
        fails.append(f"source_scope dir/* (루트 직속) 오류: {r['paths']}")
    r = rv.resolve("fields.cpp", "models/LISFLOOD-FP/source-analysis/lisflood-fp-swe-fv1-dg2.md",
                   idx, wiki=W)
    if not (len(r["paths"]) == 1 and r["paths"][0].endswith("swe/fields.cpp")):
        fails.append(f"source_scope dir/* (하위 제외) 오류: {r['paths']}")
    # `dir` (별표 없음)은 하위까지 포함한다 — 두 형태가 구분되는지 확인
    if rv.declared_scope.__doc__ is None or "dir/*" not in rv.declared_scope.__doc__:
        fails.append("declared_scope 문서에 dir/* 규칙 누락")
    # 모양 기반 억제 금지: 짧은 stem 이어도 실재하면 참조다 (io.F·bc.F 19건 선례)
    for probe in ("io.F", "bc.F"):
        if rv.resolve(probe, "models/ROMS/source-analysis/x.md", idx, wiki=W)["status"] == "UNRESOLVED":
            fails.append(f"짧은 stem 실재 파일이 미해소: {probe}")

    # note_path 계약: 절대경로는 **거부**한다 (failure mode 34).
    # 허용하면 owning_model 이 조용히 None 을 돌려 전 참조가 cross-model 로 떨어지고,
    # 실패가 아니라 다른 저장소로의 잘못된 귀속이 나온다 — 게이트로는 잡히지 않는다.
    # 실측 2026-09-21: roms_test 인용이 0건이 아니라 45/36 으로 집계됐다.
    abs_note = str(W/"models/ROMS/source-analysis/roms_4dvar.md")
    for bad, why in ((abs_note, "절대경로"), ("../outside/x.md", "위키 밖 경로")):
        try:
            rv.owning_model(bad)
            fails.append(f"note_path 계약 미강제: {why} 를 받아들임 ({bad})")
        except ValueError:
            pass
    # 정상 상대경로는 그대로 통과해야 한다(과잉 거부 금지)
    for good, want in (("models/ROMS/source-analysis/roms_4dvar.md", "ROMS"),
                       ("concepts/waves/01-theory.md", None),
                       ("textbook/notes/theory-x.md", None)):
        try:
            got = rv.owning_model(good)
            if got != want:
                fails.append(f"owning_model({good}) = {got} != {want}")
        except ValueError as e:
            fails.append(f"정상 경로를 거부함: {good} ({e})")

    print(f"fixtures {len(FIX)} + 규칙검사 9 | 실패 {len(fails)}")
    for f in fails:
        print("  FAIL:", f)
    if fails:
        print("\nRESOLVER_GATE_FAILED")
        return 1
    print("\nRESOLVER_GATE_PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
