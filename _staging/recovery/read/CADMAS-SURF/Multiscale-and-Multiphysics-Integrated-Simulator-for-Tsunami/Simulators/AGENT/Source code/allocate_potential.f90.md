---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/AGENT/Source code/allocate_potential.f90
lines: 69
sha256: 0820d0a133079290113777236668fca405f04b4503deb50194f784d5fda0b30a
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# allocate_potential.f90 — 판독 구간 기록

구간은 1행부터 69행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | 사용할 포텐셜(potential) 배열에 메모리를 할당한다는 주석(3). 관련 모듈, 인수 및 `implicit none`(14)을 선언한다. 원문: `subroutine allocate_potential(ierr)` (1); `!----------------------------------------` (2); `! 使用するポテンシャル配列へのメモリ割り当て` (3); `!----------------------------------------` (4); `  use m_potential,only: n_signpost,n_shelter,n_mob &` (5); `                     & ,allocate_move_boundary &` (6); `                     & ,allocate_signpost &` (7); `                     & ,allocate_pot_shelter &` (8); `                     & ,allocate_pot_mob &` (9); `                     & ,allocate_m_pot_shelter &` (10); `                     & ,allocate_n_potential` (11); `  use m_agent,only: n_agent` (12); `  use m_flag,only: flag_danger,flag_prob` (13); `  implicit none` (14); `!` (15); `![arguments]` (16); `  integer,intent(out):: ierr` (17); `!` (18); `![local variables]` (19); `  character(32):: rout='allocate_potential'` (20); `!` (21); `  ierr=0` (22); `!` (23); `!` (24) |
| 25–49 | 시작 시 1행 루틴 안. 진입 가능 여부 배열(25)은 항상 할당한다. 이정표(signpost) 관련 배열(30)은 n_signpost>0, 피난 경로 포텐셜 배열(37)은 n_shelter>0, 군중 포텐셜 배열(44)은 n_mob==1에서 할당한다. 각 호출의 음수 오류는 errstop으로 전달한다. 원문: `!進入可否を指定する配列` (25); `  write(100,'(a)') "debug: call allocate_move_boundary"` (26); `  call allocate_move_boundary(ierr)` (27); `   if(ierr<0) call errstop(rout,ierr)` (28); `!` (29); `!道標関連配列` (30); `  write(100,'(a)')"debug: call allocate_signpost"` (31); `  if(n_signpost>0)then` (32); `     call allocate_signpost(ierr)` (33); `      if(ierr<0) call errstop(rout,ierr)` (34); `  endif` (35); `!` (36); `!避難経路ポテンシャル配列` (37); `  write(100,'(a)')"debug: call allocate_pot_shelter"` (38); `  if(n_shelter>0)then` (39); `     call allocate_pot_shelter(ierr)` (40); `      if(ierr<0) call errstop(rout,ierr)` (41); `  endif` (42); `!` (43); `!群衆ポテンシャル配列` (44); `  write(100,'(a)')"debug: call allocate_pot_mod"` (45); `  if(n_mob==1)then` (46); `     call allocate_pot_mob(ierr)` (47); `      if(ierr<0) call errstop(rout,ierr)` (48); `  endif` (49) |
| 50–69 | 시작 시 1행 루틴 안. 위험 회피 포텐셜 배열이라는 주석(51) 아래 52–56행은 주석 처리된 출력·조건·할당·오류 정지 코드다. n_potential과 m_pot_shelter는 각각 n_agent·n_shelter를 인수로 무조건 할당하며 음수 오류를 검사한다(58–66). 원문: `!` (50); `!危険回避ポテンシャル配列` (51); `!  write(100,'(a)')"debug: call allocate_pot_shelter"` (52); `!  if(flag_danger==1)then` (53); `!     call allocate_pot_danger(ierr)` (54); `!      if(ierr<0) call errstop(rout,ierr)` (55); `!  endif` (56); `!` (57); `!n_potential` (58); `  write(100,'(a)')"debug: call allocate_n_potential"` (59); `  call allocate_n_potential(n_agent,ierr)` (60); `   if(ierr<0) call errstop(rout,ierr)` (61); `!` (62); `!m_pot_shelter` (63); `  write(100,'(a)')"debug: call allocate_m_pot_shelter"` (64); `  call allocate_m_pot_shelter(n_shelter,ierr)` (65); `   if(ierr<0) call errstop(rout,ierr)` (66); `  return` (68); `end subroutine allocate_potential` (69) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 13·51–56: flag_danger·flag_prob를 가져오지만 위험 회피 할당 분기는 주석 처리되어 있고 실행문에서 이 두 플래그를 참조하지 않는다.
