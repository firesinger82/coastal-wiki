---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Read_data/Rd_SPCADD.f
lines: 34
sha256: e1740885aa344b7a2a1e4b5ec526450756b42e4cfe7d686209d8102f5902ec5c
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Rd_SPCADD.f — 판독 구간 기록

구간은 1행부터 34행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | RD_SPCADD는 ISPA(2)·NSPA(*)·ID(8)과 문자열을 선언한다(1–5). 최초 카드(card)에서 ISPA(1)과 ID(1:7)을 읽는다(7). 9행 루프(loop)는 ID(I)=0에서 EXIT하고(10), IP 증가 후 NSPA에 저장한다(11–12). 원문: `      SUBROUTINE RD_SPCADD( ISPA, NSPA, IP, CHAR, ITI )` (1); `      CHARACTER*80 CHAR` (3); `      CHARACTER*8 BLK /'        '/` (4); `      DIMENSION ISPA(2), NSPA(*), ID(8)` (5); `      READ(CHAR,'(BN,8X,8I8)') ISPA(1), ID(1:7)` (7); `      DO I = 1, 7` (9); `        IF( ID(I) == 0 ) EXIT` (10); `        IP = IP + 1` (11); `        NSPA(IP) = ID(I)` (12); `      ENDDO` (13). [11-04 전수 검증 정정] |
| 15–34 | 시작 시 1행 RD_SPCADD 안. 15행 무한 루프에서 레코드(record)를 읽고(17) 19행 조건으로 연속행을 판별한다. 연속행은 여덟 개 ID를 읽는다(20). 21행 루프는 ID(I)=0에서 EXIT하며(22), 나머지 항목을 IP 증가 후 저장한다(23–24). ELSE(26)는 ISPA(2)에 최종 IP를 기록하고 BACKSPACE 후 반환한다(27–29). 원문: `      DO` (15); `        READ(ITI,'(A80)') CHAR` (17); `        IF( CHAR(1:8) == BLK .OR. CHAR(1:1) == '+' ) THEN` (19); `          READ(CHAR,'(BN,8X,8I8)') ID(1:8)` (20); `          DO I = 1, 8` (21); `            IF( ID(I) == 0 ) EXIT` (22); `            IP = IP + 1` (23); `            NSPA(IP) = ID(I)` (24); `          ENDDO` (25); `        ELSE` (26); `          ISPA(2) = IP` (27); `          BACKSPACE(ITI)` (28); `          RETURN` (29); `        ENDIF` (30); `      ENDDO` (32); `      END` (34). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
