---
file: models/ADCIRC/raw/source_code/adcirc/src/sun_moon_system.F90
lines: 94
sha256: 3d3b890796da513b8e3e39f85fbf32891c2170eda98f00c141b8c7fbb5b64085
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# sun_moon_system.F90 — 판독 구간 기록

구간은 1행부터 94행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–25 | 저작권·LGPL v3 이상·무보증 머리말(1–19). 구동 루틴(driver subroutine) 주석과 mod_moon_sun_coors 시작(20–21). t_astronomic_values를 가져오고 implicit none·빈 줄을 포함한다(22–25). |
| 26–40 | t_moon_sun 형식은 private include_nutation=true와 astronomic_values를 보유한다(26–28). 공개 형식 결합 절차(type-bound procedure) set_nutation/heavenly_objs_coords_jm/gmst_deg_fn은 pass(self)다(29–33). 모듈 기본 private이며 t_moon_sun을 공개한다(35–37). contains·빈 줄을 포함한다(39–40). 원문: `logical, private :: include_nutation = .true.` (27). |
| 41–47 | set_nutation은 self를 inout, NUTATION을 입력으로 받아 INCLUDE_NUTATION에 복사한다(41–46). 루틴 종료·빈 줄까지 포함한다(46–47). 원문: `self%INCLUDE_NUTATION = NUTATION` (45). |
| 48–69 | 달·태양의 지심 좌표(geocentric coordinates) 계산 주석(48–50). MOON_POS/SUN_POS 순서는 적경(right ascension, RA)·적위(declination, DEC)·거리 Delta이며 JD는 율리우스일(Julian day) 입력이라는 설명이다(51–57). 기본 장동(nutation) 포함 시 겉보기 좌표(apparent coordinates), false 설정 시 기하 좌표(geometrical coordinates)라는 주석과 SET_NUTATION(false) 호출 예시·빈 줄을 포함한다(59–69). |
| 70–85 | HEAVENLY_OBJS_COORDS_JM은 달/태양 좌표 모듈을 가져온다(70–73). self inout, JD 입력, 두 길이 3 좌표 배열과 IERR 출력을 선언한다(74–77). self%astronomic_values%compute_astronomic_values(JD)를 먼저 호출한다(79). 두 좌표 호출은 각각 배열 성분 1/2/3, JD, 같은 사전 계산 값과 INCLUDE_NUTATION을 전달한다(80–81). 끝에서 IERR=0을 대입하고 종료한다(83–85). 원문: `call self%astronomic_values%compute_astronomic_values(JD)` (79); `call MOON_COORDINATES(MOON_POS(1), MOON_POS(2), MOON_POS(3), JD, self%astronomic_values, self%INCLUDE_NUTATION)` (80); `call SUN_COORDINATES(SUN_POS(1), SUN_POS(2), SUN_POS(3), JD, self%astronomic_values, self%INCLUDE_NUTATION)` (81); `IERR = 0` (83). |
| 86–94 | GMST_DEG_FN은 그리니치 평균 항성시(Greenwich mean sidereal time, GMST) 함수 GMST_DEG를 가져온다(86–87). self/JDE를 입력받아 JDE와 INCLUDE_NUTATION 및 저장된 astronomic_values를 GMST_DEG에 전달해 결과를 반환한다(89–92). 빈 줄·모듈 종료까지 포함한다(93–94). 원문: `gmst = GMST_DEG(JDE, self%INCLUDE_NUTATION, self%astronomic_values)` (91). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 77–83: IERR는 출력 인수다. 본문은 두 좌표 호출 뒤 IERR=0을 무조건 대입한다. 이 본문에는 오류 상태를 받아 IERR를 바꾸는 조건이 없다.
- 79·86–92: HEAVENLY_OBJS_COORDS_JM은 JD로 astronomic_values를 갱신한다. GMST_DEG_FN은 저장된 astronomic_values를 넘기며 이 함수 안에는 갱신 호출이나 JDE와 저장 날짜의 일치 검사가 없다. GMST_DEG 내부는 이 파일 판독 범위에 포함하지 않았다.

