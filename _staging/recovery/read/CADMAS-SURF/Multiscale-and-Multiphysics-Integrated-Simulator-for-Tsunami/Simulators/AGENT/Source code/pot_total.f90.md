---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/AGENT/Source code/pot_total.f90
lines: 35
sha256: 12d7336cb88a10ec0f73e2b82581f5f020c8c13fb9b7c00296fe1996b158c7b0
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# pot_total.f90 — 판독 구간 기록

구간은 1행부터 35행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–21 | 고려하는 포텐셜을 가중합한다는 주석(3). 모듈·`implicit none`(8)·인수·rout를 선언하고 ierr 및 함수값을 0으로 둔다. 원문: `real(8) function pot_total(n,i,j,ierr)` (1); `!----------------------------------------` (2); `! 考慮するポテンシャルを重みをつけて足し合わせる` (3); `!----------------------------------------` (4); `  use m_potential,only: n_shelter,n_potential &` (5); `                     & ,n_mob,pot_mob_revise` (6); `  use m_agent,only: weight_shelter,weight_mob,weight_danger` (7); `  implicit none` (8); `!` (9); `![arguments]` (10); `  integer,intent(in):: n,i,j` (11); `  integer,intent(out):: ierr` (12); `!` (13); `![local variables]` (14); `  character(32):: rout='pot_total'` (15); `!` (16); `  ierr=0` (17); `!` (18); `!` (19); `  pot_total=0.0d0` (20); `!` (21) |
| 22–35 | 시작 시 1행 함수 안. 피난 경로 포텐셜 주석(22)의 n_shelter>0이면 개인 경로 포텐셜과 weight_shelter를 곱해 더한다. 군중 포텐셜 주석(27)의 n_mob==1이면 make_potential_mob_revise를 호출하고 weight_mob를 곱해 더한다. 자기 영향 제거의 근거는 `make_potential_mob_revise.f90:3,25–44`의 주석과 보정식이다. 음수 ierr는 정지한다. 원문: `!避難経路ポテンシャル` (22); `  if(n_shelter>0)then` (23); `     pot_total=pot_total+n_potential(n,i,j)*weight_shelter(n)` (24); `  endif` (25); `!` (26); `!群衆ポテンシャル` (27); `  if(n_mob==1)then` (28); `     call make_potential_mob_revise(n,ierr)` (29); `      if(ierr<0) call errstop(rout,ierr)` (30); `     pot_total=pot_total+pot_mob_revise(i,j)*weight_mob(n)` (31); `  endif` (32); `  return` (34); `end function pot_total` (35) [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 7·23–31: weight_danger를 가져오지만 이 함수의 합산식에서 사용하지 않는다.
