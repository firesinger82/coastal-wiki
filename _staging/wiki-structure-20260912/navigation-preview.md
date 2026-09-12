# 개편 후 탐색 화면 예시

**계획 검토용이며 미구현이다.** 아래는 기존 파일로 가는 탐색 링크다. 이 파일을 기술 주장의 근거로 인용하거나 링크 대상의 검증·승인을 승계하지 않는다. 실제 반영 시 각 파일의 최신 frontmatter와 disclosed-gap를 확인한다.

## waves에서 시작할 때

| 읽으려는 내용 | 이동할 기존 문서 |
|---|---|
| 개념과 용어 | [파랑 개념](../../concepts/waves/01-concept.md) |
| 이론을 자세히 읽기 | [선형파](../../textbook/notes/theory-ch08-linear-waves.md), [비선형·스펙트럼](../../textbook/notes/theory-ch09-nonlinear-spectra.md), [연안 변형](../../textbook/notes/theory-ch10-coastal-transformation.md), [스펙트럼 파랑 모델링](../../textbook/notes/theory-ch11-spectral-wave-modeling.md) |
| 분석법과 도구 | [분석법](../../concepts/waves/03-analysis-methods.md), [코드·도구](../../concepts/waves/04-code-and-tools.md) |
| 모델 사이의 처리 차이 | [쇄파 비교](../../concepts/waves/wave-breaking-cross-model.md), [저면마찰 비교](../../concepts/currents/bottom-friction-cross-model.md), [시간 적분 비교](../../concepts/currents/time-integration-cross-model.md) |
| 모델 구현으로 이동 | [SWAN](../../models/SWAN/README.md), [XBeach](../../models/XBeach/README.md), [현재 모델 적용 안내](../../concepts/waves/06-model-application.md) |
| 기준·실습 자료로 이동 | [KDS 자료 안내](../../standards/README.md), [SWAN–SWASH 연계 실습](../../examples/swan-to-swash-nesting/README.md) |

KDS는 변환 원자료, 실습은 절차 자료다. 이 링크 추가로 verified 문서나 검색 대상이 된다는 뜻은 아니다.

## XBeach에서 시작할 때

| 읽으려는 내용 | 이동할 기존 문서 |
|---|---|
| 공식 자료·판본 | [공식 자료](../../models/XBeach/web-refs/xbeach-official-resources.md), [문서 스택](../../models/XBeach/manual-notes/01-local-manual-stack.md) |
| 모드 선택과 분기 | [모드 dispatcher](../../models/XBeach/source-analysis/xbeach_mode_dispatch.md) |
| 파랑 계산 | [파랑 작용량](../../models/XBeach/source-analysis/xbeach_wave_action_balance.md), [쇄파](../../models/XBeach/source-analysis/xbeach_wave_breaking.md) |
| 흐름과 경계 | [흐름 솔버](../../models/XBeach/source-analysis/xbeach_flow_solver.md), [흐름 경계](../../models/XBeach/source-analysis/xbeach_flow_boundary_conditions.md) |
| 지형 변화 | [형태 변화](../../models/XBeach/source-analysis/xbeach_morphology.md) |
| 상태 전달·구현 제약 | [초기화·BMI·종료 계약](../../models/XBeach/source-analysis/xbeach-lifecycle-state-contracts.md), [물리 연결 계약](../../models/XBeach/source-analysis/xbeach-coupled-physics-contracts.md) — 현재 draft-unsourced, 새 주장 사람 검토 대기 |
| 개념·이론으로 돌아가기 | [파랑](../../concepts/waves/README.md), [조석](../../concepts/tides/README.md), [표사](../../concepts/sediment-transport/README.md), [처오름대](../../concepts/swash-zone/README.md) |

하단의 별도 문서 상태·분석 이력 영역에는 기존 감사·미완 기록을 유지한다. 위 링크 안내가 XBeach 전체 판독·연결 감사 완료를 뜻하지 않음을 표시한다. 개별 링크 대상이 draft이면 그 사실을 독자가 볼 수 있게 한다.
