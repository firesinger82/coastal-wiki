# SFINCS·XBeach 10-12 결론 검증

검증일: 2026-10-12.
대상은 작업 시작 시 지정 노트에 대해 읽기 전용 `git diff -U0 HEAD -- <노트>`에서 얻은 추가 줄이다.
작업 중 바뀐 diff를 새 대상으로 다시 세지 않았다.
대상은 664줄이다. 비어 있지 않은 줄은 552줄이다. 공백·표 구분선·메타데이터·도식 줄도 대상 수에 포함했다.
숫자의 단위는 서로 구분한다. 정정·보완·이상 없음은 시작 시점의 추가 줄 수다. 분류 변경은 기존 보고서 원행 ID 수다.
한 줄에 정정과 보완이 함께 있으면 정정에 한 번만 집계했다.
정본 앵커 지정과 중복 문단의 링크 전환은 보완으로 집계했다.
새 E 후보 3개는 기존 원행의 분류 변경 수에 포함하지 않았다.

검증 방법: 명시적 로컬 인용은 `nl -ba`로 열었다. 같은 줄의 식·연산자·상수·분기와 주장을 대조했다. 축약 경로와 같은 파일의 `:줄` 표기는 해당 문단의 파일로 풀어 확인했다.
기본값 표의 기존 문장도 입력 리더와 동봉 RST 원문에 대조했다. 권고값·성능 수치는 문서의 주장으로 확인했다.
과거 태그의 근거는 `external-results-sf.md`에 보존된 해당 판 원문 인용과 대조했다. 현재 로컬 소스의 같은 줄 번호를 과거 판의 원문으로 대신하지 않았다.
B070·B080은 논문의 원문 수식을 추가로 열었다. 외부 판정 보고서의 결론을 그대로 채택하지 않았다.
E 후보에서는 초기화·변환·제한·다른 분기의 보정과 의도 설명을 검색했다.
모델 실행과 컴파일은 하지 않았다. git 상태를 바꾸는 명령은 실행하지 않았다.
쓰기 대상은 지정 노트, 허용 보고서의 §5, 이 산출물이다. `external-results-*.md`와 ADCIRC·EFDC 파일은 변경하지 않았다.

## 노트별 대조 수

| 노트 | 대상 + 줄 | 비공백 | 정정 | 보완 | 이상 없음 |
|---|---:|---:|---:|---:|---:|
| [SFINCS/sfincs-model-building-running.md](../../../models/SFINCS/manual-notes/sfincs-model-building-running.md) | 17 | 13 | 9 | 0 | 8 |
| [SFINCS/sfincs-numerical-implementation.md](../../../models/SFINCS/manual-notes/sfincs-numerical-implementation.md) | 100 | 86 | 4 | 9 | 87 |
| [SFINCS/sfincs-parameters-io-reference.md](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md) | 166 | 157 | 9 | 46 | 111 |
| [SFINCS/sfincs-v2.4.0-galibier-changelog-known-issues.md](../../../models/SFINCS/manual-notes/sfincs-v2.4.0-galibier-changelog-known-issues.md) | 21 | 18 | 1 | 8 | 12 |
| [SFINCS/sfincs-architecture-source-map.md](../../../models/SFINCS/source-analysis/sfincs-architecture-source-map.md) | 49 | 40 | 0 | 5 | 44 |
| [SFINCS/sfincs_boundaries_forcing.md](../../../models/SFINCS/source-analysis/sfincs_boundaries_forcing.md) | 30 | 20 | 0 | 7 | 23 |
| [SFINCS/sfincs_flow_solver.md](../../../models/SFINCS/source-analysis/sfincs_flow_solver.md) | 37 | 29 | 2 | 5 | 30 |
| [SFINCS/sfincs_infiltration.md](../../../models/SFINCS/source-analysis/sfincs_infiltration.md) | 13 | 9 | 0 | 5 | 8 |
| [SFINCS/sfincs_io_data.md](../../../models/SFINCS/source-analysis/sfincs_io_data.md) | 36 | 28 | 0 | 4 | 32 |
| [SFINCS/sfincs_nonhydrostatic_wavemaker.md](../../../models/SFINCS/source-analysis/sfincs_nonhydrostatic_wavemaker.md) | 21 | 13 | 0 | 2 | 19 |
| [SFINCS/sfincs_snapwave.md](../../../models/SFINCS/source-analysis/sfincs_snapwave.md) | 50 | 35 | 2 | 3 | 45 |
| [SFINCS/sfincs_structures_physics.md](../../../models/SFINCS/source-analysis/sfincs_structures_physics.md) | 16 | 10 | 0 | 3 | 13 |
| [SFINCS/sfincs_subgrid_quadtree.md](../../../models/SFINCS/source-analysis/sfincs_subgrid_quadtree.md) | 25 | 17 | 1 | 3 | 21 |
| [XBeach/xbeach-coupled-physics-contracts.md](../../../models/XBeach/source-analysis/xbeach-coupled-physics-contracts.md) | 39 | 36 | 0 | 2 | 37 |
| [XBeach/xbeach_mode_dispatch.md](../../../models/XBeach/source-analysis/xbeach_mode_dispatch.md) | 3 | 3 | 0 | 0 | 3 |
| [XBeach/xbeach_nonh.md](../../../models/XBeach/source-analysis/xbeach_nonh.md) | 18 | 16 | 0 | 0 | 18 |
| [XBeach/xbeach_vegetation.md](../../../models/XBeach/source-analysis/xbeach_vegetation.md) | 23 | 22 | 0 | 2 | 21 |
| 합계 | 664 | 552 | 28 | 104 | 532 |

## 정정·보완 목록

아래 링크는 수정 후 노트 줄 번호이다. 괄호의 원래 줄 번호는 작업 시작 시 + 줄 번호이다.
각 변경 줄의 끝에는 `[10-12 결론 검증 정정]` 또는 `[10-12 결론 검증 보완]`을 붙였다.

| 노트:줄 | 구분 | 이전 요지 | 새 요지 | 근거 |
|---|---|---|---|---|
| [SFINCS/sfincs-model-building-running.md:64](../../../models/SFINCS/manual-notes/sfincs-model-building-running.md:64) (원래 64) | 정정 | 외부 HydroMT-SFINCS API를 D로 분류 | 외부 도구 API이므로 H로 변경 | docs/input.rst:13; raw 전체 rg -i -uuu; Python 함수 정의 검색 |
| [SFINCS/sfincs-model-building-running.md:65](../../../models/SFINCS/manual-notes/sfincs-model-building-running.md:65) (원래 65) | 정정 | 외부 HydroMT-SFINCS API를 D로 분류 | 외부 도구 API이므로 H로 변경 | docs/input.rst:13; raw 전체 rg -i -uuu; Python 함수 정의 검색 |
| [SFINCS/sfincs-model-building-running.md:66](../../../models/SFINCS/manual-notes/sfincs-model-building-running.md:66) (원래 66) | 정정 | 외부 HydroMT-SFINCS API를 D로 분류 | 외부 도구 API이므로 H로 변경 | docs/input.rst:13; raw 전체 rg -i -uuu; Python 함수 정의 검색 |
| [SFINCS/sfincs-model-building-running.md:67](../../../models/SFINCS/manual-notes/sfincs-model-building-running.md:67) (원래 67) | 정정 | 외부 HydroMT-SFINCS API를 D로 분류 | 외부 도구 API이므로 H로 변경 | docs/input.rst:13; raw 전체 rg -i -uuu; Python 함수 정의 검색 |
| [SFINCS/sfincs-model-building-running.md:68](../../../models/SFINCS/manual-notes/sfincs-model-building-running.md:68) (원래 68) | 정정 | 외부 HydroMT-SFINCS API를 D로 분류 | 외부 도구 API이므로 H로 변경 | docs/input.rst:13; raw 전체 rg -i -uuu; Python 함수 정의 검색 |
| [SFINCS/sfincs-model-building-running.md:69](../../../models/SFINCS/manual-notes/sfincs-model-building-running.md:69) (원래 69) | 정정 | 외부 HydroMT-SFINCS API를 D로 분류 | 외부 도구 API이므로 H로 변경 | docs/input.rst:13; raw 전체 rg -i -uuu; Python 함수 정의 검색 |
| [SFINCS/sfincs-model-building-running.md:70](../../../models/SFINCS/manual-notes/sfincs-model-building-running.md:70) (원래 70) | 정정 | 외부 HydroMT-SFINCS API를 D로 분류 | 외부 도구 API이므로 H로 변경 | docs/input.rst:13; raw 전체 rg -i -uuu; Python 함수 정의 검색 |
| [SFINCS/sfincs-model-building-running.md:71](../../../models/SFINCS/manual-notes/sfincs-model-building-running.md:71) (원래 71) | 정정 | 외부 HydroMT-SFINCS API를 D로 분류 | 외부 도구 API이므로 H로 변경 | docs/input.rst:13; raw 전체 rg -i -uuu; Python 함수 정의 검색 |
| [SFINCS/sfincs-model-building-running.md:72](../../../models/SFINCS/manual-notes/sfincs-model-building-running.md:72) (원래 72) | 정정 | 외부 HydroMT-SFINCS API를 D로 분류 | 외부 도구 API이므로 H로 변경 | docs/input.rst:13; raw 전체 rg -i -uuu; Python 함수 정의 검색 |
| [SFINCS/sfincs-numerical-implementation.md:105](../../../models/SFINCS/manual-notes/sfincs-numerical-implementation.md:105) (원래 105) | 보완 | 외부 판정 상세 문단 중복 | 정본으로 통합 | B024 정본 |
| [SFINCS/sfincs-numerical-implementation.md:109](../../../models/SFINCS/manual-notes/sfincs-numerical-implementation.md:109) (원래 109) | 정정 | 현재 이류 계산 근거를 sfincs_advection_diffusion.f90로 연결 | 실제 운동량 루틴의 이류 분기로 연결 | sfincs_momentum.f90:413–507 |
| [SFINCS/sfincs-numerical-implementation.md:165](../../../models/SFINCS/manual-notes/sfincs-numerical-implementation.md:165) (원래 165) | 정정 | 외부 판정 상세 문단 중복 및 잘못된 분류 | 정본으로 통합; 정정된 분류 반영 | B080 정본 |
| [SFINCS/sfincs-numerical-implementation.md:176](../../../models/SFINCS/manual-notes/sfincs-numerical-implementation.md:176) (원래 176) | 정정 | dtmin 계산식의 좌표계 조건 누락 | 투영좌표 식과 공통 중단 검사를 분리 | sfincs_domain.f90:1403,1475,1539; sfincs_lib.f90:634 |
| [SFINCS/sfincs-numerical-implementation.md:177](../../../models/SFINCS/manual-notes/sfincs-numerical-implementation.md:177) (원래 177) | 보완 | uvmax 임계값의 좌표계 조건 생략 | 투영좌표 조건 추가 | sfincs_domain.f90:1403,1475,1539 |
| [SFINCS/sfincs-numerical-implementation.md:258](../../../models/SFINCS/manual-notes/sfincs-numerical-implementation.md:258) (원래 258) | 보완 | 외부 판정 상세 문단 중복 | 정본으로 통합 | B067 정본 |
| [SFINCS/sfincs-numerical-implementation.md:259](../../../models/SFINCS/manual-notes/sfincs-numerical-implementation.md:259) (원래 259) | 보완 | 외부 판정 상세 문단 중복 | 정본으로 통합 | B068 정본 |
| [SFINCS/sfincs-numerical-implementation.md:260](../../../models/SFINCS/manual-notes/sfincs-numerical-implementation.md:260) (원래 260) | 보완 | 외부 판정 상세 문단 중복 | 정본으로 통합 | B069 정본 |
| [SFINCS/sfincs-numerical-implementation.md:261](../../../models/SFINCS/manual-notes/sfincs-numerical-implementation.md:261) (원래 261) | 정정 | 외부 판정 상세 문단 중복 및 잘못된 분류 | 정본으로 통합; 정정된 분류 반영 | B070 정본 |
| [SFINCS/sfincs-numerical-implementation.md:262](../../../models/SFINCS/manual-notes/sfincs-numerical-implementation.md:262) (원래 262) | 보완 | 외부 판정 상세 문단 중복 | 정본으로 통합 | B103 정본 |
| [SFINCS/sfincs-numerical-implementation.md:263](../../../models/SFINCS/manual-notes/sfincs-numerical-implementation.md:263) (원래 263) | 보완 | 외부 판정 상세 문단 중복 | 정본으로 통합 | B110 정본 |
| [SFINCS/sfincs-numerical-implementation.md:267](../../../models/SFINCS/manual-notes/sfincs-numerical-implementation.md:267) (원래 267) | 보완 | 누적 강수 E 설명 중복 | sfincs_infiltration.md의 정본 링크로 통합 | B047·C021 정본; sfincs_infiltration.f90:44,52–55 |
| [SFINCS/sfincs-numerical-implementation.md:308](../../../models/SFINCS/manual-notes/sfincs-numerical-implementation.md:308) (원래 308) | 보완 | 같은 릴리스 링크 오류 문단 중복 | 변경 이력 노트로 통합 | docs/developments.rst:283; external-results-sf.md B103 |
| [SFINCS/sfincs-parameters-io-reference.md:53](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md:53) (원래 53) | 보완 | 중복 근거가 여러 위치에 흩어짐 | 정본 앵커 지정 | [대조 보고서 §5 A013·C001](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:943) |
| [SFINCS/sfincs-parameters-io-reference.md:57](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md:57) (원래 57) | 보완 | 중복 근거가 여러 위치에 흩어짐 | 정본 앵커 지정 | [대조 보고서 §5 A017·C002](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:944) |
| [SFINCS/sfincs-parameters-io-reference.md:58](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md:58) (원래 58) | 보완 | 중복 근거가 여러 위치에 흩어짐 | 정본 앵커 지정 | [대조 보고서 §5 A019](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:946) |
| [SFINCS/sfincs-parameters-io-reference.md:68](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md:68) (원래 68) | 정정 | 초기 수위 bed level 위라는 모호한 설명 | 기준면에 대한 수위로 명시 | sfincs_input.f90:77; sfincs_initial_conditions.F90:38–39 |
| [SFINCS/sfincs-parameters-io-reference.md:76](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md:76) (원래 76) | 보완 | 중복 근거가 여러 위치에 흩어짐 | 정본 앵커 지정 | [대조 보고서 §5 A029·K066·C003](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:947) |
| [SFINCS/sfincs-parameters-io-reference.md:93](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md:93) (원래 93) | 보완 | Green-Ampt E 근거 중복 | 조건·반대 근거를 포함한 정본 링크 | sfincs_infiltration.f90:828–889 |
| [SFINCS/sfincs-parameters-io-reference.md:95](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md:95) (원래 95) | 보완 | Green-Ampt E 근거 중복 | 조건·반대 근거를 포함한 정본 링크 | sfincs_infiltration.f90:828–889 |
| [SFINCS/sfincs-parameters-io-reference.md:117](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md:117) (원래 117) | 보완 | uvmax 임계값의 좌표계 조건 생략 | 투영좌표 조건 추가 | sfincs_domain.f90:1403,1475,1539 |
| [SFINCS/sfincs-parameters-io-reference.md:119](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md:119) (원래 119) | 보완 | 중복 근거가 여러 위치에 흩어짐 | 정본 앵커 지정 | [대조 보고서 §5 A038·C004](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:949) |
| [SFINCS/sfincs-parameters-io-reference.md:121](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md:121) (원래 121) | 정정 | dtmin 계산의 좌표계 제한과 전체 검색이 빠짐 | 투영좌표로 한정; raw 전체 검색; 구면좌표 E 연결 | [대조 보고서 §5 A040](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:950) |
| [SFINCS/sfincs-parameters-io-reference.md:152](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md:152) (원래 152) | 보완 | 중복 근거가 여러 위치에 흩어짐 | 정본 앵커 지정 | [대조 보고서 §5 A049·C007](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:953) |
| [SFINCS/sfincs-parameters-io-reference.md:162](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md:162) (원래 162) | 보완 | 중복 근거가 여러 위치에 흩어짐 | 정본 앵커 지정 | [대조 보고서 §5 A059·A060·K059·K060·C009](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:955) |
| [SFINCS/sfincs-parameters-io-reference.md:163](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md:163) (원래 163) | 보완 | map과 his 행에 같은 전체 근거 반복 | 공통 조건은 map 행으로 통합 | sfincs_input.f90:86–87; 주 표의 출력 형식 덮어쓰기 조건 |
| [SFINCS/sfincs-parameters-io-reference.md:165](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md:165) (원래 165) | 보완 | 중복 근거가 여러 위치에 흩어짐 | 정본 앵커 지정 | [대조 보고서 §5 C011](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:1057) |
| [SFINCS/sfincs-parameters-io-reference.md:169](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md:169) (원래 169) | 보완 | 중복 근거가 여러 위치에 흩어짐 | 정본 앵커 지정 | [대조 보고서 §5 A070·C010](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:956) |
| [SFINCS/sfincs-parameters-io-reference.md:171](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md:171) (원래 171) | 보완 | 배수 이력 설명 중복 | 배수 절에 정본을 두고 출력 절에서 연결 | sfincs_output.f90:253–261,660–663; sfincs_ncoutput.F90:2206,3459–3470; sfincs_lib.f90:470–474 |
| [SFINCS/sfincs-parameters-io-reference.md:172](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md:172) (원래 172) | 보완 | 배수 이력 설명 중복 | 배수 절에 정본을 두고 출력 절에서 연결 | sfincs_output.f90:253–261,660–663; sfincs_ncoutput.F90:2206,3459–3470; sfincs_lib.f90:470–474 |
| [SFINCS/sfincs-parameters-io-reference.md:173](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md:173) (원래 173) | 보완 | 중복 근거가 여러 위치에 흩어짐 | 정본 앵커 지정 | [대조 보고서 §5 A074](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:957) |
| [SFINCS/sfincs-parameters-io-reference.md:180](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md:180) (원래 180) | 보완 | 건조 면 E 근거 중복 | 정본 링크 | sfincs_timestep_analysis.f90:17–19,43–55,123–124,178–188 |
| [SFINCS/sfincs-parameters-io-reference.md:191](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md:191) (원래 191) | 정정 | 예시 파일명을 읽기 기본명으로 표기 | 예시와 리더 기본값 구분 | sfincs_input.f90:212–223 |
| [SFINCS/sfincs-parameters-io-reference.md:201](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md:201) (원래 201) | 보완 | 중복 근거가 여러 위치에 흩어짐 | 정본 앵커 지정 | [대조 보고서 §5 A090·A091·C013](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:960) |
| [SFINCS/sfincs-parameters-io-reference.md:203](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md:203) (원래 203) | 정정 | B049와 B080 근거 중복; 거칠기 식 일치 | 두 정본 링크; B080 G 반영 | docs/input.rst:267; sfincs_subgrid.F90:329,347; sfincs_momentum.f90:364 |
| [SFINCS/sfincs-parameters-io-reference.md:208](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md:208) (원래 208) | 보완 | type 2 긴 근거 중복 | 정본 링크; 현재 q·uvmean 표기 유지 | A100·C014 정본 |
| [SFINCS/sfincs-parameters-io-reference.md:225](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md:225) (원래 225) | 보완 | type 2 E 설명 중복 | 쓰기 경로와 읽기 조건의 정본 링크 | sfincs_initial_conditions.F90:196,227–233; sfincs_output.f90:704–738 |
| [SFINCS/sfincs-parameters-io-reference.md:318](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md:318) (원래 318) | 보완 | Darcy–Weisbach D의 검색 범위 불명확 | raw 전체의 유일한 일치 위치 기재 | docs/input_structures.rst:222; sfincs_discharges.f90:398,402,412 |
| [SFINCS/sfincs-parameters-io-reference.md:319](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md:319) (원래 319) | 보완 | 중복 근거가 여러 위치에 흩어짐 | 정본 앵커 지정 | 해당 행의 원문 인용 |
| [SFINCS/sfincs-parameters-io-reference.md:320](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md:320) (원래 320) | 보완 | 중복 근거가 여러 위치에 흩어짐 | 정본 앵커 지정 | 해당 행의 원문 인용 |
| [SFINCS/sfincs-parameters-io-reference.md:321](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md:321) (원래 321) | 정정 | 결론의 출력 시각이 기록 시각 tout으로 오해될 수 있음 | 출력 호출 당시의 qtsrc로 한정; tout와 t 차이 보존 | sfincs_lib.f90:470,474,628; sfincs_output.f90:663; sfincs_ncoutput.F90:3467 |
| [SFINCS/sfincs-parameters-io-reference.md:322](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md:322) (원래 322) | 정정 | 결론의 출력 시각이 기록 시각 tout으로 오해될 수 있음 | 출력 호출 당시의 qtsrc로 한정; tout와 t 차이 보존 | sfincs_lib.f90:470,474,628; sfincs_output.f90:663; sfincs_ncoutput.F90:3467 |
| [SFINCS/sfincs-parameters-io-reference.md:357](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md:357) (원래 357) | 보완 | 배수 이력 설명 중복 | 배수 절에 정본을 두고 출력 절에서 연결 | sfincs_output.f90:253–261,660–663; sfincs_ncoutput.F90:2206,3459–3470; sfincs_lib.f90:470–474 |
| [SFINCS/sfincs-parameters-io-reference.md:358](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md:358) (원래 358) | 보완 | 배수 이력 설명 중복 | 배수 절에 정본을 두고 출력 절에서 연결 | sfincs_output.f90:253–261,660–663; sfincs_ncoutput.F90:2206,3459–3470; sfincs_lib.f90:470–474 |
| [SFINCS/sfincs-parameters-io-reference.md:363](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md:363) (원래 363) | 정정 | 시작 로그 원문 뒤쪽 하이픈 개수 오류 | sfincs_lib.f90:326의 문자열로 정정 | sfincs_lib.f90:326 |
| [SFINCS/sfincs-parameters-io-reference.md:365](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md:365) (원래 365) | 정정 | dtmin 계산식의 좌표계 조건 누락 | 투영좌표 식과 공통 중단 검사를 분리 | sfincs_domain.f90:1403,1475,1539; sfincs_lib.f90:634 |
| [SFINCS/sfincs-parameters-io-reference.md:387](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md:387) (원래 387) | 보완 | 같은 노트 표와 부록에 긴 근거 반복 | 주 표를 정본으로 두고 부록은 링크 | 해당 정본의 docs·입력 리더·사용식 |
| [SFINCS/sfincs-parameters-io-reference.md:388](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md:388) (원래 388) | 보완 | 같은 노트 표와 부록에 긴 근거 반복 | 주 표를 정본으로 두고 부록은 링크 | 해당 정본의 docs·입력 리더·사용식 |
| [SFINCS/sfincs-parameters-io-reference.md:389](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md:389) (원래 389) | 보완 | 같은 노트 표와 부록에 긴 근거 반복 | 주 표를 정본으로 두고 부록은 링크 | 해당 정본의 docs·입력 리더·사용식 |
| [SFINCS/sfincs-parameters-io-reference.md:390](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md:390) (원래 390) | 보완 | 같은 노트 표와 부록에 긴 근거 반복 | 주 표를 정본으로 두고 부록은 링크 | 해당 정본의 docs·입력 리더·사용식 |
| [SFINCS/sfincs-parameters-io-reference.md:391](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md:391) (원래 391) | 보완 | 같은 노트 표와 부록에 긴 근거 반복 | 주 표를 정본으로 두고 부록은 링크 | 해당 정본의 docs·입력 리더·사용식 |
| [SFINCS/sfincs-parameters-io-reference.md:394](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md:394) (원래 394) | 보완 | 같은 노트 표와 부록에 긴 근거 반복 | 주 표를 정본으로 두고 부록은 링크 | 해당 정본의 docs·입력 리더·사용식 |
| [SFINCS/sfincs-parameters-io-reference.md:396](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md:396) (원래 396) | 보완 | 같은 노트 표와 부록에 긴 근거 반복 | 주 표를 정본으로 두고 부록은 링크 | 해당 정본의 docs·입력 리더·사용식 |
| [SFINCS/sfincs-parameters-io-reference.md:397](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md:397) (원래 397) | 보완 | 같은 노트 표와 부록에 긴 근거 반복 | 주 표를 정본으로 두고 부록은 링크 | 해당 정본의 docs·입력 리더·사용식 |
| [SFINCS/sfincs-parameters-io-reference.md:398](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md:398) (원래 398) | 보완 | 같은 노트 표와 부록에 긴 근거 반복 | 주 표를 정본으로 두고 부록은 링크 | 해당 정본의 docs·입력 리더·사용식 |
| [SFINCS/sfincs-parameters-io-reference.md:399](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md:399) (원래 399) | 보완 | 같은 노트 표와 부록에 긴 근거 반복 | 주 표를 정본으로 두고 부록은 링크 | 해당 정본의 docs·입력 리더·사용식 |
| [SFINCS/sfincs-parameters-io-reference.md:400](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md:400) (원래 400) | 보완 | 같은 노트 표와 부록에 긴 근거 반복 | 주 표를 정본으로 두고 부록은 링크 | 해당 정본의 docs·입력 리더·사용식 |
| [SFINCS/sfincs-parameters-io-reference.md:402](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md:402) (원래 402) | 보완 | 같은 노트 표와 부록에 긴 근거 반복 | 주 표를 정본으로 두고 부록은 링크 | 해당 정본의 docs·입력 리더·사용식 |
| [SFINCS/sfincs-parameters-io-reference.md:403](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md:403) (원래 403) | 보완 | 같은 노트 표와 부록에 긴 근거 반복 | 주 표를 정본으로 두고 부록은 링크 | 해당 정본의 docs·입력 리더·사용식 |
| [SFINCS/sfincs-parameters-io-reference.md:404](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md:404) (원래 404) | 보완 | type 2 긴 근거 중복 | 정본 링크; 현재 q·uvmean 표기 유지 | A100·C014 정본 |
| [SFINCS/sfincs-parameters-io-reference.md:418](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md:418) (원래 418) | 정정 | dtmin 계산식의 좌표계 조건 누락 | 투영좌표 식과 공통 중단 검사를 분리 | sfincs_domain.f90:1403,1475,1539; sfincs_lib.f90:634 |
| [SFINCS/sfincs-parameters-io-reference.md:419](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md:419) (원래 419) | 보완 | dtmin 근거 반복 | 전체 검색을 기록한 정본으로 통합 | raw 전체 dtmin 검색; sfincs_domain.f90:1403,1475,1539 |
| [SFINCS/sfincs-parameters-io-reference.md:421](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md:421) (원래 421) | 보완 | D 검색 범위·보조 프로그램 결과가 불명확 | 독립 SnapWave 일치와 주 입력 부재를 구분 | raw 전체 rg -i -uuu bwvfile; sfincs_snapwave.f90:672,674–675 |
| [SFINCS/sfincs-parameters-io-reference.md:422](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md:422) (원래 422) | 보완 | D 검색 범위·보조 프로그램 결과가 불명확 | 독립 SnapWave 일치와 주 입력 부재를 구분 | raw 전체 rg -i -uuu bhsfile; sfincs_snapwave.f90:672,674–675 |
| [SFINCS/sfincs-parameters-io-reference.md:423](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md:423) (원래 423) | 보완 | D 검색 범위·보조 프로그램 결과가 불명확 | 독립 SnapWave 일치와 주 입력 부재를 구분 | raw 전체 rg -i -uuu btpfile; sfincs_snapwave.f90:672,674–675 |
| [SFINCS/sfincs-parameters-io-reference.md:424](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md:424) (원래 424) | 보완 | 헤더 필드 D의 검색 결과 미기재 | raw 전체 결과를 필드별 검색어와 함께 명시 | sfincs_spiderweb.f90:170–193; raw 전체 검색 |
| [SFINCS/sfincs-parameters-io-reference.md:427](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md:427) (원래 427) | 보완 | 외부 판정 상세 문단 중복 | 정본으로 통합 | B068 정본 |
| [SFINCS/sfincs-parameters-io-reference.md:445](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md:445) (원래 445) | 보완 | 같은 릴리스 링크 오류 문단 중복 | 변경 이력 노트로 통합 | docs/developments.rst:283; external-results-sf.md B103 |
| [SFINCS/sfincs-v2.4.0-galibier-changelog-known-issues.md:36](../../../models/SFINCS/manual-notes/sfincs-v2.4.0-galibier-changelog-known-issues.md:36) (원래 36) | 보완 | 외부 판정 상세 문단 중복 | 정본으로 통합 | B042 정본 |
| [SFINCS/sfincs-v2.4.0-galibier-changelog-known-issues.md:40](../../../models/SFINCS/manual-notes/sfincs-v2.4.0-galibier-changelog-known-issues.md:40) (원래 40) | 정정 | 파력의 가속도 전달 | 단위폭 유량 변화율 전달; 정본 링크 | sfincs_snapwave.f90:502,563–564; sfincs_momentum.f90:606,677 |
| [SFINCS/sfincs-v2.4.0-galibier-changelog-known-issues.md:50](../../../models/SFINCS/manual-notes/sfincs-v2.4.0-galibier-changelog-known-issues.md:50) (원래 50) | 보완 | 누적 강수 E 설명 중복 | sfincs_infiltration.md의 정본 링크로 통합 | B047·C021 정본; sfincs_infiltration.f90:44,52–55 |
| [SFINCS/sfincs-v2.4.0-galibier-changelog-known-issues.md:56](../../../models/SFINCS/manual-notes/sfincs-v2.4.0-galibier-changelog-known-issues.md:56) (원래 56) | 보완 | 외부 판정 상세 문단 중복 | 정본으로 통합 | B048 정본 |
| [SFINCS/sfincs-v2.4.0-galibier-changelog-known-issues.md:57](../../../models/SFINCS/manual-notes/sfincs-v2.4.0-galibier-changelog-known-issues.md:57) (원래 57) | 보완 | 외부 판정 상세 문단 중복 | 정본으로 통합 | B049 정본 |
| [SFINCS/sfincs-v2.4.0-galibier-changelog-known-issues.md:58](../../../models/SFINCS/manual-notes/sfincs-v2.4.0-galibier-changelog-known-issues.md:58) (원래 58) | 보완 | 외부 판정 상세 문단 중복 | 정본으로 통합 | B050 정본 |
| [SFINCS/sfincs-v2.4.0-galibier-changelog-known-issues.md:59](../../../models/SFINCS/manual-notes/sfincs-v2.4.0-galibier-changelog-known-issues.md:59) (원래 59) | 보완 | 외부 판정 상세 문단 중복 | 정본으로 통합 | B051 정본 |
| [SFINCS/sfincs-v2.4.0-galibier-changelog-known-issues.md:65](../../../models/SFINCS/manual-notes/sfincs-v2.4.0-galibier-changelog-known-issues.md:65) (원래 65) | 보완 | 누적 강수 E 설명 중복 | sfincs_infiltration.md의 정본 링크로 통합 | B047·C021 정본; sfincs_infiltration.f90:44,52–55 |
| [SFINCS/sfincs-v2.4.0-galibier-changelog-known-issues.md:83](../../../models/SFINCS/manual-notes/sfincs-v2.4.0-galibier-changelog-known-issues.md:83) (원래 83) | 보완 | 누적 강수 E 설명 중복 | sfincs_infiltration.md의 정본 링크로 통합 | B047·C021 정본; sfincs_infiltration.f90:44,52–55 |
| [SFINCS/sfincs-architecture-source-map.md:221](../../../models/SFINCS/source-analysis/sfincs-architecture-source-map.md:221) (원래 221) | 보완 | 결함 후보의 상세 설명 중복 | 목록은 정본으로 연결 | 각 정본의 원문·반대 경로 |
| [SFINCS/sfincs-architecture-source-map.md:222](../../../models/SFINCS/source-analysis/sfincs-architecture-source-map.md:222) (원래 222) | 보완 | 결함 후보의 상세 설명 중복 | 목록은 정본으로 연결 | 각 정본의 원문·반대 경로 |
| [SFINCS/sfincs-architecture-source-map.md:223](../../../models/SFINCS/source-analysis/sfincs-architecture-source-map.md:223) (원래 223) | 보완 | 결함 후보의 상세 설명 중복 | 목록은 정본으로 연결 | 각 정본의 원문·반대 경로 |
| [SFINCS/sfincs-architecture-source-map.md:224](../../../models/SFINCS/source-analysis/sfincs-architecture-source-map.md:224) (원래 224) | 보완 | 결함 후보의 상세 설명 중복 | 목록은 정본으로 연결 | 각 정본의 원문·반대 경로 |
| [SFINCS/sfincs-architecture-source-map.md:228](../../../models/SFINCS/source-analysis/sfincs-architecture-source-map.md:228) (원래 228) | 보완 | 같은 릴리스 링크 오류 문단 중복 | 변경 이력 노트로 통합 | docs/developments.rst:283; external-results-sf.md B103 |
| [SFINCS/sfincs_boundaries_forcing.md:95](../../../models/SFINCS/source-analysis/sfincs_boundaries_forcing.md:95) (원래 95) | 보완 | 중복 근거가 여러 위치에 흩어짐 | 정본 앵커 지정 | [대조 보고서 §5 B050](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:1028) |
| [SFINCS/sfincs_boundaries_forcing.md:102](../../../models/SFINCS/source-analysis/sfincs_boundaries_forcing.md:102) (원래 102) | 보완 | t와 tspinup 비교만 제시 | 기간→종료 시각 변환을 확인하여 단위·원점 결함 기각 | sfincs_input.f90:365–369; sfincs_boundaries.f90:851–853 |
| [SFINCS/sfincs_boundaries_forcing.md:160](../../../models/SFINCS/source-analysis/sfincs_boundaries_forcing.md:160) (원래 160) | 보완 | Darcy–Weisbach D의 검색 범위 불명확 | raw 전체의 유일한 일치 위치 기재 | docs/input_structures.rst:222; sfincs_discharges.f90:398,402,412 |
| [SFINCS/sfincs_boundaries_forcing.md:206](../../../models/SFINCS/source-analysis/sfincs_boundaries_forcing.md:206) (원래 206) | 보완 | 중복 근거가 여러 위치에 흩어짐 | 정본 앵커 지정 | [대조 보고서 §5 B068](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:1033) |
| [SFINCS/sfincs_boundaries_forcing.md:291](../../../models/SFINCS/source-analysis/sfincs_boundaries_forcing.md:291) (원래 291) | 보완 | Green-Ampt E 근거 중복 | 조건·반대 근거를 포함한 정본 링크 | sfincs_infiltration.f90:828–889 |
| [SFINCS/sfincs_boundaries_forcing.md:293](../../../models/SFINCS/source-analysis/sfincs_boundaries_forcing.md:293) (원래 293) | 보완 | Green-Ampt E 근거 중복 | 조건·반대 근거를 포함한 정본 링크 | sfincs_infiltration.f90:828–889 |
| [SFINCS/sfincs_boundaries_forcing.md:327](../../../models/SFINCS/source-analysis/sfincs_boundaries_forcing.md:327) (원래 327) | 보완 | 같은 릴리스 링크 오류 문단 중복 | 변경 이력 노트로 통합 | docs/developments.rst:283; external-results-sf.md B103 |
| [SFINCS/sfincs_flow_solver.md:92](../../../models/SFINCS/source-analysis/sfincs_flow_solver.md:92) (원래 92) | 보완 | 외부 판정 상세 문단 중복 | 정본으로 통합 | B067 정본 |
| [SFINCS/sfincs_flow_solver.md:93](../../../models/SFINCS/source-analysis/sfincs_flow_solver.md:93) (원래 93) | 보완 | 중복 근거가 여러 위치에 흩어짐 | 정본 앵커 지정 | [대조 보고서 §5 B103](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:1039) |
| [SFINCS/sfincs_flow_solver.md:119](../../../models/SFINCS/source-analysis/sfincs_flow_solver.md:119) (원래 119) | 보완 | 중복 근거가 여러 위치에 흩어짐 | 정본 앵커 지정 | [대조 보고서 §5 B024](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:1007) |
| [SFINCS/sfincs_flow_solver.md:165](../../../models/SFINCS/source-analysis/sfincs_flow_solver.md:165) (원래 165) | 정정 | 외부 판정 상세 문단 중복 및 잘못된 분류 | 정본으로 통합; 정정된 분류 반영 | B080 정본 |
| [SFINCS/sfincs_flow_solver.md:209](../../../models/SFINCS/source-analysis/sfincs_flow_solver.md:209) (원래 209) | 정정 | dtmin 식이 모든 좌표계에 적용되는 설명 | 투영좌표로 한정; 구면좌표 초기화 누락 E 추가 | sfincs_domain.f90:1403,1475,1539; sfincs_data.f90:56; sfincs_lib.f90:634; raw 전체 dtmin 검색 |
| [SFINCS/sfincs_flow_solver.md:226](../../../models/SFINCS/source-analysis/sfincs_flow_solver.md:226) (원래 224) | 보완 | 건조 면의 0/max(0,1) 후보 | 젖음 조건·집계·출력 경로의 반대 근거 추가 | sfincs_timestep_analysis.f90:17,19,43–55,123–124,178–188 |
| [SFINCS/sfincs_flow_solver.md:242](../../../models/SFINCS/source-analysis/sfincs_flow_solver.md:242) (원래 240) | 보완 | 같은 릴리스 링크 오류 문단 중복 | 변경 이력 노트로 통합 | docs/developments.rst:283; external-results-sf.md B103 |
| [SFINCS/sfincs_infiltration.md:51](../../../models/SFINCS/source-analysis/sfincs_infiltration.md:51) (원래 51) | 보완 | Green-Ampt np 인덱스 후보 | 활성 조건과 제한·변환의 반대 근거를 정본에 통합 | sfincs_infiltration.f90:399,423,483,492–494,838–889 |
| [SFINCS/sfincs_infiltration.md:65](../../../models/SFINCS/source-analysis/sfincs_infiltration.md:65) (원래 65) | 보완 | 누적 강수 E 중복 및 CN B 반대 근거 부족 | CN A 정본; :44,52–55 주석과 CN B 별도 상태 갱신 구분 | sfincs_infiltration.f90:41–55,689–715,756,765,770,777 |
| [SFINCS/sfincs_infiltration.md:70](../../../models/SFINCS/source-analysis/sfincs_infiltration.md:70) (원래 70) | 보완 | Green-Ampt E 근거 중복 | 조건·반대 근거를 포함한 정본 링크 | sfincs_infiltration.f90:828–889 |
| [SFINCS/sfincs_infiltration.md:71](../../../models/SFINCS/source-analysis/sfincs_infiltration.md:71) (원래 71) | 보완 | Green-Ampt E 근거 중복 | 조건·반대 근거를 포함한 정본 링크 | sfincs_infiltration.f90:828–889 |
| [SFINCS/sfincs_infiltration.md:92](../../../models/SFINCS/source-analysis/sfincs_infiltration.md:92) (원래 92) | 보완 | 같은 릴리스 링크 오류 문단 중복 | 변경 이력 노트로 통합 | docs/developments.rst:283; external-results-sf.md B103 |
| [SFINCS/sfincs_io_data.md:116](../../../models/SFINCS/source-analysis/sfincs_io_data.md:116) (원래 116) | 보완 | dtmapout을 항상 읽는 것처럼 설명 | dtout=0.0인 경우에만 읽는 우선순위 명시 | sfincs_input.f90:63,341–343 |
| [SFINCS/sfincs_io_data.md:209](../../../models/SFINCS/source-analysis/sfincs_io_data.md:209) (원래 209) | 보완 | 중복 근거가 여러 위치에 흩어짐 | 정본 앵커 지정 | [대조 보고서 §5 B042](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:1024) |
| [SFINCS/sfincs_io_data.md:231](../../../models/SFINCS/source-analysis/sfincs_io_data.md:231) (원래 231) | 보완 | type 2 읽기 후보와 쓰기 설명 중복 | 쓰기 1·4·5·6 및 외부 type 2 조건을 정본에 통합 | sfincs_initial_conditions.F90:196,227–233; sfincs_output.f90:704–738; docs/parameters.rst:555 |
| [SFINCS/sfincs_io_data.md:291](../../../models/SFINCS/source-analysis/sfincs_io_data.md:291) (원래 291) | 보완 | 같은 릴리스 링크 오류 문단 중복 | 변경 이력 노트로 통합 | docs/developments.rst:283; external-results-sf.md B103 |
| [SFINCS/sfincs_nonhydrostatic_wavemaker.md:140](../../../models/SFINCS/source-analysis/sfincs_nonhydrostatic_wavemaker.md:140) (원래 140) | 보완 | 중복 근거가 여러 위치에 흩어짐 | 정본 앵커 지정 | [대조 보고서 §5 B048](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:1026) |
| [SFINCS/sfincs_nonhydrostatic_wavemaker.md:218](../../../models/SFINCS/source-analysis/sfincs_nonhydrostatic_wavemaker.md:218) (원래 218) | 보완 | 같은 릴리스 링크 오류 문단 중복 | 변경 이력 노트로 통합 | docs/developments.rst:283; external-results-sf.md B103 |
| [SFINCS/sfincs_snapwave.md:50](../../../models/SFINCS/source-analysis/sfincs_snapwave.md:50) (원래 50) | 정정 | fwuv 가속도 설명; fwx·fwy 단위 모순 누락 | 전달 단위 정정; 출력 단위 속성 E 추가 | snapwave_solver.f90:1092; sfincs_snapwave.f90:427–472,502,508,563–564; sfincs_ncoutput.F90:600,608,1404,1411,2638,2651,3007–3008 |
| [SFINCS/sfincs_snapwave.md:134](../../../models/SFINCS/source-analysis/sfincs_snapwave.md:134) (원래 132) | 보완 | 중복 근거가 여러 위치에 흩어짐 | 정본 앵커 지정 | [대조 보고서 §5 B069](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:1034) |
| [SFINCS/sfincs_snapwave.md:135](../../../models/SFINCS/source-analysis/sfincs_snapwave.md:135) (원래 133) | 정정 | A·F 및 A·C·R 동일 | B·G; R 추가 항과 판 이력 한계 | preprint 식 (2.2),(2.6)–(2.7); snapwave_solver.f90:778–799,1192–1200 |
| [SFINCS/sfincs_snapwave.md:154](../../../models/SFINCS/source-analysis/sfincs_snapwave.md:154) (원래 152) | 보완 | 중복 근거가 여러 위치에 흩어짐 | 정본 앵커 지정 | [대조 보고서 §5 B051](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:1029) |
| [SFINCS/sfincs_snapwave.md:239](../../../models/SFINCS/source-analysis/sfincs_snapwave.md:239) (원래 237) | 보완 | 같은 릴리스 링크 오류 문단 중복 | 변경 이력 노트로 통합 | docs/developments.rst:283; external-results-sf.md B103 |
| [SFINCS/sfincs_structures_physics.md:74](../../../models/SFINCS/source-analysis/sfincs_structures_physics.md:74) (원래 74) | 보완 | 중복 근거가 여러 위치에 흩어짐 | 정본 앵커 지정 | [대조 보고서 §5 B110](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:1041) |
| [SFINCS/sfincs_structures_physics.md:195](../../../models/SFINCS/source-analysis/sfincs_structures_physics.md:195) (원래 195) | 보완 | type 2 E 설명 중복 | 쓰기 경로와 읽기 조건의 정본 링크 | sfincs_initial_conditions.F90:196,227–233; sfincs_output.f90:704–738 |
| [SFINCS/sfincs_structures_physics.md:250](../../../models/SFINCS/source-analysis/sfincs_structures_physics.md:250) (원래 250) | 보완 | 같은 릴리스 링크 오류 문단 중복 | 변경 이력 노트로 통합 | docs/developments.rst:283; external-results-sf.md B103 |
| [SFINCS/sfincs_subgrid_quadtree.md:115](../../../models/SFINCS/source-analysis/sfincs_subgrid_quadtree.md:115) (원래 115) | 보완 | 중복 근거가 여러 위치에 흩어짐 | 정본 앵커 지정 | [대조 보고서 §5 B049](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:1027) |
| [SFINCS/sfincs_subgrid_quadtree.md:147](../../../models/SFINCS/source-analysis/sfincs_subgrid_quadtree.md:147) (원래 147) | 정정 | 식 본체 일치, 부등호·0.999만 F | n과 g*n**2 보간의 비동치 확인; 차이 원인은 G | 논문 식 (19),(25); sfincs_subgrid.F90:323,329,347,445; momentum:364; continuity:549,553 |
| [SFINCS/sfincs_subgrid_quadtree.md:191](../../../models/SFINCS/source-analysis/sfincs_subgrid_quadtree.md:191) (원래 191) | 보완 | 중복 근거가 여러 위치에 흩어짐 | 정본 앵커 지정 | [대조 보고서 §5 B067](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:1032) |
| [SFINCS/sfincs_subgrid_quadtree.md:220](../../../models/SFINCS/source-analysis/sfincs_subgrid_quadtree.md:220) (원래 220) | 보완 | 같은 릴리스 링크 오류 문단 중복 | 변경 이력 노트로 통합 | docs/developments.rst:283; external-results-sf.md B103 |
| [XBeach/xbeach-coupled-physics-contracts.md:112](../../../models/XBeach/source-analysis/xbeach-coupled-physics-contracts.md:112) (원래 112) | 보완 | 식생 E의 긴 설명 중복 | 식생 노트를 정본으로 지정 | vegetation.F90:502–564; flow_timestep.F90:567,603; 보고서 308·524 |
| [XBeach/xbeach-coupled-physics-contracts.md:113](../../../models/XBeach/source-analysis/xbeach-coupled-physics-contracts.md:113) (원래 113) | 보완 | 식생 E의 긴 설명 중복 | 식생 노트를 정본으로 지정; 단위 후보 연결 | vegetation.F90:502–564; flow_timestep.F90:567,603; 보고서 308·524 |
| [XBeach/xbeach_vegetation.md:70](../../../models/XBeach/source-analysis/xbeach_vegetation.md:70) (원래 70) | 보완 | 중복 근거가 여러 위치에 흩어짐 | 정본 앵커 지정 | [대조 보고서 §5, 308행](../../../_staging/recovery/compare/XBeach-manual-vs-code.md#5-차이-결론) |
| [XBeach/xbeach_vegetation.md:73](../../../models/XBeach/source-analysis/xbeach_vegetation.md:73) (원래 73) | 보완 | canopy 재사용 후보만 기재 | 정본 앵커; 합산 힘의 단위 불일치 E 추가 | vegetation.F90:441,515–564; variables.def:82,121,274–280; params.def:103,502; flow_timestep.F90:567,603 |

## 분류 변경 행

분류 변경은 SFINCS의 기존 원행 ID 54개이다. XBeach 기존 원행의 분류 변경은 없다.

| 보고서 행 ID | 이전 → 새 | 근거 |
|---|---|---|
| SFINCS P001·P002·P003·P004·P005·P006·P007·P008·P009·P010·P011·P012 | D → H | `docs/input.rst:13`의 외부 HydroMT-SFINCS API 명시. 아래 raw 전체 검색. |
| SFINCS P013·P014·P015·P016·P017·P018·P019·P020·P021·P022 | D → H | `docs/input.rst:13`의 외부 HydroMT-SFINCS API 명시. 아래 raw 전체 검색. |
| SFINCS P023·P024·P025·P026·P027·P028·P029·P030·P031 | D → H | `docs/input.rst:13`의 외부 HydroMT-SFINCS API 명시. 아래 raw 전체 검색. |
| SFINCS P032·P033·P034 | D → H | `docs/input.rst:13`의 외부 HydroMT-SFINCS API 명시. 아래 raw 전체 검색. |
| SFINCS P035·P036 | D → H | `docs/input.rst:13`의 외부 HydroMT-SFINCS API 명시. 아래 raw 전체 검색. |
| SFINCS P037 | D → H | `docs/input.rst:13`의 외부 HydroMT-SFINCS API 명시. 아래 raw 전체 검색. |
| SFINCS P038·P039·P040·P041 | D → H | `docs/input.rst:13`의 외부 HydroMT-SFINCS API 명시. 아래 raw 전체 검색. |
| SFINCS P042·P043·P044·P045·P046·P047·P048·P049 | D → H | `docs/input.rst:13`의 외부 HydroMT-SFINCS API 명시. 아래 raw 전체 검색. |
| SFINCS P050·P051·P052 | D → H | `docs/input.rst:13`의 외부 HydroMT-SFINCS API 명시. 아래 raw 전체 검색. |
| SFINCS B070 | A·F → B·G | 계수 B는 문서 내부 모순이다. 0.25·0.28의 차이 원인은 미확인이다. R에는 IG 전이·바람 항이 추가된다. [정본](../../../models/SFINCS/source-analysis/sfincs_snapwave.md#cv-s-b070). |
| SFINCS B080 | 일치/F → G | n 보간과 g*n**2 보간은 일반적으로 동치가 아니다. 2.1.1 논문과 2.4.0 코드 사이의 변경 의도는 미확인이다. [정본](../../../models/SFINCS/source-analysis/sfincs_subgrid_quadtree.md#cv-s-b080). |

SFINCS 기존 360개 원행의 재집계: A 18, B 47, C 207, D 11, E 8, F 2, G 1, H 66, X 0. B070은 첫 분류 B에 한 번 집계했다.
XBeach 기존 9개 판정행의 재집계: B 5, C 2, E 2. 총괄행 1068도 기존 기준대로 한 번 센다.

## E 후보와 반대 근거

| 후보 | 확인한 반대 근거·보정 경로 | 결론 |
|---|---|---|
| SFINCS A100·C014 | `sfincs_output.f90:704–738`은 1·4·5·6만 쓴다. type 2는 생성하지 않는다. 리더의 `:227–233`은 type 2에도 uvmean 읽기를 수행한다. | E 유지. 평균 유량이 없는 외부 type 2 파일 조건이다. 자체 쓰기→읽기의 재현 오류로 확대하지 않았다. |
| SFINCS B047·C021 | `sfincs_infiltration.f90:44,52–55`의 주석을 추가했다. `:139–143`의 초기화는 후속 누적을 보정하지 않는다. CN B는 `:756,765,770,777`에서 별도 상태를 갱신한다. | E 유지. 강수 활성·CN A·storecumprcp=0 조건이다. Sonnet 11 반영. |
| SFINCS B123·C026 | `sfincs_infiltration.f90:492–494`의 단위 변환과 `:857`의 강수량 제한을 확인했다. 상태 갱신은 nm, 문제 식의 두 배열은 np이다. | E 유지. 마지막 셀 값과 현재 셀 값이 같거나 제한에 걸리면 출력 차이가 가려질 수 있다. |
| SFINCS B125·C028 | `sfincs_timestep_analysis.f90:43–55`의 누적은 젖은 면만 수행한다. `:123–124`의 집계는 젖은 횟수를 검사하지 않는다. `:178–188`의 출력 제한은 0을 -1로 바꾸지 않는다. | E 유지. 유효하지만 한 번도 젖지 않은 면 조건이다. |
| XBeach 308 | `flow_timestep.F90:807–808,931,934`의 보간·속력과 `vegetation.F90:871,877`의 porous 경로를 대조했다. 표준 경로의 u점 속력 사용은 그대로 남는다. 보고서 §5.2의 양의 항력 반례를 재검산했다. | E 유지. 2차원 내부점에서 축을 교환하면 항력이 달라지는 후보이다. |
| XBeach 524 | `vegetation.F90:452–453`은 호출 시작에 0으로 만든다. 따라서 이전 시간 단계 누적 가설은 기각한다. 층 루프의 파봉 위 분기에는 재초기화가 없다. | E 유지. 같은 호출의 앞선 층에서 얻은 0이 아닌 값 재사용에 한정한다. |
| 새 SFINCS CV-S-SF-01 | fwx·fwy 계산·전달·NetCDF 쓰기를 추적했다. rhow 나눗셈은 운동량용 fwuv에만 적용된다. 길이 단위로 바꾸는 출력 변환은 없다. | E 추가. 계산 단위 N/m²와 NetCDF units=m의 모순. [정본](../../../models/SFINCS/source-analysis/sfincs_snapwave.md#cv-s-sf-01). |
| 새 SFINCS CV-S-SF-02 | raw 전체 dtmin 검색을 확인했다. 투영좌표 ELSE의 대입 외에는 읽기·선언·주석·출력만 있다. 구면좌표도 중단 검사에 dtmin을 사용한다. | E 추가. 구면좌표에서 사용 전 대입을 찾지 못했다. 실제 저장소 값과 영향은 미확인. [정본](../../../models/SFINCS/source-analysis/sfincs_flow_solver.md#cv-s-sf-02). |
| 새 XBeach CV-S-XB-01 | raw 전체 FvgCan·FvgCau·FvgCav 검색은 vegetation.F90만 찾았다. ucan은 속도이다. canopy 항은 높이/hh를 쓰지만 함께 더하는 평균류 항은 높이를 쓴다. 합산 전 수심 곱셈은 없다. | E 추가. 표준 경로의 vegcanflo==1, 잠긴 층과 0이 아닌 ucan 조건. [정본](../../../models/XBeach/source-analysis/xbeach_vegetation.md#cv-s-xb-01). |

기각한 의심: SFINCS 경계의 t·tspinup 비교는 시간 원점 결함으로 분류하지 않았다. `sfincs_input.f90:365–369`가 기간을 tref 기준 종료 시각으로 변환한다. `sfincs_boundaries.f90:853`도 t0를 뺀다.
기각한 의심: NetCDF spiderweb pressure의 `sfincs_ncinput.F90:1044` 읽기와 `:1046` 대입 사이에는 `:1045`의 reshape가 있다. 바람 배열을 잘못 재사용한다는 해석은 성립하지 않는다.

<a id="d-search"></a>
## D 판정의 raw 전체 재검색

원래 D였던 노트의 추가 줄 17곳을 모두 포함했다. 묶인 원행은 63개이다.
검색 명령은 `rg -n -i -uuu -e <패턴> models/SFINCS/raw`이다. 숨김·무시 파일과 보조 프로그램·유틸리티를 제외하지 않았다. 파일 확장자 필터도 쓰지 않았다.
각 패턴은 단어 경계를 사용했다. SFINCS 주 입력과 독립 SnapWave 입력을 구분했다. 동명 변수의 일치는 Python API의 구현 증거로 사용하지 않았다.
Python 파일 확인 결과는 `docs/conf.py`와 `source/third_party_open/netcdf/netcdf-fortran-4.6.1/fortran/expand-interfaces.py`이다. `def (create|create_from_region|create_constant|create_cn|create_cn_with_recovery|create_uniform)` 정의는 raw 전체에서 찾지 못했다.
XBeach 대상 추가 줄에는 D 판정이 없다.

| 원래 보고서 행 ID | 원래 노트 줄 | 핵심 검색어 | 결과와 판정 |
|---|---|---|---|
| A040 | SFINCS/sfincs-parameters-io-reference.md:121,419 | `dtmin` | 문서·선언·내부 계산·중단 검사·NetCDF 속성만 일치했다. 입력 리더는 없다. D 유지. 내부 계산의 구면좌표 누락은 별도 E 후보이다. 일치 파일 5개, 일치 줄 10개. |
| E023·E024·E025 | SFINCS/sfincs-parameters-io-reference.md:421–423 | `bwvfile`·`bhsfile`·`btpfile` | bwvfile은 문서와 독립 경계 루틴 주석에 일치했다. bhsfile·btpfile은 독립 snapwave.inp 리더 :56–57에도 있다. SFINCS 주 입력의 D만 유지한다. 일치 파일 3개, 일치 줄 7개. |
| H001·H002·H003·H004·H005·H006 | SFINCS/sfincs-parameters-io-reference.md:424 | `FileVersion`·`filetype`·`grid_unit`·`quantity1`·`unit1`·`NODATA_value` | docs/input_forcing.rst에만 일치했다. read_amuv_file은 TIME 앞 헤더를 건너뛴다. D 유지. 일치 파일 1개, 일치 줄 14개. |
| P001·P002·P003·P004·P005·P006·P007·P008·P009·P010·P011·P012 | SFINCS/sfincs-model-building-running.md:64 | `x0`·`y0`·`dx`·`dy`·`nmax`·`mmax`·`rotation`·`epsg`·`region`·`res`·`rotated`·`crs` | 문서 예제와 동명 Fortran 변수·일반 용어가 일치했다. 외부 HydroMT API 구현은 찾지 못했다. 외부 API 동작이므로 D→H. 일치 파일 35개, 일치 줄 437개. |
| P013·P014·P015·P016·P017·P018·P019·P020·P021·P022 | SFINCS/sfincs-model-building-running.md:65 | `elevation_list`·`roughness_list`·`river_list`·`nlevels`·`nr_subgrid_pixels`·`write_dep_tif`·`write_man_tif`·`manning_land`·`manning_sea`·`rgh_lev_land` | 문서 예제와 동명 Fortran 변수·일반 용어가 일치했다. 외부 HydroMT API 구현은 찾지 못했다. 외부 API 동작이므로 D→H. 일치 파일 7개, 일치 줄 33개. |
| P023·P024·P025·P026·P027·P028·P029·P030·P031 | SFINCS/sfincs-model-building-running.md:66 | `qinf`·`lulc`·`reclass_table`·`reproj_method`·`antecedent_moisture`·`hsg`·`ksat`·`effective`·`block_size` | 문서 예제와 동명 Fortran 변수·일반 용어가 일치했다. 외부 HydroMT API 구현은 찾지 못했다. 외부 API 동작이므로 D→H. 일치 파일 16개, 일치 줄 46개. |
| P032·P033·P034 | SFINCS/sfincs-model-building-running.md:67 | `storage_locs`·`volume`·`height` | 문서 예제와 동명 Fortran 변수·일반 용어가 일치했다. 외부 HydroMT API 구현은 찾지 못했다. 외부 API 동작이므로 D→H. 일치 파일 29개, 일치 줄 465개. |
| P035·P036 | SFINCS/sfincs-model-building-running.md:68 | `merge`·`locations` | 문서 예제와 동명 Fortran 변수·일반 용어가 일치했다. 외부 HydroMT API 구현은 찾지 못했다. 외부 API 동작이므로 D→H. 일치 파일 28개, 일치 줄 104개. |
| P037 | SFINCS/sfincs-model-building-running.md:69 | `ini` | 문서 예제와 동명 Fortran 변수·일반 용어가 일치했다. 외부 HydroMT API 구현은 찾지 못했다. 외부 API 동작이므로 D→H. 일치 파일 3개, 일치 줄 6개. |
| P038·P039·P040·P041 | SFINCS/sfincs-model-building-running.md:70 | `geodataset`·`timeseries`·`offset`·`buffer` | 문서 예제와 동명 Fortran 변수·일반 용어가 일치했다. 외부 HydroMT API 구현은 찾지 못했다. 외부 API 동작이므로 D→H. 일치 파일 36개, 일치 줄 344개. |
| P042·P043·P044·P045·P046·P047·P048·P049 | SFINCS/sfincs-model-building-running.md:71 | `wind`·`dst_res`·`precip`·`aggregate`·`press`·`fill_value`·`magnitude`·`direction` | 문서 예제와 동명 Fortran 변수·일반 용어가 일치했다. 외부 HydroMT API 구현은 찾지 못했다. 외부 API 동작이므로 D→H. 일치 파일 58개, 일치 줄 593개. |
| P050·P051·P052 | SFINCS/sfincs-model-building-running.md:72 | `dz`·`stype`·`discharge` | 문서 예제와 동명 Fortran 변수·일반 용어가 일치했다. 외부 HydroMT API 구현은 찾지 못했다. 외부 API 동작이므로 D→H. 일치 파일 14개, 일치 줄 70개. |
| B135 | SFINCS/sfincs-parameters-io-reference.md:318; sfincs_boundaries_forcing.md:160 | `Darcy`·`Weisbach` | docs/input_structures.rst:222의 미래 계획만 일치했다. 현재 암거는 par1과 sqrt(수두차)를 쓴다. D 유지. 일치 파일 1개, 일치 줄 1개. |

다음은 각 검색의 일치 파일과 줄 번호 전체이다. 경로 기준은 `models/SFINCS/raw/`이다. 한 줄에 같은 검색어가 여러 번 나와도 한 줄로 센다. 검색 그룹 간 중복은 제거하지 않았다.

<details>
<summary>A040 검색 결과</summary>

패턴: `\b(?:dtmin)\b`

- `source_code/sfincs/docs/parameters.rst:245`
- `source_code/sfincs/source/src/sfincs_ncoutput.F90:4117`
- `source_code/sfincs/source/src/sfincs_data.f90:56`
- `source_code/sfincs/source/src/sfincs_lib.f90:632, 634, 638`
- `source_code/sfincs/source/src/sfincs_domain.f90:1526, 1530, 1534, 1539`

</details>

<details>
<summary>E023·E024·E025 검색 결과</summary>

패턴: `\b(?:bwvfile|bhsfile|btpfile)\b`

- `source_code/sfincs/docs/waves.rst:9, 11, 13`
- `source_code/sfincs/source/src/snapwave/snapwave_boundaries.f90:123, 213`
- `source_code/sfincs/source/src/snapwave/snapwave_input.f90:56–57`

</details>

<details>
<summary>H001·H002·H003·H004·H005·H006 검색 결과</summary>

패턴: `\b(?:FileVersion|filetype|grid_unit|quantity1|unit1|NODATA_value)\b`

- `source_code/sfincs/docs/input_forcing.rst:273–274, 280–281, 291–292, 302–303, 312–313, 316, 322–324`

</details>

<details>
<summary>P001·P002·P003·P004·P005·P006·P007·P008·P009·P010·P011·P012 검색 결과</summary>

패턴: `\b(?:x0|y0|dx|dy|nmax|mmax|rotation|epsg|region|res|rotated|crs)\b`

- `source_code/sfincs/docs/parameters.rst:9, 15, 21, 27, 33, 39, 45–46, 539`
- `source_code/sfincs/docs/input_forcing.rst:262, 319–320`
- `source_code/sfincs/docs/input_structures.rst:45, 50, 97, 102`
- `source_code/sfincs/docs/input.rst:26–32, 74–80, 111–112, 122–129, 136–143, 149–152, 175, 177, 222, 224, 328, 330, 392, 394, 434, 436, 548, 550, 614, 620, 625, 674, 676`
- `source_code/sfincs/source/src/sfincs_ncoutput.F90:97–101, 134, 148, 162, 176, 179–181, 261, 265, 311, 319, 703–706, 708–711, 715–718, 731, 733, 735, 915–916, 921–922, 927–928, 933–934, 943, 998, 1007, 1018, 1027, 1051, 1060, 1071, 1080, 1084–1086, 1107, 1111, 1193, 1200, 1338, 1345, 1582, 1584, 1586, 1588, 1864, 1871, 1877, 1884, 1887–1889, 1904, 1910, 1926, 1932, 1967, 1974, 2242, 2339, 2398–2399, 3506, 3969–3970, 4029, 4088–4094, 4136`
- `source_code/sfincs/source/src/sfincs_structures.f90:206–207, 209–210, 216–217, 219–220, 229–232, 238–241, 516–517, 519–522, 564–565, 567–570`
- `source_code/sfincs/docs/figures/.$Overview_status_SFINCS.drawio.bkp:3, 209, 442, 630`
- `source_code/sfincs/source/src/sfincs_ncinput.F90:680, 794, 912`
- `source_code/sfincs/source/src/sfincs_boundaries.f90:797–798`
- `source_code/sfincs/source/src/sfincs_input.f90:50–56, 96–97, 347–349, 378–380, 382, 384–386, 395`
- `source_code/sfincs/source/src/sfincs_data.f90:39–40, 58–60, 111–112, 183`
- `source_code/sfincs/source/src/sfincs_output.f90:400, 408–409, 420–421, 430–431, 438–439, 446–447, 452–453`
- `source_code/sfincs/source/src/sfincs_lib.f90:321, 704`
- `source_code/sfincs/source/src/sfincs_crosssections.f90:10, 44`
- `source_code/sfincs/source/src/sfincs_spiderweb.f90:320, 337–338, 349–350`
- `source_code/sfincs/source/src/snapwave/snapwave_infragravity.f90:439`
- `source_code/sfincs/source/src/snapwave/snapwave_data.f90:145–151`
- `source_code/sfincs/source/src/snapwave/snapwave_input.f90:23–29, 78–79`
- `source_code/sfincs/source/src/snapwave/snapwave_ncoutput.F90:102–103`
- `source_code/sfincs/docs/figures/Overview_status_SFINCS.drawio:3, 209, 442, 630`
- `source_code/sfincs/source/src/snapwave/snapwave_solver.f90:1370, 1378, 1389`
- `source_code/sfincs/source/src/snapwave/snapwave_domain.f90:37–38, 418, 420, 432, 436, 443–444, 888, 922–923, 933–934`
- `source_code/sfincs/source/src/snapwave/interp.F90:1250–1251, 1262–1265, 1706, 1720–1721, 1770–1771, 1875, 1883–1885, 1889, 1897, 1899, 1915, 1918–1919, 1924, 1954, 1957, 1959–1960, 1962, 1977, 1979–1980, 1994, 2001, 2004, 2011, 2035`
- `source_code/sfincs/source/src/sfincs_quadtree.F90:192, 194, 196, 198, 200, 202, 204, 429, 431–437, 445, 450–456, 504, 517–518, 538, 556, 571, 579, 593–599, 609–610, 630–631, 893–896`
- `source_code/sfincs/source/src/sfincs_domain.f90:207, 216–217, 224–225, 235–236, 239, 263, 267–275, 291–292, 1377–1378, 1394–1395, 1553, 1556–1557, 1565, 1568–1570, 1648, 1653–1654, 1659–1660, 1784, 2149, 2156`
- `source_code/sfincs/source/src/sfincs_momentum.f90:452–453, 455, 470, 485`
- `source_code/sfincs/source/src/sfincs_wavemaker.f90:109, 1623`
- `source_code/sfincs/source/src/sfincs_meteo.f90:262`
- `source_code/sfincs/source/src/sfincs_continuity.f90:147, 363, 367, 380, 448`
- `source_code/sfincs/source/autogen.sh:349, 354`
- `source_code/sfincs/source/third_party_open/utils/toml-f/src/tomlf/de/lexer.f90:1106, 1110–1111, 1123`
- `source_code/sfincs/source/third_party_open/utils/geometry.f90:199, 204–206, 208, 348, 366–368`
- `source_code/sfincs/source/third_party_open/netcdf/netcdf-fortran-4.6.1/docs/netcdf.m4:417–418`
- `source_code/sfincs/source/third_party_open/netcdf/netcdf-fortran-4.6.1/docs/netcdf_fortran.3:3–4`
- `source_code/sfincs/source/third_party_open/netcdf/netcdf-fortran-4.6.1/docs/texinfo.tex:7291`

</details>

<details>
<summary>P013·P014·P015·P016·P017·P018·P019·P020·P021·P022 검색 결과</summary>

패턴: `\b(?:elevation_list|roughness_list|river_list|nlevels|nr_subgrid_pixels|write_dep_tif|write_man_tif|manning_land|manning_sea|rgh_lev_land)\b`

- `source_code/sfincs/docs/input.rst:192, 274–280, 309, 313, 315, 317, 341–344`
- `source_code/sfincs/docs/parameters.rst:156–157, 162, 168`
- `source_code/sfincs/source/src/sfincs_ncoutput.F90:4111–4113`
- `source_code/sfincs/source/src/sfincs_input.f90:74–76`
- `source_code/sfincs/source/src/sfincs_data.f90:29–30`
- `source_code/sfincs/source/src/sfincs_domain.f90:2026, 2029, 2032, 2035`
- `source_code/sfincs/source/src/sfincs_snapwave.f90:630`

</details>

<details>
<summary>P023·P024·P025·P026·P027·P028·P029·P030·P031 검색 결과</summary>

패턴: `\b(?:qinf|lulc|reclass_table|reproj_method|antecedent_moisture|hsg|ksat|effective|block_size)\b`

- `source_code/sfincs/docs/parameters.rst:132, 139, 478`
- `source_code/sfincs/docs/tables/input_parameters.tab:32`
- `source_code/sfincs/docs/input.rst:53, 377, 388, 405–408, 448, 478–483`
- `source_code/sfincs/LICENSE:181`
- `source_code/sfincs/source/src/sfincs_ncoutput.F90:204, 225, 1485, 1505, 3360, 4115`
- `source_code/sfincs/source/src/sfincs_meteo.f90:1301, 1305, 1361, 1365`
- `source_code/sfincs/source/COPYING:181`
- `source_code/sfincs/source/src/sfincs_input.f90:78, 376`
- `source_code/sfincs/source/src/sfincs_data.f90:63, 390`
- `source_code/sfincs/source/src/sfincs_infiltration.f90:92, 204, 209, 215, 238, 246`
- `source_code/sfincs/source/src/snapwave/snapwave_solver.f90:1860`
- `source_code/sfincs/source/sfincs/x64/Release/LICENSING CONDITIONS DELTARES SFINCS SOURCE CODE.txt:181`
- `source_code/sfincs/source/third_party_open/netcdf/netcdf-fortran-4.6.1/docs/old/netcdf-f90.texi:3862`
- `source_code/sfincs/source/third_party_open/netcdf/netcdf-fortran-4.6.1/docs/old/netcdf-f77.texi:4233`
- `source_code/sfincs/source/third_party_open/netcdf/netcdf-fortran-4.6.1/docs/netcdf-f77.md:3795`
- `source_code/sfincs/source/third_party_open/netcdf/netcdf-fortran-4.6.1/docs/netcdf-f90-sec5-user_defined_types.md:1099`

</details>

<details>
<summary>P032·P033·P034 검색 결과</summary>

패턴: `\b(?:storage_locs|volume|height)\b`

- `source_code/sfincs/docs/parameters.rst:545, 671`
- `source_code/sfincs/LICENSE:238`
- `source_code/sfincs/docs/figures/Overview_status_SFINCS.drawio:8, 11, 14, 17, 20, 23, 26, 29, 32, 43, 46, 49, 52, 55, 58, 109, 112, 115, 118, 121, 124, 146, 149, 152, 155, 158, 161, 164, 167, 170, 173, 176, 179, 182, 185, 188, 191, 194, 197, 200, 203, 214, 217, 220, 223, 226, 229, 231–232, 235, 238, 241, 244, 255, 258, 261, 264, 267, 270, 321, 324, 327, 330, 333, 336, 358, 361, 364, 367, 370, 373, 376, 379, 382, 384–385, 388, 391, 394, 397, 400, 403, 406, 409, 412, 415, 418, 424, 427, 430, 436, 447, 450, 453, 456, 459, 462, 464–465, 468, 471, 474, 477, 488, 491, 494, 497, 500, 503, 554, 557, 560, 563, 566, 569, 591, 594, 597, 600, 603, 606, 609, 612, 615, 617–618, 621, 624, 635, 638, 641, 644, 647, 650, 652–653, 656, 659, 662, 665, 676, 679, 682, 685, 688, 691, 742, 745, 748, 751, 754, 757, 779, 782, 785, 788, 791, 794, 797, 800, 803, 806, 809, 812`
- `source_code/sfincs/source/build_scripts/Dockerfile:22`
- `source_code/sfincs/source/build_scripts/Dockerfile_cpu_local:29`
- `source_code/sfincs/source/src/sfincs_ncoutput.F90:324, 335, 347, 584, 592, 1205, 1216, 1228, 1390, 1397, 1912, 2032, 2039, 4324, 4338, 4340, 4357, 4365, 4369`
- `source_code/sfincs/source/src/sfincs_structures.f90:65, 114, 255, 257, 283, 286, 290, 526, 539`
- `source_code/sfincs/source/src/sfincs_input.f90:127, 664`
- `source_code/sfincs/source/src/sfincs_data.f90:403, 405`
- `source_code/sfincs/source/src/sfincs_discharges.f90:627`
- `source_code/sfincs/source/src/snapwave/snapwave_boundaries.f90:67, 248, 584, 587, 680`
- `source_code/sfincs/source/src/snapwave/snapwave_infragravity.f90:360, 374`
- `source_code/sfincs/source/src/snapwave/snapwave_data.f90:19, 113, 121, 129, 131, 175, 253, 264`
- `source_code/sfincs/source/src/snapwave/snapwave_solver.f90:241–242, 278, 340, 1039, 1189, 1231, 1238, 1255, 1640, 1647, 1697, 1704, 1727, 1731, 1760, 1765, 1773, 1860`
- `source_code/sfincs/source/src/sfincs_domain.f90:2077, 2091`
- `source_code/sfincs/source/src/sfincs_wavemaker.f90:1234, 1646, 1650, 1660, 1675, 1680`
- `source_code/sfincs/source/src/sfincs_snapwave.f90:647`
- `source_code/sfincs/source/COPYING:238`
- `source_code/sfincs/docs/figures/.$Overview_status_SFINCS.drawio.bkp:8, 11, 14, 17, 20, 23, 26, 29, 32, 43, 46, 49, 52, 55, 58, 109, 112, 115, 118, 121, 124, 146, 149, 152, 155, 158, 161, 164, 167, 170, 173, 176, 179, 182, 185, 188, 191, 194, 197, 200, 203, 214, 217, 220, 223, 226, 229, 231–232, 235, 238, 241, 244, 255, 258, 261, 264, 267, 270, 321, 324, 327, 330, 333, 336, 358, 361, 364, 367, 370, 373, 376, 379, 382, 384–385, 388, 391, 394, 397, 400, 403, 406, 409, 412, 415, 418, 424, 427, 430, 436, 447, 450, 453, 456, 459, 462, 464–465, 468, 471, 474, 477, 488, 491, 494, 497, 500, 503, 554, 557, 560, 563, 566, 569, 591, 594, 597, 600, 603, 606, 609, 612, 615, 617–618, 621, 624, 635, 638, 641, 644, 647, 650, 652–653, 656, 659, 662, 665, 676, 679, 682, 685, 688, 691, 742, 745, 748, 751, 754, 757, 779, 782, 785, 788, 791, 794, 797, 800, 803, 806, 809, 812`
- `source_code/sfincs/docs/input_structures.rst:80`
- `source_code/sfincs/docs/output.rst:198, 202, 271`
- `source_code/sfincs/docs/input.rst:264, 379, 417, 536, 539–540, 561–563`
- `source_code/sfincs/docs/developments.rst:108, 110–111, 180, 334`
- `source_code/sfincs/docs/figures/Deltares_logo_D-blauw_RGB.svg:1`
- `source_code/sfincs/source/sfincs/x64/Release/LICENSING CONDITIONS DELTARES SFINCS SOURCE CODE.txt:238`
- `source_code/sfincs/source/src/sfincs_continuity.f90:454, 456–457, 501, 507, 511, 517, 533`
- `source_code/sfincs/source/third_party_open/netcdf/netcdf-fortran-4.6.1/docs/texinfo.tex:415, 417, 420, 634, 636, 667, 716, 828, 837, 1185, 1227, 1496, 3035, 3039, 3056, 3268, 3297, 5140, 5224, 6054, 6344, 6347, 8445, 9697, 9933`
- `source_code/sfincs/source/third_party_open/netcdf/netcdf-fortran-4.6.1/docs/Doxyfile.developer:51`
- `source_code/sfincs/source/third_party_open/netcdf/netcdf-fortran-4.6.1/docs/Doxyfile.in:50`

</details>

<details>
<summary>P035·P036 검색 결과</summary>

패턴: `\b(?:merge|locations)\b`

- `source_code/sfincs/docs/input_forcing.rst:24, 34–35, 41, 88, 91, 135, 188–189`
- `source_code/sfincs/source/src/sfincs_boundaries.f90:60`
- `source_code/sfincs/source/src/sfincs_discharges.f90:43`
- `source_code/sfincs/source/src/snapwave/snapwave_boundaries.f90:208`
- `source_code/sfincs/source/src/snapwave/snapwave_data.f90:121–125, 131–132`
- `source_code/sfincs/source/src/snapwave/interp.F90:466, 727, 1226`
- `source_code/sfincs/docs/developments.rst:112`
- `source_code/sfincs/docs/input_structures.rst:70–71, 83, 122, 124, 153, 163, 185, 188, 194, 197`
- `source_code/sfincs/docs/output.rst:134`
- `source_code/sfincs/docs/input.rst:564, 596–597, 645–646`
- `source_code/sfincs/source/sfincs_lib/sfincs_lib.vfproj:84`
- `source_code/sfincs/source/third_party_open/utils/toml-f/src/tomlf/terminal.f90:267–269`
- `source_code/sfincs/source/third_party_open/utils/toml-f/src/tomlf/type/table.f90:195, 200, 206`
- `source_code/sfincs/source/third_party_open/utils/toml-f/src/tomlf/de/parser.f90:856`
- `source_code/sfincs/source/third_party_open/utils/toml-f/src/tomlf/de/lexer.f90:407, 426, 531, 580, 627, 758, 858, 928, 973, 1215, 1247–1248, 1301`
- `source_code/sfincs/source/third_party_open/utils/toml-f/src/tomlf/diagnostic.f90:365`
- `source_code/sfincs/source/third_party_open/utils/toml-f/src/tomlf/build/build_table.f90:827, 870, 913, 956, 999, 1042, 1085, 1128, 1171`
- `source_code/sfincs/source/third_party_open/utils/toml-f/src/tomlf/build/merge.f90:14, 27, 57, 66, 78, 104, 107, 113, 192`
- `source_code/sfincs/source/third_party_open/utils/toml-f/LICENSE-MIT:3`
- `source_code/sfincs/source/src/Makefile.am:45`
- `source_code/sfincs/source/src/sfincs_wavemaker.f90:1200`
- `source_code/sfincs/source/src/sfincs_meteo.f90:699`
- `source_code/sfincs/docs/parameters.rst:535, 564, 588`
- `source_code/sfincs/source/third_party_open/netcdf/netcdf-fortran-4.6.1/RELEASE_NOTES.md:23, 45, 56, 139, 143, 161, 167`
- `source_code/sfincs/source/third_party_open/netcdf/netcdf-fortran-4.6.1/docs/old/netcdf-f77.texi:7246, 7493, 7600, 7962`
- `source_code/sfincs/source/third_party_open/netcdf/netcdf-fortran-4.6.1/docs/netcdf.m4:1331`
- `source_code/sfincs/source/third_party_open/netcdf/netcdf-fortran-4.6.1/docs/netcdf_fortran.3:1205`
- `source_code/sfincs/source/third_party_open/netcdf/netcdf-fortran-4.6.1/docs/netcdf-f77.md:6789, 7029, 7135, 7497`

</details>

<details>
<summary>P037 검색 결과</summary>

패턴: `\b(?:ini)\b`

- `source_code/sfincs/docs/input.rst:670, 687`
- `source_code/sfincs/docs/parameters.rst:549`
- `source_code/sfincs/source/src/sfincs_initial_conditions.F90:61, 272, 279`

</details>

<details>
<summary>P038·P039·P040·P041 검색 결과</summary>

패턴: `\b(?:geodataset|timeseries|offset|buffer)\b`

- `source_code/sfincs/docs/input_forcing.rst:86–87, 89–90, 186–187, 190, 407, 437`
- `source_code/sfincs/source/autogen.sh:1574`
- `source_code/sfincs/source/third_party_open/utils/toml-f/src/tomlf/datetime.f90:19`
- `source_code/sfincs/source/third_party_open/utils/toml-f/src/tomlf/utils/io.f90:64, 83, 85`
- `source_code/sfincs/source/third_party_open/utils/toml-f/src/tomlf/de/lexer.f90:102, 124–125, 220, 234, 238–239, 242, 245–246, 254, 638, 647, 654, 771, 784, 790, 870, 877, 887, 909, 1318, 1329–1330, 1336–1337, 1388, 1391`
- `source_code/sfincs/source/third_party_open/utils/toml-f/src/tomlf/diagnostic.f90:200, 202, 207, 216, 221, 224–225, 228, 233, 236, 247, 256, 259, 267, 272, 275, 280, 291, 302, 313, 321, 333, 340, 345, 351, 428, 440, 445, 450, 454, 456`
- `source_code/sfincs/source/third_party_open/utils/toml-f/src/tomlf/utils.f90:89, 101, 105, 111, 114, 127, 139, 143, 149, 152, 165, 177, 181, 187, 190, 203, 215, 219, 225, 228, 239, 249, 251, 253, 255, 257`
- `source_code/sfincs/source/src/sfincs_discharges.f90:110`
- `source_code/sfincs/source/src/snapwave/snapwave_boundaries.f90:31, 33, 211, 236, 260, 271, 282, 543, 759`
- `source_code/sfincs/source/src/snapwave/snapwave_data.f90:30`
- `source_code/sfincs/source/third_party_open/netcdf/netcdf-fortran-4.6.1/docs/old/netcdf-f90.texi:871, 885, 887–888, 1049, 1229, 3321, 3333–3334, 3451, 3455, 3469–3470, 3528, 3533, 3552–3553, 3726, 3732, 3752, 3756, 3798, 3837, 3845, 4059, 4200, 4880, 4974, 5008, 6122, 6125`
- `source_code/sfincs/source/third_party_open/netcdf/netcdf-fortran-4.6.1/docs/netcdf-f77.md:543, 557, 559, 561, 651, 653, 660, 670, 1194, 1732, 1737, 1743, 3268, 3279–3280, 3388, 3399–3400, 3472, 3487–3488, 3706, 3764, 3772, 4093, 4224, 4859, 5154, 5185, 5321, 5554, 5725, 5898, 8636`
- `source_code/sfincs/source/third_party_open/netcdf/netcdf-fortran-4.6.1/docs/netcdf-f90-sec5-user_defined_types.md:492, 503–504, 634, 638, 655, 657, 732, 737, 761, 763, 956, 962, 982, 986, 1034, 1074, 1082, 1318, 1471`
- `source_code/sfincs/source/third_party_open/netcdf/netcdf-fortran-4.6.1/docs/old/netcdf-f77.texi:833, 847, 849–850, 944–945, 951, 961, 1500, 2055, 2061, 2067, 3680, 3692–3693, 3809, 3822–3823, 3892, 3908–3909, 4140, 4202, 4210, 4564, 4709, 5449, 5751, 5785, 5936, 6183, 6359, 9161`
- `source_code/sfincs/source/third_party_open/netcdf/netcdf-fortran-4.6.1/docs/netcdf.m4:490, 496, 530, 599, 742, 746, 1218`
- `source_code/sfincs/source/third_party_open/netcdf/netcdf-fortran-4.6.1/docs/texinfo.tex:412, 9696`
- `source_code/sfincs/source/third_party_open/netcdf/netcdf-fortran-4.6.1/docs/netcdf-f90-sec2-datasets.md:219, 235, 237, 239, 412, 623`
- `source_code/sfincs/source/third_party_open/netcdf/netcdf-fortran-4.6.1/docs/netcdf_fortran.3:68, 74, 105, 172`
- `source_code/sfincs/source/third_party_open/netcdf/netcdf-fortran-4.6.1/docs/netcdf-f90-sec6-variables.md:302, 415, 455, 606, 690, 1920, 1923`
- `source_code/sfincs/source/third_party_open/netcdf/netcdf-fortran-4.6.1/config.h.cmake.in:234`
- `source_code/sfincs/source/third_party_open/netcdf/netCDF 4.9.2/include/netcdf.h:244, 247, 382, 403, 415, 674, 679, 723, 751, 980`
- `source_code/sfincs/source/third_party_open/netcdf/netCDF 4.9.2/include/netcdf_json.h:111, 1065`
- `source_code/sfincs/source/third_party_open/netcdf/netCDF 4.9.2/include/netcdf_aux.h:83`
- `source_code/sfincs/source/third_party_open/netcdf/netcdf-fortran-4.6.1/fortran/netcdf4_func.F90:239, 243, 247, 250, 255, 262, 313, 319, 325, 349, 353, 356`
- `source_code/sfincs/source/third_party_open/netcdf/netcdf-fortran-4.6.1/fortran/module_netcdf4_nf_interfaces.F90:206, 209, 217, 220, 281, 286, 316, 320`
- `source_code/sfincs/source/third_party_open/netcdf/netcdf-fortran-4.6.1/fortran/nf_lib.c:116, 127, 145, 181`
- `source_code/sfincs/source/third_party_open/netcdf/netcdf-fortran-4.6.1/fortran/nf_control.F90:383`
- `source_code/sfincs/source/third_party_open/netcdf/netcdf-fortran-4.6.1/fortran/nf_nc4.F90:527, 530, 536, 549, 560, 569, 583, 754, 765, 800, 881, 884, 891, 905`
- `source_code/sfincs/source/third_party_open/netcdf/netcdf-fortran-4.6.1/fortran/module_netcdf4_nc_interfaces.F90:293, 299, 308, 315`
- `source_code/sfincs/source/third_party_open/netcdf/netcdf-fortran-4.6.1/nf_test4/ftst_var_compact.F:30–31`
- `source_code/sfincs/source/third_party_open/netcdf/netcdf-fortran-4.6.1/nf_test4/ftst_var_szip.F:29–30`
- `source_code/sfincs/source/third_party_open/netcdf/netcdf-fortran-4.6.1/nf_test4/ftst_vars6.F:28–29`
- `source_code/sfincs/source/third_party_open/netcdf/netcdf-fortran-4.6.1/nf_test4/f03tst_open_mem.F:42–43`
- `source_code/sfincs/source/third_party_open/netcdf/netcdf-fortran-4.6.1/nf_test/util.F:213, 216, 222–223, 246, 249, 255–256, 787, 791, 874`
- `source_code/sfincs/source/third_party_open/netcdf/netcdf-fortran-4.6.1/nf_test/tst_int64.F:93, 164, 255`
- `source_code/sfincs/source/third_party_open/netcdf/netcdf-fortran-4.6.1/nf_test/util03.F:230, 234, 240–241, 264, 267, 273–274, 819, 823, 906`

</details>

<details>
<summary>P042·P043·P044·P045·P046·P047·P048·P049 검색 결과</summary>

패턴: `\b(?:wind|dst_res|precip|aggregate|press|fill_value|magnitude|direction)\b`

- `source_code/sfincs/README.rst:35`
- `source_code/sfincs/docs/overview.rst:36, 44, 207`
- `source_code/sfincs/LICENSE:171, 239, 242–243`
- `source_code/sfincs/docs/tables/output_parameters.tab:23`
- `source_code/sfincs/docs/input.rst:110–112, 741, 855`
- `source_code/sfincs/docs/parameters.rst:10, 16, 22, 28, 46, 291, 343, 413, 607, 612, 617, 622, 637–638, 647`
- `source_code/sfincs/source/src/sfincs_ncoutput.F90:70, 125, 139, 153, 167, 193, 206, 234, 242, 252, 267, 287, 296, 309, 317, 332, 344, 359, 370, 381, 400, 410, 421, 432, 444, 456, 467, 480, 490, 502, 512, 516, 519, 524, 527, 531, 533, 535, 546, 554, 558, 572, 581, 589, 599, 607, 615, 623, 631, 639, 651, 664, 677, 737, 758, 816, 835, 1089, 1098, 1113, 1132, 1139, 1146, 1153, 1173, 1181, 1191, 1198, 1213, 1225, 1248, 1257, 1267, 1278, 1289, 1299, 1314, 1323, 1332, 1336, 1339, 1343, 1346, 1350, 1352, 1354, 1356, 1366, 1387, 1394, 1403, 1410, 1417, 1424, 1430, 1436, 1446, 1452, 1463, 1476, 1487, 1515, 1527, 1536, 1569, 1575, 1590, 1614, 1663, 1683, 1713, 1724, 1735, 1746, 1892, 1913, 1947, 1955, 1965, 1972, 1978–1979, 1985–1986, 1999, 2010, 2020, 2029, 2036, 2043, 2050, 2059, 2062, 2066, 2077, 2088, 2095, 2102, 2109, 2116, 2123, 2130, 2137, 2148, 2151, 2157, 2167, 2174, 2177, 2185, 2199, 2209, 2219, 2341, 2378, 2400–2401, 2446, 2463, 2484, 2501, 2518, 2535, 2537, 2550, 2567, 2582, 2584, 2603, 2616, 2631, 2644, 2657, 2670, 2683, 2696, 2713, 2732, 2786, 2816, 2846–2847, 2882, 2901, 2922–2924, 2946, 2967, 2982, 2999–3000, 3016, 3031, 3046, 3060, 3078, 3092, 3110, 3130, 3206–3227, 3281, 3296, 3410, 3423, 3508, 3539, 3594, 3609, 3624, 3636, 3648, 3660, 3671–3673, 3704, 3734, 3796, 3809, 3824, 3838, 3852, 3866, 3878–3880, 3944–3945, 3972–3973, 4015, 4030`
- `source_code/sfincs/source/src/sfincs_nonhydrostatic.f90:159`
- `source_code/sfincs/docs/input_forcing.rst:25, 29, 212, 214, 216, 218, 220, 222, 226, 237–238, 261, 265, 336, 345–347, 358–360, 372–374, 383, 385, 406, 408–409, 438, 444–445`
- `source_code/sfincs/docs/numerical_implementation.rst:84`
- `source_code/sfincs/docs/figures/.$Overview_status_SFINCS.drawio.bkp:402`
- `source_code/sfincs/source/src/sfincs_ncinput.F90:610, 655, 660, 983, 989`
- `source_code/sfincs/source/src/sfincs_boundaries.f90:215`
- `source_code/sfincs/source/src/sfincs_input.f90:310, 488, 729, 733`
- `source_code/sfincs/source/src/sfincs_data.f90:189, 192, 407, 409, 421`
- `source_code/sfincs/source/src/sfincs_output.f90:189, 226, 442, 587, 625, 631, 640`
- `source_code/sfincs/source/src/sfincs_discharges.f90:408`
- `source_code/sfincs/source/src/sfincs_lib.f90:223–224, 226, 233, 517, 733`
- `source_code/sfincs/source/src/sfincs_infiltration.f90:28, 63, 659, 705, 733, 811, 840, 894, 1015`
- `source_code/sfincs/source/src/sfincs_bathtub.f90:103, 107`
- `source_code/sfincs/source/src/snapwave/snapwave_boundaries.f90:269, 485, 487, 491, 495, 501, 507, 660, 747, 762, 766, 780, 814, 816`
- `source_code/sfincs/source/src/snapwave/snapwave_windsource.f90:98, 103, 108–110, 112–113, 155, 166`
- `source_code/sfincs/source/src/snapwave/snapwave_infragravity.f90:291`
- `source_code/sfincs/source/src/snapwave/snapwave_data.f90:26–29, 39–49, 69–72, 105, 115, 123, 236, 244, 279`
- `source_code/sfincs/source/src/snapwave/snapwave_ncoutput.F90:28, 107`
- `source_code/sfincs/source/src/sfincs_snapwave.f90:124, 157–158, 160, 277, 374, 376, 402, 552, 571, 661, 715, 717`
- `source_code/sfincs/source/src/sfincs_continuity.f90:116, 352–353, 373–374, 455, 473, 477`
- `source_code/sfincs/source/src/snapwave/snapwave_solver.f90:162, 189, 208, 210–213, 216, 248, 254, 261, 265, 298, 303, 305, 318, 350, 394, 426, 453, 463, 571, 627, 642, 664, 679, 687, 693, 750, 752, 799, 804, 809, 846, 1054, 1085, 1224–1226, 1244, 1323, 1332`
- `source_code/sfincs/source/src/snapwave/snapwave_domain.f90:363–365`
- `source_code/sfincs/source/src/snapwave/interp.F90:40, 43, 120, 123`
- `source_code/sfincs/source/src/sfincs_domain.f90:86–87, 99–100, 103, 115, 130, 2348, 2403`
- `source_code/sfincs/source/src/sfincs_momentum.f90:389, 547, 549, 565`
- `source_code/sfincs/source/src/sfincs_meteo.f90:72, 137–138, 155, 157, 159, 238, 243, 262, 317, 321, 409, 520, 586, 612, 657, 673, 679, 711, 751, 769, 896, 908, 931, 1074, 1211, 1235, 1273, 1297, 1348, 1357, 1408, 1412, 1592, 1602`
- `source_code/sfincs/docs/developments.rst:131`
- `source_code/sfincs/docs/index.rst:44`
- `source_code/sfincs/docs/input_structures.rst:149`
- `source_code/sfincs/docs/output.rst:148, 190, 194, 299, 303`
- `source_code/sfincs/docs/figures/Overview_status_SFINCS.drawio:402`
- `source_code/sfincs/source/COPYING:171, 239, 242–243`
- `source_code/sfincs/source/third_party_open/utils/toml-f/LICENSE-Apache:20`
- `source_code/sfincs/source/third_party_open/utils/geometry.f90:124, 165–168`
- `source_code/sfincs/source/third_party_open/netcdf/netCDF 4.9.2/include/netcdf.h:958`
- `source_code/sfincs/source/sfincs/x64/Release/LICENSING CONDITIONS DELTARES SFINCS SOURCE CODE.txt:171, 239, 242–243`
- `source_code/sfincs/source/third_party_open/netcdf/netcdf-fortran-4.6.1/config.h.cmake.in:210, 214`
- `source_code/sfincs/source/third_party_open/netcdf/netcdf-fortran-4.6.1/nf03_test/tst_f90.F90:61, 97`
- `source_code/sfincs/source/third_party_open/netcdf/netcdf-fortran-4.6.1/docs/old/netcdf-f90.texi:4957, 4976, 5031, 5046`
- `source_code/sfincs/source/third_party_open/netcdf/netcdf-fortran-4.6.1/docs/netcdf-f90-sec6-variables.md:393, 418, 484, 503`
- `source_code/sfincs/source/third_party_open/netcdf/netcdf-fortran-4.6.1/docs/old/netcdf-f77.texi:5734, 5753, 5808, 5823, 9284`
- `source_code/sfincs/source/third_party_open/netcdf/netcdf-fortran-4.6.1/nf_test4/ftst_vars6.F:161`
- `source_code/sfincs/source/third_party_open/netcdf/netcdf-fortran-4.6.1/nf_test4/f03tst_open_mem.F:208`
- `source_code/sfincs/source/third_party_open/netcdf/netcdf-fortran-4.6.1/docs/Doxyfile.developer:1517`
- `source_code/sfincs/source/third_party_open/netcdf/netcdf-fortran-4.6.1/fortran/module_netcdf4_nc_interfaces.F90:688, 694`
- `source_code/sfincs/source/third_party_open/netcdf/netcdf-fortran-4.6.1/fortran/module_netcdf4_nf_interfaces.F90:612, 615, 622, 626`
- `source_code/sfincs/source/third_party_open/netcdf/netcdf-fortran-4.6.1/fortran/nf_nc4.F90:1733, 1742, 1753, 1761, 1771, 1780`
- `source_code/sfincs/source/third_party_open/netcdf/netcdf-fortran-4.6.1/fortran/example_good.cdl:9, 29`
- `source_code/sfincs/source/third_party_open/netcdf/netcdf-fortran-4.6.1/docs/texinfo.tex:579, 1934, 5758`
- `source_code/sfincs/source/third_party_open/netcdf/netcdf-fortran-4.6.1/docs/Doxyfile.in:1484`
- `source_code/sfincs/source/third_party_open/netcdf/netcdf-fortran-4.6.1/docs/netcdf-f77.md:5138, 5156, 5207, 5220, 8747`

</details>

<details>
<summary>P050·P051·P052 검색 결과</summary>

패턴: `\b(?:dz|stype|discharge)\b`

- `source_code/sfincs/docs/overview.rst:88, 90`
- `source_code/sfincs/source/src/sfincs_ncoutput.F90:2198, 2201, 2208, 2211, 2218, 3445, 3470`
- `source_code/sfincs/source/src/sfincs_ncinput.F90:186, 209`
- `source_code/sfincs/source/src/sfincs_discharges.f90:10, 29, 55, 63, 108, 110, 136, 141, 148, 440, 520, 540, 616, 623, 627`
- `source_code/sfincs/source/src/sfincs_continuity.f90:501`
- `source_code/sfincs/docs/input.rst:417, 604, 607–608`
- `source_code/sfincs/docs/example.rst:23`
- `source_code/sfincs/docs/parameters.rst:276, 397, 540, 588, 593, 599`
- `source_code/sfincs/docs/developments.rst:289`
- `source_code/sfincs/docs/input_forcing.rst:29, 134–135, 142, 144, 160, 163, 205`
- `source_code/sfincs/docs/numerical_implementation.rst:80`
- `source_code/sfincs/docs/input_structures.rst:123, 132, 145, 147, 149, 155, 157, 186–187, 195–196, 203, 205, 222`
- `source_code/sfincs/docs/output.rst:136, 323–324, 327–328`
- `source_code/sfincs/source/third_party_open/netcdf/netcdf-fortran-4.6.1/docs/texinfo.tex:9473–9475`

</details>

<details>
<summary>B135 검색 결과</summary>

패턴: `\b(?:Darcy|Weisbach)\b`

- `source_code/sfincs/docs/input_structures.rst:222`

</details>

## Sonnet 수정 목록 반영 여부

| 번호 | 반영 여부 | 이유·위치 |
|---:|---|---|
| 1 | 범위 밖 | ADCIRC Blain PBL·wind/p15.F. ADCIRC 노트와 보고서는 쓰기 허용 대상이 아니다. |
| 2 | 범위 밖 | EFDC ISVARSETTLE·EE GUI. EFDC 노트와 보고서는 쓰기 허용 대상이 아니다. |
| 3 | 범위 밖 | ADCIRC wetdry.F의 IT·BTIME_END. 이 묶음에서 수정하지 않았다. |
| 4 | 범위 밖 | ADCIRC Duv의 PDF 판독 위치. 이 묶음에서 수정하지 않았다. |
| 5 | 범위 밖 | EFDC PSHADE와 수초 소광. 이 묶음에서 수정하지 않았다. |
| 6 | 범위 밖 | ADCIRC NetCDF nodal 변수명 근거. 이 묶음에서 수정하지 않았다. |
| 7 | 범위 밖 | ADCIRC XDMF 최종화·np/np_g. 이 묶음에서 수정하지 않았다. |
| 8 | 범위 밖 | EFDC TOXS/DYES 초기값. 이 묶음에서 수정하지 않았다. |
| 9 | 범위 밖 | ADCIRC subgrid 단위. 이 묶음에서 수정하지 않았다. |
| 10 | 범위 밖 | ADCIRC 동적 수위 보정 램프. 이 묶음에서 수정하지 않았다. |
| 11 | 반영 | sfincs_infiltration.md의 cv-s-b047을 정본으로 지정했다. numerical-implementation:267, changelog:50·65·83, architecture-source-map:222의 원래 추가 줄을 링크로 줄였다. sfincs_infiltration.f90:44,52–55를 정본과 허용 보고서 §5 B047·C021에 반영했다. |
| 12 | 범위 밖; 동일 유형 검사 | 목록의 문구는 ADCIRC 항목이다. 이 묶음에서 같은 노트 안에 없는 절을 가리키는 “2.7의 판정” 유형은 찾지 못했다. 새 참조는 보고서 행 ID 또는 실제 정본 앵커로 연결했다. |
| 13 | 범위 밖 | EFDC mhkpwr.f90의 fraction·1.0+비율. 이 묶음에서 수정하지 않았다. |

## 모든 대상 줄의 처리 대장

다음 표의 줄 번호는 작업 시작 시점의 노트 번호이다. 각 노트의 정정·보완·이상 없음 집합은 서로 겹치지 않는다. 세 집합의 합집합은 해당 노트의 원래 + 줄 전체이다.
이상 없음은 이 작업의 대조에서 새 정정 사항을 찾지 못했다는 뜻이다. 기존 E 후보의 결함을 부정하는 뜻은 아니다.

| 노트 | 정정한 원래 + 줄 | 보완한 원래 + 줄 | 이상 없는 원래 + 줄 |
|---|---|---|---|
| [SFINCS/sfincs-model-building-running.md](../../../models/SFINCS/manual-notes/sfincs-model-building-running.md) | 64–72 | 없음 | 23, 60–63, 73–75 |
| [SFINCS/sfincs-numerical-implementation.md](../../../models/SFINCS/manual-notes/sfincs-numerical-implementation.md) | 109, 165, 176, 261 | 105, 177, 258–260, 262–263, 267, 308 | 21, 34–40, 61, 82–91, 103–104, 106–108, 110–117, 133–138, 141–143, 149–150, 155–158, 161–164, 166, 171–175, 178–182, 191, 196, 198, 203, 206–209, 243–250, 254–257, 264, 270, 305–307 |
| [SFINCS/sfincs-parameters-io-reference.md](../../../models/SFINCS/manual-notes/sfincs-parameters-io-reference.md) | 68, 121, 191, 203, 321–322, 363, 365, 418 | 53, 57–58, 76, 93, 95, 117, 119, 152, 162–163, 165, 169, 171–173, 180, 201, 208, 225, 318–320, 357–358, 387–391, 394, 396–400, 402–404, 419, 421–424, 427, 445 | 15, 38–40, 46–52, 54–56, 59–60, 66–67, 69–75, 84, 110–116, 118, 120, 122–126, 141, 145, 150–151, 153–161, 164, 166–168, 179, 181–182, 192–200, 202, 204–207, 285–289, 298–300, 315, 374, 382–386, 392–393, 395, 401, 405–417, 420, 428, 442–444 |
| [SFINCS/sfincs-v2.4.0-galibier-changelog-known-issues.md](../../../models/SFINCS/manual-notes/sfincs-v2.4.0-galibier-changelog-known-issues.md) | 40 | 36, 50, 56–59, 65, 83 | 14, 38, 52–55, 77, 81, 92–95 |
| [SFINCS/sfincs-architecture-source-map.md](../../../models/SFINCS/source-analysis/sfincs-architecture-source-map.md) | 없음 | 221–224, 228 | 13, 20–38, 58, 72, 78, 110, 153–157, 182–186, 214–220, 225–227 |
| [SFINCS/sfincs_boundaries_forcing.md](../../../models/SFINCS/source-analysis/sfincs_boundaries_forcing.md) | 없음 | 95, 102, 160, 206, 291, 293, 327 | 16, 91–94, 96, 161–162, 166, 202–205, 207, 209, 215, 221, 235–237, 324–326 |
| [SFINCS/sfincs_flow_solver.md](../../../models/SFINCS/source-analysis/sfincs_flow_solver.md) | 165, 209 | 92–93, 119, 224, 240 | 16, 58–59, 88–91, 94, 115–118, 120, 125, 146–148, 156–157, 161–164, 166, 223, 225–226, 237–239 |
| [SFINCS/sfincs_infiltration.md](../../../models/SFINCS/source-analysis/sfincs_infiltration.md) | 없음 | 51, 65, 70–71, 92 | 15, 39–42, 89–91 |
| [SFINCS/sfincs_io_data.md](../../../models/SFINCS/source-analysis/sfincs_io_data.md) | 없음 | 116, 209, 231, 291 | 12, 95–108, 110–115, 117–118, 130, 205–208, 210, 288–290 |
| [SFINCS/sfincs_nonhydrostatic_wavemaker.md](../../../models/SFINCS/source-analysis/sfincs_nonhydrostatic_wavemaker.md) | 없음 | 140, 218 | 15, 114–123, 136–139, 141, 215–217 |
| [SFINCS/sfincs_snapwave.md](../../../models/SFINCS/source-analysis/sfincs_snapwave.md) | 50, 133 | 132, 152, 237 | 12, 40–41, 44–45, 59–61, 66–84, 94–96, 128–131, 134, 148–151, 153, 183, 224, 232, 235–236 |
| [SFINCS/sfincs_structures_physics.md](../../../models/SFINCS/source-analysis/sfincs_structures_physics.md) | 없음 | 74, 195, 250 | 12, 70–73, 75, 80–82, 167, 247–249 |
| [SFINCS/sfincs_subgrid_quadtree.md](../../../models/SFINCS/source-analysis/sfincs_subgrid_quadtree.md) | 147 | 115, 191, 220 | 12, 109–114, 137, 143–146, 148, 187–190, 192, 217–219 |
| [XBeach/xbeach-coupled-physics-contracts.md](../../../models/XBeach/source-analysis/xbeach-coupled-physics-contracts.md) | 없음 | 112–113 | 5, 17, 21–40, 45, 49–54, 56, 105–111 |
| [XBeach/xbeach_mode_dispatch.md](../../../models/XBeach/source-analysis/xbeach_mode_dispatch.md) | 없음 | 없음 | 123, 140, 147 |
| [XBeach/xbeach_nonh.md](../../../models/XBeach/source-analysis/xbeach_nonh.md) | 없음 | 없음 | 6, 50, 52–58, 60–68 |
| [XBeach/xbeach_vegetation.md](../../../models/XBeach/source-analysis/xbeach_vegetation.md) | 없음 | 70, 73 | 6, 38, 44–56, 61–62, 69, 71–72, 74 |

원문 위치의 기준: SFINCS의 `docs/`와 소스 파일은 `models/SFINCS/raw/source_code/sfincs/` 아래이다. XBeach의 Fortran·정의 파일은 `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/` 아래이다.
XBeach PDF의 인쇄 쪽과 PDF 쪽은 `_staging/recovery/read/XBeach/`의 해당 문서 판독 기록을 기준으로 확인했다. 다른 매뉴얼의 같은 파일명으로 바꾸지 않았다.
기존 XBeach 모드 분기 3줄과 비정수압 노트 18줄은 원문의 조건·식·보고서 분류와 대응하므로 수정하지 않았다.

검사 결과: 노트 내용은 준비한 변경안과 일치했다. 보고서의 원행별 분류 재집계가 본문의 수치와 일치했다. 새 로컬 링크의 파일과 앵커가 존재했다. `git diff --check`는 지정 노트와 허용 보고서에서 통과했다.

정정 28, 보완 104, 분류 변경 54, 이상 없음 532
