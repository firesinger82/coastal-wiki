---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/mpi_comm/m_mpi_send_i.f
lines: 11
sha256: c6c2d400a588a0fd5581b991d99d90c0482364707a4c71f4d6acdf9dd62ddbeb
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# m_mpi_send_i.f — 판독 구간 기록

구간은 1행부터 11행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | M_MPI_SEND_I는 MPI_PARAM 및 MPI 헤더를 사용한다. ISEND(N)를 선언한다(7). MYWORLD에서 IDEST로 태그 1을 사용하여 정수 자료 N개를 송신한다(9). 원문(연속행은 앞 문장에 이어짐): `      SUBROUTINE M_MPI_SEND_I(ISEND,N,IDEST)` (1); `      USE MPI_PARAM` (3); `      INCLUDE 'mpif.h'` (5); `      DIMENSION ISEND(N)` (7); `      CALL MPI_SEND(ISEND,N,MPI_INTEGER,IDEST,1,MYWORLD,IERR)` (9); `      END` (11) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 9: 통신 태그는 1로 고정되어 있다. IERR를 검사하는 문장은 없다.
