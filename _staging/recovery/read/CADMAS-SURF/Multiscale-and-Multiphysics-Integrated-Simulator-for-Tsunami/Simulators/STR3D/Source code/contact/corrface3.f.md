---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/corrface3.f
lines: 44
sha256: 02bd93a46592a54c2991c5d21df72ad3bf695789cf5761f985e243849a8fae8a
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# corrface3.f — 판독 구간 기록

구간은 1행부터 44행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | 루틴·암시적 자료형·배열 차원을 선언한다(1–4). 주석은 IFR1·IFR2를 구속(constraint), IFR3을 종속(slave) 성분으로 적는다(7–9). IC 값 2의 위치에 따라 성분 순서를 지정한다(11–23). 원문: `      SUBROUTINE CORRFACE3(DUG,IC,XYZ)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION IC(3),X(4),Y(4),Z(4),XYZ(3,4),DUG(3)` (4); 주석 원문: `C     IFR1 : CONSTRAINT` (7); 주석 원문: `C     IFR2 : CONSTRAINT` (8); 주석 원문: `C     IFR3 : SLAVE` (9); `      IF( IC(1) .EQ. 2 ) THEN` (11); `        IFR3=1` (12); `        IFR1=2` (13); `        IFR2=3` (14); `      ELSEIF( IC(2) .EQ. 2 ) THEN` (15); `        IFR3=2` (16); `        IFR1=1` (17); `        IFR2=3` (18); `      ELSEIF( IC(3) .EQ. 2 ) THEN` (19); `        IFR3=3` (20); `        IFR1=1` (21); `        IFR2=2` (22). |
| 25–44 | 시작 시 1행 CORRFACE3 루틴 안이다. 네 점의 좌표를 재배열한 뒤 두 행렬식으로 B1·B2를 계산한다(25–35). B를 조합하여 종속 성분에 넣고 두 구속 성분은 0으로 둔다(37–41). 루틴을 끝낸다(43–44). 원문: `      DO 200 I=1,4` (25); `        X(I)=XYZ(IFR1,I)` (26); `        Y(I)=XYZ(IFR2,I)` (27); `        Z(I)=XYZ(IFR3,I)` (28); `      R  = (X(1)-X(3))*(Y(2)-Y(3)) - (X(2)-X(3))*(Y(1)-Y(3))` (31); `      B1 = ( (X(4)-X(3))*(Y(2)-Y(3)) - (X(2)-X(3))*(Y(4)-Y(3)) ) / R` (32); `      R  = (X(2)-X(3))*(Y(1)-Y(3)) - (X(1)-X(3))*(Y(2)-Y(3))` (34); `      B2 = ( (X(4)-X(3))*(Y(1)-Y(3)) - (X(1)-X(3))*(Y(4)-Y(3)) ) / R` (35); `      B = (Z(1)-Z(3))*B1 + (Z(2)-Z(3))*B2 + (Z(3)-Z(4))` (37); `      DUG(IFR1) = 0.` (39); `      DUG(IFR2) = 0.` (40); `      DUG(IFR3) = B` (41). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11–23: IC의 어느 성분도 2가 아닐 때 성분 순서를 지정하는 ELSE가 없다.
- 31–35: 두 R을 분모로 쓰기 전에 0 여부를 검사하지 않는다.
