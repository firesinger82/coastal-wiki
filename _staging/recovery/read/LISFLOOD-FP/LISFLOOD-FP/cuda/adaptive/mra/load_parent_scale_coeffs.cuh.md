---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/mra/load_parent_scale_coeffs.cuh
lines: 52
sha256: 8cad47ec2adeec0db1f00328500c0452a78325095a2daa902661606e81a38737
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# load_parent_scale_coeffs.cuh — 판독 구간 기록

구간은 1행부터 52행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | `#pragma once` (1). CUDA 실행 환경, ScaleCoefficients.h, ParentScaleCoeffs.h를 포함한다(3–6). 빈 줄도 포함한다. 이 파일에는 전처리 조건 분기가 없다. |
| 8–23 | `__device__ __forceinline__` (8)인 장치 함수(device function) load_parent_scale_coeffs_hw는 ParentScaleCoeffsHW를 반환한다(9). ScaleCoefficients 참조와 int 참조 h_idx를 받는다(10–14). 반환 집합 초기화(aggregate initialization)는 d_scale_coeffs의 eta0[h_idx], qx0[h_idx], qy0[h_idx], z0[h_idx]를 이 순서로 복사한다(15–21). 함수 끝과 빈 줄도 포함한다(22–23). |
| 24–52 | `__device__ __forceinline__` (24)인 load_parent_scale_coeffs_mw는 ParentScaleCoeffsMW를 반환하고 ScaleCoefficients 참조와 int 참조 h_idx를 받는다(25–30). 반환 집합 초기화를 시작한다(31–32). 첫 묶음은 eta0[h_idx], qx0[h_idx], qy0[h_idx], z0[h_idx]이다(33–38). 둘째 묶음은 eta1x[h_idx], qx1x[h_idx], qy1x[h_idx], z1x[h_idx]이다(39–44). 셋째 묶음은 eta1y[h_idx], qx1y[h_idx], qy1y[h_idx], z1y[h_idx]이다(45–50). 모두 d_scale_coeffs에서 복사한다. 반환 초기화와 함수를 닫는다(51–52). 산술 연산이나 조건 분기는 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
