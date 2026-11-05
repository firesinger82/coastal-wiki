---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_stm_c_mpi_recv_d.f
lines: 21
sha256: a0714dc83d07517249873e01b0d3f6d67a33881748373ffd84c4eb89a5099947
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_stm_c_mpi_recv_d.f — 판독 구간 기록

구간은 1행부터 21행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | SF_STM_C_MPI_RECV_D의 선언부다. 통신자(communicator) COMM_2FC_STM을 사용한다(3). DRECV 크기는 N이고 ISTATUS 크기는 MPI_STATUS_SIZE다(12). 원문(연속 표시는 앞 문장에 이어짐): `      SUBROUTINE SF_STM_C_MPI_RECV_D(DRECV,N,ISRC)` (1); `      USE MOD_COMM, ONLY: COMM_2FC_STM` (3); `      IMPLICIT REAL*8(A-H,O-Z)` (5); `      INCLUDE 'mpif.h'` (7); `      INCLUDE 'VF_A0PRM.h'` (9); `      INCLUDE 'VF_ACPUTR.h'` (10); `      DIMENSION DRECV(N),ISTATUS(MPI_STATUS_SIZE)` (12). |
| 14–21 | 시작 시 1행 SF_STM_C_MPI_RECV_D 루틴 안. SF_STM_C_MPI_RECV_D 안. VF_A2CPUT 호출 사이에서 ISRC의 배정밀도 N개를 태그(tag) 1로 수신한다(14–19). MPI_RECV의 인수와 연속문을 그대로 적는다(16–17). 원문(연속 표시는 앞 문장에 이어짐): `      CALL VF_A2CPUT(0,ICPUST,KCP9PL)` (14); `      CALL MPI_RECV(DRECV,N,MPI_DOUBLE_PRECISION,ISRC,1,COMM_2FC_STM` (16); `     &             ,ISTATUS,IERR)` (17); `      CALL VF_A2CPUT(0,ICPUEN,KCP9PL)` (19); `      END` (21). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 16–17: MPI_RECV의 태그는 1이다. IERR를 검사하는 문장은 이 루틴에 없다.
