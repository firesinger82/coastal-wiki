---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/spcdface2.f
lines: 47
sha256: 7d2f51afc9dc94816122362d52f0e69810c0a697bae4c72a0258f225a1ca9fcf
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# spcdface2.f — 판독 구간 기록

구간은 1행부터 47행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | SPCDFACE2는 자유 방향(free direction), 종속 방향(slave direction), 구속 방향(constraint direction)을 IFR1,IFR2,IFR3로 사용한다는 주석을 둔다(7–9). 세 IC를 순회하여 각각 IC=0,2,1인 방향을 배정한다(11–19). 선언과 주석을 포함한다. 원문: `      SUBROUTINE SPCDFACE2(P,IC,XYZ,RL)` (1). `      IMPLICIT REAL*8(A-H,O-Z)` (3). `      DIMENSION IC(3),X(5),Y(5),Z(5),XYZ(3,4),P(3),RL(3)` (4). `C     IFR1 : FREE` (7). `C     IFR2 : SLAVE` (8). `C     IFR3 : CONSTRAINT` (9). `      DO 100 I=1,3` (11). `        IF( IC(I) .EQ. 0 ) THEN` (12). `          IFR1=I` (13). `        ELSEIF( IC(I) .EQ. 2 ) THEN` (14). `          IFR2=I` (15). `        ELSEIF( IC(I) .EQ. 1 ) THEN` (16). `          IFR3=I` (17). `        ENDIF` (18). `  100 CONTINUE` (19). 12–18행 IC 분기 사슬에는 ELSE가 없다. 같은 IC 값이 여러 방향에 있으면 해당 IFR 변수에는 마지막으로 일치한 I가 남는다. [11-04 전수 검증 보완] |
| 21–30 | 시작 시 1행 SPCDFACE2 루틴 안. 세 면(face) 점과 네 번째 점을 IFR 순서의 X,Y,Z로 복사한다(21–25). RL 가중합으로 다섯 번째 X,Y,Z를 계산한다(27–29). 원문: `      DO 200 I=1,4` (21). `        X(I)=XYZ(IFR1,I)` (22). `        Y(I)=XYZ(IFR2,I)` (23). `        Z(I)=XYZ(IFR3,I)` (24). `  200 CONTINUE` (25). `      X(5) = RL(1)*XYZ(IFR1,1) + RL(2)*XYZ(IFR1,2) + RL(3)*XYZ(IFR1,3)` (27). `      Y(5) = RL(1)*XYZ(IFR2,1) + RL(2)*XYZ(IFR2,2) + RL(3)*XYZ(IFR2,3)` (28). `      Z(5) = RL(1)*XYZ(IFR3,1) + RL(2)*XYZ(IFR3,2) + RL(3)*XYZ(IFR3,3)` (29). |
| 31–47 | 시작 시 1행 SPCDFACE2 루틴 안. X,Z 좌표의 두 행렬식(determinant) R로 A1,B1,A2,B2를 계산한다(31–37). 이 계수로 Y=A*X+B 관계를 구성하고 가중점 X(5),Y(5)에서의 보정 P를 구한다(39–44). P의 구속 성분은 Z(4)이다(44). RETURN과 END를 포함한다. 원문: `      R  = (X(1)-X(3))*(Z(2)-Z(3)) - (X(2)-X(3))*(Z(1)-Z(3))` (31). `      A1 = (Z(2)-Z(3))/R` (32). `      B1 = -( X(3)*(Z(2)-Z(3)) + (X(2)-X(3))*(Z(4)-Z(3)) ) / R` (33). `      R  = (X(2)-X(3))*(Z(1)-Z(3)) - (X(1)-X(3))*(Z(2)-Z(3))` (35). `      A2 = (Z(1)-Z(3))/R` (36). `      B2 = -( X(3)*(Z(1)-Z(3)) + (X(1)-X(3))*(Z(4)-Z(3)) ) / R` (37). `      A = (Y(1)-Y(3))*A1 + (Y(2)-Y(3))*A2` (39). `      B = (Y(1)-Y(3))*B1 + (Y(2)-Y(3))*B2 + Y(3)` (40). `      P(IFR1) = ( -A*B + X(5) + A*Y(5) ) / ( A*A + 1. )` (42). `      P(IFR2) = A*P(IFR1) + B` (43). `      P(IFR3) = Z(4)` (44). `      RETURN` (46). `      END` (47). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11–19: IFR1,IFR2,IFR3는 해당 IC=0,2,1 조건에서만 대입된다.
- 31–37: 두 R로 나누기 전에 0 검사는 없다.
- 29: Z(5)는 계산하지만 후속 실행문에서 참조하지 않는다.
