---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Read_data/Rd_TSTEP.f
lines: 30
sha256: d7a6273efb0886a1aea8559625d7d7b8df4fd5940511af79af70cec2adfb6603
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Rd_TSTEP.f — 판독 구간 기록

구간은 1행부터 30행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | RD_TSTEP의 IMPLICIT·ISTP(*)·NSTP(2,*)·DELT(*)와 문자열 선언을 포함한다(1–6). IP를 증가시키고(8), 9–10행 연속문에서 ISTP(1)·NSTP(1,IP)·DELT(IP)·NSTP(2,IP)를 읽는다. 11행 조건부 기본값 식은 NSTP(2,IP)가 0이면 1로 바꾼다. 원문: `      SUBROUTINE RD_TSTEP( ISTP, NSTP, DELT, IP, CHAR, ITI )` (1); `      IMPLICIT REAL*8 (A-H,O-Z)` (3); `      CHARACTER*80 CHAR` (4); `      CHARACTER*8 BLK /'        '/` (5); `      DIMENSION ISTP(*), NSTP(2,*), DELT(*)` (6); `      IP = IP + 1` (8); `      READ(CHAR,'(BN,8X,2I8,F8.0,I8)') ` / `     &  ISTP(1), NSTP(1,IP), DELT(IP), NSTP(2,IP)` (9–10; 하나의 고정형식 연속문); `      IF( NSTP(2,IP) == 0 ) NSTP(2,IP) = 1` (11). [11-04 전수 검증 정정] |
| 13–30 | 시작 시 1행 RD_TSTEP 안. 13행 무한 루프(loop)는 다음 레코드(record)를 읽는다(15). 17행 연속행 조건이 참이면 IP를 늘리고(18), 19–20행 연속문으로 NSTP(1,IP)·DELT(IP)·NSTP(2,IP)를 읽는다. 21행 조건부 기본값 식은 NSTP(2,IP)가 0이면 1로 바꾼다. ELSE(22)는 ISTP(2)에 끝 위치를 기록하고 BACKSPACE 후 반환한다(23–25). 원문: `      DO` (13); `        READ(ITI,'(A80)') CHAR` (15); `        IF( CHAR(1:8) == BLK .OR. CHAR(1:1) == '+' ) THEN` (17); `          IP = IP + 1` (18); `          READ(CHAR,'(BN,16X,I8,F8.0,I8)') ` / `     &      NSTP(1,IP), DELT(IP), NSTP(2,IP)` (19–20; 하나의 고정형식 연속문); `          IF( NSTP(2,IP) == 0 ) NSTP(2,IP) = 1` (21); `        ELSE` (22); `          ISTP(2) = IP` (23); `          BACKSPACE(ITI)` (24); `          RETURN` (25); `        ENDIF` (26); `      ENDDO` (28); `      END` (30). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
