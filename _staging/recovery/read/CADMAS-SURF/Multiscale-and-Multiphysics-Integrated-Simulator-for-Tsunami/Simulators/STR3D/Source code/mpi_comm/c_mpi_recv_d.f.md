---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/mpi_comm/c_mpi_recv_d.f
lines: 14
sha256: c5cd056d577349e637fbfe8cab7dcdbc3cd7680d49a3d4c20b86798c3ca614f8
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# c_mpi_recv_d.f — 판독 구간 기록

구간은 1행부터 14행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | C_MPI_RECV_D는 MPI_PARAM을 사용하고 A–H/O–Z 이름을 REAL*8로 암묵 선언한다(3–5). MPI 헤더와 DRECV(N), 상태(status) 배열 ISTATUS(MPI_STATUS_SIZE)를 선언한다(7–9). CPLWORLD의 ISRC에서 태그(tag) 1로 배정밀도(double precision) N개를 블로킹 수신(blocking receive)한다(11–12). 원문(연속행은 앞 문장에 이어짐): `      SUBROUTINE C_MPI_RECV_D(DRECV,N,ISRC)` (1); `      USE MPI_PARAM` (3); `      IMPLICIT REAL*8(A-H,O-Z)` (5); `      INCLUDE 'mpif.h'` (7); `      DIMENSION DRECV(N),ISTATUS(MPI_STATUS_SIZE)` (9); `      CALL MPI_RECV(DRECV,N,MPI_DOUBLE_PRECISION,ISRC,1,CPLWORLD` (11); `     &             ,ISTATUS,IERR)` (12); `      END` (14) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11–12: 수신 태그는 1로 고정되어 있다. IERR를 검사하는 문장은 없다.
