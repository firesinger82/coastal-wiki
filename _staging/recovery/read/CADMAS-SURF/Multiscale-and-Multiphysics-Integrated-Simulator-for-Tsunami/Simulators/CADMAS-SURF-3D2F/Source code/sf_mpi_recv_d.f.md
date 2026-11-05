---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_mpi_recv_d.f
lines: 20
sha256: 350d3a25149ee815dec2caf8a5f40dba9652ce684d2cc3cd73db2b7e2e9ceae0
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_mpi_recv_d.f — 판독 구간 기록

구간은 1행부터 20행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | SF_MPI_RECV_D 선언과 실수 배열 범위(1–11). mpif.h와 실행 환경 INCLUDE 세 개를 포함한다(5–9). VF_A2CPUT 시작·종료 호출 사이에서 블로킹(blocking) 수신을 게시한다(13–18). MPI_RECV의 자료형은 MPI_DOUBLE_PRECISION이고 개수는 N이다(15–16). 상대는 ISRC, 태그(tag)는 1, 통신자(communicator)는 MGCOMM이다. 상태 배열 ISTATUS(MPI_STATUS_SIZE)를 전달한다(11·15–16). 원문: `      SUBROUTINE SF_MPI_RECV_D(DRECV,N,ISRC)` (1)<br>`      IMPLICIT REAL*8(A-H,O-Z)` (3)<br>`      INCLUDE 'mpif.h'` (5)<br>`      INCLUDE 'VF_A0PRM.h'` (7)<br>`      INCLUDE 'VF_ACPUTR.h'` (8)<br>`      INCLUDE 'VF_APARAI.h'` (9)<br>`      DIMENSION DRECV(N),ISTATUS(MPI_STATUS_SIZE)` (11)<br>`      CALL VF_A2CPUT(0,ICPUST,KCP9PL)` (13)<br>연속문: `      CALL MPI_RECV(DRECV,N,MPI_DOUBLE_PRECISION,ISRC,1,MGCOMM,ISTATUS` (15); `     &             ,IERR)` (16)<br>`      CALL VF_A2CPUT(0,ICPUEN,KCP9PL)` (18)<br>`      END` (20) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 15–16: 통신 태그(tag)는 상수 1이다. MPI 호출이 IERR를 받지만 이 파일에는 IERR 조건 검사가 없다.
