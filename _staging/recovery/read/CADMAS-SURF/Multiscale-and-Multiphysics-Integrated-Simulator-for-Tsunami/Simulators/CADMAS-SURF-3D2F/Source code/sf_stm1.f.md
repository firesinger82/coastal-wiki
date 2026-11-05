---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_stm1.f
lines: 18
sha256: d90c633b46c5ac9d4ea8ddb64a6bc19216e2244da3acc840d10e926c73cac2d1
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_stm1.f — 판독 구간 기록

구간은 1행부터 18행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | SF_STM1의 선언부다. IENS=0을 설정한 뒤 IENS=1이면 SF_ENS_GEOM을 호출하는 조건이 있다(11–12). SF_DPTH_INIT을 호출하고 IRETYP>0이면 SF_RD_RESTART(DT)를 호출한다(14–16). 원문(연속 표시는 앞 문장에 이어짐): `      SUBROUTINE SF_STM1(DT)` (1); `      USE VF_A2ARRAY` (3); `      IMPLICIT REAL*8(A-H,O-Z)` (5); `      INCLUDE 'VF_A0PRM.h'` (7); `      INCLUDE 'VF_AFILEI.h'` (8); `      INCLUDE 'SF_STRUCT.h'` (9); `      IENS=0` (11); `      IF( IENS == 1 ) CALL SF_ENS_GEOM(XX,YY,ZZ)` (12); `      CALL SF_DPTH_INIT(XX,YY,ZZ,FF,GGW,GGR,NF)` (14); `      IF( IRETYP > 0 ) CALL SF_RD_RESTART(DT)` (16); `      END` (18). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11–12: IENS를 0으로 설정한 바로 다음 조건은 IENS==1이다. 이 두 문장 사이에 IENS를 바꾸는 문장은 없다.
