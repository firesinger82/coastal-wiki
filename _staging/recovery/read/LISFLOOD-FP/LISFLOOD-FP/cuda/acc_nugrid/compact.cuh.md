---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/compact.cuh
lines: 30
sha256: 262f048d5a523932cf3505953789d9e2d857ed16752f43fd3a567107df1c3653
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# compact.cuh — 판독 구간 기록

구간은 1행부터 30행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | `#pragma once` (1), cuda_runtime.h·MortonCode.h 포함(3·5), `lis::cuda::acc_nugrid` 이름공간(namespace)(7–12). 14행 주석은 Morton 코드(Morton code)의 짝수 비트를 제거하고 홀수 비트를 모은다고 적는다. 이 파일의 모든 구간에는 `#if` 계열 전처리 조건 분기가 없다. |
| 15–30 | `__host__ __device__ __forceinline__ int compact(MortonCode code)` (15)는 호스트(host)와 장치(device)에서 호출하는 인라인 함수(inline function)다. `int coord = code & 0x55555555;` (18). 비트 압축식은 `coord = (coord ^ (coord >> 1)) & 0x33333333;` (20), `coord = (coord ^ (coord >> 2)) & 0x0f0f0f0f;` (21), `coord = (coord ^ (coord >> 4)) & 0x00ff00ff;` (22), `coord = (coord ^ (coord >> 8)) & 0x0000ffff;` (23). 각 행 끝 주석은 남은 비트 위치를 그림으로 나타낸다(18·20–23). coord 반환(25), 함수·이름공간 종료와 빈 줄(26–30). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
