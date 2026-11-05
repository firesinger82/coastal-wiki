---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Read_data/Rd_TSTEPNL.f
lines: 30
sha256: 6dae2ef955d84aa648bc26c25a8769d83e6159be4854834c016e8112679c18a4
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Rd_TSTEPNL.f — 판독 구간 기록

구간은 1행부터 30행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–30 | RD_TSTEPNL의 IMPLICIT·NLP(4)·RNLP(2)을 선언하고 ID·NDT·DT·NO·MAXITER를 읽는다(1–8). 10·11행 조건부 기본값 식은 NO=0을 1, MAXITER=0을 10으로 바꾼다. 다음 레코드(record)를 읽고(13) 15행 연속행 조건을 검사한다. 참이면 EPSP를 읽고 0을 1.D-3으로 바꾼다(16–17). ELSE(18)는 BACKSPACE 후 EPSP=1.D-3을 설정한다(19–20). NLP에는 ID·NDT·MAXITER·NO를, RNLP에는 EPSP·DT를 저장한다(23–28). 원문: `      SUBROUTINE RD_TSTEPNL( NLP, RNLP, CHAR, ITI )` (1); `      IMPLICIT REAL*8 (A-H,O-Z)` (3); `      CHARACTER*80 CHAR` (4); `      CHARACTER*8 BLK /'        '/` (5); `      DIMENSION NLP(4), RNLP(2)` (6); `      READ(CHAR,'(BN,8X,2I8,F8.0,I8,16X,I8)') ID, NDT, DT, NO, MAXITER` (8); `      IF( NO == 0 ) NO = 1` (10); `      IF( MAXITER == 0 ) MAXITER = 10` (11); `      READ(ITI,'(A80)') CHAR` (13); `      IF( CHAR(1:8) == BLK .OR. CHAR(1:1) == '+' ) THEN` (15); `        READ(CHAR,'(BN,16X,F8.0)') EPSP` (16); `        IF( EPSP == 0. ) EPSP = 1.D-3` (17); `      ELSE` (18); `        BACKSPACE(ITI)` (19); `        EPSP = 1.D-3` (20); `      ENDIF` (21); `      NLP(1) = ID` (23); `      NLP(2) = NDT` (24); `      NLP(3) = MAXITER` (25); `      NLP(4) = NO` (26); `      RNLP(1) = EPSP` (27); `      RNLP(2) = DT` (28); `      END` (30). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
