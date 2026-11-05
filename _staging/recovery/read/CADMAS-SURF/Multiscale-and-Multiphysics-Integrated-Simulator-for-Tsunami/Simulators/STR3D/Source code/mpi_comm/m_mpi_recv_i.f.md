---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/mpi_comm/m_mpi_recv_i.f
lines: 11
sha256: 023c4644ea8d5bccfb4f3ee36425846a993a2e22bf3373fd4f625132453174c5
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# m_mpi_recv_i.f — 판독 구간 기록

구간은 1행부터 11행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | M_MPI_RECV_I는 MPI_PARAM 및 MPI 헤더를 사용한다. IRECV(N)과 ISTATUS(MPI_STATUS_SIZE)를 선언한다(7). MYWORLD에서 ISRC로부터 태그 1로 정수 자료 N개를 수신한다(9). 원문(연속행은 앞 문장에 이어짐): `      SUBROUTINE M_MPI_RECV_I(IRECV,N,ISRC)` (1); `      USE MPI_PARAM` (3); `      INCLUDE 'mpif.h'` (5); `      DIMENSION IRECV(N),ISTATUS(MPI_STATUS_SIZE)` (7); `      CALL MPI_RECV(IRECV,N,MPI_INTEGER,ISRC,1,MYWORLD,ISTATUS,IERR)` (9); `      END` (11) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 9: 통신 태그는 1로 고정되어 있다. IERR를 검사하는 문장은 없다.
