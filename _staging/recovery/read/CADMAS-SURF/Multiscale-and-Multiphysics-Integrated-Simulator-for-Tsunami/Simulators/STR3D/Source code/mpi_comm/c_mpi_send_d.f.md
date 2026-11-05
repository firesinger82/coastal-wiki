---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/mpi_comm/c_mpi_send_d.f
lines: 13
sha256: 515067d3af9eb88d9ce7dbee8feda947af6fc546b91c655cb248c6c6158017cd
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# c_mpi_send_d.f — 판독 구간 기록

구간은 1행부터 13행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | C_MPI_SEND_D는 MPI_PARAM과 REAL*8 암묵 선언, MPI 헤더를 사용한다(3–7). DSEND(N)을 선언한다(9). CPLWORLD의 IDEST로 태그 1을 사용하여 배정밀도 자료 N개를 블로킹 송신(blocking send)한다(11). 원문(연속행은 앞 문장에 이어짐): `      SUBROUTINE C_MPI_SEND_D(DSEND,N,IDEST)` (1); `      USE MPI_PARAM` (3); `      IMPLICIT REAL*8(A-H,O-Z)` (5); `      INCLUDE 'mpif.h'` (7); `      DIMENSION DSEND(N)` (9); `      CALL MPI_SEND(DSEND,N,MPI_DOUBLE_PRECISION,IDEST,1,CPLWORLD,IERR)` (11); `      END` (13) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11: 송신 태그는 1로 고정되어 있다. IERR를 검사하는 문장은 없다.
