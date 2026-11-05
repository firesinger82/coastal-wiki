---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_mpi_waitall.f
lines: 9
sha256: f757c0a66824e6c4a2a563c967d7463222219a6d4a7f8553540d9f08d0534e34
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_mpi_waitall.f — 판독 구간 기록

구간은 1행부터 9행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | SF_MPI_WAITALL은 크기 N의 IREQ를 받아 MPI_WAITALL을 호출한다(1·5·7). ISTATUS의 선언 범위는 MPI_STATUS_SIZE이다(5). 원문(연속 표시는 앞 문장에 이어짐): `      SUBROUTINE SF_MPI_WAITALL(N,IREQ)` (1); `      INCLUDE 'mpif.h'` (3); `      DIMENSION IREQ(N),ISTATUS(MPI_STATUS_SIZE)` (5); `      CALL MPI_WAITALL(N,IREQ,ISTATUS,IERR)` (7); `      END` (9). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 5·7: 요청 배열은 IREQ(N)이지만 상태 배열 선언은 ISTATUS(MPI_STATUS_SIZE)이며 N 차원이 없다.
- 7: MPI_WAITALL의 IERR를 검사하는 문장은 이 루틴에 없다.
