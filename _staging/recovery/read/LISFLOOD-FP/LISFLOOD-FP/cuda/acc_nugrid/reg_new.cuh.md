---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/reg_new.cuh
lines: 32
sha256: 4da252c23242ff8e57b72489c3226648ee781292a75c489f22169978435879cd
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# reg_new.cuh — 판독 구간 기록

구간은 1행부터 32행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | `#pragma once` (1)로 중복 포함을 막는다. CUDA 실행·커널 실행 매개변수, lisflood, DetailChildren, BLOCK_VAR_MACROS, index_1D, get_child_details, get_lvl_idx 헤더를 포함한다(3–10). lis::cuda::acc_nugrid 이름공간(namespace)을 연다(12–17). 전처리 조건 분기는 없다. |
| 19–32 | `template <bool SINGLE_BLOCK>` (19)<br>`__global__ void reg_new` (20)는 불리언 템플릿(template) 인자를 갖는 CUDA 커널(kernel)의 선언이다. bool* 플래그, int level, index_1D 이전·현재·다음 레벨 위치와 int num_threads를 받는다(21–28). 기본 인수와 본문은 없다. 빈 줄과 이름공간 닫기(29–32). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
