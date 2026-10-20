---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/input/read_command_line_params.cpp
lines: 48
sha256: 9f104fbf18e4fdf80194af6d5ef530f05ad6813bb9c926a6dca10a28fe7520d0
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# read_command_line_params.cpp — 판독 구간 기록

구간은 1행부터 48행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | 자기 헤더를 포함한다(1). 함수는 argc·argv와 모의/해법/출력 매개변수 참조를 받는다(3–10). 전처리 조건 분기는 없다. `for (int i = 0; i < argc - 1; i++)` (12) 안에서 flag에 argv[i]를 복사한다(14). `char* value = argv[i+1];` (15). `if ( !strncmp(flag, "-epsilon", 8) )` (17)이면 sscanf로 epsilon을 읽는다(19). |
| 21–38 | 시작 시 3행 함수·12행 for 안. `else if ( !strncmp(flag, "-solver", 7) )` (21) 분기의 `if ( !strncmp(value, "hwfv1", 5) )` (23)이면 solver_type=HWFV1(25), `solver_params.CFL         = C(0.5);` (26). `else if ( !strncmp(value, "mwdg2", 5) )` (28)이면 solver_type=MWDG2(30), `solver_params.CFL         = C(0.3);` (31). `else` (33)에서는 오류를 출력하고 exit(-1)한다(35–36). -solver 분기를 닫는다(38). CFL은 Courant–Friedrichs–Lewy 계수다. |
| 39–48 | 시작 시 3행 함수·12행 for 안. `else if ( !strncmp(flag, "-dirroot", 8) )` (39)이면 `int j = 0; while (plot_params.dirroot[j] != '\0') { plot_params.dirroot[j] = '\0'; j++; }` (41)로 기존 출력 디렉터리(directory) 문자열을 널 문자로 비운다. sscanf로 새 dirroot를 읽고(43) plot_params.make_output_directory()를 호출한다(45). 분기·for·함수를 닫는다(46–48). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 7: sim_params는 인수로 받지만 이 함수 본문에서 참조하지 않는다.
- 12–15·17–45: 루프는 i=0에서 시작하며 모든 위치에 대해 다음 인자를 value로 잡는다. 옵션을 처리한 뒤 i를 추가로 증가시키는 문장은 없다.
- 17·21·23·28·39: 옵션과 해법 문자열은 지정 길이 strncmp로 비교한다. 문자열 전체 길이를 별도로 검사하지 않는다.
- 19·43: sscanf 반환값을 검사하지 않는다. dirroot를 읽는 %s에는 필드 폭이 없다.
