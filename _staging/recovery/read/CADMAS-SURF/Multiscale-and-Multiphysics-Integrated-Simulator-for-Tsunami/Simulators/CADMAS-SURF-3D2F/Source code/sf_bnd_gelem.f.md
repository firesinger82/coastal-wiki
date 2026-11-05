---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_bnd_gelem.f
lines: 43
sha256: a3ad2bab0c5cc33a423ceb1ee8e21c6abeb518d21fed5ebce0afaa554aa567c8
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_bnd_gelem.f — 판독 구간 기록

구간은 1행부터 43행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–26 | 암시적 배정밀도(double precision)·포함 헤더·GELM·IELM·XX·YY·ZZ·GBND 배열을 선언한다. `SELECT CASE( ID )` (12)에 따라 GBND 성분을 아래 식으로 계산한다. 해석: XX·YY·ZZ의 첫째 성분을 격자선 좌표로 보면 GBND는 ID에 대응하는 경계면의 중심 좌표이다. 원문: `      SUBROUTINE SF_BND_GELEM(IEB,ID,I,J,K,XX,YY,ZZ,GELM,IELM)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      INCLUDE 'VF_A0PRM.h'` (5); `      INCLUDE 'VF_ANUMBI.h'` (6); `      INCLUDE 'SF_STRUCT.h'` (7); `      DIMENSION GELM(3,NELM),IELM(24,NELM),XX(MAXG1,NUMI),YY(MAXG1,NUMJ)` (9); `     &         ,ZZ(MAXG1,NUMK),GBND(3)` (10); `      SELECT CASE( ID )` (12); `      CASE( 1 )` (13); `        GBND(1) = XX(1,I)` (14); `        GBND(2) = ( YY(1,J) + YY(1,J+1) ) * .5D0` (15); `        GBND(3) = ( ZZ(1,K) + ZZ(1,K+1) ) * .5D0` (16); `      CASE( 2 )` (17); `        GBND(1) = ( XX(1,I) + XX(1,I+1) ) * .5D0` (18); `        GBND(2) = YY(1,J)` (19); `        GBND(3) = ( ZZ(1,K) + ZZ(1,K+1) ) * .5D0` (20); `      CASE( 3 )` (21); `        GBND(1) = ( XX(1,I) + XX(1,I+1) ) * .5D0` (22); `        GBND(2) = ( YY(1,J) + YY(1,J+1) ) * .5D0` (23); `        GBND(3) = ZZ(1,K)` (24); `      END SELECT` (25) [11-04 전수 검증 정정] |
| 27–43 | 시작 시 1행 SF_BND_GELEM 루틴 안이다. `DIST_MIN = 1.D20` (27)으로 시작한다. `DO IE = 1, NELM` (29)에서 SF_LENGTH가 반환한 DIST가 현재 DIST_MIN보다 작을 때만 DIST_MIN과 I_MIN을 갱신한다. 해석: SF_LENGTH가 두 점의 거리를 반환한다면 이 과정은 최근접 요소 번호 탐색이다. 그 요소의 IELM(2,I_MIN)==1이면 IEB에 번호를 반환하고 ELSE는 0을 반환한다. 원문: `      DIST_MIN = 1.D20` (27); `      DO IE = 1, NELM` (29); `        CALL SF_LENGTH(DIST,GBND,GELM(1,IE),3)` (30); `        IF( DIST < DIST_MIN ) THEN` (31); `          DIST_MIN = DIST` (32); `          I_MIN = IE` (33); `        ENDIF` (34); `      ENDDO` (35); `      IF( IELM(2,I_MIN) == 1 ) THEN` (37); `        IEB = I_MIN` (38); `      ELSE` (39); `        IEB = 0` (40); `      ENDIF` (41); `      END` (43) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 12–25: SELECT CASE에는 ID=1·2·3만 있고 CASE DEFAULT는 없다.
- 27–37: I_MIN 대입은 거리 DIST가 1.D20보다 작은 경우에만 있다. NELM=0 또는 해당 비교가 한 번도 참이 되지 않는 경우를 처리하는 별도 분기는 없다.
