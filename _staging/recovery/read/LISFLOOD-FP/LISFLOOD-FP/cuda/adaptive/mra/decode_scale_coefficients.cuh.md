---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/mra/decode_scale_coefficients.cuh
lines: 24
sha256: 7b8144df143fadbbad5367579dc352febcbe636a7848c515d401b15cef2464e5
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# decode_scale_coefficients.cuh — 판독 구간 기록

구간은 1행부터 24행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | 단일 포함 지시와 CUDA 런타임, Filters·부모/자식 계수·Detail·자식 복원 헤더를 포함한다(1–9). 조건부 전처리 분기는 없다. 원문: `#pragma once` (1). |
| 11–24 | 장치 강제 인라인 decode_scale_coefficients는 ParentScaleCoeffsHW와 DetailHW의 참조를 받는다(11–16). eta·qx·qy를 각각 decode_scale_children에 전달하여 ChildScaleCoeffsHW를 반환한다(17–23). 네 번째 초기화 묶음은 정수 0 네 개이다(22). 원문: `__device__ __forceinline__ ChildScaleCoeffsHW decode_scale_coefficients` (11); `return` (17); `{` (18); `decode_scale_children(parent_coeffs.eta, detail.eta),` (19); `decode_scale_children(parent_coeffs.qx,  detail.qx),` (20); `decode_scale_children(parent_coeffs.qy,  detail.qy),` (21); `{ 0, 0, 0, 0 }` (22); `};` (23). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 19–22: eta·qx·qy는 복원 루틴으로 계산하지만 네 번째 묶음은 { 0, 0, 0, 0 }으로 고정한다.
