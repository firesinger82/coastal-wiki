---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/util/harfb.f
lines: 44
sha256: 92d2e4ad7523123a6b289455aea2f3aa29f82379cc05f920d09c303aad265c43
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# harfb.f — 판독 구간 기록

구간은 1행부터 44행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | HARFB는 압축 저장(packed storage) B를 포함한 A=B*C를 설명한다(2–13). 암시적 형과 A(N1,N3)·B(1)·C(N2,N3)를 선언한다(14–15). IR=N2, LAST=0을 설정한다(19–20). 원문: `      SUBROUTINE  HARFB( A,B,C, N1,N2,N3 )` (2); `C  A = B X C  ( B MATRIX IS HARF MATRIX )` (4); `C  A      = A MATRIX   ( N1 X N3 )                        --- ( O )` (6); `C  B      = B MATRIX   ( ONE DIMENSION )                  --- ( I )` (7); `C  C      = C MATRIX   ( N2 X N3 )                        --- ( I )` (8); `C  N1     = NUMBER OF COLUMN                              --- ( I )` (9); `C  N2     = NUMBER OF COLUMN,ROWS                         --- ( I )` (10); `C  N1     = NUMBER OF ROWS                                --- ( I )` (11); `      IMPLICIT REAL*8 (A-H,O-Z)` (14); `      DIMENSION  A(N1,N3),B(1),C(N2,N3)` (15); `C--- CALCULATE MATRIX ---` (18); `      IR   = N2` (19); `      LAST = 0` (20). |
| 21–44 | 시작 시 2행 HARFB 루틴 안. I=1..N1와 J=1..N3마다 IC와 A(I,J)를 0으로 둔다(21–24). K=1..N2에서 I<=K 분기는 LAST로 IAD를 계산한다(26–28). ELSE 분기는 IC로 IAD를 계산하고 IC에 N2-K를 더한다(29–32). B(IAD)*C(K,J)를 누적한다(34). J 루프 뒤 LAST·IR을 갱신한다(38–39). 모든 루프 종료·주석·RETURN·END를 포함한다. 원문: `      DO 3000 I=1,N1` (21); `      DO 2000 J=1,N3` (22); `         IC     = 0` (23); `         A(I,J) = 0.0D0` (24); `         DO 1000 K=1,N2` (26); `            IF( I .LE. K )  THEN` (27); `                IAD = LAST + K - I + 1` (28); `             ELSE` (29); `                IAD = I  + IC` (30); `                IC  = IC + N2 - K` (31); `            ENDIF` (32); `            A(I,J) = A(I,J) + B(IAD)*C(K,J)` (34); ` 1000    CONTINUE` (36); ` 2000 CONTINUE` (37); `         LAST = LAST + IR` (38); `         IR   = IR - 1` (39); ` 3000 CONTINUE` (40); `      RETURN` (43); `      END` (44). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11: 행 수 설명의 인수 이름은 N1로 쓰였으며, 루틴 인수에는 별도로 N3가 있다(2).
- 15·28–34: B의 선언은 B(1)이며, 실제 접근 첨자는 계산된 IAD이다.
