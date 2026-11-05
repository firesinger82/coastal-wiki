---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Read_data/Rd_PLOAD4.f
lines: 38
sha256: b5de4d8a899435db7d41680b1f5cae7f8c479ac32d88357d20b119ee931d6bcb
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Rd_PLOAD4.f — 판독 구간 기록

구간은 1행부터 38행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | RD_PLOAD4의 IMPLICIT·LOGICAL THRU·배열 선언을 포함한다(1–7). 9행 THRU 조건이 참이면 IDS·IDE1·P1·IDE2를 읽고 IG1·IG3을 0으로 설정한다(10–12). ELSE(13)는 IDS·IDE1·P1·IG1·IG3을 읽는다(14). 이 분기는 IDE2에 IDE1을 대입한다(15). 원문: `      SUBROUTINE RD_PLOAD4( J_PL4, R_PL4, CHAR, ITI )` (1); `      IMPLICIT REAL*8 (A-H,O-Z)` (3); `      LOGICAL THRU` (4); `      CHARACTER*80 CHAR` (5); `      CHARACTER*8 BLK /'        '/` (6); `      DIMENSION J_PL4(6), R_PL4(4), RN(3)` (7); `      IF( THRU( CHAR(57:64) ) ) THEN` (9); `        READ(CHAR,'(BN,8X,2I8,F8.0,32X,I8)') IDS, IDE1, P1, IDE2` (10); `        IG1 = 0` (11); `        IG3 = 0` (12); `      ELSE` (13); `        READ(CHAR,'(BN,8X,2I8,F8.0,24X,2I8)') IDS, IDE1, P1, IG1, IG3` (14); `        IDE2 = IDE1` (15); `      ENDIF` (16). [11-04 전수 검증 정정] |
| 18–38 | 시작 시 1행 RD_PLOAD4 안. 다음 레코드(record)를 읽고(18) 20행 조건으로 연속행을 판별한다. 연속행은 IDC와 RN의 세 성분을 읽는다(21). ELSE(22)는 BACKSPACE 후 IDC·RN을 0으로 설정한다(23–25). IDS·IDE1·IDE2·IG1·IG3·IDC를 J_PL4(1:6)에 저장한다(28–33). R_PL4(1)은 P1이고 R_PL4(2:4)는 RN이다(35–36). 원문: `      READ(ITI,'(A80)') CHAR` (18); `      IF( CHAR(1:8) == BLK .OR. CHAR(1:1) == '+' ) THEN` (20); `        READ(CHAR,'(BN,8X,I8,3F8.0)') IDC, RN(:)` (21); `      ELSE` (22); `        BACKSPACE(ITI)` (23); `        IDC = 0` (24); `        RN(:) = 0.` (25); `      ENDIF` (26); `      J_PL4(1) = IDS` (28); `      J_PL4(2) = IDE1` (29); `      J_PL4(3) = IDE2` (30); `      J_PL4(4) = IG1` (31); `      J_PL4(5) = IG3` (32); `      J_PL4(6) = IDC` (33); `      R_PL4(1) = P1` (35); `      R_PL4(2:4) = RN(:)` (36); `      END` (38). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 10·14: 첫 카드의 실수 필드는 P1 하나만 읽는다. 35–36행의 R_PL4(2:4)에는 RN을 저장한다. RN은 연속행에서 읽거나 연속행이 없으면 0으로 설정한다(20–26). [11-04 전수 검증 정정]
