---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Count_data/Ct_MPC.f
lines: 26
sha256: 44f2ec7ffe1e8c402a8d20e7c52c3cdbc588496968dc26ab332ac6b1d0ab5fa9
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Ct_MPC.f — 판독 구간 기록

구간은 1행부터 26행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | CHAR·BLK·IG(2)를 선언한다(3–5). 다점 구속(multipoint constraint)의 현재 레코드 항목을 검사하는 READ 없이 N2를 2 늘린다(7). 원문: `      SUBROUTINE CT_MPC( N2, ITI )` (1); `      CHARACTER*80 CHAR` (3); `      CHARACTER*8 BLK /'        '/` (4); `      DIMENSION IG(2)` (5); `      N2 = N2 + 2` (7). |
| 9–26 | 시작 시 1행 Ct_MPC 루틴 안. 무한 DO에서 다음 레코드를 읽는다(9–11). 첫 8열 전체가 공백이거나 첫 글자가 +인 연속 레코드에서 두 절점 번호를 읽고 첫 0 앞까지 N2를 늘린다(13–18). 나머지는 BACKSPACE 후 반환한다(19–24). 원문: `      DO` (9); `        READ(ITI,'(A80)') CHAR` (11); `        IF( CHAR(1:8) == BLK .OR. CHAR(1:1) == '+' ) THEN` (13); `          READ(CHAR,'(BN,16X,I8,16X,I8)') IG(:)` (14); `          DO I = 1, 2` (15); `            IF( IG(I) == 0 ) RETURN` (16); `            N2 = N2 + 1` (17); `          ENDDO` (18); `        ELSE` (19); `          BACKSPACE(ITI)` (20); `          RETURN` (21); `        ENDIF` (22); `      ENDDO` (24); `      END` (26). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 7·14–17: 첫 레코드 항목은 2개로 고정 가산한다. 연속 레코드는 실제 읽은 IG 값이 0인지 검사한다.
