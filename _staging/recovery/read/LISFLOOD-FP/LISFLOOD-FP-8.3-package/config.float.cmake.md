---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP-8.3-package/config.float.cmake
lines: 8
sha256: b7a08b9bd53a73452dbfe32e4af640dd902c688ac073781262190ddb2bfc41a5
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# config.float.cmake — 판독 구간 기록

구간은 1행부터 8행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–1 | CMake 설정문은 `set(_NETCDF 1)` (1)이다. 이 파일은 `_NETCDF`를 `1`로 설정한다. |
| 2–8 | 전처리 매크로(preprocessor macro)를 지정하는 명령은 `add_compile_definitions(_NUMERIC_MODE=0)` (2), `add_compile_definitions(_ONLY_RECT=1)` (3), `add_compile_definitions(_PROFILE_MODE=0)` (4), `add_compile_definitions(_DISABLE_WET_DRY=0)` (5), `add_compile_definitions(_CALCULATE_Q_MODE=1)` (6), `add_compile_definitions(_SGM_BY_BLOCKS=0)` (7), `add_compile_definitions(_BALANCE_TYPE=0)` (8)이다. 이 구간에는 조건 분기나 주석이 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
