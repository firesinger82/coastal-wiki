---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Read_data/Rd_NLPARM.f
lines: 37
sha256: bd4ce9561d3ac4ecd422a7f35f3a78ded8134ae226e3fef2d6dcc4efb32822bc
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Rd_NLPARM.f — 판독 구간 기록

구간은 1행부터 37행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | RD_NLPARM의 IMPLICIT·NLP(4)·RNLP(2)를 선언한다(1–6). ID·NINC·MAXITER를 읽고(8), 10·11행 조건부 기본값 식으로 0 입력을 각각 10·25로 대체한다. INTOUT의 초기값은 NINC이다(13). 14행 루프(loop)가 15행 YES 조건을 만족하면 INTOUT=1로 바꾸고 EXIT한다(16–17). 원문: `      SUBROUTINE RD_NLPARM( NLP, RNLP, CHAR, ITI )` (1); `      IMPLICIT REAL*8 (A-H,O-Z)` (3); `      CHARACTER*80 CHAR` (4); `      CHARACTER*8 BLK /'        '/` (5); `      DIMENSION NLP(4), RNLP(2)` (6); `      READ(CHAR,'(BN,8X,2I8,24X,I8)') ID, NINC, MAXITER` (8); `      IF( NINC == 0 ) NINC = 10` (10); `      IF( MAXITER == 0 ) MAXITER = 25` (11); `      INTOUT = NINC` (13); `      DO I = 65, 72` (14); `        IF( CHAR(I:I+2) == 'YES' ) THEN` (15); `          INTOUT = 1` (16); `          EXIT` (17); `        ENDIF          ` (18); `      ENDDO` (19). |
| 21–37 | 시작 시 1행 RD_NLPARM 안. 다음 레코드(record)를 읽고(21) 23행 연속행 조건으로 분기한다. 연속행은 EPSP를 읽고 0이면 1.D-3으로 대체한다(24–25). ELSE(26)는 BACKSPACE 후 EPSP=1.D-3을 설정한다(27–28). ID·NINC·MAXITER·INTOUT를 NLP에, EPSP를 RNLP(1)에 저장한다(31–35). 원문: `      READ(ITI,'(A80)') CHAR` (21); `      IF( CHAR(1:8) == BLK .OR. CHAR(1:1) == '+' ) THEN` (23); `        READ(CHAR,'(BN,16X,F8.0)') EPSP` (24); `        IF( EPSP == 0. ) EPSP = 1.D-3` (25); `      ELSE` (26); `        BACKSPACE(ITI)` (27); `        EPSP = 1.D-3` (28); `      ENDIF` (29); `      NLP(1) = ID` (31); `      NLP(2) = NINC` (32); `      NLP(3) = MAXITER` (33); `      NLP(4) = INTOUT` (34); `      RNLP(1) = EPSP` (35); `      END` (37). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6·35: RNLP는 길이 2로 선언하지만 이 루틴은 RNLP(1)만 대입한다.
- 14–15: YES 검색의 시작 위치는 65–72이다. 부분문자열의 끝 위치는 I+2이므로 74열까지 검사한다.
