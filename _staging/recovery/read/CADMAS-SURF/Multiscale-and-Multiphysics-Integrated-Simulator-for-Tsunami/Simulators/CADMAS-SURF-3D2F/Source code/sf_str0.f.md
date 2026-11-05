---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_str0.f
lines: 35
sha256: 466198c20a8333981364c33ab86f945d91382f070ab1afb47372e446ede093ed
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_str0.f — 판독 구간 기록

구간은 1행부터 35행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | SF_STR0 시작. 두 배열 모듈·암시적 실수 선언 및 구조 INCLUDE를 적는다. 원문(연속행은 아래 행 번호 순서로 이어지는 한 문장): `      SUBROUTINE SF_STR0()` (1)<br>`      USE VF_A2ARRAY` (3)<br>`      USE SF_ARRAY` (4)<br>`      IMPLICIT REAL*8(A-H,O-Z)` (6)<br>`      INCLUDE 'SF_STRUCT.h'` (8) |
| 10–26 | 시작 시 1행 루틴 안. ICPL=2에서 SF_SEND_RST와 SF_RECV_CONT를 각각 호출한다(10,15). 11–26행의 나머지 호출은 인용된 순서를 따른다. SF_STR_OBST에는 정수 0을 전달한다(22). 해석: 호출 이름으로 볼 때 장애물 판독·면 준비·배열 할당을 수행하는 흐름이다. ISTM=1이면 SF_RFACE0을 호출한다. 원문(연속행은 아래 행 번호 순서로 이어지는 한 문장): `      IF(ICPL.EQ.2) CALL SF_SEND_RST()` (10)<br>`      CALL SF_RD_OBST()` (11)<br>`      CALL SF_PFACE0()` (12)<br>`      IF( ISTM == 1 ) CALL SF_RFACE0()` (13)<br>`      CALL SF_BCS_OBST()` (14)<br>`      IF(ICPL.EQ.2) CALL SF_RECV_CONT()` (15)<br>`      CALL SF_ALLOC0()` (16)<br>`      CALL SF_PFACE1()` (17)<br>`      CALL SF_PFACE3()` (18)<br>`      CALL SF_STR_OBST(GGV,GGX,GGY,GGZ,GGW,GGR,GLV,GLX,GLY,GLZ,NF,INDC` (19)<br>`     &                ,INDX,INDY,INDZ,SPC,LNDC_0,LNDC0,LNDC,KST,GGV_0` (20)<br>`     &                ,GGX_0,GGY_0,GGZ_0,XX,YY,ZZ,CM0,SUMZ,IELM,POS,POR` (21)<br>`     &                ,0,WK01,WK02,WK03,WK04,WK05,WK06,WK07,WK08,WK09` (22)<br>`     &                ,WK10,WK11,WK12,WK13,DBUF,WK14,WK15,WK16,WK17,WK18` (23)<br>`     &                ,WK19,WK20)` (24)<br>`      CALL SF_PFACE2()` (25)<br>`      CALL SF_ALLOC1()` (26) [11-04 전수 검증 정정] |
| 27–35 | 시작 시 1행 루틴 안. SF_BC_RESET을 호출한다(27–32). ICPL=1이면 SF_DEALLOC을 호출한다(33). 해석: SF_BC_RESET은 이름으로 볼 때 경계를 재설정하는 호출이다. 원문(연속행은 아래 행 번호 순서로 이어지는 한 문장): `      CALL SF_BC_RESET(INDB,INDBK,INDBE,INDBT,INDBC,BCU,BCV,BCW,BCP` (27)<br>`     &                ,BCF,BCVI,BCK,BCE,BCT,BCTI,BCC,BCCI,GGX,GGY` (28)<br>`     &                ,GGZ,GLX,GLY,GLZ,NF,INDX,INDY,INDZ,INDX0,INDY0` (29)<br>`     &                ,INDZ0,INDB0,INDBK0,INDBE0,INDBT0,INDBC0,BCU0` (30)<br>`     &                ,BCV0,BCW0,BCP0,BCF0,BCVI0,BCK0,BCE0,BCT0` (31)<br>`     &                ,BCTI0,BCC0,BCCI0,XX,YY,ZZ,IELM,POS,DVEL)` (32)<br>`      IF (ICPL.EQ.1) CALL SF_DEALLOC()` (33)<br>`      END` (35) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
