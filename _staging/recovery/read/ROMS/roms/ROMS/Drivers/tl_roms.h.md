---
file: models/ROMS/raw/source_code/roms/ROMS/Drivers/tl_roms.h
lines: 370
sha256: 2d488ccef68b0fb4abaf7de1e767fd063c6f2c3ce2d22becfe8d611194608ae4
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# tl_roms.h — 판독 구간 기록

구간은 1행부터 370행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–49 | `roms_kernel_mod` 모듈 시작(1). 저작권·라이선스와 접선 선형 모델(tangent linear model)의 초기화·시간 적분·종료 드라이버 설명(2–21). 공통 모듈과 close_inp·close_out·inp_par를 가져옴(22–30). `#ifdef MCT_LIB` (31), `# ifdef ATM_COUPLING` (32)에서 initialize_ocn2atm_coupling을 가져오고 `# endif` (34). 같은 MCT_LIB 안 `# ifdef WAV_COUPLING` (35)에서 initialize_ocn2wav_coupling을 가져오고 `# endif` (37), `#endif` (38). stdout_unit·FoundError·wrt_rst 사용(39–41), implicit none과 공개 ROMS_initialize·ROMS_run·ROMS_finalize·CONTAINS(43–49). |
| 50–80 | 시작 시 1행 roms_kernel_mod 모듈 안. ROMS_initialize 시작(51), 목적 주석·인수 first와 선택 인수 mpiCOMM 선언(52–64). 기본값 선언 `logical :: allocate_vars = .TRUE.` (68). `#ifdef DISTRIBUTE` (70)는 MyError·MySize 선언을 감싸며 `#endif` (72). chunk_size·ng·thread 선언(73), `#ifdef _OPENMP` (74)에서 my_threadnum을 선언하고 `#endif` (76). MyFile에 파일명과 루틴명을 결합하는 매개변수 선언(78–79), 빈 줄·주석 포함. |
| 81–102 | 시작 시 51행 ROMS_initialize 안. `#ifdef DISTRIBUTE` (81). `IF (PRESENT(mpiCOMM)) THEN` (87)이면 OCN_COMM_WORLD에 mpiCOMM을 대입하고 `ELSE` (89)는 MPI_COMM_WORLD를 대입(88–90). mpi_comm_rank·mpi_comm_size 호출(92–93), `#endif` (94). 첫 호출에서 매개변수와 격자를 준비한다는 주석(96–102). |
| 103–134 | 시작 시 51행 ROMS_initialize 안. `IF (first) THEN` (103)에서 first를 거짓으로 바꾸고 initialize_parallel 호출(104–109). `IF (Set_StdOutUnit) THEN` (119)이면 stdout_unit(Master)를 stdout에 넣고 스위치를 끔(120–122). inp_par(iTLM) 호출(128). `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (129). 타일 분할(tile partition)을 한 번 계산한다는 주석(131–134). |
| 135–176 | 시작 시 51행 ROMS_initialize·103행 first 참 분기 안. OpenMP 병렬 지시(135). `#if defined _OPENMP` (136)는 MyThread=my_threadnum(), `#elif defined DISTRIBUTE` (138)는 MyThread=MyRank, `#else` (140)는 MyThread=0(137–141), `#endif` (142). ng 루프(143–147)에서 `chunk_size=(NtileX(ng)*NtileE(ng)+numthreads-1)/numthreads` (144), `first_tile(ng)=MyThread*chunk_size` (145), `last_tile (ng)=first_tile(ng)+chunk_size-1` (146). `IF (Master) THEN` (154)이면 프로세스 안내 출력(155–157). ng·THREAD_RANGE 루프에서 wclock_on(ng,iTLM,0,...) 호출(159–165). 병렬 영역에서 ROMS_allocate_arrays(allocate_vars)·ROMS_initialize_arrays 호출(169–172), `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (173). first 분기 종료·빈 줄(175–176). |
| 177–218 | 시작 시 51행 ROMS_initialize 안. `#if defined MCT_LIB && (defined ATM_COUPLING \|\| defined WAV_COUPLING)` (177). ng 루프(183–190)의 `# ifdef ATM_COUPLING` (184)에서 initialize_ocn2atm_coupling(ng,MyRank) 호출(185), `# endif` (186). `# ifdef WAV_COUPLING` (187)에서 initialize_ocn2wav_coupling(ng,MyRank) 호출(188), `# endif` (189), 외부 `#endif` (191). `#ifdef FORWARD_FLUXES` (198)는 비선형 모델(nonlinear model) 표면 플럭스(surface flux)를 BLK 구조로 연결한다는 주석(200–210)을 감싼다. edit_multifile('QCK2BLK') 호출(212), `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (213), ng 루프에서 LreadBLK=.TRUE.·LreadFRC=.FALSE.(214–217), `#endif` (218). |
| 219–245 | 시작 시 51행 ROMS_initialize 안. Lstiffness를 거짓으로 설정(222). ng 루프에서 LreadFWD를 참으로 설정하고 병렬 tl_initial(ng) 호출(223–227), `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (228). 실행 횟수 Nrun=1(233). ng 루프에서 LdefTLM·LwrtTLM을 참, LcycleTLM을 거짓으로 설정(237–241). RETURN·ROMS_initialize 종료·주석(243–245). |
| 246–291 | 시작 시 1행 roms_kernel_mod 모듈 안. ROMS_run(RunInterval) 시작(246), RunInterval은 초 단위 입력 실수(dp)(250–257), ng·MyFile 선언(261–264). ng 루프의 `IF (Master) THEN` (271)에서 시작·종료 시간 단계(time step) 출력(272–274). 병렬 영역의 `#ifdef SOLVE3D` (277)는 tl_main3d(RunInterval) 호출(278), `#else` (279)는 tl_main2d(RunInterval) 호출(280), `#endif` (281). `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (284). 출력 FORMAT·RETURN·루틴 종료·주석(286–291). |
| 292–332 | 시작 시 1행 roms_kernel_mod 모듈 안. ROMS_finalize 시작(292), Fcount·ng·thread·MyFile 선언과 재시작 파일(restart file) 저장 주석(294–312). `IF (exit_flag.eq.1) THEN` (313)의 ng 루프 안 `IF (LwrtRST(ng)) THEN` (315), `IF (Master) WRITE (stdout,10)` (316)로 안내 출력(317–318). `IF (LcycleRST(ng).and.(RST(ng)%Nrec(Fcount).ge.2)) THEN` (319)이면 Rindex=2·LcycleRST=.FALSE.(320–322). blowup에 exit_flag를 복사하고 exit_flag=NoError(323–324). `#ifdef DISTRIBUTE` (325)는 wrt_rst(ng,MyRank) 호출(326), `#else` (327)는 wrt_rst(ng,-1) 호출(328), `#endif` (329). 조건·루프 종료(330–332). |
| 333–370 | 시작 시 292행 ROMS_finalize 안. 종료·시간 계측·메모리·파일 닫기 주석(333–340). `IF (Master) THEN` (341)이면 경과 시간 안내를 출력(342–344). ng·THREAD_RANGE 병렬 루프에서 wclock_off(ng,iTLM,0,...) 호출(346–352). 병렬 memory 호출(356–358), ng 루프에서 close_inp(ng,iTLM) 호출(362–364), close_out 호출(365). RETURN·ROMS_finalize 종료·빈 줄·모듈 종료(367–370). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 302·319: Fcount는 지역 정수로 선언된다. 이 루틴에는 Fcount 값 대입이 없으며 RST(ng)%Nrec(Fcount) 인덱스에 사용한다.
- 319–328: 재시작 순환 조건에서 Rindex를 2로 고정한다. wrt_rst 호출 전에 exit_flag를 NoError로 바꾼다.
