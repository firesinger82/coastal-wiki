---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/swe/boundary.h
lines: 36
sha256: 292f5073b1c39b668032ca645cf89f2648979c0daccc100e6cf43b0427e51283
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# boundary.h — 판독 구간 기록

구간은 1행부터 36행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | `#pragma once` (1)로 중복 포함을 막고 lisflood.h를 포함한다(2). linear_interpolate는 TimeSeries 포인터와 NUMERIC_TYPE 시각을 받아 NUMERIC_TYPE을 반환하는 원형(prototype)이다(4–8). 조건·계산식·함수 본문은 없다. |
| 10–36 | boundary_index_w·boundary_index_e·boundary_index_n·boundary_index_s는 모두 Pars 포인터와 const int i·j를 받아 int를 반환한다(10–36). 별도의 전처리 조건이나 기본 인수는 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
