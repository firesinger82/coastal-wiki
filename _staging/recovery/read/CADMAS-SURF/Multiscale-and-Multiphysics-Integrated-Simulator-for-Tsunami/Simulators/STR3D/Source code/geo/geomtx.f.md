---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/geo/geomtx.f
lines: 30
sha256: 5c5e3f785e4c18de6f74caca49ff8ebd585c4af01c0dc56013e7911a56ee18e3
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# geomtx.f — 판독 구간 기록

구간은 1행부터 30행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | GEOMTX는 결합 행렬 EKUP·EKPP·ECPU·ECPP·EMPU를 구성한다. IMPLICIT 및 배열 첨자 범위를 아래에 적었다. KN에 해당하는 GRID 좌표를 X로 모은다. AMAT(7)는 POR, AMAT(8)는 RKF, AMAT(9)는 RK, AMAT(10)는 RHOF로 읽는다. POR는 27행의 ECPP 계수 `POR / RKF`에 쓰인다. 해석: POR는 공극률(porosity)로 보인다. 원문: `      SUBROUTINE GEOMTX(EKUP,EKPP,ECPU,ECPP,EMPU,ND,ND3,KN,GRID,AMAT` (1); `     &                 ,ITO)` (2); `      IMPLICIT REAL*8(A-H,O-Z)` (4); `      DIMENSION EKUP(ND3,ND),EKPP(ND,ND),ECPU(ND,ND3),ECPP(ND,ND)` (5); `     &         ,EMPU(ND,ND3),KN(ND),GRID(3,*),X(3,ND),AMAT(*)` (6); `      X(:,:) = GRID(:,KN(:))` (8); `      POR  = AMAT(7)` (10); `      RKF  = AMAT(8)` (11); `      RK   = AMAT(9)` (12); `      RHOF = AMAT(10)` (13) [11-04 전수 검증 정정] |
| 15–30 | ND 선택은 4·10·6 또는 15·8 또는 20에 각각 GMTXTE1·GMTXTE2·GMTXPN2·GMTXHX2를 호출한다. 해석: 루틴 이름은 각각 사면체(tetrahedron)·삼각기둥(prism)·육면체(hexahedron) 요소를 가리키는 것으로 보인다. 계산 뒤 EKPP에 RK, ECPP에 POR/RKF, EMPU에 RK*RHOF를 곱한다. 원문: `      SELECT CASE( ND )` (15); `      CASE( 4 )` (16); `        CALL GMTXTE1(EKUP,EKPP,ECPU,ECPP,EMPU,X,ITO)` (17); `      CASE( 10 )` (18); `        CALL GMTXTE2(EKUP,EKPP,ECPU,ECPP,EMPU,X,ITO)` (19); `      CASE( 6, 15 )` (20); `        CALL GMTXPN2(EKUP,EKPP,ECPU,ECPP,EMPU,ND,ND3,X,ITO)` (21); `      CASE( 8, 20 ) ` (22); `        CALL GMTXHX2(EKUP,EKPP,ECPU,ECPP,EMPU,ND,ND3,X,ITO)` (23); `      END SELECT` (24); `      EKPP(:,:) = RK * EKPP(:,:)` (26); `      ECPP(:,:) = POR / RKF * ECPP(:,:)` (27); `      EMPU(:,:) = RK * RHOF * EMPU(:,:)` (28); `      END` (30) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 15–24: ND 선택에는 CASE DEFAULT가 없다.
- 27: ECPP 계수식은 RKF로 나눈다. 이 루틴에는 RKF=0 검사문이 없다.
