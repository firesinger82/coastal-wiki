---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/mpi_comm/cg_mpi_allreduce_d.f
lines: 23
sha256: 9099b104c929188f0d50325657c37c8c9b995fe2834cc5b223308c44f9824bd3
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# cg_mpi_allreduce_d.f — 판독 구간 기록

구간은 1행부터 23행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–23 | CG_MPI_ALLREDUCE_D는 MPI_PARAM, REAL*8 암묵 선언 및 MPI 헤더를 사용한다(3–7). 길이 N 송수신 배열을 선언한다(9). IOP=0/1/2에 대해 MPI_SUM/MPI_MAX/MPI_MIN을 고르고 CGWORLD에서 배정밀도 전체 축약을 호출한다(11–21). 원문(연속행은 앞 문장에 이어짐): `      SUBROUTINE CG_MPI_ALLREDUCE_D(DSEND,DRECV,N,IOP)` (1); `      USE MPI_PARAM` (3); `      IMPLICIT REAL*8(A-H,O-Z)` (5); `      INCLUDE 'mpif.h'` (7); `      DIMENSION DSEND(N),DRECV(N)` (9); `      SELECT CASE( IOP )` (11); `      CASE( 0 )` (12); `        MPI_OP = MPI_SUM` (13); `      CASE( 1 )` (14); `        MPI_OP = MPI_MAX` (15); `      CASE( 2 )` (16); `        MPI_OP = MPI_MIN` (17); `      END SELECT` (18); `      CALL MPI_ALLREDUCE(DSEND,DRECV,N,MPI_DOUBLE_PRECISION,MPI_OP` (20); `     &                  ,CGWORLD,IERR)` (21); `      END` (23) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11–18: SELECT CASE에는 CASE(0), CASE(1), CASE(2)만 있다. 다른 IOP에 대한 CASE DEFAULT나 MPI_OP 기본값 대입은 없다.
