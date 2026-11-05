---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_stm0.f
lines: 18
sha256: 1f4d216d7dcc439bf93ae774b347e6c7c445ff4d3586830a20539ec5fe7f999e
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_stm0.f — 판독 구간 기록

구간은 1행부터 18행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | SF_STM0의 선언부다. MYRANK=0에서 IRETYP를 IROOTSTM에 보낸다(12). SF_ALLOC0 후 SF_OBST_POR(GGV_0,GGV,NF,DBUF)를 호출한다(13–14). SF_MDPORO_H 호출에서 SUMZ 다음에 0·WK01·DBUF를 전달한다(15–16). 원문(연속 표시는 앞 문장에 이어짐): `      SUBROUTINE SF_STM0()` (1); `      USE VF_A2ARRAY` (3); `      IMPLICIT REAL*8(A-H,O-Z)` (5); `      INCLUDE 'VF_A0PRM.h'` (7); `      INCLUDE 'VF_AFILEI.h'` (8); `      INCLUDE 'VF_APARAI.h'` (9); `      INCLUDE 'SF_STRUCT.h'` (10); `      IF( MYRANK == 0 ) CALL SF_STM_C_MPI_SEND_I(IRETYP,1,IROOTSTM)` (12); `      CALL SF_ALLOC0()` (13); `      CALL SF_OBST_POR(GGV_0,GGV,NF,DBUF)` (14); `      CALL SF_MDPORO_H(GGV,GGX,GGY,GGZ,GGW,KST,NF,INDC,ZZ,SUMZ` (15); `     &                ,0,WK01,DBUF)` (16); `      END` (18). 해석: SF_OBST_POR는 공극률 처리 루틴으로 읽힌다. [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
