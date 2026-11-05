---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_str3.f
lines: 19
sha256: 3eaaf56cc98a3bdc747c378fafdb3f570108b42ff24351b60052365558fdca02
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_str3.f — 판독 구간 기록

구간은 1행부터 19행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | SF_STR3의 모듈·암시적 실수 선언·구조 INCLUDE(1–8). ICPL*IOT=1이면 SF_PRSTRN, IENS*IOT=1이면 SF_ENS_OUT을 호출한다. SF_WT_RESTART는 두 조건 밖에서 호출한다(10–17). 원문(연속행은 아래 행 번호 순서로 이어지는 한 문장): `      SUBROUTINE SF_STR3(DT)` (1)<br>`      USE VF_A2ARRAY` (3)<br>`      USE SF_ARRAY` (4)<br>`      IMPLICIT REAL*8(A-H,O-Z)` (6)<br>`      INCLUDE 'SF_STRUCT.h'` (8)<br>`      IF (ICPL*IOT.EQ.1)` (10)<br>`     &  CALL SF_PRSTRN(PRES0,PP,IPGRID,IGNO,POS,ZZ,NF)` (11)<br>`      IF (IENS*IOT.EQ.1)` (13)<br>`     &  CALL SF_ENS_OUT(XX,YY,ZZ,UU,VV,WW,PP,FF,GGV,GGX,GGY,GGZ,NF` (14)<br>`     &                 ,INDX,INDY,INDZ)` (15)<br>`      CALL SF_WT_RESTART(DT)` (17)<br>`      END` (19) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 1–17: 인수 DT는 SF_WT_RESTART에만 전달한다.
