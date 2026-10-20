---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/zorder/generate_morton_code.cuh
lines: 16
sha256: 27b43240c6a8b2c955669d5a6eaf57f6a41be781cf4b20811988e07b8af64eaf
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# generate_morton_code.cuh — 판독 구간 기록

구간은 1행부터 16행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | `#pragma once` (1)와 빈 줄(2) 뒤 `cuda_runtime.h`를 포함한다(3). 빈 줄(4) 뒤 `dilate.cuh`를 포함한다(5). 마지막은 빈 줄(6)이다. 전처리 조건 분기는 없다. |
| 7–16 | `__host__ __device__ __forceinline__` (7) 함수 `MortonCode generate_morton_code`는 `Coordinate x`, `Coordinate y`를 받는다(8–13). 주석은 비트 연산자(bitwise operator)·16진수 설명을 찾도록 안내한다(14). 반환식 원문은 `return dilate(x) \| (dilate(y) << 1);` (15)이다. 두 좌표 각각에 `dilate`를 호출하고 y 결과를 1비트 왼쪽으로 이동하여 비트 OR로 합친 모턴 코드(Morton code)를 반환한다. 함수 종료(16)이다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
