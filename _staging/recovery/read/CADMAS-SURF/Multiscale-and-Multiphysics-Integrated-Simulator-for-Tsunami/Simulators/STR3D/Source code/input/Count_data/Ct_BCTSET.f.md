---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Count_data/Ct_BCTSET.f
lines: 21
sha256: 3bfe244768031e627f07dce3edce3e0917a09c2394da187822cc4b63ea9a53b8
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Ct_BCTSET.f — 판독 구간 기록

구간은 1행부터 21행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | 80자 CHAR와 공백 8자인 BLK를 선언하고 현재 BCTSET 레코드를 N_BCTS에 1 더한다(3–6). 원문: `      SUBROUTINE CT_BCTSET( N_BCTS, ITI )` (1); `      CHARACTER*80 CHAR` (3); `      CHARACTER*8 BLK /'        '/` (4); `      N_BCTS = N_BCTS + 1` (6). |
| 8–21 | 시작 시 1행 Ct_BCTSET 루틴 안. 무한 DO에서 다음 80자 레코드를 읽는다(8–10). 첫 8열이 공백이거나 첫 글자가 +이면 연속 레코드(continuation record)로 보고 N_BCTS를 1 더한다(12–13). 나머지는 BACKSPACE로 되돌리고 반환한다(14–19). 원문: `      DO` (8); `        READ(ITI,'(A80)') CHAR` (10); `        IF( CHAR(1:8) == BLK .OR. CHAR(1:1) == '+' ) THEN` (12); `          N_BCTS = N_BCTS + 1` (13); `        ELSE` (14); `          BACKSPACE(ITI)` (15); `          RETURN` (16); `        ENDIF` (17); `      ENDDO` (19); `      END` (21). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 8–19: 연속 레코드 여부는 첫 8열 전체가 공백인지 또는 첫 글자가 +인지 검사한다. READ에는 END=·IOSTAT= 처리가 없다. [11-04 전수 검증 정정]
