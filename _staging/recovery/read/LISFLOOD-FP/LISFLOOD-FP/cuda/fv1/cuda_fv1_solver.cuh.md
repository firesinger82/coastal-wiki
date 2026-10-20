---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/fv1/cuda_fv1_solver.cuh
lines: 72
sha256: f0629ce960904990b7fac510e16f4e34c48a34bf4ac3eab6e50715857ce432ec
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_fv1_solver.cuh — 판독 구간 기록

구간은 1행부터 72행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | `#pragma once` (1)과 LISFLOOD·매개변수·통계·FV1 Flow·CUDA Sample·CUDA Solver 헤더 포함(2–7). lis::cuda::fv1 이름 공간(namespace) 안에 `class Solver : public cuda::Solver<Flow>` (16)를 선언한다. 조건부 전처리 지시는 없다. |
| 19–55 | 시작 시 9·11·13행 이름 공간·16행 Solver 클래스의 public 구역 안. 생성자는 Flow 참조, DEM·Zstar_x·Zstar_y·manning 포인터, Geometry·PhysicalParams 참조와 dim3 grid_size를 받는다(19–29). 범람원(floodplain) 유량 계산 `FloodplainQ`, `zero_thin_depth_slopes`, 고스트 셀(ghost cell) 초기화·갱신, 균일 강우 갱신, `updateMaxFieldACC(NUMERIC_TYPE t)`, 질량 통계를 받는 `update_flow_variables`, `d_U`, const `update_dt_per_element`, 소멸자를 선언한다(31–54). 기본 인수는 없다. |
| 56–72 | 시작 시 9·11·13행 이름 공간·16행 클래스 안. private 필드 U1·U2·Ux, Uold·U 참조, DEM·Zstar_x·Zstar_y·manning 포인터, bool friction, const dim3 grid_size를 선언한다(56–67). 클래스와 이름 공간을 닫는다(68–72). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 31–40: FloodplainQ·zero_thin_depth_slopes·updateMaxFieldACC의 선언이 있다. 이 헤더에는 구현이 없다.
