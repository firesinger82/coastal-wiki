---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/output/write_mesh_info.h
lines: 14
sha256: ad7e54f4e77cd6f7fd198752d90343815e064fb5b56dc59f5488b3b69cf89763
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# write_mesh_info.h — 판독 구간 기록

구간은 1행부터 14행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | `#pragma once` (1)로 중복 포함을 막는다. `<cstdio>`·`<cstdlib>`·`<cstring>` (3–5), `SimulationParams.h` (7)를 포함한다. 빈 줄도 포함된다. 조건부 전처리 분기는 없다. |
| 9–14 | `void write_mesh_info` 원형을 선언한다(9–14). `const SimulationParams& sim_params` (11), `const int& mesh_dim` (12), `const char* resdir` (13)를 받는다. 기본 인수 값이나 실행 본문은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
