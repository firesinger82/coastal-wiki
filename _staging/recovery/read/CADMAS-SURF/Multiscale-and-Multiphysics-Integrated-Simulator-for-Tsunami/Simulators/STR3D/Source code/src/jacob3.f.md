---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/jacob3.f
lines: 29
sha256: 53d08dfaf0d883a9b8db69c2e544c28b1ead1e1c469e9749a0640cf2a0aa465b
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# jacob3.f — 판독 구간 기록

구간은 1행부터 29행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | JACOB3의 일본어 인수 설명과 배열 선언이다. 세 방향의 모든 조합에서 P와 XYZ의 곱을 절점에 대해 누적하여 야코비 행렬(Jacobian matrix) XJ를 구성한다. 원문: `      SUBROUTINE JACOB3(NG,P,XYZ,XJI,DET,ITO)` (1)； `C     NG  : IN  : 節点数` (3) (절점 수 입력이다.)； `C     P   : IN  : P(i,j) = ∂Nj/∂ξi` (4)； `C     XYZ : IN  : 節点座標` (5) (절점 좌표 입력이다.)； `C     XJI : OUT : [J] ( XJ(I,J) = ∂xj/∂ξi ) の逆行列` (6) (XJ(I,J)=∂xj/∂ξi인 J의 역행렬 출력이다.)； `C     DET : OUT : \|J\|` (7) (J의 행렬식(determinant) 출력이다.)； `      IMPLICIT REAL*8(A-H,O-Z)` (9)； `      DIMENSION XJ(3,3),XJI(3,3),P(3,NG),XYZ(3,NG)` (10)； `      DO 100 I=1,3` (12)； `        DO 200 J=1,3` (13)； `          XJ(I,J)=0.` (14)； `          DO 300 K=1,NG` (15)； `            XJ(I,J)=XJ(I,J)+P(I,K)*XYZ(J,K)` (16)； `  300     CONTINUE` (17)； `  200   CONTINUE` (18)； `  100 CONTINUE` (19)。 |
| 21–29 | 시작 시 1행 JACOB3 루틴 안이다. INV3를 호출하여 역행렬(inverse matrix)과 DET를 받는다. DET < 1.D-20이면 메시지를 출력하고 ERRSTP(11,ITO)를 호출한다. 원문: `      CALL INV3(XJ,XJI,DET,ITO)` (21)； `      IF( DET .LT. 1.D-20 )  THEN` (23)； `          WRITE(ITO,*) 'ELEMENT VOLUME IS TOO SMALL.'` (24)； `          CALL ERRSTP(11,ITO)` (25)； `      ENDIF` (26)； `      RETURN` (28)； `      END` (29)。 |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 21–25: DET의 하한 검사는 INV3 호출 뒤에 있다. DET의 절댓값을 취하는 연산은 이 조건에 없다.
