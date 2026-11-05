---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/areacd.f
lines: 51
sha256: b108628c641807fc0f042a07eeed020a59a5fa97f101fd442ab79ab0301e10c1
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# areacd.f — 판독 구간 기록

구간은 1행부터 51행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | AREACD의 배정밀도(double precision)와 배열 범위를 선언한다(1–5). SUBVEC·DIRCOS·CROSS2를 7–11행의 인수로 호출한다. `DO 200 I=1,4`에서 SUBVEC를 호출한다(13–15). `CALL ATXB(GE,E,GG,3,3,4)`를 호출한다(17). 해석: 호출 이름과 인수 배열의 관계는 기준점에 대한 벡터와 국소 기저를 구성하는 형태이다. 원문(연속 표시는 같은 문장의 이어지는 행이다): `      SUBROUTINE AREACD(RL,RN,Z4,XYZ)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION GE(3,4),V12(3),V13(3),XYZ(3,4),E(3,3),GG(3,4),RL(3)` (4); `     &         ,RN(3)` (5); `C----&------------------------------------------------------------------` (6); `      CALL SUBVEC(V12,XYZ(1,2),XYZ(1,1),3)` (7); `      CALL SUBVEC(V13,XYZ(1,3),XYZ(1,1),3)` (8); `      CALL DIRCOS(E(1,1),V12,3)` (9); `      CALL CROSS2(E(1,1),V13,E(1,3))` (10); `      CALL CROSS2(E(1,3),E(1,1),E(1,2))` (11); `      DO 200 I=1,4` (13); `        CALL SUBVEC(GG(1,I),XYZ(1,I),XYZ(1,1),3)` (14); `  200 CONTINUE` (15); `      CALL ATXB(GE,E,GG,3,3,4)` (17). [11-04 전수 검증 정정] |
| 19–51 | 시작 시 1행 AREACD 루틴 안. GE의 첫 두 성분을 X1·Y1부터 X4·Y4까지 복사한다(19–26). S2와 A/B/C 계수를 계산한다(28–40). RL(1:3)을 42–44행 식으로 계산한다. `CALL SHIFT1(RN,E(1,3),3)`을 호출한다(46). `Z4 = GE(3,4)`를 대입한다(48). 해석: S2와 RL 식은 평면 삼각형의 부호 있는 배면적과 면적좌표에 해당하는 형태이다. 원문(연속 표시는 같은 문장의 이어지는 행이다): `      X1 = GE(1,1)` (19); `      Y1 = GE(2,1)` (20); `      X2 = GE(1,2)` (21); `      Y2 = GE(2,2)` (22); `      X3 = GE(1,3)` (23); `      Y3 = GE(2,3)` (24); `      X4 = GE(1,4)` (25); `      Y4 = GE(2,4)` (26); `      S2 = ( X2*Y3 + X1*Y2 + X3*Y1 ) - ( X2*Y1 + X1*Y3 + X3*Y2 )` (28); `      A1 = X2*Y3 - X3*Y2` (30); `      B1 = Y2 - Y3` (31); `      C1 = X3 - X2` (32); `      A2 = X3*Y1 - X1*Y3` (34); `      B2 = Y3 - Y1` (35); `      C2 = X1 - X3` (36); `      A3 = X1*Y2 - X2*Y1` (38); `      B3 = Y1 - Y2` (39); `      C3 = X2 - X1` (40); `      RL(1) = ( A1 + B1*X4 + C1*Y4 ) / S2` (42); `      RL(2) = ( A2 + B2*X4 + C2*Y4 ) / S2` (43); `      RL(3) = ( A3 + B3*X4 + C3*Y4 ) / S2` (44); `      CALL SHIFT1(RN,E(1,3),3)` (46); `      Z4 = GE(3,4)` (48); `      RETURN` (50); `      END` (51). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 28·42–44: RL 계산은 S2로 나눈다. 이 루틴 안에는 S2=0을 검사하는 분기가 없다.
