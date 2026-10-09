---
file: models/ADCIRC/raw/source_code/adcirc/src/sun.F90
lines: 249
sha256: 62bf7a52c7e5d49e6e478f29b064128e8e0b6a55f13a9924ff2bb29744824491
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# sun.F90 — 판독 구간 기록

구간은 1행부터 249행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–35 | 저작권·LGPL v3 이상·무보증 머리말(1–19). mod_sun_coordinates 모듈과 t_astronomic_values 사용(20–24). SUN_COORDINATES 총칭 인터페이스(generic interface)는 SUB0/SUB1 두 모듈 절차를 묶는다(26–28). 기본 private, 공개 SUN_COORDINATES와 contains·빈 줄을 포함한다(30–35). |
| 36–52 | 태양 중심차(equation of center)의 페이지 164 주석과 elemental SUN_CENTER 선언(36–43). T는 J2000부터 36525일 기준 율리우스 세기(Julian century), M은 평균 근점이각(mean anomaly)이라는 주석이다(37–38). M을 라디안(radian)으로 바꾸고 1·2·3배 M의 sine 및 T 계수로 C를 계산한다(45–49). 함수 종료·빈 줄을 포함한다(51–52). 원문: `M_R = M*DEG2RAD` (45); `C = (1.914602d0 + T*(-0.004817d0 - 0.000014d0*T))*sin(M_R) + &` (47); `(0.019993d0 - 0.000101d0*T)*sin(2.d0*M_R) + &` (48); `0.000289d0*sin(3.d0*M_R)` (49). |
| 53–68 | 태양 진경도(true longitude)와 L0/C/선택적 장동(nutation) 설명 주석(53–56). SUN_LON은 L0+C를 계산한다(57–62). DPsi가 있으면 -0.00569d0와 DPsi를 더한다(64–66). 함수 종료·빈 줄을 포함한다(67–68). 원문: `SLON = L0 + C ! Sun's true longtiude` (62); `if (present(DPsi)) then` (64); `SLON = SLON - 0.00569d0 + Dpsi` (65). |
| 69–77 | SUN_NU의 진근점이각(true anomaly) 설명·elemental 선언·M/C 입력(69–74). nu=M+C이며 함수 종료·빈 줄까지 포함한다(75–77). 원문: `nu = M + C ! its true anomerly` (75). |
| 78–96 | 태양/지구 중심 거리의 단위는 천문단위(astronomical unit)라는 주석이다(78–81). SUN_RADIUS는 진근점이각과 지구 궤도 이심률(eccentricity)을 입력받는다(82–86). nu를 라디안으로 바꾸고 1+eccen×cos(nu), 1.000001018×(1-eccen²)를 분모·분자로 계산한다(88–91). R=NUM/DEN과 함수 종료·빈 줄을 포함한다(93–96). 원문: `nu_rad = nu*DEG2RAD` (88); `DEN = 1.d0 + eccen*cos(nu_rad)` (90); `NUM = 1.000001018d0*(1.d0 - eccen*eccen)` (91); `R = NUM/DEN` (93). |
| 97–115 | 태양 적위(declination)와 황도경사(obliquity of the ecliptic) 설명 뒤 SOLAR_DEC 함수 전체가 ! 주석으로 남아 있다(97–114). 두 각도 변환, sine의 곱, asin과 RAD2DEG 변환식은 실행되지 않는 주석 원문이다(108–113). 빈 줄까지 포함한다(115). 원문: `!    SLON_RAD = SLON*DEG2RAD` (108); `!    VarEps_RAD = VarEps*DEG2RAD` (109); `!    DEC = sin(SLON_RAD)*sin(VarEps_RAD)` (111); `!    DEC = asin(DEC)*RAD2DEG` (113). |
| 116–136 | 태양 적경(right ascension) 설명 뒤 SOLAR_RA 함수 전체가 ! 주석이다(116–135). 두 각도 변환과 cosine/sine 분자·분모, atan2의 도(degree) 변환 및 mod(...,360.d0) 식이 주석으로 남아 있다(128–134). 함수 종료 주석·빈 줄을 포함한다(135–136). 원문: `!    SLON_RAD = SLON*DEG2RAD` (128); `!    VarEps_RAD = VarEps*DEG2RAD` (129); `!    NUM = cos(VarEps_RAD)*sin(SLON_RAD)` (131); `!    DEN = cos(SLON_RAD)` (132); `!    RA = mod(atan2(NUM, DEN)*RAD2DEG, 360.d0)` (134). |
| 137–177 | SUN_COORDINATES_SUB1 머리말은 장 25·페이지 163–169와 좌표·JD/ASVAL 설명을 적는다(137–147). 루틴은 RA/DEC/Delta 출력과 JD 입력, ASVAL/NUTATION 선택 입력을 선언한다(148–163). have_asval=false, use_nutation=true 기본값이다(165–166). ASVAL이 있으며 abs(ASVAL%JD-JD)<1.0d-9이면 재사용한다(168–172). NUTATION이 있으면 use_nutation에 복사한다(174–176). 빈 줄까지 포함한다(177). 원문: `have_asval = .false.` (165); `use_nutation = .true.` (166); `if (present(ASVAL)) then` (168); `if (abs(ASVAL%JD - JD) < 1.0d-9) then` (169); `if (present(NUTATION)) then` (174). |
| 178–200 | 시작 시 148행 SUN_COORDINATES_SUB1 안. have_asval이 없으면 JULIAN_CENTURIES, M_DEG/LP_DEG/OMEGA_DEG/L0_DEG, eccentricity_earth_orbit, DeltaPsiL/DeltaVarepsL/varepsilon0_ecliptic을 호출한다(178–190). M/LP/OG/L0는 modulo(...,360.d0)로 정규화하며 vareps는 vareps0+DVareps다. else는 ASVAL의 T·M·L0·eccen·DPsi·vareps를 가져온다(191–197). 조건 종료 후 SUN_CENTER(T,M)로 C를 계산한다(198–200). 원문: `if (.not. have_asval) then` (178); `T = JULIAN_CENTURIES(JD)` (179); `M = modulo(M_DEG(T), 360.d0)` (180); `LP = modulo(LP_DEG(T), 360.d0)` (181); `eccen = eccentricity_earth_orbit(T)` (182); `OG = modulo(OMEGA_DEG(T), 360.d0)` (184); `L0 = modulo(L0_DEG(T), 360.d0)` (185); `DPsi = DeltaPsiL(OG, L0, LP)` (186); `DVareps = DeltaVarepsL(OG, L0, LP)` (187); `vareps0 = varepsilon0_ecliptic(T)` (189); `vareps = vareps0 + Dvareps` (190); `M = modulo(ASVAL%M, 360.d0)` (193); `L0 = modulo(ASVAL%L0, 360.d0)` (194); `C = SUN_CENTER(T, M)` (199). |
| 201–211 | 시작 시 148행 SUN_COORDINATES_SUB1 안. use_nutation이면 DPsi가 있는 SUN_COORDINATES_SUB0을 호출한다(201–202). else는 DPsi 없이 호출한다(203–205). ECLIP2EQ(RA,DEC,lambda,beta,vareps)로 황도(ecliptic) 좌표를 적도(equatorial) 좌표로 바꾼다(207–208). 루틴 종료·빈 줄을 포함한다(210–211). 원문: `if (use_nutation) then` (201). |
| 212–249 | SUN_COORDINATES_SUB0 머리말·입출력 설명(212–226). 실제 선언은 lambda/beta/Delta 출력, L0/M/C/eccen 입력과 선택 DPsi 입력이다(227–234). beta=0을 설정한다(236). DPsi가 없으면 SUN_LON(C,L0), else는 SUN_LON(C,L0,DPsi)를 호출한다(237–241). SUN_NU 결과 snu로 SUN_RADIUS를 호출해 거리를 계산한다(243–244). return·루틴·모듈 종료와 빈 줄을 포함한다(245–249). 원문: `beta = 0.d0` (236); `if (.not. present(DPsi)) then` (237); `lambda = SUN_LON(C, L0)` (238); `lambda = SUN_LON(C, L0, DPsi)` (240); `snu = SUN_NU(M, C)` (243); `Delta = SUN_RADIUS(snu, eccen) ! Distance between centers` (244). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 55: C 설명 주석에는 eq1.495978707×1011uation이라는 문자열이 들어 있다.
- 140–147·154–158·215–231: 두 SUN_COORDINATES 루틴의 머리말 INPUT/OUTPUT 표기는 실제 intent 선언과 반대 방향이다. SUB1의 RA/DEC/Delta는 OUT이고 JD는 IN이다. SUB0의 lambda/beta/Delta는 OUT이며 L0/M/C/eccen은 IN이다.
- 178–197·201–208: NUTATION=false는 SUB0에 DPsi를 전달하지 않게 한다. ECLIP2EQ에 전달하는 vareps는 직접 계산 경로에서 vareps0+DVareps이며 false 분기에서 vareps0로 되돌리는 대입은 없다.
- 90–93: SUN_RADIUS는 DEN으로 나눈다. 이 함수에는 DEN=0이나 eccen 범위를 검사하는 조건이 없다.
- 168–171: ASVAL 재사용의 JD 차이 기준은 1.0d-9로 고정되어 있다. 이 파일에는 재사용 ASVAL의 다른 필드를 개별 검사하는 조건이 없다.

