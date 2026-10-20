---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/dg2/cuda_dg2_dem.cuh
lines: 115
sha256: dc9e5ba1d6efc2fd2c945ea2b780017311a7aa1025348bc21ba10fa87d5c7835
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_dg2_dem.cuh — 판독 구간 기록

구간은 1행부터 115행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–30 | `#pragma once` (1), `#include "cuda_dem.cuh"` (2), lis::cuda::dg2 이름공간(namespace)(4–9)이다. 전처리 조건 분기는 없다. Topography 생성자는 파일명·기하·pitch/offset 참조·nodata_elevation·acceleration·verbose를 받는다(14–23). 소멸자를 선언한다(25). 지형고(digital elevation model, DEM) 계수 포인터는 `NUMERIC_TYPE* __restrict__ _0;` (27), `NUMERIC_TYPE* __restrict__ _1x;` (28), `NUMERIC_TYPE* __restrict__ _1y;` (29)이다. |
| 31–54 | 시작 시 11행 Topography 클래스 안이다. private load_slope는 파일명·접미사·기하·pitch·offset·verbose를 받는다(32–40). zero_perimeter_slopes·clamp_boundary_values는 기하·pitch를 받는다(42–52). 클래스 끝과 빈 줄이다(53–54). |
| 55–101 | DeviceTopography는 호스트(host) Topography·Geometry를 받는 initialise(58–62)와 인수 없는 initialise_Zstar(64–67)를 선언한다. `__device__` (69·75·81·87·93) 지정은 neg_x·pos_x·neg_y·pos_y·Zdagger에 각각 붙는다. 앞 네 함수는 idx를, Zdagger는 ETA·Zstar를 받는다(70–98). free_device를 선언한다(100). |
| 102–115 | 시작 시 55행 DeviceTopography 클래스 안이다. `NUMERIC_TYPE* __restrict__ _0;` (102), `NUMERIC_TYPE* __restrict__ _1x;` (103), `NUMERIC_TYPE* __restrict__ _1y;` (104), `NUMERIC_TYPE* __restrict__ Zstar_x;` (105), `NUMERIC_TYPE* __restrict__ Zstar_y;` (106)를 공개한다. private에는 initialise_Zstar_x/y가 있다(108–110). 클래스·세 이름공간을 닫는다(111–115). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
