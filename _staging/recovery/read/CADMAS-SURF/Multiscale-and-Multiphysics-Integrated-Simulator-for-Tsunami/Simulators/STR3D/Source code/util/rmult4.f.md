---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/util/rmult4.f
lines: 42
sha256: bbbb477a3cb6d502dd6a2ba8aa35b1fd80e9bc846d4c8170261299398434e301
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# rmult4.f — 판독 구간 기록

구간은 1행부터 42행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–26 | RMULT4는 A=B+R*C의 입력·출력을 설명한다(1–13). 암시적 형(implicit typing)과 A(*)·B(*)·C(*)를 선언한다(14–15). 17–19행의 DO·대입·CONTINUE는 C로 시작하는 주석 처리된 코드이다. 이후 주석은 루프 펼치기(loop unrolling), JACK DONGARRA·LINPACK·3/11/78과 나머지 처리 루프를 적는다(20–26). 원문: `      SUBROUTINE RMULT4(A,B,R,C,N)` (1); `C       SUB FOR MULTIPLY VECTOR      A=B+R*C` (3); `C       INPUT` (5); `C       R       SCOLAR TO BE MULTIPLIED` (6); `C       N       ORDER OF A` (7); `C       B       VECTOR TO BE MULTIPLIED` (8); `C       C       VECTOR TO BE MULTIPLIED` (9); `C       OUTPUT` (11); `C       A       OUTPUT VECTOR` (12); `      IMPLICIT REAL*8(A-H,O-Z)` (14); `      DIMENSION A(*),B(*),C(*)` (15); `C                               ** MATRIX POINTER **` (16); `C===  DO 8000 I=1,N` (17); `C===  A(I)=B(I)+R*C(I)` (18); `C8000 CONTINUE` (19); `C                       + BLUS-LIKE +` (20); `C     A VECTOR PLUS A VECTOR.` (21); `C     USES UNROLLED LOOPS FOR INCREMENTS EQUAL TO ONE.` (22); `C     JACK DONGARRA, LINPACK, 3/11/78.` (23); `C        CLEAN-UP LOOP` (25). |
| 27–42 | 시작 시 1행 RMULT4 루틴 안. M=MOD(N,4)로 나머지를 계산한다(27). M=0이면 표지 40으로 이동한다(28). 나머지는 I=1..M에서 처리하고 N<4이면 반환한다(29–32). MP1=M+1 뒤 I=MP1..N을 간격 4로 순회하며 연속 네 성분을 계산한다(33–39). 주석·RETURN·END를 포함한다. 원문: `   20 M = MOD(N,4)` (27); `      IF( M .EQ. 0 ) GO TO 40` (28); `      DO 30 I = 1,M` (29); `        A(I) = B(I) + R*C(I)` (30); `   30 CONTINUE` (31); `      IF( N .LT. 4 ) RETURN` (32); `   40 MP1 = M + 1` (33); `      DO 50 I = MP1,N,4` (34); `        A(I) = B(I) + R*C(I)` (35); `        A(I + 1) = B(I + 1) + R*C(I + 1)` (36); `        A(I + 2) = B(I + 2) + R*C(I + 2)` (37); `        A(I + 3) = B(I + 3) + R*C(I + 3)` (38); `   50 CONTINUE` (39); `      RETURN` (41); `      END` (42). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 27–38: 나머지 계산과 펼친 루프의 간격 및 한 번에 계산하는 성분 수는 4로 고정되어 있다.
