---
file: models/ROMS/raw/source_code/roms/Master/mct_driver.h
lines: 187
sha256: d99af32742780d0577725be6d079ce2bf0fc646fe65d26231ed9bb92e996b2e4
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# mct_driver.h — 판독 구간 기록

구간은 1행부터 187행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–26 | 주 프로그램 `mct_driver` 시작(1), 저작권·MIT/X 라이선스·MCT 결합 목적 주석(2–14). WRF_COUPLING과 SWAN_COUPLING의 각 전처리 조건은 모델 설명·주소 주석(16–18·21–23)을 감싼다. 끝 구분 주석(25–26). 원문 조건·대입식·반복·전처리: `#ifdef WRF_COUPLING` (15); `#endif` (19); `#ifdef SWAN_COUPLING` (20); `#endif` (24). |
| 27–62 | 시작 시 1행 주 프로그램 안. 매개변수·병렬·결합·입출력·스칼라 모듈(27–31)과 MCTWorld_clean(33)을 가져온다. WRF 조건은 finalize_ocn2atm_coupling(36), SWAN 또는 REFDIF 조건은 finalize_ocn2wav_coupling(39), PIO_LIB와 DISTRIBUTE 조건은 finalize_pio(45)를 가져온다. ROMS_initialize·ROMS_run·ROMS_finalize는 공통(41–43)이다. first는 save 논리 변수(52), 색·통신자·오류·키·노드 수와 ng·provided·required는 정수(54–55), CouplingTime은 단정밀도(single precision) real(r4)(57)로 선언한다. MPI 초기화 절 머리 주석(59–62)이 뒤따른다. 원문 조건·대입식·반복·전처리: `#ifdef WRF_COUPLING` (35); `#endif` (37); `#if defined SWAN_COUPLING \|\| defined REFDIF_COUPLING` (38); `#endif` (40); `#if defined PIO_LIB && defined DISTRIBUTE` (44); `#endif` (46). |
| 63–99 | 시작 시 1행 주 프로그램 안. MULTI_THREAD 분기는 MPI_THREAD_MULTIPLE을 요구하며 mpi_init_thread(67)를 호출한다. 그 밖의 분기는 mpi_init(73)을 호출한다. 각 MyError 비영 조건은 로그와 exit_flag=6을 설정(68–77)한다. mpi_comm_size·mpi_comm_rank(83–84)를 호출하고 임시 해양 통신자(communicator)를 MPI_COMM_WORLD로 설정(90)한다. read_CouplePar(iNLM)(94)와 allocate_coupler(Nnodes)(98)를 호출한다. 원문 조건·대입식·반복·전처리: `#ifdef MULTI_THREAD` (65); `required=MPI_THREAD_MULTIPLE` (66); `IF (MyError.ne.0) THEN` (68); `exit_flag=6` (70); `#else` (72); `IF (MyError.ne.0) THEN` (74); `exit_flag=6` (76); `#endif` (78); `OCN_COMM_WORLD=MPI_COMM_WORLD` (90). |
| 100–126 | 시작 시 1행 주 프로그램 안. MyKey=0(103)을 설정한다. 해양·대기·파랑의 프로세스 순위(rank)가 pets의 처음 값과 Nthreads 위치의 마지막 값 사이인 조건(104–105·109–110·115–116)에 각각 OCNid·ATMid·WAVid를 MyColor에 대입(106·111·117)한다. 대기와 파랑 조건은 각각 ATM_COUPLING·WAV_COUPLING으로 감싼다. mpi_comm_split(MPI_COMM_WORLD, MyColor, MyKey, MyCOMM, MyError)(120–121)을 호출한다. 모델 실행 절 주석(123–126)이 뒤따른다. 원문 조건·대입식·반복·전처리: `MyKey=0` (103); `IF ((pets(Iocean)%val(1).le.MyRank).and.                          &` (104); `&    (MyRank.le.pets(Iocean)%val(Nthreads(Iocean)))) THEN` (105); `MyColor=OCNid` (106); `#ifdef ATM_COUPLING` (108); `IF ((pets(Iatmos)%val(1).le.MyRank).and.                          &` (109); `&    (MyRank.le.pets(Iatmos)%val(Nthreads(Iatmos)))) THEN` (110); `MyColor=ATMid` (111); `#endif` (113); `#ifdef WAV_COUPLING` (114); `IF ((pets(Iwaves)%val(1).le.MyRank).and.                          &` (115); `&    (MyRank.le.pets(Iwaves)%val(Nthreads(Iwaves)))) THEN` (116); `MyColor=WAVid` (117); `#endif` (119). |
| 127–152 | 시작 시 1행 주 프로그램 안. SWAN 분기에서 MyColor=WAVid이면 CouplingTime을 TimeInterval(Iocean,Iwaves)의 REAL 값으로 만들고 SWAN_INITIALIZE(MyCOMM, INPname(Iwaves))·SWAN_RUN(CouplingTime)·SWAN_FINALIZE(130–132)를 호출한다. 배타적인 REFDIF 전처리 분기는 같은 색·시간 변환을 쓰며 refdif_initialize·refdif_run·refdif_finalize(137–139)를 호출한다. 독립적인 WRF 전처리 분기에서 MyColor=ATMid이면 대기 결합 간격을 REAL로 변환하고 module_wrf_top_wrf_init·module_wrf_top_wrf_run·module_wrf_top_wrf_finalize(148–150)를 호출한다. 145–147행의 이름에 `_mp_`가 들어간 호출은 주석 처리되어 있다. 원문 조건·대입식·반복·전처리: `#if defined SWAN_COUPLING` (127); `IF (MyColor.eq.WAVid) THEN` (128); `CouplingTime=REAL(TimeInterval(Iocean,Iwaves))` (129); `#elif defined REFDIF_COUPLING` (134); `IF (MyColor.eq.WAVid) THEN` (135); `CouplingTime=REAL(TimeInterval(Iocean,Iwaves))` (136); `#endif` (141); `#ifdef WRF_COUPLING` (142); `IF (MyColor.eq.ATMid) THEN` (143); `CouplingTime=REAL(TimeInterval(Iocean,Iatmos))` (144); `#endif` (152). |
| 153–175 | 시작 시 1행 주 프로그램 안. 해양 색 조건(153)에서 first=.TRUE.를 설정(154)한다. 첫 exit_flag=NoError 조건은 ROMS_initialize(first, mpiCOMM=MyCOMM)(156)를 호출한 뒤 run_time=0에서 모든 격자의 dt*ntimes 최댓값을 계산(157–160)한다. 두 번째 같은 오류 조건은 ROMS_run(run_time)(163)을 호출한다. ROMS_finalize(165)는 이 두 오류 조건 밖의 해양 색 조건 안에 있다. 이어 PIO·파랑·대기 전처리 조건에 따라 finalize_pio(167), finalize_ocn2wav_coupling(170), finalize_ocn2atm_coupling(173)을 호출한다. 원문 조건·대입식·반복·전처리: `IF (MyColor.eq.OCNid) THEN` (153); `first=.TRUE.` (154); `IF (exit_flag.eq.NoError) THEN` (155); `run_time=0.0_r8` (157); `DO ng=1,Ngrids` (158); `run_time=MAX(run_time, dt(ng)*ntimes(ng))` (159); `IF (exit_flag.eq.NoError) THEN` (162); `#if defined PIO_LIB && defined DISTRIBUTE` (166); `#endif` (168); `#if defined SWAN_COUPLING \|\| defined REFDIF_COUPLING` (169); `#endif` (171); `#ifdef WRF_COUPLING` (172); `#endif` (174). |
| 176–187 | 시작 시 1행 주 프로그램 안이며 해양 색 조건 밖. 종료 주석(176–180) 뒤 mpi_barrier(MPI_COMM_WORLD, MyError)(181), MCTWorld_clean()(182), mpi_finalize(MyError)(183)를 순서대로 호출한다. STOP(185), 빈 줄과 프로그램 종료(184·186–187). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 65–78: MULTI_THREAD 분기는 provided를 mpi_init_thread에서 받는다. 이후 이 파일에는 provided와 required를 비교하는 문장이 없다.
- 68–78·83–98: MPI 초기화 오류 분기는 exit_flag=6을 설정한다. 해당 분기 뒤 통신자 크기·순위 조회와 결합 매개변수 판독 호출은 계속 배치되어 있다.
- 54·103–121: MyColor는 지역 선언에서 초기화하지 않는다. MyColor 대입은 세 순위 범위 조건 안에 있다. mpi_comm_split 앞에 범위에 속하지 않는 순위의 별도 대입 분기는 없다.
- 104–118: 세 순위 범위 검사는 독립적인 IF 문이다. 이 블록에는 범위 중첩을 검사하는 조건이 없다.
- 57·129·136·144: CouplingTime은 real(r4)로 선언한다. 각 결합 간격에는 종류 인수 없는 REAL 변환을 적용한다.
- 155–165: ROMS_initialize 호출 뒤의 run_time 계산은 최초 오류 조건 안에 있다. ROMS_run에는 별도의 오류 조건이 있다. ROMS_finalize는 그 두 오류 조건 밖에 있다.
