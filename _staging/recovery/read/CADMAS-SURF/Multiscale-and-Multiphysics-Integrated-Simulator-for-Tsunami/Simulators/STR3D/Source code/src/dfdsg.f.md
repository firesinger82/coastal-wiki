---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/dfdsg.f
lines: 33
sha256: 0ff3463d2fa4810243da1db20f7ced9557ae57abdad7a8c90c6d277870ef6cfb
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# dfdsg.f — 판독 구간 기록

구간은 1행부터 33행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | DFDSG의 암시적 형(implicit typing)과 길이 6인 DFDS·S를 선언한다. 주석은 von Mises 항복(yield) 부분을 가리키며 원문 철자는 `von Mieses`다. 원문: `      SUBROUTINE DFDSG(DFDS,S,IYLD,ALP)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION DFDS(6),S(6)` (4); 주석 원문 `C-----------------------------------------------------------------------` (5); 주석 원문 `C     ----- von Mieses -----` (7). |
| 9–24 | 시작 시 1행 DFDSG 루틴 안. S(1:3)의 차이 제곱과 S(4:6)의 제곱으로 VMEQ를 구한다. VMEQ의 제곱근을 √2로 나눈다. 여섯 DFDS 성분을 VMEQ로 나누어 계산한다. 해석: S를 응력 성분으로 보면 VMEQ는 von Mises 등가응력이며 DFDS는 그 미분이다. IYLD가 1이면 반환한다. 원문: `      VMEQ =   ( S(1) - S(2) )*( S(1) - S(2) ) `<br>`     &       + ( S(2) - S(3) )*( S(2) - S(3) )`<br>`     &       + ( S(3) - S(1) )*( S(3) - S(1) ) `<br>`     &       + 6.D0*( S(4)*S(4) + S(5)*S(5) + S(6)*S(6) )` (9–12); `      VMEQ = DSQRT(VMEQ)/DSQRT(2.D0)` (14); `      DFDS(1) = ( S(1) - .5D0*S(2) - .5D0*S(3) ) / VMEQ` (16); `      DFDS(2) = ( S(2) - .5D0*S(3) - .5D0*S(1) ) / VMEQ` (17); `      DFDS(3) = ( S(3) - .5D0*S(1) - .5D0*S(2) ) / VMEQ` (18); `      DFDS(4) = 3.D0*S(4) / VMEQ` (19); `      DFDS(5) = 3.D0*S(5) / VMEQ` (20); `      DFDS(6) = 3.D0*S(6) / VMEQ` (21); `      IF( IYLD == 1 ) RETURN` (23). [11-04 전수 검증 정정] |
| 25–33 | 시작 시 1행 DFDSG 루틴 안. 23행에서 반환하지 않은 경우 Drucker–Prager 계수를 A·B로 계산한다. 처음 3개 성분에는 ALP를 더한 변환을 적용하고 나머지 3개에는 A*B를 곱한다. 루틴 끝을 포함한다. 원문: 주석 원문 `C     ----- Drucker-Prager -----` (25); `      A = 1.D0 / ( 1.D0/DSQRT(3.D0) - ALP )` (27); `      B = 1.D0 / DSQRT(3.D0)` (28); `      DFDS(1:3) = A*( ALP + B*DFDS(1:3) )` (30); `      DFDS(4:6) = A*B*DFDS(4:6)` (31); `      END` (33). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 14–21: VMEQ로 나누기 전 VMEQ=0을 확인하는 조건문은 없다.
- 23·25–31: IYLD=1 이외의 모든 값은 Drucker–Prager 계산으로 진행한다.
