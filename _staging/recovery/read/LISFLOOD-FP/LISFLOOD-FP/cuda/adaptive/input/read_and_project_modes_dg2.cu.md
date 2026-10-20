---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/input/read_and_project_modes_dg2.cu
lines: 107
sha256: 3b44ada31924a33e059e6feb83abe5cd419e0ec490de99b0a552c1196bd0c66e
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# read_and_project_modes_dg2.cu — 판독 구간 기록

구간은 1행부터 107행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–28 | 자기 선언 헤더를 포함한다(1). `__host__` (3)인 호스트 함수(host function) read_and_project_modes_dg2는 파일명·조립 해(assembled solution)·절점값(nodal value)·모의/해법 매개변수·격자 크기를 받는다(4–12). 전처리 조건 분기는 없다. 파일명 버퍼 4개를 널 문자로 초기화한다(14–17). read_keyword_str로 DEMfile을 읽는다(19). `if (dem_filename_buf[0] == '\0')` (22)이면 오류를 출력한다(24). startfile을 읽는다(27). |
| 29–50 | 시작 시 4행 함수 안. 조립 해 길이의 h·qx·qy·dem 호스트 배열을 값 초기화하여 할당한다(29–32). `for (int i = 0; i < d_assem_sol.length; i++)` (34) 안에서 dem[i]에 wall_height를 복사한다(36). read_raster_file로 수심과 수치표고모형(digital elevation model, DEM)을 읽는다(39–40). `if (solver_params.startq2d)` (42)이면 startfile 이름 뒤에 .Qx·.Qy를 붙이고(44–45) 두 유량 래스터(raster)를 read_raster_file로 읽는다(47–48). |
| 51–79 | 시작 시 4행 함수 안. `const int interface_dim = mesh_dim + 1;` (51), `const int interface_y   = sim_params.ysz + 1;` (52), `const int interface_x   = sim_params.xsz + 1;` (53). `real* h_interface   = new real[interface_dim * interface_dim]();` (55), `real* qx_interface  = new real[interface_dim * interface_dim]();` (56), `real* qy_interface  = new real[interface_dim * interface_dim]();` (57), `real* dem_interface = new real[interface_dim * interface_dim]();` (58)로 네 인터페이스 배열을 값 초기화하여 할당한다. `for (Coordinate y = 0; y < interface_dim; y++)` (60), `for (Coordinate x = 0; x < interface_dim; x++)` (62) 안에서 `bool wall_or_border_x = (x == interface_x - 1 \|\| x == interface_dim - 1);` (64), `bool wall_or_border_y = (y == interface_y - 1 \|\| y == interface_dim - 1);` (65). `int i = (wall_or_border_x) ? x - 1 : x;` (67), `int j = (wall_or_border_y) ? y - 1 : y;` (68)로 경계의 바로 앞 셀을 선택한다. `int interface_idx = (interface_dim - 1 - y) * interface_dim + x;` (70), `int mode_idx      = (mesh_dim      - 1 - j) * mesh_dim      + i;` (71)로 행 방향을 뒤집은 인덱스를 구한다. 네 래스터 값을 해당 인터페이스 위치에 복사하고 두 루프를 닫는다(73–78). |
| 80–107 | 시작 시 4행 함수 안. `size_t bytes = interface_dim * interface_dim * sizeof(real);` (80). copy_cuda로 h/qx/qy/dem 인터페이스 배열을 d_nodal_vals.h/qx/qy/z에 전달한다(82–85). `const int num_blocks = get_num_blocks(d_assem_sol.length, THREADS_PER_BLOCK);` (87). CUDA 커널 실행은 `modal_projections<<<num_blocks, THREADS_PER_BLOCK>>>` (89)이며 절점값·조립 해·해법 매개변수·mesh_dim·interface_dim을 전달한다(90–96). 네 래스터 배열과 네 인터페이스 배열을 delete[]로 해제하고 함수를 닫는다(98–107). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 22–25: DEM 파일명 버퍼가 비어 있으면 오류를 출력하지만 이 조건 블록에는 exit 또는 return이 없다.
- 64–68: 경계 선택은 interface_x/y - 1 또는 interface_dim - 1과 같은지로 결정한다. 이 위치에서는 바로 앞 인덱스를 사용한다.
