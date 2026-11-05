---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/green_hx1.f
lines: 44
sha256: 309ac49c312576d942eb1d7e1b2b3a4924356908739371ef268678c4e76bf816
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# green_hx1.f — 판독 구간 기록

구간은 1행부터 44행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | GREEN_HX1의 일본어 인수 설명과 배열 선언이다. EPS(1:3)은 DUDX의 마지막 첨자 1을 쓴다. 전단 성분 EPS(4:6)은 각각 마지막 첨자 2·3·4를 쓴다. IGNL == 0이면 반환한다. 원문: `      SUBROUTINE GREEN_HX1(EPS,DUDX,IGNL)` (1)； `C     EPS  : OUT : Green-Lagrange歪` (3) (Green-Lagrange 변형률(Green-Lagrange strain) 출력이다.)； `C                  EPS(1) = ε11 at (XG1,XG2,XG3)` (4)； `C                  EPS(2) = ε22 at (XG1,XG2,XG3)` (5)； `C                  EPS(3) = ε33 at (XG1,XG2,XG3)` (6)； `C                  EPS(4) = 2*ε12 at (0,0,XG3) (次数低減積分)` (7) (0,0,XG3에서 전단 변형률 2*ε12를 계산한다. 차수 저감 적분(reduced integration)이다.)； `C                  EPS(5) = 2*ε23 at (XG1,0,0) (次数低減積分)` (8) (XG1,0,0에서 전단 변형률 2*ε23을 계산한다. 차수 저감 적분이다.)； `C                  EPS(6) = 2*ε31 at (0,XG2,0) (次数低減積分)` (9) (0,XG2,0에서 전단 변형률 2*ε31을 계산한다. 차수 저감 적분이다.)； `C     DUDX : IN  : DUDX(i,j) = ∂uj/∂xi` (10)； `C     IGNL : IN  : =0:微小変形, =1:大変形` (11) (0은 미소변형(small deformation), 1은 대변형(large deformation)이다.)； `      IMPLICIT REAL*8(A-H,O-Z)` (13)； `      DIMENSION EPS(6),DUDX(3,3,4)` (14)； `      EPS(1)=DUDX(1,1,1)` (16)； `      EPS(2)=DUDX(2,2,1)` (17)； `      EPS(3)=DUDX(3,3,1)` (18)； `      EPS(4)=DUDX(2,1,2)+DUDX(1,2,2)` (19)； `      EPS(5)=DUDX(3,2,3)+DUDX(2,3,3)` (20)； `      EPS(6)=DUDX(1,3,4)+DUDX(3,1,4)` (21)； `      IF( IGNL == 0 ) RETURN` (23)。 [11-04 전수 검증 정정] |
| 25–44 | 시작 시 1행 GREEN_HX1 루틴 안이며 23행의 `IF( IGNL == 0 ) RETURN`에서 반환하지 않은 상태이다. 따라서 이 구간은 IGNL이 0이 아닐 때 실행된다. 각 성분에 해당하는 적분 위치의 DUDX로 이차 항을 계산하여 EPS에 더한다. 원문: 연속문(25–27): `      EPS(1)=EPS(1)+0.5D0*( DUDX(1,1,1)*DUDX(1,1,1)` (25)； `     &                    + DUDX(1,2,1)*DUDX(1,2,1)` (26)； `     &                    + DUDX(1,3,1)*DUDX(1,3,1) )` (27)； 연속문(28–30): `      EPS(2)=EPS(2)+0.5D0*( DUDX(2,1,1)*DUDX(2,1,1)` (28)； `     &                    + DUDX(2,2,1)*DUDX(2,2,1)` (29)； `     &                    + DUDX(2,3,1)*DUDX(2,3,1) )` (30)； 연속문(31–33): `      EPS(3)=EPS(3)+0.5D0*( DUDX(3,1,1)*DUDX(3,1,1)` (31)； `     &                    + DUDX(3,2,1)*DUDX(3,2,1)` (32)； `     &                    + DUDX(3,3,1)*DUDX(3,3,1) )` (33)； 연속문(34–36): `      EPS(4)=EPS(4)+( DUDX(1,1,2)*DUDX(2,1,2)` (34)； `     &              + DUDX(1,2,2)*DUDX(2,2,2)` (35)； `     &              + DUDX(1,3,2)*DUDX(2,3,2) )` (36)； 연속문(37–39): `      EPS(5)=EPS(5)+( DUDX(2,1,3)*DUDX(3,1,3)` (37)； `     &              + DUDX(2,2,3)*DUDX(3,2,3)` (38)； `     &              + DUDX(2,3,3)*DUDX(3,3,3) )` (39)； 연속문(40–42): `      EPS(6)=EPS(6)+( DUDX(3,1,4)*DUDX(1,1,4)` (40)； `     &              + DUDX(3,2,4)*DUDX(1,2,4)` (41)； `     &              + DUDX(3,3,4)*DUDX(1,3,4) )` (42)； `      END` (44)。 [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 14·16–21: DUDX 배열의 마지막 첨자 크기는 4이다. 10행 주석의 DUDX(i,j)에는 이 첨자가 표기되지 않는다.
