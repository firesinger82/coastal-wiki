---
file: models/FUNWAVE/raw/source_code/FUNWAVE-TVD/GNUMake/Old_Version_Makefiles/Makefile-Onyx-Sediment-intel
lines: 106
sha256: ab2c4023640b1143162792c9565a797cc819864e786c3018838736b4274bb3dc
reader: codex gpt-6.1-sol
read_date: 2026-10-17
---

# Makefile-Onyx-Sediment-intel — 판독 구간 기록

구간은 1행부터 106행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–4 | 시작 주석 뒤에서 셸(shell), 전처리(preprocessing) 옵션과 실행 파일 이름을 설정한다. 원문: `#-----------BEGIN MAKEFILE-------------------------------------------------` (1); `SHELL         = /bin/sh` (2); `DEF_FLAGS     = -P -traditional` (3); `EXEC          = funwave_sediment` (4). |
| 5–22 | 정밀도(precision) 안내 뒤에 -DPARALLEL·-DSAMPLES·-DCARTESIAN·-DINTEL·-DSEDIMENT·-DCHECK_MASS_CONSERVATION을 활성화한다. FLAG_1·5·7·8·9·10 설정은 주석이다. 원문: `#        PRECISION          DEFAULT PRECISION: SINGLE` (7); `#                           UNCOMMENT TO SELECT DOUBLE PRECISION` (8); `#            FLAG_1 = -DDOUBLE_PRECISION` (11); `FLAG_2 = -DPARALLEL` (12); `FLAG_3 = -DSAMPLES` (13); `FLAG_4 = -DCARTESIAN` (14); `#	    FLAG_5 = -DVESSEL` (15); `FLAG_6 = -DINTEL` (16); `#             FLAG_7 = -DMIXING` (17); `#             FLAG_8 = -DCOUPLING` (18); `#             FLAG_9 = -DZALPHA` (19); `#             FLAG_10 = -DMANNING` (20); `FLAG_11 = -DSEDIMENT` (21); `FLAG_12 = -DCHECK_MASS_CONSERVATION` (22). |
| 23–37 | MPI 설정 주석 뒤에서 전처리기(preprocessor)는 /usr/bin/cpp, 컴파일러(compiler)는 ftn으로 지정한다. DEBFLGS·OPT·CLIB·MPILIB는 빈 값이다. FFLAGS 뒤의 -fPIC·-g·-O2는 인라인 주석이다. 의존성 옵션과 RANLIB도 정의한다. 원문: `#  mpi defs` (24); `CPP      = /usr/bin/cpp` (26); `CPPFLAGS = $(DEF_FLAGS)` (27); `FC       = ftn` (28); `DEBFLGS  =` (29); `OPT      =` (30); `CLIB     =` (31); `FFLAGS = $(DEBFLGS) $(OPT) #-fPIC -g -O2` (34); `MDEPFLAGS = --cpp --fext=f90 --file=-` (35); `RANLIB = ranlib` (36); `MPILIB =` (37). |
| 38–55 | CPPARGS는 CPPFLAGS·DEF_FLAGS와 FLAG_1부터 FLAG_24까지 결합한다. LIBS는 라이브러리 변수를 모은다. INCS 설정은 주석이다. 원문: `#  CAT Preprocessing Flags` (39); `CPPARGS = $(CPPFLAGS) $(DEF_FLAGS) $(FLAG_1) $(FLAG_2) \` (41); `$(FLAG_3) $(FLAG_4) $(FLAG_5) $(FLAG_6) \` (42); `$(FLAG_7) $(FLAG_8) $(FLAG_9) $(FLAG_10)  \` (43); `$(FLAG_11) $(FLAG_12) $(FLAG_13) $(FLAG_14) \` (44); `$(FLAG_15) $(FLAG_16) $(FLAG_17) $(FLAG_18) \` (45); `$(FLAG_19) $(FLAG_20) $(FLAG_21) $(FLAG_22) \` (46); `$(FLAG_23) $(FLAG_24)` (47); `#  Libraries` (49); `LIBS  = $(PV3LIB) $(CLIB)  $(PARLIB) $(IOLIBS) $(MPILIB) $(GOTMLIB)` (52); `#            INCS  = $(IOINCS) $(GOTMINCS)` (53). |
| 56–65 | 접미사 규칙(suffix rule)은 .F를 .f90으로 전처리하고 목적 파일(object file)로 컴파일한다. 중간 .f90 삭제 명령은 주석이다. 원문: `#  Preprocessing and Compilation Directives` (57); `.SUFFIXES: .o .f90 .F .F90` (59); `.F.o:` (61); `$(CPP) $(CPPARGS) $*.F > $*.f90` (62); `$(FC)  -c $(FFLAGS) $(INCS) $*.f90` (63); `#	\rm $*.f90` (64). |
| 66–80 | 모듈 목록에는 선박(vessel)·수심 보정·병렬 필드 입출력·기상(meteorology)·퇴적물(sediment) 소스가 들어 있다. MAIN을 정의하고 SRCS와 OBJS를 구성한다. MAIN 마지막 줄은 역슬래시로 다음 빈 줄에 이어진다. 원문: `#  FUNWAVE-TVD Source Code.` (66); `MODS  = mod_param.F	mod_global.F	mod_input.F mod_vessel.F  mod_bathy_correction.F \` (69); `mod_parallel_field_io.F mod_meteo.F mod_sediment.F` (70); `MAIN  = main.F bc.F fluxes.F init.F io.F tridiagnal.F       \` (72); `breaker.F derivatives.F dispersion.F etauv_solver.F \` (73); `sponge.F sources.F masks.F parallel.F statistics.F \` (74); `wavemaker.F mixing.F nesting.F misc.F samples.F\` (75); `SRCS = $(MODS)  $(MAIN)` (77); `OBJS = $(SRCS:.F=.o)` (79). |
| 81–89 | 연결(linking) 대상은 OBJS에 의존한다. 실행 파일을 연결하고 mkdir -p로 ../bin을 만든 뒤 실행 파일을 그 디렉터리로 이동한다. 원문: `#  Linking Directives` (82); `$(EXEC):	$(OBJS)` (85); `$(FC) $(FFLAGS) $(LDFLAGS) -o $(EXEC) $(OBJS) $(LIBS)` (86); `mkdir -p ../bin` (87); `mv $(EXEC) ../bin/` (88). |
| 90–106 | 주석과 빈 줄을 포함한다. tarfile은 .F 소스와 Makefile을 묶는다. clean은 .o·.mod·.f90을 삭제한다. clobber는 clean을 선행한 뒤 .f90·.o·현재 디렉터리의 실행 파일을 삭제한다. 원문: `#  Tar Up Code` (92); `tarfile:` (95); `tar cvf funwave_tvd.tar *.F  Makefile` (96); `#  Cleaning targets.` (99); `clean:` (102); `/bin/rm -f *.o *.mod *.f90` (103); `clobber:	clean` (105); `/bin/rm -f *.f90 *.o $(EXEC)` (106). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 27·41: CPPFLAGS는 DEF_FLAGS를 참조한다. CPPARGS는 CPPFLAGS와 DEF_FLAGS를 각각 나열한다.
- 35–36: MDEPFLAGS와 RANLIB는 정의되어 있다. 이 파일의 명령 줄은 두 변수를 참조하지 않는다.
- 88·105–106: 연결 뒤 실행 파일을 ../bin/으로 이동한다. clobber는 현재 디렉터리의 `$(EXEC)`를 삭제 대상으로 지정한다.
