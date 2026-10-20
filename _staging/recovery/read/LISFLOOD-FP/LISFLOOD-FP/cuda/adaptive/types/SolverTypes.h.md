---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/types/SolverTypes.h
lines: 7
sha256: 448b91a4c3e08c66218b772817429faed9ee4f06aced93cad8971318863f11da
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# SolverTypes.h — 판독 구간 기록

구간은 1행부터 7행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–2 | `#pragma once` (1)와 빈 줄(2)이다. 전처리 조건 분기는 없다. |
| 3–7 | 해법 종류 열거형(solver type enumeration) `SolverTypes`를 선언한다(3–4). 상수는 `HWFV1 = 1,` (5), `MWDG2 = 2` (6)이다. 열거형을 닫는다(7). 기본값 지정과 해법 실행 루틴은 이 선언에 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
