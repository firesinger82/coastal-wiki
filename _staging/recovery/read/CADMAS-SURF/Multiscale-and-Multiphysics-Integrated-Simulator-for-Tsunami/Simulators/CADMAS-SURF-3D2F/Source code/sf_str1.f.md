---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_str1.f
lines: 51
sha256: 6289bcc8267dc37f69a049278a744f127fc7fdc625872590ab7e76a2e278fd72
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_str1.f — 판독 구간 기록

구간은 1행부터 51행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | SF_STR1 시작. 모듈·INCLUDE·암시적 실수 선언을 적는다(1–10). ICPL=1이면 SF_PRSINI를 호출한다(12). IENS에 0을 대입한다(14). IENS=1이면 SF_ENS_GEOM을 호출하는 조건이 있다(15). ISTM=1이면 SF_DPTH_INIT을 호출한다(17). 해석: 호출 이름으로 볼 때 압력 초기화·형상 출력·수심 초기화에 해당한다. 원문(연속행은 아래 행 번호 순서로 이어지는 한 문장): `      SUBROUTINE SF_STR1(DT)` (1)<br>`      USE VF_A2ARRAY` (3)<br>`      USE SF_ARRAY` (4)<br>`      IMPLICIT REAL*8(A-H,O-Z)` (6)<br>`      INCLUDE 'VF_A0PRM.h'` (8)<br>`      INCLUDE 'VF_AFILEI.h'` (9)<br>`      INCLUDE 'SF_STRUCT.h'` (10)<br>`      IF( ICPL == 1 ) CALL SF_PRSINI(IPFACE0,AFC,IPGRID0,IPND0,ZZ)` (12)<br>`      IENS=0` (14)<br>`      IF( IENS == 1 ) CALL SF_ENS_GEOM(XX,YY,ZZ)` (15)<br>`      IF( ISTM == 1 ) CALL SF_DPTH_INIT(XX,YY,ZZ,FF,GGW,GGR,NF)` (17) [11-04 전수 검증 정정] |
| 19–37 | 시작 시 1행 루틴 안. IRETYP>0이면 ICPL=2의 면 전송 후 재시작을 읽는다. ICPL=2의 ELSEIF에서는 위치 초기화·면 갱신·MODE=1의 SF_STR_OBST·면 후처리와 할당을 수행한다(19–37). 원문(연속행은 아래 행 번호 순서로 이어지는 한 문장): `      IF( IRETYP > 0 ) THEN` (19)<br>`        IF( ICPL == 2 )` (20)<br>`     &    CALL SF_SEND_SURF(IPND0,IPFACE0,AFC,IPGRID0,ZZ,IRFACE,IRGRID0)` (21)<br>`        CALL SF_RD_RESTART(DT)` (22)<br>`      ELSEIF( ICPL == 2 ) THEN` (23)<br>`        CALL SF_POS_INIT(POS,POS2,DVEL,DVEL2,POS0,POS20,DVEL20,IPND0` (24)<br>`     &                  ,PRES0,IPFACE0,AFC,IPGRID,IPGRID0,IRFACE,IRGRID0` (25)<br>`     &                  ,IGNO,IENO,ZZ,NF,PP,DZ)` (26)<br>`        CALL SF_PFACE1()` (27)<br>`        CALL SF_PFACE3()` (28)<br>`        CALL SF_STR_OBST(GGV,GGX,GGY,GGZ,GGW,GGR,GLV,GLX,GLY,GLZ,NF,INDC` (29)<br>`     &                  ,INDX,INDY,INDZ,SPC,LNDC_0,LNDC0,LNDC,KST,GGV_0` (30)<br>`     &                  ,GGX_0,GGY_0,GGZ_0,XX,YY,ZZ,CM0,SUMZ,IELM,POS` (31)<br>`     &                  ,POR,1,WK01,WK02,WK03,WK04,WK05,WK06,WK07,WK08` (32)<br>`     &                  ,WK09,WK10,WK11,WK12,WK13,DBUF,WK14,WK15,WK16` (33)<br>`     &                  ,WK17,WK18,WK19,WK20)` (34)<br>`        CALL SF_PFACE2()` (35)<br>`        IF( ISTM == 1 ) CALL SF_RFACE2()` (36)<br>`        CALL SF_ALLOC1()` (37) |
| 38–51 | 시작 시 19행 `IF( IRETYP > 0 ) THEN`의 23행 `ELSEIF( ICPL == 2 ) THEN` 분기 안이다. 이 분기는 IRETYP>0이 거짓일 때만 검사한다. ELSE는 없다. 이 IF는 49행 `ENDIF`에서 닫힌다. SF_BC_RESET과 SF_CINIT 호출 뒤 분기·루틴을 닫는다(38–51). 원문(연속행은 아래 행 번호 순서로 이어지는 한 문장): `        CALL SF_BC_RESET(INDB,INDBK,INDBE,INDBT,INDBC,BCU,BCV,BCW,BCP` (38)<br>`     &                  ,BCF,BCVI,BCK,BCE,BCT,BCTI,BCC,BCCI,GGX,GGY` (39)<br>`     &                  ,GGZ,GLX,GLY,GLZ,NF,INDX,INDY,INDZ,INDX0,INDY0` (40)<br>`     &                  ,INDZ0,INDB0,INDBK0,INDBE0,INDBT0,INDBC0,BCU0` (41)<br>`     &                  ,BCV0,BCW0,BCP0,BCF0,BCVI0,BCK0,BCE0,BCT0` (42)<br>`     &                  ,BCTI0,BCC0,BCCI0,XX,YY,ZZ,IELM,POS,DVEL)` (43)<br>`        CALL SF_CINIT(XX,YY,ZZ,UU,VV,WW,PP,FF,FX,FY,FZ,ANU,GGV,GGX,GGY` (44)<br>`     &               ,GGZ,BCU,BCV,BCW,BCP,BCF,BCVI,DMTBTT,DMTBZZ,DMTBHH` (45)<br>`     &               ,DMTBUN,DMTBUT,DBUF,WK01,WK02,WK03,NF,INDX,INDY` (46)<br>`     &               ,INDZ,INDB,INDS,IBUF,WK14,WK15,WK16,WK17,WK18,WK19` (47)<br>`     &               ,WK20)` (48)<br>`      ENDIF` (49)<br>`      END` (51) [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 14–15: IENS에 0을 대입한 직후 IENS==1일 때 SF_ENS_GEOM을 호출하는 조건이 있다.
