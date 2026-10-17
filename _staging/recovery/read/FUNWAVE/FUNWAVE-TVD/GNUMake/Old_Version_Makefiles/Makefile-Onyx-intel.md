---
file: models/FUNWAVE/raw/source_code/FUNWAVE-TVD/GNUMake/Old_Version_Makefiles/Makefile-Onyx-intel
lines: 112
sha256: 5bdb6803dbe1f841ebadc20d090282b3c05f24bab91b4c46fdcfe7bf684723d5
reader: codex gpt-6.1-sol
read_date: 2026-10-17
---

# Makefile-Onyx-intel — 판독 구간 기록

구간은 1행부터 112행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–4 | 시작 주석 뒤에서 셸(shell), 전처리(preprocessing) 옵션과 실행 파일 이름을 설정한다. 원문: `#-----------BEGIN MAKEFILE-------------------------------------------------` (1); `SHELL         = /bin/sh` (2); `DEF_FLAGS     = -P -traditional` (3); `EXEC          = funwave_central` (4). |
| 5–25 | 정밀도(precision) 안내 뒤에 -DPARALLEL·-DSAMPLES·-DCARTESIAN·-DINTEL·-DCHECK_MASS_CONSERVATION을 활성화한다. FLAG_1·5·7·8·9·10·11·13·14 설정은 주석이다. 원문: `#        PRECISION          DEFAULT PRECISION: SINGLE` (7); `#                           UNCOMMENT TO SELECT DOUBLE PRECISION` (8); `#            FLAG_1 = -DDOUBLE_PRECISION` (11); `FLAG_2 = -DPARALLEL` (12); `FLAG_3 = -DSAMPLES` (13); `FLAG_4 = -DCARTESIAN` (14); `#	    FLAG_5 = -DVESSEL` (15); `FLAG_6 = -DINTEL` (16); `#             FLAG_7 = -DMIXING` (17); `#             FLAG_8 = -DCOUPLING` (18); `#             FLAG_9 = -DZALPHA` (19); `#             FLAG_10 = -DMANNING` (20); `#	      FLAG_11 = -DSEDIMENT` (21); `FLAG_12 = -DCHECK_MASS_CONSERVATION` (22); `#	      FLAG_13 = -DWIND` (23); `#	      FLAG_14 = -DMETEO` (24). |
| 26–40 | MPI 설정 주석 뒤에서 전처리기(preprocessor)는 /usr/bin/cpp, 컴파일러(compiler)는 ftn으로 지정한다. DEBFLGS·OPT·CLIB·MPILIB는 빈 값이다. FFLAGS 뒤의 -fPIC·-g·-O2는 인라인 주석이다. 의존성 옵션과 RANLIB도 정의한다. 원문: `#  mpi defs` (27); `CPP      = /usr/bin/cpp` (29); `CPPFLAGS = $(DEF_FLAGS)` (30); `FC       = ftn` (31); `DEBFLGS  =` (32); `OPT      =` (33); `CLIB     =` (34); `FFLAGS = $(DEBFLGS) $(OPT) #-fPIC -g -O2` (37); `MDEPFLAGS = --cpp --fext=f90 --file=-` (38); `RANLIB = ranlib` (39); `MPILIB =` (40). |
| 41–58 | CPPARGS는 CPPFLAGS·DEF_FLAGS와 FLAG_1부터 FLAG_24까지 결합한다. LIBS는 라이브러리 변수를 모은다. INCS 설정은 주석이다. 원문: `#  CAT Preprocessing Flags` (42); `CPPARGS = $(CPPFLAGS) $(DEF_FLAGS) $(FLAG_1) $(FLAG_2) \` (44); `$(FLAG_3) $(FLAG_4) $(FLAG_5) $(FLAG_6) \` (45); `$(FLAG_7) $(FLAG_8) $(FLAG_9) $(FLAG_10)  \` (46); `$(FLAG_11) $(FLAG_12) $(FLAG_13) $(FLAG_14) \` (47); `$(FLAG_15) $(FLAG_16) $(FLAG_17) $(FLAG_18) \` (48); `$(FLAG_19) $(FLAG_20) $(FLAG_21) $(FLAG_22) \` (49); `$(FLAG_23) $(FLAG_24)` (50); `#  Libraries` (52); `LIBS  = $(PV3LIB) $(CLIB)  $(PARLIB) $(IOLIBS) $(MPILIB) $(GOTMLIB)` (55); `#            INCS  = $(IOINCS) $(GOTMINCS)` (56). |
| 59–68 | 접미사 규칙(suffix rule)은 .F를 .f90으로 전처리하고 목적 파일(object file)로 컴파일한다. 중간 .f90 삭제 명령은 주석이다. 원문: `#  Preprocessing and Compilation Directives` (60); `.SUFFIXES: .o .f90 .F .F90` (62); `.F.o:` (64); `$(CPP) $(CPPARGS) $*.F > $*.f90` (65); `$(FC)  -c $(FFLAGS) $(INCS) $*.f90` (66); `#	\rm $*.f90` (67). |
| 69–83 | 모듈 목록에는 선박(vessel)·수심 보정·병렬 필드 입출력·기상(meteorology)·퇴적물(sediment)·추적자(tracer) 소스가 들어 있다. MAIN에는 본체 소스를 나열한다. SRCS는 두 목록을 결합한다. OBJS는 .F를 .o로 치환한다. 원문: `#  FUNWAVE-TVD Source Code.` (69); `MODS  = mod_param.F	mod_global.F	mod_input.F mod_vessel.F  mod_bathy_correction.F \` (72); `mod_parallel_field_io.F mod_meteo.F mod_sediment.F mod_tracer.F` (73); `MAIN  = main.F bc.F fluxes.F init.F io.F tridiagnal.F       \` (75); `breaker.F derivatives.F dispersion.F etauv_solver.F \` (76); `sponge.F sources.F masks.F parallel.F statistics.F  \` (77); `wavemaker.F mixing.F nesting.F misc.F samples.F` (78); `SRCS = $(MODS)  $(MAIN)` (80); `OBJS = $(SRCS:.F=.o)` (82). |
| 84–95 | 연결(linking) 대상은 OBJS에 의존한다. 실행 파일을 연결하고 mkdir -p로 ../bin을 만든 뒤 실행 파일을 그 디렉터리로 이동한다. 원문: `#  Linking Directives` (88); `$(EXEC):	$(OBJS)` (91); `$(FC) $(FFLAGS) $(LDFLAGS) -o $(EXEC) $(OBJS) $(LIBS)` (92); `mkdir -p ../bin` (93); `mv $(EXEC) ../bin/` (94). |
| 96–112 | 주석과 빈 줄을 포함한다. tarfile은 .F 소스와 Makefile을 묶는다. clean은 .o·.mod·.f90을 삭제한다. clobber는 clean을 선행한 뒤 .f90·.o·현재 디렉터리의 실행 파일을 삭제한다. 원문: `#  Tar Up Code` (98); `tarfile:` (101); `tar cvf funwave_tvd.tar *.F  Makefile` (102); `#  Cleaning targets.` (105); `clean:` (108); `/bin/rm -f *.o *.mod *.f90` (109); `clobber:	clean` (111); `/bin/rm -f *.f90 *.o $(EXEC)` (112). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 30·44: CPPFLAGS는 DEF_FLAGS를 참조한다. CPPARGS는 CPPFLAGS와 DEF_FLAGS를 각각 나열한다.
- 15·21·24·72–73: -DVESSEL·-DSEDIMENT·-DMETEO 설정은 주석이다. MODS에는 해당 이름의 모듈 소스와 mod_tracer.F가 포함된다.
- 94·111–112: 연결 뒤 실행 파일을 ../bin/으로 이동한다. clobber는 현재 디렉터리의 `$(EXEC)`를 삭제 대상으로 지정한다.
