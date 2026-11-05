---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/green.f
lines: 44
sha256: 1202491abb401efe4500626b413da5bf280a5cbdb01da8ca39b413486cb32f7b
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# green.f — 판독 구간 기록

구간은 1행부터 44행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | GREEN의 일본어 인수 설명과 배열 선언이다. DUDX에서 선형 변형률 여섯 성분을 계산한다. IGNL == 0이면 반환한다. 원문: `      SUBROUTINE GREEN(EPS,DUDX,IGNL)` (1)； `C     EPS  : OUT : Green-Lagrange歪` (3) (Green-Lagrange 변형률(Green-Lagrange strain) 출력이다.)； `C                  EPS(1) = ε11` (4)； `C                  EPS(2) = ε22` (5)； `C                  EPS(3) = ε33` (6)； `C                  EPS(4) = 2*ε12` (7)； `C                  EPS(5) = 2*ε23` (8)； `C                  EPS(6) = 2*ε31` (9)； `C     DUDX : IN  : DUDX(i,j) = ∂uj/∂xi` (10)； `C     IGNL : IN  : =0:微小変形, =1:大変形` (11) (0은 미소변형(small deformation), 1은 대변형(large deformation)이다.)； `      IMPLICIT REAL*8(A-H,O-Z)` (13)； `      DIMENSION EPS(6),DUDX(3,3)` (14)； `      EPS(1)=DUDX(1,1)` (16)； `      EPS(2)=DUDX(2,2)` (17)； `      EPS(3)=DUDX(3,3)` (18)； `      EPS(4)=DUDX(2,1)+DUDX(1,2)` (19)； `      EPS(5)=DUDX(3,2)+DUDX(2,3)` (20)； `      EPS(6)=DUDX(1,3)+DUDX(3,1)` (21)； `      IF( IGNL == 0 ) RETURN` (23)。 |
| 25–44 | 시작 시 1행 GREEN 루틴 안이며 23행의 `IF( IGNL == 0 ) RETURN`에서 반환하지 않은 상태이다. 따라서 이 구간은 IGNL이 0이 아닐 때 실행된다. DUDX 곱으로 Green-Lagrange 변형률의 이차 항을 여섯 성분에 더한다. EPS(1:3)에 더하는 이차 항에는 0.5 계수를 곱한다. 원문: 연속문(25–27): `      EPS(1)=EPS(1)+0.5D0*( DUDX(1,1)*DUDX(1,1)` (25)； `     &                    + DUDX(1,2)*DUDX(1,2)` (26)； `     &                    + DUDX(1,3)*DUDX(1,3) )` (27)； 연속문(28–30): `      EPS(2)=EPS(2)+0.5D0*( DUDX(2,1)*DUDX(2,1)` (28)； `     &                    + DUDX(2,2)*DUDX(2,2)` (29)； `     &                    + DUDX(2,3)*DUDX(2,3) )` (30)； 연속문(31–33): `      EPS(3)=EPS(3)+0.5D0*( DUDX(3,1)*DUDX(3,1)` (31)； `     &                    + DUDX(3,2)*DUDX(3,2)` (32)； `     &                    + DUDX(3,3)*DUDX(3,3) )` (33)； 연속문(34–36): `      EPS(4)=EPS(4)+( DUDX(1,1)*DUDX(2,1)` (34)； `     &              + DUDX(1,2)*DUDX(2,2)` (35)； `     &              + DUDX(1,3)*DUDX(2,3) )` (36)； 연속문(37–39): `      EPS(5)=EPS(5)+( DUDX(2,1)*DUDX(3,1)` (37)； `     &              + DUDX(2,2)*DUDX(3,2)` (38)； `     &              + DUDX(2,3)*DUDX(3,3) )` (39)； 연속문(40–42): `      EPS(6)=EPS(6)+( DUDX(3,1)*DUDX(1,1)` (40)； `     &              + DUDX(3,2)*DUDX(1,2)` (41)； `     &              + DUDX(3,3)*DUDX(1,3) )` (42)； `      END` (44)。 [11-04 전수 검증 정정] [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11·23: 주석은 IGNL을 0·1로 설명한다. 실행 조건은 0일 때의 반환이며 다른 모든 값은 이차 항 계산으로 이어진다.
