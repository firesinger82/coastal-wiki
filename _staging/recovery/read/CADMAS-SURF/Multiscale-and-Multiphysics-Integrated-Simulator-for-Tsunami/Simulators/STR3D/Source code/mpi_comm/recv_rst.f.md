---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/mpi_comm/recv_rst.f
lines: 19
sha256: aa063672c57939c97404c3c87b125f1e2b33912491958c4ba8dae4321615e528
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# recv_rst.f — 판독 구간 기록

구간은 1행부터 19행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | RECV_RST는 MPI_PARAM과 KK(*)를 사용한다(1–5). 모델 랭크 0은 IROOTC에서 IRSTYP/IRETYP를 받는다(7–9). 그 밖의 랭크 중 랭크 1은 명령 32를 0으로 보내고, 비영 랭크는 두 정수의 브로드캐스트에 참여한다(10–14). IRSTYP와 IRETYP를 KK(83)/KK(84)에 각각 저장한다(16–17). 원문(연속행은 앞 문장에 이어짐): `      SUBROUTINE RECV_RST(KK)` (1); `      USE MPI_PARAM` (3); `      DIMENSION KK(*)` (5); `      IF( MYRANK == 0 ) THEN` (7); `        CALL C_MPI_RECV_I(IRSTYP,1,IROOTC)` (8); `        CALL C_MPI_RECV_I(IRETYP,1,IROOTC)` (9); `      ELSE` (10); `        IF( MYRANK == 1 ) CALL M_MPI_SEND_I(32,1,0)  ! SEND IOP=32 TO GLB_COMM` (11); `        CALL M_MPI_BCAST_I(IRSTYP,1)` (12); `        CALL M_MPI_BCAST_I(IRETYP,1)` (13); `      ENDIF` (14); `      KK(83) = IRSTYP` (16); `      KK(84) = IRETYP` (17); `      END` (19) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 16–17: IRSTYP와 IRETYP의 저장 위치는 각각 KK(83)과 KK(84)이다. 해석: 두 값은 재시작 관련 값으로 읽힌다. [11-04 전수 검증 정정]
