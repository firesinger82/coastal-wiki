---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Read_data/Rd_LOAD.f
lines: 38
sha256: 2578cdd6ffbeed78d7446c029643fe691a6d39ba2ccdcb45090f649927d7490e
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Rd_LOAD.f — 판독 구간 기록

구간은 1행부터 38행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | RD_LOAD의 IMPLICIT와 LOAD(2)·SILD(*)·LILD(*)·S(4)·L(4)을 선언한다(1–6). 8–9행 연속문에서 LOAD(1), SLOD와 세 S(I)·L(I) 쌍을 읽는다. 11행 루프(loop)는 L(I)=0에서 끝난다(12). 유효 항목은 IP를 증가시켜 SILD·LILD에 저장한다(13–15). 원문: `      SUBROUTINE RD_LOAD( LOAD, SLOD, SILD, LILD, IP, CHAR, ITI )` (1); `      IMPLICIT REAL*8 (A-H,O-Z)` (3); `      CHARACTER*80 CHAR` (4); `      CHARACTER*8 BLK /'        '/` (5); `      DIMENSION LOAD(2), SILD(*), LILD(*), S(4), L(4)` (6); `      READ(CHAR,'(BN,8X,I8,F8.0,3(F8.0,I8))') ` / `     &  LOAD(1), SLOD, ( S(I), L(I), I = 1, 3 )` (8–9; 하나의 고정형식 연속문); `      DO I = 1, 3` (11); `        IF( L(I) == 0 ) EXIT` (12); `        IP = IP + 1` (13); `        SILD(IP) = S(I)` (14); `        LILD(IP) = L(I)` (15); `      ENDDO` (16). [11-04 전수 검증 정정] |
| 18–38 | 시작 시 1행 RD_LOAD 안. 18행 무한 루프에서 다음 행을 읽는다(20). 22행 조건이 참이면 연속 카드(card)의 네 쌍을 읽고(23), 24행 루프와 25행 종료 조건으로 유효 쌍을 저장한다(26–28). ELSE(30)는 LOAD(2)에 최종 IP를 기록하고 BACKSPACE 후 반환한다(31–33). 원문: `      DO` (18); `        READ(ITI,'(A80)') CHAR` (20); `        IF( CHAR(1:8) == BLK .OR. CHAR(1:1) == '+' ) THEN` (22); `          READ(CHAR,'(BN,8X,4(F8.0,I8))') ( S(I), L(I), I = 1, 4 )` (23); `          DO I = 1, 4` (24); `            IF( L(I) == 0 ) EXIT` (25); `            IP = IP + 1` (26); `            SILD(IP) = S(I)` (27); `            LILD(IP) = L(I)` (28); `          ENDDO` (29); `        ELSE` (30); `          LOAD(2) = IP` (31); `          BACKSPACE(ITI)` (32); `          RETURN` (33); `        ENDIF` (34); `      ENDDO` (36); `      END` (38). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 12·25: L(I)가 0이면 해당 DO 루프만 EXIT한다. 연속행 판독의 무한 루프는 계속된다. [11-04 전수 검증 정정]
