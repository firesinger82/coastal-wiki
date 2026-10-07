---
file: models/SFINCS/raw/source_code/sfincs/source/src/sfincs_date.f90
lines: 373
sha256: eb72907ec5127b67ac70cb594641f12d7409678557a0cb241abf37532d287a46
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# sfincs_date.f90 — 판독 구간 기록

구간은 1행부터 373행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–64 | `sfincs_date` 모듈과 `IMPLICIT NONE`(1–4). Julian 날짜·달력 전환·천문학적 연도·Modified Julian Date·지원 연도에 관한 주석과 참고문헌 Montenbruck 및 1992 Astronomical Almanac(6–44). 주석은 day와 fraction을 두 doubles로 저장한다고 설명한다(41–44). clean 버전의 월별 일수 선언은 주석 처리되어 있다(46–49). 실행 선언은 `INTEGER, PRIVATE :: days_in_month(0:12) = (/ &` (53); `&      365, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 /)` (54). 0번 원소는 365이다. `j_date`의 day와 fraction은 각각 기본 `REAL`이다(58–61). `CONTAINS`와 빈 줄까지 포함한다(63–64). |
| 65–115 | `SetYMD(ky, km, kd, zfraction)` 함수의 인수·결과·지역변수 선언(65–75). `IF (.NOT. PRESENT(zfraction)) THEN` (77)이면 fraction=0.0, `ELSE` (79)이면 입력 fraction을 복사한다(78–81). `IF (km <= 2) THEN` (83)이면 `iy = ky-1` (84), `im = km+12` (85); `ELSE` (86)는 연·월을 그대로 복사한다(87–89). 달력 분기는 `IF (ky > 1582 .OR. (ky == 1582 .AND. km > 10 &` (91); `&        .OR. (km == 10 .AND. kd >= 15))) THEN` (92). 참이면 `ib = INT(iy/400)-INT(iy/100)` (96), `ELSE` (97)는 ib=-2(101). 날짜식은 `julian_day%day = FLOOR(365.25*iy)+INT(30.6001*(im+1))+ib+1720996.5+kd` (104). 정규화는 `zf = julian_day%day-AINT(julian_day%day)+julian_day%fraction` (106), `julian_day%day = AINT(julian_day%day)` (107). `if (zf >= 1.0) THEN` (108)이면 `julian_day%fraction = zf-AINT(zf)` (109), `julian_day%day = julian_day%day+AINT(zf)` (110); `ELSE` (111)도 `julian_day%fraction = zf-AINT(zf)` (112)를 실행한다. 조건과 함수 종료까지 포함한다(113–115). |
| 116–144 | 빈 줄과 `YMD` 서브루틴의 선언(116–123). `za = FLOOR(julian_day%day+julian_day%fraction+0.5)` (125). `IF (za < 2299161.0) THEN` (127)이면 `zc = za+1524.0` (128); `ELSE` (129)는 `zb = FLOOR((za-1867216.25)/36524.25)` (130), `zc = za+zb-FLOOR(zb/4)+1525` (131). 이어서 `zd = FLOOR((zc-122.1)/365.25)` (134), `ze = FLOOR(365.25*zd)` (135), `zf = FLOOR((zc-ze)/30.6001)` (136), `kd = INT(zc-ze- FLOOR(30.6001*zf))` (138), `km = INT(zf-1-12*FLOOR((zf+0.0001)/14))` (139), `ky = INT(zd-4715-((7+km)/10))` (140), `zfraction = (julian_day%day+0.5-za)+julian_day%fraction;` (141). 루틴 종료·빈 줄(143–144). |
| 145–182 | `YD`는 연도·일수·fraction을 출력한다(145–152). `za = FLOOR(julian_day%day+julian_day%fraction+0.5)` (154). `IF (za < 2299161.0) THEN` (156)이면 `zc = za+1524.0` (157); `ELSE` (158)는 `zb = FLOOR((za-1867216.25)/36524.25)` (159), `zc = za+zb-FLOOR(zb/4)+1525` (160). `zd = FLOOR((zc-122.1)/365.25)` (163), `ze = FLOOR(365.25*zd)` (164), `zf = FLOOR((zc-ze)/30.6001)` (165), `kd = INT(zc-ze- FLOOR(30.6001*zf))` (167), `im = INT(zf-1-12*FLOOR((zf+0.0001)/14))` (168), `ky = INT(zd-4715-((7+im)/10))` (169), `zfraction = (julian_day%day+0.5-za)+julian_day%fraction` (170). `DO i = 1, im` (172) 안의 조건은 `IF (im == 2 .AND. (MOD(ky,4) == 0 .AND. MOD(ky,100) /= 0) &` (173); `&           .OR. MOD(ky,400) == 0) THEN` (174). 참이면 `kd = kd+29` (175)와 `CYCLE` (176), 그 외에는 `kd = kd + days_in_month(i-1)` (178). 루프·루틴 종료 및 주석(179–182). |
| 183–205 | `time_difference`는 두 길이 15 문자열과 8바이트 정수 초 차이를 사용한다(183–190). 두 문자열을 `(I4,2I2,1X,3I2)`로 읽는다(192–193). `ijul1 = julian_date (yyyy1,mm1,dd1)` (197), `ijul2 = julian_date (yyyy2,mm2,dd2)` (198)로 날짜를 변환한다. `sec1  = hh1*3600 + mn1*60 + ss1` (200), `sec2  = hh2*3600 + mn2*60 + ss2` (201), `dtsec = (ijul2 - ijul1)*86400 + sec2 - sec1` (202). 루틴 종료와 주석까지 포함한다(203–205). |
| 206–216 | `julian_date` 함수와 Fliegel & Van Flandern 1968 참고문헌·1970년 예제 주석(206–209). 입력 yyyy/mm/dd와 결과 julian은 기본 정수다(210–211). 계산은 `julian = dd-32075+1461*(yyyy+4800+(mm-14)/12)/4 + &` (212); `367*(mm-2-((mm-14)/12)*12)/12- &` (213); `3*((yyyy + 4900 + (mm - 14)/12)/100)/4` (214). 함수 종료·주석(215–216). |
| 217–229 | `date_to_iso8601`의 가변 길이 입력, 길이 256 결과와 정수 날짜 필드 선언(217–220). 입력 형식 `yyyymmdd HHMMSS` 주석과 `(I4,2I2,1X,3I2)` read(221–222). write는 연·월·일 사이에 `-`, 날짜·시간 사이에 공백, 시·분·초 사이에 `:`를 넣는다(225). 주석은 DFM/FEWS에서 T 없이 사용한다고 적는다(225). T를 넣는 대체 write는 주석 처리되어 있다(226). 함수 종료·주석까지 포함한다(227–229). |
| 230–262 | `convert_fewsdate`의 길이 41 FEWS 기준 문자열, 길이 15 SFINCS 기준 문자열, 정수 날짜와 8바이트 정수 dtsec/sec1/sec2, allocatable `real*4` 입력·결과 배열 선언(230–242). SFINCS 기준을 읽는다(244). FEWS 입력은 minutes since 1970이라는 주석(246). 실제 read는 `(A14,I4,A1,I2,A1,I2,A1,I2,A1,I2,A1,I2)` 형식과 정수 tmp를 구분 필드에 사용한다(248). `ijul1 = julian_date (yyyy1,mm1,dd1)` (250), `ijul2 = julian_date (yyyy2,mm2,dd2)` (251), `sec1  = hh1*3600 + mn1*60 + ss1` (253), `sec2  = hh2*3600 + mn2*60 + ss2` (254), `dtsec = (ijul2 - ijul1)*86400 + sec2 - sec1` (255). timeout을 timent 크기로 할당한다(257). 변환식은 `timeout = real((int(timein) * 60) + dtsec)  ! time from fews is in minutes, then correct for use wrt sfincs treftime` (259). 함수 종료·주석(261–262). |
| 263–297 | `convert_spw_nc_date`는 같은 문자열·날짜 필드와 `real*4` 배열을 선언하며 dtsec만 `real*8`이다(263–276). SFINCS 기준 read(278). 입력 주석은 `days since 1970-01-01 00:00:00Z`(280). `treftimefews(12:)`를 `(I4,A1,I2,A1,I2,A1,I2,A1,I2,A1,I2)` 형식으로 읽는다(282). `ijul1 = julian_date (yyyy1,mm1,dd1)` (284), `ijul2 = julian_date (yyyy2,mm2,dd2)` (285), `sec1  = hh1*3600 + mn1*60 + ss1` (287), `sec2  = hh2*3600 + mn2*60 + ss2` (288), `dtsec = (ijul2 - ijul1)*86400.0 + sec2 - sec1` (289). timeout(timent) 할당(291), `timeout = (timein * 86400) + dtsec  ! time from spiderweb is in days` (293), sec1=0(294). 함수 종료·주석(296–297). |
| 298–328 | `time_to_string`의 길이 15 결과·기준 문자열, `real*8` t_sec, 기본 REAL 작업변수와 j_date 선언(298–305). 기준 문자열 read(309), `ref_fraction = real(hh)/24 + real(mn)/1440 + real(ss)/86400` (310), `jd = SetYMD (yyyy, mm, dd, 0.0)` (311). `sec_add = ref_fraction*86400 + t_sec` (313), `ndays_add = int(sec_add/86400)` (314), `secs_time = sec_add - ndays_add*86400.0` (315), `jd%day = jd%day + 1.0*ndays_add` (316). `call YMD(jd, yyyy, mm, dd, zfraction)` (318). `hh = int(secs_time/3600)` (319), `mn = int((secs_time - hh*3600)/60)` (320), `ss = int(secs_time - hh*3600 - mn*60)` (321). write는 `yyyymmdd.HHMMSS` 형태를 만든다(325). 함수 종료·주석(327–328). |
| 329–365 | `time_to_vector`의 기본 정수 6원소 결과와 날짜 작업변수 선언(329–337). 기준 문자열 read(341), `ref_fraction = real(hh)/24 + real(mn)/1440 + real(ss)/86400` (342), `jd = SetYMD (yyyy, mm, dd, 0.0)` (343), `sec_add = ref_fraction*86400 + t_sec` (345), `ndays_add = int(sec_add/86400)` (346), `secs_time = sec_add - ndays_add*86400.0` (347), `jd%day = jd%day + 1.0*ndays_add` (348). `call YMD(jd, yyyy, mm, dd, zfraction)` (350). `hh = int(secs_time/3600)` (351), `mn = int((secs_time - hh*3600)/60)` (352), `ss = int(secs_time - hh*3600 - mn*60)` (353). 결과 1..6에 yyyy/mm/dd/hh/mn/ss를 복사한다(357–362). 함수 종료·주석까지 포함한다(364–365). |
| 366–373 | `timer(t)`는 `real*4,intent(out)` t와 정수 count/count_rate/count_max를 선언한다(366–368). `call system_clock (count,count_rate,count_max)` (369), `t = dble(count)/count_rate` (370). 루틴 종료·주석·모듈 종료(371–373). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 41–44·58–60: 주석은 day와 fraction을 두 doubles라고 설명한다. 실제 두 필드 선언은 kind를 지정하지 않은 REAL이다.
- 91–92: 달력 조건의 괄호 안에서 `km == 10 .AND. kd >= 15`는 `ky == 1582 .AND. km > 10`과 OR로 연결되어 있다. 전자의 하위 조건에는 연도 검사가 없다.
- 53–54·172–178: days_in_month(0)은 365이다. YD의 첫 루프 반복은 days_in_month(i-1), 즉 0번 원소를 사용한다.
- 172–176: YD의 윤년 조건은 루프 변수 i 대신 im을 검사한다. `MOD(ky,400) == 0`은 im==2 부분과 OR로 연결되어 있다. 참 분기는 29를 더하고 CYCLE한다.
- 192–193·222·244·248·278·282·309·341: 이 파일의 날짜 문자열 read에는 iostat나 err 지정이 없다.
- 238·248·271·282: 구분 필드를 받는 tmp는 정수다. 대응 read 형식은 A14 또는 A1이다.
- 259: FEWS 시간 변환은 timein에 int를 적용한 뒤 60을 곱한다. 결과 timeout은 real*4 배열이다(242).
- 237·270·331: 두 convert 함수의 itb는 선언 이후 사용되지 않는다. time_to_vector의 date_string도 선언 이후 사용되지 않는다.
- 302–316·333–348: t_sec는 real*8이다. sec_add·secs_time·ref_fraction과 j_date 필드는 기본 REAL이다. 두 시간 변환 함수는 int로 날짜 증가량을 계산하며 음수 초를 따로 처리하는 분기는 없다.
- 369–370: timer는 system_clock의 count_rate로 나눈다. 이 루틴에는 count_rate를 검사하는 조건문이 없다.
