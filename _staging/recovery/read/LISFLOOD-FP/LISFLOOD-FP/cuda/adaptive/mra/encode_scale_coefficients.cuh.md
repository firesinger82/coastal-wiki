---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/mra/encode_scale_coefficients.cuh
lines: 20
sha256: 3e221f33f6d704152c018c37ccde794e7815c0718b4d2db016bee794a2d085fd
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# encode_scale_coefficients.cuh — 판독 구간 기록

구간은 1행부터 20행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | 단일 포함 지시와 CUDA 런타임, ChildScaleCoefficients.h·ParentScaleCoefficient.h·encode_scale.cuh를 포함한다(1–7). 조건부 전처리 분기는 없다. 두 형식 헤더 경로는 ../classes/ 접두가 없는 원문 표기이다. 원문: `#pragma once` (1); `#include "ChildScaleCoefficients.h"` (5); `#include "ParentScaleCoefficient.h"` (6). |
| 9–20 | 장치 강제 인라인 encode_scale_coefficients는 ChildScaleCoefficients를 값으로 받는다(9–10). eta·qx·qy·z 각각에 encode_scale을 호출하여 ParentScaleCoefficient 집합을 만들고 반환한다(11–19). 원문: `__device__ __forceinline__ ParentScaleCoefficient encode_scale_coefficients(ChildScaleCoefficients child_scale_coeffs)` (9); `ParentScaleCoefficient parent_scale_coeffs =` (11); `{` (12); `encode_scale(child_scale_coeffs.eta),` (13); `encode_scale(child_scale_coeffs.qx),` (14); `encode_scale(child_scale_coeffs.qy),` (15); `encode_scale(child_scale_coeffs.z)` (16); `};` (17). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 5–6·9: 이 헤더의 형식 이름은 ChildScaleCoefficients와 ParentScaleCoefficient이다. 대상 encode_scale_coeffs.cuh의 ChildScaleCoeffsHW/MW·ParentScaleCoeffsHW/MW 표기와 다르다. 포함 파일의 존재 여부와 형식 정의는 이 파일 판독에서 확인하지 않았다.
