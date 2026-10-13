---
file: models/ROMS/raw/source_code/roms/Data/ROMS/CDL/frc_uvstress.cdl
lines: 36
sha256: 66d08e27a3c1aa27d305fd487f7d3a9b77ed4a8dc0ec632998466b452aa0c45a
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# frc_uvstress.cdl — 판독 구간 기록

구간은 1행부터 36행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | frc_uvstress / 차원 — RHO·U·V 수평 차원과 무제한 표면 운동량 응력 시간 차원(unlimited surface momentum stress time dimension)을 선언한다(1–10). 이름·값·현재 레코드 수 주석을 인용한다. 원문: `netcdf frc_uvstress {` (1); `dimensions:` (3); `	xi_rho = 386 ;` (4); `	xi_u = 385 ;` (5); `	xi_v = 386 ;` (6); `	eta_rho = 130 ;` (7); `	eta_u = 130 ;` (8); `	eta_v = 129 ;` (9); `	sms_time = UNLIMITED ; // (0 currently)` (10). |
| 12–18 | variables / 시간 메타데이터 — 표면 운동량 응력(surface momentum stress) 시간의 단위·기준 날짜·자료 간격 설명(interval)·시작일·종료일을 제시한다(13–18). 각 값과 날짜를 원문대로 인용한다. 원문: `variables:` (12); `	float sms_time(sms_time) ;` (13); `		sms_time:long_name = "surface momentum stress time" ;` (14); `		sms_time:units = "days since 1992-01-01 00:00:00" ;` (15); `		sms_time:interval = "367 daily data" ;` (16); `		sms_time:start_date = "01-Jan-1993" ;` (17); `		sms_time:end_date = "07-Jan-1994" ;` (18). |
| 19–29 | variables / 표면 응력 — u·v 표면 운동량 응력을 short 형식으로 선언하고 배열 차원·긴 이름(long_name)·단위·시간·축척 계수(scale_factor)를 지정한다(19–28). 두 성분의 단위 문자열 차이도 그대로 인용한다(21·26). 원문: `	short sustr(sms_time, eta_u, xi_u) ;` (19); `		sustr:long_name = "surface u-momentum stress" ;` (20); `		sustr:units = "Newton meter-2" ;` (21); `		sustr:time = "sms_time" ;` (22); `		sustr:scale_factor = 0.0005 ;` (23); `	short svstr(sms_time, eta_v, xi_v) ;` (24); `		svstr:long_name = "surface v-momentum stress" ;` (25); `		svstr:units = "Newton meter-2 * 1000" ;` (26); `		svstr:time = "sms_time" ;` (27); `		svstr:scale_factor = 0.0005 ;` (28). |
| 30–36 | global attributes / 전역 속성 — 외력(forcing) 파일 유형·NCEP/NCAR 재분석(re-analysis) 제목·격자 파일·원본 자료 파일·추출 이력을 제시한다(30–35). 닫는 중괄호까지 포함한다(36). 자료값을 지정하는 data 절은 없다. 원문: `// global attributes:` (30); `		:type = "ROMS FORCING file" ;` (31); `		:title = "NCEP/NCAR Global Atmospheric Re-analyses v4/97" ;` (32); `		:grd_file = "roms_nena_grid_3.nc" ;` (33); `		:source_file = "../natl/ncepflx1_NATL1993.nc" ;` (34); `		:source_file_history = "extraction from grib files using NCEP_GRBdaily - 27-Mar-2002 17:08:28" ;` (35); `}` (36). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 21·23·26·28: u응력의 단위 문자열은 `Newton meter-2`이다. v응력의 단위 문자열은 `Newton meter-2 * 1000`이다. 두 성분의 `scale_factor`는 모두 `0.0005`이다.
