---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Read_data/Rd_TEMPP1.f
lines: 73
sha256: 166783b43d0f2bcab8aeedb15f80ec2b308ff2d922e9ce081d20fc9c059dd779
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Rd_TEMPP1.f — 판독 구간 기록

구간은 1행부터 73행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | RD_TEMPP1의 IMPLICIT·LOGICAL THRU·JE(8)·J_TMP1(4,*)·R_TMP1(2,*)와 두 공백 표식을 선언한다(1–8). 시작 위치 IS=IP+1을 기록한다(10). 12행의 16자 공백 검사로 T1·T2 입력 위치를 구분한다. 참 분기는 ITYP=1로 2F8.0을 읽고(13–14), ELSE(15)는 ITYP=2로 16열을 건너 2F8.0을 읽는다(16–17). IP 증가 후 J_TMP1(2:3,IP)에 JE(1)을 대입한다(20–21). 원문: `      SUBROUTINE RD_TEMPP1( J_TMP1, R_TMP1, IP, CHAR, ITI )` (1); `      IMPLICIT REAL*8 (A-H,O-Z)` (3); `      LOGICAL THRU` (4); `      CHARACTER*80 CHAR` (5); `      CHARACTER*8 BLK /'        '/` (6); `      CHARACTER*16 BLK2 /'                '/` (7); `      DIMENSION JE(8), J_TMP1(4,*), R_TMP1(2,*)` (8); `      IS = IP + 1` (10); `      IF( CHAR(41:56) == BLK2 ) THEN` (12); `        ITYP = 1` (13); `        READ(CHAR,'(BN,8X,2I8,2F8.0)') IDS, JE(1), T1, T2` (14); `      ELSE` (15); `        ITYP = 2` (16); `        READ(CHAR,'(BN,8X,2I8,16X,2F8.0)') IDS, JE(1), T1, T2` (17); `      ENDIF` (18); `      IP = IP + 1` (20); `      J_TMP1(2:3,IP) = JE(1)` (21). [11-04 전수 검증 정정] |
| 23–56 | 시작 시 1행 RD_TEMPP1 안. 23행 무한 루프(loop)는 행을 읽고(25) 27행 연속행 조건을 검사한다. 29행 THRU 조건이 참이면 JE(1:2)를 읽어 저장한다(31–34). 그 안의 36행 THRU 조건이 참이면 JE(1:2)를 다시 읽어 새 열에 저장한다(38–41). 첫 THRU 조건의 ELSE(45)는 JE의 여덟 성분을 읽는다(47). 49행 루프는 JE(I)=0이면 EXIT한다(50). 각 반복은 IP를 증가시켜 J_TMP1(2:3,IP)에 JE(I)를 대입한다(51–52). 원문: `      DO` (23); `        READ(ITI,'(A80)') CHAR` (25); `        IF( CHAR(1:8) == BLK .OR. CHAR(1:1) == '+' ) THEN` (27); `          IF( THRU( CHAR(17:24) ) ) THEN` (29); `            READ(CHAR,'(BN,8X,I8,8X,I8)') JE(1:2)` (31); `            IP = IP + 1` (33); `            J_TMP1(2:3,IP) = JE(1:2)` (34); `            IF( THRU( CHAR(41:48) ) ) THEN` (36); `              READ(CHAR,'(BN,32X,I8,8X,I8)') JE(1:2)` (38); `              IP = IP + 1` (40); `              J_TMP1(2:3,IP) = JE(1:2)` (41); `            ENDIF` (43); `          ELSE` (45); `            READ(CHAR,'(BN,8X,8I8)') JE(:)` (47); `            DO I = 1, 8` (49); `              IF( JE(I) == 0 ) EXIT` (50); `              IP = IP + 1` (51); `              J_TMP1(2:3,IP) = JE(I)` (52); `            ENDDO` (53); `          ENDIF` (55). [11-04 전수 검증 정정] |
| 57–73 | 시작 시 23행 `DO` 안이며 이 루프는 71행 `ENDDO`에서 닫힌다. 27행 `IF( CHAR(1:8) == BLK .OR. CHAR(1:1) == '+' ) THEN` 블록은 69행 `ENDIF`에서 닫힌다. 29행 IF/ELSE는 55행에서 닫혔다. ELSE(57)는 27행의 비연속행 분기이다. IE=IP로 끝 위치를 정하고(59), IS:IE 전체에 IDS·ITYP·T1·T2를 저장한다(61–64). BACKSPACE 후 반환한다(66–67). 조건·루프·루틴 종료와 주석을 포함한다(69–73). 원문: `        ELSE` (57); `          IE = IP` (59); `          J_TMP1(1,IS:IE) = IDS` (61); `          J_TMP1(4,IS:IE) = ITYP` (62); `          R_TMP1(1,IS:IE) = T1` (63); `          R_TMP1(2,IS:IE) = T2` (64); `          BACKSPACE(ITI)` (66); `          RETURN` (67); `        ENDIF` (69); `      ENDDO` (71); `      END` (73). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 50·57–67: JE(I)가 0이면 안쪽 DO만 EXIT한다. IDS·ITYP·T1·T2는 비연속행을 읽은 뒤에 IS:IE 범위에 대입한다. [11-04 전수 검증 정정]
