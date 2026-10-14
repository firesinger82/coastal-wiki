---
title: "ROMS 대조 결론 노트 반영 — 작업 20"
canonical_source: self
citation_status: verified
verification_method: "2026-10-14 ROMS recovery 대조 보고서 반영"
last_source_check: "2026-10-14 (recovery 대조 반영)"
note_author: "Codex"
note_date: 2026-10-14
---

# ROMS 대조 결론 노트 반영 — 작업 20

배정표: [note-job-20.tsv](../assign/note-job-20.tsv).
입력은 대조 보고서의 수정안·차이 결론·최종 전수 검증 기록이다.
파일별 완료 기록은 각 노트 반영 후 덧붙인다.

## 배정 범위

| 대상 파일 | 배정 행 수 | 반영 방식 |
|---|---:|---|
| [roms_nonlinear_core_remaining.md](../../../models/ROMS/source-analysis/roms_nonlinear_core_remaining.md) | 69 | 배정 행 표와 수정안 반영 |
| [roms_4dvar_drivers.md](../../../models/ROMS/source-analysis/roms_4dvar_drivers.md) | 51 | 배정 행 표와 수정안 반영 |
| [roms_kpp_boundary_layer.md](../../../models/ROMS/source-analysis/roms_kpp_boundary_layer.md) | 32 | 배정 행 표와 수정안 반영 |
| [roms_nonlinear_physics_modules.md](../../../models/ROMS/source-analysis/roms_nonlinear_physics_modules.md) | 5 | 배정 행 표와 수정안 반영 |
| [roms_include_cppdefs.md](../../../models/ROMS/source-analysis/roms_include_cppdefs.md) | 689 | 기존 차이 파일 링크와 수정안 반영 |

위 네 표의 행 수는 note-job-20.tsv의 대상 파일별 행을 세었다.
cppdefs의 행 수와 결론별 개수는 ROMS-assign-*.tsv의 3열을 기준으로 센다.

## roms_nonlinear_core_remaining.md 완료

- 추가·수정 줄: models/ROMS/source-analysis/roms_nonlinear_core_remaining.md:7–8, models/ROMS/source-analysis/roms_nonlinear_core_remaining.md:21, models/ROMS/source-analysis/roms_nonlinear_core_remaining.md:23, models/ROMS/source-analysis/roms_nonlinear_core_remaining.md:56, models/ROMS/source-analysis/roms_nonlinear_core_remaining.md:62, models/ROMS/source-analysis/roms_nonlinear_core_remaining.md:99, models/ROMS/source-analysis/roms_nonlinear_core_remaining.md:117–118, models/ROMS/source-analysis/roms_nonlinear_core_remaining.md:132, models/ROMS/source-analysis/roms_nonlinear_core_remaining.md:135, models/ROMS/source-analysis/roms_nonlinear_core_remaining.md:137–138, models/ROMS/source-analysis/roms_nonlinear_core_remaining.md:140–144, models/ROMS/source-analysis/roms_nonlinear_core_remaining.md:156–157, models/ROMS/source-analysis/roms_nonlinear_core_remaining.md:167–168, models/ROMS/source-analysis/roms_nonlinear_core_remaining.md:173, models/ROMS/source-analysis/roms_nonlinear_core_remaining.md:202, models/ROMS/source-analysis/roms_nonlinear_core_remaining.md:210, models/ROMS/source-analysis/roms_nonlinear_core_remaining.md:212, models/ROMS/source-analysis/roms_nonlinear_core_remaining.md:222–223, models/ROMS/source-analysis/roms_nonlinear_core_remaining.md:225, models/ROMS/source-analysis/roms_nonlinear_core_remaining.md:242–323.
- 넣은 행 수: 69행이다. note-job-20.tsv의 이 파일 배정 69행과 같다.
- 차이 표 위치: `models/ROMS/source-analysis/roms_nonlinear_core_remaining.md:255–323`.
- 반영한 수정안 행 ID: `callflow-nonlinear:RF1-021`, `callflow-nonlinear:RF1-030`, `callflow-nonlinear:RF1-031`, `mixing-bc-forcing:RMF1-954`, `outputs-metadata:OMD-N009`, `outputs-metadata:OMD-N010`, `outputs-metadata:OMD-N042`, `outputs-metadata:OMD-N043`, `outputs-metadata:OMD-N044`, `outputs-metadata:OMD-N045`, `outputs-metadata:OMD-N046`, `outputs-metadata:OMD-N047`, `outputs-metadata:OMD-N048`, `sediment-ice-vegetation:RN1-042`, `theory-numerics:RTN-384`, `theory-numerics:RTN-389`, `theory-numerics:RTN-393`, `theory-numerics:RTN-394`, `tools-guides:RTG-1985`, `tools-guides:RTG-1986`, `tools-guides:RTG-1987`.
- OMD-N046의 DISTRIBUTE 조건은 기존 문장을 유지했다.
- 넣지 않은 행과 이유: 없음.

## roms_4dvar_drivers.md 완료

- 추가·수정 줄: models/ROMS/source-analysis/roms_4dvar_drivers.md:7–8, models/ROMS/source-analysis/roms_4dvar_drivers.md:22, models/ROMS/source-analysis/roms_4dvar_drivers.md:36, models/ROMS/source-analysis/roms_4dvar_drivers.md:49, models/ROMS/source-analysis/roms_4dvar_drivers.md:56, models/ROMS/source-analysis/roms_4dvar_drivers.md:58–61, models/ROMS/source-analysis/roms_4dvar_drivers.md:65, models/ROMS/source-analysis/roms_4dvar_drivers.md:74–80, models/ROMS/source-analysis/roms_4dvar_drivers.md:82, models/ROMS/source-analysis/roms_4dvar_drivers.md:99, models/ROMS/source-analysis/roms_4dvar_drivers.md:110–111, models/ROMS/source-analysis/roms_4dvar_drivers.md:143–144, models/ROMS/source-analysis/roms_4dvar_drivers.md:183, models/ROMS/source-analysis/roms_4dvar_drivers.md:185, models/ROMS/source-analysis/roms_4dvar_drivers.md:192–257.
- 넣은 행 수: 51행이다. note-job-20.tsv의 이 파일 배정 51행과 같다.
- 차이 표 위치: `models/ROMS/source-analysis/roms_4dvar_drivers.md:207–257`.
- 반영한 수정안 행 ID: `callflow-da:RF2-021`, `callflow-da:RF2-022`, `callflow-da:RF2-032`, `da-4dvar:DA1-805`, `da-4dvar:DA1-806`, `da-4dvar:DA1-809`, `da-representer:RT2-392`, `da-representer:RT2-393`, `da-representer:RT2-394`.
- RT2-394의 ROMSJEDI 초기화·run·finalize 설명은 기존 문장을 유지했다.
- RT2-393은 보고서의 RPCG·congrad·MINRES 결론 문장을 옮겼다.
- 넣지 않은 행과 이유: 없음.

## roms_kpp_boundary_layer.md 완료

- 추가·수정 줄: models/ROMS/source-analysis/roms_kpp_boundary_layer.md:6–7, models/ROMS/source-analysis/roms_kpp_boundary_layer.md:22, models/ROMS/source-analysis/roms_kpp_boundary_layer.md:81–82, models/ROMS/source-analysis/roms_kpp_boundary_layer.md:84–85, models/ROMS/source-analysis/roms_kpp_boundary_layer.md:89, models/ROMS/source-analysis/roms_kpp_boundary_layer.md:91–92, models/ROMS/source-analysis/roms_kpp_boundary_layer.md:111–112, models/ROMS/source-analysis/roms_kpp_boundary_layer.md:127, models/ROMS/source-analysis/roms_kpp_boundary_layer.md:129, models/ROMS/source-analysis/roms_kpp_boundary_layer.md:137–139, models/ROMS/source-analysis/roms_kpp_boundary_layer.md:141–182.
- 넣은 행 수: 32행이다. note-job-20.tsv의 이 파일 배정 32행과 같다.
- 차이 표 위치: `models/ROMS/source-analysis/roms_kpp_boundary_layer.md:151–182`.
- 반영한 수정안 행 ID: `mixing-bc-forcing:RMF1-923`, `mixing-bc-forcing:RMF1-924`, `mixing-bc-forcing:RMF1-925`, `mixing-bc-forcing:RMF1-926`, `mixing-bc-forcing:RMF1-927`.
- RMF1-923의 엄격한 준중립 부등호를 유지했다. RMF1-926의 Jwtype 1–9 제한과 두 band 계산을 유지했다.
- 넣지 않은 행과 이유: 없음.

## roms_nonlinear_physics_modules.md 완료

- 추가·수정 줄: models/ROMS/source-analysis/roms_nonlinear_physics_modules.md:6–7, models/ROMS/source-analysis/roms_nonlinear_physics_modules.md:28, models/ROMS/source-analysis/roms_nonlinear_physics_modules.md:56, models/ROMS/source-analysis/roms_nonlinear_physics_modules.md:58, models/ROMS/source-analysis/roms_nonlinear_physics_modules.md:74, models/ROMS/source-analysis/roms_nonlinear_physics_modules.md:84, models/ROMS/source-analysis/roms_nonlinear_physics_modules.md:107, models/ROMS/source-analysis/roms_nonlinear_physics_modules.md:116, models/ROMS/source-analysis/roms_nonlinear_physics_modules.md:118, models/ROMS/source-analysis/roms_nonlinear_physics_modules.md:120, models/ROMS/source-analysis/roms_nonlinear_physics_modules.md:122, models/ROMS/source-analysis/roms_nonlinear_physics_modules.md:128–134, models/ROMS/source-analysis/roms_nonlinear_physics_modules.md:138, models/ROMS/source-analysis/roms_nonlinear_physics_modules.md:140–142, models/ROMS/source-analysis/roms_nonlinear_physics_modules.md:146–154, models/ROMS/source-analysis/roms_nonlinear_physics_modules.md:157–171.
- 넣은 행 수: 5행이다. note-job-20.tsv의 이 파일 배정 5행과 같다.
- 차이 표 위치: `models/ROMS/source-analysis/roms_nonlinear_physics_modules.md:167–171`.
- 반영한 수정안 행 ID: `biology:NT-014`, `biology:NT-015`, `callflow-nonlinear:RF1-022`, `outputs-metadata:OMD-N026`, `outputs-metadata:OMD-N027`, `outputs-metadata:OMD-N028`, `outputs-metadata:OMD-N029`.
- OMD-N026·OMD-N028의 진단 기능 설명을 유지했다. OMD-N027의 절 제목을 유지했다.
- 넣지 않은 행과 이유: 없음.

## roms_include_cppdefs.md 완료

- 추가·수정 줄: models/ROMS/source-analysis/roms_include_cppdefs.md:7–8, models/ROMS/source-analysis/roms_include_cppdefs.md:20, models/ROMS/source-analysis/roms_include_cppdefs.md:24–26, models/ROMS/source-analysis/roms_include_cppdefs.md:29–31, models/ROMS/source-analysis/roms_include_cppdefs.md:36, models/ROMS/source-analysis/roms_include_cppdefs.md:40, models/ROMS/source-analysis/roms_include_cppdefs.md:44, models/ROMS/source-analysis/roms_include_cppdefs.md:46, models/ROMS/source-analysis/roms_include_cppdefs.md:50, models/ROMS/source-analysis/roms_include_cppdefs.md:55, models/ROMS/source-analysis/roms_include_cppdefs.md:58, models/ROMS/source-analysis/roms_include_cppdefs.md:81, models/ROMS/source-analysis/roms_include_cppdefs.md:87, models/ROMS/source-analysis/roms_include_cppdefs.md:92, models/ROMS/source-analysis/roms_include_cppdefs.md:96, models/ROMS/source-analysis/roms_include_cppdefs.md:100, models/ROMS/source-analysis/roms_include_cppdefs.md:102, models/ROMS/source-analysis/roms_include_cppdefs.md:106, models/ROMS/source-analysis/roms_include_cppdefs.md:114–115, models/ROMS/source-analysis/roms_include_cppdefs.md:119, models/ROMS/source-analysis/roms_include_cppdefs.md:121–124, models/ROMS/source-analysis/roms_include_cppdefs.md:127–128, models/ROMS/source-analysis/roms_include_cppdefs.md:132, models/ROMS/source-analysis/roms_include_cppdefs.md:140–141, models/ROMS/source-analysis/roms_include_cppdefs.md:149–150, models/ROMS/source-analysis/roms_include_cppdefs.md:155–157, models/ROMS/source-analysis/roms_include_cppdefs.md:159, models/ROMS/source-analysis/roms_include_cppdefs.md:164–167, models/ROMS/source-analysis/roms_include_cppdefs.md:177, models/ROMS/source-analysis/roms_include_cppdefs.md:181–184, models/ROMS/source-analysis/roms_include_cppdefs.md:186–189, models/ROMS/source-analysis/roms_include_cppdefs.md:212, models/ROMS/source-analysis/roms_include_cppdefs.md:223, models/ROMS/source-analysis/roms_include_cppdefs.md:228–239.
- 반영 행 수: 기존 차이 파일 링크로 689행을 연결했다. ROMS-assign-*.tsv의 3열이 source-analysis/roms_include_cppdefs.md인 배정 689행과 같다.
- 차이 절 위치: `models/ROMS/source-analysis/roms_include_cppdefs.md:233–239`.
- 기존 차이 파일의 행 수는 순서대로 230·230·229행이다. 세 파일의 고유 행 ID 689개는 배정표와 같다.
- 결론별 개수는 A 56·B 34·C 533·D 0·E 20·F 46이다. 이 수는 ROMS-assign-*.tsv의 해당 3열 행에서 셌다.
- 반영한 수정안 행 ID: `testcases:RT1-1522`, `testcases:RT1-1523`, `testcases:RT1-1524`, `testcases:RT1-1525`, `testcases:RT1-1526`, `testcases:RT1-1536`, `mixing-bc-forcing:RMF1-965`, `sediment-ice-vegetation:RN1-043`, `sediment-ice-vegetation:RN1-047`, `coupling-nesting-parallel:RCN-1981`, `coupling-nesting-parallel:RCN-1982`, `theory-numerics:RTN-403`, `biology:NT-012`, `biology:NT-013`, `build-options-history:RBH-3448`, `build-options-history:RBH-3449`, `build-options-history:RBH-3450`, `build-options-history:RBH-3451`, `build-options-history:RBH-3452`, `build-options-history:RBH-3453`, `build-options-history:RBH-3454`, `build-options-history:RBH-3455`, `build-options-history:RBH-3456`, `build-options-history:RBH-3457`, `build-options-history:RBH-3458`, `build-options-history:RBH-3459`, `build-options-history:RBH-3460`, `build-options-history:RBH-3461`, `build-options-history:RBH-3462`, `build-options-history:RBH-3463`, `build-options-history:RBH-3464`, `build-options-history:RBH-3465`, `build-options-history:RBH-3466`, `build-options-history:RBH-3467`, `build-options-history:RBH-3468`, `build-options-history:RBH-3469`, `build-options-history:RBH-3470`, `build-options-history:RBH-3471`, `build-options-history:RBH-3472`, `build-options-history:RBH-3473`, `build-options-history:RBH-3474`, `build-options-history:RBH-3475`, `da-representer:RT2-395`, `da-representer:RT2-396`, `outputs-metadata:OMD-N024`, `outputs-metadata:OMD-N025`, `da-4dvar:DA1-815`, `da-4dvar:DA1-816`.
- 유지한 조건·출처의 수정안 행 ID: `testcases:RT1-1526`, `mixing-bc-forcing:RMF1-965`, `sediment-ice-vegetation:RN1-043`, `coupling-nesting-parallel:RCN-1981`, `theory-numerics:RTN-403`, `biology:NT-013`, `build-options-history:RBH-3452`, `build-options-history:RBH-3455`, `build-options-history:RBH-3458`, `build-options-history:RBH-3460`, `build-options-history:RBH-3462`, `build-options-history:RBH-3463`, `build-options-history:RBH-3464`, `build-options-history:RBH-3466`, `build-options-history:RBH-3469`, `build-options-history:RBH-3472`, `build-options-history:RBH-3473`, `build-options-history:RBH-3474`, `da-representer:RT2-396`, `outputs-metadata:OMD-N025`, `da-4dvar:DA1-816`.
- 넣지 않은 행과 이유: 없음.

## 최종 배정·형식 점검

- 직접 표의 행 ID는 note-job-20.tsv의 157개와 같다. 네 표의 행 수는 69·51·32·5이다.
- Markdown 표를 메모리에서 파싱했다. 배정 157행은 모두 6열로 렌더됐다.
- cppdefs 차이 파일의 고유 행 ID 689개는 ROMS-assign-*.tsv의 해당 3열 행과 같다.
- 수정안 행 ID는 노트별로 21·9·5·7·48개이다. 보고서의 대상 노트 참조 행에서 센 값과 같다.
- 다섯 노트의 citation_status를 유지했다. 다섯 노트의 last_source_check와 verification_method는 요청한 값과 같다.
- 상대 링크와 금지 문자열 점검을 통과했다. git diff --check를 통과했다.
- 최종 형식 보완 줄: `models/ROMS/source-analysis/roms_4dvar_drivers.md:135`이다. 인용 앞의 공백을 추가해 시간 구간을 링크로 읽는 문제를 고쳤다.
- RF2-032의 코드 원문은 계산 흐름 보고서의 최소화기 호출·zgrad0·px·ADmodVal 인용을 연결했다.
- 넣지 않은 행과 이유: 없음.
