---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/encode_scale.cuh
lines: 79
sha256: d4131624a1e530527dd9f6e9e2696b56dcc5eaa29b756ec7c3d4ecd6e28c7e65
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# encode_scale.cuh — 판독 구간 기록

구간은 1행부터 79행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | `#pragma once` (1), CUDA 실행 환경·상위 `lisflood.h`·자식 스케일 계수(scale coefficient)·Haar 필터(Haar filter) 헤더 포함(3–6). 전처리 조건 분기는 없다. `lis::cuda::acc_nugrid` 이름 공간(namespace)을 연다(8–13). |
| 15–27 | 시작 시 8–13행 이름 공간 안. `encode_scale`의 줄 주석 정의(15–18)에 적힌 반환식은 `//	return C(0.5) * (H0 * (H0 * u.child_0 + H1 * u.child_2) + H1 * (H0 * u.child_1 + H1 * u.child_3));` (17). 20행은 `/*`로 네 인수 `encode_scale_11` 블록 주석을 연다. 그 주석 안의 반환식은 `return C(0.5) * (H0_11 * (H0_11 * u0.child_0  + H0_12 * u1y.child_0 + H1_11 * u0.child_2  + H1_12 * u1y.child_2) +`<br>`H0_12 * (H0_11 * u1x.child_0 + H0_12 * uxy.child_0 + H1_11 * u1x.child_2 + H1_12 * uxy.child_2) +`<br>`H1_11 * (H0_11 * u0.child_1  + H0_12 * u1y.child_1 + H1_11 * u0.child_3  + H1_12 * u1y.child_3) +`<br>`H1_12 * (H0_11 * u1x.child_1 + H0_12 * uxy.child_1 + H1_11 * u1x.child_3 + H1_12 * uxy.child_3));` (22–25). 이 함수 모양의 주석은 26행에서 중괄호를 닫지만 블록 주석은 계속 열린 상태이다. |
| 28–51 | 시작 시 8–13행 이름 공간·20행 블록 주석 안. 네 인수 `encode_scale_12` 주석 반환식은 `return C(0.5) * (H0_11 * (H0_21 * u0.child_0  + H0_22 * u1y.child_0 + H1_21 * u0.child_2  + H1_22 * u1y.child_2) +`<br>`H0_12 * (H0_21 * u1x.child_0 + H0_22 * uxy.child_0 + H1_21 * u1x.child_2 + H1_22 * uxy.child_2) +`<br>`H1_11 * (H0_21 * u0.child_1  + H0_22 * u1y.child_1 + H1_21 * u0.child_3  + H1_22 * u1y.child_3) +`<br>`H1_12 * (H0_21 * u1x.child_1 + H0_22 * uxy.child_1 + H1_21 * u1x.child_3 + H1_22 * uxy.child_3));` (30–33), `encode_scale_21` 주석 반환식은 `return C(0.5) * (H0_21 * (H0_11 * u0.child_0  + H0_12 * u1y.child_0 + H1_11 * u0.child_2  + H1_12 * u1y.child_2) +`<br>`H0_22 * (H0_11 * u1x.child_0 + H0_12 * uxy.child_0 + H1_11 * u1x.child_2 + H1_12 * uxy.child_2) +`<br>`H1_21 * (H0_11 * u0.child_1  + H0_12 * u1y.child_1 + H1_11 * u0.child_3  + H1_12 * u1y.child_3) +`<br>`H1_22 * (H0_11 * u1x.child_1 + H0_12 * uxy.child_1 + H1_11 * u1x.child_3 + H1_12 * uxy.child_3));` (38–41), `encode_scale_22` 주석 반환식은 `return C(0.5) * (H0_21 * (H0_21 * u0.child_0  + H0_22 * u1y.child_0 + H1_21 * u0.child_2  + H1_22 * u1y.child_2) +`<br>`H0_22 * (H0_21 * u1x.child_0 + H0_22 * uxy.child_0 + H1_21 * u1x.child_2 + H1_22 * uxy.child_2) +`<br>`H1_21 * (H0_21 * u0.child_1  + H0_22 * u1y.child_1 + H1_21 * u0.child_3  + H1_22 * u1y.child_3) +`<br>`H1_22 * (H0_21 * u1x.child_1 + H0_22 * uxy.child_1 + H1_21 * u1x.child_3 + H1_22 * uxy.child_3));` (46–49). 50행의 `}*/`가 함수 모양의 중괄호와 블록 주석을 닫는다. 이 구간의 함수 모양 코드는 모두 주석이다. |
| 52–59 | 시작 시 8–13행 이름 공간 안이며 블록 주석 밖. 실제 함수 지정은 `__device__ __forceinline__ NUMERIC_TYPE encode_scale_11(ScaleChildren& u0, ScaleChildren& u1x, ScaleChildren& u1y)` (52). 평균 스케일 성분의 반환식은 `return HH0_11 * u0.child_0 + HH0_12 * u1x.child_0 + HH0_13 * u1y.child_0 +`<br>`HH1_11 * u0.child_2 + HH1_12 * u1x.child_2 + HH1_13 * u1y.child_2 +`<br>`HH2_11 * u0.child_1 + HH2_12 * u1x.child_1 + HH2_13 * u1y.child_1 +`<br>`HH3_11 * u0.child_3 + HH3_12 * u1x.child_3 + HH3_13 * u1y.child_3;` (54–57). `HH` 필터 1행으로 네 자식의 세 성분을 선형 결합한다. 조건 분기는 없다. |
| 60–67 | 시작 시 8–13행 이름 공간 안. 실제 함수 지정은 `__device__ __forceinline__ NUMERIC_TYPE encode_scale_21(ScaleChildren& u0, ScaleChildren& u1x, ScaleChildren& u1y)` (60). 21 성분의 반환식은 `return HH0_21 * u0.child_0 + HH0_22 * u1x.child_0 + HH0_23 * u1y.child_0 +`<br>`HH1_21 * u0.child_2 + HH1_22 * u1x.child_2 + HH1_23 * u1y.child_2 +`<br>`HH2_21 * u0.child_1 + HH2_22 * u1x.child_1 + HH2_23 * u1y.child_1 +`<br>`HH3_21 * u0.child_3 + HH3_22 * u1x.child_3 + HH3_23 * u1y.child_3;` (62–65). `HH` 필터 2행을 사용한다. 조건 분기는 없다. |
| 68–79 | 시작 시 8–13행 이름 공간 안. 실제 함수 지정은 `__device__ __forceinline__ NUMERIC_TYPE encode_scale_12(ScaleChildren& u0, ScaleChildren& u1x, ScaleChildren& u1y)` (68). 12 성분의 반환식은 `return HH0_31 * u0.child_0 + HH0_32 * u1x.child_0 + HH0_33 * u1y.child_0 +`<br>`HH1_31 * u0.child_2 + HH1_32 * u1x.child_2 + HH1_33 * u1y.child_2 +`<br>`HH2_31 * u0.child_1 + HH2_32 * u1x.child_1 + HH2_33 * u1y.child_1 +`<br>`HH3_31 * u0.child_3 + HH3_32 * u1x.child_3 + HH3_33 * u1y.child_3;` (70–73). `HH` 필터 3행을 사용한다. 함수와 이름 공간 종료·빈 줄을 포함한다(74–79). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 15–50·52–74: uxy를 받는 네 인수 버전과 22 성분은 주석 안에 있다. 실행 정의는 세 인수의 11·21·12 성분 세 개이다.
