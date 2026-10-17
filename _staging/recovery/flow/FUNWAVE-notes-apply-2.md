---
title: "FUNWAVE 대조 결론 노트 반영 기록 — job 2"
citation_status: verified
last_source_check: "2026-10-18 (recovery 대조 반영)"
verification_method: "2026-10-18 FUNWAVE recovery 대조 보고서 반영"
---

# FUNWAVE 대조 결론 노트 반영 기록 — job 2

배정 근거는 [FUNWAVE-note-job-2.tsv](../assign/FUNWAVE-note-job-2.tsv)이다.
배정표의 행 수는 227개이다.
대상 노트는 [funwave-infrastructure.md](../../../models/FUNWAVE/source-analysis/funwave-infrastructure.md)이다.

상태: 반영 완료.

대상 노트의 추가·수정 범위는 다음과 같다.

| 파일:줄 | 반영 내용 | 수정안 행 ID |
|---|---|---|
| `models/FUNWAVE/source-analysis/funwave-infrastructure.md:5–6` | verification_method 구절 추가와 last_source_check 추가 | frontmatter |
| `models/FUNWAVE/source-analysis/funwave-infrastructure.md:17–18` | 벽 경계와 별도 경계 분기 | theory-numerics:FT1-282, v21-manual:FV1-564 |
| `models/FUNWAVE/source-analysis/funwave-infrastructure.md:25–29` | Kappa 대입과 재구성식의 사용 여부 | theory-numerics:FT1-284, v21-manual:FV1-565 |
| `models/FUNWAVE/source-analysis/funwave-infrastructure.md:39–40` | io.F 전체 길이와 READ_INPUT 길이 구분 | inputs:FI1-321 |
| `models/FUNWAVE/source-analysis/funwave-infrastructure.md:42–49` | 관측점 출력 열·건조점·버퍼·구면 좌표 조건 | examples:FX1-914, v21-examples:FV2-406 |
| `models/FUNWAVE/source-analysis/funwave-infrastructure.md:54–59` | INI_SOL 입력·LAGTIME 분기·alpha·중심 좌표 | examples:FX1-915, v21-examples:FV2-405 |
| `models/FUNWAVE/source-analysis/funwave-infrastructure.md:64–67` | 결합 첫 시각·보간 조건·제목행 읽기 후보 | examples:FX1-916, v21-examples:FV2-406 |
| `models/FUNWAVE/source-analysis/funwave-infrastructure.md:69–74` | CFL 분모·고정 시간 간격·최소값 집계 범위 | theory-numerics:FT1-283, inputs:FI1-322, v21-manual:FV1-566, aux-docs-build:FN1-919, callflow:RF-049 |
| `models/FUNWAVE/source-analysis/funwave-infrastructure.md:83–95` | OUTPUT 위치·RK 순서·경계·분산 교환의 직접 호출자 | inputs:FI1-318, v21-manual:FV1-569, callflow:RF-043 |
| `models/FUNWAVE/source-analysis/funwave-infrastructure.md:100–336` | 판본 설명과 문서·코드 차이 표 | 배정표의 227개 행 |

수정안의 서로 다른 반영 행 ID는 위 표에서 센 18개이다.
본문 정정 줄에는 `[10-18 대조 정정]`을 붙였다.
inputs:FI1-326과 v21-manual:FV1-567이 유지하도록 한 GLOBAL 문장은 대상 노트 78행에 그대로 있다.
v21-manual:FV1-568이 유지하도록 한 PARAM 문장은 대상 노트 79행에 그대로 있다.

표에 넣은 행 수는 다음과 같다.
집계 기준은 배정표의 보고서 약칭과 대상 노트 110–336행의 행 ID이다.

| 보고서 약칭 | 배정표 행 수 | 넣은 행 수 |
|---|---:|---:|
| theory-numerics | 17 | 17 |
| inputs | 42 | 42 |
| examples | 23 | 23 |
| v21-manual | 45 | 45 |
| v21-examples | 18 | 18 |
| aux-docs-build | 27 | 27 |
| gpu-vs-tvd | 46 | 46 |
| callflow | 9 | 9 |
| 합계 | 227 | 227 |

배정표와 표의 행 ID 집합은 같다.
배정표와 표의 결론 분류는 같다.
표의 중복 행은 없다.
보고서 최종 결론 문장과 표의 결론 문장은 인용 표기와 추가 메타데이터를 제외하면 같다.
A 34개 행의 결론 문장에는 보고서의 커밋 HASH와 날짜를 넣었다.
E 20개 행에는 보고서의 강도를 넣었다.
Markdown 표 파서는 본문 227개 행을 각각 6개 칸으로 읽었다.
상대 링크의 대상 파일은 모두 존재한다.
대상 노트와 이 기록의 last_source_check는 `2026-10-18 (recovery 대조 반영)`이다.
대상 노트의 citation_status는 기존 verified를 유지했다.

넣지 않은 배정 행: 없음.
넣지 않은 배정 행의 이유: 해당 없음.
