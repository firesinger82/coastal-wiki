---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/derxte1.f
lines: 55
sha256: 590aa81e9e256bd418559467f8df8f252e9ca3e296cb9e2468fbe8c65366f43c
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# derxte1.f — 판독 구간 기록

구간은 1행부터 55행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | DERXTE1의 입출력과 배열을 선언한다. `テトラの体積*6`은 사면체(tetrahedron) 체적의 6배, `節点座標`는 절점좌표(nodal coordinate)다. 네 절점의 세 좌표를 스칼라 변수에 복사한다. 원문: `      SUBROUTINE DERXTE1(DNDX,V6,XYZ,ITO)` (1); 주석 원문 `C     DNDX : OUT : DNDX(i,j) = ∂Nj/∂xi` (3); 주석 원문 `C     V6   : OUT : テトラの体積*6` (4); 주석 원문 `C     XYZ  : IN  : 節点座標` (5); `      IMPLICIT REAL*8(A-H,O-Z)` (7); `      DIMENSION XYZ(3,4),B(4),C(4),D(4),DNDX(3,4)` (8); 주석 원문 `C----&------------------------------------------------------------------` (9); `      X1 = XYZ(1,1)` (10); `      Y1 = XYZ(2,1)` (11); `      Z1 = XYZ(3,1)` (12); `      X2 = XYZ(1,2)` (13); `      Y2 = XYZ(2,2)` (14); `      Z2 = XYZ(3,2)` (15); `      X3 = XYZ(1,3)` (16); `      Y3 = XYZ(2,3)` (17); `      Z3 = XYZ(3,3)` (18); `      X4 = XYZ(1,4)` (19); `      Y4 = XYZ(2,4)` (20); `      Z4 = XYZ(3,4)` (21). |
| 23–42 | 시작 시 1행 DERXTE1 루틴 안. 좌표 차이의 삼중곱으로 V6를 계산한다. 네 절점 각각의 B·C·D를 좌표 곱의 합차와 V6 나눗셈으로 구한다. V6의 23–25행 연속문 전체를 인용한다. 원문: `      V6 = -(   (X1-X4)*(Y2-Y4)*(Z3-Z4) + (X3-X4)*(Z2-Z4)*(Y1-Y4)`<br>`     &        + (X2-X4)*(Y3-Y4)*(Z1-Z4) - (Z1-Z4)*(Y2-Y4)*(X3-X4)`<br>`     &        - (X1-X4)*(Y3-Y4)*(Z2-Z4) - (Y1-Y4)*(X2-X4)*(Z3-Z4)  )` (23–25); `      B(1) = -( Y3*Z4 + Y4*Z2 + Z3*Y2 - Z2*Y3 - Y2*Z4 - Y4*Z3 ) / V6` (27); `      C(1) = -( X2*Z4 + X3*Z2 + X4*Z3 - Z2*X4 - X3*Z4 - X2*Z3 ) / V6` (28); `      D(1) = -( X2*Y3 + X3*Y4 + X4*Y2 - Y3*X4 - Y2*X3 - X2*Y4 ) / V6` (29); `      B(2) = -( Y1*Z4 + Y4*Z3 + Z1*Y3 - Z3*Y1 - Y3*Z4 - Y4*Z1 ) / V6` (31); `      C(2) = -( X3*Z4 + X1*Z3 + X4*Z1 - Z3*X4 - X1*Z4 - X3*Z1 ) / V6` (32); `      D(2) = -( X3*Y1 + X1*Y4 + X4*Y3 - Y1*X4 - Y3*X1 - X3*Y4 ) / V6` (33); `      B(3) = -( Y1*Z2 + Y2*Z4 + Z1*Y4 - Z4*Y1 - Y4*Z2 - Y2*Z1 ) / V6` (35); `      C(3) = -( X4*Z2 + X1*Z4 + X2*Z1 - Z4*X2 - X1*Z2 - X4*Z1 ) / V6` (36); `      D(3) = -( X4*Y1 + X1*Y2 + X2*Y4 - Y1*X2 - Y4*X1 - X4*Y2 ) / V6` (37); `      B(4) = -( Y3*Z2 + Y2*Z1 + Z3*Y1 - Z1*Y3 - Y1*Z2 - Y2*Z3 ) / V6` (39); `      C(4) = -( X1*Z2 + X3*Z1 + X2*Z3 - Z1*X2 - X3*Z2 - X1*Z3 ) / V6` (40); `      D(4) = -( X1*Y3 + X3*Y2 + X2*Y1 - Y3*X2 - Y1*X3 - X1*Y2 ) / V6` (41). |
| 43–55 | 시작 시 1행 DERXTE1 루틴 안. 네 절점의 B·C·D를 DNDX 세 행에 복사한다. V6가 1.D-20보다 작으면 오류 메시지를 출력하고 ERRSTP(11,ITO)를 호출한다. 반환문과 루틴 끝을 포함한다. 원문: `      DO 100 J=1,4` (43); `        DNDX(1,J)=B(J)` (44); `        DNDX(2,J)=C(J)` (45); `        DNDX(3,J)=D(J)` (46); `  100 CONTINUE` (47); `      IF( V6 < 1.D-20 ) THEN` (49); `        WRITE(ITO,*) 'ELEMENT VOLUME IS TOO SMALL.'` (50); `        CALL ERRSTP(11,ITO)` (51); `      ENDIF` (52); `      RETURN` (54); `      END` (55). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 27–41·49–52: V6로 나누는 계산을 먼저 수행한다. V6<1.D-20 검사는 그 계산과 DNDX 복사 뒤에 있다.
