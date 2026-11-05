---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Read_data/Rd_FORCE.f
lines: 19
sha256: cb6517b306bcd6d6f305659c37a80094740eb54490d6a7ee510df5167bf79344
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Rd_FORCE.f — 판독 구간 기록

구간은 1행부터 19행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | RD_FORCE의 IMPLICIT와 J_FRC(3)·R_FRC(6)·RN(3) 선언을 포함한다(1–5). IDS·IG·IDC·F·RN을 읽고 정수 세 성분을 저장한다(7–11). 13행 FORCE 조건에서는 R_FRC(1:3)에 F와 RN의 곱을 대입한다(14). 15행 MOMENT 조건에서는 R_FRC(4:6)에 대입한다(16). ELSE는 없으므로 두 조건이 모두 거짓이면 R_FRC를 대입하지 않는다(13–17). 조건·루틴 종료를 포함한다(17–19). 원문: `      SUBROUTINE RD_FORCE( J_FRC, R_FRC, CHAR )` (1); `      IMPLICIT REAL*8 (A-H,O-Z)` (3); `      CHARACTER*80 CHAR` (4); `      DIMENSION J_FRC(3), R_FRC(6), RN(3)` (5); `      READ(CHAR,'(BN,8X,3I8,4F8.0)') IDS, IG, IDC, F, RN(:)` (7); `      J_FRC(1) = IDS` (9); `      J_FRC(2) = IG` (10); `      J_FRC(3) = IDC` (11); `      IF( CHAR(1:8) == 'FORCE   ' ) THEN` (13); `        R_FRC(1:3) = F * RN(:)` (14); `      ELSEIF( CHAR(1:8) == 'MOMENT  ' ) THEN` (15); `        R_FRC(4:6) = F * RN(:)` (16); `      ENDIF` (17); `      END` (19). [11-04 전수 검증 정정] [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 13–17: FORCE 분기는 R_FRC(4:6)를 대입하지 않는다. MOMENT 분기는 R_FRC(1:3)를 대입하지 않는다.
