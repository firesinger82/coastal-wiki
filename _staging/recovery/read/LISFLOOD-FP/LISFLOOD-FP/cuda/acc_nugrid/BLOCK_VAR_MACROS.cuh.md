---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/BLOCK_VAR_MACROS.cuh
lines: 36
sha256: 5155025dd8522f4c60f16f75d3735764a1bb5359a7993b9d48f43c19ef0599ec
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# BLOCK_VAR_MACROS.cuh — 판독 구간 기록

구간은 1행부터 36행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | `#pragma once` (1). `#ifndef THREADS_PER_BLOCK_MRA` (3)는 해당 매크로가 외부에서 정의되지 않았을 때만 전체 3–20행 블록을 처리한다. 주석은 허용값을 64·256·1024라고 적는다(4). `#define THREADS_PER_BLOCK_MRA 256` (5)가 이 블록의 기본값이다. 2·6행은 빈 줄. |
| 7–20 | 시작 시 3행 `#ifndef THREADS_PER_BLOCK_MRA` 안. `#if   THREADS_PER_BLOCK_MRA == 64` (7)는 `#define SHARED_MEMORY_BLOCK_DIM 8` (8), `#define LVL_SINGLE_BLOCK 3` (9). `#elif THREADS_PER_BLOCK_MRA == 256` (11)는 `#define SHARED_MEMORY_BLOCK_DIM 16` (12), `#define LVL_SINGLE_BLOCK 4` (13). `#elif THREADS_PER_BLOCK_MRA == 1024` (15)는 `#define SHARED_MEMORY_BLOCK_DIM 32` (16), `#define LVL_SINGLE_BLOCK 5` (17). `#endif` (19)는 값 선택, `#endif` (20)는 외부 정의 검사 종료다. 이 파일 안의 5행 정의를 따르면 256 분기가 선택된다. THREADS_PER_BLOCK_MRA가 이미 외부 정의되어 있으면 이 구간 전체를 건너뛴다. #else 분기는 없다. |
| 21–29 | 3행 조건 밖. `#ifndef NUM_VARS` (22), `#define NUM_VARS 4` (23), `#endif` (24). `#ifndef NUM_CHILDREN` (26), `#define NUM_CHILDREN 4` (27), `#endif` (28). 각 매크로가 외부 정의되지 않았을 때만 해당 기본값을 정의한다. 21·25·29행은 빈 줄. |
| 30–36 | `#ifndef SIGNIFICANT` (30), `#define SIGNIFICANT true` (31), `#endif` (32). 빈 줄(33) 뒤 `#ifndef INSIGNIFICANT` (34), `#define INSIGNIFICANT false` (35), `#endif` (36). 각각 외부 정의가 없을 때의 기본값이며 #else 분기는 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 3–20: SHARED_MEMORY_BLOCK_DIM·LVL_SINGLE_BLOCK의 세 값 선택 분기 전체가 THREADS_PER_BLOCK_MRA 미정의 조건 안에 있다. 외부에서 THREADS_PER_BLOCK_MRA를 정의한 경우 이 파일은 두 보조 매크로를 정의하지 않는다.
- 5–17: THREADS_PER_BLOCK_MRA 미정의 경로는 먼저 값을 256으로 정의한다. 이 경로에서 64·1024 분기는 선택되지 않는다.
