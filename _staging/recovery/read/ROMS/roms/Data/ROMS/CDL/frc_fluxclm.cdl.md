---
file: models/ROMS/raw/source_code/roms/Data/ROMS/CDL/frc_fluxclm.cdl
lines: 72
sha256: 873e62c51ac81f72d2d3f8937bb83f74e1ad94ab9938ec512937c56d525fe1db
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# frc_fluxclm.cdl — 판독 구간 기록

구간은 1행부터 72행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | frc_fluxclm / 차원 — RHO·U·V 수평 차원과 단파·해수면 온도·열 플럭스·담수 플럭스·해수면 염분별 유한 시간 차원(finite time dimension)을 선언한다(1–14). 각 이름·값을 인용한다. 원문: `netcdf frc_fluxclm {` (1); `dimensions:` (3); `	xi_rho = 386 ;` (4); `	xi_u = 385 ;` (5); `	xi_v = 386 ;` (6); `	eta_rho = 130 ;` (7); `	eta_u = 130 ;` (8); `	eta_v = 129 ;` (9); `	srf_time = 12 ;` (10); `	sst_time = 12 ;` (11); `	shf_time = 12 ;` (12); `	swf_time = 12 ;` (13); `	sss_time = 12 ;` (14). |
| 16–36 | variables / 순환 시간 — 외력(forcing)별 시간 변수의 긴 이름(long_name)·일 단위·주기 길이(cycle_length)를 제시한다(17–36). 각 선언·속성을 그대로 인용한다. 원문: `variables:` (16); `	float srf_time(srf_time) ;` (17); `		srf_time:long_name = "solar shortwave radiation time" ;` (18); `		srf_time:units = "day" ;` (19); `		srf_time:cycle_length = 365.25 ;` (20); `	float sst_time(sst_time) ;` (21); `		sst_time:long_name = "sea surface temperature" ;` (22); `		sst_time:units = "day" ;` (23); `		sst_time:cycle_length = 365.25 ;` (24); `	float shf_time(shf_time) ;` (25); `		shf_time:long_name = "surface heat flux time" ;` (26); `		shf_time:units = "day" ;` (27); `		shf_time:cycle_length = 365.25 ;` (28); `	float swf_time(swf_time) ;` (29); `		swf_time:long_name = "surface freshwater flux time" ;` (30); `		swf_time:units = "day" ;` (31); `		swf_time:cycle_length = 365.25 ;` (32); `	float sss_time(sss_time) ;` (33); `		sss_time:long_name = "sea surface salinity" ;` (34); `		sss_time:units = "day" ;` (35); `		sss_time:cycle_length = 365.25 ;` (36). |
| 37–50 | variables / 단파·해수면 온도·열 민감도 — 단파 복사(solar shortwave radiation)의 부호 규약, 해수면 온도(sea surface temperature, SST) 및 SST에 대한 표면 순 열 플럭스 민감도(surface net heat flux sensitivity)의 배열 차원·단위·시간 참조를 제시한다(37–50). 원문: `	float swrad(srf_time, eta_rho, xi_rho) ;` (37); `		swrad:long_name = "solar shortwave radiation" ;` (38); `		swrad:units = "Watts meter-2" ;` (39); `		swrad:positive_value = "downward flux, heating" ;` (40); `		swrad:negative_value = "upward flux, cooling" ;` (41); `		swrad:time = "srf_time" ;` (42); `	float SST(sst_time, eta_rho, xi_rho) ;` (43); `		SST:long_name = "sea surface temperature" ;` (44); `		SST:units = "Celsius" ;` (45); `		SST:time = "sst_time" ;` (46); `	float dQdSST(sst_time, eta_rho, xi_rho) ;` (47); `		dQdSST:long_name = "surface net heat flux sensitivity to SST" ;` (48); `		dQdSST:units = "Watts meter-2 Celsius-1" ;` (49); `		dQdSST:time = "sst_time" ;` (50). |
| 51–66 | variables / 순 열·담수 플럭스·해수면 염분 — 순 열 플럭스(net heat flux), E-P 담수 플럭스(freshwater flux) 및 해수면 염분(sea surface salinity, SSS)을 선언한다(51–65). 열 플럭스의 하향 가열·상향 냉각 및 담수 플럭스의 순 증발·순 강수 부호 설명을 그대로 인용한다(54–55·60–61). 원문: `	float shflux(shf_time, eta_rho, xi_rho) ;` (51); `		shflux:long_name = "surface net heat flux" ;` (52); `		shflux:units = "Watts meter-2" ;` (53); `		shflux:positive_value = "downward flux, heating" ;` (54); `		shflux:negative_value = "upward flux, cooling" ;` (55); `		shflux:time = "shf_time" ;` (56); `	float swflux(swf_time, eta_rho, xi_rho) ;` (57); `		swflux:long_name = "surface freshwater flux (E-P)" ;` (58); `		swflux:units = "centimeter day-1" ;` (59); `		swflux:positive_value = "net evaporation" ;` (60); `		swflux:negative_value = "net precipitation" ;` (61); `		swflux:time = "swf_time" ;` (62); `	float SSS(sss_time, eta_rho, xi_rho) ;` (63); `		SSS:long_name = "sea surface salinity" ;` (64); `		SSS:time = "sss_time" ;` (65). |
| 67–72 | global attributes / 전역 속성 — 외력 파일 유형·월별 기후값(climatology) 제목·격자 파일명을 제시한다(67–70). 마지막 빈 줄·닫는 중괄호까지 포함한다(71–72). 자료값을 지정하는 data 절은 없다. 원문: `// global attributes:` (67); `		:type = "ROMS FORCING file" ;` (68); `		:title = "NENA COADS Monthly Climatology" ;` (69); `		:grd_file = "roms_nena_grid_3.nc" ;` (70); `}` (72). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 21–24·43–46: `sst_time:long_name`과 `SST:long_name`은 모두 `sea surface temperature`이다. `sst_time`의 단위는 `day`이고 `SST`의 단위는 `Celsius`이다.
- 33–36·63–65: `sss_time:long_name`과 `SSS:long_name`은 모두 `sea surface salinity`이다. `sss_time`의 단위는 `day`이다. `SSS`에는 단위 속성이 없다.
