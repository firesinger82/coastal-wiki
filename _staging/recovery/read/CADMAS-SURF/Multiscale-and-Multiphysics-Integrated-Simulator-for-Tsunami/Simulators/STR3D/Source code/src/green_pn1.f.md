---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/green_pn1.f
lines: 36
sha256: e2cc36863eadda770174341eaee58a5b4af3ac45819cd988eabf5eebd169d1a5
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# green_pn1.f — 판독 구간 기록

구간은 1행부터 36행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | GREEN_PN1의 일본어 인수 설명과 배열 선언이다. EPS의 1:4 성분을 선형 변위 기울기로 계산한다. IGNL == 0이면 반환한다. 원문: `      SUBROUTINE GREEN_PN1(EPS,DUDX,IGNL)` (1)； `C     EPS  : OUT : Green-Lagrange歪` (3) (Green-Lagrange 변형률(Green-Lagrange strain) 출력이다.)； `C                  EPS(1) = ε11` (4)； `C                  EPS(2) = ε22` (5)； `C                  EPS(3) = ε33` (6)； `C                  EPS(4) = 2*ε12` (7)； `C                  EPS(5) = 2*ε23` (8)； `C                  EPS(6) = 2*ε31` (9)； `C     DUDX : IN  : DUDX(i,j) = ∂uj/∂xi` (10)； `C     IGNL : IN  : =0:微小変形, =1:大変形` (11) (0은 미소변형(small deformation), 1은 대변형(large deformation)이다.)； `      IMPLICIT REAL*8(A-H,O-Z)` (13)； `      DIMENSION EPS(6),DUDX(3,3)` (14)； `      EPS(1)=DUDX(1,1)` (16)； `      EPS(2)=DUDX(2,2)` (17)； `      EPS(3)=DUDX(3,3)` (18)； `      EPS(4)=DUDX(2,1)+DUDX(1,2)` (19)； `      IF( IGNL == 0 ) RETURN` (21)。 |
| 23–36 | 시작 시 1행 GREEN_PN1 루틴 안이며 21행의 `IF( IGNL == 0 ) RETURN`에서 반환하지 않은 상태이다. 따라서 이 구간은 IGNL이 0이 아닐 때 실행된다. EPS의 1:4 성분에 이차 기울기 곱을 더하고 루틴을 끝낸다. 원문: 연속문(23–25): `      EPS(1)=EPS(1)+0.5D0*( DUDX(1,1)*DUDX(1,1)` (23)； `     &                    + DUDX(1,2)*DUDX(1,2)` (24)； `     &                    + DUDX(1,3)*DUDX(1,3) )` (25)； 연속문(26–28): `      EPS(2)=EPS(2)+0.5D0*( DUDX(2,1)*DUDX(2,1)` (26)； `     &                    + DUDX(2,2)*DUDX(2,2)` (27)； `     &                    + DUDX(2,3)*DUDX(2,3) )` (28)； 연속문(29–31): `      EPS(3)=EPS(3)+0.5D0*( DUDX(3,1)*DUDX(3,1)` (29)； `     &                    + DUDX(3,2)*DUDX(3,2)` (30)； `     &                    + DUDX(3,3)*DUDX(3,3) )` (31)； 연속문(32–34): `      EPS(4)=EPS(4)+( DUDX(1,1)*DUDX(2,1)` (32)； `     &              + DUDX(1,2)*DUDX(2,2)` (33)； `     &              + DUDX(1,3)*DUDX(2,3) )` (34)； `      END` (36)。 [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 8–9·16–34: 주석에는 EPS(5)·EPS(6)의 의미가 있다. 이 파일에는 두 성분의 대입문이 없다.
