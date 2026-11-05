---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_c_mpi_send_i.f
lines: 21
sha256: ffb1613c4926bec35c49ecb05f0e8f0cdf5a9b99bb0f13411f8f036c8733c2f4
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_c_mpi_send_i.f — 판독 구간 기록

구간은 1행부터 21행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | COMM_2FC_STR를 가져오고 IMPLICIT·mpif.h·상수/타이머 헤더를 포함한다. 정수 ISEND(N)을 선언한다. 헤더의 상수·공유 목록은 이 묶음의 해당 헤더 기록에서 설명했다. 원문: `      SUBROUTINE SF_C_MPI_SEND_I(ISEND,N,IDEST)` (1); `      USE MOD_COMM, ONLY: COMM_2FC_STR` (3); `      IMPLICIT REAL*8(A-H,O-Z)` (5); `      INCLUDE 'mpif.h'` (7); `      INCLUDE 'VF_A0PRM.h'` (9); `      INCLUDE 'VF_ACPUTR.h'` (10); `      DIMENSION ISEND(N)` (12) |
| 14–21 | 시작 시 1행 SF_C_MPI_SEND_I 루틴 안이다. VF_A2CPUT로 KCP9PL 측정을 시작한다. MPI_SEND의 16–17행은 하나의 고정형식 연속 호출이다. COMM_2FC_STR에서 IDEST를 대상으로 태그(tag) 1의 정수 원소 N개를 송신한다. 측정 종료 후 루틴을 끝낸다. 타이머 시작·정지 및 합산 플래그의 근거는 같은 디렉터리의 `VF_ACPUTR.h:19–20`이다. KCP9PL의 정의는 `VF_ACPUTR.h:9,41`에 있다. 원문: `      CALL VF_A2CPUT(0,ICPUST,KCP9PL)` (14); `      CALL MPI_SEND(ISEND,N,MPI_INTEGER,IDEST,1,COMM_2FC_STR` (16); `     &             ,IERR)` (17); `      CALL VF_A2CPUT(0,ICPUEN,KCP9PL)` (19); `      END` (21) [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 16–21: 통신 태그는 상수 1이다. IERR는 지역 변수로 받으며 검사문이나 호출자 반환 인수가 없다.
