---
file: models/ROMS/raw/source_code/roms/ROMS/Drivers/propagator_fsv.h
lines: 385
sha256: 8f16634d0a3699ad5d2fd1c52664ae6c13081f688b9ce6a3defc303522198747
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# propagator_fsv.h — 판독 구간 기록

구간은 1행부터 385행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–36 | `propagator_mod` 시작(1), 저작권·MIT/X 라이선스 안내(3–8). 강제력 특이 벡터(forcing singular vector) 전파 연산자(propagator)는 접선 선형 모델(tangent linear model, TLM)의 [0,t] 전진 적분 뒤 수반 모델(adjoint model, ADM)의 [t,0] 역방향 적분을 수행한다는 주석(10–17). Moore 등의 2004년 문헌(19–23). mod_kinds·implicit none·PRIVATE·PUBLIC propagator_fsv·CONTAINS·구분 주석(27–36). |
| 37–76 | 시작 시 1행 모듈 안. propagator_fsv(RunInterval,state,ad_state) 입구(37). 매개변수·병렬 모듈(40–41). `#ifdef SOLVE3D` (42)의 mod_coupling 사용(43), `#endif` (44). 상태·시간 모듈 및 close_inp, tl_statenorm, ad_ini_perturb, tl_unpack/ad_pack, initialize_forces 사용(45–54). `#ifdef SOLVE3D` (55)의 set_depth 사용(56), `#endif` (57). FoundError 사용(58). RunInterval·state(Ngrids)는 입력, ad_state(Ngrids)는 inout(62–65). ng/tile·스칼라(scalar) ktmp/ntmp·StateNorm(Ngrids) 및 MyFile 선언(69–75), 주석(76). |
| 77–112 | 시작 시 37행 propagator_fsv 안. `Nrun=Nrun+1` (81). `IF (Master) THEN` (82)에서 격자(grid)별 반복·수렴 Ritz 값(Ritz value) 수 로그(83–89). 격자마다 iif/indx1/kstp/krhs/knew=1·PREDICTOR_2D_STEP=.FALSE.·iic=0·nstp/nrhs/nnew=1·synchro_flag=.TRUE.·tdays=dstart(93–107). `time(ng)=tdays(ng)*day2sec` (108), `ntstart(ng)=INT((time(ng)-dstart*day2sec)/dt(ng))+1` (109). ntend=ntimes·ntfirst=ntstart(110–111), 루프 종료(112). |
| 113–150 | 시작 시 37행 propagator_fsv 안. 순방향 타일(tile) 루프에서 initialize_ocean(ng,tile,iTLM)(120–124). `#ifdef SOLVE3D` (126)의 정지 기본 상태(basic state) 두께와 시간 불변 노름(norm) 주석(128–132). 역방향 타일 루프에서 set_depth(ng,tile,iTLM)(134–138), `#endif` (139). 순방향 타일 루프에서 tl_unpack(ng,tile,Nstr(ng),Nend(ng),state(ng)%vector)(145–150). |
| 151–182 | 시작 시 37행 propagator_fsv 안. 역방향 타일 루프에서 tl_statenorm(ng,tile,kstp(ng),nstp(ng),StateNorm(ng))(156–160). `IF (Master) THEN` (161)의 초기 TLM 노름 로그(162–164). 격자마다 close_inp(ng,iTLM)(173–174), `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (175). tl_get_idata(ng)(177), `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (178). tl_get_data(ng)(180), `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (181), 격자 루프 종료(182). |
| 183–201 | 시작 시 37행 propagator_fsv 안. `IF (Master) THEN` (189)에서 TLM 적분 로그(190). `time(ng)=time(ng)-dt(ng)` (192), `iic(ng)=ntstart(ng)-1` (193). `#ifdef SOLVE3D` (196)의 tl_main3d(RunInterval)(197), `#else` (198)의 tl_main2d(RunInterval)(199), `#endif` (200). `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (201). |
| 202–246 | 시작 시 37행 propagator_fsv 안. 순방향 타일 루프에서 initialize_ocean으로 iNLM·iADM 상태를 지운다(207–210). `#ifdef SOLVE3D` (211)의 initialize_coupling(ng,tile,0)(212), `#endif` (213). `#ifdef SOLVE3D` (217)에서 정지 기본 상태 최종 두께 주석(219–223), 역방향 타일 루프의 set_depth(ng,tile,iADM)(225–229), `#endif` (230). 순방향 타일 루프에서 tl_statenorm(ng,tile,knew(ng),nstp(ng),StateNorm(ng))(236–240). `IF (Master) THEN` (241)의 최종 TLM 노름 로그(242–244), 루프 종료·주석(245–246). |
| 247–286 | 시작 시 37행 propagator_fsv 안. 수반 역방향 적분 안내(247–252). 격자마다 ktmp=knew·ntmp=nstp를 보존하고 iif/indx1/kstp=1·krhs=3·knew=2·PREDICTOR_2D_STEP=.FALSE.·iic=0·nstp/nrhs=1·nnew=2·synchro_flag=.TRUE.(253–268). `tdays(ng)=dstart+dt(ng)*REAL(ntimes(ng),r8)*sec2day` (269), `time(ng)=tdays(ng)*day2sec` (270), `ntstart(ng)=ntimes(ng)+1` (271). ntend=1·ntfirst=ntend(272–273). 다음 격자·역방향 타일 루프에서 ad_ini_perturb(ng,tile,ktmp,knew(ng),ntmp,nstp(ng))로 에너지 노름(energy norm)을 적용한 최종 TLM 상태를 ADM 초기 상태로 요청한다(276–286). |
| 287–322 | 시작 시 37행 propagator_fsv 안. 격자마다 close_inp(ng,iADM)(294–295), `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (296). ad_get_idata(ng)(298), `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (299). ad_get_data(ng)(301), `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (302). `IF (Master) THEN` (310)의 ADM 적분 로그(311). `time(ng)=time(ng)+dt(ng)` (313), `iic(ng)=ntstart(ng)+1` (314). `#ifdef SOLVE3D` (317)의 ad_main3d(RunInterval)(318), `#else` (319)의 ad_main2d(RunInterval)(320), `#endif` (321). `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (322). |
| 323–353 | 시작 시 37행 propagator_fsv 안. 순방향 타일 루프에서 initialize_ocean(ng,tile,iNLM)(330–332). `#ifdef SOLVE3D` (333)의 initialize_coupling(ng,tile,0)(334), `#endif` (335). `#ifdef SOLVE3D` (339)에서 초기 정지 상태 두께를 다시 계산한다는 주석(341–345). 역방향 타일 루프의 set_depth(ng,tile,iADM)(347–351), `#endif` (352), 주석(353). |
| 354–385 | 시작 시 37행 propagator_fsv 안. 순방향 타일 루프의 ad_pack(ng,tile,Nstr(ng),Nend(ng),ad_state(ng)%vector)(358–363), `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (364). 다음 순방향 타일 루프에서 initialize_forces를 iTLM 및 iADM에 각각 호출한다(370–375). 로그 FORMAT(377–380), RETURN·루틴 종료·빈 줄·모듈 종료(382–385). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 70·253–274·281–286: ktmp와 ntmp는 격자 차원이 없는 지역 스칼라이다. 첫 격자 루프는 각 격자의 knew와 nstp를 이 두 스칼라에 순서대로 대입한다. 다음 격자 루프는 ad_ini_perturb에 동일한 두 스칼라를 전달한다.
