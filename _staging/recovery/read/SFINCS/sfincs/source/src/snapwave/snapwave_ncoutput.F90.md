---
file: models/SFINCS/raw/source_code/sfincs/source/src/snapwave/snapwave_ncoutput.F90
lines: 140
sha256: 89a310a8c399643b5a308494c14c6079306ae7a55ce4b789da98934f15cb215a
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# snapwave_ncoutput.F90 — 판독 구간 기록

구간은 1행부터 140행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | `#define NF90(nf90call) call handle_err(nf90call,__FILE__,__LINE__)` (1)는 NetCDF 호출 결과와 파일명·행 번호를 handle_err에 전달한다. snapwave_ncoutput 모듈을 시작한다(2). sfincs_log·netcdf를 사용한다(4–5). implicit none·contains와 구분 주석을 둔다(3·6–10). |
| 11–29 | `write_snapwave_mesh(fname, crsgeo)`를 시작한다(11). snapwave_data를 사용한다(13). fname은 길이 256의 입력 문자열이고 crsgeo는 입력 logical이다(17–18). 파일·차원·변수 ID를 선언한다(20–25). 원문 기본값은 `integer, parameter :: nc_deflate_level = 2` (27), `real*4, parameter  :: FILL_VALUE = -99999.0` (28)이다. 주석·빈 줄을 포함한다(12·14–16·19·26·29). |
| 30–54 | 시작 시 11행 write_snapwave_mesh 안. `NF90(nf90_create(trim(fname), ior(NF90_CLOBBER, NF90_NETCDF4), ncid))` (31)로 NetCDF4 파일을 생성한다. nf90_def_dim은 노드 수 no_nodes·면 수 no_faces·면당 최대 노드 수 4를 정의한다(32–34). nf90_put_att는 Conventions·NetCDF 라이브러리 버전·Producer·build_revision·build_date·title을 기록한다(37–42). mesh2d를 스칼라 NF90_INT로 정의한다(45). topology_dimension=2와 노드 좌표·차원·면 연결 변수 이름을 속성으로 기록한다(46–53). 구분 주석을 포함한다(30·35–36·43–44·54). |
| 55–72 | 시작 시 11행 write_snapwave_mesh 안. 원문 조건은 `if (crsgeo) then` (55)이다. 참 분기는 mesh2d_node_x·mesh2d_node_y를 NF90_FLOAT의 노드 차원 변수로 정의한다(57·65). nf90_def_var_deflate는 shuffle=1·deflate=1·level=nc_deflate_level을 설정한다(58·66). nf90_put_att는 단위 degrees, standard_name·long_name으로 longitude 또는 latitude, mesh=mesh2d, location=node를 기록한다(59–63·67–71). 구분 주석을 포함한다(56·64·72). |
| 73–92 | 시작 시 11행 write_snapwave_mesh·55행 crsgeo 조건 안. `else` (73)는 crsgeo 불성립 분기이다. mesh2d_node_x·mesh2d_node_y를 NF90_DOUBLE로 정의한다(75·83). nf90_def_var_deflate를 같은 설정으로 호출한다(76·84). nf90_put_att는 단위 m, standard_name으로 projection_x_coordinate 또는 projection_y_coordinate, 좌표 설명·mesh=mesh2d·location=node를 기록한다(77–81·85–89). 조건을 종료한다(91). 주석을 포함한다(74·82·90·92). |
| 93–111 | 시작 시 11행 write_snapwave_mesh 안이며 crsgeo 조건 밖. nf90_def_var는 mesh2d_face_nodes를 NF90_INT의 (최대 면 노드 수, 면 수) 변수로 정의한다(93). 압축 설정 뒤 연결 역할·mesh·location=face·반시계방향 노드 매핑 설명·start_index=1·_FillValue=-999를 기록한다(94–100). crs를 스칼라 NF90_INT로 정의하고 EPSG 속성에 문자열 '-'를 기록한다(102–103). mesh2d_node_z를 NF90_FLOAT의 노드 차원 변수로 정의한다(105). 압축·_FillValue=FILL_VALUE·단위 m·standard_name=altitude·long_name=bed_level_above_reference_level을 기록한다(106–110). 구분 주석을 포함한다(101·104·111). |
| 112–126 | 시작 시 11행 write_snapwave_mesh 안. nf90_enddef로 정의 모드를 끝낸다(112). nf90_put_var는 x·y·face_nodes·zb를 각각 좌표·연결·바닥고 변수에 기록한다(115–118). nf90_close로 파일을 닫는다(121). 루틴을 종료한다(123). 주석·빈 줄·다음 루틴 구분선을 포함한다(113–114·119–120·122·124–126). |
| 127–140 | `handle_err(status,file,line)`을 시작한다(127). 입력 status·file·line과 지역 정수 status2를 선언한다(129–132). 원문 조건은 `if(status /= nf90_noerr) then` (134)이다. 참이면 nf90_strerror(status)를 사용하여 파일명·행 번호·오류 문자열을 unit 0에 출력한다(136). 주석은 unit 6을 stdout, unit 0을 stderr라고 적는다(135). 조건·루틴·모듈을 종료한다(137–140). 주석·빈 줄을 포함한다(128·133·139). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 37: Conventions 속성의 값은 `"Conventions = 'CF-1.8 UGRID-1.0 Deltares-0.10'"`이다. 값 문자열에도 Conventions라는 이름과 등호가 들어 있다.
- 102–103·115–118: crs를 정의하고 EPSG 속성에 '-'를 넣는다. 변수 기록 블록에는 crs의 값에 대한 nf90_put_var 호출이 없다.
- 57·65·75·83: 좌표 변수 정의 옆 주석은 cell centre라고 적는다. 같은 변수의 location 속성은 node이다(63·71·81·89).
- 132: status2는 선언 이후 이 파일에서 사용되지 않는다.
- 134–138: handle_err의 오류 분기는 메시지를 출력한다. 이 루틴에는 stop이나 종료 루틴 호출이 없다.
