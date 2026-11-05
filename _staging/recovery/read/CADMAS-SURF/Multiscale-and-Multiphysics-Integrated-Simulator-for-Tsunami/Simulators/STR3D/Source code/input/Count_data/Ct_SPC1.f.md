---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Count_data/Ct_SPC1.f
lines: 36
sha256: 6c48165f787c0d6cc63e49a3746d6c5d52ea9038f4724e8de479593a0711e7dd
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Ct_SPC1.f — 판독 구간 기록

구간은 1행부터 36행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | 논리형 THRU·CHAR·BLK·IG(8)를 선언한다(3–6). CHAR(33:40)의 THRU 호출이 참이면 N_SPC1을 1 늘리고 반환한다(8–10). ELSE에서는 현재 레코드의 6개 번호를 읽어 첫 0 앞까지 센다(11–17). 원문: `      SUBROUTINE CT_SPC1( N_SPC1, CHAR, ITI )` (1); `      LOGICAL THRU` (3); `      CHARACTER*80 CHAR` (4); `      CHARACTER*8 BLK /'        '/` (5); `      DIMENSION IG(8)` (6); `      IF( THRU( CHAR(33:40) ) ) THEN` (8); `        N_SPC1 = N_SPC1 + 1` (9); `        RETURN` (10); `      ELSE` (11); `        READ(CHAR,'(BN,24X,6I8)') IG(1:6)` (12); `        DO I = 1, 6` (13); `          IF( IG(I) == 0 ) RETURN` (14); `          N_SPC1 = N_SPC1 + 1` (15); `        ENDDO` (16); `      ENDIF` (17). |
| 19–36 | 시작 시 1행 Ct_SPC1 루틴 안. 무한 DO에서 다음 레코드를 읽는다(19–21). 첫 8열 전체가 공백이거나 첫 글자가 +이면 8개 번호를 읽어 첫 0 앞까지 N_SPC1을 늘린다(23–28). 나머지는 BACKSPACE 후 반환한다(29–34). 원문: `      DO` (19); `        READ(ITI,'(A80)') CHAR` (21); `        IF( CHAR(1:8) == BLK .OR. CHAR(1:1) == '+' ) THEN` (23); `          READ(CHAR,'(BN,8X,8I8)') IG(1:8)` (24); `          DO I = 1, 8` (25); `            IF( IG(I) == 0 ) RETURN` (26); `            N_SPC1 = N_SPC1 + 1` (27); `          ENDDO` (28); `        ELSE` (29); `          BACKSPACE(ITI)` (30); `          RETURN` (31); `        ENDIF` (32); `      ENDDO` (34); `      END` (36). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 8–10: THRU 참 분기는 범위 길이를 계산하지 않고 N_SPC1을 1 늘린 뒤 반환한다.
- 14·26·29–31: 번호가 0이면 즉시 반환한다. 비연속 레코드 분기에서만 BACKSPACE를 수행한다.
