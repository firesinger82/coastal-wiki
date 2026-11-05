---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Read_data/Rd_RLOAD1.f
lines: 30
sha256: 8cf24c5086ea43bed4392d1fa4618b051f99915d37478451c75aea31a2a7b314
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Rd_RLOAD1.f — 판독 구간 기록

구간은 1행부터 30행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–23 | RD_RLOAD1의 IMPLICIT·IRL1(7)을 선언하고 ID·IDEX·ITC·ITD를 읽는다(1–7). ITYP 기본값은 0이다(9). 10행 루프(loop)는 57–64열을 검색하고 공백이면 CYCLE한다(11). 12·14·16·18행 조건으로 0/L·1/D·2/V·3/A를 각각 0·1·2·3에 대응시킨다(13·15·17·19). ELSE는 없으므로 첫 비공백 문자가 모든 조건과 불일치하면 ITYP는 기본값 0으로 남는다(9–20). 공백이 아닌 첫 문자 처리 후 EXIT한다(21). 원문: `      SUBROUTINE RD_RLOAD1( IRL1, CHAR )` (1); `      IMPLICIT REAL*8 (A-H,O-Z)` (3); `      CHARACTER*80 CHAR` (4); `      DIMENSION IRL1(7)` (5); `      READ(CHAR,'(BN,8X,2I8,16X,3I8)') ID, IDEX, ITC, ITD` (7); `      ITYP= 0` (9); `      DO I = 57, 64` (10); `        IF( CHAR(I:I) == ' ' ) CYCLE` (11); `        IF( CHAR(I:I) == '0' .OR. CHAR(I:I) == 'L' ) THEN` (12); `          ITYP = 0` (13); `        ELSEIF( CHAR(I:I) == '1' .OR. CHAR(I:I) == 'D' ) THEN` (14); `          ITYP = 1` (15); `        ELSEIF( CHAR(I:I) == '2' .OR. CHAR(I:I) == 'V' ) THEN` (16); `          ITYP = 2` (17); `        ELSEIF( CHAR(I:I) == '3' .OR. CHAR(I:I) == 'A' ) THEN` (18); `          ITYP = 3` (19); `        ENDIF` (20); `        EXIT` (21); `      ENDDO` (22). [11-04 전수 검증 보완] |
| 24–30 | 시작 시 1행 RD_RLOAD1 안. ID·IDEX는 IRL1(1:2), ITC·ITD·ITYP는 IRL1(5:7)에 저장한다(24–28). 끝 주석·END를 포함한다(29–30). 원문: `      IRL1(1) = ID` (24); `      IRL1(2) = IDEX` (25); `      IRL1(5) = ITC` (26); `      IRL1(6) = ITD` (27); `      IRL1(7) = ITYP` (28); `      END` (30). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 10–22: 첫 비공백 문자가 네 조건 모두와 일치하지 않아도 EXIT하며 ITYP는 기본값 0으로 남는다.
- 5·24–28: IRL1(3:4)는 이 루틴에서 대입하지 않는다.
