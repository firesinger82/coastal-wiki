---
file: models/SFINCS/raw/source_code/sfincs/source/src/sfincs_initial_conditions.F90
lines: 290
sha256: 60a739c7323fb61e59628c20e0d54642d8059f331d293307ec2744cc2e6dd801
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# sfincs_initial_conditions.F90 — 판독 구간 기록

구간은 1행부터 290행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | `sfincs_initial_conditions` 모듈 시작과 sfincs_data·sfincs_log·sfincs_error·netcdf 사용(1–6). 모듈 배열 inizs는 real*8, inizs4·iniq는 real*4 allocatable 1차원 배열(8–10). contains와 구분 주석(12–13). |
| 14–43 | `set_initial_conditions()` 시작과 sfincs_ncinput 사용, 초기 수위·유량·속도 설정 주석(14–18). implicit none, nm·nmu·ip·iuv, facint·dzuv·zmax·zmin·huv·zsuv, nchar·iok·varname 선언(20–32). inizs(np)·inizs4(np)·iniq(npuv+ncuv+1) 할당(34–36). iniq의 크기 설명은 36행 주석이다. inizs·inizs4에 zini를 복사하고 iniq=0 초기화(38–40). 입력 유형 확인 주석(42–43). |
| 44–95 | 시작 시 14행 set_initial_conditions 루틴 안. `if (rstfile(1:4) /= 'none') then` (44)이면 로그·check_file_exists 후 `call read_binary_restart_file() ! Note - older type real*4 for zs` (54). 병렬 `elseif (zsinifile(1:4) /= 'none') then` (56)은 로그·check_file_exists(58–61). 내부 `if (zsinifile(nchar - 1 : nchar) == 'nc') then` (63)이면 NetCDF·real*8 입력 주석과 로그(65–71), varname='zs'(75), `call read_netcdf_quadtree_to_sfincs_real8(zsinifile, varname, inizs) !ncfile, varname, varout)` (76). read_nc_ini_file 호출은 주석 처리(73). 내부 else(78)는 binary·real*4 입력 주석·로그 후 `call read_zsini_file()` (86). 입력 선택 else(90)는 초기 조건 미제공 주석만(92). 조건 종료·주석(94–95). |
| 96–123 | 시작 시 14행 set_initial_conditions 루틴 안. `do nm = 1, np` (98)의 `if (subgrid) then` (100)은 `zs(nm) = max(subgrid_z_zmin(nm), inizs(nm)) ! Water level at zini or bed level (whichever is higher)` (101). else(102)는 `zs(nm) = max(zb(nm), inizs(nm)) ! Water level at zini or bed level (whichever is higher)` (103). 셀 루프 종료(106). `do ip = 1, npuv` (110)에서 q(ip)=iniq(ip)(112), uv_index_z_nm·uv_index_z_nmu를 nm·nmu에 복사(117–118). `zsuv = max(zs(nm), zs(nmu)) ! water level at uv point` (120), iok=false(122). 운동량 루틴과 같은 초기 속도 방법이라는 주석(114–115). |
| 124–150 | 시작 시 14행 set_initial_conditions·110행 ip 루프 안. `if (subgrid) then` (124)에서 zmin·zmax를 subgrid_uv_zmin·subgrid_uv_zmax로 설정(126–127). `if (zsuv>zmin + huthresh) then` (129)이면 iok=true(130). subgrid else(133)는 `if (zsuv>zbuvmx(ip)) then` (135)이면 iok=true(136). 검사 종료 후 `if (iok) then` (141), `if (subgrid) then` (143), `if (zsuv>zmax - 1.0e-4) then` (145). 완전히 젖은 경로의 식은 `huv    = subgrid_uv_havg_zmax(ip) + zsuv` (149). 구분 주석(150). |
| 151–175 | 시작 시 14행 set_initial_conditions·110행 ip 루프·141행 iok 참 분기·143행 subgrid 참 분기·145행 `if (zsuv>zmax - 1.0e-4) then` 블록 안. else(151)는 이 조건이 거짓일 때의 표 보간 경로. [검증 보완: sonnet 표본] 식은 `dzuv   = (subgrid_uv_zmax(ip) - subgrid_uv_zmin(ip)) / (subgrid_nlevels - 1)` (155), `iuv    = int((zsuv - subgrid_uv_zmin(ip))/dzuv) + 1` (156), `facint = (zsuv - (subgrid_uv_zmin(ip) + (iuv - 1)*dzuv) ) / dzuv` (157), `huv    = subgrid_uv_havg(iuv, ip) + (subgrid_uv_havg(iuv + 1, ip) - subgrid_uv_havg(iuv, ip))*facint` (158). 145행 조건 밖 subgrid 경로에서 `huv    = max(huv, huthresh)` (162). 143행의 else(164)는 `huv    = max(zsuv - zbuv(ip), huthresh)` (166). subgrid 조건 밖 iok 경로에서 `uv(ip)   = max(min(q(ip)/huv, 4.0), -4.0)` (170). 속도 범위는 이 식의 -4.0..4.0이다. iok 조건·ip 루프 종료와 주석(172–175). |
| 176–182 | 시작 시 14행 set_initial_conditions 루틴 안이며 ip 루프 밖. inizs·iniq 해제(176–177). 루틴 종료(179)와 구분 주석(178·180–182). |
| 183–218 | `read_binary_restart_file()` 시작과 binary restart 주석, implicit none, integer rsttype·real*4 rdummy 선언(183–190). unit 500을 unformatted stream으로 open(192). 주석은 유형 1=zs/q/uvmean, 2=zs/q, 3=zs, 4=cnb의 scs_Se 추가, 5=gai의 GA_sigma·GA_F 추가, 6=hor의 rain_T1 추가라고 나열(194–200). rdummy·rsttype·rdummy read(202–204), 유형 로그·write_log(206–207). `if (rsttype < 1 .or. rsttype > 6) then` (209)이면 경고·write_log(213–214) 후 close(216). 유효 유형의 else는 218행에서 열린다. |
| 219–236 | 시작 시 183행 read_binary_restart_file·209행 유형 검사 else(218) 안. rdummy·inizs4·rdummy를 read(221–223). `if (rsttype==1 .or. rsttype==2 .or. rsttype==4 .or. rsttype==5 .or. rsttype==6) then` (227)이면 rdummy·iniq·rdummy를 read(228–230), 이어 rdummy·uvmean·rdummy를 read(232–234). 조건 종료와 주석(235–236). |
| 237–269 | 시작 시 183행 read_binary_restart_file·209행 유형 검사 else(218) 안. `if (rsttype==4) then ! Infiltration method cnb` (237)은 rdummy·scs_Se를 read(239–240). 241행 로그는 주석 처리. `elseif (rsttype==5) then ! Infiltration method gai` (243)는 rdummy·GA_sigma·rdummy·GA_F read(245–248), sigmafile 덮어쓰기 로그·write_log(249–250). `elseif (rsttype==6) then ! Infiltration method horton` (252)는 rdummy·rain_T1 read(254–255), fcfile 관련 로그·write_log(256–257). 침투 선택 종료(259) 후 close(261), real*4에서 real*8로 inizs=inizs4 복사(263–264). 유형 검사·루틴 종료와 주석(266–269). |
| 270–290 | `read_zsini_file()` 시작과 binary 초기 수위 주석·implicit none(270–274). 파일 로그·write_log(276–277). 279행 write_log는 v2.1.1 이하 binary와 v2.1.2+가 호환되지 않으며 real*8 수위를 담은 파일을 다시 만들라고 경고한다. unit 500을 unformatted stream으로 open하고 inizs4를 read한 뒤 close(281–283). inizs=inizs4로 real*8 배열에 복사(285–286). 루틴·모듈 종료와 주석(288–290). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 30·63: nchar는 지역 정수로 선언된다. 이 파일에는 nchar에 값을 대입하는 문장이 없다. NetCDF 확장자 검사는 nchar를 부분 문자열 인덱스로 사용한다.
- 34–36·176–179: set_initial_conditions는 inizs·inizs4·iniq를 할당한다. 루틴 끝에서는 inizs·iniq만 해제한다.
- 44·56: 초기 조건 파일 유무 검사는 파일명의 첫 네 문자만 'none'과 비교한다.
- 122–172: uv(ip) 대입은 iok 참 분기 안에 있다. iok 거짓일 때 uv(ip)를 대입하는 else는 이 루틴에 없다.
- 155–158: 표 보간은 subgrid_nlevels-1과 dzuv로 나눈다. iuv와 iuv+1을 표 인덱스로 사용한다. 이 보간 블록에는 분모 검사나 인덱스 제한문이 없다.
- 196·227–234: 유형 2의 주석은 zs·q만 나열한다. 유형 2도 iniq와 uvmean을 모두 읽는 조건에 포함된다.
- 237–255: restart의 침투 배열 read는 rsttype으로 분기한다. 이 블록에는 현재 inftype 또는 배열 할당 여부를 검사하는 조건이 없다.
- 279·282·286: binary 초기 수위 경고는 real*8 파일을 요구한다. 실행 read 대상은 real*4 배열 inizs4이다. 이후 inizs4를 real*8 배열 inizs에 복사한다.
- 6·14–288: netcdf 모듈을 가져온다. 이 파일에는 nf90 계열 직접 호출이 없다. NetCDF 수위 입력은 sfincs_ncinput의 read_netcdf_quadtree_to_sfincs_real8을 호출한다.
