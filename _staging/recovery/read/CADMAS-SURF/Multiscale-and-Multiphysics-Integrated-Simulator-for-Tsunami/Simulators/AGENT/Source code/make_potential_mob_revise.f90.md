---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/AGENT/Source code/make_potential_mob_revise.f90
lines: 50
sha256: 20720185d2a29f6660b0808815f9119a36e4574f6d196e75d0ac3859118a62d0
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# make_potential_mob_revise.f90 — 판독 구간 기록

구간은 1행부터 50행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | 에이전트 자신을 포함하지 않는 군중 포텐셜 계산 주석(3). `implicit none`(8), 인수·변수를 선언한다. 16행 rout 선언은 주석 처리되었다. 셀 단위 반경과 제곱 반경을 구한다. 원문: `subroutine make_potential_mob_revise(n,ierr)` (1); `!----------------------------------------` (2); `! エージェント自身を含まない群衆ポテンシャルを計算` (3); `!----------------------------------------` (4); `  use m_potential,only: ipmax,jpmax,dxy &` (5); `                     & ,r_mob,pot_mob,pot_mob_revise` (6); `  use m_agent,only: i_agent,j_agent` (7); `  implicit none` (8); `!` (9); `![arguments]` (10); `  integer,intent(out):: ierr` (11); `!` (12); `![local variables]` (13); `  integer:: n,i,j,is,js,ie,je,ir2,irmob,irmob2` (14); `  real(8):: rmobdxy,rr` (15); `!  character(32):: rout='make_potential_mob_revise'` (16); `!` (17); `  ierr=0` (18); `!` (19); `  rmobdxy=r_mob/dxy` (20); `  irmob =int(rmobdxy)` (21); `  irmob2=int(rmobdxy**2)` (22); `!` (23); `!` (24) |
| 25–50 | 시작 시 1행 루틴 안. 제n 에이전트의 군중 포텐셜 상당분을 빼서 보정 포텐셜로 만든다는 주석(25). 전체 장을 복사한 뒤 에이전트 주변 범위를 제한한다. `if(ir2<=irmob2)then` 안에서 `if(ir2==0)then`이면 `rr=dxy`를 설정한다(38–40). 그 외에는 `rr=sqrt(dble(ir2))*dxy`를 계산한다(41–43). `pot_mob_revise(i,j)=pot_mob(i,j)+1.0d0/rr`로 보정 배열을 갱신한다(44). 원문: `!第nエージェントによる群衆ポテンシャル相当分をpot_mobから差し引いてpot_mob_reviseとする` (25); `  pot_mob_revise(:,:)=pot_mob(:,:)` (26); `  is=i_agent(n)-irmob` (27); `    if(is<1) is=1` (28); `  ie=i_agent(n)+irmob` (29); `    if(ie>ipmax) ie=ipmax` (30); `  js=j_agent(n)-irmob` (31); `    if(js<1) js=1` (32); `  je=j_agent(n)+irmob` (33); `    if(je>jpmax) je=jpmax` (34); `  do j=js,je` (35); `  do i=is,ie` (36); `    ir2=(i_agent(n)-i)**2+(j_agent(n)-j)**2` (37); `    if(ir2<=irmob2)then` (38); `      if(ir2==0)then` (39); `        rr=dxy` (40); `      else` (41); `        rr=sqrt(dble(ir2))*dxy` (42); `      endif` (43); `      pot_mob_revise(i,j)=pot_mob(i,j)+1.0d0/rr` (44); `    endif` (45); `  enddo` (46); `  enddo` (47); `!` (48); `  return` (49); `end subroutine make_potential_mob_revise` (50) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
