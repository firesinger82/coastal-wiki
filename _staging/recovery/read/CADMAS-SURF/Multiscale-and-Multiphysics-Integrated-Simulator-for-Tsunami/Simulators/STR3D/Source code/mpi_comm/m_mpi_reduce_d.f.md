---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/mpi_comm/m_mpi_reduce_d.f
lines: 23
sha256: 9839139cc6c972e82f477e797caf6d3b3b1a99fd5cac7af9136f1ac6e8fd3092
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# m_mpi_reduce_d.f — 판독 구간 기록

구간은 1행부터 23행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–23 | M_MPI_REDUCE_D는 MPI_PARAM, REAL*8 암묵 선언 및 MPI 헤더를 사용한다(3–7). DSEND(N)/DRECV(N)을 선언한다(9). SELECT CASE의 IOP=0/1/2에서 MPI_SUM/MPI_MAX/MPI_MIN을 선택한다(11–18). MYWORLD의 루트 0으로 배정밀도 자료 N개를 축약(reduce)한다(20–21). 원문(연속행은 앞 문장에 이어짐): `      SUBROUTINE M_MPI_REDUCE_D(DSEND,DRECV,N,IOP)` (1); `      USE MPI_PARAM` (3); `      IMPLICIT REAL*8(A-H,O-Z)` (5); `      INCLUDE 'mpif.h'` (7); `      DIMENSION DSEND(N),DRECV(N)` (9); `      SELECT CASE( IOP )` (11); `      CASE( 0 )` (12); `        MPI_OP = MPI_SUM` (13); `      CASE( 1 )` (14); `        MPI_OP = MPI_MAX` (15); `      CASE( 2 )` (16); `        MPI_OP = MPI_MIN` (17); `      END SELECT` (18); `      CALL MPI_REDUCE(DSEND,DRECV,N,MPI_DOUBLE_PRECISION,MPI_OP,0` (20); `     &               ,MYWORLD,IERR)` (21); `      END` (23) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11–18: CASE DEFAULT와 MPI_OP의 기본값 대입은 없다.
- 20–21: MPI_REDUCE의 루트는 0으로 고정되어 있다.
