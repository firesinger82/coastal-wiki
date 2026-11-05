---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/vecmid.f
lines: 37
sha256: 614f214578a8e9cd87ab540f056df913439081368a406cae687f004d49bad654
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vecmid.f — 판독 구간 기록

구간은 1행부터 37행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–21 | VECMID 입구와 인덱스 표를 사용한 내적(dot product) 설명·선언이다(1–9). 단순 DO 누적식은 주석 처리되어 있다(11–14). 루프 펼치기(loop unrolling)의 출처와 나머지 처리 주석이다(15–20). 원문: `      SUBROUTINE VECMID(RR,RA,RB,INDX,NSIZE)` (1); 주석: `C                          DDOT WITH INDX TABLE   ` (3); 주석: `C                                   IP=INDX(I)` (4); 주석: `C                                 RR=RA(I)*RB(IP)` (5); `      IMPLICIT REAL*8(A-H,O-Z)` (7); `      DIMENSION RA(NSIZE),RB(*)` (8); `      DIMENSION INDX(NSIZE)` (9); 주석: `C===  DO 1000 I=1,NSIZE` (11); 주석: `C===  IP=INDX(I)` (12); 주석: `C===  RR=RR+RA(I)*RB(IP)` (13); 주석: `C1000 CONTINUE` (14); 주석: `C                       + BLUS-LIKE +` (15); 주석: `C     A VECTOR PLUS A VECTOR.` (16); 주석: `C     USES UNROLLED LOOPS FOR INCREMENTS EQUAL TO ONE.` (17); 주석: `C     JACK DONGARRA, LINPACK, 3/11/78.` (18); 주석: `C        CLEAN-UP LOOP` (20) |
| 22–37 | 시작 시 VECMID 루틴(1) 안이다. MOD(NSIZE,4)개의 나머지를 먼저 누적하고 필요하면 반환한다(22–27). 나머지 구간은 네 항씩 RR에 누적한다(28–34). 원문: `   20 M = MOD(NSIZE,4)` (22); `      IF( M .EQ. 0 ) GO TO 40` (23); `      DO 30 I = 1,M` (24); `       RR = RR + RA(I)*RB(INDX(I))` (25); `   30 CONTINUE` (26); `      IF( NSIZE .LT. 4 ) RETURN` (27); `   40 MP1 = M + 1` (28); `      DO 50 I = MP1,NSIZE,4` (29); `       RR = RR + RA(I)*RB(INDX(I))` (30); `       RR = RR + RA(I+1)*RB(INDX(I + 1))` (31); `       RR = RR + RA(I+2)*RB(INDX(I + 2))` (32); `       RR = RR + RA(I+3)*RB(INDX(I + 3))` (33); `   50 CONTINUE` (34); `      RETURN` (36); `      END` (37) M이 0이면 23행에서 레이블 40(28행)으로 이동한다. 이 경로는 나머지 루프와 NSIZE<4의 RETURN을 건너뛴다. [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 22–34: RR을 0으로 초기화하는 실행문은 없다. 입력 RR에 내적을 더한다.
