---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/module/makefile
lines: 34
sha256: 684e855c07b1630a8a16d9f52e0b7c413cbba28830a6d52a80ec993ca33f266e
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# makefile — 판독 구간 기록

구간은 1행부터 34행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | FFLAGS=-c $(FOPT)와 모듈 객체 목록. input_work.o·m_val.o·mpc_work.o·m_part.o·mused.o·mavbl.o·m_mumps.o·mpi_param.o·mod_comm.o를 지정하며 all이 이 목록에 의존한다. 빈 줄을 포함한다. 원문: `FFLAGS = -c $(FOPT)` (1); `OBJS = input_work.o m_val.o mpc_work.o m_part.o mused.o mavbl.o m_mumps.o mpi_param.o mod_comm.o` (3); `all : $(OBJS)` (5). |
| 7–12 | mused.o와 mavbl.o의 개별 규칙. 각각 같은 이름의 .f90를 FCOMP와 FFLAGS로 컴파일한다. 명령은 판독만 했다. 원문: `mused.o : mused.f90` (7); `	$(FCOMP) $(FFLAGS) mused.f90` (8); `mavbl.o : mavbl.f90` (10); `	$(FCOMP) $(FFLAGS) mavbl.f90` (11). |
| 13–24 | input_work·m_val·mpc_work·m_mumps의 .mod와 .o를 함께 적은 규칙. 각 .f90가 선행 조건이고 명령 인수 $?는 대상보다 새 선행 파일 목록을 뜻한다. 원문 대상·명령을 모두 보존한다. 원문: `input_work.mod input_work.o : input_work.f90` (13); `	$(FCOMP) $(FFLAGS) $?` (14); `m_val.mod m_val.o : m_val.f90` (16); `	$(FCOMP) $(FFLAGS) $?` (17); `mpc_work.mod mpc_work.o : mpc_work.f90` (19); `	$(FCOMP) $(FFLAGS) $?` (20); `m_mumps.mod m_mumps.o : m_mumps.f90` (22); `	$(FCOMP) $(FFLAGS) $?` (23). |
| 25–34 | mpi_param·m_part·mod_comm의 .mod 및 .o 규칙. 각 .f90에 의존하고 FCOMP·FFLAGS·$?를 사용한다. 33·34행 빈 줄을 포함한다. 원문: `mpi_param.mod mpi_param.o : mpi_param.f90` (25); `	$(FCOMP) $(FFLAGS) $?` (26); `m_part.mod m_part.o : m_part.f90` (28); `	$(FCOMP) $(FFLAGS) $?` (29); `mod_comm.mod mod_comm.o : mod_comm.f90` (31); `	$(FCOMP) $(FFLAGS) $?` (32). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
