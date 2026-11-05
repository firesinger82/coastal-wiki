---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/util/harfta.f
lines: 33
sha256: bc77b8a46921dd3a667fa24c8bc43bebd0819f8f899dedf3d91c6ccbc33075b1
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# harfta.f — 판독 구간 기록

구간은 1행부터 33행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | HARFTA는 A=B의 전치(transpose) 곱하기 C를 계산하여 압축 저장(packed storage)한다는 주석을 갖는다(2–13). 암시적 형과 A(1)·B(N1,N2)·C(N1,N2)를 선언한다(14–15). IC를 0으로 둔다(19). 원문: `      SUBROUTINE  HARFTA( A,B,C, N1,N2 )` (2); `C  A = BT X C  ( A MATRIX IS HARF MATRIX )` (4); `C  A      = A MATRIX   ( ONE DIMENSION )                  --- ( O )` (6); `C  B      = B MATRIX   ( N1 X N2 )                        --- ( I )` (7); `C  C      = C MATRIX   ( N1 X N2 )                        --- ( I )` (8); `C  N1     = NUMBER OF COLUMN                              --- ( I )` (9); `C  N2     = NUMBER OF COLUMN,ROWS                         --- ( I )` (10); `C  N1     = NUMBER OF ROWS                                --- ( I )` (11); `      IMPLICIT REAL*8 (A-H,O-Z)` (14); `      DIMENSION  A(1),B(N1,N2),C(N1,N2)` (15); `C--- CALCULATE MATRIX ---` (18); `      IC = 0` (19). |
| 20–33 | 시작 시 2행 HARFTA 루틴 안. I=1..N2, J=I..N2마다 IC를 증가시키고 A(IC)를 0으로 둔다(20–23). K=1..N1에서 B(K,I)*C(K,J)를 누적한다(25–27). 루프 종료·주석·RETURN·END를 포함한다. 원문: `      DO 3000 I=1,N2` (20); `      DO 2000 J=I,N2` (21); `         IC    = IC + 1` (22); `         A(IC) = 0.0D0` (23); `         DO 1000 K=1,N1` (25); `            A(IC) = A(IC) + B(K,I)*C(K,J)` (26); ` 1000    CONTINUE` (27); ` 2000 CONTINUE` (28); ` 3000 CONTINUE` (29); `      RETURN` (32); `      END` (33). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11: 행 수 설명의 인수 이름은 N1로 쓰였다.
- 15·22–26: A의 선언은 A(1)이며, 실제 접근 첨자는 누적하는 IC이다.
