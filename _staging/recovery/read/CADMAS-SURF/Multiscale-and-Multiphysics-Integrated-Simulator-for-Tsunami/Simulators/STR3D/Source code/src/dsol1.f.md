---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/dsol1.f
lines: 32
sha256: 0fc03c25be5c573864fd12ff744adfb2a6223f784af6a7132699bda1ee544163
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# dsol1.f — 판독 구간 기록

구간은 1행부터 32행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | DSOL1의 주석은 균열 고체요소(cracked solid element)의 구성행렬(constitutive matrix)을 설명한다. D는 길이 21의 상삼각(upper triangle) 저장 배열이다. E는 영률(Young's modulus), ANU는 푸아송비(Poisson's ratio)다. 암시적 형과 D의 크기를 선언한다. 원문: 주석 원문 `C***********************************************************************` (1); `      SUBROUTINE  DSOL1( D,E,ANU )` (2); 주석 원문 `C***********************************************************************` (3); 주석 원문 `C  MAKE D-MATRIX OF CRACKED SOLID ELEMENT` (4); 주석 원문 `C  D      = D-MATRIX     1   2   3   4   5   6            --- ( O )` (6); 주석 원문 `C                            7   8   9  10  11` (7); 주석 원문 `C                               12  13  14  15` (8); 주석 원문 `C                                   16  17  18` (9); 주석 원문 `C                                       19  20` (10); 주석 원문 `C                                           21` (11); 주석 원문 `C  E      = YOUNG'S MODULUS                               --- ( I )` (12); 주석 원문 `C  ANU    = POISSON RATIO                                 --- ( I )` (13); 주석 원문 `C-----------------------------------------------------------------------` (15); `      IMPLICIT REAL*8 (A-H,O-Z)` (16); `      DIMENSION  D(21)` (17). |
| 19–32 | 시작 시 2행 DSOL1 루틴 안. E·ANU로 A와 전단계수(shear modulus) G를 계산한다. D 전체를 0으로 초기화하고 지정된 일곱 위치에 E·A·G의 배수를 둔다. 루틴 끝을 포함한다. 원문: `      A = E / ( 1.D0 - ANU*ANU )` (19); `      G = .5D0 * E / ( 1.D0 + ANU )` (20); `      D(:) = 0.` (22); `      D( 1) = E * 1.D-4` (24); `      D( 7) = A` (25); `      D( 8) = A * ANU` (26); `      D(12) = A` (27); `      D(16) = G * .25D0` (28); `      D(19) = G` (29); `      D(21) = G * .25D0` (30); `      END` (32). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 24·28·30: D(1)의 계수 1.D-4와 D(16)·D(21)의 계수 .25D0는 상수로 고정되어 있다.
