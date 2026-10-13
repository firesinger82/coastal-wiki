---
file: models/ROMS/raw/source_code/roms/ROMS/Drivers/rp_roms.h
lines: 371
sha256: a7a950ca2542b2c580f8870b28b44c575ee80ab0ef45527d1cddd9fa19e1e177
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# rp_roms.h — 판독 구간 기록

구간은 1행부터 371행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–21 | `roms_kernel_mod`를 연다(1). 저작권·MIT/X 라이선스 주석을 포함한다(3–8). 대표함수(representer) 접선형 모형(tangent linear model)의 초기화·시간 적분·종료를 ESMF 규약으로 제어하는 드라이버라는 설명이다(10–18). 세 진입점 ROMS_initialize·ROMS_run·ROMS_finalize와 구분 주석을 포함한다(16–21). |
| 22–50 | 1행 모듈 선언 안이다. 매개변수·병렬·배열·입출력·스칼라 모듈을 가져온다(22–27). `close_inp`, `close_out`, `inp_par`, 표준 출력 설정·오류 검사·`wrt_rst`를 가져온다(29–41). MCT_LIB에서 대기·파랑 결합 옵션에 따라 해양 결합 초기화 루틴을 가져온다(31–38). implicit none·세 공개 진입점·CONTAINS를 포함한다(43–49). 전처리 지시 원문: `#ifdef MCT_LIB` (31); `# ifdef ATM_COUPLING` (32); `# endif` (34); `# ifdef WAV_COUPLING` (35); `# endif` (37); `#endif` (38). |
| 51–95 | `ROMS_initialize(first,mpiCOMM)`를 연다(51). 상태와 내부·외부 매개변수 할당·초기화 목적을 설명한다(55–56). first는 입출력 논리 인수, mpiCOMM은 선택 입력이다(62–64). 선언 기본값은 `logical :: allocate_vars = .TRUE.` (68)이다. 조건부 MPI·OpenMP 및 격자·스레드 변수와 MyFile을 선언한다(70–79). DISTRIBUTE에서 mpiCOMM이 있으면 해당 통신자(communicator), 없으면 MPI_COMM_WORLD를 설정하고 `mpi_comm_rank`, `mpi_comm_size`를 호출한다(81–94). 전처리 지시 원문: `#ifdef DISTRIBUTE` (70); `#endif` (72); `#ifdef _OPENMP` (74); `#endif` (76); `#ifdef DISTRIBUTE` (81); `#endif` (94). 조건·분기 원문: `IF (PRESENT(mpiCOMM)) THEN` (87); `ELSE` (89). |
| 96–130 | 51행 `ROMS_initialize` 안이다. first 참 분기에서 first를 거짓으로 바꾸고 `initialize_parallel`을 호출한다(103–109). Set_StdOutUnit이 참이면 `stdout_unit(Master)`로 출력 단위를 설정하고 스위치를 끈다(119–122). `inp_par(iRPM)`으로 대표함수 모형의 입력을 처리하고 오류이면 반환한다(128–129). first 분기는 이어진다. 조건·분기 원문: `IF (first) THEN` (103); `IF (Set_StdOutUnit) THEN` (119); `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (129). |
| 131–176 | 51행 `ROMS_initialize`·103행 first 참 분기 안이다. OpenMP 병렬 구역(135–148)에서 _OPENMP는 my_threadnum(), DISTRIBUTE는 MyRank, 다른 구성은 0을 MyThread로 설정한다(136–142). 격자별 타일 분할식은 `chunk_size=(NtileX(ng)*NtileE(ng)+numthreads-1)/numthreads` (144), `first_tile(ng)=MyThread*chunk_size` (145), `last_tile (ng)=first_tile(ng)+chunk_size-1` (146)이다. Master가 프로세스 정보를 보고한다(154–157). 격자·THREAD_RANGE의 OpenMP 구역에서 `wclock_on(ng,iRPM,0,...)`을 호출한다(159–165). 별도 OpenMP 구역에서 `ROMS_allocate_arrays(allocate_vars)`, `ROMS_initialize_arrays`를 호출하고 구역 밖에서 오류를 검사한다(169–173). first 분기를 닫는다(175). 전처리 지시 원문: `#if defined _OPENMP` (136); `#elif defined DISTRIBUTE` (138); `#else` (140); `#endif` (142). 조건·분기 원문: `IF (Master) THEN` (154); `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (173). |
| 177–219 | 51행 `ROMS_initialize` 안이며 first 조건 밖이다. MCT_LIB와 대기 또는 파랑 결합 옵션에서 격자별 `initialize_ocn2atm_coupling`·`initialize_ocn2wav_coupling`을 MyRank로 호출한다(177–191). FORWARD_FLUXES는 비선형 모형(nonlinear model, NLM)의 QCK 표면 플럭스를 BLK 구조로 연결한다는 주석이다(198–210). `edit_multifile('QCK2BLK')`를 호출하고 오류를 검사한다(212–213). 격자별 LreadBLK를 참, LreadFRC를 거짓으로 설정한다(214–217). 전처리 지시 원문: `#if defined MCT_LIB && (defined ATM_COUPLING \|\| defined WAV_COUPLING)` (177); `# ifdef ATM_COUPLING` (184); `# endif` (186); `# ifdef WAV_COUPLING` (187); `# endif` (189); `#endif` (191); `#ifdef FORWARD_FLUXES` (198); `#endif` (218). 조건·분기 원문: `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (213). |
| 220–245 | 51행 `ROMS_initialize` 안이다. 유한 진폭(finite amplitude)의 대표함수 모형 초기화 주석과 Lstiffness=거짓 설정을 포함한다(220–222). 격자별 LreadFWD를 참으로 설정하고 OpenMP 구역에서 `rp_initial(ng)`을 호출한다(223–227). 구역 밖에서 오류를 검사한다(228). Nrun을 1로 설정한다(233). 격자별 TLM 정의·쓰기를 켜고 순환 기록(cycling output)을 끈다(237–241). 반환하고 초기화 루틴을 닫는다(243–244). 조건·분기 원문: `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (228). |
| 246–291 | `ROMS_run(RunInterval)`를 연다(246). 지정 시간 구간의 대표함수 모형 적분 목적과 RunInterval의 초 단위 입력을 선언한다(250–257). 격자 번호·파일 식별자를 선언한다(261–264). 격자별 Master가 RP 단계 범위를 보고한다(270–274). OpenMP 구역에서 SOLVE3D이면 `rp_main3d(RunInterval)`, 아니면 `rp_main2d(RunInterval)`을 호출한다(276–282). 구역 밖에서 오류를 검사한다(284). 단계 보고 형식을 선언하고 반환하며 실행 루틴을 닫는다(286–290). 전처리 지시 원문: `#ifdef SOLVE3D` (277); `#else` (279); `#endif` (281). 조건·분기 원문: `IF (Master) THEN` (271); `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (284). |
| 292–334 | `ROMS_finalize`를 연다(292). 종료 목적, 격자·스레드·파일 인덱스·파일 식별자를 선언한다(296–305). exit_flag=1이면 격자별 LwrtRST 참 조건에서 Master가 발산(blowing-up) 저장 메시지를 보고한다(313–318). 현재 RST 파일 인덱스를 Fcount에 복사한다(319). LcycleRST가 참이고 레코드 수가 2 이상이면 Rindex=2로 지정하고 순환 기록을 끈다(320–323). blowup에 오류를 보존하고 exit_flag를 NoError로 설정한다(324–325). DISTRIBUTE는 MyRank, 다른 구성은 -1을 인수로 `wrt_rst`를 호출한다(326–330). 출력 조건·격자 루프·발산 조건을 닫는다(331–333). 전처리 지시 원문: `#ifdef DISTRIBUTE` (326); `#else` (328); `#endif` (330). 조건·분기 원문: `IF (exit_flag.eq.1) THEN` (313); `IF (LwrtRST(ng)) THEN` (315); `IF (Master) WRITE (stdout,10)` (316); `IF (LcycleRST(ng).and.(RST(ng)%Nrec(Fcount).ge.2)) THEN` (320). |
| 335–371 | 292행 `ROMS_finalize` 안이다. Master가 경과시간 머리말을 쓴다(342–345). 격자별 OpenMP 구역의 THREAD_RANGE에서 `wclock_off(ng,iRPM,0,...)`을 호출한다(347–353). 별도 OpenMP 구역에서 `memory`를 호출한다(357–359). 격자별 `close_inp(ng,iRPM)`과 공통 `close_out`으로 파일을 닫는다(363–366). 반환·종료 루틴·모듈을 닫는다(368–371). 조건·분기 원문: `IF (Master) THEN` (342). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 92–93: MPI rank·size 조회는 같은 MyError 변수로 반환값을 받는다. 이 두 호출 뒤에는 MyError를 검사하는 실행문이 없다.
- 103–104·128–129·169–175: first를 거짓으로 바꾼 뒤 입력과 배열 초기화를 수행한다. 두 단계의 오류 반환 경로에는 first를 참으로 복원하는 대입이 없다.
- 143–147: chunk_size는 전체 타일 수를 numthreads로 나눈 올림 형태의 정수식이다. last_tile은 first_tile+chunk_size-1로 계산하며 이 블록에는 전체 타일 수로 제한하는 MIN 식이 없다.
