---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Read_data/Rd_GRID.f
lines: 19
sha256: dad383e0b400f54d8cad2e25dd99b136b39df6120fbb5b957485a46bfb7e9b26
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Rd_GRID.f — 판독 구간 기록

구간은 1행부터 19행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | RD_GRID의 인수 선언은 고정형식(fixed form) 연속문이다(1–2). IMPLICIT와 GRID(3)·INDGR(*)를 선언한다(4–6). 8행 조건이 참이면 8열 형식으로 읽는다(9). ELSE(10)는 16열 형식의 두 레코드(record)로 읽는다(11–12). 분기 종료 후 IGCD를 0으로 대입하고 INDGR(INDG)에 I_GRID를 등록한다(15–17). 원문: `      SUBROUTINE RD_GRID( INDG, IGCD, GRID, INDGR, I_GRID, CHAR, ITI,` / `     &                    ISTR )` (1–2; 하나의 고정형식 연속문); `      IMPLICIT REAL*8 (A-H,O-Z)` (4); `      CHARACTER*80 CHAR` (5); `      DIMENSION GRID(3), INDGR(*)` (6); `      IF( ISTR == 0 ) THEN` (8); `        READ(CHAR,'(BN,8X,I8,8X,3F8.0,I8)') INDG, GRID(:), IGCD` (9); `      ELSE` (10); `        READ(CHAR,'(BN,8X,I16,16X,2F16.0)') INDG, GRID(1:2)` (11); `        READ(ITI,'(BN,8X,F16.0,I16)') GRID(3), IGCD` (12); `      ENDIF` (13); `      IGCD = 0` (15); `      INDGR(INDG) = I_GRID` (17); `      END` (19). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 9·12·15: 두 형식 모두 IGCD를 입력에서 읽지만 분기 종료 후 IGCD=0으로 덮어쓴다.
