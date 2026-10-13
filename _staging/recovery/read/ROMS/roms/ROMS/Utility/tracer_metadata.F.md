---
file: models/ROMS/raw/source_code/roms/ROMS/Utility/tracer_metadata.F
lines: 94
sha256: f17c6c2d3ca614dd1b8d908effcd2cabfdb00edd436e17f5d186004308957002
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# tracer_metadata.F — 판독 구간 기록

구간은 1행부터 94행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–31 | cppdefs.h를 포함하고 tracer_metadata_mod를 선언한다(1–2). 저작권·라이선스와 추적자(tracer) 이름·표준 메타데이터(metadata) 이름에서 배열 인덱스를 구한다는 모듈 주석을 둔다(4–16). BIOLOGY이면 mod_biology를 가져온다(20–22). tracer_index를 공개하고 CONTAINS를 연다(28–30). 조건·계산식·호출·전처리 원문: `#include "cppdefs.h"` (1); `#ifdef BIOLOGY` (20); `#endif` (22). |
| 32–60 | tracer_index(name)의 결과 이름은 t_index이다(32). 입력 문자열 name과 정수 결과 t_index를 선언한다(51·55). 함수 주석은 logical 함수와 실행 오류 플래그 검사를 설명하며 출력 이름은 foundit으로 적혀 있다(36–45). 실제 이름 조회 코드 전의 구분 주석까지 포함한다(57–60). |
| 61–71 | 시작 시 바깥 블록 `FUNCTION tracer_index (name) RESULT (t_index)` (32) 안. TRIM(name)을 SELECT CASE로 분기한다(61). 온도(temperature) 상태·보정·고유벡터(eigenvector)·수면·경계 이름, 두 표준 온도 이름, shflux 계열, 표준 열속(heat flux), AKt·표준 수직 확산 계수(vertical diffusion coefficient) 이름을 모두 itemp에 연결한다(62–71). 각 문자열은 CASE 원문에 그대로 기록한다. 조건·계산식·호출·전처리 원문: `SELECT CASE (TRIM(name))` (61); `CASE ('temp', 'temp_Bcorr', 'temp_eigen', 'temp_sur',           &` (62); `&        'temp_west', 'temp_east', 'temp_south', 'temp_north',     &` (63); `&        'temp_obc_eigen',                                         &` (64); `&        'sea_water_temperature',                                  &` (65); `&        'sea_water_potential_temperature',                        &` (66); `&        'shflux', 'shflux_Bcorr', 'shflux_eigen',                 &` (67); `&        'surface_downward_heat_flux_in_sea_water',                &` (68); `&        'AKt',                                                    &` (69); `&     'vertical_diffusion_coefficient_of_temperature_in_sea_water')` (70); `t_index = itemp` (71). |
| 72–80 | 시작 시 바깥 블록 `FUNCTION tracer_index (name) RESULT (t_index)` (32) · `SELECT CASE (TRIM(name))` (61), 현재 분기 `CASE ('temp', 'temp_Bcorr', 'temp_eigen', 'temp_sur',           &` (62) 안. 염분(salinity) 상태·보정·고유벡터·수면·경계 이름, 표준 염분 이름, ssflux 계열, 표준 염속(salt flux), AKs·표준 수직 확산 계수 이름을 isalt에 연결한다(72–80). 각 문자열은 CASE 원문에 그대로 기록한다. 조건·계산식·호출·전처리 원문: `CASE ('salt', 'salt_Bcorr', 'salt_eigen', 'salt_sur',           &` (72); `&        'salt_west', 'salt_east', 'salt_south', 'salt_north',     &` (73); `&        'salt_obc_eigen',                                         &` (74); `&        'sea_water_salinity',                                     &` (75); `&        'ssflux', 'ssflux_Bcorr', 'ssflux_eigen',                 &` (76); `&        'salt_flux_into_sea_water',                               &` (77); `&        'AKs',                                                    &` (78); `&     'vertical_diffusion_coefficient_of_salinity_in_sea_water')` (79); `t_index = isalt` (80). |
| 81–94 | 시작 시 바깥 블록 `FUNCTION tracer_index (name) RESULT (t_index)` (32) · `SELECT CASE (TRIM(name))` (61), 현재 분기 `CASE ('salt', 'salt_Bcorr', 'salt_eigen', 'salt_sur',           &` (72) 안. CASE DEFAULT에서는 Master가 찾지 못한 이름을 출력하고 exit_flag=5를 설정한다(81–86). 오류 FORMAT을 선언하고 RETURN 후 함수·모듈을 닫는다(88–94). 이 분기에는 t_index 대입문이 없다. 조건·계산식·호출·전처리 원문: `CASE DEFAULT` (81); `IF (Master) THEN` (82); `exit_flag=5` (85). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 32·36–37·45·55: 실제 함수 결과는 정수 t_index이다. 주석은 logical 함수·실행 오류 검사와 출력 foundit을 적고 있다.
- 55·81–86: t_index 선언에는 초기값이 없다. CASE DEFAULT는 exit_flag=5만 설정하며 t_index에는 값을 대입하지 않는다.
- 20–22·61–86: BIOLOGY이면 mod_biology를 가져온다. 이 파일의 SELECT CASE에는 온도·염분 이름 집합과 CASE DEFAULT만 있다.
