---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Set_table/sid_count.f
lines: 17
sha256: 27524ef8095f4c12585c6aa7f87cf3a248a4d07bbf09c8f764f0bb53ffc7405c
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sid_count.f — 판독 구간 기록

구간은 1행부터 17행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | SID_COUNT는 입력 첫 성분의 서로 다른 세트 수를 센다. NSID=0에서 시작한다(5). 각 입력 I에 대해 I-1부터 1까지 역순으로 비교하고 일치하면 해당 입력의 증가를 건너뛴다(7–15). 앞에 일치 항목이 없으면 NSID를 1 증가시킨다(13). 원문(고정형식 연속행은 아래 인접 행을 하나의 문장으로 읽음): `      SUBROUTINE SID_COUNT( NSID, J_IDX, M, N_IDX )` (1) <br> `      DIMENSION J_IDX(M,N_IDX)` (3) <br> `      NSID = 0` (5) <br> `      DO 10 I = 1, N_IDX` (7) <br> `        DO J = I - 1, 1, -1` (9) <br> `          IF( J_IDX(1,I) == J_IDX(1,J) ) GOTO 10` (10) <br> `        ENDDO` (11) <br> `        NSID = NSID + 1` (13) <br> `   10 CONTINUE` (15) <br> `      END` (17) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
