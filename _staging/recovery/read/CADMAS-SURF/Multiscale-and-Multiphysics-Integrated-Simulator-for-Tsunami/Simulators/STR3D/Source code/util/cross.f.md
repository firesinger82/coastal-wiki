---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/util/cross.f
lines: 14
sha256: 9192aa3dfa65300e59b724123969f002ca30f125b653b088b5104690325bde19
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# cross.f — 판독 구간 기록

구간은 1행부터 14행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | CROSS의 인수와 암시적 형, 세 성분의 A·B·C를 선언한다(1–7). 세 성분의 외적(cross product)을 C(1:3)에 계산한다(9–11). 주석·RETURN·END까지 포함한다. 원문: `      SUBROUTINE CROSS (A,B,C)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `C     C=A*B` (5); `      DIMENSION A(3),B(3),C(3)` (7); `      C(1) = A(2) * B(3) - A(3) * B(2)` (9); `      C(2) = A(3) * B(1) - A(1) * B(3)` (10); `      C(3) = A(1) * B(2) - A(2) * B(1)` (11); `      RETURN` (13); `      END` (14). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
