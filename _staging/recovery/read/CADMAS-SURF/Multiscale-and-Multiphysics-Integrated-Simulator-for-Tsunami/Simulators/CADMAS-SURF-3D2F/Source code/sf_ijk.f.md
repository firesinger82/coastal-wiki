---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_ijk.f
lines: 13
sha256: bd48ee6e317c56b8bc0ea002895980346224a3dbfebe112b19ac926e56808b09
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_ijk.f — 판독 구간 기록

구간은 1행부터 13행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | SF_IJK 선언과 INCLUDE 두 개(1–6). `K  =(IJK-1)/(NUMI*NUMJ)+1`로 K를 구한다(8). `IJK=IJK-NUMI*NUMJ*(K-1)`로 인수 IJK를 갱신한다(9). 갱신된 IJK로 `J  =(IJK-1)/NUMI+1`과 `I  =IJK-NUMI*(J-1)`을 차례로 계산한다(10–11). 원문: `      SUBROUTINE SF_IJK(I,J,K,IJK)` (1)<br>`      IMPLICIT REAL*8(A-H,O-Z)` (3)<br>`      INCLUDE 'VF_A0PRM.h'` (5)<br>`      INCLUDE 'VF_ANUMBI.h'` (6)<br>`      K  =(IJK-1)/(NUMI*NUMJ)+1` (8)<br>`      IJK=IJK-NUMI*NUMJ*(K-1)` (9)<br>`      J  =(IJK-1)/NUMI+1` (10)<br>`      I  =IJK-NUMI*(J-1)` (11)<br>`      END` (13) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 9: 입력 인수 IJK에 대입하여 원래 3차원 선형 번호를 층 내부의 2차원 번호로 바꾼다.
