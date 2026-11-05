---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_prstrn.f
lines: 24
sha256: 3a4d8d02500096e761427063e24385cf0dd3fa4c77562a97aebfcacf4ae8cb5d
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_prstrn.f — 판독 구간 기록

구간은 1행부터 24행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | SF_PRSTRN의 선언부다(1–13). SF_GPRES(PRES0,PP,IPGRID,IGNO,POS,ZZ,NF)를 호출한다(15). MYRANK=0이면 TNOW와 각 절점의 PRES0를 1PE15.7 서식으로 ITPFIL에 쓴다(17–22). 원문(연속 표시는 앞 문장에 이어짐): `      SUBROUTINE SF_PRSTRN(PRES0,PP,IPGRID,IGNO,POS,ZZ,NF)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      INCLUDE 'VF_A0PRM.h'` (5); `      INCLUDE 'VF_AFILEI.h'` (6); `      INCLUDE 'VF_ANUMBI.h'` (7); `      INCLUDE 'VF_APARAI.h'` (8); `      INCLUDE 'VF_ATIMER.h'` (9); `      INCLUDE 'SF_STRUCT.h'` (10); `      DIMENSION PRES0(NNOD0),PP(NUMI,NUMJ,NUMK),IPGRID(2,NNOD)` (12); `     &         ,POS(3,NNOD),ZZ(MAXG1,NUMK),NF(NUMI,NUMJ,NUMK),IGNO(NNOD)` (13); `      CALL SF_GPRES(PRES0,PP,IPGRID,IGNO,POS,ZZ,NF)` (15); `      IF( MYRANK == 0 ) THEN` (17); `        WRITE(ITPFIL,'(1PE15.7)') TNOW` (18); `        DO I = 1, NNOD0` (19); `          WRITE(ITPFIL,'(1PE15.7)') PRES0(I)` (20); `        ENDDO` (21); `      ENDIF` (22); `      END` (24). 해석: SF_GPRES는 압력을 모으는 루틴으로 읽힌다. [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
