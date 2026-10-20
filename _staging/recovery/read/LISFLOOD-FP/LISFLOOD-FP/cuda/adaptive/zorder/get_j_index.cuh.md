---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/zorder/get_j_index.cuh
lines: 9
sha256: 3ba9df5145bd7a4913d5ca11e6128a7e19efc9b53cd2332da9a52b35fff1e00e
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# get_j_index.cuh — 판독 구간 기록

구간은 1행부터 9행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–4 | `#pragma once` (1)와 빈 줄(2) 뒤 `../zorder/compact.cuh`를 포함한다(3). 마지막은 빈 줄(4)이다. 전처리 조건 분기는 없다. |
| 5–9 | `__host__ __device__ __forceinline__` (5) 함수 `Coordinate get_j_index(MortonCode code)`를 정의한다(6–7). 반환식은 `return compact(code >> 1);` (8)이다. 모턴 코드(Morton code)를 1비트 오른쪽으로 이동한 뒤 `compact`에 전달하여 좌표를 반환한다. 함수 종료(9)이다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
