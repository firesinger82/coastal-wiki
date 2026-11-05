---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_cross2.f
lines: 18
sha256: 3df9e389bd6213ba6c977306625e544951a49c9188d155dafb3218b70343a30a
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_cross2.f — 판독 구간 기록

구간은 1행부터 18행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | SF_CROSS2 선언과 A(3)·B(3)·C(3) 배열 범위(1–7). 외적(cross product)을 길이로 나눈 단위 벡터(unit vector) C를 만든다(9–16). 5행 주석도 원문으로 인용한다. 원문: `      SUBROUTINE SF_CROSS2(A,B,C)` (1)<br>`      IMPLICIT REAL*8(A-H,O-Z)` (3)<br>`C     C=A*B/\|A*B\|` (5)<br>`      DIMENSION A(3),B(3),C(3)` (7)<br>`      X = A(2) * B(3) - A(3) * B(2)` (9)<br>`      Y = A(3) * B(1) - A(1) * B(3)` (10)<br>`      Z = A(1) * B(2) - A(2) * B(1)` (11)<br>`      XLN =DSQRT(X*X+Y*Y+Z*Z)` (12)<br>`      XLN = 1.0 /XLN` (13)<br>`      C(1) = X * XLN` (14)<br>`      C(2) = Y * XLN` (15)<br>`      C(3) = Z * XLN` (16)<br>`      RETURN` (17)<br>`      END` (18) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 12–16: 외적의 길이 XLN에 대한 0 검사 없이 1.0/XLN을 계산한다.
