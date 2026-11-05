---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_comm_init.f
lines: 94
sha256: 313636fa946ca766907d6b17a4e8d7cd7bf574b7983e585bce035c6200dd8d7c
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_comm_init.f — 판독 구간 기록

구간은 1행부터 94행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–34 | SF_COMM_INIT 선언과 MOD_COMM 사용(1–7). INCLUDE 세 개를 포함한다(9–11). 통신자(communicator)를 복사하고 ICPL=0에서 시작한다(13–15). SF_C_MPI_COMM_SIZE가 반환한 MPROCS가 NPROCS보다 크면 ICPL=2로 설정한다(17–21). 23–33행은 랭크(rank) 확인과 SF_C_MPI_ALLREDUCE_I 호출을 주석 처리한 코드다. 원문: `      SUBROUTINE SF_COMM_INIT()` (1)<br>`      USE MOD_COMM, ONLY: COMM_WORK_2FC_STR, COMM_2FC_STR` (3)<br>`      IMPLICIT REAL*8(A-H,O-Z)` (5)<br>`      LOGICAL IEX` (7)<br>`      INCLUDE 'VF_A0PRM.h'` (9)<br>`      INCLUDE 'VF_APARAI.h'` (10)<br>`      INCLUDE 'SF_STRUCT.h'` (11)<br>`      COMM_2FC_STR = COMM_WORK_2FC_STR` (13)<br>`      ICPL = 0` (15)<br>`      CALL SF_C_MPI_COMM_SIZE(MPROCS)` (17)<br>`      IF( MPROCS > NPROCS ) THEN` (19)<br>`        ICPL = 2` (21)<br>`!        IF( MYRANK == 0 ) THEN` (23)<br>`!          CALL SF_C_MPI_COMM_RANK(IRANK)` (24)<br>`!        ELSE` (25)<br>`!          IRANK = 0` (26)<br>`!        ENDIF` (27)<br>`!        CALL SF_C_MPI_ALLREDUCE_I(IRANK,IROOTC,1)` (29)<br>`!        IRANK = 0` (31)<br>`!        CALL SF_C_MPI_ALLREDUCE_I(IRANK,IROOTS,1)` (33) [11-04 전수 검증 정정] |
| 35–74 | 시작 시 19행 `IF( MPROCS > NPROCS ) THEN` 안이다. 이 분기는 73행 `ENDIF`에서 닫힌다. SF_C_MPI_COMM_RANK로 IRANK를 얻는다(35). MYRANK=0인 프로세스만 JRANK에 IRANK를 넣는다(37–41). IRANK=0이 JRANK를 모아 IROOTC에 합산하고 전체에 보낸다(43–55). JRANK를 0으로 바꾼 뒤 같은 송수신 구조로 IROOTS를 모은다(57–71). 19행 분기를 닫는다(73). 원문: `        CALL SF_C_MPI_COMM_RANK(IRANK)` (35)<br>`        IF( MYRANK == 0 ) THEN` (37)<br>`          JRANK = IRANK` (38)<br>`        ELSE` (39)<br>`          JRANK = 0` (40)<br>`        ENDIF` (41)<br>`        IF( IRANK == 0 ) THEN` (43)<br>`          IROOTC = JRANK` (44)<br>`          DO I = 1, MPROCS - 1` (45)<br>`            CALL SF_C_MPI_RECV_I(JRANK,1,I)` (46)<br>`            IROOTC = IROOTC + JRANK` (47)<br>`          ENDDO` (48)<br>`          DO I = 1, MPROCS - 1` (49)<br>`            CALL SF_C_MPI_SEND_I(IROOTC,1,I)` (50)<br>`          ENDDO` (51)<br>`        ELSE` (52)<br>`          CALL SF_C_MPI_SEND_I(JRANK,1,0)` (53)<br>`          CALL SF_C_MPI_RECV_I(IROOTC,1,0)` (54)<br>`        ENDIF` (55)<br>`        JRANK = 0` (57)<br>`        IF( IRANK == 0 ) THEN` (59)<br>`          IROOTS = JRANK` (60)<br>`          DO I = 1, MPROCS - 1` (61)<br>`            CALL SF_C_MPI_RECV_I(JRANK,1,I)` (62)<br>`            IROOTS = IROOTS + JRANK` (63)<br>`          ENDDO` (64)<br>`          DO I = 1, MPROCS - 1` (65)<br>`            CALL SF_C_MPI_SEND_I(IROOTS,1,I)` (66)<br>`          ENDDO` (67)<br>`        ELSE` (68)<br>`          CALL SF_C_MPI_SEND_I(JRANK,1,0)` (69)<br>`          CALL SF_C_MPI_RECV_I(IROOTS,1,0)` (70)<br>`        ENDIF` (71)<br>`      ENDIF` (73) [11-04 전수 검증 보완] |
| 75–94 | 시작 시 1행 SF_COMM_INIT 루틴 안. MYRANK=0이고 ICPL=0이면 data.bdf의 존재를 조사하고 존재할 때 ICPL=1로 바꾼다(75–78). VF_P1BCSI로 ICPL을 배포하고 IPART=0을 설정한다(80–82). ICPL=2이면 PLOWER2·GMIN·FMIN을 각각 1.D-1로, 그 밖에는 0.D0으로 설정한다(84–92). 원문: `      IF( MYRANK == 0 .AND. ICPL == 0 ) THEN` (75)<br>`        INQUIRE( FILE = 'data.bdf', EXIST = IEX )` (76)<br>`        IF( IEX ) ICPL = 1` (77)<br>`      ENDIF` (78)<br>`      CALL VF_P1BCSI(ICPL,1,0)` (80)<br>`      IPART = 0` (82)<br>`      IF( ICPL == 2 ) THEN` (84)<br>`        PLOWER2 = 1.D-1` (85)<br>`        GMIN = 1.D-1` (86)<br>`        FMIN = 1.D-1` (87)<br>`      ELSE` (88)<br>`        PLOWER2 = 0.D0` (89)<br>`        GMIN = 0.D0` (90)<br>`        FMIN = 0.D0` (91)<br>`      ENDIF` (92)<br>`      END` (94) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 57–70: IROOTS 합산에 쓰는 JRANK는 송수신 분기 직전 0으로 대입한다. 이 파일에는 해당 분기 전에 JRANK를 다른 값으로 바꾸는 실행문이 없다.
- 23–33: SF_C_MPI_ALLREDUCE_I 호출 두 개는 주석 처리되어 있다. 실행 경로는 43–71행의 개별 송수신이다.
