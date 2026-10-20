---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/utilities/get_lvl_idx.cuh
lines: 23
sha256: 71311b9bef0d687dde41a9ba29e00b01274f3d8b7687cd847036f8eefe051a0e
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# get_lvl_idx.cuh — 판독 구간 기록

구간은 1행부터 23행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | `#pragma once` (1)와 빈 줄(2) 뒤 `cuda_runtime.h` (3), 빈 줄(4), `../types/HierarchyIndex.h` (5)를 포함한다. 빈 줄(6) 뒤 주석은 모턴 코드(Morton code)로 1차원에 배치한 격자 계층에서 세분화 수준(refinement level)의 시작 인덱스를 구한다고 적는다(7–9). 주석의 다른 설명 위치를 이번 판독에서 따라가지는 않았다. 전처리 조건 분기는 없다. |
| 10–23 | `__host__ __device__ __forceinline__` (10)로 호스트와 장치(device) 양쪽의 강제 인라인 함수 `HierarchyIndex get_lvl_idx(int level)`를 정의한다(11–12). 주석은 수준 n까지의 누적 원소 수를 `(4^(n+1) - 1) / 3`, 수준 n의 시작을 `(4^n - 1) / 3`으로 설명한다(13–19). 빈 줄(20) 뒤 시프트(shift)와 4의 거듭제곱 관계를 주석으로 적는다(21). 반환식 원문은 `return ( ( 1 << (2 * level) ) - 1 ) / 3;` (22)이다. 함수 종료(23)이다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11–22: `level`은 `int` 인수이다. 반환식은 정수 리터럴 `1`을 `2 * level`만큼 왼쪽으로 시프트한다. 이 함수에는 `level`의 부호나 시프트 횟수 범위를 검사하는 조건이 없다.
