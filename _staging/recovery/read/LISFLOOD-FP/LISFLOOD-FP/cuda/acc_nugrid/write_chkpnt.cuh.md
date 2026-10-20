---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/write_chkpnt.cuh
lines: 37
sha256: f76c15983fda804262a7367b6792d496643af10aff40902a4fc8c9f57d8c3938
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# write_chkpnt.cuh — 판독 구간 기록

구간은 1행부터 37행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | `#pragma once` (1). stdio·stdlib·AssembledSolution·NonUniformNeighbours·cuda_utils·compact·get_lvl_idx를 포함한다(3–9). lis::cuda::acc_nugrid 이름공간(namespace)을 연다(11–16). 전처리 조건 분기는 없다. |
| 18–37 | `__host__ void write_chkpnt` (18)는 호스트(host) 함수 원형이다. 조립 해(assembled solution)·이웃·파일명·Pars·Solver는 const 참조, States는 수정 가능한 참조이다(20–25). NUMERIC_TYPE 통계 배열 포인터 네 개, bool non_uniform_n, const int& num_finest_elems, int verbose를 받는다(26–32). 기본 인수와 본문은 없다(33). 빈 줄과 이름공간 닫기(34–37). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
