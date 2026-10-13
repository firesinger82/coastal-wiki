---
file: models/ROMS/raw/source_code/roms/ROMS/Drivers/propagator_fte.h
lines: 293
sha256: 1b92d5906987be38a32d28c453413e4cd6ff6f9e5bae38052b6fb7f077ef1e85
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# propagator_fte.h — 판독 구간 기록

구간은 1행부터 293행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–35 | `propagator_mod` 시작(1), 저작권·MIT/X 라이선스 안내(3–8). 시간에 따라 변하는 순환을 선형화한 전파 연산자(propagator) R(0,t)의 유한 시간 고유모드(finite-time eigenmode, FTE)를 구한다는 주석(10–16). 접선 선형 모델(tangent linear model, TLM)로 임의 섭동 상태를 [0,t]에서 한 번 전진 적분한다고 적는다(14–16). Moore 등의 2004년 문헌(18–22). mod_kinds·implicit none·PRIVATE·PUBLIC propagator_fte·CONTAINS·주석(26–35). |
| 36–76 | 시작 시 1행 모듈 안. propagator_fte(RunInterval,state,tl_state) 입구(36). 매개변수·병렬 모듈(39–40). `#ifdef SOLVE3D` (41)에서 mod_coupling 사용(42), `#endif` (43). 상태·시간 모듈 및 close_inp, tl_statenorm, tl_unpack/tl_pack 사용(44–51). `#ifdef SOLVE3D` (52)에서 set_depth 사용(53), `#endif` (54). FoundError 사용(55). RunInterval·state(Ngrids)는 입력, tl_state(Ngrids)는 inout(59–62). `#ifdef SOLVE3D` (66)에서 `logical :: FirstPass = .TRUE.` (67), `#endif` (69). ng/tile·StateNorm(Ngrids)·MyFile 선언(70–75), 주석(76). |
| 77–118 | 시작 시 36행 propagator_fte 안. OpenMP MASTER 영역(81–91)의 `Nrun=Nrun+1` (82), `IF (Master) THEN` (83)에서 반복·수렴 Ritz 값(Ritz value) 수 로그(84–90). 격자(grid)마다 iif/indx1/kstp/krhs/knew=1·PREDICTOR_2D_STEP=.FALSE.·iic=0·nstp/nrhs/nnew=1·synchro_flag=.TRUE.·tdays=dstart(95–109). `time(ng)=tdays(ng)*day2sec` (110). MASTER 영역(111–115)의 `ntstart(ng)=INT((time(ng)-dstart*day2sec)/dt(ng))+1` (112), ntend=ntimes·ntfirst=ntstart(113–114). 격자 루프 종료·BARRIER·주석(116–118). |
| 119–158 | 시작 시 36행 propagator_fte 안. 순방향 타일(tile) 루프에서 initialize_ocean(ng,tile,iTLM) 호출 뒤 격자별 BARRIER(125–130). `#ifdef SOLVE3D` (132)에서 정지 기본 상태(basic state)의 두께를 시간 불변 노름(norm)에 쓴다는 주석(134–138). 역방향 타일 루프에서 set_depth(ng,tile,iTLM) 및 BARRIER(140–145), `#endif` (146). 순방향 타일 루프에서 tl_unpack(ng,tile,Nstr(ng),Nend(ng),state(ng)%vector) 및 BARRIER(152–158). |
| 159–197 | 시작 시 36행 propagator_fte 안. 역방향 타일 루프에서 tl_statenorm(ng,tile,kstp(ng),nstp(ng),StateNorm(ng))(164–168), BARRIER(169). MASTER 영역의 `IF (Master) THEN` (172)에서 초기 TLM 노름 로그(173–176). 다음 격자 루프 MASTER 영역에서 close_inp(ng,iTLM)(185–187), `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (188). tl_get_idata(ng)(190), `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (191). tl_get_data(ng)(193), MASTER 종료·BARRIER(194–195), `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (196), 루프 종료(197). |
| 198–220 | 시작 시 36행 propagator_fte 안. 격자 루프 MASTER 영역의 `IF (Master) THEN` (205)에서 적분 로그(206). `time(ng)=time(ng)-dt(ng)` (208), MASTER 종료(209), `iic(ng)=ntstart(ng)-1` (210), 격자 루프 종료·BARRIER(211–212). `#ifdef SOLVE3D` (214)에서 tl_main3d(RunInterval)(215), `#else` (216)에서 tl_main2d(RunInterval)(217), `#endif` (218). BARRIER(219), `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (220). |
| 221–253 | 시작 시 36행 propagator_fte 안. 기본 상태의 평균 자유 수면(free surface)을 지운다는 주석(222–226). 순방향 타일 루프의 initialize_ocean(ng,tile,iNLM)(228–230). `#ifdef SOLVE3D` (231)에서 initialize_coupling(ng,tile,0)(232), `#endif` (233), BARRIER(235). `#ifdef SOLVE3D` (238)에서 최종 정지 기본 상태 두께를 계산한다는 주석(240–244). 역방향 타일 루프의 set_depth(ng,tile,iTLM)과 BARRIER(246–251), `#endif` (252), 주석(253). |
| 254–272 | 시작 시 36행 propagator_fte 안. 순방향 타일 루프에서 tl_statenorm(ng,tile,knew(ng),nstp(ng),StateNorm(ng))(258–262), BARRIER(263). MASTER 영역의 `IF (Master) THEN` (266)에서 최종 TLM 노름 로그(267–270). 격자 루프 종료·주석(271–272). |
| 273–293 | 시작 시 36행 propagator_fte 안. 역방향 타일 루프에서 tl_pack(ng,tile,Nstr(ng),Nend(ng),tl_state(ng)%vector)(277–281), BARRIER(282), 격자 루프 종료(283). 로그 FORMAT(285–288), 빈 줄·RETURN·루틴 종료·빈 줄·모듈 종료(289–293). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 66–69: SOLVE3D의 지역 논리 FirstPass는 참으로 선언 초기화되며 이후 이 파일에서 사용되지 않는다.
