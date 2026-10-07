---
file: models/SFINCS/raw/source_code/sfincs/source/src/snapwave/snapwave_date.f90
lines: 87
sha256: ab44d8e635bfd523a84dbb48c5d31c16f614349bb63225b3f3bdf13ca56eb3cd
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# snapwave_date.f90 — 판독 구간 기록

구간은 1행부터 87행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–27 | snapwave_date 모듈 시작, implicit none, contains, 구분 주석(1–4). `time_difference(datespw,datesim,dtsec)`는 두 길이 15 문자열을 `(I4,2I2,1X,3I2)`로 연·월·일·시·분·초 정수에 읽는다(5–15). `ijul1 = julian_date (yyyy1,mm1,dd1)` (19), `ijul2 = julian_date (yyyy2,mm2,dd2)` (20)로 Julian 날짜를 구한다. `sec1  = hh1*3600 + mn1*60 + ss1` (22), `sec2  = hh2*3600 + mn2*60 + ss2` (23), `dtsec = (ijul2 - ijul1)*86400 + sec2 - sec1` (24)로 두 번째 시각에서 첫 번째 시각을 뺀 초 차이를 계산한다. 주석·루틴 종료·빈 줄(25–27). |
| 28–38 | `julian_date (yyyy, mm, dd) RESULT (julian)` 함수 시작(28). 주석은 Fliegel & Van Flandern, CACM 11(10):657, 1968과 예시 `julian_date(1970,1,1)=2440588`을 적는다(29–31). 입력과 반환값은 INTEGER이다(32–33). 원문 식은 `julian = dd-32075+1461*(yyyy+4800+(mm-14)/12)/4 + &` (34); `367*(mm-2-((mm-14)/12)*12)/12- &` (35); `3*((yyyy + 4900 + (mm - 14)/12)/100)/4` (36)이다. 함수 종료·주석(37–38). |
| 39–52 | `date_to_iso8601(date_string)` 함수가 가변 길이 입력과 길이 256 출력을 선언한다(39–41). 연·월·일·시·분·초를 yyyy/mm/dd/hh/no_nodes/ss에 읽는다(42–44). 입력 주석은 yyyymmdd HHMMSS이다(43). `write(date_iso8601, '(I4,A1,I0.2,A1,I0.2,A1,I0.2,A1,I0.2,A1,I0.2)')  yyyy, '-', mm, '-', dd, ' ', hh, ':', no_nodes, ':', ss  !in DFM/FEWS without the T` (47)로 날짜와 시각 사이에 공백을 쓴다. 'T'를 쓰는 대체 write는 주석 처리되어 있다(48). 함수 종료·주석·빈 줄(49–52). |
| 53–72 | `convert_fewsdate(treftimefews, tbnd, ntbnd)` 함수 시작(53). sfincs_input use는 주석 처리되어 있다(55). 길이 41 treftimefews/trefstr, 날짜·초 차이 정수, allocatable 단정밀도 입력·반환 배열을 선언한다(57–64). trefstr을 `(I4,2I2,1X,3I2)`로 읽는다(67). 주석은 FEWS 입력을 minutes since 1970-01-01 00:00:00.0 +0000으로 적는다(69). `read(treftimefews, '(A14,I4,A1,I2,A1,I2,A1,I2,A1,I2,A1,I2)')tmp,yyyy2,tmp,mm2,tmp,dd2,tmp,hh2,tmp,mn2,tmp,ss2 !assume time in UTC, whole seconds` (71)로 FEWS 기준 날짜를 읽는다. |
| 73–87 | 시작 시 53행 convert_fewsdate 함수 안. `ijul1 = julian_date (yyyy1,mm1,dd1)` (73), `ijul2 = julian_date (yyyy2,mm2,dd2)` (74), `sec1  = hh1*3600 + mn1*60 + ss1` (76), `sec2  = hh2*3600 + mn2*60 + ss2` (77), `dtsec = (ijul2 - ijul1)*86400 + sec2 - sec1` (78)로 기준 날짜의 초 차이를 계산한다. tbndout(ntbnd)을 할당한다(80). `tbndout = (tbnd * 60) + dtsec  ! time from fews is in minutes, then correct for use wrt sfincs treftime` (82)로 분을 초로 바꾸고 기준 차이를 더한다. 함수 종료·빈 줄·주석·모듈 종료(83–87). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 53·55·57·67: convert_fewsdate의 trefstr은 지역 문자열이다. trefstr은 함수 인수가 아니며, read 전에 값을 설정하는 실행문은 이 함수에 없다. sfincs_input use는 주석 처리되어 있다.
- 60·71: tmp는 integer로 선언되어 있다. FEWS 문자열 read는 A14와 각 A1 필드의 수신 변수로 tmp를 사용한다.
- 47–48: date_to_iso8601의 실행 write는 날짜와 시각 사이에 공백을 쓴다. 'T'를 쓰는 write는 주석 처리되어 있다.
