---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_c_mpi_comm_rank.f
lines: 9
sha256: 53ad917411bd7272807a16236aa9126ef998f5e93242e36ddc37085a09756a3f
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_c_mpi_comm_rank.f — 판독 구간 기록

구간은 1행부터 9행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | COMM_2FC_STR와 mpif.h를 가져온다. MPI_COMM_RANK의 커뮤니케이터(communicator) 인수는 COMM_2FC_STR이며 결과 MYRANK를 호출자 인수로 반환한다. 별도 IMPLICIT 선언은 없다. 원문: `      SUBROUTINE SF_C_MPI_COMM_RANK(MYRANK)` (1); `      USE MOD_COMM, ONLY: COMM_2FC_STR` (3); `      INCLUDE 'mpif.h'` (5); `      CALL MPI_COMM_RANK(COMM_2FC_STR,MYRANK,IERR)` (7); `      END` (9) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 7–9: MPI_COMM_RANK의 IERR를 검사하거나 호출자 인수로 반환하지 않는다.
