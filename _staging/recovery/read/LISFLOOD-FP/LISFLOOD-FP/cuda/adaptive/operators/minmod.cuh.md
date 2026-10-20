---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/operators/minmod.cuh
lines: 25
sha256: 127f7c20b9ca1f98b77d36de123a9b90f860f37d150b9ab6b4374759a5dfe5c2
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# minmod.cuh — 판독 구간 기록

구간은 1행부터 25행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–14 | `#pragma once`와 CUDA 런타임·실수 형식 헤더를 포함한다(1–5). CUDA 장치 함수(device function) `minmod`가 실수 세 개를 상수 참조로 받는다(7–14). 전처리 조건 분기는 없다. 원문: `#pragma once` (1); `__device__ __forceinline__` (7). |
| 15–25 | 시작 시 7–14행 `minmod` 안. a와 b, a와 c의 곱이 모두 양수이면 a의 부호를 계산하고 세 절댓값의 최솟값에 그 부호를 곱해 반환한다(15–20). `else`에서는 `C(0.0)`을 반환한다(21–24). 함수 종료를 포함한다(25). 원문: `if ( ( a * b > C(0.0) ) && ( a * c > C(0.0) ) )` (15); `const real sign_a = ( a > C(0.0) ) - ( a < C(0.0) );` (17); `return min( abs(a), min( abs(b), abs(c) ) ) * sign_a;` (19); `else` (21); `return C(0.0);` (23). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
