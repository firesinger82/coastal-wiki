---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/util/cross2.f
lines: 18
sha256: 04c794ed16770f919dd4444563cd64790465932c9df725760b39d7fae3c6d546
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# cross2.f — 판독 구간 기록

구간은 1행부터 18행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | CROSS2는 외적(cross product)을 그 크기로 나눈다는 주석을 갖는다(1–7). X·Y·Z를 계산하고 크기의 역수를 XLN에 대입한다(9–13). C(1:3)에 역수를 곱한 성분을 대입한다(14–16). RETURN·END까지 포함한다. 원문: `      SUBROUTINE CROSS2 (A,B,C)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `C     C=A*B/\|A*B\|` (5); `      DIMENSION A(3),B(3),C(3)` (7); `      X = A(2) * B(3) - A(3) * B(2)` (9); `      Y = A(3) * B(1) - A(1) * B(3)` (10); `      Z = A(1) * B(2) - A(2) * B(1)` (11); `      XLN =DSQRT(X*X+Y*Y+Z*Z)` (12); `      XLN = 1.0 /XLN` (13); `      C(1) = X * XLN` (14); `      C(2) = Y * XLN` (15); `      C(3) = Z * XLN` (16); `      RETURN` (17); `      END` (18). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 12–16: XLN의 역수를 취하기 전에 XLN이 0인지 검사하는 문장은 없다.
