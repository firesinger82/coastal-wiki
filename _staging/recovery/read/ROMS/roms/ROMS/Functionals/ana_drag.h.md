---
file: models/ROMS/raw/source_code/roms/ROMS/Functionals/ana_drag.h
lines: 287
sha256: cdeb60bed926192fe7b5820bfcbcdcf98eead846d56144160751f8b04fe9f046
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# ana_drag.h — 판독 구간 기록

구간은 1행부터 287행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–71 | ana_drag 시작(2), 저작권·라이선스(4–9). RHO점(RHO-point)의 해저 거칠기 길이(bottom roughness length, m), 선형 항력 계수(linear drag coefficient, m/s), 이차 항력 계수(quadratic drag coefficient, 무차원)를 설정한다는 주석(11–26). 모듈·인수·MyFile(30–41), `#include "tile.h"` (43)로 tile.h를 끼워 넣는다. ana_drag_tile 호출(45–57)의 `#if defined SEDIMENT \|\| defined BBL_MODEL` (48)에서 SEDBED(ng)%bottom 전달(49), `#endif` (50). `#if defined UV_LOGDRAG` (51)는 GRID%ZoBot(52), `#elif defined UV_LDRAG` (53)는 GRID%rdrag(54), `#elif defined UV_QDRAG` (55)는 GRID%rdrag2(56), `#endif` (57). `#ifdef DISTRIBUTE` (61)의 `IF (Lanafile) THEN` (62), `#else` (63)의 `IF (Lanafile.and.(tile.eq.0)) THEN` (64), `#endif` (65) 뒤 ANANAME(2)=MyFile(66). 조건 종료·RETURN·루틴 종료·주석(67–71). |
| 72–109 | ana_drag_tile 시작(73–85). 인수 목록의 `#if defined SEDIMENT \|\| defined BBL_MODEL` (76)는 bottom(77), `#endif` (78). `#if defined UV_LOGDRAG` (79)는 ZoBot(80), `#elif defined UV_LDRAG` (81)는 rdrag(82), `#elif defined UV_QDRAG` (83)는 rdrag2(84), `#endif` (85). 공통 모듈(88–93), `#if defined SEDIMENT \|\| defined BBL_MODEL` (94)에서 mod_sediment 사용(95), `#endif` (96). exchange_r2d_tile(98), `#ifdef DISTRIBUTE` (99)에서 mp_exchange2d 사용(100), `#endif` (101), stats_2dfld 사용(102). 인수 선언(106–108), 주석(109). |
| 110–134 | 시작 시 73행 ana_drag_tile 안. `#ifdef ASSUMED_SHAPE` (110)에서 `# if defined SEDIMENT \|\| defined BBL_MODEL` (111)는 bottom assumed-shape 배열(112), `# endif` (113). `# if defined UV_LOGDRAG` (114)는 ZoBot(115), `# elif defined UV_LDRAG` (116)는 rdrag(117), `# elif defined UV_QDRAG` (118)는 rdrag2(119), `# endif` (120). 외부 `#else` (122) 안 `# if defined SEDIMENT \|\| defined BBL_MODEL` (124)는 bottom(LBi:UBi,LBj:UBj,MBOTP)(125), `# endif` (126). `# if defined UV_LOGDRAG` (127)는 ZoBot(128), `# elif defined UV_LDRAG` (129)는 rdrag(130), `# elif defined UV_QDRAG` (131)는 rdrag2(132), `# endif` (133); `#endif` (134). 각 항력 배열은 intent(out)이다. |
| 135–171 | 시작 시 73행 ana_drag_tile 안. `logical, save :: first = .TRUE.` (138)와 i·j·cff·저장 속성 Stats 선언(140–144). `#include "set_bounds.h"` (146)로 set_bounds.h를 끼워 넣는다. `IF (first) THEN` (152)는 first를 거짓으로 바꾸고 Stats checksum·count·avg·rms를 0으로 설정(153–155·158–159), `Stats % min=Large` (156); `Stats % max=-Large` (157). `#if defined UV_LOGDRAG` (163)의 주석은 거칠기 길이 m(164), `#elif defined UV_LDRAG` (165)의 주석은 선형 계수 m/s(166), `#elif defined UV_QDRAG` (167)의 주석은 이차 계수 무차원(168), `#endif` (169). 조건 종료·구분 주석 포함. |
| 172–193 | 시작 시 73행 ana_drag_tile 안. `#if defined UPWELLING` (172). `# if defined UV_LOGDRAG` (173)의 j·i 루프(174–175)는 `ZoBot(i,j)=0.05_r8*(1.0_r8+TANH(GRID(ng)%h(i,j)/50.0_r8))` (176). `# elif defined UV_LDRAG` (179)의 j·i 루프(180–181)는 `rdrag(i,j)=0.002_r8*(1.0_r8-TANH(GRID(ng)%h(i,j)/150.0_r8))` (182). `# elif defined UV_QDRAG` (185)의 j·i 루프(186–187)는 Chezy 계수(Chezy coefficient) 주석과 `cff=1.8_r8*GRID(ng)%h(i,j)*LOG(GRID(ng)%h(i,j))` (188); `rdrag2(i,j)=g/(cff*cff)` (189). 각 루프 종료(177–178·183–184·190–191), `# endif` (192). `#else` (193)는 UPWELLING 불성립 분기를 연다. |
| 194–216 | 시작 시 73행 ana_drag_tile·172행 `#if defined UPWELLING`의 193행 `#else` 안. `# if defined UV_LOGDRAG` (194)의 j·i 루프(195–196)는 `ZoBot(i,j)=???` (197). `# elif defined UV_LDRAG` (200)의 j·i 루프(201–202)는 `rdrag(i,j)=???` (203). `# elif defined UV_QDRAG` (206)의 j·i 루프(207–208)는 `rdrag2(i,j)=???` (209). 루프 종료(198–199·204–205·210–211), `# endif` (212); `#endif` (213). 통계 출력 주석(215–216). |
| 217–240 | 시작 시 73행 ana_drag_tile 안. `#if defined UV_LOGDRAG` (217)에서 stats_2dfld(...,ZoBot) 호출(218–219), `IF (DOMAIN(ng)%NorthEast_Corner(tile)) THEN` (220)이면 설명·ng·Stats 최솟값·최댓값 출력(221–223). `#elif defined UV_LDRAG` (225)에서 stats_2dfld(...,rdrag) 호출(226–227), `IF (DOMAIN(ng)%NorthEast_Corner(tile)) THEN` (228)이면 같은 통계 출력(229–230). `#elif defined UV_QDRAG` (232)에서 stats_2dfld(...,rdrag2) 호출(233–234), `IF (DOMAIN(ng)%NorthEast_Corner(tile)) THEN` (235)이면 같은 통계 출력(236–237). 조건 종료(224·231·238), `#endif` (239), 주석(240). |
| 241–268 | 시작 시 73행 ana_drag_tile 안. `IF (EWperiodic(ng).or.NSperiodic(ng)) THEN` (243)이면 exchange_r2d_tile 호출(244–252). 전달 배열은 `#if defined UV_LOGDRAG` (246)의 ZoBot(247), `#elif defined UV_LDRAG` (248)의 rdrag(249), `#elif defined UV_QDRAG` (250)의 rdrag2(251), `#endif` (252). 조건 종료(253), `#ifdef DISTRIBUTE` (255)에서 mp_exchange2d(...,1,...,NghostPoints,EWperiodic(ng),NSperiodic(ng),...) 호출(256–267). 전달 배열은 `# if defined UV_LOGDRAG` (260)의 ZoBot(261), `# elif defined UV_LDRAG` (262)의 rdrag(263), `# elif defined UV_QDRAG` (264)의 rdrag2(265), `# endif` (266); `#endif` (267). 빈 줄 포함(254·268). |
| 269–287 | 시작 시 73행 ana_drag_tile 안. `#if defined UV_LOGDRAG && (defined SEDIMENT \|\| defined BBL_MODEL)` (269). j·i 루프에서 bottom(i,j,izdef)에 ZoBot(i,j)를 복사(275–279), `#endif` (280). 통계 FORMAT(282–284), RETURN·루틴 종료(286–287), 주석·빈 줄 포함. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 193–213: UPWELLING이 아닌 분기의 ZoBot·rdrag·rdrag2 대입 우변은 모두 ???이다.
- 188–189: UPWELLING 이차 항력 식은 LOG(GRID(ng)%h(i,j))와 cff*cff 분모를 사용한다. 이 블록에는 수심이나 cff의 범위를 검사하는 조건이 없다.
- 138·144·152–160: first와 Stats에는 저장 속성이 있다. Stats 초기화는 first 조건 안에만 있으며 격자별 Stats 배열은 선언하지 않는다.
- 112·125·269–280: bottom은 intent(out) 배열이다. 이 파일에서 bottom 대입은 UV_LOGDRAG와 SEDIMENT 또는 BBL_MODEL의 결합 조건 안에서 izdef 성분에만 수행한다.
