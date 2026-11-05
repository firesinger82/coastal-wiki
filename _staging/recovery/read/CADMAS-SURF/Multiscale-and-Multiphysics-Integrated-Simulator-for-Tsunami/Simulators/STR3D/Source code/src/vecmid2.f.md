---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/vecmid2.f
lines: 33
sha256: 9169e2173b4df8041e38554b478aea275c09b372589157519888194e9479ebad
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vecmid2.f — 판독 구간 기록

구간은 1행부터 33행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | VECMID2 입구와 선언이다(1–5). 인덱스 위치에 RA(I)*RB를 더하는 단순 DO는 주석이다(7–10). 루프 펼치기의 출처와 나머지 처리 주석이다(11–16). 원문: `      SUBROUTINE VECMID2(RR,RA,RB,INDX,NSIZE)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION RR(*),RA(NSIZE)` (4); `      DIMENSION INDX(NSIZE)` (5); 주석: `C     DO 1000 I=1,NSIZE` (7); 주석: `C     IP=INDX(I)` (8); 주석: `C     RR(IP)=RR(IP)+RA(I)*RB` (9); 주석: `C1000 CONTINUE` (10); 주석: `C                       + BLUS-LIKE +` (11); 주석: `C     A VECTOR PLUS A VECTOR.` (12); 주석: `C     USES UNROLLED LOOPS FOR INCREMENTS EQUAL TO ONE.` (13); 주석: `C     JACK DONGARRA, LINPACK, 3/11/78.` (14); 주석: `C        CLEAN-UP LOOP` (16) |
| 18–33 | 시작 시 VECMID2 루틴(1) 안이다. 나머지 항을 먼저 처리하고 NSIZE 조건으로 반환한다(18–23). 그 뒤 네 항씩 RR의 INDX 위치에 RA*RB를 더한다(24–30). 원문: `      M = MOD(NSIZE,4)` (18); `      IF( M .EQ. 0 ) GO TO 40` (19); `      DO 30 I = 1,M` (20); `       RR(INDX(I)) = RR(INDX(I)) + RA(I)*RB` (21); `   30 CONTINUE` (22); `      IF( NSIZE .LT. 4 ) RETURN` (23); `   40 MP1 = M + 1` (24); `      DO 50 I = MP1,NSIZE,4` (25); `       RR(INDX(I)) = RR(INDX(I)) + RA(I)*RB` (26); `       RR(INDX(I+1)) = RR(INDX(I+1)) + RA(I+1)*RB` (27); `       RR(INDX(I+2)) = RR(INDX(I+2)) + RA(I+2)*RB` (28); `       RR(INDX(I+3)) = RR(INDX(I+3)) + RA(I+3)*RB` (29); `   50 CONTINUE` (30); `      RETURN` (32); `      END` (33) M이 0이면 19행에서 레이블 40(24행)으로 이동한다. 이 경로는 나머지 루프와 NSIZE<4의 RETURN을 건너뛴다. [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 18–30: RR 전체를 초기화하는 실행문은 없다. 각 INDX 위치의 기존 RR에 값을 더한다.
