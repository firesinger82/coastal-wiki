---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/cuda_flow.cu
lines: 64
sha256: 1fa04fc223006930286169d9afd7c8bf7f2ac87dd65adcbe153e965f3fb7c381
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_flow.cu — 판독 구간 기록

구간은 1행부터 64행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | flow·solver 헤더(1–2). `__device__ lis::cuda::FlowVector lis::cuda::FlowVector::star` (4)는 `NUMERIC_TYPE Hstar = calculate_Hstar(Z, Zstar);` (10), `return { Hstar, Hstar*speed(HU), Hstar*speed(HV) };` (12)로 지반고 재구성(reconstruction) 벡터를 반환한다. 이 파일에는 전처리 조건 분기가 없다. |
| 15–40 | `__device__` (15) physical_flux_x(16)의 `if (H <= cuda::solver_params.DepthThresh)` (18)는 FlowVector() 반환(20). `else` (22)는 `return { HU, HU*HU/H + C(0.5)*cuda::physical_params.g*H*H, HU*HV/H };` (24). `__device__` (28) physical_flux_y(29)의 `if (H <= cuda::solver_params.DepthThresh)` (31)는 FlowVector() 반환(33), `else` (35)는 `return { HV, HU*HV/H, HV*HV/H + C(0.5)*cuda::physical_params.g*H*H };` (37). |
| 41–64 | `__device__ NUMERIC_TYPE lis::cuda::FlowVector::calculate_Hstar` (41)는 `NUMERIC_TYPE ETA = H + Z;` (47), `return FMAX(C(0.0), ETA - Zstar);` (48). `__device__ NUMERIC_TYPE lis::cuda::FlowVector::speed` (51)는 `if (H >= cuda::solver_params.DepthThresh)` (56)에서 `return discharge/H;` (58), `else` (60)는 `return C(0.0);` (62). 함수 종료(64). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 18·31·56: 물리 플럭스(physical flux)는 H가 DepthThresh와 같으면 FlowVector()를 반환한다. speed는 같은 경계에서 discharge/H를 계산한다.
