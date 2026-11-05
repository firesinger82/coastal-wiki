---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_mpi_send_d.f
lines: 19
sha256: d349e2dc78f24e0a2378c8a9e38d68ae01628b29a11a3b42cf10f0f242a52c06
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_mpi_send_d.f — 판독 구간 기록

구간은 1행부터 19행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | SF_MPI_SEND_D의 선언부다. 전송 배열 DSEND의 크기는 N이다. 원문(연속 표시는 앞 문장에 이어짐): `      SUBROUTINE SF_MPI_SEND_D(DSEND,N,IDEST)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      INCLUDE 'mpif.h'` (5); `      INCLUDE 'VF_A0PRM.h'` (7); `      INCLUDE 'VF_ACPUTR.h'` (8); `      INCLUDE 'VF_APARAI.h'` (9); `      DIMENSION DSEND(N)` (11). |
| 12–19 | 시작 시 1행 SF_MPI_SEND_D 루틴 안. VF_A2CPUT 호출 사이에서 배정밀도 N개를 MGCOMM의 IDEST로 전송한다(13–17). MPI_SEND의 태그(tag)는 1이다(15). 원문(연속 표시는 앞 문장에 이어짐): `      CALL VF_A2CPUT(0,ICPUST,KCP9PL)` (13); `      CALL MPI_SEND(DSEND,N,MPI_DOUBLE_PRECISION,IDEST,1,MGCOMM,IERR)` (15); `      CALL VF_A2CPUT(0,ICPUEN,KCP9PL)` (17); `      END` (19). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 15: MPI_SEND의 태그는 상수 1이며 IERR를 검사하는 문장은 이 루틴에 없다.
