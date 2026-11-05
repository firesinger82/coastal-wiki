---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_mpi_reduce_i.f
lines: 24
sha256: 53853037c50ddfd384e09ff5bec07f7f29676fcdb44b9cadaf7c84a916945b84
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_mpi_reduce_i.f — 판독 구간 기록

구간은 1행부터 24행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | SF_MPI_REDUCE_I의 선언부다. ISEND와 IRECV는 크기 N의 정수 배열이다. 원문(연속 표시는 앞 문장에 이어짐): `      SUBROUTINE SF_MPI_REDUCE_I(ISEND,IRECV,N,IROOT)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      INCLUDE 'mpif.h'` (5); `      INCLUDE 'VF_A0PRM.h'` (7); `      INCLUDE 'VF_ACPUTR.h'` (8); `      INCLUDE 'VF_APARAI.h'` (9); `      DIMENSION ISEND(N),IRECV(N)` (11). |
| 13–24 | 시작 시 1행 SF_MPI_REDUCE_I 루틴 안. 분기 전후에 VF_A2CPUT을 호출한다(13·22). NPROCS가 1보다 크면 MGCOMM의 IROOT에 정수 MPI 합 리덕션(reduction)을 수행한다(15–17). 그 외에는 배열을 복사한다(18–20). 원문(연속 표시는 앞 문장에 이어짐): `      CALL VF_A2CPUT(0,ICPUST,KCP9PL)` (13); `      IF( NPROCS > 1 ) THEN` (15); `        CALL MPI_REDUCE(ISEND,IRECV,N,MPI_INTEGER,MPI_SUM,IROOT,MGCOMM` (16); `     &                 ,IERR)` (17); `      ELSE` (18); `        IRECV = ISEND` (19); `      ENDIF` (20); `      CALL VF_A2CPUT(0,ICPUEN,KCP9PL)` (22); `      END` (24). 해석: VF_A2CPUT 호출은 통신 전후 시간 계측으로 읽힌다. [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 16–17: MPI_REDUCE는 IERR를 받지만 이 루틴에는 IERR 조건 검사가 없다.
