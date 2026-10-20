---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/mra/store_scale_coeffs.cuh
lines: 125
sha256: 30bf8c4bbaa7b88d8af3a1b45eb8a8e61f3567994051df9e213385461f79d7bd
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# store_scale_coeffs.cuh — 판독 구간 기록

구간은 1행부터 125행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | `#pragma once` (1) 뒤 CUDA 실행·부모 및 자식 스케일 계수(scale coefficient)·ScaleCoefficients·HierarchyIndex 헤더를 포함한다(3–8). 조건부 전처리 분기는 없다. |
| 10–22 | `__device__ __forceinline__` (10) 지정의 store_scale_coeffs ParentScaleCoeffsHW 오버로드를 정의한다(11–17). const HierarchyIndex& h_idx를 받는다(15). 부모 eta·qx·qy를 eta0·qx0·qy0의 h_idx에 복사한다(18–20). 함수 종료·빈 줄(21–22). |
| 23–43 | `__device__ __forceinline__` (23) 지정의 ParentScaleCoeffsMW 오버로드를 정의한다(24–30). _0의 eta·qx·qy는 eta0·qx0·qy0(31–33), _1x는 eta1x·qx1x·qy1x(35–37), _1y는 eta1y·qx1y·qy1y(39–41)의 h_idx에 복사한다. 함수 종료·빈 줄(42–43). |
| 44–72 | `__device__ __forceinline__` (44) 지정의 ChildScaleCoeffsHW 오버로드다(45–51). child_coeffs의 eta·qx·qy에서 child_0..child_3을 eta0·qx0·qy0의 h_idx + 0..h_idx + 3에 복사한다(52–65). z0 저장문 네 개는 67–70행 블록 주석이라 실행되지 않는다. 함수 종료·빈 줄(71–72). |
| 73–95 | `__device__ __forceinline__` (73) 지정의 ChildScaleCoeffsMW 오버로드를 정의한다(74–80). eta._0·qx._0·qy._0의 child_0..child_3을 eta0·qx0·qy0의 h_idx + 0..h_idx + 3에 복사한다(81–94). |
| 96–125 | 시작 시 73–80행 ChildScaleCoeffsMW용 store_scale_coeffs 함수 안. eta._1x·qx._1x·qy._1x의 child_0..child_3을 eta1x·qx1x·qy1x의 h_idx + 0..h_idx + 3에 복사한다(96–109). eta._1y·qx._1y·qy._1y는 eta1y·qx1y·qy1y의 같은 네 위치로 복사한다(111–124). 함수 종료(125). 이 파일의 네 함수에는 조건문·루프·기본 인수가 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 67–70: ChildScaleCoeffsHW 오버로드의 z0 저장문 네 개는 블록 주석이다.
- 81–124: ChildScaleCoeffsMW 오버로드는 eta·qx·qy의 _0·_1x·_1y를 저장한다. 이 오버로드에는 z 저장문이 없다.
