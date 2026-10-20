---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/mra/store_scale_coefficients.cuh
lines: 70
sha256: af39fcabf2a124bb5103fd5bf51c50fc57d78676d4e08500abbb0c2d5f33bd61
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# store_scale_coefficients.cuh — 판독 구간 기록

구간은 1행부터 70행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | `#pragma once` (1), CUDA 실행·cstdio·ParentScaleCoeffs·ChildScaleCoeffs·ScaleCoefficients·index_1D 헤더 포함(3–10). 조건부 전처리 분기는 없다. |
| 12–23 | `__device__ __forceinline__ void store_scale_coefficients` (12) 장치 함수의 ParentScaleCoeffsHW 오버로드다. const 참조 parent_coeffs·d_scale_coeffs·index_1D h_idx를 받는다(14–16). 부모 eta·qx·qy를 전역 eta0·qx0·qy0의 h_idx 위치에 복사한다(19–21). 함수 종료·빈 줄(22–23). |
| 24–43 | `__device__ __forceinline__ void store_scale_coefficients` (24)의 ParentScaleCoeffsMW 오버로드다(26–30). 부모 _0의 eta·qx·qy는 eta0·qx0·qy0(31–33), _1x는 eta1x·qx1x·qy1x(35–37), _1y는 eta1y·qx1y·qy1y(39–41)의 h_idx 위치로 복사한다. 함수 종료·빈 줄(42–43). |
| 44–70 | `__device__ __forceinline__ void store_scale_coefficients` (44)의 ChildScaleCoeffsHW 오버로드다(46–50). eta·qx·qy의 child_0..child_3을 각각 eta0·qx0·qy0의 h_idx + 0..h_idx + 3에 복사한다(51–64). z0의 같은 네 위치 복사문은 66–69행 블록 주석에 있어 실행하지 않는다. 함수 종료(70). 이 파일의 세 함수에는 조건문·루프·기본 인수가 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 12–70: 이 파일에는 ParentScaleCoeffsHW·ParentScaleCoeffsMW·ChildScaleCoeffsHW 오버로드가 있다. ChildScaleCoeffsMW 오버로드는 없다.
- 66–69: 자식 z0 저장문 네 개는 블록 주석에 들어 있다.
