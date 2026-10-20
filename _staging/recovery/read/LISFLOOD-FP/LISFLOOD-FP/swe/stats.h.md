---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/swe/stats.h
lines: 42
sha256: 99a5a933e8334fcbc48e4fabd98213d5d1410d7dec39a175eab7c802e8471515
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# stats.h — 판독 구간 기록

구간은 1행부터 42행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–26 | `#pragma once`(1)와 lisflood 헤더 포함(2) 뒤 질량 수지(mass balance) 갱신(4–11), 침수 면적 산정(13–17), 유량 통계 초기화(19), 점원(point source) 유량 누적(21–25)을 선언한다. 조건부 전처리 분기·계산식·기본 인수값·실행문은 없다. 원문: `#pragma once` (1); `#include "../lisflood.h"` (2). |
| 27–42 | 경계 플럭스 누적(27–33), 성분 속도 갱신(35–40), 최대 수심장 갱신(42)의 원형을 선언한다. 경계형은 Pars·Solver·BoundCs·Arrays를 받고 최대 수심형은 Pars·Arrays만 받는다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
