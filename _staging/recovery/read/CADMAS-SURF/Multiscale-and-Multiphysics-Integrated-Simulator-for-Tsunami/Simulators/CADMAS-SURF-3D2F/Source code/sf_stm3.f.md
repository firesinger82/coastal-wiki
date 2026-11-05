---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_stm3.f
lines: 14
sha256: 2c519442ab695b3fe9dc6369abb731c68cfef2f3a5cd668ebcb43543e8a596ee
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_stm3.f — 판독 구간 기록

구간은 1행부터 14행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | SF_STM3의 선언부다. IENS*IOT가 1이면 SF_ENS_OUT을 호출한다(9–11). 그 조건 밖에서 SF_WT_RESTART(DT)를 호출한다(12). 원문(연속 표시는 앞 문장에 이어짐): `      SUBROUTINE SF_STM3(DT)` (1); `      USE VF_A2ARRAY` (3); `      IMPLICIT REAL*8(A-H,O-Z)` (5); `      INCLUDE 'SF_STRUCT.h'` (7); `      IF (IENS*IOT.EQ.1)` (9); `     &  CALL SF_ENS_OUT(XX,YY,ZZ,UU,VV,WW,PP,FF,GGV,GGX,GGY,GGZ,NF` (10); `     &                 ,INDX,INDY,INDZ)` (11); `      CALL SF_WT_RESTART(DT)` (12); `      END` (14). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
