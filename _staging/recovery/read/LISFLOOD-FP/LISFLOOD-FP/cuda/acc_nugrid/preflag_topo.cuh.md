---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/preflag_topo.cuh
lines: 29
sha256: 6d6b3db0d0055c523ef75db21e2d8eb2ac00ce6b3231a5c040933c8de592c9f7
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# preflag_topo.cuh — 판독 구간 기록

구간은 1행부터 29행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | `#pragma once` (1) 및 CUDA 유틸리티·encode_and_thresh_topo·get_num_blocks·index_1D 헤더 포함(3–6). lis::cuda::acc_nugrid 이름공간을 연다(8–13). 이 파일 전체에는 조건부 전처리 분기가 없다. |
| 15–29 | 호스트 함수 선언은 `__host__ void preflag_topo` (15)이다. ScaleCoefficients·Details·Maxes·NUMERIC_TYPE eps·int lev 참조, bool* d_sig_details, bool non_uniform_n 및 int startfile을 받는다(16–25). 함수 본문과 기본 인수는 없다. 빈 줄과 이름공간 닫기를 포함한다(26–29). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
