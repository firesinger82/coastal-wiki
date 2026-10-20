---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/swe/input.h
lines: 13
sha256: db1526a6e28540198316d4b10beef0c084d8b44b297f1cece467a646b359b80e
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# input.h — 판독 구간 기록

구간은 1행부터 13행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | `#pragma once`(1)와 lisflood 헤더 포함(3) 뒤 ASCII 격자(ASCII raster) 판독 함수 `read_ascfile`(5–12)를 선언한다. const char* 파일명·메시지, Pars 포인터, NUMERIC_TYPE 필드 포인터, const int verbose를 받는다. 기본 인수값·조건부 전처리 분기·실행문은 없다. 마지막 빈 줄도 포함한다. 원문: `#pragma once` (1); `#include "../lisflood.h"` (3). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
