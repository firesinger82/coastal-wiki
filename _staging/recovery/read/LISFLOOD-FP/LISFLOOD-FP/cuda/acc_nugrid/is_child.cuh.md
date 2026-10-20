---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/is_child.cuh
lines: 28
sha256: 45cd382c45e6398822b19520e5920821e67792129998386007312d97e3f42499
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# is_child.cuh — 판독 구간 기록

구간은 1행부터 28행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | `#pragma once` (1) 뒤 CUDA 실행 환경·`MortonCode.h`·`index_1D.h`를 포함한다(3–5). `lis::cuda::acc_nugrid` 이름 공간을 연다(7–12). 이 파일에는 전처리 조건 분기가 없다. |
| 14–28 | 시작 시 7–12행의 `lis::cuda::acc_nugrid` 이름 공간 안. CUDA 함수 지정은 `__device__ __forceinline__ bool is_child` (14)이다. 인수는 `MortonCode fine_code`, `MortonCode current_code`, `int level`, `Parameters parameters`이다(16–19). 반환식은 `return ( ( fine_code >> ( 2 * (parameters.L - level) ) ) == current_code);` (23)이다. 세밀한 모턴 코드(Morton code)를 오른쪽으로 비트 이동(bit shift)한 값과 현재 코드를 비교한다. 함수와 이름 공간을 닫는다(24–28). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 18–23: 오른쪽 이동 폭은 `2 * (parameters.L - level)`이다. 이 함수에는 `level`과 `parameters.L`의 관계나 이동 폭의 범위를 검사하는 조건문이 없다.
