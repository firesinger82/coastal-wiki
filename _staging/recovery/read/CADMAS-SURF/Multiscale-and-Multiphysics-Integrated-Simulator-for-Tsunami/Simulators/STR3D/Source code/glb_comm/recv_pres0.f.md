---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/glb_comm/recv_pres0.f
lines: 44
sha256: ee4374cfab6cea1026a07a0cb2532d6797bba04964ed8394322adb5de015a793
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# recv_pres0.f — 판독 구간 기록

구간은 1행부터 44행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | M_VAL·MPI_PARAM·암시적 배정밀도와 PRESS 포인터를 선언한다(3–8). NNOD·NPFC는 KK(8)·KK(81)에서 얻는다(10–11). 원문: `      SUBROUTINE RECV_PRES0(KK)` (1); `      USE M_VAL` (3); `      USE MPI_PARAM` (4); `      IMPLICIT REAL*8(A-H,O-Z)` (6); `      DIMENSION KK(*)` (7); `      REAL(8), POINTER :: PRESS(:)` (8); `      NNOD = KK(8)` (10); `      NPFC = KK(81)` (11). |
| 13–30 | 시작 시 1행 recv_pres0 루틴 안. 프로세스 1에서 I_BCT를 받는다(13). I_BCT 양수 분기에서 AFC·IPND를 할당하고 IROOTC로부터 수신하여 표면·절점별로 분배한 뒤 해제한다(15–29). 원문: `      CALL M_MPI_RECV_I(I_BCT,1,1)` (13); `      IF( I_BCT > 0 ) THEN` (15); `        ALLOCATE( AFC(NPFC) )` (17); `        ALLOCATE( IPND(NNOD) )` (18); `        CALL C_MPI_RECV_D(AFC,NPFC,IROOTC)` (20); `        CALL C_MPI_RECV_I(IPND,NNOD,IROOTC)` (21); `        CALL SCATTER_SURFACE(AFC,1)` (23); `        CALL SCATTER_NODAL_I(IPND,1)` (24); `        DEALLOCATE( AFC )` (26); `        DEALLOCATE( IPND )` (27); `      ENDIF` (29). |
| 31–44 | 시작 시 1행 recv_pres0 루틴 안. PRESS(NNOD)를 할당·수신·분배·해제한다(31–34). TNEXT를 수신하여 방송한다(36–37). TNEXT가 0.D0이면 반환한다(39). 해석: TNEXT는 다음 시각이다. 그 외에는 프로세스 1에서 TIM을 받아 IROOTC로 보낸다(41–42). 원문: `      ALLOCATE( PRESS(NNOD) )` (31); `      CALL C_MPI_RECV_D(PRESS,NNOD,IROOTC)` (32); `      CALL SCATTER_NODAL_D(PRESS,1)` (33); `      DEALLOCATE( PRESS )` (34); `      CALL C_MPI_RECV_D(TNEXT,1,IROOTC)` (36); `      CALL M_MPI_BCAST_D(TNEXT,1)` (37); `      IF( TNEXT == 0.D0 ) RETURN` (39); `      CALL M_MPI_RECV_D(TIM,1,1)` (41); `      CALL C_MPI_SEND_D(TIM,1,IROOTC)` (42); `      END` (44). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
