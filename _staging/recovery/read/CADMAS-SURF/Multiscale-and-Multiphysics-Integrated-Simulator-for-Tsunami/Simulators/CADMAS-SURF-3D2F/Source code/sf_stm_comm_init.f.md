---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_stm_comm_init.f
lines: 69
sha256: e25d49e56f61cca54f4d83e30d8e1a67717625d34ce73e98f01cb5ab3c40ded1
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_stm_comm_init.f — 판독 구간 기록

구간은 1행부터 69행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | SF_STM_COMM_INIT의 선언부다. COMM_WORK_2FC_STM을 COMM_2FC_STM에 복사하고 ISTM=0으로 초기화한다(11–13). SF_STM_C_MPI_COMM_SIZE로 MPROCS를 받는다(15). 원문(연속 표시는 앞 문장에 이어짐): `      SUBROUTINE SF_STM_COMM_INIT()` (1); `      USE MOD_COMM, ONLY: COMM_WORK_2FC_STM, COMM_2FC_STM` (3); `      IMPLICIT REAL*8(A-H,O-Z)` (5); `      INCLUDE 'VF_A0PRM.h'` (7); `      INCLUDE 'VF_APARAI.h'` (8); `      INCLUDE 'SF_STRUCT.h'` (9); `      COMM_2FC_STM = COMM_WORK_2FC_STM` (11); `      ISTM = 0` (13); `      CALL SF_STM_C_MPI_COMM_SIZE(MPROCS)` (15). |
| 17–45 | 시작 시 1행 SF_STM_COMM_INIT 루틴 안. SF_STM_COMM_INIT 안. MPROCS>NPROCS이면 ISTM=1이며 ICPL=1이면 VF_A2ERR를 호출한다(17–22). 통신 순위 IRANK를 얻는다(24). MYRANK=0인 프로세스는 JRANK=IRANK, 그 외에는 0이다(26–30). IRANK=0은 각 JRANK를 더해 IROOTC를 구한 뒤 전송하고 다른 순위는 JRANK를 보내고 IROOTC를 받는다(32–44). 원문(연속 표시는 앞 문장에 이어짐): `      IF( MPROCS > NPROCS ) THEN` (17); `        ISTM = 1` (19); `        IF( ICPL == 1 )` (21); `     &    CALL VF_A2ERR('SF_STM_COMM_INIT','STR PROCESS NOT FOUND.')` (22); `        CALL SF_STM_C_MPI_COMM_RANK(IRANK)` (24); `        IF( MYRANK == 0 ) THEN` (26); `          JRANK = IRANK` (27); `        ELSE` (28); `          JRANK = 0` (29); `        ENDIF` (30); `        IF( IRANK == 0 ) THEN` (32); `          IROOTC = JRANK` (33); `          DO I = 1, MPROCS - 1` (34); `            CALL SF_STM_C_MPI_RECV_I(JRANK,1,I)` (35); `            IROOTC = IROOTC + JRANK` (36); `          ENDDO` (37); `          DO I = 1, MPROCS - 1` (38); `            CALL SF_STM_C_MPI_SEND_I(IROOTC,1,I)` (39); `          ENDDO` (40); `        ELSE` (41); `          CALL SF_STM_C_MPI_SEND_I(JRANK,1,0)` (42); `          CALL SF_STM_C_MPI_RECV_I(IROOTC,1,0)` (43); `        ENDIF` (44). |
| 46–63 | 시작 시 `      IF( MPROCS > NPROCS ) THEN` (17)의 참 분기 안이다. 이 분기는 62행 ENDIF에서 닫힌다. JRANK=0으로 다시 설정한다(46). IRANK=0은 모든 JRANK를 더해 IROOTSTM을 구하고 전송한다(48–56). 다른 순위는 JRANK를 보내고 IROOTSTM을 받는다(57–60). 바깥 분기를 닫는다(62). 원문(연속 표시는 앞 문장에 이어짐): `        JRANK = 0` (46); `        IF( IRANK == 0 ) THEN` (48); `          IROOTSTM = JRANK` (49); `          DO I = 1, MPROCS - 1` (50); `            CALL SF_STM_C_MPI_RECV_I(JRANK,1,I)` (51); `            IROOTSTM = IROOTSTM + JRANK` (52); `          ENDDO` (53); `          DO I = 1, MPROCS - 1` (54); `            CALL SF_STM_C_MPI_SEND_I(IROOTSTM,1,I)` (55); `          ENDDO` (56); `        ELSE` (57); `          CALL SF_STM_C_MPI_SEND_I(JRANK,1,0)` (58); `          CALL SF_STM_C_MPI_RECV_I(IROOTSTM,1,0)` (59); `        ENDIF` (60); `      ENDIF` (62). [11-04 전수 검증 보완] |
| 64–69 | 시작 시 1행 SF_STM_COMM_INIT 루틴 안. SF_STM_COMM_INIT 안이며 17행 분기 밖. VF_P1BCSI로 ISTM을 배포한다(64). ICPL=2·MYRANK=0이면 IROOTS에 ISTM을 보낸다(66–67). 원문(연속 표시는 앞 문장에 이어짐): `      CALL VF_P1BCSI(ISTM,1,0)` (64); `      IF( ICPL == 2 .AND. MYRANK == 0 )` (66); `     &  CALL SF_C_MPI_SEND_I(ISTM,1,IROOTS)` (67); `      END` (69). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 46·48–59: 이 파일의 JRANK는 두 번째 집약 직전에 0으로 설정된다. 다른 순위에서 수신할 JRANK의 생성 과정은 이 파일에 없다.
