---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/AGENT/Source code/read_signpost.f90
lines: 58
sha256: b762d2e3b5f63d73cbb3d4251dc65e40ffc67ac6b02f284b43df6890c66f87aa
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# read_signpost.f90 — 판독 구간 기록

구간은 1행부터 58행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–25 | 이정표 데이터 읽기 주석(3). 모듈·`implicit none`(8), 인수·지역 변수와 pi를 선언한다. 입력 각도는 라디안이 아니라 도라는 주석(17). signpost.inp를 연다. 원문: `subroutine read_signpost(ierr)` (1); `!----------------------------------------` (2); `! 道標データの読み込み` (3); `!----------------------------------------` (4); `  use m_potential,only: n_signpost,i_signpost,j_signpost  &` (5); `                     & ,r_signpost,theta_signpost` (6); `!` (7); `  implicit none` (8); `!` (9); `![arguments]` (10); `  integer,intent(out):: ierr` (11); `!` (12); `![local variables]` (13); `  character(32):: rout='read_signpost'` (14); `  character(256):: line` (15); `  integer:: n,nn` (16); `  real(8):: theta_signpost_deg    !入力ファイル読み込み時は、RadianではなくDegreeで` (17); `  real(8),parameter:: pi=3.141592653589793d0` (18); `!` (19); `  ierr=0` (20); `!` (21); `!` (22); `  open(21,file='signpost.inp',status='old',form='formatted',err=99)` (23); `!` (24); `!` (25) |
| 26–58 | 시작 시 1행 루틴 안. EOF까지 첫 글자 # 행을 제외하고 nn·위치·반경·각도를 읽는다. 각도를 도에서 라디안으로 변환한다(33). EOF 뒤 n>n_signpost는 경고 10, read 실패는 -30, open 실패는 -99로 보고한다. 파일 닫기와 반환을 포함한다. 원문: `  n=0` (26); `  do` (27); `     read(21,'(a256)',end=10) line` (28); `     if( line(1:1)=='#' ) cycle` (29); `     n=n+1` (30); `     read(line,*,err=30) nn,i_signpost(n),j_signpost(n) &` (31); `                      & ,r_signpost(n),theta_signpost_deg` (32); `     theta_signpost(n)=theta_signpost_deg*pi/180d0    ! Degree => Radian` (33); `  enddo` (34); `10 continue` (35); `  if(n>n_signpost)then` (36); `     ierr=10` (37); `     call errmsg(rout,ierr)` (38); `     write(*,*) 'n > n_signpost : signpost.inp'` (39); `  endif` (40); `  goto 31` (41); `30 continue` (42); `     ierr=-30` (43); `     call errmsg(rout,ierr)` (44); `     write(*,*) 'read error : signpost.inp'` (45); `31 continue` (46); `!` (47); `!` (48); `  close(21)` (49); `!` (50); `  return` (51); `!` (52); `99 continue` (53); `  ierr=-99` (54); `  call errmsg(rout,ierr)` (55); `  write(*,*) 'cannot open signpost.inp'` (56); `  return` (57); `end subroutine read_signpost` (58) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 30–36: 배열에 저장한 뒤 EOF에서 n>n_signpost를 검사한다. 입력 중 상한 검사는 이 루프에 없다.
- 36–40: 입력 개수 초과만 검사하며 n<n_signpost 조건은 없다.
