---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Count_data/Ct_SPCADD.f
lines: 31
sha256: 0c42a94eb529953effca0af96d0189e6dabfb631d58486a1ecbff207a5793293
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Ct_SPCADD.f — 판독 구간 기록

구간은 1행부터 31행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | 80자 CHAR·공백 8자인 BLK·ID(8)를 선언한다(3–5). 현재 레코드에서 7개 집합 번호(set ID)를 읽고 I=1..7에서 첫 0 앞까지 N2를 늘린다(7–12). 원문: `      SUBROUTINE CT_SPCADD( N2, CHAR, ITI )` (1); `      CHARACTER*80 CHAR` (3); `      CHARACTER*8 BLK /'        '/` (4); `      DIMENSION ID(8)` (5); `      READ(CHAR,'(BN,16X,7I8)') ID(1:7)` (7); `      DO I = 1, 7` (9); `        IF( ID(I) == 0 ) RETURN` (10); `        N2 = N2 + 1` (11); `      ENDDO` (12). |
| 14–31 | 시작 시 1행 Ct_SPCADD 루틴 안. 무한 DO에서 다음 레코드를 읽는다(14–16). 첫 8열 전체가 공백이거나 첫 글자가 +이면 8개 집합 번호를 읽고 첫 0 앞까지 N2를 늘린다(18–23). 나머지는 BACKSPACE 후 반환한다(24–29). 원문: `      DO` (14); `        READ(ITI,'(A80)') CHAR` (16); `        IF( CHAR(1:8) == BLK .OR. CHAR(1:1) == '+' ) THEN` (18); `          READ(CHAR,'(BN,8X,8I8)') ID(1:8)` (19); `          DO I = 1, 8` (20); `            IF( ID(I) == 0 ) RETURN` (21); `            N2 = N2 + 1` (22); `          ENDDO` (23); `        ELSE` (24); `          BACKSPACE(ITI)` (25); `          RETURN` (26); `        ENDIF` (27); `      ENDDO` (29); `      END` (31). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 9–11·20–22: 첫 0 항목에서 바로 반환한다. 그 뒤 필드는 검사하지 않는다.
