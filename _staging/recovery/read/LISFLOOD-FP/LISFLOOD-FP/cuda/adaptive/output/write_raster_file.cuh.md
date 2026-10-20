---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/output/write_raster_file.cuh
lines: 23
sha256: 001809f931c91a9ae0cc64e86ff915ca32e7ed82a9df4d28f17c25470789c699
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# write_raster_file.cuh — 판독 구간 기록

구간은 1행부터 23행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | `#pragma once` (1)로 중복 포함을 막는다. `<cstdio>`·`<cstring>` (3–4), `BLOCK_VAR_MACROS.cuh`·`cuda_utils.cuh` (6–7), `SimulationParams.h`·`PlottingParams.h`·`SaveInterval.h` (9–11)를 포함한다. 빈 줄도 포함된다. 조건부 전처리 분기는 없다. |
| 13–23 | CUDA 호스트(host) 지시 `__host__` (13)와 `void write_raster_file` 원형을 선언한다(14–23). 출력 설정, 확장자, 래스터(raster) 실수 포인터, 모의 설정, `const SaveInterval massint`, 최세 격자 간격, 격자 차원을 받는다(16–22). 기본 인수 값이나 실행 본문은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
