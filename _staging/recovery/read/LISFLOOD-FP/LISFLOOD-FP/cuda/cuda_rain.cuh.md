---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/cuda_rain.cuh
lines: 54
sha256: 2e0e6c19f5252935e9ba75c78d8d51c126d300e1802efcee055161456016f227
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_rain.cuh — 판독 구간 기록

구간은 1행부터 54행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | `#pragma once` (1), rain·cuda_solver 헤더(3–4), lis::cuda 이름 공간(namespace)(6–9), 빈 줄. 별도 전처리 조건 분기는 없다. |
| 11–26 | `__device__` (11)의 rate_at_cell(12–17), `__device__` (19)의 rate_at_cell_ACC(20–25) 원형. 두 함수는 NUMERIC_TYPE* rain_data와 int i·j를 받아 NUMERIC_TYPE을 반환한다. |
| 27–39 | 시작 시 6–9행 lis::cuda 이름 공간 안. DynamicRain 이름 공간(27–28)의 `__global__` (29), `__launch_bounds__(CUDA_BLOCK_SIZE)` (30), void update(31–37) 원형. NUMERIC_TYPE* DEM·H·rain_data를 받는다. 이름 공간 종료(38), 빈 줄(39). |
| 40–54 | 시작 시 6–9행 lis::cuda 이름 공간 안. DynamicRain 이름 공간을 다시 연다(40–41). `__global__` (42), `__launch_bounds__(CUDA_BLOCK_SIZE)` (43), void updateACC(44–50) 원형은 같은 포인터 세 개를 받는다. 이름 공간 모두 종료(51–54). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
