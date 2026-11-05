---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_mpi_allreduce_i.f
lines: 33
sha256: 34951f73897142068abbede18084cbf5b4aa6bc9e31dfc488f47591cdc81f7aa
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_mpi_allreduce_i.f — 판독 구간 기록

구간은 1행부터 33행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–33 | SF_MPI_ALLREDUCE_I 선언과 정수 배열 범위(1–11). mpif.h와 실행 환경 INCLUDE 세 개를 포함한다(5–9). VF_A2CPUT 시작·종료 호출 사이에서 전역 축약(all-reduce)을 수행한다(13–31). IOP=0·1·2는 각각 MPI_SUM·MPI_MAX·MPI_MIN이다(15–22). NPROCS>1이면 MPI_INTEGER 자료형과 MGCOMM으로 MPI_ALLREDUCE를 호출하고, 그 밖에는 ISEND를 IRECV에 직접 복사한다(24–29). 원문: `      SUBROUTINE SF_MPI_ALLREDUCE_I(ISEND,IRECV,N,IOP)` (1)<br>`      IMPLICIT REAL*8(A-H,O-Z)` (3)<br>`      INCLUDE 'mpif.h'` (5)<br>`      INCLUDE 'VF_A0PRM.h'` (7)<br>`      INCLUDE 'VF_ACPUTR.h'` (8)<br>`      INCLUDE 'VF_APARAI.h'` (9)<br>`      DIMENSION ISEND(N),IRECV(N)` (11)<br>`      CALL VF_A2CPUT(0,ICPUST,KCP9PL)` (13)<br>`      SELECT CASE( IOP )` (15)<br>`      CASE( 0 )` (16)<br>`        MPI_OP = MPI_SUM` (17)<br>`      CASE( 1 )` (18)<br>`        MPI_OP = MPI_MAX` (19)<br>`      CASE( 2 )` (20)<br>`        MPI_OP = MPI_MIN` (21)<br>`      END SELECT` (22)<br>`      IF( NPROCS > 1 ) THEN` (24)<br>연속문: `        CALL MPI_ALLREDUCE(ISEND,IRECV,N,MPI_INTEGER,MPI_OP,MGCOMM` (25); `     &                    ,IERR)` (26)<br>`      ELSE` (27)<br>`        IRECV = ISEND` (28)<br>`      ENDIF` (29)<br>`      CALL VF_A2CPUT(0,ICPUEN,KCP9PL)` (31)<br>`      END` (33) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 15–26: IOP 선택문에는 CASE DEFAULT가 없고 MPI_OP의 사전 초기화가 없다.
- 25–31: MPI_ALLREDUCE가 IERR를 받지만 이 파일에는 IERR 조건 검사가 없다.
