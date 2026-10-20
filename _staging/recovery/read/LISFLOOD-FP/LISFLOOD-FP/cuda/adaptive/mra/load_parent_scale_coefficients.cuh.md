---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/mra/load_parent_scale_coefficients.cuh
lines: 23
sha256: ad7d2afbcaa3275aae7863b60fb9aea912d65dbf49b5f3db39f354e7112d78d1
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# load_parent_scale_coefficients.cuh — 판독 구간 기록

구간은 1행부터 23행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | `#pragma once` (1). CUDA 실행 환경, ScaleCoefficients.h, ParentScaleCoeffs.h를 포함한다(3–6). 빈 줄도 포함한다. 이 파일에는 전처리 조건 분기가 없다. |
| 8–23 | `__device__ __forceinline__ ParentScaleCoeffsHW load_parent_scale_coefficients` (8)는 ScaleCoefficients 참조와 int 참조 h_idx를 받는다(9–13). parent_coeffs의 집합 초기화(aggregate initialization)는 d_scale_coeffs의 eta0[h_idx], qx0[h_idx], qy0[h_idx], z0[h_idx]를 이 순서로 복사한다(14–20). parent_coeffs를 반환한다(22). 산술 연산이나 조건 분기는 없다. 빈 줄과 함수 끝도 포함한다(21·23). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
