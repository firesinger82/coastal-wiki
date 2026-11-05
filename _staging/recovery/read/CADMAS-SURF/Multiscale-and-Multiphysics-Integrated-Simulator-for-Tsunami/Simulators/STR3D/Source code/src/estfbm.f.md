---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/estfbm.f
lines: 48
sha256: 4d66802430d33b48517651bc8dcc167196d427d5e7e724232005887f8a874667
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# estfbm.f — 판독 구간 기록

구간은 1행부터 48행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | 해석: 보(beam) 강성 계산 루틴의 선언·3점 적분표 포함·국소좌표 준비 구간이다. LCCBM과 DERXBM0를 호출하고 ESTF를 0으로 초기화한다. 원문: `      SUBROUTINE ESTFBM(ESTF,GRID,UG,VG,NP,D1,D2,V,D,S,IGNL)` (1)； `      IMPLICIT REAL*8(A-H,O-Z)` (3)； 연속문(5–9): `      DIMENSION TE(3,3),U(3,2),VS(3,2),VT(3,2),VST(3,2),VTT(3,2)` (5)； `     &         ,AS(3,3,2),AT(3,3,2),GRID(3,*),UG(6,*),VG(3,2,2),NP(2)` (6)； `     &         ,V(3),BX(3,12),BY(3,12),BZ(3,12),UX(3),UY(3),UZ(3)` (7)； `     &         ,B(3,12),D(6,3,3),S(3,3,3),BTD(12,3),BTDB(78),E(78,3)` (8)； `     &         ,SE(78),ESTF(78),WK(144)` (9)； `      INCLUDE 'gauss_ln_3.h'` (11)； `      CALL LCCBM(RL,TE,U,VST,VTT,AS,AT,VS,VT,GRID,UG,VG,NP,V,IGNL)` (13)； `      CALL DERXBM0(BY,BZ,UY,UZ,VS,VT,AS,AT)` (15)； `      ESTF(:) = 0.` (17)。 [11-04 전수 검증 정정] |
| 19–48 | 시작 시 1행 ESTFBM 루틴 안이다. I·J 적분 루프에서 DERXBM·BLMBM·MATML을 호출한다. IGNL이 양수이면 ETABM을 호출하고 S와 E로 SE를 계산한다. ELSE에서는 SE를 0으로 한다. ESTF 누적 뒤 STFGL을 호출한다. 해석: S는 응력이고 WGT는 적분 가중치이다. 해석: STFGL은 좌표를 변환한다. 원문: `      DO I = 1, 3` (19)； `      DO J = 1, 3` (20)； `        SG = XG(I,3)` (22)； `        TG = XG(J,3)` (23)； `        WGT = WG(I,3)*WG(J,3)` (24)； `        CALL DERXBM(BX,UX,SG,TG,RL,D1,D2,U,VS,VT,AS,AT)` (26)； `        CALL BLMBM(B,BX,BY,BZ,UX,UY,UZ,IGNL)` (28)； `        CALL MATML(BTD,2,B,3,D(1,I,J),1,12,3,3)` (29)； `        CALL MATML(BTDB,1,BTD,2,B,2,12,12,3)` (30)； `        IF( IGNL > 0 ) THEN` (32)； `          CALL ETABM(E,SG,TG,RL,D1,D2,VST,VTT,BX,BY,BZ,UX,UY,UZ)` (33)； 연속문(34–35): `          SE(:) = S(1,I,J) * E(:,1) + 2.D0 * S(2,I,J) * E(:,2)` (34)； `     &                              + 2.D0 * S(3,I,J) * E(:,3)` (35)； `        ELSE` (36)； `          SE(:) = 0.` (37)； `        ENDIF` (38)； 연속문(40–41): `        ESTF(:) = ESTF(:) ` (40)； `     &            + ( BTDB(:) + SE(:) ) * WGT * D1 * D2 * RL * .25D0` (41)； `      ENDDO` (43)； `      ENDDO` (44)； `      CALL STFGL(ESTF,WK,TE,12,3)` (46)； `      END` (48)。 [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 19–24: 적분점 수는 두 방향 각각 3으로 고정된다.
- 32–38: S와 E로 SE를 계산하는 분기는 `IGNL > 0`인 경우에만 실행한다. [11-04 전수 검증 정정]
