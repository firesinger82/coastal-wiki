---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_cinit.f
lines: 56
sha256: 40ee669255f1e16c74955c77a3167ccc99c5ea62175ec151fde7a81c0130097d
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_cinit.f — 판독 구간 기록

구간은 1행부터 56행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–32 | SF_CINIT의 입구는 1–5행 연속 문장이다. IMPLICIT·INCLUDE와 14–31행의 배열 선언을 보존한다. 아래 인수 배열을 선언한다. 해석: 이름과 후속 호출로 보면 이 배열들은 유체장과 경계 자료의 초기화에 쓰이는 것으로 보인다. 이 구간에는 개별 배열의 물리적 용도를 설명하는 주석이 없다. 원문: `      SUBROUTINE SF_CINIT(XX,YY,ZZ,UU,VV,WW,PP,FF,FX,FY,FZ,ANU,GGV,GGX` (1); `     &                   ,GGY,GGZ,BCU,BCV,BCW,BCP,BCF,BCVI,DMTBTT,DMTBZZ` (2); `     &                   ,DMTBHH,DMTBUN,DMTBUT,DBUF,WK01,WK02,WK03,NF` (3); `     &                   ,INDX,INDY,INDZ,INDB,INDS,IBUF,NFP,INDXP,INDYP` (4); `     &                   ,INDZP,GGXP,GGYP,GGZP)` (5); `      IMPLICIT REAL*8(A-H,O-Z)` (7); `      INCLUDE 'VF_A0PRM.h'` (9); `      INCLUDE 'VF_AFILEI.h'` (10); `      INCLUDE 'VF_ANUMBI.h'` (11); `      INCLUDE 'VF_APARAI.h'` (12); `      DIMENSION XX(MAXG1,NUMI),YY(MAXG1,NUMJ),ZZ(MAXG1,NUMK)` (14); `     &         ,UU(NUMI,NUMJ,NUMK),VV(NUMI,NUMJ,NUMK),WW(NUMI,NUMJ,NUMK)` (15); `     &         ,PP(NUMI,NUMJ,NUMK),FF(NUMI,NUMJ,NUMK),FX(NUMI,NUMJ,NUMK)` (16); `     &         ,FY(NUMI,NUMJ,NUMK),FZ(NUMI,NUMJ,NUMK),BCU(NUMB,3)` (17); `     &         ,BCV(NUMB,3),BCW(NUMB,3),BCP(NUMB),BCF(NUMB),BCVI(NUMB)` (18); `     &         ,DMTBTT(MTBTT),DMTBZZ(MTBZZ),DMTBHH(MTBTT)` (19); `     &         ,DMTBUN(MTBZZ,MTBTT),DMTBUT(MTBZZ,MTBTT),DBUF(*),IBUF(*)` (20); `     &         ,WK01(NUMI,NUMJ,NUMK),WK02(NUMI,NUMJ,NUMK)` (21); `     &         ,WK03(NUMI,NUMJ,NUMK),NF(NUMI,NUMJ,NUMK)` (22); `     &         ,INDX(NUMI,NUMJ,NUMK),INDY(NUMI,NUMJ,NUMK)` (23); `     &         ,INDZ(NUMI,NUMJ,NUMK),INDS(NUMI*NUMJ*NUMK)` (24); `     &         ,INDB(MAXB1,NUMB),NFP(NUMI,NUMJ,NUMK)` (25); `     &         ,INDXP(NUMI,NUMJ,NUMK),INDYP(NUMI,NUMJ,NUMK)` (26); `     &         ,INDZP(NUMI,NUMJ,NUMK),ANU(NUMI,NUMJ,NUMK)` (27); `     &         ,GGX(NUMI,NUMJ,NUMK),GGY(NUMI,NUMJ,NUMK)` (28); `     &         ,GGZ(NUMI,NUMJ,NUMK),GGV(NUMI,NUMJ,NUMK)` (29); `     &         ,GGXP(NUMI,NUMJ,NUMK),GGYP(NUMI,NUMJ,NUMK)` (30); `     &         ,GGZP(NUMI,NUMJ,NUMK)` (31) [11-04 전수 검증 정정] |
| 33–44 | 시작 시 1행 SF_CINIT 루틴 안이다. SF_RESET_UU의 넷째 인수로 각각 1·2·3을 전달한다. SF_RESET_FF의 첫째 인수로 PP와 FF를 각각 전달한 뒤 VF_BWFF·VF_FNFINI·VF_FNFPRV·VF_CFXYZ를 순서대로 호출한다. 호출 루틴 내부는 이 파일의 판독 범위가 아니다. 원문: `      CALL SF_RESET_UU(UU,INDXP,INDX,1,DBUF)` (33); `      CALL SF_RESET_UU(VV,INDYP,INDY,2,DBUF)` (34); `      CALL SF_RESET_UU(WW,INDZP,INDZ,3,DBUF)` (35); `      CALL SF_RESET_FF(PP,NFP,NF,DBUF)` (37); `      CALL SF_RESET_FF(FF,NFP,NF,DBUF)` (38); `      CALL VF_BWFF(FF,BCF,INDB)` (40); `      CALL VF_FNFINI(FF,BCF,NF,INDX,INDY,INDZ,INDS,IBUF)` (41); `      CALL VF_FNFPRV(FF,BCF,NF,INDX,INDY,INDZ,INDS,IBUF)` (42); `      CALL VF_CFXYZ(XX,YY,ZZ,FF,FX,FY,FZ,GGV,DBUF,NF,INDX,INDY,INDZ)` (43) [11-04 전수 검증 정정] |
| 45–56 | 시작 시 1행 SF_CINIT 루틴 안이다. SF_MDFXYZ의 45–46행과 VF_BWUWN의 48–50행은 각각 한 연속 호출이다. 그 뒤 VF_BWUWT와 VF_BWPP를 호출한다. 이 루틴 자체에는 조건문이나 DO 루프가 없다. 원문: `      CALL SF_MDFXYZ(FX,FY,FZ,INDX,INDY,INDZ,GGX,GGY,GGZ,GGXP,GGYP,GGZP` (45); `     &              ,DBUF)` (46); `      CALL VF_BWUWN(XX,YY,ZZ,UU,VV,WW,FF,BCU,BCV,BCW,BCF` (48); `     &             ,DMTBTT,DMTBZZ,DMTBHH,DMTBUN,DMTBUT,DBUF` (49); `     &             ,WK01,WK02,WK03,NF,INDX,INDY,INDB)` (50); `      CALL VF_BWUWT(XX,YY,ZZ,UU,VV,WW,ANU,BCU,BCV,BCW,BCF,BCVI,INDB)` (52); `      CALL VF_BWPP(PP,BCP,INDB)` (54); `      END` (56) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 17–18: BCU·BCV·BCW는 (NUMB,3)으로 선언되고 BCP는 (NUMB)으로 선언된다. [11-04 전수 검증 정정]
