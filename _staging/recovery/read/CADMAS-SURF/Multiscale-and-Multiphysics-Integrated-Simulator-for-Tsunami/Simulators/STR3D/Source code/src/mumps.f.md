---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/mumps.f
lines: 16
sha256: d14cc61c7c1c184f0d0e3588fbf3bb0c0b67dce80f8b2d30a62b2a067de41142
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# mumps.f — 판독 구간 기록

구간은 1행부터 16행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | MUMPS 래퍼(wrapper)의 M_MUMPS 사용과 선언이다. MUMPS_PAR%JOB를 5로 설정하고 M_MPI_BCAST_I로 방송한다. DMUMPS를 호출하고 RHS 전체를 X로 복사한다. 원문: `      SUBROUTINE MUMPS(X,NEQSOL,ITO)` (1)； `      USE M_MUMPS` (3)； `      IMPLICIT REAL*8(A-H,O-Z)` (5)； `      DIMENSION X(NEQSOL)` (6)； `      MUMPS_PAR%JOB = 5` (8)； `      CALL M_MPI_BCAST_I(MUMPS_PAR%JOB,1)` (10)； `      CALL DMUMPS(MUMPS_PAR)` (12)； `      X(:) = MUMPS_PAR%RHS(:)` (14)； `      END` (16)。 |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 1–16: ITO는 인수이지만 이 파일의 실행문에는 쓰이지 않는다.
- 12–14: DMUMPS 호출 뒤 상태 검사 없이 RHS를 X로 복사한다.
