---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Read_data/Rd_TLOAD1.f
lines: 29
sha256: 30f3e12ab70502f0cd07f49e78e2ac9e166d9a95c941138e38da4992ad73037a
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Rd_TLOAD1.f — 판독 구간 기록

구간은 1행부터 29행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–29 | RD_TLOAD1의 IMPLICIT·ITL1(4)을 선언하고 ID·IDEX·IDT를 읽는다(1–7). ITYP 기본값은 0이다(9). 10행 루프(loop)는 33–40열을 검색하고 공백이면 CYCLE한다(11). 12·14·16·18행 조건으로 0/L·1/D·2/V·3/A를 각각 0·1·2·3에 대응시킨다(13·15·17·19). ELSE는 없으므로 첫 비공백 문자가 모든 조건과 불일치하면 ITYP는 기본값 0으로 남는다(9–20). 공백이 아닌 첫 문자 처리 후 EXIT한다(21). ITL1(1:4)에 ID·IDEX·ITYP·IDT를 저장한다(24–27). 원문: `      SUBROUTINE RD_TLOAD1( ITL1, CHAR )` (1); `      IMPLICIT REAL*8 (A-H,O-Z)` (3); `      CHARACTER*80 CHAR` (4); `      DIMENSION ITL1(4)` (5); `      READ(CHAR,'(BN,8X,2I8,16X,I8)') ID, IDEX, IDT` (7); `      ITYP= 0` (9); `      DO I = 33, 40` (10); `        IF( CHAR(I:I) == ' ' ) CYCLE` (11); `        IF( CHAR(I:I) == '0' .OR. CHAR(I:I) == 'L' ) THEN` (12); `          ITYP = 0` (13); `        ELSEIF( CHAR(I:I) == '1' .OR. CHAR(I:I) == 'D' ) THEN` (14); `          ITYP = 1` (15); `        ELSEIF( CHAR(I:I) == '2' .OR. CHAR(I:I) == 'V' ) THEN` (16); `          ITYP = 2` (17); `        ELSEIF( CHAR(I:I) == '3' .OR. CHAR(I:I) == 'A' ) THEN` (18); `          ITYP = 3` (19); `        ENDIF` (20); `        EXIT` (21); `      ENDDO` (22); `      ITL1(1) = ID` (24); `      ITL1(2) = IDEX` (25); `      ITL1(3) = ITYP` (26); `      ITL1(4) = IDT` (27); `      END` (29). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 10–22: 첫 비공백 문자가 네 조건 모두와 일치하지 않아도 EXIT하며 ITYP는 기본값 0으로 남는다.
