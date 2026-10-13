---
file: models/ROMS/raw/source_code/roms/ROMS/Drivers/propagator_op.h
lines: 372
sha256: d5c5f8fd2428b53a516b2e1f755a908bd0999ba9ec34d11780ec45230dce474d
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# propagator_op.h — 판독 구간 기록

구간은 1행부터 372행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–36 | `propagator_mod` 시작(1), 저작권·MIT/X 라이선스 안내(3–8). 최적 섭동(optimal perturbation) 특이 벡터(singular vector)의 전파 연산자(propagator)는 접선 선형 모델(tangent linear model, TLM)의 [0,t] 전진 적분 뒤 수반 모델(adjoint model, ADM)의 [t,0] 역방향 적분을 수행한다는 주석(10–17). Moore 등의 2004년 문헌(19–23). mod_kinds·implicit none·PRIVATE·PUBLIC propagator_op·CONTAINS·주석(27–36). |
| 37–75 | 시작 시 1행 모듈 안. propagator_op(RunInterval,state,ad_state) 입구(37). 매개변수·병렬 모듈(40–41). `#ifdef SOLVE3D` (42)의 mod_coupling 사용(43), `#endif` (44). 상태·입출력·시간 모듈 및 close_inp, tl_statenorm, ad_ini_perturb, tl_unpack/ad_pack 사용(45–53). `#ifdef SOLVE3D` (54)의 set_depth 사용(55), `#endif` (56). FoundError(57). RunInterval·state(Ngrids)는 입력, ad_state(Ngrids)는 inout(61–64). ng/tile·스칼라(scalar) ktmp/ntmp·StateNorm(Ngrids)·MyFile 선언(68–74), 주석(75). |
| 76–112 | 시작 시 37행 propagator_op 안. `Nrun=Nrun+1` (80). `IF (Master) THEN` (81)의 격자(grid)별 반복·수렴 Ritz 값(Ritz value) 수 로그(82–88). 격자마다 iif/indx1/kstp/krhs/knew=1·PREDICTOR_2D_STEP=.FALSE.·iic=0·nstp/nrhs/nnew=1·synchro_flag=.TRUE.·tdays=dstart(92–106). `time(ng)=tdays(ng)*day2sec` (107), `ntstart(ng)=INT((time(ng)-dstart*day2sec)/dt(ng))+1` (108). ntend=ntimes·ntfirst=ntstart(109–110), 루프 종료·주석(111–112). |
| 113–149 | 시작 시 37행 propagator_op 안. 순방향 타일(tile) 루프의 initialize_ocean(ng,tile,iTLM)(119–123). `#ifdef SOLVE3D` (125)에서 정지 기본 상태(basic state)의 두께를 시간 불변 노름(norm)에 쓴다는 주석(127–131). 역방향 타일 루프의 set_depth(ng,tile,iTLM)(133–137), `#endif` (138). 순방향 타일 루프의 tl_unpack(ng,tile,Nstr(ng),Nend(ng),state(ng)%vector)(144–149). |
| 150–181 | 시작 시 37행 propagator_op 안. 역방향 타일 루프의 tl_statenorm(ng,tile,kstp(ng),nstp(ng),StateNorm(ng))(155–159). `IF (Master) THEN` (160)의 초기 TLM 노름 로그(161–163). 격자마다 close_inp(ng,iTLM)(172–173), `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (174). tl_get_idata(ng)(176), `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (177). tl_get_data(ng)(179), `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (180), 격자 루프 종료(181). |
| 182–200 | 시작 시 37행 propagator_op 안. 격자 루프의 `IF (Master) THEN` (188)에서 적분 로그(189). `time(ng)=time(ng)-dt(ng)` (191), `iic(ng)=ntstart(ng)-1` (192). `#ifdef SOLVE3D` (195)의 tl_main3d(RunInterval)(196), `#else` (197)의 tl_main2d(RunInterval)(198), `#endif` (199). `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (200). |
| 201–245 | 시작 시 37행 propagator_op 안. 순방향 타일 루프의 initialize_ocean으로 iNLM 및 iADM 상태를 지운다(206–209). `#ifdef SOLVE3D` (210)의 initialize_coupling(ng,tile,0)(211), `#endif` (212). `#ifdef SOLVE3D` (216)에서 정지 기본 상태 최종 두께 안내(218–222). 역방향 타일 루프의 set_depth(ng,tile,iTLM)(224–228), `#endif` (229). 순방향 타일 루프의 tl_statenorm(ng,tile,knew(ng),nstp(ng),StateNorm(ng))(235–239). `IF (Master) THEN` (240)에서 최종 TLM 노름 로그(241–243), 루프 종료·주석(244–245). |
| 246–285 | 시작 시 37행 propagator_op 안. 수반 역방향 적분 안내(246–251). 격자마다 ktmp=knew·ntmp=nstp를 보존하고 iif/indx1/kstp=1·krhs=3·knew=2·PREDICTOR_2D_STEP=.FALSE.·iic=0·nstp/nrhs=1·nnew=2·synchro_flag=.TRUE.(252–267). `tdays(ng)=dstart+dt(ng)*REAL(ntimes(ng),r8)*sec2day` (268), `time(ng)=tdays(ng)*day2sec` (269), `ntstart(ng)=ntimes(ng)+1` (270). ntend=1·ntfirst=ntend(271–272). 다음 격자·역방향 타일 루프의 ad_ini_perturb(ng,tile,ktmp,knew(ng),ntmp,nstp(ng))로 최종 TLM 상태의 에너지 노름(energy norm)을 적용한 ADM 초기 조건을 요청한다(275–285). |
| 286–321 | 시작 시 37행 propagator_op 안. 격자마다 close_inp(ng,iADM)(293–294), `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (295). ad_get_idata(ng)(297), `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (298). ad_get_data(ng)(300), `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (301). 격자 루프의 `IF (Master) THEN` (309)에서 ADM 적분 로그(310). `time(ng)=time(ng)+dt(ng)` (312), `iic(ng)=ntstart(ng)+1` (313). `#ifdef SOLVE3D` (316)의 ad_main3d(RunInterval)(317), `#else` (318)의 ad_main2d(RunInterval)(319), `#endif` (320). `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (321). |
| 322–352 | 시작 시 37행 propagator_op 안. 순방향 타일 루프의 initialize_ocean(ng,tile,iNLM)(329–331). `#ifdef SOLVE3D` (332)의 initialize_coupling(ng,tile,0)(333), `#endif` (334). `#ifdef SOLVE3D` (338)에서 정지 기본 상태 초기 두께 안내(340–344). 역방향 타일 루프의 set_depth(ng,tile,iADM)(346–350), `#endif` (351), 주석(352). |
| 353–372 | 시작 시 37행 propagator_op 안. 순방향 타일 루프의 ad_pack(ng,tile,Nstr(ng),Nend(ng),ad_state(ng)%vector)(357–362). 로그 FORMAT(364–367), RETURN·루틴 종료·빈 줄·모듈 종료(369–372). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 69·252–273·280–285: ktmp와 ntmp는 격자 차원이 없는 지역 스칼라이다. 첫 격자 루프가 각 격자의 knew와 nstp를 이 두 스칼라에 순서대로 대입한다. 다음 격자 루프는 ad_ini_perturb에 동일한 두 스칼라를 전달한다.
