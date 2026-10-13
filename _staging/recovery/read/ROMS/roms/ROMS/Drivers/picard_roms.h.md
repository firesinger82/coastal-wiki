---
file: models/ROMS/raw/source_code/roms/ROMS/Drivers/picard_roms.h
lines: 387
sha256: 13af24497d19bafc5a0ae38dac5a6ac2f9494d3c9a36bde811b685ffbe96a5fa
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# picard_roms.h — 판독 구간 기록

구간은 1행부터 387행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–33 | `roms_kernel_mod` 시작(1), 저작권·MIT/X 라이선스·License_ROMS.md 안내(3–8). Picard 반복(Picard iteration) 드라이버의 목적은 약한 제약 4차원 변분 자료동화(weak-constraint four-dimensional variational data assimilation, R4D-Var)의 대표자(representer) 접선 선형 모델(tangent linear model)을 시험하는 것이다(10–16). 주석 식은 `!         d(S')/d(t) = N(So) + A(S' - So)                              !` (18). So는 이전 반복의 접선 선형 해라는 주석(20–22). 세 제어 루틴 안내 및 구분 주석(24–33). |
| 34–62 | 시작 시 1행 모듈 안. 매개변수·병렬·배열·입출력·스칼라(scalar) 및 close_file/close_inp/close_out·inp_par 사용(34–42). `#ifdef MCT_LIB` (43), `# ifdef ATM_COUPLING` (44)에서 initialize_ocn2atm_coupling 사용(45), `# endif` (46). `# ifdef WAV_COUPLING` (47)에서 initialize_ocn2wav_coupling 사용(48), `# endif` (49), `#endif` (50). stdout_unit/FoundError/wrt_rst 사용(51–53). implicit none·PUBLIC·CONTAINS·주석(55–62). |
| 63–92 | 시작 시 1행 모듈 안. ROMS_initialize(first,mpiCOMM) 입구·초기화 목적(63–70). first는 inout, mpiCOMM은 optional 입력(74–76). `logical :: allocate_vars = .TRUE.` (80). `#ifdef DISTRIBUTE` (82), MyError/MySize 선언(83), `#endif` (84). 타일(tile)·격자(grid)·스레드(thread) 변수(85). `#ifdef _OPENMP` (86), my_threadnum 선언(87), `#endif` (88). MyFile 선언·빈 줄(90–92). |
| 93–114 | 시작 시 63행 ROMS_initialize 안. `#ifdef DISTRIBUTE` (93)의 `IF (PRESENT(mpiCOMM)) THEN` (99)이면 입력 통신자(communicator) 사용(100), `ELSE` (101)이면 MPI_COMM_WORLD 사용(102). mpi_comm_rank/mpi_comm_size 호출(104–105), `#endif` (106). 최초 호출 및 앙상블(ensemble) 재호출을 설명하는 주석(108–114). |
| 115–146 | 시작 시 63행 ROMS_initialize 안. `IF (first) THEN` (115)의 first=.FALSE.(116), initialize_parallel(121). `IF (Set_StdOutUnit) THEN` (131)에서 `stdout=stdout_unit(Master)` (132), Set_StdOutUnit=.FALSE.(133). inp_par(iNLM)(140), `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (141). 타일(tile) 범위의 최초 설정 주석(143–146). |
| 147–188 | 시작 시 63행 ROMS_initialize·115행 first 참 분기 안. OpenMP 병렬 영역(147·160). `#if defined _OPENMP` (148)의 `MyThread=my_threadnum()` (149), `#elif defined DISTRIBUTE` (150)의 MyRank 복사(151), `#else` (152)의 MyThread=0(153), `#endif` (154). 격자 루프의 `chunk_size=(NtileX(ng)*NtileE(ng)+numthreads-1)/numthreads` (156), `first_tile(ng)=MyThread*chunk_size` (157), `last_tile (ng)=first_tile(ng)+chunk_size-1` (158). `IF (Master) THEN` (166)의 프로세스 로그(167–169). 격자 루프 내부의 OpenMP 영역에서 THREAD_RANGE별 wclock_on(ng,iNLM,0,...)(171–177). 별도 OpenMP 영역에서 ROMS_allocate_arrays·ROMS_initialize_arrays(181–184), `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (185). first 분기 종료·빈 줄(187–188). |
| 189–207 | 시작 시 63행 ROMS_initialize 안. `#if defined MCT_LIB && (defined ATM_COUPLING \|\| defined WAV_COUPLING)` (189)의 격자 루프(195–202). `# ifdef ATM_COUPLING` (196)에서 initialize_ocn2atm_coupling(ng,MyRank)(197), `# endif` (198). `# ifdef WAV_COUPLING` (199)에서 initialize_ocn2wav_coupling(ng,MyRank)(200), `# endif` (201), `#endif` (203). RETURN·루틴 종료·주석(205–207). |
| 208–233 | 시작 시 1행 모듈 안. ROMS_run(RunInterval) 입구·지정된 초 단위 구간의 대표자 모델 적분 목적(208–219). ng와 MyFile 선언(223–226), 앙상블 매개변수를 Picard 반복에 쓴다는 주석(228–233). |
| 234–258 | 시작 시 208행 ROMS_run 안. `ITER_LOOP : DO Nrun=ERstr,ERend` (234). 격자마다 TLM 파일명에는 Nrun, FWD 파일명에는 `Nrun-1`을 사용한다(239–241). 원문은 `WRITE (TLM(ng)%name,10) TRIM(TLM(ng)%head), Nrun` (240), `WRITE (FWD(ng)%name,10) TRIM(TLM(ng)%head), Nrun-1` (241). `IF (Master) THEN` (243)에서 반복 번호·두 파일명 로그(244–247). 다음 격자 루프는 iic=0·LdefTLM/LwrtTLM=.TRUE.·LdefRST=.FALSE.로 설정한다(253–258). |
| 259–285 | 시작 시 208행 ROMS_run·234행 ITER_LOOP 안. 격자마다 OpenMP 영역에서 rp_initial(ng) 호출(262–265), `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (266). `IF (Master) THEN` (272)의 대표자 적분 로그(273). OpenMP 영역(277–283) 내부의 `#ifdef SOLVE3D` (278)에서는 rp_main3d(RunInterval)(279), `#else` (280)에서는 rp_main2d(RunInterval)(281), `#endif` (282). `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (284), 주석(285). |
| 286–307 | 시작 시 208행 ROMS_run·234행 ITER_LOOP 안. 격자마다 close_file(ng,iRPM,TLM(ng))(288–289), `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (290). close_file(ng,iRPM,FWD(ng))(292), `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (293). 격자·ITER_LOOP 종료(294–296). 파일명 FORMAT은 `10   FORMAT (a,'_',i3.3,'.nc')` (298). 반복·파일명·적분 로그 FORMAT(299–303). RETURN·루틴 종료·주석(305–307). |
| 308–349 | 시작 시 1행 모듈 안. ROMS_finalize 입구와 비선형 모델(nonlinear model) 종료라는 주석(308–314), Fcount/ng/thread 및 MyFile 선언(318–321). `IF (exit_flag.eq.1) THEN` (329) 안 격자 루프의 `IF (LwrtRST(ng)) THEN` (331), `IF (Master) WRITE (stdout,10)` (332). Fcount 복사(335). `IF (LcycleRST(ng).and.(RST(ng)%Nrec(Fcount).ge.2)) THEN` (336)이면 Rindex=2·LcycleRST=.FALSE.(337–338). blowup 보존·exit_flag=NoError(340–341). `#ifdef DISTRIBUTE` (342)의 wrt_rst(ng,MyRank)(343), `#else` (344)의 wrt_rst(ng,-1)(345), `#endif` (346). 조건·루프 종료(347–349). |
| 350–387 | 시작 시 308행 ROMS_finalize 안. `IF (Master) THEN` (358)에서 경과 시간 로그(359–361). 격자마다 OpenMP 영역·THREAD_RANGE 루프에서 wclock_off(ng,iNLM,0,...)(363–369). OpenMP 영역에서 memory 호출(373–375). 격자마다 close_inp(ng,iNLM)(379–381), close_out(382). RETURN·루틴 종료·빈 줄·모듈 종료(384–387). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 250–257: 주석은 각 반복에서 이력 파일과 재시작 파일 정의를 활성화한다고 적는다. 실행문은 LdefTLM을 참으로 설정하고 LdefRST를 거짓으로 설정한다.
- 264·279·281·312·366·380: 적분 경로는 rp_initial과 rp_main3d/rp_main2d를 호출한다. 종료 루틴 설명은 nonlinear model이라고 적으며 시간 계측과 입력 닫기에는 iNLM을 전달한다.
