---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/AGENT/Source code/make_potential_mob.f90
lines: 62
sha256: 61aa20f60060c82fc7737763e65e5387731b5c4d1e157bb7a548ca450d1ef68b
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# make_potential_mob.f90 — 판독 구간 기록

구간은 1행부터 62행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | 군중 포텐셜 설정 주석(3). `implicit none`(8), 인수와 작업 변수를 선언한다. 16행 rout 선언은 주석 처리되었다. 반경을 dxy로 나누고 정수 반경 및 제곱 반경을 구한다(20–22). 원문: `subroutine make_potential_mob(ierr)` (1); `!----------------------------------------` (2); `! 群衆ポテンシャルの設定` (3); `!----------------------------------------` (4); `  use m_potential,only: ipmax,jpmax,dxy &` (5); `                     & ,r_mob,nsum_agent,pot_mob` (6); `  use m_agent,only: n_agent,i_agent,j_agent,agent_status` (7); `  implicit none` (8); `!` (9); `![arguments]` (10); `  integer,intent(out):: ierr` (11); `!` (12); `![local variables]` (13); `  integer:: n,i,j,ip,jp,is,js,ie,je,ir2,irmob,irmob2` (14); `  real(8):: rmobdxy,rr` (15); `!  character(32):: rout='make_potential_mob'` (16); `!` (17); `  ierr=0` (18); `!` (19); `  rmobdxy=r_mob/dxy` (20); `  irmob =int(rmobdxy)` (21); `  irmob2=int(rmobdxy**2)` (22); `!` (23); `!` (24) |
| 25–62 | 시작 시 1행 루틴 안. 각 셀의 생존 에이전트 수 계산 주석(25) 아래 상태가 3이 아닌 에이전트를 센다. 군중 포텐셜은 반경 안 0명이면 0, n명이면 거리에 따라 음의 인원수/거리 합이라는 주석(33). 각 격자 주변 범위를 영역 안으로 제한하고 원 안 셀을 누적한다. 같은 셀은 rr=dxy, 그 외는 격자 거리의 제곱근에 dxy를 곱한다. 원문: `!各セル内の生存エージェント数を計算` (25); `  nsum_agent(:,:)=0` (26); `  do n=1,n_agent` (27); `    if(agent_status(n)/=3) &` (28); `     & nsum_agent(i_agent(n),j_agent(n))=nsum_agent(i_agent(n),j_agent(n))+1` (29); `  enddo` (30); `!` (31); `!` (32); `!群衆ポテンシャルの計算(範囲r_mob内に0人ならpot_mob=0，n人なら距離rによりpot_mob=-(n1/r1+n2/r2+…))` (33); `  pot_mob(:,:)=0.0d0` (34); `  do jp=1,jpmax` (35); `  do ip=1,ipmax` (36); `    is=ip-irmob` (37); `      if(is<1) is=1` (38); `    ie=ip+irmob` (39); `      if(ie>ipmax) ie=ipmax` (40); `    js=jp-irmob` (41); `      if(js<1) js=1` (42); `    je=jp+irmob` (43); `      if(je>jpmax) je=jpmax` (44); `    do j=js,je` (45); `    do i=is,ie` (46); `      ir2=(ip-i)**2+(jp-j)**2` (47); `      if(ir2<=irmob2)then` (48); `        if(ir2==0)then` (49); `          rr=dxy` (50); `        else` (51); `          rr=sqrt(dble(ir2))*dxy` (52); `        endif` (53); `        pot_mob(ip,jp)=pot_mob(ip,jp)-dble(nsum_agent(i,j))/rr` (54); `      endif` (55); `    enddo` (56); `    enddo` (57); `  enddo` (58); `  enddo` (59); `!` (60); `  return` (61); `end subroutine make_potential_mob` (62) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 28–29: 인원수 집계 조건은 agent_status/=3이므로 상태 0도 이 조건을 통과한다.
- 20–22·50–54: dxy를 분모로 사용하며 이 파일에 dxy=0 검사는 없다.
