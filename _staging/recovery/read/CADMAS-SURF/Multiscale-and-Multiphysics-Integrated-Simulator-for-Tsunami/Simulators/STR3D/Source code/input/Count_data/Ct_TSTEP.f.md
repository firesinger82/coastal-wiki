---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Count_data/Ct_TSTEP.f
lines: 21
sha256: be682eabb8eb93583dd0f05ea84a3493824a34f94dd2ebb544119d1c9da853c9
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Ct_TSTEP.f — 판독 구간 기록

구간은 1행부터 21행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | CT_TSTEP 선언과 80자 판독 버퍼(buffer), 공백 표식 선언(1–4). 최초 카드(card)를 N2_TSTP에 계수한다(6). 원문: `      SUBROUTINE CT_TSTEP( N2_TSTP, ITI )` (1); `      CHARACTER*80 CHAR` (3); `      CHARACTER*8 BLK /'        '/` (4); `      N2_TSTP = N2_TSTP + 1` (6). |
| 8–21 | 시작 시 1행 CT_TSTEP 안. 8행 무한 루프(loop)에서 80자씩 읽는다(10). 12행 조건이 참이면 연속 카드를 계수한다(13). ELSE(14)는 입력을 한 레코드(record) 되돌리고 반환한다(15–16). 루프·루틴 종료와 주석을 포함한다(17–21). 원문: `      DO` (8); `        READ(ITI,'(A80)') CHAR` (10); `        IF( CHAR(1:8) == BLK .OR. CHAR(1:1) == '+' ) THEN` (12); `          N2_TSTP = N2_TSTP + 1` (13); `        ELSE` (14); `          BACKSPACE(ITI)` (15); `          RETURN` (16); `        ENDIF` (17); `      ENDDO` (19); `      END` (21). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 8–19: 무한 루프 안의 READ에는 END·ERR·IOSTAT 지정이 없다.
