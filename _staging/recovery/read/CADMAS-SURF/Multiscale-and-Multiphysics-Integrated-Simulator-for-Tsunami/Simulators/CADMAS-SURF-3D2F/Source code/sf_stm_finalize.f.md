---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_stm_finalize.f
lines: 18
sha256: 37ed5e047cb28be2575fb06a7ce41cf11f32b28a37e66e1774bf16d09ea9c4d8
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_stm_finalize.f — 판독 구간 기록

구간은 1행부터 18행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | SF_STM_FINALIZE의 선언부다. MYRANK=0이면 DRECV(NUMI0,NUMJ0)를 할당하여 IROOTSTM에서 배정밀도 배열을 받는다(11–13). 배열을 해제한 후 정수 상수 1을 IROOTSTM으로 보낸다(14–15). 원문(연속 표시는 앞 문장에 이어짐): `      SUBROUTINE SF_STM_FINALIZE()` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      INCLUDE 'VF_A0PRM.h'` (5); `      INCLUDE 'VF_APARAI.h'` (6); `      INCLUDE 'SF_STRUCT.h'` (7); `      REAL(8), POINTER :: DRECV(:,:)` (9); `      IF( MYRANK == 0 ) THEN` (11); `        ALLOCATE( DRECV(NUMI0,NUMJ0) )` (12); `        CALL SF_STM_C_MPI_RECV_D(DRECV,NUMI0*NUMJ0,IROOTSTM)` (13); `        DEALLOCATE( DRECV )` (14); `        CALL SF_STM_C_MPI_SEND_I(1,1,IROOTSTM)` (15); `      ENDIF` (16); `      END` (18). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 12–15: 수신한 DRECV는 다른 계산에 쓰지 않고 해제한다. 응답으로 정수 상수 1을 전송한다.
