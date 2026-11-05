---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/enpfrc.f
lines: 30
sha256: fcc556c2b2b9c650ccafae7e0c6fc38cf631382f36e20cebefa2eba49aa899fe
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# enpfrc.f — 판독 구간 기록

구간은 1행부터 30행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | ENPFRC의 인수와 암시적 형 및 배열 크기를 선언한다. FC·EPS·S·GRID·UG를 ENPFTE1에 전달하는 문장은 12행이다. 해당 인수의 등가절점력·변형률·응력·절점좌표·절점변위 설명은 `enpfte1.f:3–7`에 있다. 원문: `      SUBROUTINE ENPFRC(FC,EPS,S,GRID,UG,VG,ITYP,NP,NNP,RODA,BARD,BVEC,D`<br>`     &                 ,IGNL,ITO)` (1–2); `      IMPLICIT REAL*8(A-H,O-Z)` (4); `      DIMENSION FC(*),EPS(*),S(*),GRID(3,*),UG(6,*),NP(NNP),D(*)`<br>`     &         ,VG(3,2,2),BARD(*),BVEC(3)` (5–6). [11-04 전수 검증 보완] |
| 8–23 | 시작 시 1–2행 ENPFRC 루틴 안. ITYP 2·6에서는 NNP의 4·10·6·15·8·20에 따라 ENPFTE1·ENPFTE2·ENPFPN1·ENPFPN2·ENPFHX1·ENPFHX2를 호출한다. 원문: `      SELECT CASE( ITYP )` (8); `      CASE( 2, 6 )` (9); `        SELECT CASE( NNP )` (10); `        CASE( 4 )` (11); `          CALL ENPFTE1(FC,EPS,S,GRID,UG,NP,D,IGNL,ITO)` (12); `        CASE( 10 )` (13); `          CALL ENPFTE2(FC,EPS,S,GRID,UG,NP,D,IGNL,ITO)` (14); `        CASE( 6 )` (15); `          CALL ENPFPN1(FC,EPS,S,GRID,UG,NP,D,IGNL,ITO)` (16); `        CASE( 15 )` (17); `          CALL ENPFPN2(FC,EPS,S,GRID,UG,NP,D,IGNL,ITO)` (18); `        CASE( 8 )` (19); `          CALL ENPFHX1(FC,EPS,S,GRID,UG,NP,D,IGNL,ITO)` (20); `        CASE( 20 )` (21); `          CALL ENPFHX2(FC,EPS,S,GRID,UG,NP,D,IGNL,ITO)` (22); `        END SELECT` (23). |
| 24–30 | 시작 시 8행 `      SELECT CASE( ITYP )` 안이다. 이 SELECT는 28행 `      END SELECT`에서 닫힌다. ITYP 3은 ENPFTRS를 호출한다. ITYP 4는 ENPFBM에 BARD(2), BARD(1), BVEC 순서로 값을 전달한다. 해석: BARD(2)와 BARD(1)은 치수이다. SELECT와 루틴 끝을 포함한다. 원문: `      CASE( 3 )` (24); `        CALL ENPFTRS(FC,EPS,S,GRID,UG,NP,RODA,D,IGNL)` (25); `      CASE( 4 )` (26); `        CALL ENPFBM(FC,EPS,S,GRID,UG,VG,NP,BARD(2),BARD(1),BVEC,D,IGNL)` (27); `      END SELECT` (28); `      END` (30). [11-04 전수 검증 보완] [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 8–28: ITYP와 NNP의 두 SELECT CASE에는 CASE DEFAULT가 없다. 해당 CASE가 없으면 힘 계산 루틴을 호출하지 않는다.
