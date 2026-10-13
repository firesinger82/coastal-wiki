---
file: models/ROMS/raw/source_code/roms/ROMS/Drivers/propagator_hop.h
lines: 378
sha256: 9e47943dee73ed632ebb2a63ded0bd899f88dd1d82108ed870e85901fece9350
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# propagator_hop.h — 판독 구간 기록

구간은 1행부터 378행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–41 | `propagator_mod` 시작(1), 저작권·MIT/X 라이선스 안내(3–8). 최적 섭동(optimal perturbation)과 헤시안 특이 벡터(Hessian singular vector)의 전파 연산자(propagator)는 지정 시간의 빠른 섭동 성장을 구한다는 주석(10–17). 접선 선형 모델(tangent linear model, TLM) 전진 적분 뒤 수반 모델(adjoint model, ADM)을 뒤로 적분한다고 적는다(15–17). Moore 등의 2004년 문헌 및 Smith 등의 2015년 논문·DOI 주석(19–28). mod_kinds·implicit none·PRIVATE·PUBLIC propagator_hop·CONTAINS·주석(32–41). |
| 42–81 | 시작 시 1행 모듈 안. propagator_hop(RunInterval,state,ad_state) 입구(42). 매개변수·병렬 모듈(45–46). `#ifdef SOLVE3D` (47)의 mod_coupling 사용(48), `#endif` (49). 상태·입출력·시간 모듈 및 close_inp, tl_statenorm, ad_ini_perturb, ad_inner2state/tl_inner2state, ini_C_norm 사용(50–59). `#ifdef SOLVE3D` (60)의 set_depth 사용(61), `#endif` (62). FoundError(63). RunInterval·state(Ngrids)는 입력, ad_state(Ngrids)는 inout(67–70). ng/tile·스칼라(scalar) ktmp/ntmp/Lini·StateNorm(Ngrids)·MyFile 선언(74–80), 주석(81). |
| 82–120 | 시작 시 42행 propagator_hop 안. `Nrun=Nrun+1` (86). `IF (Master) THEN` (87)의 격자(grid)별 반복·수렴 Ritz 값(Ritz value) 수 로그(88–94). 격자마다 iif/indx1/kstp/krhs/knew=1·PREDICTOR_2D_STEP=.FALSE.·iic=0·nstp/nrhs/nnew=1·synchro_flag=.TRUE.·tdays=dstart(98–112). `time(ng)=tdays(ng)*day2sec` (113), `ntstart(ng)=INT((time(ng)-dstart*day2sec)/dt(ng))+1` (114). ntend=ntimes·ntfirst=ntstart(115–116). Lini=1(119), 주석(120). |
| 121–156 | 시작 시 42행 propagator_hop 안. 순방향 타일(tile) 루프에서 initialize_ocean(ng,tile,iTLM)(127–131). `#ifdef SOLVE3D` (133)에서 정지 기본 상태(basic state) 두께를 시간 불변 노름(norm)에 쓴다는 주석(135–139). 역방향 타일 루프에서 set_depth(ng,tile,iTLM)(141–145), `#endif` (146). 순방향 타일 루프에서 tl_inner2state(ng,tile,Lini,state(ng)%vector)로 TLM 초기 조건을 구한다(152–156). |
| 157–188 | 시작 시 42행 propagator_hop 안. 역방향 타일 루프에서 ini_C_norm(ng,tile,kstp(ng),nstp(ng),StateNorm(ng))로 초기 분석 오차 노름(analysis-error norm)을 요청한다(158–166). `IF (Master) THEN` (167)의 초기 노름 로그(168–170). 격자마다 close_inp(ng,iTLM)(179–180), `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (181). tl_get_idata(ng)(183), `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (184). tl_get_data(ng)(186), `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (187), 루프 종료(188). |
| 189–207 | 시작 시 42행 propagator_hop 안. 격자 루프의 `IF (Master) THEN` (195)에서 TLM 적분 로그(196). `time(ng)=time(ng)-dt(ng)` (198), `iic(ng)=ntstart(ng)-1` (199). `#ifdef SOLVE3D` (202)의 tl_main3d(RunInterval)(203), `#else` (204)의 tl_main2d(RunInterval)(205), `#endif` (206). `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (207). |
| 208–252 | 시작 시 42행 propagator_hop 안. 순방향 타일 루프에서 initialize_ocean으로 iNLM 및 iADM 상태를 지운다(213–216). `#ifdef SOLVE3D` (217)의 initialize_coupling(ng,tile,0)(218), `#endif` (219). `#ifdef SOLVE3D` (223)의 정지 기본 상태 최종 두께 주석(225–229), 역방향 타일 루프에서 set_depth(ng,tile,iTLM)(231–235), `#endif` (236). 순방향 타일 루프에서 tl_statenorm(ng,tile,knew(ng),nstp(ng),StateNorm(ng))으로 최종 에너지 노름(energy norm)을 요청한다(238–246). `IF (Master) THEN` (247)의 최종 노름 로그(248–250), 루프 종료·주석(251–252). |
| 253–292 | 시작 시 42행 propagator_hop 안. ADM 역방향 적분 안내(253–258). 격자마다 ktmp=knew·ntmp=nstp를 보존하고 iif/indx1/kstp=1·krhs=3·knew=2·PREDICTOR_2D_STEP=.FALSE.·iic=0·nstp/nrhs=1·nnew=2·synchro_flag=.TRUE.(259–274). `tdays(ng)=dstart+dt(ng)*REAL(ntimes(ng),r8)*sec2day` (275), `time(ng)=tdays(ng)*day2sec` (276), `ntstart(ng)=ntimes(ng)+1` (277). ntend=1·ntfirst=ntend(278–279). 다음 격자·역방향 타일 루프에서 ad_ini_perturb(ng,tile,ktmp,knew(ng),ntmp,nstp(ng))로 최종 TLM 상태의 에너지 노름을 적용한 ADM 초기 조건을 요청한다(282–292). |
| 293–328 | 시작 시 42행 propagator_hop 안. 격자마다 close_inp(ng,iADM)(300–301), `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (302). ad_get_idata(ng)(304), `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (305). ad_get_data(ng)(307), `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (308). 격자 루프의 `IF (Master) THEN` (316)에서 ADM 적분 로그(317). `time(ng)=time(ng)+dt(ng)` (319), `iic(ng)=ntstart(ng)+1` (320). `#ifdef SOLVE3D` (323)의 ad_main3d(RunInterval)(324), `#else` (325)의 ad_main2d(RunInterval)(326), `#endif` (327). `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (328). |
| 329–359 | 시작 시 42행 propagator_hop 안. 순방향 타일 루프에서 initialize_ocean(ng,tile,iNLM)(336–338). `#ifdef SOLVE3D` (339)의 initialize_coupling(ng,tile,0)(340), `#endif` (341). `#ifdef SOLVE3D` (345)에서 초기 정지 기본 상태 두께 계산 안내(347–351). 역방향 타일 루프의 set_depth(ng,tile,iADM)(353–357), `#endif` (358), 주석(359). |
| 360–378 | 시작 시 42행 propagator_hop 안. 순방향 타일 루프에서 ad_inner2state(ng,tile,Lini,ad_state(ng)%vector)로 수반 상태 벡터를 구한다(364–368). 로그 FORMAT(370–373), RETURN·루틴 종료·빈 줄·모듈 종료(375–378). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 75·259–280·287–292: ktmp와 ntmp는 격자 차원이 없는 지역 스칼라이다. 첫 격자 루프가 각 격자의 knew와 nstp를 이 두 스칼라에 순서대로 대입한다. 다음 격자 루프는 ad_ini_perturb에 동일한 두 스칼라를 전달한다.
