---
title: "ADCIRC 기능 지도와 근거 준비 상태"
topic: general
canonical_source: self
citation_status: source-needed
note_author: "Codex — Fable 5.1 계획·독립 검토 반영"
note_date: 2026-09-14
review_by: "Claude Fable 5.1 — 기능 분류/새 조석 확인 방법 한정 대조; 과학적 사람 승인 아님"
verification_method: "공식 기능 분류 및 아래 선정 문서 절 대조. 기존 노트는 탐색·metadata 확인이며 전체 주장 재검증 아님. 조석 입력 한정 코드 대조는 연결 노트의 범위를 따른다. 실제 실행·수치/물리 검증·개별 입력 품질 확인 미수행."
historical_verification: "기존 2026-04 토픽 조직도의 verified 이력은 git에 보존. 갱신한 기능 지도의 승인으로 상속하지 않음."
source_correction_human_approval: not-issued
---

# ADCIRC 기능 지도와 근거 준비 상태

기능을 찾고, 설정·식·구현·검증에서 어떤 근거를 더 확보해야 하는지 안내한다. **기능 목록의 정리와 모델의 검증 완료는 별개다.** 이 지도는 새 구성의 `source-needed` 노트이며, 링크된 기존 노트의 `verified`·갭·과거 승인도 각 노트의 원래 범위에 한정된다.

## 기준 판본과 읽는 법

- **S**: `models/ADCIRC/raw/source_code/adcirc/`의 코드와 동봉 `docs/`, HEAD `6037225ce4573efd3c1f8877a5dc908d01c199a8`. 아래 상대 코드·문서 인용은 이 루트 기준이다. 기존 분석 노트가 다른 판본을 기술하면 그 노트의 판본을 먼저 확인한다.
- **W**: [공식 문서 사이트](https://adcirc.github.io/adcirc/) 2026-09-14 조회판. S와 전역적으로 같다고 가정하지 않는다. [이론 안내](https://adcirc.github.io/adcirc/theory/index.html)는 v44.XX 보고서와 이후 기능 보강을 구분한다. 오래된 이론식과 S의 모든 옵션이 일치한다는 뜻은 아니다.
- **T**: `models/ADCIRC/raw/source_code/adcirc-testsuite/`, HEAD `72bb573073ea89e538890f9352dd8e92bae562f5`. 예제·회귀검사 근거이며 ADCIRC S의 실행 검증 이력이 아니다.
- **포함**은 모델 기능 근거를 구축할 범위, **보류**는 필요한 문서·옵션·판본을 더 확인할 범위, **대상외**는 이 ADCIRC 지도에서 내부를 분석하지 않을 범위다. 이전 전체 감사 집합의 범위를 바꾸는 표가 아니다.
- **분류 확인**은 공식 개요/목차에 항목이 있다는 뜻이다. **조건 대조**는 명시한 절의 설명만 읽었다는 뜻이다. **기존 노트**는 근거 위치를 확보했지만 그 구현 주장을 이번에 재대조하지 않았다는 뜻이다. 세 표현 모두 기능 전체의 준비 완료를 뜻하지 않는다.

## 공식 기능 분류와 기존 근거

행의 판본은 S이며 W는 현재 분류를 교차 확인하는 데 썼다. 각 행의 문서·코드 확인 한계와 다음 갭을 함께 읽는다. 실행 확인·수치 검증·물리 검증·입력 품질의 공통 상태는 다음 절에 있다.

| 기능 | 범위와 이유 | 문서 지원의 확인 범위 | 코드 구현 근거 위치·이번 확인 | 다음에 메울 근거 (`source-needed`) |
|---|---|---|---|---|
| F01 격자·좌표·수심 | 포함 — 모든 입력과 결과의 공간 기준 | [fort.14][d14]의 격자/경계 구조, [ICS][dics] §Available ICS Values 조건 대조 | [전처리](adcirc-preprocessing-foundation.md), [수심](adcirc-bathymetry-input-foundation.md), [도메인 설계](adcirc-domain-design-process.md): 기존 노트 | 원자료 기준면·해상도·오차, 좌표 변환과 노드 수심의 독립 대조 |
| F02 2D 지배식·수치 옵션 | 포함 — 설정에 따른 해법 구분 | [IM][dim] §Default IM Values·Six-digit IM Codes의 분류/일부 조건 대조 | [GWCE](adcirc-gwce-implementation.md), [운동량](adcirc-momentum-implementation.md), [시간 흐름](adcirc-timestep-orchestration.md), [선형해법](adcirc-itpack-solver.md): 기존 노트 | 선택 IM과 TAU0·시간가중·DTDP 조합의 식/분기 및 기준해·보존/민감도 |
| F03 마찰·수평 혼합·공간 속성 | 포함 — 운동량·소산 설정 | [설정 분류][dcfg] Model/Physics Parameters 항목 확인; 수치 권고값 미대조 | [운동량](adcirc-momentum-implementation.md), [노드 속성](adcirc-nodal-attributes.md): 기존 노트 | NOLIBF·ESLM·fort.13 속성의 활성 조건/기본값, 물리적 계수 근거 |
| F04 조석 수위 경계 | 포함 — 첫 입력 근거 묶음 | [상세 정의][dparam] NBFR·AMIG/FF/FACE·EMO/EFA 조건 대조 | [harmonic-prep](tide/adcirc-tide-harmonic-prep.md), [forcing](tide/adcirc-tide-forcing-implementation.md): NBFR·노드순서·위상/시간 한정 대조 | 외부 DB 규약과 실제 경계 자료의 품질·변환 확인; 아래 조석 진입점 |
| F05 조석 퍼텐셜·SAL | 포함 — 경계 수위와 다른 강제 항 | [상세 정의][dparam] NTIP·NTIF 및 [조석 개요][dtide]의 불일치 대조 | [forcing](tide/adcirc-tide-forcing-implementation.md): 전통 분조 ETRF 항 한정 대조. [조석 경로](adcirc-tidal-forcing.md)의 나머지는 기존 노트 | full-formula/SAL 전체 조건·파일·분조 정합, 정량 효과와 외부 SAL 제품 정의 |
| F06 내부조석 에너지 전환 | 포함 — 공식 조석 분류에 존재 | [조석 개요][dtide] 항목 확인; 수심/소산 권고 수치는 이번 지도의 확정 근거로 쓰지 않음 | [조석 경로](adcirc-tidal-forcing.md), [노드 속성](adcirc-nodal-attributes.md): 기존 노트 | 적용 조건·평균화·소산량 근거와 기존 source-needed 정량 주장 |
| F07 바람·기압·폭풍해일 | 포함 — 공식 응용 기능 | [Model Features][dfeatures]·[설정 분류][dcfg] Meteorological Forcing/GAHM 항목 확인 | [NWS 구현](adcirc-met-forcing-implementation.md), [GAHM](adcirc_gahm_vortex_model.md), [폭풍해일](storm-surge/adcirc-storm-surge.md): 기존 노트 | NWS별 시간/공간/단위와 풍응력식, 입력 오차·독립 관측 검증 |
| F08 유량·하천·비주기 수위·방사 경계 | 포함 — 물과 운동량의 경계 전달 | [경계 분류][dbc]와 [fort.14][d14] 항목/형식 확인; 세부 IBTYPE 조건은 기존 노트 재대조 필요 | [경계조건](adcirc-boundary-conditions.md), [주기 유량](adcirc-nffr-periodic-flux-boundary.md): 기존 노트 | IBTYPE·NFFR·비주기 입력의 부호/단위/순서와 물수지 |
| F09 젖음·마름과 연안 침수 | 포함 — 공식 침수 응용 기능 | [Model Features][dfeatures]·[설정 분류][dcfg] NOLIFA 항목 확인 | [wetting/drying](adcirc-wetting-drying-implementation.md): 기존 노트 | H0·속도 문턱의 조건과 미출처 권고값, 침수 경계·질량 보존 검증 |
| F10 제방·월류·VEW | 포함 — 구조물과 수로 경계 | [특수기능][dspecial]·[VEW][dvew] §What are VEWs 조건 대조: 문서는 lumped explicit 모드 제한을 명시 | [weir](adcirc-weir-boundary.md), [경계조건](adcirc-boundary-conditions.md): 기존 노트 | IBTYPE/격자·구조물 제원과 활성 분기, 월류식/보존의 검증 |
| F11 3D 순환·경압·2D+ | 포함 — 공식 경압 기능을 누락하지 않음 | [IM][dim]의 모드 분류, [2D+][d2plus] §Version 대조: 일부 v55, 개선은 v56 이상이라는 문서 구분 유지 | [3D 모드](adcirc-3d-mode.md), [VSSOL](adcirc-3d-vssol-vertical-scheme.md), [경압 결합](adcirc-baroclinic-coupling.md): 기존 노트 | 층/혼합/밀도·열염 입력과 외부 OGCM 전달 계약, 2D+와 3D 해법 구분 |
| F12 물질 이송·준설/투기 응용 | 포함 — 공식 응용 목록에 존재 | [Model Features][dfeatures] 항목과 [IM][dim] 수동 스칼라 모드 분류 대조 | [transport](adcirc-transport-solver.md): 기존 3D 노트. [문헌 색인](../web-refs/adcirc-foundational-papers.md) §7은 서지/초록 수준 | 2D/3D 선택 경로와 물질·경계 조건. 응용 명칭만으로 현재판의 퇴적물·지형변동 기능을 확정하지 않음 |
| F13 파랑–흐름 상호작용 | 포함 — ADCIRC 결합 인터페이스 | [Model Features·Programs][dfeatures]의 ADCSWAN/PADCSWAN 분류 확인 | [SWAN 결합](adcirc-swan-coupling.md): 기존 노트 | 교환 변수·단위·시각·격자·보간·피드백·중복 물리와 양쪽 판본 |
| F14 초기조건·ramp·재시작 | 포함 — 의도한 시간 구간의 실행 | [설정 분류][dcfg] Initial Conditions/Ramping 항목 확인 | [hotstart](adcirc-hotstart.md), [fort.15 확인표](adcirc-fort15-checklist-v1.md): 기존 노트 | 초기 수위·하천·hotstart 시각/상태와 외력 연속성, spin-up 판정 |
| F15 실행·빌드·MPI | 포함 — 모델 자체의 실행 경로 | [Programs][dfeatures] ADCIRC/PADCIRC/ADCPREP와 [실행 안내][drun] 분류 확인 | [병렬 구현](adcirc-parallel-implementation.md), [파일 연결](adcirc-fort-files-reference.md): 기존 노트 | 빌드 옵션·실행파일·분할/halo/출력 회수의 실제 확인; 라이브러리 내부는 제외 |
| F16 출력·조화분해·진단 | 포함 — 실행과 결과를 확인할 수단 | [fort.51][d51] 구조와 [상세 정의][dparam] NFREQ·THAS/THAF·NHAINC·NHASE 계열 대조 | [출력 구현](adcirc-output-writers-implementation.md), [조석 경로](adcirc-tidal-forcing.md): 기존 노트 | 요청한 정점·변수·시간의 실제 출력, 분석창·분조분리·기준시각·진단 한계 |
| F17 교각·동적 수위 보정·얼음 | 보류 — 별도 조건 대조를 먼저 할 확장 기능 | [특수기능][dspecial]의 3항목과 각 소개 절 확인. 이 지도로 구현/정확도 확정 안 함 | [노드 속성](adcirc-nodal-attributes.md), [시간 흐름](adcirc-timestep-orchestration.md), [기상](adcirc-met-forcing-implementation.md): 인접 근거 후보 | 각 전용 문서/논문과 활성 코드 연결. 동적 보정 문서의 초기 v53 결함 경고 포함 |
| F18 DG·Ali dispersion·subgrid·시변 지형/위어 | 보류 — 관련 기능별 판본/범위 추가 대조 필요 | DG는 [DG 노트](adcirc-dg-continuity-solver.md)의 별도 PR 근거 후보; Ali는 [조석 목차][dtide] 항목. 나머지는 기존 수심/위어 노트의 문서 포인터이며 이번 지원 조건 미확인 | [DG](adcirc-dg-continuity-solver.md), [수심](adcirc-bathymetry-input-foundation.md), [weir](adcirc-weir-boundary.md): 기존 노트 | PR·문서·로컬 HEAD의 실제 포함 여부와 옵션별 알고리즘·입력 계약 |
| F19 LIBADC·ASWIP·운영/전처리 도구 | 보류 — 선택 실행에 필요한 인터페이스까지만 | [Programs][dfeatures] LIBADC/ASWIP/Utilities 분류 확인 | [ASGS](adcirc_asgs_operational_system.md), [전처리](adcirc-preprocessing-foundation.md), [도구 색인](../manual-notes/12-tooling-ecosystem.md): 기존 노트 | 선택한 기능에 필요한 버전·호출·자료 변환 계약. 도구 내부 전량 판독은 조건 아님 |
| F20 독립 SWAN·범용 부속 도구 내부 | 대상외 — 별도 모델/의존성의 내부 | [Programs][dfeatures] SWAN/PUNSWAN은 구별된 프로그램 | SWAN 자체는 [SWAN 모델](../../SWAN/README.md), ADCIRC 쪽은 F13/F15 | ADCIRC 모델 자체의 MPI 호출과 결합 경로는 F13/F15에 포함 |

이 표는 공식 개요의 일곱 응용 분류를 F04/F07(조석·바람), F07/F09(해일·홍수), F13(파랑 상호작용), F12(준설·투기/이송), F11(경압), F09/F10(침수·방호)에 연결한다. 응용 분류를 지원 옵션 전체의 검증으로 해석하지 않는다. [Model Features][dfeatures]와 [Model Configuration][dcfg]·[Special Features][dspecial]를 함께 사용했으며, 모든 하위 옵션을 나열한 참조서는 아니다.

## 근거 수준과 준비 상태

| 수준 | 이번 확보한 것 | 미확인·다음 필요 근거 |
|---|---|---|
| 문서 지원 | 표의 공식 분류·선정 절과 조건 | 목차만 확인한 기능의 상세 지원 조건, 판본 차이 |
| 코드 구현 | 기존 노트로 경로 연결; 조석 입력의 명시 구간만 한정 대조 | 그 외 노트의 코드/식/기본값을 실제 사용할 주장별로 재대조 |
| 실행 확인 | [공식 예제][dexamples]·[baseline 선택](adcirc-baseline-selection.md)·[구성](adcirc-baseline-anatomy.md) 위치 | **이번 미수행**. 실행파일·입력·옵션·로그·기대한 출력의 실제 증거 |
| 수치 검증 | T의 회귀검사 위치와 [예제 색인](../manual-notes/07-examples-index.md) | **이번 미수행**. 회귀 일치와 별도로 해석해/기준해·보존량·격자/시간 민감도 근거 |
| 물리 검증 | [기초 문헌 색인](../web-refs/adcirc-foundational-papers.md) §2/§4의 후보 위치 | **이번 미수행**. 색인은 첫 페이지 서지/초록 확인 범위이므로 논문 결과 대조 완료가 아님. 독립 관측·실험·오차/불확실성·적용 조건 필요 |
| 입력 품질·불확실성 | [조석 확인 방법](tide/adcirc-tide-harmonic-prep.md#input-quality-and-validation) | **개별 자료 확인 미수행**. 사용할 DB/지형/관측 판본과 범위·변환·오차를 먼저 고정 |

## 조석 입력에서 시작하기

1. **입력 형식·식·코드**: [harmonic-prep의 한정 대조와 확인 방법](tide/adcirc-tide-harmonic-prep.md#input-quality-and-validation). NBFR/노드순서/위상·시간, NTIP와 NTIF 구분을 읽는다. [조석 개요][dtide]의 `NTIP`·`AMIG` 설명 불일치는 상세 정의·코드에 대조한 주의사항이 이 노트에 있다.
2. **실행 확인 후보**: T의 `test_list.yaml:423–434`가 `adcirc_quarterannular-2d-netcdf`와 여섯 비교 출력 파일을 지정한다. `test_runner/adcirc_test/adcirctest.py:429–445`는 해당 `control/`과 계산 출력을 대조한다. 이 회귀 일치가 독립 관측검증을 대신하지 않는다. T README의 허용오차를 해역의 물리 허용오차로 복사하지 않는다.
3. **다른 강제 경로 후보**: [전지구 M2 예제][dglobal]는 퍼텐셜/SAL과 전지구 조화분해를 다루는 v55 이상 예제다. 개방경계 NBFR 예제와 구분한다. 그 예제의 시간간격·계수를 지역 모델 권고값으로 사용하지 않는다.
4. **다음 근거 확보**: 외부 DB의 위상·노달보정·단위 원문, 변환/보간 확인, 독립 관측의 기준면·시간·품질 및 목적별 오차 기준. 기준 미확정인 채 실행·물리 검증 준비 완료로 표시하지 않는다.

## 공통 자료와 비교 시작 경계

[모델 기초](adcirc.md), [fort.* 참조](adcirc-fort-files-reference.md), [파라미터 용어](adcirc-parameter-glossary-v1.md), [매뉴얼 허브](../manual-notes/01-docs-hub.md), [공식 자원](../web-refs/adcirc-official-resources.md)은 여러 기능이 공유하는 탐색 자료다. 현재의 지도만으로 새 비교·융합 결론을 확정하지 않는다. 참여 기능의 설정·식·코드·입력 규약과 필요한 검증 근거가 갖춰진 주장부터 연결하며, 실제 결합은 변수·단위·좌표/기준면·시간·보간/보존·피드백·중복 물리를 추가로 확인한다. 구축 기준은 [BUILD-PLAN §4–7](../../../BUILD-PLAN.md)에 따른다.

[dfeatures]: https://adcirc.github.io/adcirc/introduction/what_is_adcirc.html
[dcfg]: https://adcirc.github.io/adcirc/user_guide/model_configuration/index.html
[dspecial]: https://adcirc.github.io/adcirc/user_guide/special_features/index.html
[dtide]: https://adcirc.github.io/adcirc/user_guide/model_configuration/tides/index.html
[dparam]: https://adcirc.github.io/adcirc/technical_reference/parameter_definitions/index.html
[d14]: https://adcirc.github.io/adcirc/technical_reference/input_files/fort14.html
[d51]: https://adcirc.github.io/adcirc/technical_reference/output_files/fort51.html
[dim]: https://adcirc.github.io/adcirc/user_guide/model_configuration/model_parameters/im.html
[dics]: https://adcirc.github.io/adcirc/user_guide/model_configuration/model_parameters/ics.html
[dbc]: https://adcirc.github.io/adcirc/user_guide/model_configuration/boundary_conditions/index.html
[d2plus]: https://adcirc.github.io/adcirc/user_guide/special_features/adcirc2d_plus.html
[dvew]: https://adcirc.github.io/adcirc/user_guide/special_features/vertical_element_walls.html
[drun]: https://adcirc.github.io/adcirc/user_guide/running_adcirc/index.html
[dexamples]: https://adcirc.github.io/adcirc/user_guide/examples/index.html
[dglobal]: https://adcirc.github.io/adcirc/user_guide/examples/global_astronomical_m2_tide.html

S의 선정 근거 구간은 아래와 같다. 코드는 연결된 조석 노트에 표시한 한정 구간만 대조했으며, 목록에 없는 세부 옵션은 이번 지원 조건 확인에 포함하지 않는다.

- 공식 분류: `docs/introduction/what_is_adcirc.rst:4–33`; `docs/theory/index.rst:1–8`; `docs/user_guide/model_configuration/index.rst:1–14`, `model_parameters/index.rst:1–18`, `physics_parameters/index.rst:1–11`, `initial_conditions/index.rst:1–11`, `boundary_conditions/index.rst:1–12`; `docs/user_guide/special_features/index.rst:1–15`; `docs/user_guide/running_adcirc/index.rst:1–11`.
- 모드·격자·특수기능 조건: `docs/user_guide/model_configuration/model_parameters/im.rst:10–130`, `ics.rst:10–62`; `docs/technical_reference/input_files/fort14.rst:6–41`; `docs/user_guide/special_features/adcirc2d_plus.rst:8–23`, `vertical_element_walls.rst:6–18`, `bridge_piers.rst:1–21`, `dynamic_water_level_correction.rst:7–32`, `ice_modifications.rst:1–36`.
- 조석·출력: `docs/user_guide/model_configuration/tides/index.rst:1–72`; `docs/technical_reference/parameter_definitions/index.rst:452–459,544–550,758–801,1140–1187,1191–1213`; `docs/technical_reference/output_files/fort51.rst:1–28`.
- 공개 예제: `docs/user_guide/examples/index.rst:1–45`, `global_astronomical_m2_tide.rst:8–48`. T의 회귀 비교 위치는 위 조석 진입점에 별도로 인용했다.
