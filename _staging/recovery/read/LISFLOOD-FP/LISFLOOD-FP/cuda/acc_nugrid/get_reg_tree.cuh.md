---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/get_reg_tree.cuh
lines: 26
sha256: 319eac5094616e56eac4baad619b63e874c53dc981f3e4e866725e87168a9146
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# get_reg_tree.cuh — 판독 구간 기록

구간은 1행부터 26행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | `#pragma once` (1) 뒤 CUDA 실행 환경·오류 검사·블록 매크로·CUDA 유틸리티·`reg_new.cuh`·`get_num_blocks.h`·`index_1D.h`를 포함한다(3–9). `lis::cuda::acc_nugrid` 이름 공간을 연다(11–16). 이 파일에는 전처리 조건 분기가 없다. |
| 18–26 | 시작 시 11–16행의 `lis::cuda::acc_nugrid` 이름 공간 안. `__host__ void get_reg_tree` (18)를 `bool* d_sig_details`와 `int lev` 인수로 선언한다(19–22). 선언 뒤 이름 공간을 닫는다(23–26). 함수 본문과 기본 인수 값은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
