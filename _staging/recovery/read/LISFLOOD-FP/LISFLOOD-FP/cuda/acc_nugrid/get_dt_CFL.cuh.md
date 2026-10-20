---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/get_dt_CFL.cuh
lines: 22
sha256: 5bd126d82fcb40e33613aeb4d7113d1d8a6d21550511b079363cfb2ba8f7d0f1
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# get_dt_CFL.cuh — 판독 구간 기록

구간은 1행부터 22행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | `#pragma once` (1) 뒤 CUB 장치 축약·CUDA 유틸리티(utility)·`../../lisflood.h`를 포함한다(3–5). `lis::cuda::acc_nugrid` 이름 공간을 연다(7–12). 이 파일에는 `#if` 계열의 컴파일 조건 분기가 없다. |
| 14–22 | 시작 시 7–12행의 `lis::cuda::acc_nugrid` 이름 공간 안. 호스트 함수 선언은 `__host__ NUMERIC_TYPE get_dt_CFL` (14)이다. 입력 배열 포인터는 `NUMERIC_TYPE*& d_dt_CFL`, 길이는 `const int& sol_len`이다(16–17). 선언과 이름 공간을 닫는다(18–22). 함수 본문과 기본 인수 값은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
