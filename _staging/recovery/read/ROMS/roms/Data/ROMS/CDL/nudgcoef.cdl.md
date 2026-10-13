---
file: models/ROMS/raw/source_code/roms/Data/ROMS/CDL/nudgcoef.cdl
lines: 44
sha256: c1527eddec89318a4d2f9fd19a94fc76b5c347a44518ce6399eb1e8d5502ac1a
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# nudgcoef.cdl — 판독 구간 기록

구간은 1행부터 44행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | 파일 시작·차원 — `espresso_nudgcoef` 파일의 수평 RHO 격자와 수직 S좌표 차원을 선언한다(1–5). 변수 절 머리를 포함한다(6). 차원 이름과 값을 그대로 인용한다(3–5). 원문: `netcdf espresso_nudgcoef {` (1); `dimensions:` (2); `	xi_rho = 130 ;` (3); `	eta_rho = 82 ;` (4); `	s_rho = 36 ;` (5); `variables:` (6). |
| 7–18 | 격자 유형·좌표 — 격자 유형 논리 스위치의 값과 의미를 선언한다(7–10). RHO점 경도와 위도를 선언한다(11–18). 배열 차원, 단위, 표준 이름을 그대로 인용한다(11–18). 원문: `	int spherical ;` (7); `		spherical:long_name = "grid type logical switch" ;` (8); `		spherical:flag_values = 0, 1 ;` (9); `		spherical:flag_meanings = "Cartesian spherical" ;` (10); `	double lon_rho(eta_rho, xi_rho) ;` (11); `		lon_rho:long_name = "longitude of RHO-points" ;` (12); `		lon_rho:units = "degree_east" ;` (13); `		lon_rho:standard_name = "longitude" ;` (14); `	double lat_rho(eta_rho, xi_rho) ;` (15); `		lat_rho:long_name = "latitude of RHO-points" ;` (16); `		lat_rho:units = "degree_north" ;` (17); `		lat_rho:standard_name = "latitude" ;` (18). |
| 19–38 | 너징 계수(nudging coefficients) — 2차원 운동량, 3차원 운동량, 수온, 염분, 일반 추적자의 역너징 계수(inverse nudging coefficients)를 선언한다(19–38). 각 배열 차원과 `day-1` 단위를 그대로 인용한다(19·21·23·25·27·29·31·33·35·37). 각 `coordinates` 문자열의 끝 공백도 원문 인용에 포함한다(22·26·30·34·38). 이 구간은 계수의 데이터 값·기본값·유효 범위를 지정하지 않는다(19–38). 원문: `	double M2_NudgeCoef(eta_rho, xi_rho) ;` (19); `		M2_NudgeCoef:long_name = "2D momentum inverse nudging coefficients" ;` (20); `		M2_NudgeCoef:units = "day-1" ;` (21); `		M2_NudgeCoef:coordinates = "xi_rho eta_rho " ;` (22); `	double M3_NudgeCoef(s_rho, eta_rho, xi_rho) ;` (23); `		M3_NudgeCoef:long_name = "3D momentum inverse nudging coefficients" ;` (24); `		M3_NudgeCoef:units = "day-1" ;` (25); `		M3_NudgeCoef:coordinates = "xi_rho eta_rho s_rho " ;` (26); `	double temp_NudgeCoef(s_rho, eta_rho, xi_rho) ;` (27); `		temp_NudgeCoef:long_name = "temp inverse nudging coefficients" ;` (28); `		temp_NudgeCoef:units = "day-1" ;` (29); `		temp_NudgeCoef:coordinates = "xi_rho eta_rho s_rho " ;` (30); `	double salt_NudgeCoef(s_rho, eta_rho, xi_rho) ;` (31); `		salt_NudgeCoef:long_name = "salt inverse nudging coefficients" ;` (32); `		salt_NudgeCoef:units = "day-1" ;` (33); `		salt_NudgeCoef:coordinates = "xi_rho eta_rho s_rho " ;` (34); `	double tracer_NudgeCoef(s_rho, eta_rho, xi_rho) ;` (35); `		tracer_NudgeCoef:long_name = "generic tracer inverse nudging coefficients" ;` (36); `		tracer_NudgeCoef:units = "day-1" ;` (37); `		tracer_NudgeCoef:coordinates = "xi_rho eta_rho s_rho " ;` (38). |
| 39–44 | 전역 속성·파일 끝 — 전역 파일 유형, 지역·해상도가 들어 있는 제목, 생성 스크립트와 시각을 지정한다(40–43). 빈 줄과 마지막 닫는 중괄호를 포함한다(39·44). 이 파일에는 그림 참조가 없다(1–44). 원문: `// global attributes:` (40); `		:type = "Nudging Coeffcients file" ;` (41); `		:title = "North Atlantic Damee #4, 0.75 Resolution" ;` (42); `		:history = "Nudging coefficient file created from d_nudgcoef.m: Wednesday - March 5, 2014 - 5:6:0.24549 PM" ;` (43); `}` (44). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 22·26·30·34·38행: `coordinates` 속성은 `xi_rho eta_rho` 또는 `xi_rho eta_rho s_rho`를 가리킨다. 이 이름들은 차원 절(2–5행)에 있으나 변수 절(6–38행)에는 같은 이름의 좌표 변수 선언이 없다.
- 41행: 전역 `type` 문자열은 `Nudging Coeffcients file`로 적혀 있다. 변수 설명(20·24·28·32·36행)은 `coefficients`를 사용한다.
