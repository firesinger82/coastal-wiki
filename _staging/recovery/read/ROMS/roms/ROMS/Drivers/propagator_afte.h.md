---
file: models/ROMS/raw/source_code/roms/ROMS/Drivers/propagator_afte.h
lines: 267
sha256: d84dc41ea2c201d73159ae2546eb406e8a61cfc4bd9d1466a7a21604eac6c380
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# propagator_afte.h — 판독 구간 기록

구간은 1행부터 267행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–35 | `propagator_mod` 시작(1). 저작권·MIT/X 라이선스·License_ROMS.md 안내(3–8). 수반 유한 시간 고유값(adjoint finite-time eigenvalue) 전파 연산자(propagator)는 임의 상태 u를 [t,0]에서 뒤로 적분하여 transpose[R(t,0)]*u를 얻는다는 주석(10–16). Moore 등의 2004년 문헌 주석(18–22). mod_kinds·implicit none·PRIVATE·PUBLIC propagator_afte·CONTAINS·구분 주석(26–35). |
| 36–76 | 시작 시 1행 모듈 안. propagator_afte(RunInterval,state,ad_state) 입구(36). 매개변수·병렬 모듈(39–40). `#ifdef SOLVE3D` (41)의 mod_coupling 사용(42), `#endif` (43). 상태·입출력·시간 모듈 및 close_inp, ad_statenorm, ad_unpack/ad_pack 사용(44–51). `#ifdef SOLVE3D` (52)의 set_depth 사용(53), `#endif` (54). FoundError 사용(55). RunInterval은 입력, state(Ngrids)는 입력, ad_state(Ngrids)는 inout인 T_GST 배열(59–62). `#ifdef SOLVE3D` (66)에서 `logical :: FirstPass = .TRUE.` (67), `#endif` (68). 격자(grid)·타일(tile)·StateNorm 및 MyFile 선언(70–75), 주석(76). |
| 77–112 | 시작 시 36행 propagator_afte 안. 주석은 접선 선형 모델(tangent linear model)의 전진 적분이라고 적는다(77–79). `Nrun=Nrun+1` (81). `IF (Master) THEN` (82)의 격자 루프에서 반복 번호·수렴 Ritz 값(Ritz value) 수 Nconv 로그(83–89). 격자마다 iif/indx1/kstp=1·krhs=3·knew=2·PREDICTOR_2D_STEP=.FALSE.·iic=0·nstp/nrhs=1·nnew=2·synchro_flag=.TRUE.(93–106). 시간 식은 `tdays(ng)=dstart+dt(ng)*REAL(ntimes(ng),r8)*sec2day` (107), `time(ng)=tdays(ng)*day2sec` (108), `ntstart(ng)=ntimes(ng)+1` (109). ntend=1·ntfirst=ntend(110–111), 루프 종료(112). |
| 113–139 | 시작 시 36행 propagator_afte 안. 격자·순방향 타일 루프에서 initialize_ocean(ng,tile,iADM)로 수반 상태를 지운다(120–124). `#ifdef SOLVE3D` (126)에서 정지 기본 상태(basic state)의 층 두께를 노름(norm) 스케일에 쓴다는 주석(128–132). 역방향 타일 루프에서 set_depth(ng,tile,iADM)(134–138). `#endif` (139). |
| 140–166 | 시작 시 36행 propagator_afte 안. 순방향 타일 루프에서 ad_unpack(ng,tile,Nstr(ng),Nend(ng),state(ng)%vector)로 수반 초기 상태를 풀어 놓는다(145–150). 역방향 타일 루프에서 ad_statenorm(ng,tile,knew(ng),nstp(ng),StateNorm(ng))(156–160). `IF (Master) THEN` (161)에서 초기 수반 노름 로그(162–164), 격자 루프 종료·주석(165–166). |
| 167–202 | 시작 시 36행 propagator_afte 안. 격자마다 close_inp(ng,iADM)(173–174), `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (175). ad_get_idata(ng)(177), `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (178). ad_get_data(ng)(180), `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (181). 적분 전 격자 루프의 `IF (Master) THEN` (189)에서 로그(190). `time(ng)=time(ng)+dt(ng)` (192), `iic(ng)=ntstart(ng)+1` (193). `#ifdef SOLVE3D` (196)에서 ad_main3d(RunInterval)(197), `#else` (198)에서 ad_main2d(RunInterval)(199), `#endif` (200). `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (201), 주석(202). |
| 203–232 | 시작 시 36행 propagator_afte 안. 기본 상태와 평균 자유 수면(free surface)을 지운다는 주석(203–207). 순방향 타일 루프에서 initialize_ocean(ng,tile,iNLM)(209–211). `#ifdef SOLVE3D` (212)에서 initialize_coupling(ng,tile,0)(213), `#endif` (214). `#ifdef SOLVE3D` (218)의 정지 기본 상태 최종 두께 주석(220–224). 역방향 타일 루프에서 set_depth(ng,tile,iADM)(226–230). `#endif` (231), 주석(232). |
| 233–267 | 시작 시 36행 propagator_afte 안. 순방향 타일 루프에서 ad_statenorm(ng,tile,knew(ng),nstp(ng),StateNorm(ng))(237–241). `IF (Master) THEN` (242)에서 최종 수반 노름 로그(243–245). 역방향 타일 루프에서 ad_pack(ng,tile,Nstr(ng),Nend(ng),ad_state(ng)%vector)로 최종 상태를 포장한다(252–257). 로그 FORMAT(259–262), RETURN·루틴 종료·빈 줄·모듈 종료(264–267). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 66–68: SOLVE3D의 지역 논리 FirstPass는 참으로 선언 초기화되며 이후 이 파일에서 사용되지 않는다.
- 78·185·197·199: 첫 실행 절의 제목은 접선 선형 모델의 전진 적분이라고 적는다. 실제 적분 호출은 ad_main3d/ad_main2d이고 적분 앞 주석은 수반 모델의 역방향 적분이라고 적는다.
