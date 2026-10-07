---
file: models/SFINCS/raw/source_code/sfincs/source/src/sfincs_spiderweb.f90
lines: 486
sha256: 2efdb9665b61d02362530d1e927d839d401c82eb28d6df4e447d211fd3cdae65
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# sfincs_spiderweb.f90 — 판독 구간 기록

구간은 1행부터 486행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–40 | `sfincs_spiderweb` 모듈은 sfincs_log·sfincs_read를 사용한다(1–6). `read_spw_file`은 파일명, nt·nrows·ncols, spwrad, nquant, 기준시각 trefstr를 받는다(8–39). time·xe·ye는 nt 크기의 real*4 출력이다(33–35). vmag·vdir·pdrp·prcp는 (nt,nrows,ncols) 크기의 real*4 출력이다(36–39). 정수·문자열 선언, 빈 줄과 구분 주석을 포함한다. |
| 41–81 | 시작 시 8행 read_spw_file 루틴 안. 네 기상 배열을 0으로 초기화한다(41–44). 파일을 장치 번호 888로 연다(48). nheader=0으로 시작하여 `do ip = 1, 30     !read first 30 lines to find first TIME block` (52)에서 문자열을 읽는다. `id=index(line,'TIME')` (55), `if (id == 1) then` (57), `nheader = ip - 1` (58) 뒤 exit한다. 루프 밖 `if (nheader ==0) then !in case not possible to find header` (63) 안에서 `if (nquant==4) then` (65)이면 `nheader = 18` (66), `else` (67)이면 `nheader = 16` (68)이다. 대체 헤더 수를 write_log로 기록한다(71–72). rewind 후 1..nheader의 행을 읽어 건너뛴다(76–80). |
| 82–132 | 시작 시 8행 read_spw_file 루틴 안. `do it = 1, nt` (82)에서 시간 문자열을 읽고 `compute_time_in_seconds(line,trefstr,dtsec)`를 호출한다(86–88). `time(it) = dtsec * 1.0 ! Convert to seconds w.r.t. reference time` (90)으로 저장한다. xe 판독은 `j=index(line,'=')` (95), `keystr = trim(line(1:j-1))` (96), `valstr = trim(line(j+1:j+12))` (97) 뒤 valstr를 xe(it)로 읽는다(98). ye도 `j=index(line,'=')` (103), `keystr = trim(line(1:j-1))` (104), `valstr = trim(line(j+1:j+12))` (105) 뒤 읽는다(106). Peye 행은 문자열로만 읽는다(110). n=1..nrows 루프 세 개가 각각 vmag·vdir·pdrp의 m=1..ncols 값을 읽는다(112–120). `if (nquant==4) then` (122)일 때만 같은 방식으로 prcp를 읽는다(123–125). 시간 루프를 닫고 파일과 루틴을 닫는다(128–132). |
| 133–161 | 구분 주석과 AMU 판독 주석 뒤 `read_amuv_file`이 시작한다(133–135). 파일명·nt·nrows·ncols·trefstr 인수와 정수·문자열 작업변수를 선언한다(139–157). 출력 time은 nt, uv는 (nt,nrows,ncols) 크기의 real*4이다(159–160). |
| 162–194 | 시작 시 135행 read_amuv_file 루틴 안. uv를 0으로 초기화하고 장치 888로 파일을 연다(162–166). nheader=0, `do ip = 1, 30     !read first 30 lines to find first TIME block` (170), `id=index(line,'TIME')` (173), `if (id == 1) then` (175), `nheader = ip - 1 !-2 as in Hurrywave?` (176), exit 순서로 헤더를 찾는다. `if (nheader ==0) then !in case not possible to find header` (181)이면 `nheader = 13` (183)으로 설정하고 write_log를 호출한다(185–186). rewind 후 1..nheader 행을 건너뛴다(190–194). |
| 195–229 | 시작 시 135행 read_amuv_file 루틴 안. `do it = 1, nt` (196)에서 시간 문자열을 읽고 compute_time_in_seconds를 호출한다(200–202). 204–218행의 문자열 분해·날짜 차이·분 단위 변환 코드는 주석 처리되어 있다. 실행식은 `time(it) = dtsec*1.0` (219)이다. n=1..nrows 루프는 각 행의 uv(it,n,m), m=1..ncols를 읽는다(221–223). 시간 루프 종료, close, 루틴 종료와 구분 주석을 포함한다(225–229). |
| 230–257 | 빈 줄 뒤 `read_spw_dimensions`가 시작한다(231). 파일명과 nt·nrows·ncols·spwrad 출력, nquant 및 작업변수를 선언한다(235–246). 파일을 열고 `call read_int_input(888,'n_cols',ncols,0)` (252), `call read_int_input(888,'n_rows',nrows,0)` (253), `call read_int_input(888,'n_quantity',nquant,0)` (254), `call read_real_input(888,'spw_radius',spwrad,0.0)` (255)으로 차원·물리량 수·반경을 읽는다. 호출에 전달하는 기본값은 각각 0·0·0·0.0이다. 파일을 닫는다(257). |
| 258–294 | 시작 시 231행 read_spw_dimensions 루틴 안. 파일을 다시 열고 nheader=0으로 초기화한다(261–264). `do ip = 1, 30     !read first 30 lines to find first TIME block` (265), `id=index(line,'TIME')` (268), `if (id == 1) then` (270), `nheader = ip - 1 !-2 as in Hurrywave?` (271) 뒤 exit한다. `if (nheader ==0) then !in case not possible to find header` (276) 안의 `if (nquant==4) then` (278)은 `nheader = 18` (279)을 설정한다. `else` (280)는 `nheader = 16` (281)을 설정한다. write_log 호출 뒤 rewind하고 헤더 행을 건너뛴다(284–293). |
| 295–319 | 시작 시 231행 read_spw_dimensions 루틴 안. nt=0으로 시작하고 `do while(.true.)` (299)에서 iostat=stat로 한 행을 읽는다(300). `if (stat<0) exit` (301)이면 종료한다. 그렇지 않으면 `nt = nt + 1` (302), `j=index(line,'=')` (303), `keystr = trim(line(1:j-1))` (304), `valstr = trim(line(j+1:j+12))` (305)을 실행한다. cdummy로 세 행을 읽어 건너뛴다(306–308). `do ip = 1, nrows*nquant` (309)에서 자료 행을 건너뛴다(310). 루프·파일·루틴 종료와 후속 구분 주석을 포함한다(311–319). |
| 320–352 | `read_amuv_dimensions`가 시작한다(320). 파일명, nt·nrows·ncols, x_llcorner·y_llcorner·dx·dy 출력과 작업변수를 선언한다(324–338). 파일을 연다(342). `call read_int_input(888,'n_cols',ncols,0)` (344), `call read_int_input(888,'n_rows',nrows,0)` (345), `call read_int_input(888,'n_quantity',nquant,0)` (346), `call read_real_input(888,'x_llcorner',x_llcorner,0.0)` (347), `call read_real_input(888,'y_llcorner',y_llcorner,0.0)` (348), `call read_real_input(888,'dx',dx,0.0)` (349), `call read_real_input(888,'dy',dy,0.0)` (350)을 호출한다. 정수 기본 인수는 0, 실수 기본 인수는 0.0이다. 파일을 닫는다(352). |
| 353–386 | 시작 시 320행 read_amuv_dimensions 루틴 안. 파일을 다시 연다(356). nheader=0, `do ip = 1, 30     !read first 30 lines to find first TIME block` (360), `id=index(line,'TIME')` (364), `if (id == 1) then` (366), `nheader = ip - 1` (367), exit 순서로 헤더를 찾는다. `if (nheader ==0) then !in case not possible to find header` (373)이면 `nheader = 13` (375)으로 대체하고 write_log를 호출한다(377–378). rewind 후 1..nheader 행을 건너뛴다(382–386). |
| 387–409 | 시작 시 320행 read_amuv_dimensions 루틴 안. nt=0 뒤 `do while(.true.)` (392)에서 iostat=stat로 읽는다(393). `if (stat<0) exit` (394)로 종료를 검사한다. `nt = nt + 1` (395), `j=index(line,'=')` (396), `keystr = trim(line(1:j-1))` (397), `valstr = trim(line(j+1:j+12))` (398) 뒤 `do ip = 1, nrows*nquant` (399)에서 cdummy로 자료 행을 건너뛴다(400). 두 루프·파일·루틴 종료와 빈 줄을 포함한다(401–409). |
| 410–431 | `compute_time_in_seconds`는 sfincs_date를 사용한다(410–412). 임의 길이 line과 길이 15의 trefstr를 입력으로, integer*8 dtsec를 출력으로 받는다(414–416). 문자열 위치·변환계수 정수, 연월일시분초 문자 조각, 날짜·시간 문자열 및 real tim을 선언한다(418–431). |
| 432–466 | 시작 시 410행 compute_time_in_seconds 루틴 안. `j = index(line, '=')` (433), `jsince = index(line, 'since')` (435), `jsc = index(line, 'seconds')` (437), `jmn = index(line, 'minutes')` (438), `jhr = index(line, 'hours')` (439), `jdy = index(line, 'days')` (440)을 계산한다. `if (jsc > 0) then` (442)은 junit=jsc와 `ifac   = 1` (445)을 설정한다. 병렬 `elseif (jmn > 0) then` (447)은 junit=jmn과 `ifac  = 60` (450)을 설정한다. 병렬 `elseif (jhr > 0) then` (452)은 junit=jhr과 `ifac  = 3600` (455)을 설정한다. 병렬 `elseif (jdy > 0) then` (457)은 junit=jdy와 `ifac  = 86400` (460)을 설정한다. `else` (462)에는 Error 주석만 있다(464). 분기를 닫는다(466). |
| 467–486 | 시작 시 410행 compute_time_in_seconds 루틴 안이며 442행 단위 선택 분기 밖. `valstr = trim(line(j+1:junit-1))` (468)을 real tim으로 읽는다(470). `timstr = trim(line(jsince + 6 : jsince + 24))` (472)을 고정 문자 형식으로 연월일시분초에 읽는다(476). `datespw = cyspw // cmspw // cdspw // ' ' // chhspw // cmmspw // cssspw` (478)을 구성하고 `time_difference(datespw,trefstr,dtsec)`를 호출한다(480). `dtsec = tim*ifac - dtsec ! Convert to seconds w.r.t. reference time` (482)으로 기준시각 상대 초를 구한다. 루틴·모듈 종료와 빈 줄을 포함한다(484–486). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 32·41–130: read_spw_file의 spwrad 입력 인수는 선언 이후 이 루틴의 실행문에서 사용되지 않는다.
- 52–74·170–188·265–287·360–380: 네 판독 루틴은 처음 30행 안에서 행 첫 위치의 TIME을 찾는다. nheader가 0이면 SPW는 nquant=4일 때 18, 그 외 16을 사용한다. AMU/AMV 차원·자료 판독은 13을 사용한다.
- 58·63·176·181·271·276·367·373: 첫 행에서 TIME을 찾으면 nheader에 ip−1=0을 대입한다. 이후 nheader==0 검사도 같은 값 0을 사용한다.
- 95–106·303–305·396–398: keystr를 대입하지만 이후 키 이름을 검사하는 조건문은 해당 루틴에 없다. xe·ye의 값 문자열은 등호 뒤 최대 12문자 구간으로 고정한다.
- 299–312·392–402: 시간 블록 계수 루프의 종료 검사는 stat<0이다. stat>0을 검사하는 조건문은 두 루프에 없다. 후속 자료 행 read에는 iostat 인수가 없다.
- 418·442–468·482: junit·ifac 선언에는 초기값이 없다. 네 단위 문자열을 모두 찾지 못하는 else에는 주석만 있다. 그 분기 뒤 substring과 시간 변환은 junit·ifac를 사용한다.
- 435·472·476·478: since 문자열의 검색 결과를 검사하는 조건문은 없다. 날짜 문자열은 jsince+6부터 jsince+24까지 추출하고 고정 문자 형식으로 읽는다. 시간대 문자열을 판독하는 실행문은 이 루틴에 없다.
