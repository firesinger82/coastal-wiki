---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/util/cross1.f
lines: 14
sha256: 114fa6a4729137b9565f4c998aa06d25fc6832db052739c9929d61426f5556ae
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# cross1.f — 판독 구간 기록

구간은 1행부터 14행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | CROSS1의 인수와 암시적 형, A(3)·B(3)를 선언한다(1–6). 외적(cross product)의 성분 X·Y·Z를 구하고 그 유클리드 노름(Euclidean norm)을 S에 계산한다(8–11). RETURN·END와 마지막 빈 줄(14)을 포함한다. 원문: `      SUBROUTINE CROSS1 (A,B,S)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION A(3),B(3)` (6); `      X = A(2) * B(3) - A(3) * B(2)` (8); `      Y = A(3) * B(1) - A(1) * B(3)` (9); `      Z = A(1) * B(2) - A(2) * B(1)` (10); `      S =DSQRT(X*X+Y*Y+Z*Z)` (11); `      RETURN` (12); `      END` (13). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
