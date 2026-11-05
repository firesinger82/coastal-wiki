---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_stm_c_mpi_comm_rank.f
lines: 9
sha256: 968f662a91d3cc5d9014e6e0999b4d132799e87a361d924097d13c6e5f3ce827
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_stm_c_mpi_comm_rank.f — 판독 구간 기록

구간은 1행부터 9행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | MOD_COMM의 COMM_2FC_STM만 가져온다(3). mpif.h를 포함한다(5). MPI_COMM_RANK로 해당 통신자(communicator)의 순위를 MYRANK에 받는다(7). 원문(연속 표시는 앞 문장에 이어짐): `      SUBROUTINE SF_STM_C_MPI_COMM_RANK(MYRANK)` (1); `      USE MOD_COMM, ONLY: COMM_2FC_STM` (3); `      INCLUDE 'mpif.h'` (5); `      CALL MPI_COMM_RANK(COMM_2FC_STM,MYRANK,IERR)` (7); `      END` (9). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 7: MPI_COMM_RANK는 IERR를 받지만 이 루틴에는 IERR 검사문이 없다.
