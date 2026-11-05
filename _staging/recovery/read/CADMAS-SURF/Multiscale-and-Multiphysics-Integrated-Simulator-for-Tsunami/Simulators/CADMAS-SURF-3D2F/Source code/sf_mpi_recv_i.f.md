---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_mpi_recv_i.f
lines: 19
sha256: 33043e56306d0e01a0ab6eb9a34f13db64c5f3dd564e2436d4e01be5d332cdbc
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_mpi_recv_i.f — 판독 구간 기록

구간은 1행부터 19행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | SF_MPI_RECV_I 선언과 정수 배열 범위(1–11). mpif.h와 실행 환경 INCLUDE 세 개를 포함한다(5–9). VF_A2CPUT 시작·종료 호출 사이에서 블로킹(blocking) 수신을 게시한다(13–17). MPI_RECV의 자료형은 MPI_INTEGER이고 개수는 N이다(15). 상대는 ISRC, 태그(tag)는 1, 통신자(communicator)는 MGCOMM이다. 상태 배열 ISTATUS(MPI_STATUS_SIZE)를 전달한다(11·15). 원문: `      SUBROUTINE SF_MPI_RECV_I(IRECV,N,ISRC)` (1)<br>`      IMPLICIT REAL*8(A-H,O-Z)` (3)<br>`      INCLUDE 'mpif.h'` (5)<br>`      INCLUDE 'VF_A0PRM.h'` (7)<br>`      INCLUDE 'VF_ACPUTR.h'` (8)<br>`      INCLUDE 'VF_APARAI.h'` (9)<br>`      DIMENSION IRECV(N),ISTATUS(MPI_STATUS_SIZE)` (11)<br>`      CALL VF_A2CPUT(0,ICPUST,KCP9PL)` (13)<br>`      CALL MPI_RECV(IRECV,N,MPI_INTEGER,ISRC,1,MGCOMM,ISTATUS,IERR)` (15)<br>`      CALL VF_A2CPUT(0,ICPUEN,KCP9PL)` (17)<br>`      END` (19) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 15: 통신 태그(tag)는 상수 1이다. MPI 호출이 IERR를 받지만 이 파일에는 IERR 조건 검사가 없다.
