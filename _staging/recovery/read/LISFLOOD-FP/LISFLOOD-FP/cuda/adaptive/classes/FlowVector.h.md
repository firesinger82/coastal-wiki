---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/classes/FlowVector.h
lines: 124
sha256: 7353bb60c26b74db21410fb9f2de4ebb1a7811a9b8b4a2916ee70776ec26ddc8
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# FlowVector.h — 판독 구간 기록

구간은 1행부터 124행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | `#pragma once` (1), cuda_runtime.h·real.h 포함(3–5). 전처리 조건 분기는 없다. FlowVector는 real h·qx·qy를 보유한다(7–11). `__device__ __forceinline__` (13)의 get_speed는 q·tol_h를 받아(14–19) 삼항식 `return (h < tol_h) ? 0 : q / h;` (20)을 반환한다. |
| 23–49 | 시작 시 7–8행 FlowVector 구조체 안. `__device__ __forceinline__` (23)의 calc_h_star는 z·z_intermediate를 받는다(24–29). 수위 식 `real eta = h + z;` (30), 비음수 깊이 반환식 `return max(C(0.0), eta - z_intermediate);` (32). `__device__ __forceinline__` (35)의 get_star는 z·z_intermediate·tol_h를 받는다(36–42). calc_h_star와 get_speed를 이용한 세 계산식 `real h_star  = calc_h_star(z, z_intermediate);`<br>`real qx_star = h_star * get_speed(qx, tol_h);`<br>`real qy_star = h_star * get_speed(qy, tol_h);` (43–45) 뒤 h_star·qx_star·qy_star를 반환한다(47). |
| 50–66 | 시작 시 7–8행 FlowVector 구조체 안. `__device__ __forceinline__` (50)의 phys_flux_x는 tol_h·g를 받는다(51–56). `if (h < tol_h)` (57)이면 영 벡터를 반환한다(59). `else` (61)의 x방향 물리 플럭스(physical flux) 반환식은 `return { qx, qx * qx / h + g * h * h / C(2.0), qx * qy / h };` (63). |
| 67–85 | 시작 시 7–8행 FlowVector 구조체 안. `__device__ __forceinline__` (67)의 phys_flux_y는 tol_h·g를 받는다(68–73). `if (h < tol_h)` (74)이면 영 벡터를 반환한다(76). `else` (78)의 y방향 물리 플럭스 반환식은 `return { qy, qx * qy / h, qy * qy / h + g * h * h / C(2.0) };` (80). 메서드·구조체 종료(82–84). |
| 86–105 | 구조체 밖 연산자. `__host__ __device__` (86)의 operator+는 두 FlowVector를 받아(87–92) 성분별 합 `return { lhs.h + rhs.h, lhs.qx + rhs.qx, lhs.qy + rhs.qy };` (93)을 반환한다. `__host__ __device__` (96)의 operator-는 성분별 차 `return { lhs.h - rhs.h, lhs.qx - rhs.qx, lhs.qy - rhs.qy };` (103)를 반환한다(97–104). |
| 106–124 | `__host__ __device__` (106)의 operator*는 real lhs와 FlowVector rhs를 받아(107–112) 성분별 곱 `return { lhs * rhs.h, lhs * rhs.qx, lhs * rhs.qy };` (113)을 반환한다. `__host__ __device__` (116)의 operator/는 FlowVector lhs와 real rhs를 받아(117–122) 성분별 나눗셈 `return { lhs.h / rhs, lhs.qx / rhs, lhs.qy / rhs };` (123)을 반환한다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 117–123: operator/는 rhs로 세 성분을 나눈다. 연산자 본문에는 rhs가 0인지 확인하는 분기가 없다.
