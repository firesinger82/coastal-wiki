---
file: models/ADCIRC/raw/source_code/adcirc/util/hstime.F
lines: 139
sha256: 1e87d420af5ab1f44add24c0c2ecc21b13f9842c578ca1f1313721b61bfe1f6a
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# hstime.F — 판독 구간 기록

구간은 1행부터 139행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–27 | ADCIRC 명칭·저작권·LGPL 3 이상·무보증 머리말(1–19).바이너리(binary) hotstart 파일에서 시각을 읽어 표준 출력에 쓰는 프로그램이라는 주석과 작성·NetCDF 지원 갱신 이력(20–26).빈 줄(27). |
| 28–52 | hstime 프로그램과 implicit none(28–29).`#ifdef ADCNETCDF` (30) 안에서 netcdf.inc를 포함하고 상태·파일·차원·변수 식별자, 시각 개수 및 real(8) allocatable times를 선언한다(31–38).명령행 카운터, 길이 2048의 인수·파일명, 파일 존재·오류·형식 플래그, real(8) timeHSF를 선언한다(39–48).netCDFFormat/fileFound를 false로 초기화한다(50–51).주석(52). |
| 53–85 | 시작 시 28행 hstime 프로그램 안.`DO WHILE (i < argCount)` (55)에서 i를 증가시키고 GET_COMMAND_ARGUMENT로 인수를 받는다.`SELECT CASE(cmdLineArg(1:2))` (58)의 `CASE("-n")` (59)은 netCDFFormat=true로 설정한다.`#ifndef ADCNETCDF` (61)이면 오류를 장치 0에 쓰고 장치 6에 'null'을 출력한 뒤 STOP이다(62–67).`CASE("-f")` (68)는 다음 인수를 fileName으로 받는다(69–70).`CASE DEFAULT` (71)는 미인식 오류·'null' 출력 후 stop이다.INQUIRE 뒤 `IF (fileFound.eqv..false.) THEN` (80)이면 파일 없음 오류·'null' 출력 후 STOP이다(81–84). |
| 86–111 | 시작 시 28행 hstime 프로그램 안.`IF (netCDFFormat.eqv..true.) THEN` (87), `#ifdef ADCNETCDF` (88)에서 nf_open(NF_NOWRITE)·nf_inq_unlimdim·nf_inq_dimlen으로 파일과 무제한 차원(unlimited dimension)의 길이를 얻는다(89–94).각 호출 뒤 check_err를 호출한다.`if (timesLen.eq.0) then` (96)이면 'null' 출력·close(99)·데이터 없음 오류 출력·stop이다(97–101).times(timesLen)를 할당하고 nf_inq_varid로 "time" 변수를 찾는다(103–105).`iret = nf_get_vara_double(ncid,varid,1,timesLen,times)` (106) 뒤 check_err를 호출한다(107).마지막 times(timesLen)를 출력하고 nf_close 및 check_err를 호출한다(108–110).전처리 종료(111). |
| 112–127 | 시작 시 28행 hstime 프로그램·87행 NetCDF 조건의 분기 경계.`ELSE` (112)는 장치 99에 ACCESS='DIRECT'·RECL=8·ACTION='READ'·STATUS='OLD'로 파일을 연다(113–114).`IF (errorIO.gt.0) THEN` (115)이면 오류·'null' 출력 후 STOP이다(116–119).IHOTSTP=3으로 설정하고 REC=IHOTSTP의 TIMEHSF를 읽어 출력한다(121–123).장치 99 close·분기 종료·프로그램 종료·주석(124–127). |
| 128–139 | `#ifdef ADCNETCDF` (128) 안의 check_err(iret) 루틴과 netcdf.inc 포함·인수 선언(129–132).`if (iret .ne. NF_NOERR) then` (133)이면 nf_strerror(iret)를 장치 0에 출력하고 'null'을 장치 6에 출력한 뒤 stop이다(134–136).분기·루틴·전처리 종료(137–139). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 46·53–79: fileName 선언에는 초기값이 없다.파일명 대입은 "-f" 분기 안에 있다.INQUIRE 전에 "-f" 지정 여부를 확인하는 분기는 없다.
- 58–70: 옵션 비교는 명령행 인수의 처음 두 문자만 사용한다."-f" 다음 인수를 받기 전에 남은 인수 개수를 확인하는 문장은 없다.
- 89–101: NetCDF 데이터가 없는 분기에서는 close(99)를 호출한다.이 분기에 nf_close(ncid) 호출은 없다.
- 113–123: 바이너리 판독은 RECL=8과 레코드 3으로 고정되어 있다.파일 버전을 읽거나 이 레코드 위치를 선택하는 분기는 없다.
- 115–123: open의 IOSTAT는 검사한다.TIMEHSF read에는 IOSTAT·ERR·END 지정이 없다.
