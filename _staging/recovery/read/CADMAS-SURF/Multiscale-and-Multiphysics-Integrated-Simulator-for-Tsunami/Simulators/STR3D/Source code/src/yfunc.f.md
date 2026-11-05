---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/yfunc.f
lines: 22
sha256: 27af2bfce600f71895849aa8d34c0393176eb3f7403e4bd5edca13901e097308
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# yfunc.f — 판독 구간 기록

구간은 1행부터 22행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | YFUNC 루틴의 인수는 F·S·IYLD·ALP이다(1). 암시적 형(implicit typing), J1·J2D의 배정밀도와 6성분 S 배열을 선언한다(3–5). 원문: `      SUBROUTINE YFUNC(F,S,IYLD,ALP)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      REAL*8 J1,J2D` (4); `      DIMENSION S(6)` (5). |
| 7–13 | 시작 시 1행 YFUNC 루틴 안. J2D는 S(1)·S(2)·S(3)의 쌍별 차이 제곱 합에 S(4)·S(5)·S(6)의 제곱 합의 6배를 더한 뒤 6으로 나눈 값이다(7–12). 해석: S(1:3)을 정상 성분으로 보고 S(4:6)을 전단 성분으로 보면 이 식은 편차 성분의 두 번째 불변량에 해당한다. 7–10행은 6열의 &로 이어지는 하나의 대입문이다. 원문: `      J2D =   ( S(1) - S(2) )*( S(1) - S(2) )` (7); `     &      + ( S(2) - S(3) )*( S(2) - S(3) )` (8); `     &      + ( S(3) - S(1) )*( S(3) - S(1) )` (9); `     &      + 6.D0*( S(4)*S(4) + S(5)*S(5) + S(6)*S(6) )` (10); `      J2D = J2D/6.D0` (12). [11-04 전수 검증 정정] |
| 14–22 | 시작 시 1행 YFUNC 루틴 안. IYLD에 따라 von Mises 또는 Drucker–Prager 항복 함수(yield function) F를 계산한다(14–19). 두 번째 분기는 J1과 계수 A를 먼저 계산한다. ELSE는 없다. IYLD가 1도 2도 아니면 F에 값을 대입하지 않는다(14–20). 조건 종료·주석·루틴 종료를 포함한다(20–22). 원문: `      IF( IYLD == 1 ) THEN       ! von Mieses` (14); `        F = DSQRT (3.D0 * J2D)` (15); `      ELSEIF( IYLD == 2 ) THEN  ! Drucker-Prager` (16); `        J1 = S(1) + S(2) + S(3)` (17); `        A = 1.D0 / ( 1.D0/DSQRT(3.D0) - ALP )` (18); `        F = A*( ALP*J1 + DSQRT(J2D) )` (19); `      ENDIF` (20); `      END` (22). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 14–20: F에 값을 대입하는 분기는 IYLD가 1 또는 2일 때뿐이다.
- 18: A의 분모는 1.D0/DSQRT(3.D0)-ALP이며, 이 분모의 0 여부를 검사하는 문장은 없다.
