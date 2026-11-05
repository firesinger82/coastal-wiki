---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Count_data/Ct_LOAD.f
lines: 31
sha256: 02e49027e165ddaa8a40dd075349cc901bea750e93ec5750b01576a559d6d433
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Ct_LOAD.f — 판독 구간 기록

구간은 1행부터 31행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | CHAR·BLK·LID(4)를 선언한다(3–5). 현재 레코드에서 3개의 하중 번호(load ID)를 LID(1:3)에 읽는다(7). I=1..3에서 0을 만나면 반환하고 각 유효 항목을 N2_LD에 더한다(9–12). 원문: `      SUBROUTINE CT_LOAD( N2_LD, CHAR, ITI )` (1); `      CHARACTER*80 CHAR` (3); `      CHARACTER*8 BLK /'        '/` (4); `      DIMENSION LID(4)` (5); `      READ(CHAR,'(BN,24X,3(8X,I8))') LID(1:3)` (7); `      DO I = 1, 3` (9); `        IF( LID(I) == 0 ) RETURN` (10); `        N2_LD = N2_LD + 1` (11); `      ENDDO` (12). |
| 14–31 | 시작 시 1행 Ct_LOAD 루틴 안. 무한 DO에서 다음 80자 레코드를 읽는다(14–16). 첫 8열 전체가 공백이거나 첫 글자가 +이면 4개 하중 번호를 읽어 첫 0 앞까지 N2_LD를 늘린다(18–23). 나머지는 BACKSPACE 후 반환한다(24–29). 원문: `      DO` (14); `        READ(ITI,'(A80)') CHAR` (16); `        IF( CHAR(1:8) == BLK .OR. CHAR(1:1) == '+' ) THEN` (18); `          READ(CHAR,'(BN,8X,4(8X,I8))') LID(1:4)` (19); `          DO I = 1, 4` (20); `            IF( LID(I) == 0 ) RETURN` (21); `            N2_LD = N2_LD + 1` (22); `          ENDDO` (23); `        ELSE` (24); `          BACKSPACE(ITI)` (25); `          RETURN` (26); `        ENDIF` (27); `      ENDDO` (29); `      END` (31). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 9–11·20–22: 첫 0 항목에서 바로 반환한다. 그 뒤 필드는 검사하지 않는다.
