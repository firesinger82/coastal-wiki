---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/seq/geomtx_s.f
lines: 26
sha256: 2271a5d7aa06f92f6da13d21a1118bad4722a2daad733d93e49c741e86a4d739
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# geomtx_s.f — 판독 구간 기록

구간은 1행부터 26행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | GEOMTX_S의 암시적 형·배열 선언. KN의 좌표를 X에 복사한다. AMAT(7)에서 POR, AMAT(8)·AMAT(9)에서 RKF·RK를 얻는다. 원문: `      SUBROUTINE GEOMTX_S(EKPP,ECPP,ND,NN,KN,GRID,AMAT,ITO)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION EKPP(NN),ECPP(NN),KN(ND),GRID(3,*),X(3,ND),AMAT(*)` (4); `      X(:,:) = GRID(:,KN(:))` (6); `      POR  = AMAT(7)` (8); `      RKF  = AMAT(8)` (9); `      RK   = AMAT(9)` (10). [11-04 전수 검증 정정] |
| 12–26 | GEOMTX_S 루틴 안. 절점 수에 따라 GMTXTE1_S·GMTXTE2_S·GMTXPN2_S·GMTXHX2_S를 호출한다. EKPP는 RK, ECPP는 POR/RKF로 스케일링한다. 원문: `      SELECT CASE( ND )` (12); `      CASE( 4 )` (13); `        CALL GMTXTE1_S(EKPP,ECPP,X,ITO)` (14); `      CASE( 10 )` (15); `        CALL GMTXTE2_S(EKPP,ECPP,X,ITO)` (16); `      CASE( 6, 15 )` (17); `        CALL GMTXPN2_S(EKPP,ECPP,ND,NN,X,ITO)` (18); `      CASE( 8, 20 ) ` (19); `        CALL GMTXHX2_S(EKPP,ECPP,ND,NN,X,ITO)` (20); `      END SELECT` (21); `      EKPP(:) = RK * EKPP(:)` (23); `      ECPP(:) = POR / RKF * ECPP(:)` (24); `      END` (26). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 12–24: SELECT CASE에 CASE DEFAULT는 없다. RKF로 나누기 전 0 검사문은 없다.
