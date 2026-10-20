---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/mra/get_max_from_array.cuh
lines: 23
sha256: 2230d6310795b354ff744d0ffd4ce16bab49b376a5e25059cb73c18b05bafb7f
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# get_max_from_array.cuh — 판독 구간 기록

구간은 1행부터 23행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | `#pragma once` (1). CUB 장치 축약 헤더, cmath, cuda_utils.cuh, real.h를 포함하고 빈 줄을 둔다(2–10). 이 파일에는 전처리 조건 분기가 없다. |
| 11–17 | AbsMax 함수 객체(functor)를 정의한다(11–16). `template <typename T>` (13), `__device__ __forceinline__` (14)를 사용한다. 삼항 연산자를 포함하는 연산자 본문 원문은 `T operator()(const T& a, const T& b) const { return ( abs(a) > abs(b) ) ? abs(a) : abs(b); }` (15)이다. 절댓값이 같으면 오른쪽 abs(b)를 반환한다. 빈 줄까지 포함한다(17). |
| 18–23 | `__host__` (18)인 get_max_from_array 선언이다(19–23). d_array는 real 포인터이고 array_length는 const int 참조이다(21–22). 이 선언에는 기본 인수가 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
