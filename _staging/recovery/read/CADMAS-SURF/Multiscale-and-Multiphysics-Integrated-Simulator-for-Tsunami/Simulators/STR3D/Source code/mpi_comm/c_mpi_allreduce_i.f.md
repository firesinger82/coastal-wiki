---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/mpi_comm/c_mpi_allreduce_i.f
lines: 12
sha256: bf9bfffa9bcf160d7c1a69c3f18100a0dd4e80bc8f73c445558a70b49bc07614
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# c_mpi_allreduce_i.f — 판독 구간 기록

구간은 1행부터 12행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | C_MPI_ALLREDUCE_I는 MPI_PARAM과 MPI 헤더를 사용한다(1–5). 길이 N 정수 송수신 배열을 선언한다(7). CPLWORLD에서 MPI_INTEGER 자료 N개를 MPI_SUM으로 전체 축약(all-reduce)하여 IRECV에 돌려준다(9–10). 원문(연속행은 앞 문장에 이어짐): `      SUBROUTINE C_MPI_ALLREDUCE_I(ISEND,IRECV,N)` (1); `      USE MPI_PARAM` (3); `      INCLUDE 'mpif.h'` (5); `      DIMENSION ISEND(N),IRECV(N)` (7); `      CALL MPI_ALLREDUCE(ISEND,IRECV,N,MPI_INTEGER,MPI_SUM,CPLWORLD` (9); `     &                  ,IERR)` (10); `      END` (12) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 9–10: MPI_ALLREDUCE의 IERR를 받지만 이 루틴에는 오류값 검사문이 없다.
