---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/spcdedge.f
lines: 38
sha256: c7f5a9626533300de7a557d4375dd2716ff785bb9bf06eeb2ff38afc8ffb11da
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# spcdedge.f — 판독 구간 기록

구간은 1행부터 38행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | SPCDEDGE는 변(edge) 위의 보정 위치 P를 구한다. 주석의 IFR1은 구속(constraint), IFR2,IFR3는 종속 방향(slave direction)이다(7–9). IC=1인 첫 방향을 IFR1로 고르고 나머지 방향을 배정한다(11–23). 선언·구분 주석을 포함한다. 원문: `      SUBROUTINE SPCDEDGE(P,IC,XYZ)` (1). `      IMPLICIT REAL*8(A-H,O-Z)` (3). `      DIMENSION IC(3),X(3),Y(3),Z(3),XYZ(3,3),P(3)` (4). `C     IFR1 : CONSTRAINT` (7). `C     IFR2 : SLAVE` (8). `C     IFR3 : SLAVE` (9). `      IF( IC(1) .EQ. 1 ) THEN` (11). `        IFR1=1` (12). `        IFR2=2` (13). `        IFR3=3` (14). `      ELSEIF( IC(2) .EQ. 1 ) THEN` (15). `        IFR1=2` (16). `        IFR2=1` (17). `        IFR3=3` (18). `      ELSEIF( IC(3) .EQ. 1 ) THEN` (19). `        IFR1=3` (20). `        IFR2=1` (21). `        IFR3=2` (22). `      ENDIF` (23). |
| 25–38 | 시작 시 1행 SPCDEDGE 루틴 안. 세 점의 좌표를 IFR 순서의 X,Y,Z로 복사한다(25–29). X(3)을 통과하도록 T를 계산하고 P의 구속 성분을 보존하며 나머지 성분을 선형 보간(linear interpolation)한다(31–35). RETURN과 END를 포함한다. 원문: `      DO 100 I=1,3` (25). `        X(I)=XYZ(IFR1,I)` (26). `        Y(I)=XYZ(IFR2,I)` (27). `        Z(I)=XYZ(IFR3,I)` (28). `  100 CONTINUE` (29). `      T=(X(3)-X(1))/(X(2)-X(1))` (31). `      P(IFR1) = X(3)` (33). `      P(IFR2) = Y(1) + T*( Y(2)-Y(1) )` (34). `      P(IFR3) = Z(1) + T*( Z(2)-Z(1) )` (35). `      RETURN` (37). `      END` (38). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11–23: IC의 어떤 성분도 1이 아닐 때 IFR1,IFR2,IFR3를 설정하는 ELSE가 없다.
- 31: X(2)-X(1)로 나누기 전에 0 검사가 없다.
