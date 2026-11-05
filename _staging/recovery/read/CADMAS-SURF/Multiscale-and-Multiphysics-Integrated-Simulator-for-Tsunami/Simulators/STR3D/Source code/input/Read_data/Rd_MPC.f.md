---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Read_data/Rd_MPC.f
lines: 43
sha256: 685669144cbd9cd7c2b27b4e7d205041084c6afc6fde2ab0561de3c24ad52e45
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Rd_MPC.f — 판독 구간 기록

구간은 1행부터 43행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | RD_MPC의 IMPLICIT·배열 범위 선언을 포함한다(1–6). 8–9행 연속문에서 IDS와 두 묶음의 IG(I)·IC(I)·A(I)를 읽는다. J_MPC(2)는 저장 시작 위치 IP+1이다(12). 14행 루프(loop)는 두 묶음을 IP 증가 후 J2_MPC와 R2_MPC에 저장한다(15–18). 원문: `      SUBROUTINE RD_MPC( J_MPC, J2_MPC, R2_MPC, IP, CHAR, ITI )` (1); `      IMPLICIT REAL*8 (A-H,O-Z)` (3); `      CHARACTER*80 CHAR` (4); `      CHARACTER*8 BLK /'        '/` (5); `      DIMENSION J_MPC(3), J2_MPC(2,*), R2_MPC(*), IG(2), IC(2), A(2)` (6); `      READ(CHAR,'(BN,8X,I8,2(2I8,F8.0))') ` / `     &  IDS, ( IG(I), IC(I), A(I), I = 1, 2 )` (8–9; 하나의 고정형식 연속문); `      J_MPC(1) = IDS` (11); `      J_MPC(2) = IP + 1` (12); `      DO I = 1, 2` (14); `        IP = IP + 1` (15); `        J2_MPC(1,IP) = IG(I)` (16); `        J2_MPC(2,IP) = IC(I)` (17); `        R2_MPC(IP) = A(I)` (18); `      ENDDO` (19). [11-04 전수 검증 정정] |
| 21–43 | 시작 시 1행 RD_MPC 안. 21행 무한 루프에서 레코드(record)를 읽고(23) 25행 조건으로 연속행을 판정한다. 연속행 READ는 26–27행의 한 문장이다. 28행 루프는 IG(I)=0이면 EXIT한다(29). 유효 항목은 IP 증가 후 저장한다(30–33). ELSE(35)는 J_MPC(3)에 끝 위치 IP를 기록하고 BACKSPACE 후 반환한다(36–38). 원문: `      DO` (21); `        READ(ITI,'(A80)') CHAR` (23); `        IF( CHAR(1:8) == BLK .OR. CHAR(1:1) == '+' ) THEN` (25); `          READ(CHAR,'(BN,16X,2(2I8,F8.0))') ` / `     &      ( IG(I), IC(I), A(I), I = 1, 2 )` (26–27; 하나의 고정형식 연속문); `          DO I = 1, 2` (28); `            IF( IG(I) == 0 ) EXIT` (29); `            IP = IP + 1` (30); `            J2_MPC(1,IP) = IG(I)` (31); `            J2_MPC(2,IP) = IC(I)` (32); `            R2_MPC(IP) = A(I)` (33); `          ENDDO` (34); `        ELSE` (35); `          J_MPC(3) = IP` (36); `          BACKSPACE(ITI)` (37); `          RETURN` (38); `        ENDIF` (39); `      ENDDO` (41); `      END` (43). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 14–19·28–34: 최초 카드(card)의 두 묶음은 IG=0 검사 없이 저장한다. 연속 카드의 두 묶음에는 IG=0 종료 검사가 있다.
