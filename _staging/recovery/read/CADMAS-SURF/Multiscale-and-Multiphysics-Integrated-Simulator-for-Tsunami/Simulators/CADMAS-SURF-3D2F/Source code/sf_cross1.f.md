---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_cross1.f
lines: 14
sha256: aae507664ad73216447bfb9a0c8c284a1a160ccefac493f1050fbc184a681c3d
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_cross1.f — 판독 구간 기록

구간은 1행부터 14행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | SF_CROSS1의 A(3)·B(3) 선언과 빈 주석을 포함한다(1–7). 외적(cross product)의 세 성분을 계산하고 그 유클리드 노름(Euclidean norm)을 S에 반환한다(8–12). 원문: `      SUBROUTINE SF_CROSS1 (A,B,S)` (1)<br>`      IMPLICIT REAL*8(A-H,O-Z)` (3)<br>`      DIMENSION A(3),B(3)` (6)<br>`      X = A(2) * B(3) - A(3) * B(2)` (8)<br>`      Y = A(3) * B(1) - A(1) * B(3)` (9)<br>`      Z = A(1) * B(2) - A(2) * B(1)` (10)<br>`      S =DSQRT(X*X+Y*Y+Z*Z)` (11)<br>`      RETURN` (12)<br>`      END` (13) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
