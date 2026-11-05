---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Set_table/St_BCTPARA.f
lines: 22
sha256: beb46e0799aa432efe8de4e568ea23820f5033c621cc0541c371402ebe178d65
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# St_BCTPARA.f — 판독 구간 기록

구간은 1행부터 22행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | ST_BCTPARA의 IMPLICIT와 4–5행의 고정형식(fixed form) 배열 선언 연속문을 포함한다. 7행 루프(loop)는 I=1부터 NICPR까지 순회한다. 9행 내부 루프에서 11행 ID 일치 조건을 검사한다. 처음 일치하는 R_BCTP의 두 성분을 CPR에 복사하고 내부 루프를 EXIT한다(13–14). 루프·루틴 종료 및 주석을 포함한다(16–22). 원문: `      SUBROUTINE ST_BCTPARA( CPR, NICPR, ICPR, J_BCTP, R_BCTP, N_BCTP)` (1); `      IMPLICIT REAL*8 (A-H,O-Z)` (3); `      DIMENSION CPR(2,NICPR), ICPR(2,NICPR), J_BCTP(N_BCTP),` / `     &          R_BCTP(2,N_BCTP)` (4–5; 하나의 고정형식 연속문); `      DO I = 1, NICPR` (7); `        DO J = 1, N_BCTP` (9); `          IF( J_BCTP(J) == ICPR(1,I) ) THEN` (11); `            CPR(:,I) = R_BCTP(:,J)` (13); `            EXIT` (14); `          ENDIF` (16); `        ENDDO` (18); `      ENDDO` (20); `      END` (22). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 7–20: ID가 일치하지 않은 CPR(:,I)는 이 루틴에서 대입하지 않는다.
