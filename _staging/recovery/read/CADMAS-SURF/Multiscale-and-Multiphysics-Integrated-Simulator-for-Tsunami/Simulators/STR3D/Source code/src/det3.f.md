---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/det3.f
lines: 30
sha256: b9ebffbaa9253fa3f5083f8d90872a48996d8b22067b19a358a79f0975e56883
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# det3.f — 판독 구간 기록

구간은 1행부터 30행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | DET3의 입출력과 배열을 선언한다. `節点数`는 절점 수(number of nodes), `節点座標`는 절점좌표(nodal coordinate)다. 3행 주석은 DET를 야코비안 행렬식으로 표시한다. 5행 주석은 P(i,j)를 ∂Nj/∂ξi로 표시한다. 해석: N을 형상함수로 보면 P는 형상함수 미분이다. 원문: `      SUBROUTINE DET3(DET,NG,P,XYZ,ITO)` (1); 주석 원문 `C     DET : OUT : \|J\| ( Jij = ∂xj/∂ξi )` (3); 주석 원문 `C     NG  : IN  : 節点数` (4); 주석 원문 `C     P   : IN  : P(i,j) = ∂Nj/∂ξi` (5); 주석 원문 `C     XYZ : IN  : 節点座標` (6); `      IMPLICIT REAL*8(A-H,O-Z)` (8); `      DIMENSION XJ(3,3),P(3,NG),XYZ(3,NG)` (9). [11-04 전수 검증 정정] |
| 11–19 | 시작 시 1행 DET3 루틴 안. I·J·K 루프에서 P와 XYZ의 곱을 누적하여 3×3 야코비안 행렬 XJ를 만든다. 원문: `      DO 100 I=1,3` (11); `        DO 200 J=1,3` (12); `          XJ(I,J)=0.` (13); `          DO 300 K=1,NG` (14); `            XJ(I,J)=XJ(I,J)+P(I,K)*XYZ(J,K)` (15); `  300     CONTINUE` (16); `  200   CONTINUE` (17); `  100 CONTINUE` (18). |
| 20–30 | 시작 시 1행 DET3 루틴 안. 3항의 연속문으로 DET를 전개한다. DET가 1.D-20보다 작으면 오류 메시지와 ERRSTP(11,ITO)를 실행한다. 반환문과 루틴 끝을 포함한다. 원문: `      DET =  XJ(1,1) * ( XJ(2,2)*XJ(3,3)-XJ(3,2)*XJ(2,3) )`<br>`     *     + XJ(2,1) * ( XJ(3,2)*XJ(1,3)-XJ(1,2)*XJ(3,3) )`<br>`     *     + XJ(3,1) * ( XJ(1,2)*XJ(2,3)-XJ(2,2)*XJ(1,3) )` (20–22); `      IF( DET .LT. 1.D-20 )  THEN` (24); `        WRITE(ITO,*) 'ELEMENT VOLUME IS TOO SMALL.'` (25); `        CALL ERRSTP(11,ITO)` (26); `      ENDIF` (27); `      RETURN` (29); `      END` (30). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 24: 행렬식 검사는 DET<1.D-20이다. ABS(DET)를 쓰지 않는다.
