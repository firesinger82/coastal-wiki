---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/geometry.h
lines: 13
sha256: 5d62e5f2873c22858e524736cd5b8b593ce5d99d3609817fe4bbd756c70b7855
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# geometry.h — 판독 구간 기록

구간은 1행부터 13행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | 조건부 전처리 분기 없이 `#pragma once`로 헤더 중복 포함을 막고 `lisflood.h`를 포함한다(1–2). `typedef struct Geometry`는 xsz·ysz 정수와 NUMERIC_TYPE의 blx·bly·tly·dx·dy를 선언한다(4–13). 이 구조체 선언에는 기본값 대입이 없다. 원문: `#pragma once` (1); `#include "lisflood.h"` (2). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
