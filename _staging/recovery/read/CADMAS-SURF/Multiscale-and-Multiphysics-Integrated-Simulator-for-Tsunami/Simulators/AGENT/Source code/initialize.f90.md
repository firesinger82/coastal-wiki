---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/AGENT/Source code/initialize.f90
lines: 42
sha256: a048caf91ce65748d0560d59f071b3c2a4c666e4fae2d4bf5b3abfb0ab466956
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# initialize.f90 — 판독 구간 기록

구간은 1행부터 42행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | 초기화라는 주석(3). 시간·에이전트·피난처·CADMAS 모듈 및 `implicit none`(11), 인수와 지역 변수를 선언한다. 원문: `subroutine initialize(ierr)` (1); `!----------------------------------------` (2); `! 初期化` (3); `!----------------------------------------` (4); `  use m_timectl,only: time,time_start` (5); `  use m_agent,only: rw_tnext &` (6); `                 & ,istat_escaped,istat_moving,istat_dead &` (7); `                 & ,n_agent,agent_status,i_agent,j_agent,agent_z` (8); `  use m_potential,only: agent_shelter` (9); `  use m_cadmas,only: height` (10); `  implicit none` (11); `!` (12); `!  [arguments]` (13); `  integer,intent(out):: ierr` (14); `!` (15); `!  [local variables]` (16); `  character(32):: rout='initialize'` (17); `  integer:: n,m` (18); `!` (19); `  ierr=0` (20); `!` (21); `!` (22) |
| 23–42 | 시작 시 1행 루틴 안. 계산 시작 시각 초기화(23), 에이전트 상태 초기화(26), 에이전트 통계값 초기화(33), 무작위 보행(random walk) 갱신 시각 초기화(38) 주석. time=time_start, 상태 1, 피난처 0을 설정한다. n=1..n_agent에서 z를 height로 설정한다. 피난 완료·사망 수는 0, 이동 중 수는 n_agent, rw_tnext는 0으로 둔다. 원문: `!計算開始時刻の初期化` (23); `  time=time_start` (24); `!` (25); `!エージェントの状態を初期化` (26); `  agent_status(:)=1` (27); `  agent_shelter(:)=0` (28); `  do n=1,n_agent` (29); `    agent_z(n) = height(i_agent(n),j_agent(n))` (30); `  enddo` (31); `!` (32); `!エージェント統計値を初期化` (33); `  istat_escaped = 0` (34); `  istat_moving  = n_agent` (35); `  istat_dead    = 0` (36); `!` (37); `!RandomWalk更新時刻の初期化` (38); `  rw_tnext=0.0d0` (39); `!` (40); `  return` (41); `end subroutine initialize` (42) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 17–18: rout와 m은 선언되지만 이후 실행문에서 참조되지 않는다.
