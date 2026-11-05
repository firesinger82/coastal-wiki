---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_stm_obst.f
lines: 53
sha256: a53ba124e1e6fdcea84e729e97de69967eac91eebe71cd5c48a891be08a63f95
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_stm_obst.f — 판독 구간 기록

구간은 1행부터 53행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–27 | SF_STM_OBST의 선언부다. GGV·GGX·GGY·GGZ 등 12–26행에 인용한 3차원 배열의 크기는 NUMI·NUMJ·NUMK다. KST·SUMZ는 NUMI·NUMJ이고 DBUF는 NUMBUF*MAXBUF다(21·26). 원문(연속 표시는 앞 문장에 이어짐): `      SUBROUTINE SF_STM_OBST(GGV,GGX,GGY,GGZ,GGW,GLV,GLX,GLY,GLZ,NF` (1); `     &                      ,INDC,INDX,INDY,INDZ,KST,GGV_0,GGX_0,GGY_0` (2); `     &                      ,GGZ_0,XX,YY,ZZ,CM0,SUMZ,MODE,WK01,DBUF,NFP` (3); `     &                      ,INDXP,INDYP,INDZP,GGXP,GGYP,GGZP)` (4); `      IMPLICIT REAL*8(A-H,O-Z)` (6); `      INCLUDE 'VF_A0PRM.h'` (8); `      INCLUDE 'VF_ANUMBI.h'` (9); `      INCLUDE 'VF_APARAI.h'` (10); `      DIMENSION GGV(NUMI,NUMJ,NUMK),GGX(NUMI,NUMJ,NUMK)` (12); `     &         ,GGY(NUMI,NUMJ,NUMK),GGZ(NUMI,NUMJ,NUMK)` (13); `     &         ,GGW(NUMI,NUMJ,NUMK),GGV_0(NUMI,NUMJ,NUMK)` (14); `     &         ,GGX_0(NUMI,NUMJ,NUMK),GGY_0(NUMI,NUMJ,NUMK)` (15); `     &         ,GGZ_0(NUMI,NUMJ,NUMK),XX(MAXG1,NUMI),YY(MAXG1,NUMJ)` (16); `     &         ,ZZ(MAXG1,NUMK),WK01(NUMI,NUMJ,NUMK),INDX(NUMI,NUMJ,NUMK)` (17); `     &         ,INDY(NUMI,NUMJ,NUMK),INDZ(NUMI,NUMJ,NUMK)` (18); `     &         ,NF(NUMI,NUMJ,NUMK),GLV(NUMI,NUMJ,NUMK)` (19); `     &         ,GLX(NUMI,NUMJ,NUMK),GLY(NUMI,NUMJ,NUMK)` (20); `     &         ,GLZ(NUMI,NUMJ,NUMK),DBUF(NUMBUF*MAXBUF)` (21); `     &         ,CM0(NUMI,NUMJ,NUMK),INDC(NUMI,NUMJ,NUMK)` (22); `     &         ,INDXP(NUMI,NUMJ,NUMK),INDYP(NUMI,NUMJ,NUMK)` (23); `     &         ,INDZP(NUMI,NUMJ,NUMK),NFP(NUMI,NUMJ,NUMK)` (24); `     &         ,GGXP(NUMI,NUMJ,NUMK),GGYP(NUMI,NUMJ,NUMK)` (25); `     &         ,GGZP(NUMI,NUMJ,NUMK),KST(NUMI,NUMJ),SUMZ(NUMI,NUMJ)` (26). [11-04 전수 검증 정정] |
| 28–42 | 시작 시 1행 SF_STM_OBST 루틴 안. SF_STM_OBST 안. NF·INDX·INDY·INDZ와 GGX·GGY·GGZ를 이전 상태 배열에 복사한다(28–36). GGV·GGX·GGY·GGZ에 각각 GGV_0·GGX_0·GGY_0·GGZ_0를 복사한다(38–41). 원문(연속 표시는 앞 문장에 이어짐): `      NFP = NF` (28); `      INDXP = INDX` (30); `      INDYP = INDY` (31); `      INDZP = INDZ` (32); `      GGXP = GGX` (34); `      GGYP = GGY` (35); `      GGZP = GGZ` (36); `      GGV = GGV_0` (38); `      GGX = GGX_0` (39); `      GGY = GGY_0` (40); `      GGZ = GGZ_0` (41). 해석: GGV는 공극률 배열로 읽힌다. 해석: GGX·GGY·GGZ는 면 배열로 읽힌다. [11-04 전수 검증 정정] |
| 43–53 | 시작 시 1행 SF_STM_OBST 루틴 안. SF_STM_OBST 안이며 상태 복사 뒤다. SF_MDPORO_H에 MODE를 전달한다(43–44). SF_INDX_RESET에 INDX·INDY·INDZ·NF·GGX·GGY·GGZ를 전달한다(46). 이후 VF_CGLV와 VF_CGLXYZ를 차례로 호출한다(48–51). 호출 인수와 고정형식 연속문을 그대로 적는다. 원문(연속 표시는 앞 문장에 이어짐): `      CALL SF_MDPORO_H(GGV,GGX,GGY,GGZ,GGW,KST,NF,INDC,ZZ,SUMZ,MODE` (43); `     &                ,WK01,DBUF)` (44); `      CALL SF_INDX_RESET(INDX,INDY,INDZ,NF,GGX,GGY,GGZ)` (46); `      CALL VF_CGLV(CM0,GGV,GLV,NF)` (48); `      CALL VF_CGLXYZ(XX,YY,ZZ,CM0,GGX,GGY,GGZ,GLX,GLY,GLZ,DBUF,NF,INDX` (50); `     &              ,INDY,INDZ)` (51); `      END` (53). 해석: SF_INDX_RESET은 면 인덱스를 갱신하는 루틴으로 읽힌다. 해석: VF_CGLV와 VF_CGLXYZ는 GLV·GLX·GLY·GLZ를 계산하는 루틴으로 읽힌다. [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
