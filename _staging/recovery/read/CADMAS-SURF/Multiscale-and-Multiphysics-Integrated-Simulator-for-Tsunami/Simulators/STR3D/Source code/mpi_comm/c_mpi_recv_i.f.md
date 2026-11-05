---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/mpi_comm/c_mpi_recv_i.f
lines: 11
sha256: 80a29ed22eeb6e82bed51bc76f302949398d61a24f40485b2c9ce002ec6933cc
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# c_mpi_recv_i.f — 판독 구간 기록

구간은 1행부터 11행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | C_MPI_RECV_I는 MPI_PARAM과 MPI 헤더를 사용한다(3–5). IRECV(N)와 ISTATUS(MPI_STATUS_SIZE)를 선언한다(7). CPLWORLD의 ISRC에서 태그 1로 정수 N개를 블로킹 수신한다(9). 원문(연속행은 앞 문장에 이어짐): `      SUBROUTINE C_MPI_RECV_I(IRECV,N,ISRC)` (1); `      USE MPI_PARAM` (3); `      INCLUDE 'mpif.h'` (5); `      DIMENSION IRECV(N),ISTATUS(MPI_STATUS_SIZE)` (7); `      CALL MPI_RECV(IRECV,N,MPI_INTEGER,ISRC,1,CPLWORLD,ISTATUS,IERR)` (9); `      END` (11) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 9: 수신 태그는 1로 고정되어 있다. IERR를 검사하는 문장은 없다.
