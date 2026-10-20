---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/mra/encode_scale_coeffs.cuh
lines: 45
sha256: b24e9a1ba31adc5720ac97e1a99bf78520247f0a747bf929d98643096963920e
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# encode_scale_coeffs.cuh — 판독 구간 기록

구간은 1행부터 45행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | 단일 포함 지시와 CUDA 런타임·../classes/ChildScaleCoeffs.h·../classes/ParentScaleCoeffs.h·encode_scale.cuh를 포함한다(1–7). 조건부 전처리 분기는 없다. 원문: `#pragma once` (1). |
| 9–20 | HW encode_scale_coeffs 장치 강제 인라인 오버로드이다(9–11). ChildScaleCoeffsHW 상수 참조를 받아 eta·qx·qy·z의 encode_scale 결과를 ParentScaleCoeffsHW로 반환한다(12–19). 원문: `__device__ __forceinline__` (9); `return` (12); `{` (13); `encode_scale(child_coeffs.eta),` (14); `encode_scale(child_coeffs.qx),` (15); `encode_scale(child_coeffs.qy),` (16); `encode_scale(child_coeffs.z)` (17); `};` (18). |
| 21–45 | MW encode_scale_coeffs 장치 강제 인라인 오버로드이다(21–23). ChildScaleCoeffsMW 상수 참조를 받는다. eta·qx·qy·z의 encode_scale_0 결과, encode_scale_1x 결과, encode_scale_1y 결과를 각각 한 묶음으로 구성하여 ParentScaleCoeffsMW로 반환한다(24–44). 원문: `__device__ __forceinline__` (21); `return` (24); `{` (25); `{` (26); `encode_scale_0(child_coeffs.eta),` (27); `encode_scale_0(child_coeffs.qx),` (28); `encode_scale_0(child_coeffs.qy),` (29); `encode_scale_0(child_coeffs.z)` (30); `},` (31); `{` (32); `encode_scale_1x(child_coeffs.eta),` (33); `encode_scale_1x(child_coeffs.qx),` (34); `encode_scale_1x(child_coeffs.qy),` (35); `encode_scale_1x(child_coeffs.z)` (36); `},` (37); `{` (38); `encode_scale_1y(child_coeffs.eta),` (39); `encode_scale_1y(child_coeffs.qx),` (40); `encode_scale_1y(child_coeffs.qy),` (41); `encode_scale_1y(child_coeffs.z)` (42); `}` (43); `};` (44). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
