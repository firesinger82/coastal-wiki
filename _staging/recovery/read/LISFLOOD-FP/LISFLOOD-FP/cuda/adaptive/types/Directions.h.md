---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/types/Directions.h
lines: 14
sha256: 17a893f8803ace2daa0e9d781728d1bc8faf45a9ab473aca8ef87041be2aef31
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# Directions.h — 판독 구간 기록

구간은 1행부터 14행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–2 | `#pragma once` (1)와 빈 줄(2)이다. 전처리 조건 분기는 없다. |
| 3–14 | 방향 열거형(enumeration) `Directions`를 선언한다(3–4). 상수는 `NORTH = 1, // 0001` (5), `EAST  = 2, // 0010` (6), `SOUTH = 4, // 0100` (7), `WEST  = 8  // 1000` (8)이다. 빈 줄(9) 뒤 주석은 비트 OR(bitwise OR)로 북·동=3, 북·서=9, 남·동=6, 남·서=12를 조합한다고 적는다(10–13). 열거형을 닫는다(14). 호출 루틴과 실행 조건은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
