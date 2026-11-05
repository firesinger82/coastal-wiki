---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/module/mpi_param.f90
lines: 10
sha256: 22039426a08bac8ca89f11fc2e24f2218e3138ec0367a1a3f4678db80d283055
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# mpi_param.f90 — 판독 구간 기록

구간은 1행부터 10행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | MPI_PARAM 모듈과 `IMPLICIT NONE` (3)을 선언한다. 해석: 결합 통신자 CPLWORLD와 MYRANK0/IROOTC, 모델 통신자 MYWORLD와 NPROCS/MYRANK, CGWORLD 및 ICPL/ISTM을 정수 스칼라로 선언한다(5–8). 원문(연속행은 앞 문장에 이어짐): `MODULE MPI_PARAM` (1); `  IMPLICIT NONE` (3); `  INTEGER :: CPLWORLD, MYRANK0, IROOTC` (5); `  INTEGER :: MYWORLD, NPROCS, MYRANK` (6); `  INTEGER :: CGWORLD` (7); `  INTEGER :: ICPL,ISTM` (8); `END MODULE MPI_PARAM` (10) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 5–8: 선언된 정수 스칼라에는 이 파일 내 초기값이 없다.
