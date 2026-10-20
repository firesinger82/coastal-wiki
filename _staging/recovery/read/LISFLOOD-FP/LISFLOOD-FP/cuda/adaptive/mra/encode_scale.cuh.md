---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/mra/encode_scale.cuh
lines: 54
sha256: 44ebe72bf817dd587f3a7321e9158ac8a786d31e643d78360820de40b4e1051c
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# encode_scale.cuh — 판독 구간 기록

구간은 1행부터 54행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | 단일 포함 지시와 CUDA 런타임·real·ScaleChildren·Filters 헤더를 포함한다(1–7). 조건부 전처리 분기는 없다. 원문: `#pragma once` (1). |
| 9–14 | HW encode_scale 장치 강제 인라인 함수는 네 자식을 H0/H1로 결합하고 C(0.5)를 곱해 실수 부모 계수를 반환한다(9–13). 원문: `__device__ __forceinline__` (9); `return C(0.5) * (H0 * (H0 * u.child_0 + H1 * u.child_2) + H1 * (H0 * u.child_1 + H1 * u.child_3));` (12). |
| 15–23 | MW encode_scale_0 장치 강제 인라인 함수는 자식별 0/1x/1y 성분과 HH0..HH3 첫 행의 계수들을 합산하고 C(2.0)으로 나눈다(15–22). 필터 순서 0/1/2/3은 자식 0/2/1/3에 대응한다. 원문: `__device__ __forceinline__` (15); `return (HH0_11 * u._0.child_0 + HH0_12 * u._1x.child_0 + HH0_13 * u._1y.child_0 +` (18); `HH1_11 * u._0.child_2 + HH1_12 * u._1x.child_2 + HH1_13 * u._1y.child_2 +` (19); `HH2_11 * u._0.child_1 + HH2_12 * u._1x.child_1 + HH2_13 * u._1y.child_1 +` (20); `HH3_11 * u._0.child_3 + HH3_12 * u._1x.child_3 + HH3_13 * u._1y.child_3) / C(2.0);` (21). |
| 24–32 | MW encode_scale_1x 장치 강제 인라인 함수는 HH0..HH3 두 번째 행과 자식별 0/1x/1y 성분을 결합하고 C(2.0)으로 나눈다(24–31). 원문: `__device__ __forceinline__` (24); `return (HH0_21 * u._0.child_0 + HH0_22 * u._1x.child_0 + HH0_23 * u._1y.child_0 +` (27); `HH1_21 * u._0.child_2 + HH1_22 * u._1x.child_2 + HH1_23 * u._1y.child_2 +` (28); `HH2_21 * u._0.child_1 + HH2_22 * u._1x.child_1 + HH2_23 * u._1y.child_1 +` (29); `HH3_21 * u._0.child_3 + HH3_22 * u._1x.child_3 + HH3_23 * u._1y.child_3) / C(2.0);` (30). |
| 33–46 | 33행부터 45행까지는 블록 주석이다. GC 계수를 서로 다른 u0/u1x/u1y 구조 표기와 u._0/u._1x/u._1y 표기로 적은 식 두 묶음이다(35–43). 주석이므로 컴파일하지 않는다. 조건부 전처리 분기는 없다. 원문: `GC0_31 * u0.child_0 + GC0_32 * u1x.child_0 + GC0_33 * u1y.child_0 +` (35); `GC1_31 * u0.child_2 + GC1_32 * u1x.child_2 + GC1_33 * u1y.child_2 +` (36); `GC2_31 * u0.child_1 + GC2_32 * u1x.child_1 + GC2_33 * u1y.child_1 +` (37); `GC3_31 * u0.child_3 + GC3_32 * u1x.child_3 + GC3_33 * u1y.child_3` (38); `GC0_31 * u._0.child_0 + GC0_32 * u._1x.child_0 + GC0_33 * u._1y.child_0` (40); `GC1_31 * u._0.child_2 + GC1_32 * u._1x.child_2 + GC1_33 * u._1y.child_2` (41); `GC2_31 * u._0.child_1 + GC2_32 * u._1x.child_1 + GC2_33 * u._1y.child_1` (42); `GC3_31 * u._0.child_3 + GC3_32 * u._1x.child_3 + GC3_33 * u._1y.child_3` (43). |
| 47–54 | MW encode_scale_1y 장치 강제 인라인 함수는 HH0..HH3 세 번째 행과 자식별 0/1x/1y 성분을 결합하고 C(2.0)으로 나눈다(47–54). 원문: `__device__ __forceinline__` (47); `return (HH0_31 * u._0.child_0 + HH0_32 * u._1x.child_0 + HH0_33 * u._1y.child_0 +` (50); `HH1_31 * u._0.child_2 + HH1_32 * u._1x.child_2 + HH1_33 * u._1y.child_2 +` (51); `HH2_31 * u._0.child_1 + HH2_32 * u._1x.child_1 + HH2_33 * u._1y.child_1 +` (52); `HH3_31 * u._0.child_3 + HH3_32 * u._1x.child_3 + HH3_33 * u._1y.child_3) / C(2.0);` (53). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 33–45: GC 계수 식은 블록 주석 안에 있다. 활성 encode_scale_1y 반환식은 50–53행 HH 계수를 사용한다.
