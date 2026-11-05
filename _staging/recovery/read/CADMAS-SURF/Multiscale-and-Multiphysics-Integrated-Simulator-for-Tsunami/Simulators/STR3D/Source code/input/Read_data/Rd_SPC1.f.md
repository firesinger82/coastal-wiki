---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Read_data/Rd_SPC1.f
lines: 62
sha256: 4cca0ab48c5fcc7a7e1838b2ef58959e3c317205ce67759b2513964daa654ae0
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Rd_SPC1.f — 판독 구간 기록

구간은 1행부터 62행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–35 | RD_SPC1은 LOGICAL THRU와 IG(8)·J_SPC1(9,*) 등을 선언한다(1–7). 9행 THRU 조건이 참이면 IDS·C·IG(1:2)를 읽는다(11). IP 증가 후 IDS·IG(1)·IG(2)를 저장하며 RESFR를 호출한 뒤 반환한다(13–19). ELSE(21)는 최초 카드(card)의 IDS·C·IG(1:6)을 읽는다(23). 25행 루프(loop)는 IG(I)=0이면 반환한다(26). 이 루프는 J_SPC1(2,IP)·J_SPC1(3,IP)에 같은 IG(I)를 저장하고 RESFR를 호출한다(27–31). 원문: `      SUBROUTINE RD_SPC1( J_SPC1, IP, CHAR, ITI )` (1); `      LOGICAL THRU` (3); `      CHARACTER*80 CHAR` (4); `      CHARACTER*8 C` (5); `      CHARACTER*8 BLK /'        '/` (6); `      DIMENSION IG(8), J_SPC1(9,*)` (7); `      IF( THRU( CHAR(33:40) ) ) THEN` (9); `        READ(CHAR,'(BN,8X,I8,A8,I8,8X,I8)') IDS, C, IG(1:2)` (11); `        IP = IP + 1` (13); `        J_SPC1(1,IP) = IDS` (14); `        J_SPC1(2,IP) = IG(1)` (15); `        J_SPC1(3,IP) = IG(2)` (16); `        CALL RESFR( J_SPC1(4,IP), C )` (17); `        RETURN` (19); `      ELSE` (21); `        READ(CHAR,'(BN,8X,I8,A8,6I8)') IDS, C, IG(1:6)` (23); `        DO I = 1, 6` (25); `          IF( IG(I) == 0 ) RETURN` (26); `          IP = IP + 1` (27); `          J_SPC1(1,IP) = IDS` (28); `          J_SPC1(2,IP) = IG(I)` (29); `          J_SPC1(3,IP) = IG(I)` (30); `          CALL RESFR( J_SPC1(4,IP), C )` (31); `        ENDDO` (32); `      ENDIF` (34). [11-04 전수 검증 정정] |
| 36–62 | 시작 시 1행 RD_SPC1 안이며 9행 IF/ELSE 밖. 36행 무한 루프는 다음 행을 읽는다(38). 40행 연속행 조건이 참이면 IG(1:8)을 읽는다(42). 44행 루프는 IG(I)=0이면 즉시 반환한다(45). 각 항목은 IP를 늘려 저장하고 RESFR를 호출한다(46–50). ELSE(53)는 BACKSPACE 후 반환한다(55–56). 원문: `      DO` (36); `        READ(ITI,'(A80)') CHAR` (38); `        IF( CHAR(1:8) == BLK .OR. CHAR(1:1) == '+' ) THEN` (40); `          READ(CHAR,'(BN,8X,8I8)') IG(1:8)` (42); `          DO I = 1, 8` (44); `            IF( IG(I) == 0 ) RETURN` (45); `            IP = IP + 1` (46); `            J_SPC1(1,IP) = IDS` (47); `            J_SPC1(2,IP) = IG(I)` (48); `            J_SPC1(3,IP) = IG(I)` (49); `            CALL RESFR( J_SPC1(4,IP), C )` (50); `          ENDDO` (51); `        ELSE` (53); `          BACKSPACE(ITI)` (55); `          RETURN` (56); `        ENDIF` (58); `      ENDDO` (60); `      END` (62). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 19·26·36–38: THRU 분기와 최초 카드에서 IG(I)가 0인 분기는 다음 레코드(record)를 읽지 않고 반환한다. [11-04 전수 검증 정정]
- 45·55: 연속행에서 IG(I)가 0이면 BACKSPACE 없이 반환한다. 비연속행에서는 BACKSPACE한다. [11-04 전수 검증 정정]
