---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/tests/h_init_c_property.cuh
lines: 25
sha256: 4caa817cc57b33aaa1d2a986caca82755b817ff459debb57959de8c5750b3326
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# h_init_c_property.cuh — 판독 구간 기록

구간은 1행부터 25행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | `#pragma once` (1)로 중복 포함을 막는다. `cuda_runtime.h` (3)와 `Depths1D.h` (5)를 포함한다. CUDA 장치(device) 지시와 강제 인라인 지시 `__device__ __forceinline__` (7)가 붙은 `h_init_c_property`를 정의한다(8–14). 경계값 `bcs`, 지반고 `z_int`, 좌표 `x_or_y_int`를 상수 참조로 받는다(10–12). 빈 줄도 포함된다. 조건부 전처리 분기는 없다. |
| 15–25 | 시작 시 8–14행 `h_init_c_property` 본문 안. `eta_west`·`eta_east`를 `bcs.hl`·`bcs.hr`에서 복사한다(15–16). 수심 식은 `real h = eta_west - z_int;` (18)다. 무조건 `return h;` (20)를 실행한다. 그 뒤 원문 반환문은 `return (h < 0) ? 0 : h;` (22), `return (x_or_y_int <= 25) ? ( (h < 0) ? bcs.hl : h ) : eta_east - z_int;` (24)다. 두 반환문은 20행 반환 뒤에 위치한다. 빈 줄과 함수 종료를 포함한다(17·19·21·23·25). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 18–24: `return h;` 뒤에 삼항 반환문 두 개가 있다. 이 함수의 실행은 22·24행에 도달하지 않는다. 실제 반환 경로는 0 하한 제한 없이 `eta_west - z_int`를 반환한다.
- 15–24: `eta_east`를 초기화하지만 20행 반환 전에는 참조하지 않는다. 좌표 인수 `x_or_y_int`도 20행 반환 전에는 참조하지 않는다.
