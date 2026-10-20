---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/mra/extra_significance.cuh
lines: 27
sha256: 98010e7e54fe02b205559d4e9e740103787fac1ff687ee8454d429b6c7829c8f
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# extra_significance.cuh — 판독 구간 기록

구간은 1행부터 27행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | `#pragma once` (1). `#ifndef M_BAR` (3)이 참이면 `#define M_BAR C(1.5)` (4)를 적용하고 `#endif // !M_BAR` (5)로 닫는다. M_BAR가 이미 정의되어 있으면 4행 정의를 건너뛴다. 빈 줄을 포함한다. CUDA 실행 환경 헤더, BLOCK_VAR_MACROS.cuh, SolverParams.h, HierarchyIndex.h, get_lvl_idx.cuh를 포함한다(8–16). 이 포함부는 3행 전처리 조건 밖이다. |
| 18–27 | 3행 전처리 조건 밖. `template<bool SINGLE_BLOCK>` (18), `__global__` (19)인 CUDA 커널(kernel) extra_significance를 선언한다(20–27). 인수는 상세 계수의 중요도 표시(significance flag) d_sig_details, 정규화 상세 계수(normalized detail coefficient) 배열 d_norm_details, 값으로 받는 solver_params, level, num_threads이다(22–26). 이 파일에는 커널 본문과 SINGLE_BLOCK별 실행 분기가 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
