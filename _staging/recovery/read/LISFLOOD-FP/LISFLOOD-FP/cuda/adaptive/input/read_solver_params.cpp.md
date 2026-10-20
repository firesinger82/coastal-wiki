---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/input/read_solver_params.cpp
lines: 50
sha256: 77b4e89d5a615463ed00fb5a22f1eb06e82d2884f79b85cb566920e5319272dc
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# read_solver_params.cpp — 판독 구간 기록

구간은 1행부터 50행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | 헤더 포함과 read_solver_params 정의이다(1–7). SolverParams를 생성한 뒤 최대 세분화 수준·초기 시간 간격·epsilon·벽 높이를 정수/실수 키 판독 루틴으로 읽는다(8–13). 이 파일에는 이 네 입력값의 별도 범위 검사나 조건부 전처리 분기가 없다. 원문: `solver_params.L             = read_keyword_int (input_filename, "max_ref_lvl", 11);` (10); `solver_params.initial_tstep = read_keyword_real(input_filename, "initial_tstep", 13);` (11); `solver_params.epsilon       = read_keyword_real(input_filename, "epsilon", 7);` (12); `solver_params.wall_height   = read_keyword_real(input_filename, "wall_height", 11);` (13). |
| 15–30 | 시작 시 3행 read_solver_params 루틴 안. hwfv1 키가 참이면 HWFV1과 CFL=C(0.5)를 선택한다(15–19). 앞 조건이 거짓이고 mwdg2 키가 참이면 MWDG2와 CFL=C(0.3)를 선택한다(20–24). else는 오류 출력과 exit(-1)을 실행한다(25–29). CFL은 Courant 수(Courant number) 필드이다. 원문: `if ( read_keyword_bool(input_filename, "hwfv1", 5) )` (15); `{` (16); `solver_params.solver_type = HWFV1;` (17); `solver_params.CFL         = C(0.5);` (18); `else if ( read_keyword_bool(input_filename, "mwdg2", 5) )` (20); `{` (21); `solver_params.solver_type = MWDG2;` (22); `solver_params.CFL         = C(0.3);` (23); `else` (25). |
| 31–50 | 시작 시 3행 read_solver_params 루틴 안이며 솔버(solver) 선택 분기 밖이다. grading과 limitslopes를 읽고, limitslopes가 참일 때 tol_Krivo를 읽는다(31–38). refine_wall을 읽고 참이면 ref_thickness를 읽는다(40–45). startq2d를 읽고 구조체를 반환한다(47–50). 원문: `solver_params.grading = read_keyword_bool(input_filename, "grading", 7);` (31); `solver_params.limitslopes = read_keyword_bool(input_filename, "limitslopes", 11);` (33); `if (solver_params.limitslopes)` (35); `solver_params.tol_Krivo = read_keyword_real(input_filename, "tol_Krivo", 9);` (37); `solver_params.refine_wall = read_keyword_bool(input_filename, "refine_wall", 11);` (40); `if (solver_params.refine_wall)` (42); `solver_params.ref_thickness = read_keyword_int(input_filename, "ref_thickness", 13);` (44); `solver_params.startq2d = read_keyword_bool(input_filename, "startq2d", 8);` (47). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 15–24: hwfv1 검사가 mwdg2 검사보다 먼저 실행되는 if/else if 구조이다. hwfv1이 참이면 mwdg2 검사는 실행하지 않는다.
- 35–45: tol_Krivo와 ref_thickness는 각각 limitslopes와 refine_wall이 참일 때만 이 루틴에서 대입한다. 생성자 내부 기본값은 이 파일에서 정의하지 않는다.
