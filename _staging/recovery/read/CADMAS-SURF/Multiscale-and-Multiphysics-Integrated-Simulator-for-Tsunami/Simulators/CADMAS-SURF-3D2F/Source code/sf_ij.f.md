---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_ij.f
lines: 11
sha256: 2c08220e7e65f3de86be6d84e6ceaf3137bc14ae4406f54cf52d0ca47326fc67
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_ij.f — 판독 구간 기록

구간은 1행부터 11행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | SF_IJ 선언과 INCLUDE 두 개(1–6). NUMI를 이용한 정수 나눗셈(integer division)으로 선형 번호 IJ를 J·I 좌표로 변환한다(8–9). 원문: `      SUBROUTINE SF_IJ(I,J,IJ)` (1)<br>`      IMPLICIT REAL*8(A-H,O-Z)` (3)<br>`      INCLUDE 'VF_A0PRM.h'` (5)<br>`      INCLUDE 'VF_ANUMBI.h'` (6)<br>`      J  =(IJ-1)/NUMI+1` (8)<br>`      I  =IJ-NUMI*(J-1)` (9)<br>`      END` (11) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
