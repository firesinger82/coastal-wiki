---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_c_mpi_comm_size.f
lines: 9
sha256: 4df38d936852488b579dad646adc4a290dfc596d1d259e20310b9cbf67050c82
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_c_mpi_comm_size.f — 판독 구간 기록

구간은 1행부터 9행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | COMM_2FC_STR와 mpif.h를 가져온다. MPI_COMM_SIZE의 커뮤니케이터(communicator) 인수는 COMM_2FC_STR이며 크기 NPROCS를 호출자 인수로 반환한다. 별도 IMPLICIT 선언은 없다. 원문: `      SUBROUTINE SF_C_MPI_COMM_SIZE(NPROCS)` (1); `      USE MOD_COMM, ONLY: COMM_2FC_STR` (3); `      INCLUDE 'mpif.h'` (5); `      CALL MPI_COMM_SIZE(COMM_2FC_STR,NPROCS,IERR)` (7); `      END` (9) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 7–9: MPI_COMM_SIZE의 IERR를 검사하거나 호출자 인수로 반환하지 않는다.
