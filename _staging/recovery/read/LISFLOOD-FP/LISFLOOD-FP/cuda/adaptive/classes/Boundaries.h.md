---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/classes/Boundaries.h
lines: 40
sha256: 79087cea8f2c2eacfb352a64b2c77ecff2fef70713ee9490a9b929bd11101d36
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# Boundaries.h — 판독 구간 기록

구간은 1행부터 40행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | `#pragma once` (1), Boundary.h 포함(3). 전처리 조건 분기는 없다. Boundaries 구조체는 north·east·south·west의 Boundary 네 개를 보유한다(5–10). |
| 12–27 | 시작 시 5–6행 Boundaries 구조체 안. 생성자는 input_filename·sim_params·cell_size·test_case와 NORTH·EAST·SOUTH·WEST를 각 Boundary 생성자에 전달한다(12–24). `if (test_case != 0) fprintf(stdout, "Running built-in test case, using open boundary conditions.\n");` (25)로 내장 시험의 개방 경계(open boundary) 안내를 출력한다. 방향 상수의 정의·값은 이 파일에 없다. |
| 28–40 | 시작 시 5–6행 Boundaries 구조체 안. update_all_inlets는 input_filename과 current_time을 받는다(28–33). 네 방향의 update_inlet에 current_time을 전달한다(34–37). 메서드(method)·구조체 종료(38–40). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 28–37: update_all_inlets는 input_filename을 인수로 선언하지만 본문에서 사용하지 않는다.
