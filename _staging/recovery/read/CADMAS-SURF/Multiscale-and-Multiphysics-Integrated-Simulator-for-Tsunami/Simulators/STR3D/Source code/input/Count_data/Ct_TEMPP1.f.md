---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Count_data/Ct_TEMPP1.f
lines: 36
sha256: e75537c0bd49da652876dc9680ba052593ba606de0aba7bb5858571f80e9b620
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Ct_TEMPP1.f — 판독 구간 기록

구간은 1행부터 36행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 논리형 THRU·80자 CHAR·공백 8자인 BLK·IE(8)를 선언한다(3–6). 현재 TEMPP1 레코드를 N_TMP1에 1 더한다(8). 원문: `      SUBROUTINE CT_TEMPP1( N_TMP1, ITI )` (1); `      LOGICAL THRU` (3); `      CHARACTER*80 CHAR` (4); `      CHARACTER*8 BLK /'        '/` (5); `      DIMENSION IE(8)` (6); `      N_TMP1 = N_TMP1 + 1` (8). |
| 10–26 | 시작 시 1행 Ct_TEMPP1 루틴 안. 무한 DO에서 다음 레코드를 읽는다(10–12). 첫 8열 전체가 공백이거나 첫 글자가 +인 연속 레코드에서 CHAR(17:24)의 THRU가 참이면 개수를 1 늘리고 CHAR(41:48)의 THRU도 참이면 하나 더 늘린다(14–18). 첫 THRU가 거짓이면 요소 번호 8개를 읽고 첫 0 앞까지 N_TMP1을 늘린다(19–25). 원문: `      DO` (10); `        READ(ITI,'(A80)') CHAR` (12); `        IF( CHAR(1:8) == BLK .OR. CHAR(1:1) == '+' ) THEN` (14); `          IF( THRU( CHAR(17:24) ) ) THEN` (16); `            N_TMP1 = N_TMP1 + 1` (17); `            IF( THRU( CHAR(41:48) ) ) N_TMP1 = N_TMP1 + 1` (18); `          ELSE` (19); `            READ(CHAR,'(BN,8X,8I8)') IE(:)` (20); `            DO I = 1, 8` (21); `              IF( IE(I) == 0 ) EXIT` (22); `              N_TMP1 = N_TMP1 + 1` (23); `            ENDDO` (24); `          ENDIF` (25). [11-04 전수 검증 정정] |
| 27–36 | 시작 시 1행 Ct_TEMPP1 루틴 안. 시작 시 10행 `DO` 안이며 이 루프는 34행 `ENDDO`에서 닫힌다. 시작 시 14행 `IF( CHAR(1:8) == BLK .OR. CHAR(1:1) == '+' ) THEN`의 분기 전환 위치이며 이 IF는 32행 `ENDIF`에서 닫힌다. 연속 레코드가 아닌 ELSE는 BACKSPACE 후 반환한다(27–32). 루프·루틴을 닫는다(34–36). 원문: `        ELSE` (27); `          BACKSPACE(ITI)` (29); `          RETURN` (30); `        ENDIF` (32); `      ENDDO` (34); `      END` (36). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 16–18: THRU 참 분기는 각 범위 길이를 계산하지 않고 범위당 1을 더한다.
- 20–24: 명시 목록에서 IE=0이면 내부 I 루프만 EXIT한다. 바깥 레코드 판독 DO는 계속한다.
