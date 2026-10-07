---
file: models/SFINCS/raw/source_code/sfincs/source/src/sfincs_obspoints.f90
lines: 144
sha256: 2c21880be87a387929f56c1e6b6cd42f3ce907db6e9d5d05e9bd7bdff71760f4
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# sfincs_obspoints.f90 — 판독 구간 기록

구간은 1행부터 144행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–30 | sfincs_obspoints 모듈과 contains(1–3), `read_obs_points()` 시작(5). 관측 파일 판독 주석과 sfincs_data/log/error·quadtree 사용을 포함한다(7–12). 좌표·임시 실수, 관측·격자·문자열 인덱스와 stat, logical ok, 길이 256의 line/line2, allocatable value를 선언한다(14–25). 관측 수 nobs를 0으로 초기화한다(29). |
| 31–64 | 시작 시 5행 read_obs_points 루틴 안. `if (obsfile(1:4) /= 'none') then` (31)에서 시작 로그·write_log 호출(33–34), `ok = check_file_exists(obsfile, 'Observation points obs file', .true.)` (36)을 수행한다. 유닛 500으로 파일을 열고 `do while(.true.)` (39)에서 iostat=stat로 dummy를 읽는다(40). `if (stat<0) exit` (41)로 종료하며 `nobs = nobs + 1` (42)로 수를 센다. rewind 후 좌표·관측값·격자 대응·ID·이름·격자 좌표·바닥고·바람 대응 배열을 모두 nobs 크기로 할당한다(44–58). value는 크기 2로 할당하고 두 값을 0으로 초기화한다(60–63). |
| 65–91 | 시작 시 5행 루틴·31행 관측 파일 조건 안. `do n = 1, nobs` (65)에서 한 줄을 문자열로 읽는다(67). `j1=index(line,"'")` (68), `jdq=index(line,'"')` (69)로 인용부호 위치를 찾는다. `if (j1 == 0 .and. jdq==0) then! no name supplied, give standard name` (70)이면 `j2 = 11` (71), 빈 이름 설정(72), station_과 I0.3 관측 번호로 이름을 쓴다(73). `elseif (j1>0) then ! name supplied,` (74)이면 `line2 = adjustl(trim(line(j1+1:256)))` (75), `j2=index(line2,"'")` (76), `nameobs(n) = adjustl(trim(line2(1:j2-1)))` (77)로 작은따옴표 이름을 얻는다. `else` (78)는 `line2 = adjustl(trim(line(jdq+1:256)))` (79), `j2=index(line2,'"')` (80), `nameobs(n) = adjustl(trim(line2(1:j2-1)))` (81)로 큰따옴표 이름을 얻는다. 조건 밖에서 value의 두 수를 내부 read하고 xobs/yobs에 복사한다(84–86). 루프 종료·파일 close를 포함한다(88–90). |
| 92–126 | 시작 시 5행 루틴·31행 관측 파일 조건 안. `do iobs = 1, nobs` (94)에서 nmindobs/mindobs/nindobs=0, idobs=iobs로 초기화한다(96–99). 기본 격자 좌표·바닥고는 `xgobs(iobs)    = -999.0` (100), `ygobs(iobs)    = -999.0` (101), `zbobs(iobs)    = -999.0` (102)이다. `nmq = find_quadtree_cell(xobs(iobs), yobs(iobs))` (104)로 셀을 찾는다. `if (nmq>0) then` (106)에서 SFINCS 셀 대응을 얻는다(108). 내부 `if (nm > 0) then` (110)이면 관측 셀 번호·n/m·격자 좌표를 채운다(112–117). `if (subgrid) then` (119)은 바닥고를 subgrid_z_zmin에서 복사한다(120). `else` (121)는 zb에서 복사한다(122). subgrid 조건 밖에서 세분화 수준 iref를 얻고 nm 조건을 닫는다(125–126). |
| 127–144 | 시작 시 5행 루틴·31행 관측 파일 조건·94행 iobs 루프·106행 nmq 양수 조건 안. nm 조건 밖에서 이름·nm/n/m/iref·바닥고를 로그로 쓴다(128–129). `else` (131)는 nmq 조건의 불성립 경로이며 모델 영역 밖 경고와 write_log 호출을 수행한다(133–134). nmq 조건·관측 루프·파일 조건·루틴·모듈 종료와 사이 주석을 포함한다(136–144). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 39–43: 관측 수 계산은 stat<0일 때만 종료한다. stat>0에 대한 별도 조건은 이 루프에 없다.
- 68–81: 이름 판독은 여는 인용부호를 검사한다. 닫는 인용부호 검색 결과 j2가 0인지 검사하는 조건은 문자열 슬라이스 앞에 없다.
- 96–125·128: n/m/iref 대입은 nm>0 조건 안에 있다. 이 세 변수를 포함하는 로그는 nm>0 조건 밖이며 nmq>0 조건 안에 있다.
- 47–51·58·96–98·142: zobs/hobs/nmwindobs는 이 루틴에서 할당되지만 값 대입은 없다. mindobs/nindobs에는 0 대입만 있고 찾은 n/m을 복사하는 문장은 없다.
- 16·36·142: xtmp/ytmp/di1/dj1은 선언 이후 이 루틴에서 사용되지 않는다. check_file_exists 결과 ok는 받지만 이후 조건이나 실행식에서 참조하지 않는다.
