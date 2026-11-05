---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_dcopy.f
lines: 8
sha256: 4f7294da235d8a764171f2048d8160c68269f15a560466870b3c23cbdd44bbd0
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_dcopy.f — 판독 구간 기록

구간은 1행부터 8행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | SF_DCOPY 선언과 A(N)·B(N)의 실수 배열 범위(1–4). 배열 전체 대입으로 B를 A에 복사한다(6). 원문: `      SUBROUTINE SF_DCOPY(A,B,N)` (1)<br>`      IMPLICIT REAL*8(A-H,O-Z)` (3)<br>`      DIMENSION A(N),B(N)` (4)<br>`      A = B` (6)<br>`      END` (8) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
