---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_c_mpi_allreduce_i.f
lines: 21
sha256: c579e5d52bdf7a3b673a361e826a6bfff574e0d4a907856ca8af172003665c1f
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_c_mpi_allreduce_i.f — 판독 구간 기록

구간은 1행부터 21행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | COMM_2FC_STR만 모듈에서 가져온다. IMPLICIT·mpif.h·상수/타이머 헤더·ISEND(N)·IRECV(N)를 선언한다. 타이머(timer) 상수와 공유 변수의 내용은 이 기록 묶음의 VF_ACPUTR.h에서 설명했다. 원문: `      SUBROUTINE SF_C_MPI_ALLREDUCE_I(ISEND,IRECV,N)` (1); `      USE MOD_COMM, ONLY: COMM_2FC_STR` (3); `      IMPLICIT REAL*8(A-H,O-Z)` (5); `      INCLUDE 'mpif.h'` (7); `      INCLUDE 'VF_A0PRM.h'` (9); `      INCLUDE 'VF_ACPUTR.h'` (10); `      DIMENSION ISEND(N),IRECV(N)` (12) |
| 14–21 | 시작 시 1행 SF_C_MPI_ALLREDUCE_I 루틴 안이다. VF_A2CPUT로 KCP9PL 측정을 시작하고 MPI_ALLREDUCE의 MPI_INTEGER·MPI_SUM으로 N개 정수 합을 COMM_2FC_STR 전체에 반환한다. 16–17행은 한 연속 호출이다. 측정을 종료하고 끝낸다. 타이머 시작·정지 및 합산 플래그의 근거는 같은 디렉터리의 `VF_ACPUTR.h:19–20`이다. KCP9PL의 정의는 `VF_ACPUTR.h:9,41`에 있다. 원문: `      CALL VF_A2CPUT(0,ICPUST,KCP9PL)` (14); `      CALL MPI_ALLREDUCE(ISEND,IRECV,N,MPI_INTEGER,MPI_SUM` (16); `     &                  ,COMM_2FC_STR,IERR)` (17); `      CALL VF_A2CPUT(0,ICPUEN,KCP9PL)` (19); `      END` (21) [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 16–21: MPI_ALLREDUCE의 IERR는 지역 변수로 받는다. 이 루틴에는 IERR 검사문이나 호출자 반환 인수가 없다.
