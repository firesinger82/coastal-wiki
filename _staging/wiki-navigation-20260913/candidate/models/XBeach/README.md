# models/XBeach

이 디렉토리는 XBeach 구현·메커니즘의 canonical이다. 원본과 AI 분석은 각 노트의 인용·frontmatter로 구분한다.

## 기능별 탐색

아래는 기존 노트로 가는 **탐색 링크**다. 링크가 그 노트의 검증·승인을 이 파일에 승계시키지 않는다 ([CONVENTIONS.md §8.1](../../CONVENTIONS.md)).

범례 — `V` = `citation_status: verified` / `V*` = verified 노트이지만 **2026-09-12 AI 정정에 대한 사람 승인 미발급**(`source_correction_human_approval: not-issued`) / `D` = `draft-unsourced`(새 주장 사람 검토 대기).

| 기능 | 노트 |
|---|---|
| 공식 자료·판본 | [공식 자료](web-refs/xbeach-official-resources.md) V [미감사] · [문서 스택](manual-notes/01-local-manual-stack.md) V [미감사] |
| 모드 선택·실행 흐름 | [모드 dispatcher](source-analysis/xbeach_mode_dispatch.md) V* [미감사] · [메인 프로그램](source-analysis/xbeach.md) V [미감사] · [초기화](source-analysis/xbeach_initialize.md) V* [미감사] · [시간 간격 제어](source-analysis/xbeach_timestep_control.md) V [미감사] · [입력 파라미터](source-analysis/xbeach_params.md) V [미감사] · [인프라 모듈](source-analysis/xbeach_infrastructure.md) V* [미감사] |
| 파랑 계산 | [파랑 작용량 균형](source-analysis/xbeach_wave_action_balance.md) V* [미감사] · [정상 파랑](source-analysis/xbeach_wave_stationary.md) V* [미감사] · [단일 방향](source-analysis/xbeach_single_dir.md) V [미감사] · [쇄파](source-analysis/xbeach_wave_breaking.md) V [미감사] · [파랑 보조 함수](source-analysis/xbeach_wave_functions.md) V [미감사] |
| 파랑 경계·생성 | [경계 파랑 생성](source-analysis/xbeach_wave_boundary_generation.md) V* [미감사] · [파랑 경계 모듈](source-analysis/wave/xbeach_wave_boundary.md) V* [미감사] · [경계·wave setup](source-analysis/wave/xbeach-boundary-and-wave-setup.md) V [미감사] |
| 흐름·경계·비정수압 | [흐름 solver](source-analysis/xbeach_flow_solver.md) V* [미감사] · [수치 solver](source-analysis/xbeach_solver.md) V [미감사] · [흐름 경계조건](source-analysis/xbeach_flow_boundary_conditions.md) V [미감사] · [비정수압](source-analysis/xbeach_nonh.md) V* [미감사] · [조위 강제](source-analysis/xbeach_tide_forcing.md) V* [미감사] · [Q3D](source-analysis/xbeach_q3d.md) V [미감사] |
| 표사·지형 변화 | [형태 변화](source-analysis/xbeach_morphology.md) V* [미감사] · [형태 변화 기초](source-analysis/xbeach-morphology-foundation.md) V [미감사] · [intra-wave 표사](source-analysis/xbeach_intrawave_sediment_transport.md) V* [미감사] · [avalanching](source-analysis/xbeach_avalanching.md) V [미감사] · [저면 마찰](source-analysis/xbeach_bed_friction.md) V [미감사] · [지하수](source-analysis/xbeach_groundwater.md) V [미감사] |
| 선택 기능 | [식생](source-analysis/xbeach_vegetation.md) V* [미감사] · [선박 파](source-analysis/xbeach_ship_waves.md) V [미감사] · [BeachWizard](source-analysis/xbeach_beachwizard.md) V [미감사] · [SWAN 연계](source-analysis/xbeach_swan_handoff.md) V [미감사] |
| 출력·용어 | [출력](source-analysis/xbeach_output.md) V* [미감사] · [파라미터 용어집](source-analysis/xbeach-parameter-glossary-v1.md) V [미감사] |
| 상태 계약·수식 대응 (검토본) | [초기화·hotstart·BMI·종료 계약](source-analysis/xbeach-lifecycle-state-contracts.md) D · [지형·지하수·Q3D 연결 계약](source-analysis/xbeach-coupled-physics-contracts.md) D · [빌드·모드 연결](source-analysis/xbeach-build-mode-connectivity.md) D · [매뉴얼 수식–구현 대응](manual-notes/xbeach-manual-equation-code-contracts.md) D |

`D` 네 편은 새 주장의 사람 검토를 받지 않았으므로 승인 완료 근거로 인용할 수 없다. 매뉴얼 수식–구현 대응도 XBeach 전 수식의 검증 완료를 뜻하지 않는다(고정 잔여 R2/R4 미완). 전체 모델 연결 감사는 미완이며, 이 목차는 456파일 전량의 의미 판독 완료를 뜻하지 않는다.

갭 표기: `[공시]` = `has_source_needed: true`, `[갭없음]` = `false`, `[미감사]` = 필드 부재(unknown). `V`와 `V*`만으로 갭 부재를 뜻하지 않는다.

## 개념·이론으로 돌아가기

| 개념 축 | 문서 |
|---|---|
| 파랑 | [concepts/waves](../../concepts/waves/README.md) |
| 조석 | [concepts/tides](../../concepts/tides/README.md) |
| 표사이동 | [concepts/sediment-transport](../../concepts/sediment-transport/README.md) |
| 처오름대 | [concepts/swash-zone](../../concepts/swash-zone/README.md) |
| 모델 간 비교 | [쇄파 소산 cross-model](../../concepts/waves/wave-breaking-cross-model.md) V [공시] · [저면마찰 cross-model](../../concepts/currents/bottom-friction-cross-model.md) V [공시] |

## 모델과 모드

XBeach의 로컬 소스, 공식 문서와 배포처는 [공식 자료](web-refs/xbeach-official-resources.md)와 [문서 스택](manual-notes/01-local-manual-stack.md)에 정리한다. `stationary`, `surfbeat`, `nonh`의 분기와 별도 비정수압 층 설정은 [모드 dispatcher](source-analysis/xbeach_mode_dispatch.md)를 따른다. stationary를 single-layer 모드와 동일시하지 않는다.

## 2026-09-09 전수 감사와 canonical 반영

P0 v3 분모는 456파일이다. 281파일은 독립 2회 판독, 22파일은 문서·도해 단독 판독, 153파일은 바이너리 메타데이터 조사로 처리했다. 456파일 전부의 의미 판독을 뜻하지 않는다. [완료 원장](../../_staging/total-read/model-audit/XBeach/closure/README.md)은 승인된 보충 103건, 이월 충돌 3건·인용 미검증 10건, 문서 207건, 구성요소 귀속의 최종 대응을 기록한다.

- [소스 보충 60건](source-analysis/xbeach-source-audit-supplements.md): 입력·경계·형태·interface·출력의 적용 한계.
- [빌드·배포 보충 43건](source-analysis/xbeach-build-and-vendor-audit.md): 외부 netCDF·MPICH·Texinfo 등의 범위를 구분한다.
- [충돌·반증 재판정](source-analysis/xbeach-audit-resolved-claims.md): 기각 근거와 조건부 경고를 함께 보존한다.
- [문서 모순과 버전 차이](manual-notes/xbeach-document-discrepancies-and-version-drift.md): 2015 Kingsday·master와 2010 비정수압 초안을 별개 출처로 다룬다.
- [Kingsday 기술 문서](manual-notes/xbeach-kingsday-technical-reference.md), [master 매뉴얼](manual-notes/xbeach-master-manual.md), [2010 비정수압 보고서](manual-notes/xbeach-nonhydrostatic-report-2010.md).
- [경계 적용 한계 도해](source-analysis/xbeach-boundary-limit-figures.md), [공식 예제 공급원](source-analysis/xbeach-first-baseline-case-selection.md).

구성요소 귀속은 저작권 판정이 아니다. vendor·생성 파일의 기록 수를 XBeach 솔버의 고유 결함 수로 합산하지 않는다. [파일·처분 귀속 원장](../../_staging/total-read/model-audit/XBeach/closure/attribution.json).

## 2026-09-12 연결 분석 보충

- [지형·지하수·Q3D 연결 계약](source-analysis/xbeach-coupled-physics-contracts.md): **검토본(draft-unsourced), 새 주장 사람 검토 대기**. 입경 배열 덮어쓰기, 침투량 단위, 수심 갱신 시점, Q3D 실행 조건과 선박·식생·강우·조도의 생산/소비 시점을 추적했다.
- [초기화·hotstart·BMI·종료 상태 계약](source-analysis/xbeach-lifecycle-state-contracts.md): **검토본(draft-unsourced), 새 주장 사람 검토 대기**. 기존 12개 계약과 네 진입점 계열을 연결하고 오류 종료·getter 상태 설명을 정정했다.
- [빌드 대상·소스 생성·모드 연결](source-analysis/xbeach-build-mode-connectivity.md): **검토본(draft-unsourced)**. 별도 BMI 프로젝트, 생성 include, 비연결 소스와 여섯 dispatcher 경로를 정리했다.
- [매뉴얼 수식–구현 대응](manual-notes/xbeach-manual-equation-code-contracts.md): **검토본(draft-unsourced)**. (2.5)~(2.10)의 파수 보정, B.37/C.37의 지형 갱신, 불포화 침투식의 판본 표기·시간 이산화를 대조했다.
- [Q3D](source-analysis/xbeach_q3d.md)의 Van Rijn 1993 제외 조건과 설정표를 원문에 맞췄다.
- [비정수압 보고서](manual-notes/xbeach-nonhydrostatic-report-2010.md)에 원본 PDF와 DOC 수식 객체로 대조한 기호 4곳을 보충했다.

이는 2026-09-09 감사 완료 이력과 별도인 연결 분석 보충이다. 전체 모델 연결 검토·사람 승인 완료를 뜻하지 않는다.

## 노트 현황

| 경로 | 노트 수 |
|---|---:|
| source-analysis | 40 |
| manual-notes | 8 |
| web-refs | 1 |

2026-07-12의 코어 118파일 감사는 역사적 단계이며 이번 P0 v3 분모와 구별한다. 이번 완료는 감사·지식 반영 범위이며 원본 솔버의 결함을 패치했다는 뜻은 아니다.
