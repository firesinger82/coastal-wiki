---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/mpi_comm/c_mpi_send_i.f
lines: 11
sha256: 3ecab607ee43bb76f48b8517bf94640dd4514ba07270999cef0fe8ea07af8d2c
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# c_mpi_send_i.f — 판독 구간 기록

구간은 1행부터 11행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | C_MPI_SEND_I는 MPI_PARAM과 MPI 헤더를 사용하고 ISEND(N)을 선언한다(3–7). CPLWORLD의 IDEST로 태그 1을 사용하여 정수 N개를 블로킹 송신한다(9). 원문(연속행은 앞 문장에 이어짐): `      SUBROUTINE C_MPI_SEND_I(ISEND,N,IDEST)` (1); `      USE MPI_PARAM` (3); `      INCLUDE 'mpif.h'` (5); `      DIMENSION ISEND(N)` (7); `      CALL MPI_SEND(ISEND,N,MPI_INTEGER,IDEST,1,CPLWORLD,IERR)` (9); `      END` (11) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 9: 송신 태그는 1로 고정되어 있다. IERR를 검사하는 문장은 없다.
