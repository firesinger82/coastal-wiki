---
file: models/ROMS/raw/source_code/roms/Data/ROMS/CDL/frc_tides.cdl
lines: 70
sha256: 1630d2fbab311174e0b76acde697a3f5ecd4497b351a61862aafbe711aa40455
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# frc_tides.cdl — 판독 구간 기록

구간은 1행부터 70행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | frc_tides / 차원 — RHO 수평 차원, 분조(tidal constituent) 이름 문자 길이의 차원과 무제한 조석 주기 차원(unlimited tide-period dimension)을 선언한다(1–7). 차원값과 현재 개수 주석을 그대로 인용한다. 원문: `netcdf frc_tides {` (1); `dimensions:` (3); `	eta_rho = 106 ;` (4); `	xi_rho = 242 ;` (5); `	two = 2 ;` (6); `	tide_period = UNLIMITED ; // (11 currently)` (7). |
| 9–26 | variables / 위상 기준일·좌표·마스크 — 영 위상(zero phase) 기준 날짜의 표기·C·Fortran 형식, RHO점 위도(latitude)·경도(longitude), 육지·물 마스크(mask) 옵션을 제시한다(10–26). 원문: `variables:` (9); `	double zero_phase_date ;` (10); `		zero_phase_date:long_name = "tidal reference date for zero phase" ;` (11); `		zero_phase_date:units = "days as %Y%m%d.%f" ;` (12); `		zero_phase_date:C_format = "%13.4f" ;` (13); `		zero_phase_date:FORTRAN_format = "(f13.4)" ;` (14); `	double lat_rho(eta_rho, xi_rho) ;` (15); `		lat_rho:long_name = "latitude of RHO-points" ;` (16); `		lat_rho:units = "degree_north" ;` (17); `		lat_rho:field = "lat_rho, scalar" ;` (18); `	double lon_rho(eta_rho, xi_rho) ;` (19); `		lon_rho:long_name = "longitude of RHO-points" ;` (20); `		lon_rho:units = "degree_east" ;` (21); `		lon_rho:field = "lon_rho, scalar" ;` (22); `	double mask_rho(eta_rho, xi_rho) ;` (23); `		mask_rho:long_name = "mask on RHO-points" ;` (24); `		mask_rho:option_0 = "land" ;` (25); `		mask_rho:option_1 = "water" ;` (26). |
| 27–38 | variables / 조석 주기·수위 — 조석 각주기(tide angular period)의 시간 단위와 조석 수위 위상각(tidal elevation phase angle)·진폭(amplitude) 배열을 선언한다(27–38). 위상각 단위는 선택한 시간 원점 대비 최대 수위 시점 설명을 포함하며 그대로 인용한다(33). 원문: `	double tide_period(tide_period) ;` (27); `		tide_period:long_name = "tide angular period" ;` (28); `		tide_period:units = "hours" ;` (29); `		tide_period:field = "tide_period, scalar, series" ;` (30); `	double tide_Ephase(tide_period, eta_rho, xi_rho) ;` (31); `		tide_Ephase:long_name = "tidal elevation phase angle" ;` (32); `		tide_Ephase:units = "degrees, time of maximum elevation with respect to chosen time origin" ;` (33); `		tide_Ephase:field = "tide_Ephase, scalar, series" ;` (34); `	double tide_Eamp(tide_period, eta_rho, xi_rho) ;` (35); `		tide_Eamp:long_name = "tidal elevation amplitude" ;` (36); `		tide_Eamp:units = "meter" ;` (37); `		tide_Eamp:field = "tide_Eamp, scalar, series" ;` (38). |
| 39–57 | variables / 조류 타원·분조 이름 — 조류 위상각(tidal current phase angle), 동쪽과 타원 장반경 사이의 경사각(inclination angle), 단반경(semi-minor axis)·장반경(semi-major axis)에 대한 최소·최대 조류와 분조 이름을 선언한다(39–56). 각 차원·기호·단위·설명을 원문대로 인용한다. 원문: `	double tide_Cphase(tide_period, eta_rho, xi_rho) ;` (39); `		tide_Cphase:long_name = "tidal current phase angle" ;` (40); `		tide_Cphase:units = "degrees, time of maximum velocity with respect chosen time origin" ;` (41); `		tide_Cphase:field = "tide_Cphase, scalar" ;` (42); `	double tide_Cangle(tide_period, eta_rho, xi_rho) ;` (43); `		tide_Cangle:long_name = "tidal current inclination angle" ;` (44); `		tide_Cangle:units = "degrees between semi-major axis and East" ;` (45); `		tide_Cangle:field = "tide_Cangle, scalar" ;` (46); `	double tide_Cmin(tide_period, eta_rho, xi_rho) ;` (47); `		tide_Cmin:long_name = "minimum tidal current, ellipse semi-minor axis" ;` (48); `		tide_Cmin:units = "meter second-1" ;` (49); `		tide_Cmin:field = "tide_Cmin, scalar" ;` (50); `	double tide_Cmax(tide_period, eta_rho, xi_rho) ;` (51); `		tide_Cmax:long_name = "maximum tidal current, ellipse semi-major axis" ;` (52); `		tide_Cmax:units = "meter second-1" ;` (53); `		tide_Cmax:field = "tide_Cmax, scalar" ;` (54); `	char tidal_constituents(tide_period, two) ;` (55); `		tidal_constituents:long_name = "Tidal Constituent Names" ;` (56). |
| 58–66 | global attributes / 전역 속성 — 조석 외력(tidal forcing) 파일 유형·제목·격자 파일·OTPS 출처·분조 목록·출처 URL·기록 시각을 제시한다(58–65). 분조 이름과 값은 원문대로 인용한다. 원문: `// global attributes:` (58); `		:type = "ROMS Forcing File" ;` (59); `		:title = "DOPPIO Tidal Forcing from OTPS" ;` (60); `		:grid_file = "grid_doppio.nc" ;` (61); `		:source = "OTPS" ;` (62); `		:tidal_constituents = "m2, s2, n2, k2, k1, o1, p1, q1, m4, ms, mn" ;` (63); `		:source_url = "http://www.coas.oregonstate.edu/research/po/research/tide/region.html" ;` (64); `		:history = "FORCING file, Tuwsday - April 2, 2014 - 14:28:53" ;` (65). |
| 67–70 | data / 영 위상 기준 날짜 — data 절에서 `zero_phase_date`의 실제 자료값을 지정한다(67–69). 입력 예제행을 그대로 인용하고 마지막 중괄호까지 포함한다(70). 원문: `data:` (67); ` zero_phase_date = 20060101.0000 ;` (69); `}` (70). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 7·67–70: 무제한 `tide_period` 차원의 주석은 `(11 currently)`이다. data 절에는 `zero_phase_date`만 있으며 `tide_period` 자료값은 없다.
