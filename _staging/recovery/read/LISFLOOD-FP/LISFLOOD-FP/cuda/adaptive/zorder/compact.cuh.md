---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/zorder/compact.cuh
lines: 21
sha256: dc71452c9c0d998246bd8ccbbbe1c7f73648739e9bd46e8bca08d6a25f33a789
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# compact.cuh — 판독 구간 기록

구간은 1행부터 21행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | `#pragma once` (1)와 빈 줄(2) 뒤 `cuda_runtime.h`를 포함한다(3). 빈 줄(4) 뒤 `Coordinate.h`·`MortonCode.h`를 포함한다(5–6). 빈 줄(7) 뒤 주석은 모턴 코드(Morton code)의 짝수 비트를 제거하고 홀수 비트를 모은다고 설명한다(8). 전처리 조건 분기는 없다. |
| 9–21 | `__host__ __device__ __forceinline__` (9)로 호스트(host)와 장치(device) 양쪽의 강제 인라인 함수(inline function) `Coordinate compact(MortonCode code)`를 정의한다(10–11). 이진 배치 주석(12) 뒤 첫 식은 `Coordinate coord = code & 0x55555555;` (13)이다. 빈 줄(14) 뒤 `coord = (coord ^ (coord >> 1)) & 0x33333333;` (15), `coord = (coord ^ (coord >> 2)) & 0x0f0f0f0f;` (16), `coord = (coord ^ (coord >> 4)) & 0x00ff00ff;` (17), `coord = (coord ^ (coord >> 8)) & 0x0000ffff;` (18)를 순서대로 수행한다. 각 식의 뒤 주석은 비트가 모이는 이진 배치를 보인다(13·15–18). 빈 줄(19) 뒤 `return coord;` (20)로 결과를 반환한다. 함수 종료(21)이다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 13–18: 비트 압축(bit compaction)의 마스크와 시프트 횟수는 고정 상수이다. 마지막 마스크는 `0x0000ffff`이다.
