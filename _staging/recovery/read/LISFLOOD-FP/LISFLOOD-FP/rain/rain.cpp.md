---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/rain/rain.cpp
lines: 9
sha256: a8161b4eefadcff614b9b5c399a98fd380a45af2eaa09bb83a50d492178da37d
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# rain.cpp — 판독 구간 기록

구간은 1행부터 9행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | rain.h를 포함한다(1). `#if _NETCDF == 1` (3)이면 `#include "rain.tpp"` (4)를 포함한다. 해당 조건 불성립 `#else` (5)에서는 `#include "rain_stub.tpp"` (6)을 포함한다. `#endif` (7)로 조건을 닫고 `template class DynamicRain<>;` (9)로 기본 할당자(allocator)의 DynamicRain을 명시적으로 인스턴스화한다(explicit instantiation). _NETCDF의 값 정의는 이 파일에 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
