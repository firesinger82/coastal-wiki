---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/CHECK_CUDA_ERROR.cuh
lines: 19
sha256: d785131e733fa678db1a10e130526023e470986b4ce2fec13b99a3bdbfeb59f8
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# CHECK_CUDA_ERROR.cuh — 판독 구간 기록

구간은 1행부터 19행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | `#pragma once` (1), cuda_runtime.h·stdio.h·stdlib.h 포함(3·5–6), CUDA 오류 검사 주석(8). `#define CHECK_CUDA_ERROR(ans) { CUDAAssert( (ans), __FILE__, __LINE__); }` (9)는 인수의 오류값과 호출 파일·행 번호를 CUDAAssert에 전달한다. 이 파일의 모든 구간에는 `#if` 계열 전처리 조건 분기가 없다. |
| 11–19 | `inline void CUDAAssert(cudaError_t error, const char* file, int line, bool abort = true)` (11)로 abort 기본값을 true로 설정한다. `if (error != cudaSuccess)` (13)에서 cudaGetErrorString(error)·file·line을 표준 오류에 출력한다(15). `if (abort) exit(error);` (17). 두 블록 종료(18–19). CUDA 성공이면 출력·종료문에 도달하지 않는다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
