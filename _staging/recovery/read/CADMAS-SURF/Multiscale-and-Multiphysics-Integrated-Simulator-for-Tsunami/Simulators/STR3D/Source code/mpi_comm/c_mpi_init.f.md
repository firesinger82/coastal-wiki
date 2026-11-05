---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/mpi_comm/c_mpi_init.f
lines: 87
sha256: 416490310f3dd01cc2f30d15c8c6d7ad0862ace00f615c6a6515d19ebd07df85
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# c_mpi_init.f — 판독 구간 기록

구간은 1행부터 87행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–27 | C_MPI_INIT는 MOD_COMM에서 COMM_WORK_2FC_STR/COMM_MODEL을 가져오고 MPI_PARAM 및 MPI 헤더를 사용한다(1–6). 두 통신자를 CPLWORLD/MYWORLD에 대입하고 크기·랭크를 조회한다(8–18). MYRANK>0이면 색상 0, 그 밖에는 색상 1로 CGWORLD를 분할한다(20–25). 23행의 MPI_UNDFINED 인수 호출은 주석 처리되어 있다. ICPL은 0으로 초기화한다(27). 원문(연속행은 앞 문장에 이어짐): `      SUBROUTINE C_MPI_INIT()` (1); `      USE MOD_COMM, ONLY: COMM_WORK_2FC_STR, COMM_MODEL` (3); `      USE MPI_PARAM` (4); `      INCLUDE 'mpif.h'` (6); `      CPLWORLD = COMM_WORK_2FC_STR` (8); `      CALL MPI_COMM_SIZE(CPLWORLD,NPROCS0,IERR)` (10); `      CALL MPI_COMM_RANK(CPLWORLD,MYRANK0,IERR)` (12); `      MYWORLD = COMM_MODEL` (14); `      CALL MPI_COMM_SIZE(MYWORLD,NPROCS,IERR)` (16); `      CALL MPI_COMM_RANK(MYWORLD,MYRANK,IERR)` (18); `      IF( MYRANK > 0 ) THEN` (20); `        CALL MPI_COMM_SPLIT(MYWORLD,0,0,CGWORLD,IERR)` (21); `      ELSE` (22); `!        CALL MPI_COMM_SPLIT(MYWORLD,MPI_UNDFINED,0,CGWORLD,IERR)` (23); `        CALL MPI_COMM_SPLIT(MYWORLD,1,0,CGWORLD,IERR)` (24); `      ENDIF` (25); `      ICPL = 0` (27) |
| 28–60 | 시작 시 1행 C_MPI_INIT 루틴 안. NPROCS0>NPROCS이면 ICPL=2를 설정한다(29–31). 이전 allreduce 기반 코드는 주석 처리되어 있다(33–43). IRANK=0으로 설정한다(45). 결합 랭크 0에서 다른 랭크의 IRANK를 받아 IROOTC에 합산하고 0을 제외한 모든 결합 랭크로 되보낸다(47–55). 그 밖의 랭크는 0으로 보내고 결과를 받는다(56–59). 원문(연속행은 앞 문장에 이어짐): `      IF( NPROCS0 > NPROCS ) THEN` (29); `        ICPL = 2` (31); `!        IRANK = 0` (33); `!        CALL C_MPI_ALLREDUCE_I(IRANK,IROOTC,1)` (35); `!        IF( MYRANK == 0 ) THEN` (37); `!          IRANK = MYRANK0` (38); `!        ELSE` (39); `!          IRANK = 0` (40); `!        ENDIF` (41); `!        CALL C_MPI_ALLREDUCE_I(IRANK,IROOTS,1)` (43); `        IRANK = 0` (45); `        IF( MYRANK0 == 0 ) THEN` (47); `          IROOTC = IRANK` (48); `          DO I = 1, NPROCS0 - 1` (49); `            CALL C_MPI_RECV_I(IRANK,1,I)` (50); `            IROOTC = IROOTC + IRANK` (51); `          ENDDO` (52); `          DO I = 1, NPROCS0 - 1` (53); `            CALL C_MPI_SEND_I(IROOTC,1,I)` (54); `          ENDDO` (55); `        ELSE` (56); `          CALL C_MPI_SEND_I(IRANK,1,0)` (57); `          CALL C_MPI_RECV_I(IROOTC,1,0)` (58); `        ENDIF` (59) [11-04 전수 검증 정정] |
| 61–87 | 시작 시 1행 C_MPI_INIT 루틴·29행 `IF( NPROCS0 > NPROCS ) THEN` 참 분기 안이며 이 분기는 81행 `ENDIF`에서 닫힌다. 모델 랭크 0만 자신의 결합 랭크를 IRANK에 넣고 나머지는 0으로 설정한다(61–65). 결합 랭크 0에서 IROOTS 합산과 배포를 수행하고 다른 랭크는 송수신으로 참여한다(67–79). 29행 분기를 닫는다(81). ICPL=2이며 모델 랭크 0이면 IROOTC로부터 ISTM을 받고, 85행 `CALL M_MPI_BCAST_I(ISTM,1)`은 ICPL과 MYRANK에 관계없이 실행한다. 모델 통신자와 루트 0의 근거는 `mpi_comm/m_mpi_bcast_i.f:9`이다. 원문(연속행은 앞 문장에 이어짐): `        IF( MYRANK == 0 ) THEN` (61); `          IRANK = MYRANK0` (62); `        ELSE` (63); `          IRANK = 0` (64); `        ENDIF` (65); `        IF( MYRANK0 == 0 ) THEN` (67); `          IROOTS = IRANK` (68); `          DO I = 1, NPROCS0 - 1` (69); `            CALL C_MPI_RECV_I(IRANK,1,I)` (70); `            IROOTS = IROOTS + IRANK` (71); `          ENDDO` (72); `          DO I = 1, NPROCS0 - 1` (73); `            CALL C_MPI_SEND_I(IROOTS,1,I)` (74); `          ENDDO` (75); `        ELSE` (76); `          CALL C_MPI_SEND_I(IRANK,1,0)` (77); `          CALL C_MPI_RECV_I(IROOTS,1,0)` (78); `        ENDIF` (79); `      ENDIF` (81); `      IF( ICPL == 2 .AND. MYRANK == 0 ) CALL C_MPI_RECV_I(ISTM,1,IROOTC)` (83); `      CALL M_MPI_BCAST_I(ISTM,1)` (85); `      END` (87) [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 20–25: CGWORLD 분할의 ELSE에서도 색상 1을 사용하여 MPI_COMM_SPLIT을 호출한다. MPI_UNDFINED를 쓰는 대체 호출은 주석 처리되어 있다.
- 45–59: IRANK를 0으로 초기화한다. `MYRANK0 == 0` 분기의 50행 `CALL C_MPI_RECV_I(IRANK,1,I)`는 수신값을 IRANK에 저장한다. 51행은 그 수신값을 IROOTC에 더한다. [11-04 전수 검증 정정]
- 67–79: IROOTS는 이 루틴의 지역변수로 계산되고 배포된다. MPI_PARAM 모듈에서 가져온 변수로 선언되지 않는다.
- 27–31·83–85: ISTM 수신은 ICPL==2 .AND. MYRANK==0에서만 실행한다. ICPL=0 경로에서 이 루틴은 ISTM을 대입하지 않고 M_MPI_BCAST_I를 호출한다.
