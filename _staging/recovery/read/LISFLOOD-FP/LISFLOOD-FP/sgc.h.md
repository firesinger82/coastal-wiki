---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/sgc.h
lines: 28
sha256: ba6f0f56ba310e4685dbf1fe2023f3f7a872953d10bb38bc45d3a294a3ce6359
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# sgc.h — 판독 구간 기록

구간은 1행부터 28행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | `#pragma once` (1)로 중복 포함을 막고 lisflood.h를 포함한다(3). CalcSGC_UpV·CalcSGC_A·CalcSGC_R·SGC_hotstart·CalcSGCz의 원형(prototype)은 전처리 조건 밖에 있다(5–9). 반환형·포인터 인수와 CalcSGCz의 const int verbose를 선언하며 함수 본문은 없다. |
| 11–28 | `#ifdef RESULT_CHECK` (11)이므로 RESULT_CHECK가 정의된 경우에만 이 구간 원형이 보인다. 하위 격자 수로(subgrid channel)와 범람원(floodplain)의 유량 함수 SGC_FloodplainQ·CalcFPQxSGC·CalcFPQySGC, 수심 갱신 SGC_UpdateH와 경계 SGC_BCs를 선언한다(13–18). 증발·강우·라우팅(routing)·체적에서 수심 계산·계수 준비·점 자유경계 원형은 20–26행이다. `#endif` (28)로 조건을 닫는다. RESULT_CHECK가 정의되지 않으면 13–26행 선언은 제외된다. 이 파일은 RESULT_CHECK 값을 정의하지 않는다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 5–9·11–28: 다섯 원형은 RESULT_CHECK 조건 밖에 있고 SGC_wp_prams를 포함한 나머지 원형은 그 조건 안에 있다.
