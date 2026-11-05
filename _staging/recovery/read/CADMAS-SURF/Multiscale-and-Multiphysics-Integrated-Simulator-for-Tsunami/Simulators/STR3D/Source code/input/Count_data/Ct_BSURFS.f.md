---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Count_data/Ct_BSURFS.f
lines: 26
sha256: 42648905d4b1fa4f76ca421a0df35c09227880ee2db7086c0c920638e6e894fe
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Ct_BSURFS.f — 판독 구간 기록

구간은 1행부터 26행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | 80자 CHAR·공백 8자인 BLK·IE(2)를 선언한다(3–5). 현재 레코드로 N_BSRF를 1 증가시킨다(7). 원문: `      SUBROUTINE CT_BSURFS( N_BSRF, ITI )` (1); `      CHARACTER*80 CHAR` (3); `      CHARACTER*8 BLK /'        '/` (4); `      DIMENSION IE(2)` (5); `      N_BSRF = N_BSRF + 1` (7). |
| 9–26 | 시작 시 1행 Ct_BSURFS 루틴 안. 무한 DO에서 다음 레코드를 읽는다(9–11). 연속 레코드이면 두 I8 필드를 IE에 읽고 I=1..2에서 0을 만나면 반환하며 그 전까지 N_BSRF를 늘린다(13–18). 연속 레코드가 아니면 BACKSPACE 후 반환한다(19–24). 원문: `      DO` (9); `        READ(ITI,'(A80)') CHAR` (11); `        IF( CHAR(1:8) == BLK .OR. CHAR(1:1) == '+' ) THEN` (13); `          READ(CHAR,'(BN,8X,I8,24X,I8)') IE(:)` (14); `          DO I = 1, 2` (15); `            IF( IE(I) == 0 ) RETURN` (16); `            N_BSRF = N_BSRF + 1` (17); `          ENDDO` (18); `        ELSE` (19); `          BACKSPACE(ITI)` (20); `          RETURN` (21); `        ENDIF` (22); `      ENDDO` (24); `      END` (26). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 15–17·19–21: IE가 0이면 현재 연속 레코드를 되돌리지 않고 반환한다. 연속 레코드가 아닌 경우에만 BACKSPACE를 수행한다.
