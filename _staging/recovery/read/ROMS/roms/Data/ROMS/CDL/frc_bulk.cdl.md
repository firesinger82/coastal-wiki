---
file: models/ROMS/raw/source_code/roms/Data/ROMS/CDL/frc_bulk.cdl
lines: 58
sha256: 57a2daa428bb37d566dfc5d019cf399e43b42c12be0668ebde60820e4454ae4b
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# frc_bulk.cdl — 판독 구간 기록

구간은 1행부터 58행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | frc_bulk / 차원 — RHO·U·V 수평 차원과 무제한 시간 차원(unlimited time dimension)을 선언한다(1–10). 이름·값·현재 레코드 수 주석을 인용한다. 원문: `netcdf frc_bulk {` (1); `dimensions:` (3); `	xi_rho = 111 ;` (4); `	eta_rho = 241 ;` (5); `	xi_u = 110 ;` (6); `	eta_u = 241 ;` (7); `	xi_v = 111 ;` (8); `	eta_v = 240 ;` (9); `	time = UNLIMITED ; // (0 currently)` (10). |
| 12–23 | variables / 시간·풍속 — 대기 외력(atmospheric forcing) 시간과 수정 율리우스일(modified Julian day) 단위, RHO점 u·v 풍속 성분의 배열·단위·시간 참조를 선언한다(13–23). 원문: `variables:` (12); `	double time(time) ;` (13); `		time:long_name = "atmospheric forcing time" ;` (14); `		time:units = "modified Julian day" ;` (15); `	float Uwind(time, eta_rho, xi_rho) ;` (16); `		Uwind:long_name = "surface u-wind component" ;` (17); `		Uwind:units = "meter second-1" ;` (18); `		Uwind:time = "time" ;` (19); `	float Vwind(time, eta_rho, xi_rho) ;` (20); `		Vwind:long_name = "surface v-wind component" ;` (21); `		Vwind:units = "meter second-1" ;` (22); `		Vwind:time = "time" ;` (23). |
| 24–39 | variables / 대기 상태·강우 — 표면 기압(surface air pressure), 기온(surface air temperature), 상대습도(relative humidity), 강우율(rain fall rate)의 차원·설명·단위·시간 참조를 제시한다(24–39). 원문: `	float Pair(time, eta_rho, xi_rho) ;` (24); `		Pair:long_name = "surface air pressure" ;` (25); `		Pair:units = "millibar" ;` (26); `		Pair:time = "time" ;` (27); `	float Tair(time, eta_rho, xi_rho) ;` (28); `		Tair:long_name = "surface air temperature" ;` (29); `		Tair:units = "Celsius" ;` (30); `		Tair:time = "time" ;` (31); `	float Qair(time, eta_rho, xi_rho) ;` (32); `		Qair:long_name = "surface air relative humidity" ;` (33); `		Qair:units = "percentage" ;` (34); `		Qair:time = "time" ;` (35); `	float rain(time, eta_rho, xi_rho) ;` (36); `		rain:long_name = "rain fall rate" ;` (37); `		rain:units = "kilogram meter-2 second-1" ;` (38); `		rain:time = "time" ;` (39). |
| 40–51 | variables / 복사 — 단파 복사(solar shortwave radiation)와 순 장파 복사 플럭스(net longwave radiation flux)의 차원·단위·시간 참조를 제시한다(40–51). 양의 값은 하향 가열 플럭스, 음의 값은 상향 냉각 플럭스로 설명한다(43–44·49–50). 각 부호 설명을 원문대로 인용한다. 원문: `	float swrad(time, eta_rho, xi_rho) ;` (40); `		swrad:long_name = "solar shortwave radiation" ;` (41); `		swrad:units = "Watts meter-2" ;` (42); `		swrad:positive_value = "downward flux, heating" ;` (43); `		swrad:negative_value = "upward flux, cooling" ;` (44); `		swrad:time = "time" ;` (45); `	float lwrad(time, eta_rho, xi_rho) ;` (46); `		lwrad:long_name = "net longwave radiation flux" ;` (47); `		lwrad:units = "Watts meter-2" ;` (48); `		lwrad:positive_value = "downward flux, heating" ;` (49); `		lwrad:negative_value = "upward flux, cooling" ;` (50); `		lwrad:time = "time" ;` (51). |
| 52–58 | global attributes / 전역 속성 — 외력 파일 유형·대기장 제목·기록 시각을 제시한다(53–56). 마지막 빈 줄·닫는 중괄호까지 포함한다(57–58). 자료값을 지정하는 data 절은 없다. 원문: `// global attributes:` (53); `		:type = "FORCING file" ;` (54); `                :title = "NJB COAMPS Atmospheric Fields" ;` (55); `		:history = "FORCING file, 1.0, Thursday - July 12, 2001 - 10:55:42.8034 AM" ;` (56); `}` (58). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
