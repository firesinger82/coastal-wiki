---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/mpi_comm/m_mpi_bcast_i.f
lines: 11
sha256: daeca722f0f400560f2b9482839d592ef953d005346956ab4090f4b61b278f47
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# m_mpi_bcast_i.f — 판독 구간 기록

구간은 1행부터 11행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | M_MPI_BCAST_I는 MPI_PARAM 및 MPI 헤더를 사용한다. IBUF(N)를 선언한다(7). MYWORLD에서 루트(root) 0으로부터 정수 자료 N개를 브로드캐스트한다(9). 원문(연속행은 앞 문장에 이어짐): `      SUBROUTINE M_MPI_BCAST_I(IBUF,N)` (1); `      USE MPI_PARAM` (3); `      INCLUDE 'mpif.h'` (5); `      DIMENSION IBUF(N)` (7); `      CALL MPI_BCAST(IBUF,N,MPI_INTEGER,0,MYWORLD,IERR)` (9); `      END` (11) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 9: 브로드캐스트 루트는 0로 고정되어 있다. IERR를 검사하는 문장은 없다.
