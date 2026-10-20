---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/Directions.h
lines: 14
sha256: 17a893f8803ace2daa0e9d781728d1bc8faf45a9ab473aca8ef87041be2aef31
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# Directions.h — 판독 구간 기록

구간은 1행부터 14행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | `#pragma once` (1), 빈 줄(2), 열거형(enum) `enum Directions` (3–4). 방향 비트 값은 `NORTH = 1, // 0001` (5), `EAST  = 2, // 0010` (6), `SOUTH = 4, // 0100` (7), `WEST  = 8  // 1000` (8). 9행은 빈 줄. 이 파일의 모든 구간에는 `#if` 계열 전처리 조건 분기가 없다. |
| 10–14 | 시작 시 3행 Directions 열거형 안. 모서리의 비트 논리합(bitwise OR)은 주석 `// NORTH \| EAST = 3` (10), `// NORTH \| WEST = 9` (11), `// SOUTH \| EAST = 6` (12), `// SOUTH \| WEST = 12` (13)으로만 제시한다. 열거형 종료(14). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
