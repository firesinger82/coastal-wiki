---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_str2.f
lines: 45
sha256: faab272bf4dc21b260329e22d61947804a409562d25388d19de6b85b128af58e
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_str2.f — 판독 구간 기록

구간은 1행부터 45행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | SF_STR2 시작. 모듈과 시간·구조 INCLUDE를 사용한다. ISTM=1이면 SF_DPTH_UPDATE를 호출한다(11–13). SF_POS_UPDATE1은 이 조건 밖에서 호출한다(14–16). 해석: SF_DPTH_UPDATE는 이름으로 볼 때 수심 갱신 호출이다. 원문(연속행은 아래 행 번호 순서로 이어지는 한 문장): `      SUBROUTINE SF_STR2(DT,DTO)` (1)<br>`      USE VF_A2ARRAY` (3)<br>`      USE SF_ARRAY` (4)<br>`      IMPLICIT REAL*8(A-H,O-Z)` (6)<br>`      INCLUDE 'VF_ATIMER.h'` (8)<br>`      INCLUDE 'SF_STRUCT.h'` (9)<br>`      IF( ISTM == 1 )` (11)<br>`     &  CALL SF_DPTH_UPDATE(DZ,SUMZ,XX,YY,ZZ,UU,VV,FF,FX,FY,GGX,GGY,GGW` (12)<br>`     &                     ,GGR,LNDC,NF,INDX,INDY,FLFU,FLFV,DT,DTO)` (13)<br>`      CALL SF_POS_UPDATE1(IPND0,PRES0,DELZ0,IFIX0,GRID,POS,IPGRID` (14)<br>`     &                   ,IPGRID0,IRGRID,IELM,IGNO,XX,YY,ZZ,NF,PP,DZ` (15)<br>`     &                   ,LNDC0,DT)` (16) [11-04 전수 검증 정정] |
| 17–32 | 시작 시 1행 루틴 안. TNOW+DT와 TSTR2 및 IPART 조건으로 장애물을 갱신한다. SF_POS_UPDATE2·면 갱신·MODE=2의 SF_STR_OBST·ISTM 조건의 SF_RFACE2·할당을 수행한다(17–32). 원문(연속행은 아래 행 번호 순서로 이어지는 한 문장): `      IF( TNOW + DT > TSTR2 .AND. IPART == 1 ) CALL SF_UPDT_OBST()` (17)<br>`      CALL SF_POS_UPDATE2(POS,POS1,POS2,DVEL,DVEL1,DVEL2,POS0,POS10` (18)<br>`     &                   ,POS20,DVEL10,DVEL20,SPC,IPND0,PRES0,DELZ0` (19)<br>`     &                   ,IFIX0,GRDL,IGFC,IELM,AFC,IGNO,IENO,XX,YY,ZZ` (20)<br>`     &                   ,DT)` (21)<br>`      CALL SF_PFACE1()` (22)<br>`      CALL SF_PFACE3()` (23)<br>`      CALL SF_STR_OBST(GGV,GGX,GGY,GGZ,GGW,GGR,GLV,GLX,GLY,GLZ,NF,INDC` (24)<br>`     &                ,INDX,INDY,INDZ,SPC,LNDC_0,LNDC0,LNDC,KST,GGV_0` (25)<br>`     &                ,GGX_0,GGY_0,GGZ_0,XX,YY,ZZ,CM0,SUMZ,IELM,POS,POR` (26)<br>`     &                ,2,WK01,WK02,WK03,WK04,WK05,WK06,WK07,WK08,WK09` (27)<br>`     &                ,WK10,WK11,WK12,WK13,DBUF,WK14,WK15,WK16,WK17,WK18` (28)<br>`     &                ,WK19,WK20)` (29)<br>`      CALL SF_PFACE2()` (30)<br>`      IF( ISTM == 1 ) CALL SF_RFACE2()` (31)<br>`      CALL SF_ALLOC1()` (32) |
| 33–45 | 시작 시 1행 루틴 안. SF_BC_RESET과 SF_CINIT을 호출하고 종료한다(33–45). 원문(연속행은 아래 행 번호 순서로 이어지는 한 문장): `      CALL SF_BC_RESET(INDB,INDBK,INDBE,INDBT,INDBC,BCU,BCV,BCW,BCP` (33)<br>`     &                ,BCF,BCVI,BCK,BCE,BCT,BCTI,BCC,BCCI,GGX,GGY` (34)<br>`     &                ,GGZ,GLX,GLY,GLZ,NF,INDX,INDY,INDZ,INDX0,INDY0` (35)<br>`     &                ,INDZ0,INDB0,INDBK0,INDBE0,INDBT0,INDBC0,BCU0` (36)<br>`     &                ,BCV0,BCW0,BCP0,BCF0,BCVI0,BCK0,BCE0,BCT0` (37)<br>`     &                ,BCTI0,BCC0,BCCI0,XX,YY,ZZ,IELM,POS,DVEL)` (38)<br>`      CALL SF_CINIT(XX,YY,ZZ,UU,VV,WW,PP,FF,FX,FY,FZ,ANU,GGV,GGX,GGY` (39)<br>`     &             ,GGZ,BCU,BCV,BCW,BCP,BCF,BCVI,DMTBTT,DMTBZZ,DMTBHH` (40)<br>`     &             ,DMTBUN,DMTBUT,DBUF,WK01,WK02,WK03,NF,INDX,INDY` (41)<br>`     &             ,INDZ,INDB,INDS,IBUF,WK14,WK15,WK16,WK17,WK18,WK19` (42)<br>`     &             ,WK20)` (43)<br>`      END` (45) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
