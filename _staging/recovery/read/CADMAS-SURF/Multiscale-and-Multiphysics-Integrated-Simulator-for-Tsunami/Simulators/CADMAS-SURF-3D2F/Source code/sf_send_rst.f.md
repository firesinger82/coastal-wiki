---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_send_rst.f
lines: 16
sha256: 848bc4310772ad7becb0d27be5ffe56000b2c82fe8b365652c34e864b960f6a1
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_send_rst.f — 판독 구간 기록

구간은 1행부터 16행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | SF_SEND_RST의 선언부다. MYRANK=0이면 IRSTYP·IRETYP를 IROOTS로 보낸다(10–12). 같은 루트(root) 분기에서 ISTM=1일 때 IRETYP를 IROOTSTM으로도 보낸다(13). 원문(연속 표시는 앞 문장에 이어짐): `      SUBROUTINE SF_SEND_RST()` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      INCLUDE 'VF_A0PRM.h'` (5); `      INCLUDE 'VF_AFILEI.h'` (6); `      INCLUDE 'VF_APARAI.h'` (7); `      INCLUDE 'SF_STRUCT.h'` (8); `      IF( MYRANK == 0 ) THEN` (10); `        CALL SF_C_MPI_SEND_I(IRSTYP,1,IROOTS)` (11); `        CALL SF_C_MPI_SEND_I(IRETYP,1,IROOTS)` (12); `        IF( ISTM == 1 ) CALL SF_STM_C_MPI_SEND_I(IRETYP,1,IROOTSTM)` (13); `      ENDIF` (14); `      END` (16). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
