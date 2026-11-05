---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/spcdface3.f
lines: 42
sha256: 9e3a7ce6f6061277bdad811865ed1e7aa7190d401fecf6eb994e227e15df331e
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# spcdface3.f — 판독 구간 기록

구간은 1행부터 42행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | SPCDFACE3의 주석은 IFR1,IFR2를 구속 방향(constraint direction), IFR3를 종속 방향(slave direction)으로 명시한다(7–9). IC=2인 첫 방향을 IFR3로 정하고 나머지 방향을 배정한다(11–23). 선언과 주석을 포함한다. 원문: `      SUBROUTINE SPCDFACE3(P,IC,XYZ)` (1). `      IMPLICIT REAL*8(A-H,O-Z)` (3). `      DIMENSION IC(3),X(4),Y(4),Z(4),XYZ(3,4),P(3)` (4). `C     IFR1 : CONSTRAINT` (7). `C     IFR2 : CONSTRAINT` (8). `C     IFR3 : SLAVE` (9). `      IF( IC(1) .EQ. 2 ) THEN` (11). `        IFR3=1` (12). `        IFR1=2` (13). `        IFR2=3` (14). `      ELSEIF( IC(2) .EQ. 2 ) THEN` (15). `        IFR3=2` (16). `        IFR1=1` (17). `        IFR2=3` (18). `      ELSEIF( IC(3) .EQ. 2 ) THEN` (19). `        IFR3=3` (20). `        IFR1=1` (21). `        IFR2=2` (22). `      ENDIF` (23). |
| 25–42 | 시작 시 1행 SPCDFACE3 루틴 안. 네 점을 IFR 순서의 X,Y,Z로 복사한다(25–29). X,Y의 행렬식(determinant)으로 B1,B2를 구한다(31–35). X(4),Y(4)를 보존하고 면(face)의 Z 보간식으로 나머지 P 성분을 구한다(37–39). RETURN과 END를 포함한다. 원문: `      DO 200 I=1,4` (25). `        X(I)=XYZ(IFR1,I)` (26). `        Y(I)=XYZ(IFR2,I)` (27). `        Z(I)=XYZ(IFR3,I)` (28). `  200 CONTINUE` (29). `      R  = (X(1)-X(3))*(Y(2)-Y(3)) - (X(2)-X(3))*(Y(1)-Y(3))` (31). `      B1 = ( (X(4)-X(3))*(Y(2)-Y(3)) - (X(2)-X(3))*(Y(4)-Y(3)) ) / R` (32). `      R  = (X(2)-X(3))*(Y(1)-Y(3)) - (X(1)-X(3))*(Y(2)-Y(3))` (34). `      B2 = ( (X(4)-X(3))*(Y(1)-Y(3)) - (X(1)-X(3))*(Y(4)-Y(3)) ) / R` (35). `      P(IFR1) = X(4)` (37). `      P(IFR2) = Y(4)` (38). `      P(IFR3) = (Z(1)-Z(3))*B1 + (Z(2)-Z(3))*B2 + Z(3)` (39). `      RETURN` (41). `      END` (42). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11–23: IC의 어떤 성분도 2가 아닐 때 IFR1,IFR2,IFR3를 설정하는 ELSE가 없다.
- 31–35: 두 R로 나누기 전에 0 검사는 없다.
