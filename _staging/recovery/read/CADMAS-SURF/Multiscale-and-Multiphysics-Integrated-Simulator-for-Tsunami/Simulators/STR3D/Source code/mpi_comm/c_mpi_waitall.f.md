---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/mpi_comm/c_mpi_waitall.f
lines: 9
sha256: ce089fc1e9b7a9bfc00dc4319dd5dea26747bce8049efb7f4e04ff93c5584a8b
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# c_mpi_waitall.f — 판독 구간 기록

구간은 1행부터 9행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | C_MPI_WAITALL은 MPI 헤더를 포함한다(3). 길이 N의 요청(request) 배열 IREQ와 상태 배열 ISTATUS(MPI_STATUS_SIZE)를 선언한다(5). MPI_WAITALL에 N개 요청을 넘겨 완료를 기다린다(7). 원문(연속행은 앞 문장에 이어짐): `      SUBROUTINE C_MPI_WAITALL(N,IREQ)` (1); `      INCLUDE 'mpif.h'` (3); `      DIMENSION IREQ(N),ISTATUS(MPI_STATUS_SIZE)` (5); `      CALL MPI_WAITALL(N,IREQ,ISTATUS,IERR)` (7); `      END` (9) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 5·7: 요청 배열은 IREQ(N)으로 선언하고 상태 배열은 ISTATUS(MPI_STATUS_SIZE)로 선언한다. 상태 배열 선언에는 N 차원이 없다.
