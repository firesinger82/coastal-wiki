---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_mpi_irecv_d.f
lines: 20
sha256: a4edadfc71d6f6786cee82dc28c510bdb23130c717f16165eea2ffbb7539b5e8
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_mpi_irecv_d.f — 판독 구간 기록

구간은 1행부터 20행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | SF_MPI_IRECV_D 선언과 실수 배열 범위(1–11). mpif.h와 실행 환경 INCLUDE 세 개를 포함한다(5–9). VF_A2CPUT 시작·종료 호출 사이에서 비차단(nonblocking) 수신을 게시한다(13–18). MPI_IRECV의 자료형은 MPI_DOUBLE_PRECISION이고 개수는 N이다(15–16). 상대는 ISRC, 태그(tag)는 1, 통신자(communicator)는 MGCOMM이다. 요청 핸들(request handle)을 IREQ로 돌려준다. 완료 대기는 이 루틴에 없다. 원문: `      SUBROUTINE SF_MPI_IRECV_D(DRECV,N,ISRC,IREQ)` (1)<br>`      IMPLICIT REAL*8(A-H,O-Z)` (3)<br>`      INCLUDE 'mpif.h'` (5)<br>`      INCLUDE 'VF_A0PRM.h'` (7)<br>`      INCLUDE 'VF_ACPUTR.h'` (8)<br>`      INCLUDE 'VF_APARAI.h'` (9)<br>`      DIMENSION DRECV(N)` (11)<br>`      CALL VF_A2CPUT(0,ICPUST,KCP9PL)` (13)<br>연속문: `      CALL MPI_IRECV(DRECV,N,MPI_DOUBLE_PRECISION,ISRC,1,MGCOMM,IREQ` (15); `     &              ,IERR)` (16)<br>`      CALL VF_A2CPUT(0,ICPUEN,KCP9PL)` (18)<br>`      END` (20) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 15–16: 통신 태그(tag)는 상수 1이다. MPI 호출이 IERR를 받지만 이 파일에는 IERR 조건 검사가 없다.
