---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/classes/SolverParams.h
lines: 73
sha256: 0338ea76176d03155886a57280a66296f55019aa14ff472ad116d8ea818eb4c4
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# SolverParams.h — 판독 구간 기록

구간은 1행부터 73행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–27 | `#pragma once` (1), 실수형·해법 종류·정수/불리언/실수 키 판독 헤더 포함(3–8). 전처리 조건 분기는 없다. 기본값: `int  L             = 0;` (12), `real initial_tstep = C(0.0);` (13), `real epsilon       = C(0.0);` (14), `real tol_h         = C(1e-3);` (15), `real tol_q         = C(0.0);` (16), `real tol_s         = C(1e-9);` (17), `real wall_height   = C(0.0);` (18), `int  solver_type   = 0;` (19), `real CFL           = C(0.0);` (20), `bool grading       = false;` (21), `bool limitslopes   = false;` (22), `real tol_Krivo     = C(9999.0);` (23), `bool refine_wall   = false;` (24), `int  ref_thickness = 0;` (25), `bool startq2d      = false;` (26). |
| 28–53 | 생성자는 `max_ref_lvl`·`initial_tstep`·`epsilon`·`wall_height`를 읽는다(28–36). `if ( read_keyword_bool(input_filename, "hwfv1", 5) )` (38)이면 solver_type=HWFV1, `this->CFL         = C(0.5);` (41). `else if ( read_keyword_bool(input_filename, "mwdg2", 5) )` (43)이면 solver_type=MWDG2, `this->CFL         = C(0.3);` (46). `else` (48)에서는 오류 출력 후 `exit(-1)` (50–51). CFL은 Courant–Friedrichs–Lewy 계수다. |
| 54–73 | 시작 시 28행 생성자 안. grading·limitslopes 키를 읽는다(54–56). `if (this->limitslopes)` (58)이면 `tol_Krivo`를 읽는다(60). refine_wall 키를 읽고(63), `if (this->refine_wall)` (65)이면 `ref_thickness`를 읽는다(67). 마지막으로 startq2d 키를 읽고 생성자와 구조체를 닫는다(70–73). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 38–46: hwfv1 검사가 mwdg2 검사보다 앞선 if/else if 구조다. 두 키가 함께 존재할 때 두 번째 검사는 첫 번째 조건이 거짓일 때만 실행된다.
- 33–36·54–70: 판독 값의 범위 검사를 이 생성자 내부에서 추가로 수행하는 문장은 없다.
