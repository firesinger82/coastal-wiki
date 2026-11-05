---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/main/mumps_para.f
lines: 24
sha256: 259e90514331c7f126a55ce702600cadd23e6b751eab1f9781ecbd8f6df305ee
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# mumps_para.f — 판독 구간 기록

구간은 1행부터 24행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | MUMPS_PARA는 M_MUMPS·MPI_PARAM을 사용하고 MUMPS_PAR%COMM에 MYWORLD를 지정한다(3–6). 무한 DO 루프에서 M_MPI_BCAST_I(MUMPS_PAR%JOB,1)로 작업을 받는다(8–10). JOB=0이면 반환하며 그 외에는 DMUMPS를 호출한다(12–14). JOB=-1이면 ICNTL(1)·ICNTL(2)을 0, ICNTL(4)를 1로 설정한 뒤 다음 작업을 받는다(16–22). 원문(고정형식 연속행은 아래 인접 행을 하나의 문장으로 읽음): `      SUBROUTINE MUMPS_PARA()` (1) <br> `      USE M_MUMPS` (3) <br> `      USE MPI_PARAM` (4) <br> `      MUMPS_PAR%COMM = MYWORLD` (6) <br> `      DO` (8) <br> `        CALL M_MPI_BCAST_I(MUMPS_PAR%JOB,1)` (10) <br> `        IF( MUMPS_PAR%JOB == 0 ) RETURN` (12) <br> `        CALL DMUMPS(MUMPS_PAR)` (14) <br> `        IF( MUMPS_PAR%JOB == -1 ) THEN` (16) <br> `          MUMPS_PAR%ICNTL(1) = 0` (17) <br> `          MUMPS_PAR%ICNTL(2) = 0` (18) <br> `          MUMPS_PAR%ICNTL(4) = 1` (19) <br> `        ENDIF` (20) <br> `      ENDDO` (22) <br> `      END` (24) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 14–19: JOB=-1에 대한 ICNTL 설정은 DMUMPS 호출 뒤에 실행한다.
