---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Read_data/Rd_BSURFS.f
lines: 34
sha256: 985181c00112ab204c772a468fa147f61e672dc356819360a2483c5ffd5999fe
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Rd_BSURFS.f — 판독 구간 기록

구간은 1행부터 34행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | RD_BSURFS는 IE(2)·IG(3,2)·J_BSRF(5,*)를 선언한다(1–5). 첫 카드(card)에서 ID, IE(1), IG(:,1)을 읽는다(7). IP를 증가시키고 J_BSRF의 다섯 성분에 저장한다(9–12). 원문: `      SUBROUTINE RD_BSURFS( J_BSRF, IP, CHAR, ITI )` (1); `      CHARACTER*80 CHAR` (3); `      CHARACTER*8 BLK /'        '/` (4); `      DIMENSION IE(2), IG(3,2), J_BSRF(5,*)` (5); `      READ(CHAR,'(BN,8X,I8,24X,4I8)') ID, IE(1), IG(:,1)` (7); `      IP = IP + 1` (9); `      J_BSRF(1,IP) = ID` (10); `      J_BSRF(2,IP) = IE(1)` (11); `      J_BSRF(3:5,IP) = IG(:,1)` (12). [11-04 전수 검증 정정] |
| 14–34 | 시작 시 1행 RD_BSURFS 안. 14행 무한 루프(loop)는 다음 레코드(record)를 읽는다(16). 18행 연속행 조건이 참이면 READ의 내포 DO(implied DO)로 두 묶음을 읽는다(19). 20행 루프에서 IE(I)가 0이면 즉시 반환한다(21). 나머지는 IP를 늘려 동일 ID와 IE(I)·IG(:,I)를 저장한다(22–25). ELSE(27)는 한 레코드 되돌린 후 반환한다(28–29). 원문: `      DO` (14); `        READ(ITI,'(A80)') CHAR` (16); `        IF( CHAR(1:8) == BLK .OR. CHAR(1:1) == '+' ) THEN` (18); `          READ(CHAR,'(BN,8X,8I8)') ( IE(I), IG(:,I), I = 1, 2 )` (19); `          DO I = 1, 2` (20); `            IF( IE(I) == 0 ) RETURN` (21); `            IP = IP + 1` (22); `            J_BSRF(1,IP) = ID` (23); `            J_BSRF(2,IP) = IE(I)` (24); `            J_BSRF(3:5,IP) = IG(:,I)` (25); `          ENDDO` (26); `        ELSE` (27); `          BACKSPACE(ITI)` (28); `          RETURN` (29); `        ENDIF` (30); `      ENDDO` (32); `      END` (34). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 21: IE(I)가 0인 연속행에서는 BACKSPACE 없이 반환한다. 27–29행의 비연속행 반환은 BACKSPACE를 수행한다. [11-04 전수 검증 정정]
