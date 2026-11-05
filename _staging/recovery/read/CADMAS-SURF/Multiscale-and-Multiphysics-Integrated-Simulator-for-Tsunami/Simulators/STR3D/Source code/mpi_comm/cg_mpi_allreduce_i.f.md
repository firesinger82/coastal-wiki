---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/mpi_comm/cg_mpi_allreduce_i.f
lines: 22
sha256: 15ad58997395b887d4556a0f0c2adf514033d58a08ff1bdb9cc57ed21576493a
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# cg_mpi_allreduce_i.f — 판독 구간 기록

구간은 1행부터 22행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | CG_MPI_ALLREDUCE_I는 MPI_PARAM, REAL*8 암묵 선언 및 MPI 헤더를 사용한다(3–7). 정수 이름 ISEND/IRECV의 길이는 N이다(9). IOP=0/1/2에 따라 MPI_SUM/MPI_MAX/MPI_MIN을 골라 CGWORLD에서 정수 전체 축약을 호출한다(11–20). 원문(연속행은 앞 문장에 이어짐): `      SUBROUTINE CG_MPI_ALLREDUCE_I(ISEND,IRECV,N,IOP)` (1); `      USE MPI_PARAM` (3); `      IMPLICIT REAL*8(A-H,O-Z)` (5); `      INCLUDE 'mpif.h'` (7); `      DIMENSION ISEND(N),IRECV(N)` (9); `      SELECT CASE( IOP )` (11); `      CASE( 0 )` (12); `        MPI_OP = MPI_SUM` (13); `      CASE( 1 )` (14); `        MPI_OP = MPI_MAX` (15); `      CASE( 2 )` (16); `        MPI_OP = MPI_MIN` (17); `      END SELECT` (18); `      CALL MPI_ALLREDUCE(ISEND,IRECV,N,MPI_INTEGER,MPI_OP,CGWORLD,IERR)` (20); `      END` (22) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11–18: SELECT CASE에는 CASE(0), CASE(1), CASE(2)만 있다. 다른 IOP에 대한 CASE DEFAULT나 MPI_OP 기본값 대입은 없다.
