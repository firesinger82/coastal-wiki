---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_mdfxyz.f
lines: 42
sha256: 8f667a096f711e489d71731c8b6ffb46ddb654d3cdb34c40b8dab3d1c48a5cdf
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_mdfxyz.f — 판독 구간 기록

구간은 1행부터 42행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–42 | SF_MDFXYZ 선언, INCLUDE 네 개와 배열 범위(1–16). K=2:NUMK-1 및 국소 수평 셀을 순회한다(18–36). 각 방향에서 IND*=0, GG*와 GG*P의 불일치, GG*<GMIN, F*<FMIN의 네 조건을 모두 만족하면 해당 FX·FY·FZ를 FMIN으로 올린다(22–32). 여기서 *는 X·Y·Z 중 해당 방향이다. VF_P3SRD2의 세 번째 인수로 각각 1·2·3을 전달한다(38–40). 해석: GG*는 현재 면 공극률이고 GG*P는 이전 값이며 F*는 면 VOF 함수다. 원문: 연속문: `      SUBROUTINE SF_MDFXYZ(FX,FY,FZ,INDX,INDY,INDZ,GGX,GGY,GGZ,GGXP,GGYP` (1); `     &                    ,GGZP,DBUF)` (2)<br>`      IMPLICIT REAL*8(A-H,O-Z)` (4)<br>`      INCLUDE 'VF_A0PRM.h'` (6)<br>`      INCLUDE 'VF_ANUMBI.h'` (7)<br>`      INCLUDE 'VF_APARAI.h'` (8)<br>`      INCLUDE 'SF_STRUCT.h'` (9)<br>연속문: `      DIMENSION FX(NUMI,NUMJ,NUMK),FY(NUMI,NUMJ,NUMK),FZ(NUMI,NUMJ,NUMK)` (11); `     &         ,GGX(NUMI,NUMJ,NUMK),GGY(NUMI,NUMJ,NUMK)` (12); `     &         ,GGZ(NUMI,NUMJ,NUMK),INDX(NUMI,NUMJ,NUMK)` (13); `     &         ,INDY(NUMI,NUMJ,NUMK),INDZ(NUMI,NUMJ,NUMK),DBUF(*)` (14); `     &         ,GGXP(NUMI,NUMJ,NUMK),GGYP(NUMI,NUMJ,NUMK)` (15); `     &         ,GGZP(NUMI,NUMJ,NUMK)` (16)<br>`      DO K = 2, NUMK - 1` (18)<br>`        DO J = MYJS, MYJE` (19)<br>`          DO I = MYIS, MYIE` (20)<br>연속문: `            IF( INDX(I,J,K) == 0 .AND. GGX(I,J,K) /= GGXP(I,J,K) .AND.` (22); `     &          GGX(I,J,K) < GMIN .AND. FX(I,J,K) < FMIN )` (23); `     &        FX(I,J,K) = FMIN` (24)<br>연속문: `            IF( INDY(I,J,K) == 0 .AND. GGY(I,J,K) /= GGYP(I,J,K) .AND.` (26); `     &          GGY(I,J,K) < GMIN .AND. FY(I,J,K) < FMIN )` (27); `     &        FY(I,J,K) = FMIN` (28)<br>연속문: `            IF( INDZ(I,J,K) == 0 .AND. GGZ(I,J,K) /= GGZP(I,J,K) .AND.` (30); `     &          GGZ(I,J,K) < GMIN .AND. FZ(I,J,K) < FMIN )` (31); `     &        FZ(I,J,K) = FMIN` (32)<br>`          ENDDO` (34)<br>`        ENDDO` (35)<br>`      ENDDO` (36)<br>`      CALL VF_P3SRD2(FX,DBUF,1)` (38)<br>`      CALL VF_P3SRD2(FY,DBUF,2)` (39)<br>`      CALL VF_P3SRD2(FZ,DBUF,3)` (40)<br>`      END` (42) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
