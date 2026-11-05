---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/vecmid3.f
lines: 39
sha256: 899e952f8e893788647b80504c0dc3ba8a6eee442093b18e311e0b50ebe5b481
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vecmid3.f — 판독 구간 기록

구간은 1행부터 39행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | VECMID3 입구와 인덱스 표를 사용한 내적 설명·선언이다(1–9). 초기화와 단순 DO 누적식은 주석이다(11–15). 루프 펼치기의 출처와 나머지 처리 주석이다(16–21). 원문: `      SUBROUTINE VECMID3(RR,RA,RB,INDX,NSIZE)` (1); 주석: `C                          DDOT WITH INDX TABLE   ` (3); 주석: `C                                   IP=INDX(I)` (4); 주석: `C                                 RR=RA(I)*RB(IP)` (5); `      IMPLICIT REAL*8(A-H,O-Z)` (7); `      DIMENSION RA(NSIZE),RB(*)` (8); `      DIMENSION INDX(NSIZE)` (9); 주석: `C===  RR=0.0D0` (11); 주석: `C===  DO 1000 I=1,NSIZE` (12); 주석: `C===  IP=INDX(I)` (13); 주석: `C===  RR=RR+RA(I)*RB(IP)` (14); 주석: `C1000 CONTINUE` (15); 주석: `C                       + BLUS-LIKE +` (16); 주석: `c     a vector plus a vector.` (17); 주석: `c     uses unrolled loops for increments equal to one.` (18); 주석: `c     jack dongarra, linpack, 3/11/78.` (19); 주석: `c        clean-up loop` (21) |
| 23–39 | 시작 시 VECMID3 루틴(1) 안이다. 실행문 RR=0.0D0으로 시작한다(23). 나머지를 먼저 누적하고, 이후 네 항씩 인덱스 내적을 누적한다(24–36). 원문: `      RR=0.0D0` (23); `   20 m = mod(NSIZE,4)` (24); `      if( m .eq. 0 ) go to 40` (25); `      do 30 i = 1,m` (26); `       RR = RR + RA(I)*RB(INDX(I))` (27); `   30 continue` (28); `      if( NSIZE .lt. 4 ) return` (29); `   40 mp1 = m + 1` (30); `      do 50 i = mp1,NSIZE,4` (31); `       RR = RR + RA(I)*RB(INDX(I))` (32); `       RR = RR + RA(I+1)*RB(INDX(I + 1))` (33); `       RR = RR + RA(I+2)*RB(INDX(I + 2))` (34); `       RR = RR + RA(I+3)*RB(INDX(I + 3))` (35); `   50 continue` (36); `      RETURN` (38); `      END` (39) M이 0이면 25행에서 레이블 40(30행)으로 이동한다. 이 경로는 나머지 루프와 NSIZE<4의 RETURN을 건너뛴다. [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
