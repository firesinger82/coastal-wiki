---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/geo/velte2.f
lines: 16
sha256: 8eb6ccca71484b580b180fa3110ae411c9632f3186f83b3405d858f07e8db425
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# velte2.f — 판독 구간 기록

구간은 1행부터 16행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | VELTE2는 VELG(3,5)에서 VEL(3,10)을 계산한다. 실수 IMPLICIT·배열 선언과 대응 표 DATA II를 아래에 그대로 적었다. I=1,4에서 VELG(:,I)의 3배에서 VELG(:,5)의 2배를 뺀다. 해석: 루틴 이름과 대응 표는 10절점 사면체(tetrahedron)의 적분점 값을 절점으로 외삽(extrapolation)하는 용도로 보인다. VELG(:,5)를 중심값으로 쓰는 근거는 `geo/gnpfte2.f:51–53`이다. 원문: `      SUBROUTINE VELTE2(VEL,VELG)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION VEL(3,10),VELG(3,5),II(2,10)` (4); `      DATA II / 8*0,  1,2,  2,3,  3,1,  1,4,  2,4,  3,4 /` (5); `      DO I = 1, 4` (7); `        VEL(:,I) = 3.D0 * VELG(:,I) - 2.D0 * VELG(:,5)` (8); `      ENDDO` (9) [11-04 전수 검증 정정] |
| 11–16 | I=5,10에서 VELG(:,II(1,I))와 VELG(:,II(2,I))의 합에 1.5D0을 곱하고 VELG(:,5)의 2배를 뺀다. 해석: I=5,10은 중간 절점에 해당하는 것으로 보인다. 12–13행은 한 대입 연속문이다. 원문: `      DO I = 5, 10` (11); `        VEL(:,I) = 1.5D0 * ( VELG(:,II(1,I)) + VELG(:,II(2,I)) )` (12); `     &           - 2.D0 * VELG(:,5)` (13); `      ENDDO` (14); `      END` (16) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
