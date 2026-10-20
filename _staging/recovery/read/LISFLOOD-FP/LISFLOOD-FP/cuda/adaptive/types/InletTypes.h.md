---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/types/InletTypes.h
lines: 11
sha256: 9b389c4739d8bcd7b37ae45fb4007207e2aa9a0868bb15aeab89abc8ef8c94d6
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# InletTypes.h — 판독 구간 기록

구간은 1행부터 11행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–2 | `#pragma once` (1)와 빈 줄(2)이다. 전처리 조건 분기는 없다. |
| 3–11 | 유입부 종류 열거형(inlet type enumeration) `InletTypes`를 선언한다(3–4). 상수는 `CLOSED = 1,` (5), `FREE   = 2,` (6), `HFIX   = 4,` (7), `HVAR   = 8,` (8), `QFIX   = 16,` (9), `QVAR   = 32` (10)이다. 열거형을 닫는다(11). 기본값 지정과 각 상수의 처리 루틴은 이 선언에 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
