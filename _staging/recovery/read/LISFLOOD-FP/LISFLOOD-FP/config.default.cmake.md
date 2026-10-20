---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/config.default.cmake
lines: 8
sha256: 62ea38671e809ea980f435d3ee929c8aab981aa3f88dee9186ffcde9784eb00a
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# config.default.cmake — 판독 구간 기록

구간은 1행부터 8행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–8 | 기본 설정은 `set(_NETCDF 1)` (1)이다. 컴파일 전처리 정의(preprocessor definitions)는 `add_compile_definitions(_NUMERIC_MODE=1)` (2), `add_compile_definitions(_ONLY_RECT=1)` (3), `add_compile_definitions(_PROFILE_MODE=0)` (4), `add_compile_definitions(_DISABLE_WET_DRY=0)` (5), `add_compile_definitions(_CALCULATE_Q_MODE=1)` (6), `add_compile_definitions(_SGM_BY_BLOCKS=0)` (7), `add_compile_definitions(_BALANCE_TYPE=0)` (8)이다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
