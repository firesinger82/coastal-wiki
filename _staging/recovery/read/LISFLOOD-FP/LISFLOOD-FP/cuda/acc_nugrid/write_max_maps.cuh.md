---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/write_max_maps.cuh
lines: 30
sha256: 54fd04c7f0ebaa6ab8e397b262313f36fd941b8a501e596c9039e32bc872bd96
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# write_max_maps.cuh — 판독 구간 기록

구간은 1행부터 30행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | `#pragma once` (1). stdio·string·BLOCK_VAR_MACROS·cuda_utils·AssembledSolution 헤더를 포함한다(3–7). lis::cuda::acc_nugrid 이름공간(namespace)을 연다(9–14). 전처리 조건 분기는 없다. |
| 16–30 | `__host__ void write_max_maps` (16)는 호스트(host) 함수 선언이다. 결과 경로, const int& mesh_dim, const Pars& pars, NUMERIC_TYPE* maxH·totalHtm·maxHtm·initHtm을 받는다(17–24). 마지막 기본 인수의 원문은 `const int& precision = DEFAULT_PRECISION` (25). DEFAULT_PRECISION의 수치 정의는 이 파일에 없다. 선언 끝·빈 줄·이름공간 닫기를 포함한다(26–30). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
