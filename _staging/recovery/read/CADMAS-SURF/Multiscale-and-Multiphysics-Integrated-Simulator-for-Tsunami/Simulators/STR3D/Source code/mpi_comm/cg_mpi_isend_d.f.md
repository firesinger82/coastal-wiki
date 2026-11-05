---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/mpi_comm/cg_mpi_isend_d.f
lines: 14
sha256: f6a2468f1cd3340899a024ccc2b55d09f3a1be4972968b47462c8b3a981da0e4
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# cg_mpi_isend_d.f — 판독 구간 기록

구간은 1행부터 14행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | CG_MPI_ISEND_D는 MPI_PARAM, REAL*8 암묵 선언 및 MPI 헤더를 사용한다(3–7). 길이 N 자료 배열을 선언한다(9). CGWORLD에서 태그 0으로 배정밀도 자료 N개를 비블로킹 송신(nonblocking send)하고 요청 핸들을 IREQ로 받는다(11–12). 원문(연속행은 앞 문장에 이어짐): `      SUBROUTINE CG_MPI_ISEND_D(DSEND,N,IDEST,IREQ)` (1); `      USE MPI_PARAM` (3); `      IMPLICIT REAL*8(A-H,O-Z)` (5); `      INCLUDE 'mpif.h'` (7); `      DIMENSION DSEND(N)` (9); `      CALL MPI_ISEND(DSEND,N,MPI_DOUBLE_PRECISION,IDEST,0,CGWORLD,IREQ` (11); `     &              ,IERR)` (12); `      END` (14) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11–12: 통신 태그는 0으로 고정되어 있다. 이 루틴에는 요청 완료 대기문과 IERR 검사문이 없다.
