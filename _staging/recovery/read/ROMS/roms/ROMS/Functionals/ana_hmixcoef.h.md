---
file: models/ROMS/raw/source_code/roms/ROMS/Functionals/ana_hmixcoef.h
lines: 321
sha256: 24dd14dafe76f23aa7d95b905b3f59f9a1c8c64789a2ceb7cd3bbfd28fa536fa
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# ana_hmixcoef.h — 판독 구간 기록

구간은 1행부터 321행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–51 | 파일의 첫 루틴은 ana_sponge(2). 저작권·라이선스(4–9), 수평 혼합(horizontal mixing) 계수를 격자 크기에 맞춰 재척도화(rescaling)하고 스펀지 영역(sponge area)에서 증가시킨다는 주석(11–13). 쌍조화 계수(biharmonic coefficient)는 이미 제곱근을 취한 m² s⁻¹/² 단위라는 주석(15–18). mod_param·인수·MyFile 선언(22–31), `#include "tile.h"` (33)로 tile.h를 끼워 넣는다. ana_sponge_tile 호출(35–37). `#ifdef DISTRIBUTE` (41)의 `IF (Lanafile) THEN` (42), `#else` (43)의 `IF (Lanafile.and.(tile.eq.0)) THEN` (44), `#endif` (45) 뒤 ANANAME(8)=MyFile(46). 조건 종료·RETURN·루틴 종료·주석(47–51). |
| 52–87 | ana_sponge_tile 시작(53–55), mod_param·mod_grid·mod_mixing·mod_scalars·exchange_2d_mod 사용(58–63). `#ifdef DISTRIBUTE` (64)에서 mp_exchange2d 사용(65), 그 안 `# ifdef SOLVE3D` (66)에서 mp_exchange3d 사용(67), `# endif` (68); `#endif` (69). 인수·Iwrk·i·itrc·j·cff·cff1·cff2·fac 선언(73–81), `#ifdef WC13` (82)에서 온도·염분(salinity) 계수 변수 선언(83), `#endif` (84). `#include "set_bounds.h"` (86)로 set_bounds.h를 끼워 넣는다. 주석·빈 줄 포함. |
| 88–110 | 시작 시 53행 ana_sponge_tile 안. `#if defined ADRIA02` (92)는 아드리아해(Adriatic Sea) 남쪽 스펀지 분기. `fac=4.0_r8` (96). `# if defined UV_VIS2` (97)의 i 루프(98)·j=JstrT..MIN(6,JendT) 루프(99)에서 `cff=visc2(ng)+REAL(6-j,r8)*(fac*visc2(ng)-visc2(ng))/6.0_r8` (100), visc2_r·visc2_p에 cff 복사(101–102). j=MAX(JstrT,7)..JendT 루프(104)에서 `MIXING(ng) % visc2_r(i,j)=0.0_r8` (105); `MIXING(ng) % visc2_p(i,j)=0.0_r8` (106). 루프 종료(103·107–108), `# endif` (109), 빈 줄(110). |
| 111–125 | 시작 시 53행 ana_sponge_tile·92행 `#if defined ADRIA02` 안. `# if defined TS_DIF2` (111)의 itrc=1..NAT·i·j=JstrT..MIN(6,JendT) 루프(112–114)에서 `cff=tnu2(itrc,ng)+                                          &` (115); `&          REAL(6-j,r8)*(fac*tnu2(itemp,ng)-tnu2(itemp,ng))/6.0_r8` (116), diff2(i,j,itrc)=cff 복사(117). j=MAX(JstrT,7)..JendT 루프(119)는 `MIXING(ng) % diff2(i,j,itrc)=0.0_r8` (120). 루프 종료(118·121–123), `# endif` (124), 빈 줄(125). |
| 126–139 | 시작 시 53행 ana_sponge_tile·92행 `#if defined ADRIA02`에서 시작한 응용 전처리 선택 안. `#elif defined WC13` (126)는 미국 서해안(US West Coast) 스펀지 분기. `Iwrk=INT(user(1))  ! same for sponge and nudging layers` (130)로 스펀지와 너징(nudging) 영역 공통 폭을 설정. `# if defined UV_VIS2` (132), Marchesiello et al. 2003 운동량(momentum) 점성(viscosity) 주석(134–135). `cff1=visc2(ng)` (137); `cff2=100.0_r8` (138). 주석·빈 줄 포함. |
| 140–149 | 시작 시 53행 ana_sponge_tile·126행 `#elif defined WC13`·132행 `# if defined UV_VIS2` 안. 남쪽 경계 주석(140). j=JstrT..MIN(Iwrk,JendT) 루프(142)에서 `cff=cff1+REAL(Iwrk-j,r8)*(cff2-cff1)/REAL(Iwrk,r8)` (143), i 루프(144)는 `MIXING(ng)%visc2_r(i,j)=MAX(MIN(cff,cff2),cff1)` (145); `MIXING(ng)%visc2_p(i,j)=MAX(MIN(cff,cff2),cff1)` (146). 루프 종료·주석(147–149). |
| 150–159 | 시작 시 53행 ana_sponge_tile·126행 `#elif defined WC13`·132행 `# if defined UV_VIS2` 안. 북쪽 경계 주석(150). j=MAX(JstrT,Mm(ng)+1-Iwrk)..JendT 루프(152)에서 `cff=cff2-REAL(Mm(ng)+1-j,r8)*(cff2-cff1)/REAL(Iwrk,r8)` (153), i 루프(154)는 `MIXING(ng) % visc2_r(i,j)=MAX(MIN(cff,cff2),cff1)` (155); `MIXING(ng) % visc2_p(i,j)=MAX(MIN(cff,cff2),cff1)` (156). 루프 종료·주석(157–159). |
| 160–170 | 시작 시 53행 ana_sponge_tile·126행 `#elif defined WC13`·132행 `# if defined UV_VIS2` 안. 서쪽 경계 주석(160). i=IstrT..MIN(Iwrk,IendT)·j=MAX(JstrT,i)..MIN(Mm(ng)+1-i,JendT) 루프(162–163)에서 `cff=cff1+REAL(Iwrk-i,r8)*(cff2-cff1)/REAL(Iwrk,r8)` (164); `MIXING(ng) % visc2_r(i,j)=MAX(MIN(cff,cff2),cff1)` (165); `MIXING(ng) % visc2_p(i,j)=MAX(MIN(cff,cff2),cff1)` (166). 루프 종료(167–168), `# endif` (169), 빈 줄(170). |
| 171–184 | 시작 시 53행 ana_sponge_tile·126행 `#elif defined WC13` 안. `# if defined TS_DIF2` (171), Marchesiello et al. 2003 추적자(tracer) 확산계수(diffusivity) 주석(173–174). `cff1_t=tnu2(itemp,ng)` (176), `#  ifdef SALINITY` (177)에서 `cff1_s=tnu2(isalt,ng)` (178), `#  endif` (179). `cff2_t=50.0_r8` (180); `cff2_s=50.0_r8` (181). 남쪽 경계 주석(183–184). |
| 185–197 | 시작 시 53행 ana_sponge_tile·126행 `#elif defined WC13`·171행 `# if defined TS_DIF2` 안. j=JstrT..MIN(Iwrk,JendT) 루프(185)에서 `cff_t=cff1_t+REAL(Iwrk-j,r8)*(cff2_t-cff1_t)/REAL(Iwrk,r8)` (186). `#  ifdef SALINITY` (187)에서 `cff_s=cff1_s+REAL(Iwrk-j,r8)*(cff2_s-cff1_s)/REAL(Iwrk,r8)` (188), `#  endif` (189). i 루프(190)의 `MIXING(ng) % diff2(i,j,itemp)=MAX(MIN(cff_t,cff2_t),cff1_t)` (191), `#  ifdef SALINITY` (192)에서 `MIXING(ng) % diff2(i,j,isalt)=MAX(MIN(cff_s,cff2_s),cff1_s)` (193), `#  endif` (194). 루프 종료·주석(195–197). |
| 198–212 | 시작 시 53행 ana_sponge_tile·126행 `#elif defined WC13`·171행 `# if defined TS_DIF2` 안. 북쪽 경계의 j=MAX(JstrT,Mm(ng)+1-Iwrk)..JendT 루프(200)에서 `cff_t=cff2_t-REAL(Mm(ng)+1-j,r8)*(cff2_t-cff1_t)/REAL(Iwrk,r8)` (201). `#  ifdef SALINITY` (202)에서 `cff_s=cff2_s-REAL(Mm(ng)+1-j,r8)*(cff2_s-cff1_s)/REAL(Iwrk,r8)` (203), `#  endif` (204). i 루프(205)의 `MIXING(ng) % diff2(i,j,itemp)=MAX(MIN(cff_t,cff2_t),cff1_t)` (206), `#  ifdef SALINITY` (207)에서 `MIXING(ng) % diff2(i,j,isalt)=MAX(MIN(cff_s,cff2_s),cff1_s)` (208), `#  endif` (209). 루프 종료·주석(210–212). |
| 213–228 | 시작 시 53행 ana_sponge_tile·126행 `#elif defined WC13`·171행 `# if defined TS_DIF2` 안. 서쪽 경계 i=IstrT..MIN(Iwrk,IendT)·j=MAX(JstrT,i)..MIN(Mm(ng)+1-i,JendT) 루프(215–216)의 `cff_t=cff1_t+REAL(Iwrk-i,r8)*(cff2_t-cff1_t)/REAL(Iwrk,r8)` (217). `#  ifdef SALINITY` (218)에서 `cff_s=cff1_s+REAL(Iwrk-i,r8)*(cff2_s-cff1_s)/REAL(Iwrk,r8)` (219), `#  endif` (220). `MIXING(ng) % diff2(i,j,itemp)=MAX(MIN(cff_t,cff2_t),cff1_t)` (221), `#  ifdef SALINITY` (222)에서 `MIXING(ng) % diff2(i,j,isalt)=MAX(MIN(cff_s,cff2_s),cff1_s)` (223), `#  endif` (224). 루프 종료(225–226), `# endif` (227); `#endif` (228). |
| 229–247 | 시작 시 53행 ana_sponge_tile 안. 모든 응용에 공통인 교환 블록을 바꾸지 말라는 원문 주석(234–235). `#ifdef UV_VIS2` (237)의 `IF (EWperiodic(ng).or.NSperiodic(ng)) THEN` (238)에서 exchange_r2d_tile(...,visc2_r)(239–241)·exchange_p2d_tile(...,visc2_p)(242–244) 호출. 조건 종료(245), `#endif` (246), 빈 줄(247). |
| 248–258 | 시작 시 53행 ana_sponge_tile 안. `#ifdef UV_VIS4` (248)의 `IF (EWperiodic(ng).or.NSperiodic(ng)) THEN` (249)에서 exchange_r2d_tile(...,visc4_r)(250–252)·exchange_p2d_tile(...,visc4_p)(253–255) 호출. 조건 종료(256), `#endif` (257), 빈 줄(258). |
| 259–280 | 시작 시 53행 ana_sponge_tile 안. `#ifdef SOLVE3D` (259), 그 안 `# ifdef TS_DIF2` (260)의 `IF (EWperiodic(ng).or.NSperiodic(ng)) THEN` (261)에서 itrc=1..NT(ng) 루프로 exchange_r2d_tile(...,diff2(:,:,itrc)) 호출(262–266), 조건 종료(267), `# endif` (268). `# ifdef TS_DIF4` (270)의 `IF (EWperiodic(ng).or.NSperiodic(ng)) THEN` (271)에서 같은 추적자 루프로 exchange_r2d_tile(...,diff4(:,:,itrc)) 호출(272–276), 조건 종료(277), `# endif` (278); `#endif` (279). 빈 줄 포함. |
| 281–300 | 시작 시 53행 ana_sponge_tile 안. `#ifdef DISTRIBUTE` (281), 그 안 `# ifdef UV_VIS2` (283)에서 mp_exchange2d(...,2,...,NghostPoints,EWperiodic(ng),NSperiodic(ng),visc2_r,visc2_p) 호출(284–289), `# endif` (290). `# ifdef UV_VIS4` (292)에서 같은 형식으로 visc4_r·visc4_p 교환(293–298), `# endif` (299). 주석·빈 줄 포함. |
| 301–321 | 시작 시 53행 ana_sponge_tile·281행 `#ifdef DISTRIBUTE` 안. `# ifdef SOLVE3D` (301), 그 안 `#  ifdef TS_DIF2` (302)에서 mp_exchange3d(...,1,...,1,NT(ng),NghostPoints,EWperiodic(ng),NSperiodic(ng),diff2) 호출(303–307), `#  endif` (308). `#  ifdef TS_DIF4` (310)에서 같은 형식으로 diff4 교환(311–315), `#  endif` (316); `# endif` (317); `#endif` (318). 주석·RETURN·ana_sponge_tile 종료(319–321). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 2·53·321: 파일명은 ana_hmixcoef.h이지만 루틴명은 ana_sponge와 ana_sponge_tile이다.
- 115–116: ADRIA02 확산식의 첫 항은 tnu2(itrc,ng)이다. 증가 항은 itrc와 관계없이 tnu2(itemp,ng)를 사용한다.
- 104–106·119–120: ADRIA02는 j>=7 구간의 visc2_r·visc2_p·diff2를 0으로 대입한다.
- 130·143·153·164·186·201·217: WC13의 Iwrk는 INT(user(1))이다. 스펀지 식은 Iwrk를 분모에 사용하며 이 파일에는 별도의 Iwrk 범위 검사 조건이 없다.
- 92–228·248–257·270–278: 스펀지 값 계산은 ADRIA02·WC13의 UV_VIS2·TS_DIF2 분기에 있다. UV_VIS4·TS_DIF4는 경계 교환 블록에서만 등장한다.
