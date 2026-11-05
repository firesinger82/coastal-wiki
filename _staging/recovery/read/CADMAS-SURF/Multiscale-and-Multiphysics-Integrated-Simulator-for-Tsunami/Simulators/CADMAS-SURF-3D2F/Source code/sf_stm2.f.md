---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_stm2.f
lines: 27
sha256: fad4d5766362d8eb0b5bf6123d54669c9ce84db18c25d43b48d293cc64871ecb
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_stm2.f — 판독 구간 기록

구간은 1행부터 27행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | SF_STM2의 선언부다. SF_DPTH_UPDATE에 인용한 인수 목록을 전달한다(8–9). 이 호출의 마지막 두 인수는 DT·DTO다. SF_STM_OBST의 SUMZ 다음 인수에 2를 전달한다(10–13). 이어서 SF_ALLOC1을 호출한다(14). 원문(연속 표시는 앞 문장에 이어짐): `      SUBROUTINE SF_STM2(DT,DTO)` (1); `      USE VF_A2ARRAY` (3); `      USE SF_ARRAY` (4); `      IMPLICIT REAL*8(A-H,O-Z)` (6); `      CALL SF_DPTH_UPDATE(DZ,SUMZ,XX,YY,ZZ,UU,VV,FF,FX,FY,GGX,GGY,GGW` (8); `     &                   ,GGR,LNDC,NF,INDX,INDY,FLFU,FLFV,DT,DTO)` (9); `      CALL SF_STM_OBST(GGV,GGX,GGY,GGZ,GGW,GLV,GLX,GLY,GLZ,NF,INDC,INDX` (10); `     &                ,INDY,INDZ,KST,GGV_0,GGX_0,GGY_0,GGZ_0,XX,YY,ZZ` (11); `     &                ,CM0,SUMZ,2,WK01,DBUF,WK14,WK15,WK16,WK17,WK18` (12); `     &                ,WK19,WK20)` (13); `      CALL SF_ALLOC1()` (14). [11-04 전수 검증 정정] |
| 15–27 | 시작 시 1행 SF_STM2 루틴 안. SF_STM2 안. SF_BC_RESET에 15–20행의 인수 목록을 전달한다. 이어서 SF_CINIT에 21–25행의 인수 목록을 전달한다. 고정형식 연속문은 아래 각 행이 앞 문장에 이어진다. 원문(연속 표시는 앞 문장에 이어짐): `      CALL SF_BC_RESET(INDB,INDBK,INDBE,INDBT,INDBC,BCU,BCV,BCW,BCP` (15); `     &                ,BCF,BCVI,BCK,BCE,BCT,BCTI,BCC,BCCI,GGX,GGY` (16); `     &                ,GGZ,GLX,GLY,GLZ,NF,INDX,INDY,INDZ,INDX0,INDY0` (17); `     &                ,INDZ0,INDB0,INDBK0,INDBE0,INDBT0,INDBC0,BCU0` (18); `     &                ,BCV0,BCW0,BCP0,BCF0,BCVI0,BCK0,BCE0,BCT0` (19); `     &                ,BCTI0,BCC0,BCCI0,XX,YY,ZZ,IELM,POS,DVEL)` (20); `      CALL SF_CINIT(XX,YY,ZZ,UU,VV,WW,PP,FF,FX,FY,FZ,ANU,GGV,GGX,GGY` (21); `     &             ,GGZ,BCU,BCV,BCW,BCP,BCF,BCVI,DMTBTT,DMTBZZ,DMTBHH` (22); `     &             ,DMTBUN,DMTBUT,DBUF,WK01,WK02,WK03,NF,INDX,INDY` (23); `     &             ,INDZ,INDB,INDS,IBUF,WK14,WK15,WK16,WK17,WK18,WK19` (24); `     &             ,WK20)` (25); `      END` (27). 해석: SF_BC_RESET의 인수들은 현재·이전 경계 배열과 위치·속도 배열을 포함하는 것으로 읽힌다. 해석: SF_CINIT의 인수들은 유체·경계·인덱스·작업 배열로 읽힌다. [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
