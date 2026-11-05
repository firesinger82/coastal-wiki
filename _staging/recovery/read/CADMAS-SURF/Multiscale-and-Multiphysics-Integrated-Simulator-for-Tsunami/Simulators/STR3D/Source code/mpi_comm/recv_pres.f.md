---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/mpi_comm/recv_pres.f
lines: 45
sha256: e50015d2239cb9d50ec110219b6a4e58908e176e1fdc2bee85d274a376b9f007
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# recv_pres.f — 판독 구간 기록

구간은 1행부터 45행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–28 | RECV_PRES는 MPI_PARAM과 REAL*8 암묵 선언을 사용한다(1–6). PRESS(NNOD)/AFC(NPFC)/IPND(NNOD)/D_T(NSTEP)를 선언한다(8). 모델 랭크 0은 IROOTC에서 PRESS와 TNEXT를 받고, I_BCT>0이면 먼저 AFC/IPND를 받는다(10–16). 다른 모델 랭크는 랭크 1이 명령 12와 I_BCT를 0으로 보내며, I_BCT>0에 따라 AFC/IPND를 받고 PRESS를 받은 뒤 TNEXT 브로드캐스트에 참여한다(17–28). 원문(연속행은 앞 문장에 이어짐): `      SUBROUTINE RECV_PRES(AFC,IPND,PRESS,TNEXT,D_T,NSTEP,NNOD,NPFC` (1); `     &                    ,I_BCT)` (2); `      USE MPI_PARAM` (4); `      IMPLICIT REAL*8(A-H,O-Z)` (6); `      DIMENSION PRESS(NNOD),AFC(NPFC),IPND(NNOD),D_T(NSTEP)` (8); `      IF( MYRANK == 0 ) THEN` (10); `        IF( I_BCT > 0 ) THEN` (11); `          CALL C_MPI_RECV_D(AFC,NPFC,IROOTC)` (12); `          CALL C_MPI_RECV_I(IPND,NNOD,IROOTC)` (13); `        ENDIF` (14); `        CALL C_MPI_RECV_D(PRESS,NNOD,IROOTC)` (15); `        CALL C_MPI_RECV_D(TNEXT,1,IROOTC)` (16); `      ELSE` (17); `        IF( MYRANK == 1 ) THEN` (18); `          CALL M_MPI_SEND_I(12,1,0)  ! SEND IOP=12 TO GLB_COMM` (19); `          CALL M_MPI_SEND_I(I_BCT,1,0)` (20); `        ENDIF` (21); `        IF( I_BCT > 0 ) THEN` (22); `          CALL M_MPI_RECV_D(AFC,NPFC,0)` (23); `          CALL M_MPI_RECV_I(IPND,NNOD,0)` (24); `        ENDIF` (25); `        CALL M_MPI_RECV_D(PRESS,NNOD,0)` (26); `        CALL M_MPI_BCAST_D(TNEXT,1)` (27); `      ENDIF` (28) |
| 29–45 | 시작 시 1행 RECV_PRES 루틴 안. TNEXT==0.D0이면 반환한다(30). TIM을 0으로 초기화하고 D_T(I)를 누적하여 TIM>=TNEXT에서 루프를 종료한다(32–37). 모델 랭크 0은 TIM을 IROOTC로 보내고, 랭크 1은 TIM을 모델 랭크 0으로 보낸다(39–43). 39–43행 IF/ELSEIF 사슬에는 ELSE가 없다. MYRANK가 0도 1도 아니면 이 사슬에서 TIM을 보내지 않는다. 원문(연속행은 앞 문장에 이어짐): `      IF( TNEXT == 0.D0 ) RETURN` (30); `      TIM = 0.` (32); `      DO I = 1, NSTEP` (34); `        TIM = TIM + D_T(I)` (35); `        IF( TIM >= TNEXT ) EXIT` (36); `      ENDDO` (37); `      IF( MYRANK == 0 ) THEN` (39); `        CALL C_MPI_SEND_D(TIM,1,IROOTC)` (40); `      ELSEIF( MYRANK == 1 ) THEN` (41); `        CALL M_MPI_SEND_D(TIM,1,0)` (42); `      ENDIF` (43); `      END` (45) [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 34–37: 누적 시간 루프에는 TIM>=TNEXT 조기 종료가 있다. NSTEP까지 누적해도 이 조건을 만족하지 않은 경우를 처리하는 별도 문장은 없다.
