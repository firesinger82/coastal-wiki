---
file: models/ROMS/raw/source_code/roms/Master/roms.h
lines: 149
sha256: 595f3a9079161976319eef2f2d372e85427734cce593f86028e0312751481400
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# roms.h — 판독 구간 기록

구간은 1행부터 149행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–48 | 주 프로그램(program) MyROMS 선언(1), 저작권·라이선스·빈 주석(2–8). 대기 모델과 결합하지 않는 해양 실행 드라이버라는 주석(10–14). 자유수면·정수압·원시 방정식과 지형 추종 좌표(terrain-following coordinates) 설명은 주석이다(16–19). 비선형·접선 선형(tangent linear)·수반(adjoint) 모델 개발자 목록과 구분 주석이 이어진다(20–48). |
| 49–70 | 시작 시 1행 MyROMS 안이며 열린 전처리 조건은 없다. mod_param·mod_parallel·mod_iounits·mod_scalars와 ROMS_deallocate_arrays를 가져온다(49–54). roms_kernel_mod에서 ROMS_initialize·ROMS_run·ROMS_finalize를 가져온다(56–58). `#if defined PIO_LIB && defined DISTRIBUTE` (59)이면 finalize_pio를 가져오며 `#endif` (61)로 닫는다. implicit none, 저장 논리 변수 first와 정수 ng/MyError/provided/required 선언 및 빈 줄·주석을 포함한다(62–70). |
| 71–102 | 시작 시 1행 MyROMS 안. `#ifdef DISTRIBUTE` (71), `# ifdef MPI` (72), `#  ifdef MULTI_THREAD` (78). 다중 스레드 분기는 required=MPI_THREAD_MULTIPLE 설정 후 `CALL mpi_init_thread (required, provided, MyError)` (80)이다. `IF (MyError.ne.0) THEN` (81)이면 로그와 exit_flag=6을 설정한다(82–84). `#  else` (85)는 `CALL mpi_init (MyError)` (86), `IF (MyError.ne.0) THEN` (87), 오류 로그·exit_flag=6(88–90)이다. `#  endif` (91) 뒤 `CALL mpi_comm_rank (MPI_COMM_WORLD, MyRank, MyError)` (96), `IF (MyError.ne.0) THEN` (97)이면 로그·exit_flag=6(98–100). `# endif` (101), `#endif` (102)로 MPI와 DISTRIBUTE를 닫는다. |
| 103–125 | 시작 시 1행 MyROMS 안이며 열린 전처리 조건은 없다. 초기화 설명 주석 뒤 `IF (exit_flag.eq.NoError) THEN` (109)이면 first를 참으로 설정하고 ROMS_initialize(first)를 호출한다(110–112). 시간 진행 설명 뒤 별도 `IF (exit_flag.eq.NoError) THEN` (119)이면 run_time을 0.0_r8로 초기화하고 `DO ng=1,Ngrids` (121)에서 `run_time=MAX(run_time, dt(ng)*ntimes(ng))` (122)를 계산한다. 루프 밖에서 ROMS_run(run_time)를 호출하고 조건을 닫는다(123–125). |
| 126–138 | 시작 시 1행 MyROMS 안이며 열린 전처리 조건은 없다. 종료 설명 주석과 ROMS_finalize 호출(126–131). `#if defined PIO_LIB && defined DISTRIBUTE` (132)이면 finalize_pio 호출(133), `#endif` (134). ROMS_deallocate_arrays 호출(135). `#if defined DISTRIBUTE && defined MPI` (136)이면 mpi_finalize(MyError) 호출(137), `#endif` (138). 이 종료 호출들은 109·119행 오류 검사 조건 밖이다. |
| 139–149 | 시작 시 1행 MyROMS 안이며 열린 전처리 조건은 없다. 오류 신호와 셸 오류 처리 설명 주석(139–145). `!!    IF ((exit_flag.ne.NoError).or.(blowup.ne.0)) STOP 911   ! F-2003` (146)은 주석이다. 실행 조건은 `IF ((exit_flag.ne.NoError).or.(blowup.ne.0)) ERROR STOP ! F-2008` (147)이다. 빈 주석과 주 프로그램 종료(148–149). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 109–125·131–138: 초기화와 실행은 exit_flag.eq.NoError 조건으로 감싼다. ROMS_finalize와 배열 해제는 해당 조건 밖에 있다.
- 69·137: mpi_finalize는 MyError를 받는다. 이 호출 뒤 MyError를 검사하는 실행문은 없으며 최종 ERROR STOP은 exit_flag와 blowup만 검사한다(147).
