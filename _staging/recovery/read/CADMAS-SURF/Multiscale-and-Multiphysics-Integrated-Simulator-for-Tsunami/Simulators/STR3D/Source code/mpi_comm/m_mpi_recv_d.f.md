---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/mpi_comm/m_mpi_recv_d.f
lines: 14
sha256: 417d27e7e829e7ae41025964ce54c6193871428b11229c62c0f73a92282c90ac
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# m_mpi_recv_d.f — 판독 구간 기록

구간은 1행부터 14행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | M_MPI_RECV_D는 MPI_PARAM, REAL*8 암묵 선언 및 MPI 헤더를 사용한다. DRECV(N)과 ISTATUS(MPI_STATUS_SIZE)를 선언한다(9). MYWORLD에서 ISRC로부터 태그 1로 배정밀도 자료 N개를 수신한다(11–12). 원문(연속행은 앞 문장에 이어짐): `      SUBROUTINE M_MPI_RECV_D(DRECV,N,ISRC)` (1); `      USE MPI_PARAM` (3); `      IMPLICIT REAL*8(A-H,O-Z)` (5); `      INCLUDE 'mpif.h'` (7); `      DIMENSION DRECV(N),ISTATUS(MPI_STATUS_SIZE)` (9); `      CALL MPI_RECV(DRECV,N,MPI_DOUBLE_PRECISION,ISRC,1,MYWORLD,ISTATUS` (11); `     &             ,IERR)` (12); `      END` (14) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11–12: 통신 태그는 1로 고정되어 있다. IERR를 검사하는 문장은 없다.
