---
title: "FUNWAVE 노트 대조 반영 기록 — 작업 6"
citation_status: verified
last_source_check: "2026-10-18 (recovery 대조 반영)"
verification_method: "2026-10-18 FUNWAVE recovery 대조 보고서 반영"
---

# FUNWAVE 노트 대조 반영 기록 — 작업 6

배정표는 [FUNWAVE-note-job-6.tsv](../assign/FUNWAVE-note-job-6.tsv)이다.
대상 노트는 [funwave-flux-tvd.md](../../../models/FUNWAVE/source-analysis/funwave-flux-tvd.md)이다.
배정표의 행 수는 120개이다.

진행 상태: 완료.

대상 노트의 차이 표는 배정표의 120개 행을 포함한다.

| 구분 | 파일:줄 | 반영 내용 |
|---|---|---|
| 수정 | `models/FUNWAVE/source-analysis/funwave-flux-tvd.md:5–6` | verification_method에 대조 반영 구절을 추가했다. last_source_check를 갱신했다. citation_status는 유지했다. |
| 수정 | `models/FUNWAVE/source-analysis/funwave-flux-tvd.md:20` | WEN의 CARTESIAN 조건을 반영했다. |
| 수정 | `models/FUNWAVE/source-analysis/funwave-flux-tvd.md:23` | 산술평균 플럭스의 실제 선택 조건을 반영했다. |
| 수정 | `models/FUNWAVE/source-analysis/funwave-flux-tvd.md:32` | FMI의 활성 분기를 반영했다. 활성화 커밋과 날짜를 적었다. 불안정성 경고 주석을 구분했다. |
| 수정 | `models/FUNWAVE/source-analysis/funwave-flux-tvd.md:35` | 기존 표의 수식에서 세로줄을 이스케이프했다. |
| 수정 | `models/FUNWAVE/source-analysis/funwave-flux-tvd.md:38` | 분산 플럭스 축약식의 마스크 조건을 반영했다. |
| 수정 | `models/FUNWAVE/source-analysis/funwave-flux-tvd.md:46` | High 1계 미분의 오차 차수를 정정했다. CAL_DISPERSION의 호출 여부를 반영했다. |
| 추가 | `models/FUNWAVE/source-analysis/funwave-flux-tvd.md:65–197` | 문서와 코드 차이 절을 추가했다. 문서 판과 코드 판을 적었다. 배정 행의 원문과 최종 결론을 넣었다. |

행 수는 배정표와 노트 표의 행 ID에서 셌다.

| 보고서 약칭 | 배정표 행 수 | 넣은 행 수 | 노트 표의 파일:줄 |
|---|---|---|---|
| theory-numerics | 17 | 17 | `models/FUNWAVE/source-analysis/funwave-flux-tvd.md:78–94` |
| inputs | 2 | 2 | `models/FUNWAVE/source-analysis/funwave-flux-tvd.md:95–96` |
| examples | 1 | 1 | `models/FUNWAVE/source-analysis/funwave-flux-tvd.md:97` |
| v21-manual | 31 | 31 | `models/FUNWAVE/source-analysis/funwave-flux-tvd.md:98–128` |
| v21-examples | 3 | 3 | `models/FUNWAVE/source-analysis/funwave-flux-tvd.md:129–131` |
| aux-docs-build | 10 | 10 | `models/FUNWAVE/source-analysis/funwave-flux-tvd.md:132–141` |
| gpu-vs-tvd | 51 | 51 | `models/FUNWAVE/source-analysis/funwave-flux-tvd.md:142–192` |
| callflow | 5 | 5 | `models/FUNWAVE/source-analysis/funwave-flux-tvd.md:193–197` |
| 합계 | 120 | 120 | `models/FUNWAVE/source-analysis/funwave-flux-tvd.md:78–197` |

노트 표의 결론 열에서 센 분류는 A 9개, B 27개, C 20개, D 5개, E 1개, F 58개이다.

담당 노트의 수정안을 지정한 행 ID는 다음과 같다.

| 수정안 행 ID | 반영 위치(파일:줄) | 반영 내용 |
|---|---|---|
| theory-numerics:FT1-276 | `models/FUNWAVE/source-analysis/funwave-flux-tvd.md:23` | 산술평균 플럭스 경로의 선택 조건을 정정했다. |
| theory-numerics:FT1-277 | `models/FUNWAVE/source-analysis/funwave-flux-tvd.md:32` | FMI의 활성화 이력을 반영했다. |
| theory-numerics:FT1-278 | `models/FUNWAVE/source-analysis/funwave-flux-tvd.md:46` | DERIVATIVE_X_High의 2차 오차를 반영했다. |
| v21-manual:FV1-556 | `models/FUNWAVE/source-analysis/funwave-flux-tvd.md:20` | WEN의 CARTESIAN 조건을 반영했다. |
| v21-manual:FV1-558 | `models/FUNWAVE/source-analysis/funwave-flux-tvd.md:32` | 현재 FMI가 비활성이라는 설명을 정정했다. |
| v21-manual:FV1-559 | `models/FUNWAVE/source-analysis/funwave-flux-tvd.md:38` | MASK9u·MASK9v의 면 보정 조건을 반영했다. |
| v21-manual:FV1-560 | `models/FUNWAVE/source-analysis/funwave-flux-tvd.md:46` | 4차 1계라는 표기를 정정했다. High 루틴의 호출 설명을 반영했다. |
| aux-docs-build:FN1-918 | `models/FUNWAVE/source-analysis/funwave-flux-tvd.md:32` | FMI의 활성 호출과 경고 주석을 구분했다. |

v21-manual:FV1-557의 유지 지시는 `models/FUNWAVE/source-analysis/funwave-flux-tvd.md:30`에 반영했다.
해당 CONSTRUCTION의 piecewise-linear 설명은 기존 문장과 같다.

넣지 않은 배정 행은 없다.
반영하지 않은 담당 노트 수정안은 없다.
배정 행 ID의 누락과 중복은 없다.
표의 각 행은 6열이다.
표의 120개 결론 문장을 보고서의 최종 결론 문장과 대조했다.
A 행은 결론 문장에 커밋 HASH와 날짜를 포함한다.
E 행은 약함 강도를 포함한다.
코드 원문 칸의 인용 조각을 해당 보고서의 원문과 대조했다.
대상 노트와 이 기록의 링크는 상대 경로이다.
