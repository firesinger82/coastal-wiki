---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Set_table/tb_count.f
lines: 13
sha256: ea5ef395870e1d9702b1b3007ff8402380c5342c530f39de64aa5ec53b0981b5
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# tb_count.f — 판독 구간 기록

구간은 1행부터 13행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | TB_COUNT는 N=0에서 시작한다(5). 각 입력 I의 J_IDX(2,I):J_IDX(3,I) 범위를 순회한다(7–11). 역표 INDR(J)>0인 번호마다 N을 1 증가시킨다(9). 배열 J_IDX(M,N_IDX)·INDR(*) 선언과 빈 주석·루틴 끝을 포함한다(1–13). 원문(고정형식 연속행은 아래 인접 행을 하나의 문장으로 읽음): `      SUBROUTINE TB_COUNT( N, J_IDX, M, N_IDX, INDR )` (1) <br> `      DIMENSION J_IDX(M,N_IDX), INDR(*)` (3) <br> `      N = 0` (5) <br> `      DO I = 1, N_IDX` (7) <br> `        DO J = J_IDX(2,I), J_IDX(3,I)` (8) <br> `          IF( INDR(J) > 0 ) N = N + 1` (9) <br> `        ENDDO` (10) <br> `      ENDDO` (11) <br> `      END` (13) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
