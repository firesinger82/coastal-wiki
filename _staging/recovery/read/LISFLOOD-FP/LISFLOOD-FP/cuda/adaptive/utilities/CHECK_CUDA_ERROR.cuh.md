---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/utilities/CHECK_CUDA_ERROR.cuh
lines: 19
sha256: d3f6d28e03c30a5c78e27fc1f0ecaa5c45e5194301b2ad30f7339183e53b262a
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# CHECK_CUDA_ERROR.cuh — 판독 구간 기록

구간은 1행부터 19행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | `#pragma once` (1)와 빈 줄(2) 뒤 CUDA 실행 환경(runtime) 헤더를 포함한다(3). 빈 줄과 `cstdio`·`cstdlib` 포함 및 용도 주석이 있다(4–7). 오류 검사 주석(8) 뒤 매크로 원문은 `#define CHECK_CUDA_ERROR(ans) { CUDAAssert( (ans), __FILE__, __LINE__); }` (9)이다. 오류값과 호출 지점의 파일명·행 번호를 `CUDAAssert`에 넘긴다. 마지막은 빈 줄(10)이다. 전처리 조건 분기는 없다. |
| 11–19 | 인라인 함수(inline function) 원형은 `inline void CUDAAssert(cudaError_t error, const char* file, int line, bool abort = true)` (11)이다. 기본 `abort`는 참이다. 함수 본문(12)에서 `if (error != cudaSuccess)` (13)가 참일 때 `cudaGetErrorString(error)`를 호출하여 오류 문자열을 얻고 파일명·행 번호와 함께 표준 오류로 출력한다(15). 빈 줄(16) 뒤 `if (abort) exit(error);` (17)는 같은 오류 분기 안에서 종료 여부를 결정한다. 두 블록을 닫는다(18–19). 성공 상태에서는 출력과 종료를 수행하지 않는다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
