---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/AGENT/Source code/underwater_function.f90
lines: 96
sha256: 73e9fc458784572496d8b33be16ff670632732c31d2dbb8b9c048804ebab6418
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# underwater_function.f90 — 판독 구간 기록

구간은 1행부터 96행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–39 | 머리말은 사면 경사에 따른 이동 속력 변화율 계산이라고 쓴다(3). 입력은 n,t(5–6), 출력은 무차원 속력 보정 계수 F(8–9)다. 모듈·`implicit none`(13)·인수·지역 변수를 선언한다. 에이전트 위치 수심과 두 성분 유속을 읽고 depth_limit=0.7·flow_limit=2.5로 무차원 등급을 계산한다. 두 유속이 모두 0이 아닐 때만 제곱합 제곱근을 쓰고 아니면 flow_now=0이다. 원문: `subroutine underwater_function(n,t,F)` (1); `!----------------------------------------` (2); `! 斜面勾配による移動速度の変化率を計算` (3); `!` (4); `! <入力>` (5); `! n,t` (6); `!` (7); `! <出力>` (8); `! F: 移動速度の補正係数[-]` (9); `!----------------------------------------` (10); `  use m_agent,only: i_agent,j_agent` (11); `  use m_cadmas,only: depth,uu,vv` (12); `  implicit none` (13); `!` (14); `![arguments]` (15); `  real(8),intent(in):: n,t` (16); `  real(8),intent(out):: F` (17); `!` (18); `![local variables]` (19); `  integer i_now,j_now` (20); `  real(8) depth_now,flow_now,depth_rank,flow_rank,depth_limit,flow_limit` (21); `!` (22); `  i_now = i_agent(n)` (24); `  j_now = j_agent(n)` (25); `!man` (26); `  depth_limit = 0.7` (27); `  flow_limit = 2.5` (28); `  depth_now = depth(i_now,j_now)` (30); `  if(uu(i_now,j_now)/=0 .and. vv(i_now,j_now)/=0)then` (31); `    flow_now = SQRT(uu(i_now,j_now)**2 + vv(i_now,j_now)**2)` (32); `  else` (33); `    flow_now = 0` (34); `  endif` (35); `  depth_rank = depth_now / depth_limit` (37); `  flow_rank = flow_now / flow_limit` (38) |
| 40–75 | 시작 시 1행 루틴 안. 시작 시 1행 underwater_function 루틴 안. 수심 등급 <0.2·<0.4·<0.6의 분기마다 유속 등급의 0.2 간격 조건으로 F를 계단식으로 둔다. 첫 수심 분기는 F=1.0·0.8·0.6·0.4·0.2·0.0, 둘째는 0.8·0.6·0.4·0.2·0.0, 셋째는 0.6·0.4·0.2·0.0이다. 조건과 대입 원문을 모두 보존한다. 원문: `  if(depth_rank <0.2)then` (40); `    if(flow_rank<0.2)then` (41); `      F=1.0` (42); `    elseif(flow_rank<0.4)then` (43); `      F=0.8` (44); `    elseif(flow_rank<0.6)then` (45); `      F=0.6` (46); `    elseif(flow_rank<0.8)then` (47); `      F=0.4` (48); `    elseif(flow_rank<1.0)then` (49); `      F=0.2` (50); `    else` (51); `      F=0.0` (52); `    endif` (53); `  elseif(depth_rank <0.4)then` (54); `    if(flow_rank<0.2)then` (55); `      F=0.8` (56); `    elseif(flow_rank<0.4)then` (57); `      F=0.6` (58); `    elseif(flow_rank<0.6)then` (59); `      F=0.4` (60); `    elseif(flow_rank<0.8)then` (61); `      F=0.2` (62); `    else` (63); `      F=0.0` (64); `    endif` (65); `  elseif(depth_rank <0.6)then` (66); `    if(flow_rank<0.2)then` (67); `      F=0.6` (68); `    elseif(flow_rank<0.4)then` (69); `      F=0.4` (70); `    elseif(flow_rank<0.6)then` (71); `      F=0.2` (72); `    else` (73); `      F=0.0` (74); `    endif` (75) |
| 76–96 | 시작 시 1행 루틴, 40행 조건문의 66행 분기 안. 시작 시 `if(depth_rank <0.2)then`(40)의 `elseif(depth_rank <0.6)then` 분기(66) 안이다. 76·84행 ELSEIF와 90행 ELSE를 거쳐 92행 `endif`에서 닫힌다. 수심 등급 <0.8에서는 유속 등급 <0.2에 0.4, <0.4에 0.2, 그 외 0이다. 수심 등급 <1.0에서는 유속 등급 <0.2에 0.2, 그 외 0이다. 나머지 수심은 F=0이다. 체인과 루틴을 종료한다. 원문: `  elseif(depth_rank <0.8)then` (76); `    if(flow_rank<0.2)then` (77); `      F=0.4` (78); `    elseif(flow_rank<0.4)then` (79); `      F=0.2` (80); `    else` (81); `      F=0.0` (82); `    endif` (83); `  elseif(depth_rank <1.0)then` (84); `    if(flow_rank<0.2)then` (85); `      F=0.2` (86); `    else` (87); `      F=0.0` (88); `    endif` (89); `  else` (90); `    F=0.0` (91); `  endif` (92); `!` (94); `  return` (95); `end subroutine underwater_function` (96) [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 16·24–25: n은 real(8) 인수로 선언되며 i_agent·j_agent의 배열 첨자로 쓰인다.
- 16: 입력 t는 이 루틴의 실행문에서 사용되지 않는다.
- 31–35: 두 유속 중 한 성분만 0인 경우에도 flow_now는 0으로 설정된다.
- 3·27–38: 머리말은 사면 경사라고 쓰지만 실행 계산에는 수심과 유속 등급을 사용한다.
