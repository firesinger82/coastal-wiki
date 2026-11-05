---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/AGENT/Source code/read_shelter.f90
lines: 56
sha256: a922999bd361ab74a702b57f6d902e74a9323f7804cd4c364ba50c5c7d05a5c4
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# read_shelter.f90 — 판독 구간 기록

구간은 1행부터 56행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | 피난소 데이터 읽기 주석(3). 모듈·`implicit none`(7)·인수·변수를 선언하고 shelter.inp를 연다. 원문: `subroutine read_shelter(ierr)` (1); `!----------------------------------------` (2); `! 避難所データの読み込み` (3); `!----------------------------------------` (4); `  use m_potential,only: n_shelter,i_shelter,j_shelter,shelter_height,move_boundary` (5); `!` (6); `  implicit none` (7); `!` (8); `![arguments]` (9); `  integer,intent(out):: ierr` (10); `!` (11); `![local variables]` (12); `  character(32):: rout='read_shelter'` (13); `  character(256):: line` (14); `  integer:: n,nn` (15); `!` (16); `  ierr=0` (17); `!` (18); `!` (19); `  open(22,file='shelter.inp',status='old',form='formatted',err=99)` (20); `!` (21); `!` (22) |
| 23–56 | 시작 시 1행 루틴 안. EOF까지 첫 글자 # 행을 제외하고 nn·위치·표고를 순차 읽는다. move_boundary가 0이 아니면 도로 밖이라는 로그를 쓴다. EOF 뒤 n>n_shelter는 양수 경고 10, read 실패는 -30, open 실패는 -99로 보고한다. 파일 닫기·반환을 포함한다. 원문: `  n=0` (23); `  do` (24); `     read(22,'(a256)',end=10) line` (25); `     if( line(1:1)=='#' ) cycle` (26); `     n=n+1` (27); `     read(line,*,err=30) nn,i_shelter(n),j_shelter(n),shelter_height(n)` (28); `     if(move_boundary(i_shelter(n),j_shelter(n)) /= 0)then` (29); `       write(100,*)"shelter",nn," is not on the road"` (30); `     endif` (31); `  enddo` (32); `10 continue` (33); `  if(n>n_shelter)then` (34); `     ierr=10` (35); `     call errmsg(rout,ierr)` (36); `     write(*,*) 'n > n_shelter : shelter.inp'` (37); `  endif` (38); `  goto 31` (39); `30 continue` (40); `     ierr=-30` (41); `     call errmsg(rout,ierr)` (42); `     write(*,*) 'read error : shelter.inp'` (43); `31 continue` (44); `!` (45); `!` (46); `  close(22)` (47); `!` (48); `  return` (49); `!` (50); `99 continue` (51); `  ierr=-99` (52); `  call errmsg(rout,ierr)` (53); `  write(*,*) 'cannot open shelter.inp'` (54); `  return` (55); `end subroutine read_shelter` (56) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 27–34: 배열에 먼저 저장하고 EOF 뒤 n>n_shelter를 검사한다. 입력 중 상한 검사는 이 루프에 없다.
- 28–29: 입력 피난소 인덱스로 move_boundary를 참조하기 전에 격자 범위를 검사하는 조건은 이 블록에 없다.
- 34–38: 입력 개수 초과만 검사하며 n<n_shelter 조건은 없다.
