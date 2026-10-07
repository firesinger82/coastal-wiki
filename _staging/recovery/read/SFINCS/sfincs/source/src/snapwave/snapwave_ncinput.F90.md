---
file: models/SFINCS/raw/source_code/sfincs/source/src/snapwave/snapwave_ncinput.F90
lines: 119
sha256: 4dcb45b8e16569fa3ff06ac51b0f7ac6fabf15d958babf120716d60b0fb4e617
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# snapwave_ncinput.F90 — 판독 구간 기록

구간은 1행부터 119행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | `#define NF90(nf90call) call handle_err(nf90call,__FILE__,__LINE__)` (1)로 NetCDF 호출 결과와 파일·행 정보를 handle_err에 전달한다. snapwave_ncinput 모듈은 sfincs_log와 netcdf를 사용하며 implicit none을 둔다(2–7). net_type_snapwave는 ncid, 지점·시간 차원 ID, x/y 및 time/hs/tp/wd/ds 변수 ID를 보유한다(9–15). 모듈 인스턴스 net_file_snapwave와 contains·빈 줄·주석을 포함한다(17–22). |
| 23–54 | `read_netcdf_wave_boundary_data()`는 sfincs_date, netcdf, snapwave_data를 사용한다(23–29). FEWS 형식 변수 이름을 선언한다(31–40). 상수 원문은 `character (len=256), parameter :: time_varname = 'time'` (35), `character (len=256), parameter :: hs_varname   = 'hs'` (36), `character (len=256), parameter :: tp_varname   = 'tp'` (37), `character (len=256), parameter :: wd_varname   = 'wd'` (38), `character (len=256), parameter :: ds_varname   = 'ds'` (39), `character (len=256), parameter :: units        = 'units'` (40)이다. `!   if (crsgeo) then` (42)과 lon/lat 설정·else·endif는 주석이다(42–45·48). 실행 설정은 x_varname='x', y_varname='y'이다(46–47). 로그 작성과 `call write_log(logstr, 0)` (51), 판독 시작 주석(53–54). |
| 55–73 | 시작 시 23행 read_netcdf_wave_boundary_data 루틴 안. `NF90(nf90_open(trim(netsnapwavefile), NF90_CLOBBER, net_file_snapwave%ncid))` (55)로 파일을 연다. nf90_inq_dimid로 time/stations를 찾고, nf90_inquire_dimension으로 ntwbnd/nwbnd를 얻는다(58–63). nf90_inq_varid로 x/y/time/hs/tp/wd/ds ID를 얻는다(66–72). x 좌표 ID 호출의 주석은 SnapWave 격자와 같은 UTM zone이어야 한다고 적는다(66). 각 호출은 NF90 매크로를 거친다. |
| 74–104 | 시작 시 23행 read_netcdf_wave_boundary_data 루틴 안. x_bwv/y_bwv를 nwbnd, t_bwv를 ntwbnd, hs_bwv/tp_bwv/wd_bwv/ds_bwv를 (nwbnd,ntwbnd)로 할당한다(76–82). nf90_get_var로 각 배열을 읽는다(85–91). nf90_get_att로 시간 변수의 UNITS를 treftimefews에 읽는다(94). `t_bwv = convert_fewsdate(t_bwv, ntwbnd, treftimefews, trefstr)` (97)로 sfincs_date의 시간 변환 함수를 호출한다. 시간대 주석은 UTC이다(96). `NF90(nf90_close(net_file_snapwave%ncid))` (99), 루틴 종료·빈 줄(100–104). |
| 105–119 | 구분 주석 뒤 `handle_err(status,file,line)`이 시작한다(105–106). 입력 status/file/line과 지역 status2를 선언한다(108–111). `if(status /= nf90_noerr) then` (113)이면 `write(0,'("NETCDF ERROR: ",a,i6,":",a)') file,line,trim(nf90_strerror(status))` (115)로 파일·행·오류문을 출력한다. 주석은 unit 6=stdout, unit 0=stderr이다(114). 조건·루틴·모듈 종료(116–119). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 42–48: crsgeo 분기와 lon/lat 설정은 주석 처리되어 있다. 실행 코드의 좌표 변수 이름은 항상 x/y이다.
- 55: nf90_open 호출의 mode 인수는 NF90_CLOBBER이다. 이 파일에는 mode를 바꾸는 조건이 없다.
- 76–97: 이 루틴은 좌표·시각·hs/tp/wd/ds만 할당하고 읽는다. zs_bwv와 IG 경계 배열을 읽는 실행문은 없다.
- 106–117: handle_err는 오류가 나면 stderr에 출력하고 반환한다. 이 루틴에는 stop이나 오류 전달용 반환값이 없다. status2는 선언 이후 사용되지 않는다(111).
