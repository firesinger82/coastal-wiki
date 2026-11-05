---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/AGENT/Source code/main.f90
lines: 74
sha256: 24e40e0901f5cff7dad717a047f5a1582df602a164348a558c3c358e4b271873
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# main.f90 — 판독 구간 기록

구간은 1행부터 74행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | 메인 루틴 주석(3). `implicit none`(7), 루틴명과 ierr를 선언한다. 버전 시작 문구 출력, cpu_time 및 init_mpmd를 호출한다(13–17). 15–16행 시간 출력 코드는 주석 처리되었다. 장치 90의 로그 출력 시작이라는 주석(21)과 open_file(0,ierr), 음수 오류 정지가 이어진다. 원문: `program main` (1); `!----------------------------------------` (2); `!メインルーチン` (3); `!----------------------------------------` (4); `  use mod_comm,only: init_mpmd` (5); `  use m_timectl,only: time_begin_s,time_end_s` (6); `  implicit none` (7); `!` (8); `![local variables]` (9); `  character(32):: rout='main'` (10); `  integer:: ierr` (11); `!` (12); `  write(*,*)"agent_ver3.5 start"` (13); `  call cpu_time(time_begin_s)` (14); `  !open(unit=99,file='cpu_time.txt')` (15); `  !write(99,*)'time_begin_s= ',time_begin_s` (16); `  call init_mpmd` (17); `!` (18); `  ierr=0` (19); `!` (20); `  call open_file(0,ierr)                  ! LOG出力(装置番号：90)開始` (21); `   if(ierr<0) call errstop(rout,ierr)` (22); `!` (23); `!` (24) |
| 25–55 | 시작 시 1행 프로그램 안. 입력 데이터 읽기 주석(26). 계산 조건 read_condition(31), 에이전트 데이터 read_agent(36), 사용할 포텐셜 배열 메모리 할당 allocate_potential(41), 포텐셜 입력 read_potential(46), 초기 설정·지형을 읽는 read_cadmas(0,ierr)(51)를 차례로 호출한다. 각 음수 ierr에 errstop을 호출한다. 표준출력 디버그 문장은 주석 처리되었다. 원문: `!----------------------------------------` (25); `! 入力データの読込み` (26); `!----------------------------------------` (27); `!` (28); `  write(100,'(a)')"debug: call read_condition"` (29); `  !write(*,*)"debug: call read_condition"` (30); `  call read_condition(ierr)               ! 計算条件の読み込み` (31); `   if(ierr<0) call errstop(rout,ierr)` (32); `!` (33); `   write(100,'(a)')"debug: call read_agent"` (34); `   !write(*,*)"debug: call read_agent"` (35); `   call read_agent(ierr)                   ! エージェントデータの読み込み` (36); `    if(ierr<0) call errstop(rout,ierr)` (37); `!` (38); `  write(100,'(a)')"debug: call allocate_potential"` (39); `  !write(*,*)"debug: call allocate_potential"` (40); `  call allocate_potential(ierr)           ! 使用するポテンシャル関連配列へのメモリ割り当て` (41); `   if(ierr<0) call errstop(rout,ierr)` (42); `!` (43); `  write(100,'(a)')"debug: call read_potential"` (44); `  !write(*,*)"debug: call read_potential"` (45); `  call read_potential(ierr)               ! ポテンシャル関連入力データの読み込み` (46); `   if(ierr<0) call errstop(rout,ierr)` (47); `!` (48); `  write(100,'(a)')"debug: call read_cadmas"` (49); `  !write(*,*)"debug: call read_cadmas"` (50); `  call read_cadmas(0,ierr)                ! CADMAS-SURF出力データの読み込み(初期設定＆地形読み込み)` (51); `   if(ierr<0) call errstop(rout,ierr)` (52); `   write(*,*)"finish reading input data"` (54); `!` (55) |
| 56–74 | 시작 시 1행 프로그램 안. 시간 적분 계산 주석(57). solver와 오류 정지, mpi_finalize(ierr)를 호출한다(61–64). 장치 90 로그 출력 종료라는 주석(66)과 open_file(1,ierr)를 포함한다. CPU 시간 계측 종료 주석과 cpu_time·write·close(69–71)는 주석 처리되었다. 종료 문구를 출력한다. 원문: `!----------------------------------------` (56); `! 時間積分計算` (57); `!----------------------------------------` (58); `  !write(100,'(a)')"debug: call solver"` (59); `  !write(*,*)"debug: call solver"` (60); `  call solver(ierr)` (61); `  if(ierr<0) call errstop(rout,ierr)` (62); `!` (63); `  call mpi_finalize(ierr)` (64); `!` (65); `  call open_file(1,ierr)                  ! LOG出力(装置番号：90)終了` (66); `   if(ierr<0) call errstop(rout,ierr)` (67); `!` (68); `   !call cpu_time(time_end_s)              !CPU時間計測終了` (69); `   !write(99,*)'time_end_s= ',time_end_s` (70); `   !close(99)` (71); `!` (72); `   write(*,*)"agent_ver3.5 end"` (73); `end program main` (74) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 64–67: mpi_finalize 호출 뒤 open_file을 호출하고 그 결과가 음수이면 errstop을 호출하는 순서다.
- 21·66: 로그 관련 주석의 장치 번호는 90이며 같은 루틴의 디버그 write 대상은 100이다.
