---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/mpi_comm/send_pos.f
lines: 47
sha256: aa4a3779dad865eced7fdab162f3a33d091a51813b3eb079a0b82210529ce532
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# send_pos.f — 판독 구간 기록

구간은 1행부터 47행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | SEND_POS는 MPI_PARAM, REAL*8 암묵 선언과 POS(3,NNOD)/FLUX(3,NELM)를 선언한다(1–7). TIM==0.D0이면 모델 랭크 0은 POS 전체를 IROOTC로 보내고 IGEO>0일 때 FLUX도 보낸다(9–14). 비영 랭크에서는 랭크 1이 명령 14를 보내며 각 비영 랭크는 POS의 선두 `3*NNODI`개 값을 모델 랭크 0으로 보낸다(16–23). 해석: NNODI는 내부 절점 수로 읽힌다. 원문(연속행은 앞 문장에 이어짐): `      SUBROUTINE SEND_POS(ISEND,IGEO,NNOD,NNODI,NELM,POS,FLUX,TIM,TNEXT)` (1); `      USE MPI_PARAM` (3); `      IMPLICIT REAL*8(A-H,O-Z)` (5); `      DIMENSION POS(3,NNOD), FLUX(3,NELM)` (7); `      IF( TIM == 0.D0 ) THEN` (9); `        IF( MYRANK == 0 ) THEN` (11); `          CALL C_MPI_SEND_D(POS,3*NNOD,IROOTC)` (13); `          IF( IGEO > 0 ) CALL C_MPI_SEND_D(FLUX,3*NELM,IROOTC)` (14); `        ELSE` (16); `          IF( MYRANK == 1 ) CALL M_MPI_SEND_I(14,1,0)  ! SEND IOP=14 TO GLB_COMM` (18); `          CALL M_MPI_SEND_D(POS,3*NNODI,0)` (19); `        ENDIF` (21); `      ENDIF` (23) [11-04 전수 검증 정정] |
| 25–47 | 시작 시 1행 SEND_POS 루틴 안. 앞의 TIM==0.D0 분기와 별도로 TIM>=TNEXT를 검사한다(25). 참이면 랭크 0은 POS를 IROOTC로 보낸다(27–29). 랭크 0은 `IGEO > 0`일 때 FLUX도 보낸다(30). 비영 랭크 중 랭크 1만 명령 14를 모델 랭크 0으로 보낸다(34). 모든 비영 랭크는 POS의 선두 `3*NNODI`개 값을 모델 랭크 0으로 보낸다(35). TIM>=TNEXT인 모든 랭크는 ISEND=1로 설정한다(39). 거짓이면 ISEND=0으로 설정한다(41–45). 원문(연속행은 앞 문장에 이어짐): `      IF( TIM >= TNEXT ) THEN` (25); `        IF( MYRANK == 0 ) THEN` (27); `          CALL C_MPI_SEND_D(POS,3*NNOD,IROOTC)` (29); `          IF( IGEO > 0 ) CALL C_MPI_SEND_D(FLUX,3*NELM,IROOTC)` (30); `        ELSE` (32); `          IF( MYRANK == 1 ) CALL M_MPI_SEND_I(14,1,0)  ! SEND IOP=14 TO GLB_COMM` (34); `          CALL M_MPI_SEND_D(POS,3*NNODI,0)` (35); `        ENDIF` (37); `        ISEND = 1` (39); `      ELSE` (41); `        ISEND = 0` (43); `      ENDIF` (45); `      END` (47) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 9–25: TIM==0.D0 조건과 TIM>=TNEXT 조건은 독립된 IF 블록이다. TIM=0이며 TNEXT<=0이면 두 블록의 송신문을 모두 실행하는 코드 구조다.
