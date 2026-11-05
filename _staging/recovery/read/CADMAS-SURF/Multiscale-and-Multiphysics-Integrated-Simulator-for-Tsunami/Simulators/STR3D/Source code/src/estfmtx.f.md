---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/estfmtx.f
lines: 30
sha256: 688d8299db0161b86e235bcb48dede9572470423f5cc356650901bc0c0507380
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# estfmtx.f — 판독 구간 기록

구간은 1행부터 30행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | ESTFMTX 인수와 가변 크기 배열을 선언한다. 원문: 연속문(1–2): `      SUBROUTINE ESTFMTX(ESTF,GRID,UG,VG,ITYP,NP,NNP,RODA,BARD,BVEC,D,S` (1)； `     &                  ,IGNL,ITO)` (2)； `      IMPLICIT REAL*8(A-H,O-Z)` (4)； 연속문(5–6): `      DIMENSION ESTF(*),GRID(3,*),UG(6,*),NP(NNP),D(*),S(*),VG(3,2,2)` (5)； `     &         ,BARD(*),BVEC(3)` (6)。 |
| 8–30 | 시작 시 1행 ESTFMTX 루틴 안이다. ITYP와 NNP에 따라 호출 루틴을 선택한다. ITYP 2·6은 NNP별 루틴을 호출한다. ITYP 3은 ESTFTRS를 호출한다. ITYP 4는 ESTFBM을 호출한다. 해석: ITYP는 요소 종류이고 NNP는 절점 수이다. 해석: ITYP 2·6의 분기는 고체 요소 강성을 계산한다. 원문: `      SELECT CASE( ITYP )` (8)； `      CASE( 2, 6 )` (9)； `        SELECT CASE( NNP )` (10)； `        CASE( 4 )` (11)； `          CALL ESTFTE1(ESTF,GRID,UG,NP,D,S,IGNL,ITO)` (12)； `        CASE( 10 )` (13)； `          CALL ESTFTE2(ESTF,GRID,UG,NP,D,S,IGNL,ITO)` (14)； `        CASE( 6 )` (15)； `          CALL ESTFPN1(ESTF,GRID,UG,NP,D,S,IGNL,ITO)` (16)； `        CASE( 15 )` (17)； `          CALL ESTFPN2(ESTF,GRID,UG,NP,D,S,IGNL,ITO)` (18)； `        CASE( 8 )` (19)； `          CALL ESTFHX1(ESTF,GRID,UG,NP,D,S,IGNL,ITO)` (20)； `        CASE( 20 )` (21)； `          CALL ESTFHX2(ESTF,GRID,UG,NP,D,S,IGNL,ITO)` (22)； `        END SELECT` (23)； `      CASE( 3 )` (24)； `        CALL ESTFTRS(ESTF,GRID,UG,NP,RODA,D,S,IGNL)` (25)； `      CASE( 4 )` (26)； `        CALL ESTFBM(ESTF,GRID,UG,VG,NP,BARD(2),BARD(1),BVEC,D,S,IGNL)` (27)； `      END SELECT` (28)； `      END` (30)。 [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 8–28: 바깥 ITYP 선택과 안쪽 NNP 선택에는 CASE DEFAULT가 없다.
