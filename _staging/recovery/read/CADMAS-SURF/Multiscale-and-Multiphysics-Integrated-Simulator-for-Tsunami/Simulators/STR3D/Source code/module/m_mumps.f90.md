---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/module/m_mumps.f90
lines: 8
sha256: 7f7fb1f2b334d55d19da737bda92d7ff9b4032314f9da0a6edd28b57ed663e0a
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# m_mumps.f90 — 판독 구간 기록

구간은 1행부터 8행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | M_MUMPS 모듈에서 IMPLICIT NONE을 선언한다(1–3). dmumps_struc.h를 INCLUDE하고 그 파생형(derived type) DMUMPS_STRUC의 MUMPS_PAR를 모듈 변수로 선언한다(5–6). 모듈을 닫는다(8). INCLUDE·형식 선언 원문을 아래에 보존한다. 원문(고정형식 연속행은 아래 인접 행을 하나의 문장으로 읽음): `MODULE M_MUMPS` (1) <br> `  IMPLICIT NONE` (3) <br> `  INCLUDE 'dmumps_struc.h'` (5) <br> `  TYPE(DMUMPS_STRUC) :: MUMPS_PAR` (6) <br> `END MODULE M_MUMPS` (8) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
