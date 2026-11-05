---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Read_data/Rd_PLOAD2.f
lines: 27
sha256: ebabfd467e2d19c8261638a54388498c6f4e44822e582f5b666337791dc719ae
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Rd_PLOAD2.f — 판독 구간 기록

구간은 1행부터 27행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–27 | RD_PLOAD2의 IMPLICIT·LOGICAL THRU·배열 범위 선언을 포함한다(1–6). 8행 THRU 호출 조건이 참이면 IDS·P·IDE1·IDE2를 읽는다(9). I_PL4를 늘려 J_PL4(1:3,I_PL4)와 R_PL4(1,I_PL4)에 저장한다(10–14). ELSE(15)는 IDS·P·IDE의 여섯 성분을 읽는다(16). 17행 루프(loop)는 IDE(I)가 0이면 EXIT한다(18). 나머지는 I_PL4를 늘려 J_PL4(2,I_PL4)와 J_PL4(3,I_PL4)에 같은 IDE(I)를 저장한다(19–23). 원문: `      SUBROUTINE RD_PLOAD2( J_PL4, R_PL4, I_PL4, CHAR )` (1); `      IMPLICIT REAL*8 (A-H,O-Z)` (3); `      LOGICAL THRU` (4); `      CHARACTER*80 CHAR` (5); `      DIMENSION J_PL4(6,*), R_PL4(4,*), IDE(6)` (6); `      IF( THRU( CHAR(33:40) ) ) THEN` (8); `        READ(CHAR,'(BN,8X,I8,F8.0,I8,8X,I8)') IDS, P, IDE1, IDE2` (9); `        I_PL4 = I_PL4 + 1` (10); `        J_PL4(1,I_PL4) = IDS` (11); `        J_PL4(2,I_PL4) = IDE1` (12); `        J_PL4(3,I_PL4) = IDE2` (13); `        R_PL4(1,I_PL4) = P` (14); `      ELSE` (15); `        READ(CHAR,'(BN,8X,I8,F8.0,6I8)') IDS, P, IDE(:)` (16); `        DO I = 1, 6` (17); `          IF( IDE(I) == 0 ) EXIT` (18); `          I_PL4 = I_PL4 + 1` (19); `          J_PL4(1,I_PL4) = IDS` (20); `          J_PL4(2,I_PL4) = IDE(I)` (21); `          J_PL4(3,I_PL4) = IDE(I)` (22); `          R_PL4(1,I_PL4) = P` (23); `        ENDDO` (24); `      ENDIF` (25); `      END` (27). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6·11–14·20–23: J_PL4의 첫 세 성분과 R_PL4의 첫 성분만 대입한다. 나머지 성분의 초기화는 이 루틴에 없다.
