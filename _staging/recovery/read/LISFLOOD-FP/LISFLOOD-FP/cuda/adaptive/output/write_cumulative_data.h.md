---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/output/write_cumulative_data.h
lines: 24
sha256: a4cfd706c17c21ffa065bf8904a24fb33ba69c768aee35aa9ca288ee012b0259
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# write_cumulative_data.h — 판독 구간 기록

구간은 1행부터 24행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | `#pragma once` (1)로 중복 포함을 막는다. `BLOCK_VAR_MACROS.cuh` (3), 표준 입출력·종료·문자열·시계 헤더(5–8), `SimulationParams.h`·`PlottingParams.h` (10–11)를 포함한다. 빈 줄도 포함된다. 조건부 전처리 분기는 없다. |
| 13–24 | `void write_cumulative_data` 원형을 선언한다(13–24). `start`는 `const clock_t` 값 인수다(15). 현재 시간, 두 실행 시간, 시간 간격, 셀 수, 모의 설정, 출력 설정은 상수 참조다(16–22). `first_t_step`은 `const bool` 값 인수다(23). 기본 인수 값이나 실행 본문은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
