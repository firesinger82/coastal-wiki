---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/corredge.f
lines: 38
sha256: ebda483d999d95e2c49cb404288d2537ac018f6f6139020cc7e1210af499b6ad
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# corredge.f — 판독 구간 기록

구간은 1행부터 38행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | 루틴·암시적 자료형·배열 차원을 선언한다(1–4). 주석은 IFR1을 구속(constraint), IFR2·IFR3을 종속(slave) 성분으로 구분한다(7–9). 원문: `      SUBROUTINE CORREDGE(DUG,IC,XYZ)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION IC(3),X(3),Y(3),Z(3),XYZ(3,3),DUG(3)` (4); 주석 원문: `C     IFR1 : CONSTRAINT` (7); 주석 원문: `C     IFR2 : SLAVE` (8); 주석 원문: `C     IFR3 : SLAVE` (9). |
| 11–38 | 시작 시 1행 CORREDGE 루틴 안이다. IC 값 1의 위치로 성분 순서를 선택한다(11–23). 좌표 세 성분을 재배열한다(25–29). X 좌표 보간비 T로 DUG의 두 종속 성분을 계산하고 구속 성분은 0으로 둔다(31–35). RETURN·END로 끝낸다(37–38). 원문: `      IF( IC(1) .EQ. 1 ) THEN` (11); `        IFR1=1` (12); `        IFR2=2` (13); `        IFR3=3` (14); `      ELSEIF( IC(2) .EQ. 1 ) THEN` (15); `        IFR1=2` (16); `        IFR2=1` (17); `        IFR3=3` (18); `      ELSEIF( IC(3) .EQ. 1 ) THEN` (19); `        IFR1=3` (20); `        IFR2=1` (21); `        IFR3=2` (22); `      DO 100 I=1,3` (25); `        X(I)=XYZ(IFR1,I)` (26); `        Y(I)=XYZ(IFR2,I)` (27); `        Z(I)=XYZ(IFR3,I)` (28); `      T=(X(3)-X(1))/(X(2)-X(1))` (31); `      DUG(IFR1) = 0.` (33); `      DUG(IFR2) = Y(1)-Y(3) + T*( Y(2)-Y(1) )` (34); `      DUG(IFR3) = Z(1)-Z(3) + T*( Z(2)-Z(1) )` (35). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11–23: IC의 어느 성분도 1이 아닐 때 IFR1·IFR2·IFR3을 지정하는 ELSE가 없다.
- 31: 분모 X(2)-X(1)의 0 여부를 검사하는 문장이 없다.
