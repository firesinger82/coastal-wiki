---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/volcd.f
lines: 52
sha256: c3bef385e24480b6b44be688843e5b20dc0c2889de6a95f0254d0bd89dddd333
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# volcd.f — 판독 구간 기록

구간은 1행부터 52행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | VOLCD는 네 점 XYZ와 점 POS에서 체적 좌표(volume coordinate) RN을 계산한다. XYZ 성분을 X1..Z4로 복사하고 좌표 차이의 행렬식(determinant) 식으로 V6를 구한다(6–21). 선언과 주석을 포함한다. 원문: `      SUBROUTINE VOLCD(RN,XYZ,POS)` (1). `      IMPLICIT REAL*8(A-H,O-Z)` (3). `      DIMENSION XYZ(3,4),POS(3),A(4),B(4),C(4),D(4),RN(4)` (4). `      X1 = XYZ(1,1)` (6). `      Y1 = XYZ(2,1)` (7). `      Z1 = XYZ(3,1)` (8). `      X2 = XYZ(1,2)` (9). `      Y2 = XYZ(2,2)` (10). `      Z2 = XYZ(3,2)` (11). `      X3 = XYZ(1,3)` (12). `      Y3 = XYZ(2,3)` (13). `      Z3 = XYZ(3,3)` (14). `      X4 = XYZ(1,4)` (15). `      Y4 = XYZ(2,4)` (16). `      Z4 = XYZ(3,4)` (17). 연속문(19–21): `      V6 = -(   (X1-X4)*(Y2-Y4)*(Z3-Z4) + (X3-X4)*(Z2-Z4)*(Y1-Y4)` (19); `     &        + (X2-X4)*(Y3-Y4)*(Z1-Z4) - (Z1-Z4)*(Y2-Y4)*(X3-X4)` (20); `     &        - (X1-X4)*(Y3-Y4)*(Z2-Z4) - (Y1-Y4)*(X2-X4)*(Z3-Z4)  )` (21). |
| 23–46 | 시작 시 1행 VOLCD 루틴 안. 네 좌표 성분마다 A,B,C,D의 좌표 다항식 계수를 구성한다(23–45). 각 A의 연속행과 B,C,D 식은 아래 원문과 같다. 원문: 연속문(23–24): `      A(1) =   X2*Y3*Z4 + X3*Y4*Z2 + X4*Z3*Y2` (23); `     &       - Z2*Y3*X4 - Y2*X3*Z4 - X2*Y4*Z3` (24). `      B(1) = -( Y3*Z4 + Y4*Z2 + Z3*Y2 - Z2*Y3 - Y2*Z4 - Y4*Z3 )` (25). `      C(1) = -( X2*Z4 + X3*Z2 + X4*Z3 - Z2*X4 - X3*Z4 - X2*Z3 )` (26). `      D(1) = -( X2*Y3 + X3*Y4 + X4*Y2 - Y3*X4 - Y2*X3 - X2*Y4 )` (27). 연속문(29–30): `      A(2) =   X3*Y1*Z4 + X1*Y4*Z3 + X4*Z1*Y3` (29); `     &       - Z3*Y1*X4 - Y3*X1*Z4 - X3*Y4*Z1` (30). `      B(2) = -( Y1*Z4 + Y4*Z3 + Z1*Y3 - Z3*Y1 - Y3*Z4 - Y4*Z1 )` (31). `      C(2) = -( X3*Z4 + X1*Z3 + X4*Z1 - Z3*X4 - X1*Z4 - X3*Z1 )` (32). `      D(2) = -( X3*Y1 + X1*Y4 + X4*Y3 - Y1*X4 - Y3*X1 - X3*Y4 )` (33). 연속문(35–36): `      A(3) =   X4*Y1*Z2 + X1*Y2*Z4 + X2*Z1*Y4` (35); `     &       - Z4*Y1*X2 - Y4*X1*Z2 - X4*Y2*Z1` (36). `      B(3) = -( Y1*Z2 + Y2*Z4 + Z1*Y4 - Z4*Y1 - Y4*Z2 - Y2*Z1 )` (37). `      C(3) = -( X4*Z2 + X1*Z4 + X2*Z1 - Z4*X2 - X1*Z2 - X4*Z1 )` (38). `      D(3) = -( X4*Y1 + X1*Y2 + X2*Y4 - Y1*X2 - Y4*X1 - X4*Y2 )` (39). 연속문(41–42): `      A(4) =   X1*Y3*Z2 + X3*Y2*Z1 + X2*Z3*Y1` (41); `     &       - Z1*Y3*X2 - Y1*X3*Z2 - X1*Y2*Z3` (42). `      B(4) = -( Y3*Z2 + Y2*Z1 + Z3*Y1 - Z1*Y3 - Y1*Z2 - Y2*Z3 )` (43). `      C(4) = -( X1*Z2 + X3*Z1 + X2*Z3 - Z1*X2 - X3*Z2 - X1*Z3 )` (44). `      D(4) = -( X1*Y3 + X3*Y2 + X2*Y1 - Y3*X2 - Y1*X3 - X1*Y2 )` (45). |
| 47–52 | 시작 시 1행 VOLCD 루틴 안. I=1..4에서 POS에 대한 A+B*x+C*y+D*z를 V6로 나누어 RN(I)을 구한다(47–49). RETURN과 END를 포함한다. 원문: `      DO 100 I=1,4` (47). `        RN(I) = ( A(I) + B(I)*POS(1) + C(I)*POS(2) + D(I)*POS(3) ) / V6` (48). `  100 CONTINUE` (49). `      RETURN` (51). `      END` (52). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 19–21·48: V6로 나누기 전에 V6=0 검사가 없다.
