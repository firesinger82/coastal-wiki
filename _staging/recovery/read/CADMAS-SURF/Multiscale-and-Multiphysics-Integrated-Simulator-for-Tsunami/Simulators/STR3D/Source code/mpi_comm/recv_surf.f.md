---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/mpi_comm/recv_surf.f
lines: 60
sha256: 978800d3ad4078707c95b274adca5bd808061e8693c11d7328136e4e1c205c9b
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# recv_surf.f — 판독 구간 기록

구간은 1행부터 60행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–28 | RECV_SURF는 MPI_PARAM/M_VAL 및 REAL*8 암묵 선언을 사용한다(1–8). KK(8)/KK(94)에서 NNOD/NIGSF를 읽는다(10–11). 모델 랭크 0은 IROOTC에서 WLEVEL/ALEVEL/NPFC를 받는다(13–16). 비영 랭크 중 MYRANK가 1인 랭크만 명령 11을 모델 랭크 0으로 보낸다(18). 모든 비영 랭크는 WLEVEL/ALEVEL 브로드캐스트에 참여한다(19–20). 모든 비영 랭크는 모델 랭크 0으로부터 NPFC를 받는다(21). RR(8)/RR(9)와 KK(81)에 값을 저장한다(24–27). 원문(연속행은 앞 문장에 이어짐): `      SUBROUTINE RECV_SURF(KK,RR)` (1); `      USE MPI_PARAM` (3); `      USE M_VAL` (4); `      IMPLICIT REAL*8(A-H,O-Z)` (6); `      DIMENSION KK(*),RR(*)` (8); `      NNOD = KK(8)` (10); `      NIGSF = KK(94)` (11); `      IF( MYRANK == 0 ) THEN` (13); `        CALL C_MPI_RECV_D(WLEVEL,1,IROOTC)` (14); `        CALL C_MPI_RECV_D(ALEVEL,1,IROOTC)` (15); `        CALL C_MPI_RECV_I(NPFC,1,IROOTC)` (16); `      ELSE` (17); `        IF( MYRANK == 1 ) CALL M_MPI_SEND_I(11,1,0)  ! SEND IOP=11 TO GLB_COMM` (18); `        CALL M_MPI_BCAST_D(WLEVEL,1)` (19); `        CALL M_MPI_BCAST_D(ALEVEL,1)` (20); `        CALL M_MPI_RECV_I(NPFC,1,0)` (21); `      ENDIF` (22); `      RR(8) = WLEVEL` (24); `      RR(9) = ALEVEL` (25); `      KK(81) = NPFC` (27) [11-04 전수 검증 정정] |
| 29–60 | 시작 시 1행 RECV_SURF 루틴 안. IPFC(10,NPFC), AFC(NPFC), IPND(NNOD)를 할당한다(29–31). 모델 랭크 0은 IROOTC에서, 다른 랭크는 모델 랭크 0에서 세 배열을 받는다(33–41). ISTM==0이면 반환한다(43). 남은 경로에서는 랭크 0만 IRF를 할당하고 모든 랭크가 IRND를 할당한다(45–46). 랭크 0은 IRF/IRND를, 다른 랭크는 IRND만 받는다(48–53). IRMSH/RMSH/DELZ/SUMZ를 할당하고 종료한다(55–60). 원문(연속행은 앞 문장에 이어짐): `      ALLOCATE( IPFC(10,NPFC) )` (29); `      ALLOCATE( AFC(NPFC) )` (30); `      ALLOCATE( IPND(NNOD) )` (31); `      IF( MYRANK == 0 ) THEN` (33); `        CALL C_MPI_RECV_I(IPFC,10*NPFC,IROOTC)` (34); `        CALL C_MPI_RECV_D(AFC,NPFC,IROOTC)` (35); `        CALL C_MPI_RECV_I(IPND,NNOD,IROOTC)` (36); `      ELSE` (37); `        CALL M_MPI_RECV_I(IPFC,10*NPFC,0)` (38); `        CALL M_MPI_RECV_D(AFC,NPFC,0)` (39); `        CALL M_MPI_RECV_I(IPND,NNOD,0)` (40); `      ENDIF` (41); `      IF( ISTM == 0 ) RETURN` (43); `      IF( MYRANK == 0 ) ALLOCATE( IRF(NPFC) )` (45); `      ALLOCATE( IRND(NNOD) )` (46); `      IF( MYRANK == 0 ) THEN` (48); `        CALL C_MPI_RECV_I(IRF,NPFC,IROOTC)` (49); `        CALL C_MPI_RECV_I(IRND,NNOD,IROOTC)` (50); `      ELSE` (51); `        CALL M_MPI_RECV_I(IRND,NNOD,0)` (52); `      ENDIF` (53); `      ALLOCATE( IRMSH(6,NNOD) )` (55); `      ALLOCATE( RMSH(4,NNOD) )` (56); `      ALLOCATE( DELZ(NNOD) )` (57); `      ALLOCATE( SUMZ(NNOD+NIGSF) )` (58); `      END` (60) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 29·34·38: IPFC의 첫 차원은 10이다. 정수 전송 개수는 `10*NPFC`이다. 해석: IPFC의 각 열은 한 면의 자료로 읽힌다. [11-04 전수 검증 정정]
- 55–58: IRMSH/RMSH/DELZ/SUMZ는 할당 후 이 루틴에서 값 대입이나 수신을 하지 않는다.
