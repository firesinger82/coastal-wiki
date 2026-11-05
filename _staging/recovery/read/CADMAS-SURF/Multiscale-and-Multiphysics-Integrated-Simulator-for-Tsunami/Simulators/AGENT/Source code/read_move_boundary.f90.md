---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/AGENT/Source code/read_move_boundary.f90
lines: 54
sha256: 07f7a98894ec9dbeba55408c6f3d3d1e137b5e463a04256ce074f58281b93143
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# read_move_boundary.f90 — 판독 구간 기록

구간은 1행부터 54행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | 진입 가능 여부 입력 데이터 읽기 주석(3). `implicit none`(7)과 인수·지역 변수를 선언하고 move_boundary.inp를 연다. 원문: `subroutine read_move_boundary(ierr)` (1); `!----------------------------------------` (2); `! 進入可否を指定する入力データ読み込み` (3); `!----------------------------------------` (4); `  use m_potential,only: ipmax,jpmax,move_boundary` (5); `!` (6); `  implicit none` (7); `!` (8); `![arguments]` (9); `  integer,intent(out):: ierr` (10); `!` (11); `![local variables]` (12); `  character(32):: rout='read_move_boundary'` (13); `  character(256):: line` (14); `  integer:: i,j` (15); `!` (16); `  ierr=0` (17); `!` (18); `!` (19); `  open(20,file='move_boundary.inp',status='old',form='formatted',err=99)` (20); `!` (21); `!` (22) |
| 23–54 | 시작 시 1행 루틴 안. 상하 방향 진입 가능 여부 주석(23). 첫 줄 첫 글자가 #이 아니면 -30과 errmsg를 보고한다. j=jpmax..1 역순으로 move_boundary를 읽고 read 실패는 -40을 보고한 뒤 닫는다. open 실패는 -99를 보고한다. 마지막 빈 줄까지 포함한다. 원문: `!上下方向の進入可否` (23); `!` (24); `  read(20,'(a256)') line` (25); `  if( line(1:1)/='#' )then` (26); `     ierr=-30` (27); `     call errmsg(rout,ierr)` (28); `     write(*,*) 'read error : move_boundary.inp'` (29); `  endif` (30); `!` (31); `  do j=jpmax,1,-1` (32); `     read(20,*,err=40) (move_boundary(i,j),i=1,ipmax)` (33); `  enddo` (34); `  goto 41` (35); `40 continue` (36); `     ierr=-40` (37); `     call errmsg(rout,ierr)` (38); `     write(*,*) 'read error : move_boundary.inp'` (39); `41 continue` (40); `!!` (41); `!` (42); `  close(20)` (43); `!` (44); `!` (45); `  return` (46); `!` (47); `99 continue` (48); `  ierr=-99` (49); `  call errmsg(rout,ierr)` (50); `  write(*,*) 'cannot open move_boundary.inp'` (51); `  return` (52); `end subroutine read_move_boundary` (53) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 26–33: 헤더 첫 글자가 #이 아니어도 오류 출력 뒤 격자 읽기로 계속 진행한다.
