---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Read_data/Rd_BCTSET.f
lines: 30
sha256: b66cd94fee9780a3e7b98dd0091631e2e635701a98a31fbc13b617ff6a5db9f9
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Rd_BCTSET.f — 판독 구간 기록

구간은 1행부터 30행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | RD_BCTSET 선언과 암시적 형식(implicit typing), ID(2)·J_BCTS(3,*) 배열 선언을 포함한다(1–6). 첫 카드(card)에서 IDS와 ID 두 값을 읽는다(8). IP를 증가시키고 IDS 및 두 ID를 J_BCTS의 새 열에 저장한다(10–12). 원문: `      SUBROUTINE RD_BCTSET( J_BCTS, IP, CHAR, ITI )` (1); `      IMPLICIT REAL*8 (A-H,O-Z)` (3); `      CHARACTER*80 CHAR` (4); `      CHARACTER*8 BLK /'        '/` (5); `      DIMENSION ID(2), J_BCTS(3,*)` (6); `      READ(CHAR,'(BN,8X,3I8)') IDS, ID(:)` (8); `      IP = IP + 1` (10); `      J_BCTS(1,IP) = IDS` (11); `      J_BCTS(2:3,IP) = ID(:)` (12). |
| 14–30 | 시작 시 1행 RD_BCTSET 안. 14행 무한 루프(loop)에서 다음 레코드(record)를 읽고 18행 조건으로 연속행을 판별한다. 연속행은 16열을 건너 두 ID를 읽어 동일 IDS로 저장한다(19–22). ELSE(23)는 BACKSPACE 후 반환한다(24–25). 루프 종료·주석·END를 포함한다(26–30). 원문: `      DO` (14); `        READ(ITI,'(A80)') CHAR` (16); `        IF( CHAR(1:8) == BLK .OR. CHAR(1:1) == '+' ) THEN` (18); `          READ(CHAR,'(BN,16X,2I8)') ID(:)` (19); `          IP = IP + 1` (20); `          J_BCTS(1,IP) = IDS` (21); `          J_BCTS(2:3,IP) = ID(:)` (22); `        ELSE` (23); `          BACKSPACE(ITI)` (24); `          RETURN` (25); `        ENDIF` (26); `      ENDDO` (28); `      END` (30). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 14–28: 연속행 READ에는 END·ERR·IOSTAT 지정이 없다.
