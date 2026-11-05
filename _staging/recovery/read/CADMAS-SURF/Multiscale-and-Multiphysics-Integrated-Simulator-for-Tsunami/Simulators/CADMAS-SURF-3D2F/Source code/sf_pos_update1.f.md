---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_pos_update1.f
lines: 36
sha256: 9c6ec264b1042c50fc07ec11461bb262c8a260f9fa208040d36758ab9d0c09e3
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_pos_update1.f — 판독 구간 기록

구간은 1행부터 36행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | SF_POS_UPDATE1의 선언부다. 다음 시각 TNEXT를 TNOW+DT로 계산한다(19). 원문(연속 표시는 앞 문장에 이어짐): `      SUBROUTINE SF_POS_UPDATE1(IPND0,PRES0,DELZ0,IFIX0,GRID,POS,IPGRID` (1); `     &                         ,IPGRID0,IRGRID,IELM,IGNO,XX,YY,ZZ,NF,PP` (2); `     &                         ,DZ,LNDC,DT)` (3); `      IMPLICIT REAL*8(A-H,O-Z)` (5); `      INCLUDE 'VF_A0PRM.h'` (7); `      INCLUDE 'VF_ANUMBI.h'` (8); `      INCLUDE 'VF_APARAI.h'` (9); `      INCLUDE 'VF_ATIMER.h'` (10); `      INCLUDE 'SF_STRUCT.h'` (11); `      DIMENSION GRID(3,NNOD),POS(3,NNOD),IELM(24,NELM),IGNO(NNOD)` (13); `     &         ,XX(MAXG1,NUMI),YY(MAXG1,NUMJ),ZZ(MAXG1,NUMK)` (14); `     &         ,NF(NUMI,NUMJ,NUMK),PP(NUMI,NUMJ,NUMK),IPGRID(2,NNOD)` (15); `     &         ,IPGRID0(2,NNOD0),IPND0(NNOD0),PRES0(NNOD0),DZ(NUMI,NUMJ)` (16); `     &         ,LNDC(NUMI,NUMJ),IRGRID(NNOD),DELZ0(NNOD0),IFIX0(NNOD0)` (17); `      TNEXT = TNOW + DT` (19). |
| 21–36 | 시작 시 1행 SF_POS_UPDATE1 루틴 안. SF_POS_UPDATE1 안. TNEXT>TSTR2일 때만 갱신한다(21). ICON=1·MYRANK=0이면 SF_GIPND를 호출한다(23–24). SF_GPRES를 호출한다(26). ISTM=1이면 SF_GDPTH 호출 후 DZ를 0으로 만들고 SF_VOLCHK를 호출한다(28–32). 원문(연속 표시는 앞 문장에 이어짐): `      IF( TNEXT > TSTR2 ) THEN` (21); `        IF( ICON == 1 .AND. MYRANK == 0 )` (23); `     &    CALL SF_GIPND(IPND0,IPGRID0,NNOD0)` (24); `        CALL SF_GPRES(PRES0,PP,IPGRID,IGNO,POS,ZZ,NF)` (26); `        IF( ISTM == 1 ) THEN` (28); `          CALL SF_GDPTH(DELZ0,DZ,LNDC,IRGRID,IGNO,POS,XX,YY)` (29); `          DZ(:,:) = 0.D0` (30); `          CALL SF_VOLCHK(IFIX0,IELM,IGNO,GRID,POS,XX,YY)` (31); `        ENDIF` (32); `      ENDIF` (34); `      END` (36). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
