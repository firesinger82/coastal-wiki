---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_mpi_irecv_i.f
lines: 19
sha256: 6ae8258c59a3b94434b4129b6bdab8212e2bc4453af7bde903ca8519ae253160
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_mpi_irecv_i.f — 판독 구간 기록

구간은 1행부터 19행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | SF_MPI_IRECV_I 선언과 정수 배열 범위(1–11). mpif.h와 실행 환경 INCLUDE 세 개를 포함한다(5–9). VF_A2CPUT 시작·종료 호출 사이에서 비차단(nonblocking) 수신을 게시한다(13–17). MPI_IRECV의 자료형은 MPI_INTEGER이고 개수는 N이다(15). 상대는 ISRC, 태그(tag)는 1, 통신자(communicator)는 MGCOMM이다. 요청 핸들(request handle)을 IREQ로 돌려준다. 완료 대기는 이 루틴에 없다. 원문: `      SUBROUTINE SF_MPI_IRECV_I(IRECV,N,ISRC,IREQ)` (1)<br>`      IMPLICIT REAL*8(A-H,O-Z)` (3)<br>`      INCLUDE 'mpif.h'` (5)<br>`      INCLUDE 'VF_A0PRM.h'` (7)<br>`      INCLUDE 'VF_ACPUTR.h'` (8)<br>`      INCLUDE 'VF_APARAI.h'` (9)<br>`      DIMENSION IRECV(N)` (11)<br>`      CALL VF_A2CPUT(0,ICPUST,KCP9PL)` (13)<br>`      CALL MPI_IRECV(IRECV,N,MPI_INTEGER,ISRC,1,MGCOMM,IREQ,IERR)` (15)<br>`      CALL VF_A2CPUT(0,ICPUEN,KCP9PL)` (17)<br>`      END` (19) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 15: 통신 태그(tag)는 상수 1이다. MPI 호출이 IERR를 받지만 이 파일에는 IERR 조건 검사가 없다.
