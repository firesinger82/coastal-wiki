---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Read_data/Rd_SOLID.f
lines: 26
sha256: cdef1c79890ac78535e7c8ef2f52400e7224948810ce4c5daa0c8b638c64d10c
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Rd_SOLID.f — 판독 구간 기록

구간은 1행부터 26행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | RD_SOLID는 CHAR·공백 표식과 J_SOL(22)을 선언한다(1–5). IP=0에서 IS=IP+1·IE=IP+8을 계산한다(7–9). 최초 카드(card)의 정수 여덟 개를 J_SOL(IS:IE)에 읽는다(10). 원문: `      SUBROUTINE RD_SOLID( J_SOL, CHAR, ITI )` (1); `      CHARACTER*80 CHAR` (3); `      CHARACTER*8 BLK /'        '/` (4); `      DIMENSION J_SOL(22)` (5); `      IP = 0` (7); `      IS = IP + 1` (8); `      IE = IP + 8` (9); `      READ(CHAR,'(BN,8X,8I8)') J_SOL(IS:IE)` (10). |
| 12–26 | 시작 시 1행 RD_SOLID 안. 12행 무한 루프(loop)에서 레코드(record)를 읽는다(13). 14행 연속행 조건이 참이면 IP를 8 늘려 IS·IE를 계산한다(15–17). 18행 조건부 대입은 IE의 상한을 22로 제한한다. 해당 슬라이스(slice)를 읽는다(19). ELSE(20)는 BACKSPACE 후 반환한다(21–22). 원문: `      DO` (12); `        READ(ITI,'(A80)') CHAR` (13); `        IF( CHAR(1:8) == BLK .OR. CHAR(1:1) == '+' ) THEN` (14); `          IP = IP + 8` (15); `          IS = IP + 1` (16); `          IE = IP + 8` (17); `          IF( IE > 22 ) IE = 22` (18); `          READ(CHAR,'(BN,8X,8I8)') J_SOL(IS:IE)` (19); `        ELSE` (20); `          BACKSPACE(ITI)` (21); `          RETURN` (22); `        ENDIF` (23); `      ENDDO` (24); `      END` (26). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 15–19: IE는 22로 제한하지만 IS에는 상한 검사가 없다. 연속행 판독을 끝내는 별도 개수 조건은 없다.
