---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/output/write_soln_vtk.cu
lines: 222
sha256: cb26197945dc5307dd6deae85bc1dc638eb4ab73cbd8892972e94f984390b0c9
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# write_soln_vtk.cu — 판독 구간 기록

구간은 1행부터 222행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–40 | `#include "write_soln_vtk.cuh"` (1), CUDA 호스트(host) 지시가 붙은 `__host__ void write_soln_vtk` 정의(3–14). 출력 설정, 조립 해(assembled solution), `d_dt_CFL`, 최세 격자 간격 두 개, 모의·해석기 설정, 저장 간격을 받는다(5–12). 255바이트 경로 버퍼를 초기화한다(15). 원문 경로 작성은 `sprintf(fullpath, "%s%c%s%c%d%s", plot_params.dirroot, '/', plot_params.resroot, '-', saveint.count - 1, ".vtk");` (17)다. `fopen(fullpath, "w")` (19) 뒤 `if (NULL == fp)` (21)이면 `__FILE__`·`__LINE__`을 오류 출력에 쓰고 `exit(-1)`을 호출한다(23–24). 시작 로그(27)와 VTK 3.0·ASCII·`UNSTRUCTURED_GRID`·`POINTS %d float` 헤더를 쓴다(29–39). 점 수 식은 `d_assem_sol.length * 4` (38)다. 이 파일에는 조건부 전처리 분기가 없다. |
| 41–69 | 시작 시 3–14행 `write_soln_vtk` 본문 안이며 21행 오류 분기 밖. 모턴 부호(Morton code)의 원점이 0이라는 주석(41–43) 뒤 `real xmax_0_orig = sim_params.xsz * dx_finest;` (44), `real ymax_0_orig = sim_params.ysz * dx_finest;` (45)를 계산한다. 길이가 `d_assem_sol.length`인 호스트 배열 `h`·`qx`·`qy`·`z`·`dt`·`act_idcs`·`levels`를 할당한다(47–53). 복사 크기 식은 `size_t bytes_flow     = d_assem_sol.length * sizeof(real);` (55), `size_t bytes_act_idcs = d_assem_sol.length * sizeof(HierarchyIndex);` (56), `size_t bytes_levels   = d_assem_sol.length * sizeof(int);` (57)다. `copy_cuda`를 일곱 번 호출해 `h0`·`qx0`·`qy0`·`z0`·`d_dt_CFL`·활성 인덱스·수준을 복사한다(59–65). 확장 영역 제외 셀 수라는 주석 뒤 `num_bound`를 0으로 초기화한다(67–68). |
| 70–91 | 시작 시 3–14행 `write_soln_vtk` 본문 안. `for (int i = 0; i < d_assem_sol.length; i++)` (70) 안에서 활성 인덱스와 수준을 가져온다(72–73). `MortonCode code = act_idx - get_lvl_idx(level);` (75), `real local_cell_size_x = dx_finest * ( 1 << (solver_params.L - level) );` (77), `real local_cell_size_y = dy_finest * ( 1 << (solver_params.L - level) );` (78)를 계산한다. 좌표 복원식은 `Coordinate x = compact(code);` (80), `Coordinate y = compact(code >> 1);` (81)다. 중심 좌표는 `real x_centre = x * local_cell_size_x + local_cell_size_x / C(2.0);` (83), `real y_centre = y * local_cell_size_y + local_cell_size_y / C(2.0);` (84)다. 경계 조건 대입은 `bool bound = (x_centre < xmax_0_orig && y_centre < ymax_0_orig);` (86)다. `//if (!bound) continue;` (88)는 주석이다. `num_bound++;` (90)을 실행한다. |
| 92–117 | 시작 시 3–14행 `write_soln_vtk` 본문·70행 `for` 루프 안. 꼭짓점 초기화의 연속 원문은 `Points points =` (92), `{` (93), `sim_params.xmin + x * local_cell_size_x,       // lower left  x` (94), `sim_params.ymin + y * local_cell_size_y,       // lower left  y` (95), `sim_params.xmin + x * local_cell_size_x,       // upper left  x` (96), `sim_params.ymin + (y + 1) * local_cell_size_y, // upper left  y` (97), `sim_params.xmin + (x + 1) * local_cell_size_x, // lower right x` (98), `sim_params.ymin + y * local_cell_size_y,       // lower right y` (99), `sim_params.xmin + (x + 1) * local_cell_size_x, // upper right x` (100), `sim_params.ymin + (y + 1) * local_cell_size_y  // upper right y` (101), `};` (102)다. `fprintf`는 `NUM_FRMT`로 왼쪽 아래·왼쪽 위·오른쪽 아래·오른쪽 위 좌표를 순서대로 쓴다(104–115). 각 점의 세 번째 좌표는 `C(1.0)`이다(111–114). 루프 종료와 빈 줄을 포함한다(116–117). |
| 118–148 | 시작 시 3–14행 `write_soln_vtk` 본문 안이며 70행 루프 밖. `fprintf(fp, "\nCELLS %d %d\n", d_assem_sol.length, d_assem_sol.length * 5);` (118)로 셀 헤더를 쓴다. `for (int i = 0; i < d_assem_sol.length; i++)` (120)에서 `int pt_ctr = i * 4;` (123), `fprintf(fp, "4 %d %d %d %d\n", 0 + pt_ctr, 1 + pt_ctr, 2 + pt_ctr, 3 + pt_ctr);` (125)로 연결을 쓴다. `CELL_TYPES` 헤더(128) 뒤 `for (int i = 0; i < d_assem_sol.length; i++)` (130)에서 셀 유형 상수 8을 쓴다(132). `CELL_DATA` 헤더(135), `SCALARS dt float 1`·`LOOKUP_TABLE default` (137–142) 뒤 `for (int i = 0; i < d_assem_sol.length; i++)` (144)에서 `dt[i]`를 출력한다(146). |
| 149–188 | 시작 시 3–14행 `write_soln_vtk` 본문 안이며 앞 반복문 밖. `h` 스칼라(scalar) 헤더와 기본 조회표를 출력한다(149–154). `for (int i = 0; i < d_assem_sol.length; i++)` (156)에서 `h[i]`를 쓴다(158). `qx` 헤더(161–166) 뒤 `for (int i = 0; i < d_assem_sol.length; i++)` (168)에서 삼항식 `real vx = (h[i] < solver_params.tol_h) ? C(0.0) : qx[i] / h[i];` (170)을 계산한다. 출력 값은 `qx[i]`다(172). `qy` 헤더(175–180) 뒤 `for (int i = 0; i < d_assem_sol.length; i++)` (182)에서 `real vy = (h[i] < solver_params.tol_h) ? C(0.0) : qy[i] / h[i];` (184)를 계산한다. 출력 값은 `qy[i]`다(186). 빈 줄도 포함된다. |
| 189–222 | 시작 시 3–14행 `write_soln_vtk` 본문 안이며 앞 반복문 밖. `z` 스칼라(scalar) 헤더와 기본 조회표를 쓴다(189–194). `for (int i = 0; i < d_assem_sol.length; i++)` (196)에서 `z[i]`를 출력한다(198). `eta` 헤더와 기본 조회표(201–206) 뒤 `for (int i = 0; i < d_assem_sol.length; i++)` (208)에서 `fprintf( fp, "%" NUM_FRMT "\n", h[i] + z[i] );` (210)로 수면 높이를 쓴다. `fclose(fp)`를 호출한다(213). 할당한 일곱 배열을 `delete[]`로 해제하고 루틴을 닫는다(215–222). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 9·44–45·77–78: 인수 `dy_finest`는 지역 y 셀 크기 계산에 사용된다. 원점 0 기준 y 경계 `ymax_0_orig`는 `sim_params.ysz * dx_finest`로 계산된다.
- 67–90·118·128·135: `bound`를 계산하지만 이를 참조하는 `if (!bound) continue;`는 주석 처리되어 있다. `num_bound`는 증가 후 참조되지 않는다. 셀 수 헤더들은 `d_assem_sol.length`를 사용한다.
- 168–186: `vx`·`vy`는 삼항식으로 계산한 뒤 참조되지 않는다. 두 출력문은 `qx[i]`·`qy[i]`를 기록한다.
- 111–114·189–210: 모든 꼭짓점의 세 번째 좌표는 `C(1.0)`으로 고정되어 있다. 배열 `z`와 수면 높이 식 `h[i] + z[i]`는 별도 셀 데이터로 기록된다.
- 15·17: 경로 버퍼 크기는 255로 고정되어 있다. 경로 작성에는 `sprintf`를 사용한다. 이 함수에는 경로 길이 검사문이 없다.
