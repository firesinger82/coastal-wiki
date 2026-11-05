---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Set_table/nm_count.f
lines: 26
sha256: 79a7217b35ea77392c1e209a8c8f2c1e773d754ddf71287900db427218bb90b2
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# nm_count.f — 판독 구간 기록

구간은 1행부터 26행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–26 | NM_COUNT는 요소 저장 배열의 첫 차원 NM을 산출한다. ND_MAX 기본값은 2다(5). 셸 절점을 최대 8개까지 세며 8개인 경우 9로 바꾼다(7–14). 고체 절점을 최대 20개까지 세고 최대값을 갱신한다(16–22). 최종 NM은 ND_MAX+7이다(24). 배열 범위와 암시적 정수 변수 이름을 원문으로 보존한다. 원문(고정형식 연속행은 아래 인접 행을 하나의 문장으로 읽음): `      SUBROUTINE NM_COUNT( NM, J_SHEL, N_SHEL, J_SOL, N_SOL )` (1) <br> `      DIMENSION J_SHEL(10,N_SHEL), J_SOL(22,N_SOL)` (3) <br> `      ND_MAX = 2` (5) <br> `      DO I = 1, N_SHEL` (7) <br> `        DO J = 1, 8` (8) <br> `          IF( J_SHEL(2+J,I) == 0 ) EXIT` (9) <br> `        ENDDO` (10) <br> `        ND = J - 1` (11) <br> `        IF( ND == 8 ) ND = 9` (12) <br> `        IF( ND > ND_MAX ) ND_MAX = ND` (13) <br> `      ENDDO` (14) <br> `      DO I = 1, N_SOL` (16) <br> `        DO J = 1, 20` (17) <br> `          IF( J_SOL(2+J,I) == 0 ) EXIT` (18) <br> `        ENDDO` (19) <br> `        ND = J - 1` (20) <br> `        IF( ND > ND_MAX ) ND_MAX = ND` (21) <br> `      ENDDO` (22) <br> `      NM = ND_MAX + 7` (24) <br> `      END` (26) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
