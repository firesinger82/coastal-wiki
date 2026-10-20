---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/fv2/cuda_fv2_dem.cuh
lines: 67
sha256: e21319ce909bcc0249174d478a14fababa6f6e68a20df140b2288b912b21c132
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_fv2_dem.cuh — 판독 구간 기록

구간은 1행부터 67행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | `#pragma once` (1), cuda_dem.cuh 포함(2), lis::cuda::fv2 이름 공간(namespace)(4–9), Topography 클래스와 public 구역(11–13). 조건부 전처리 지시는 없다. |
| 14–37 | 시작 시 4·6·8행 이름 공간·11행 Topography 클래스 안. 생성자는 파일명·Geometry 참조·pitch/offset 참조·nodata_elevation·acceleration·verbose를 받는다(14–23). 소멸자(25)와 `NUMERIC_TYPE* __restrict__ _0;` (27)를 공개한다. private의 clamp_boundary_values는 Geometry와 pitch를 받는다(29–35). 클래스 종료와 빈 줄(36–37). |
| 38–67 | 4·6·8행 이름 공간 안에서 DeviceTopography를 선언한다(38–63). initialise는 Topography·Geometry 참조를 받는다(41–45). 장치 함수(device function)는 `__device__` (47) `NUMERIC_TYPE Zdagger` (48)이며 ETA와 Zstar를 받는다(49–52). free_device와 `NUMERIC_TYPE* __restrict__ _0;` (56), `NUMERIC_TYPE* __restrict__ Zstar_x;` (57), `NUMERIC_TYPE* __restrict__ Zstar_y;` (58)를 공개한다. 두 Zstar 초기화 함수는 private이다(60–62). 이름 공간을 닫는다(65–67). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
