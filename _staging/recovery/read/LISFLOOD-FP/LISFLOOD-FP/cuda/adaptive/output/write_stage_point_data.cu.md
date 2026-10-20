---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/output/write_stage_point_data.cu
lines: 193
sha256: 1d8749ab58ee6c05ac7dfc0a921da1bf37260c5041953bec21968e2e62ad47e8
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# write_stage_point_data.cu — 판독 구간 기록

구간은 1행부터 193행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–32 | `#include "write_stage_point_data.cuh"` (1), CUDA 호스트(host) 지시 `__host__` (3), `write_stage_point_data` 정의·인수·본문 시작(4–17). 격자 차원, 해석기·출력 설정, 조립 해(assembled solution), 최세 격자, 출력 지점(stage point), 시간, 두 격자 간격, 첫 단계 여부를 받는다(6–15). `if (stage_points.num_points == 0) return;` (18)로 지점이 없으면 반환한다. `int num_finest_elems = mesh_dim * mesh_dim;` (20), `size_t bytes = sizeof(real) * num_finest_elems;` (22)로 복사량을 정한다. `copy_cuda`로 `h0`·`z0`를 호스트 `h`·`z`에 복사한다(24–25). `if (plot_params.voutput_stage)` (27) 안에서만 `qx0`·`qy0`도 복사한다(29–30). 이 파일에는 조건부 전처리 분기가 없다. |
| 33–50 | 시작 시 4–17행 `write_stage_point_data` 본문 안이며 27행 분기 밖. 길이 255의 경로 버퍼 세 개를 널 문자로 초기화한다(33–35). `sprintf` 호출 세 개는 `plot_params.dirroot`, `'/'`, `plot_params.resroot` 뒤에 `".stage"`·`".xvelocity"`·`".yvelocity"`를 붙인다(37–39). 삼항식을 포함한 연속 선언은 `FILE* fp_h  = fopen(fullpath_h,  (first_t_step) ? "w" : "a");` (41), `FILE* fp_vx = fopen(fullpath_vx, (first_t_step) ? "w" : "a");` (42), `FILE* fp_vy = fopen(fullpath_vy, (first_t_step) ? "w" : "a");` (43)다. `if (NULL == fp_h \|\| NULL == fp_vx \|\| NULL == fp_vy)` (45)이면 `__FILE__`·`__LINE__`을 오류에 출력하고 `exit(-1)`을 호출한다(47–48). |
| 51–80 | 시작 시 4–17행 `write_stage_point_data` 본문 안. `if (first_t_step)` (51) 안에서 수심 단위 m와 지점 정보 열 이름을 출력한다(53–54). `for (int point = 0; point < stage_points.num_points; point++)` (56) 안에서 `Coordinate i = get_i_index( stage_points.codes[point] );` (58), `Coordinate j = get_j_index( stage_points.codes[point] );` (59), `int idx = mesh_dim * j + i;` (61)를 계산한다. 출력 인수는 `point + 1` (71), `i * dx_finest + dx_finest / C(2.0)` (72), `j * dy_finest + dy_finest / C(2.0)` (73), `p_finest_grid.z[idx]` (74)다. `NUM_FRMT`로 좌표와 지반고를 출력한다(63–75). 루프 종료(76) 후 수심 시계열 제목과 지점 수를 쓴다(78–79). 51행 분기는 계속된다. |
| 81–132 | 시작 시 4–17행 `write_stage_point_data` 본문·51행 `if (first_t_step)` 참 분기 안. `if (plot_params.voutput_stage)` (81)이면 두 속도 파일에 단위 m/s와 지점 정보 열 이름을 쓴다(83–87). `for (int point = 0; point < stage_points.num_points; point++)` (89) 안에서 `Coordinate i = get_i_index( stage_points.codes[point] );` (91), `Coordinate j = get_j_index( stage_points.codes[point] );` (92), `int idx = mesh_dim * j + i;` (94)를 계산한다. 두 `fprintf` 호출의 계산 인수는 각각 `point + 1` (104·118), `i * dx_finest + dx_finest / C(2.0)` (105·119), `j * dy_finest + dy_finest / C(2.0)` (106·120)이며 지반고 `p_finest_grid.z[idx]`도 쓴다(107·121). 반복문 종료 후 두 속도 시계열 제목과 지점 수를 출력한다(125–129). 81행 조건과 51행 조건을 닫고 빈 줄을 포함한다(130–132). |
| 133–156 | 시작 시 4–17행 `write_stage_point_data` 본문 안이며 51행 조건 밖. 현재 시간을 수심 파일에 출력한다(133). `if (plot_params.voutput_stage)` (135)이면 두 속도 파일에도 시간을 출력한다(137–138). `for (int point = 0; point < stage_points.num_points; point++)` (141) 안에서 `Coordinate i = get_i_index( stage_points.codes[point] );` (143), `Coordinate j = get_j_index( stage_points.codes[point] );` (144), `int idx = j * mesh_dim + i;` (146)를 계산한다. 수심 출력 형식의 여러 줄 삼항 원문은 `( (point + 1) == stage_points.num_points )` (151), `? "%" NUM_FRMT` (152), `: "%" NUM_FRMT " ",` (153)다. 마지막 지점 뒤에는 공백을 붙이지 않으며 `p_finest_grid.h[idx]`를 쓴다(154). 반복문은 계속된다. |
| 157–180 | 시작 시 4–17행 `write_stage_point_data` 본문·141행 지점 `for` 루프 안. `if (plot_params.voutput_stage)` (157) 안에서 `real vx = (p_finest_grid.h[idx] < solver_params.tol_h) ? C(0.0) : p_finest_grid.qx[idx] / p_finest_grid.h[idx];` (159), `real vy = (p_finest_grid.h[idx] < solver_params.tol_h) ? C(0.0) : p_finest_grid.qy[idx] / p_finest_grid.h[idx];` (160)를 계산한다. x 속도 형식의 연속 삼항 원문은 `( (point + 1) == stage_points.num_points )` (165), `? "%" NUM_FRMT` (166), `: "%" NUM_FRMT " ",` (167)이며 `vx`를 출력한다(168). y 속도 형식은 `( (point + 1) == stage_points.num_points )` (174), `? "%" NUM_FRMT` (175), `: "%" NUM_FRMT " ",` (176)이며 `vy`를 출력한다(177). 속도 조건과 지점 루프를 닫는다(179–180). |
| 181–193 | 시작 시 4–17행 `write_stage_point_data` 본문 안이며 141행 반복문 밖. 수심 파일에 줄바꿈을 쓴다(182). `if (plot_params.voutput_stage)` (184) 안에서 두 속도 파일에도 줄바꿈을 쓴다(186–187). 이 분기 밖에서 `fclose(fp_h)`, `fclose(fp_vx)`, `fclose(fp_vy)`를 모두 호출한다(190–192). 루틴 종료와 빈 줄도 포함된다(181·183·189·193). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 27–31·41–45·135–139·157–179·190–192: 속도 배열 복사와 속도 데이터 출력은 `plot_params.voutput_stage` 조건 안에 있다. 세 파일의 열기·열기 실패 검사·닫기는 이 조건 밖에 있다.
- 71–74·104–107·118–121: 지점 헤더의 좌표는 격자 인덱스와 격자 간격으로 계산된다. 이 좌표 출력식에는 별도의 원점 좌표를 더하는 항이 없다.
- 33–39: 경로 버퍼 세 개의 크기는 각각 255로 고정되어 있다. 경로 작성에는 `sprintf`를 사용한다. 이 함수에는 경로 길이 검사문이 없다.
