---
file: models/FUNWAVE/raw/source_code/FUNWAVE-TVD/GNUMake/Old_Version_Makefiles/Makefile-Topaz-sgi
lines: 106
sha256: c8f00506e409fd4155f91885406da8d2557edf7a54b4323a7b36a852beda5558
reader: codex gpt-6.1-sol
read_date: 2026-10-17
---

# Makefile-Topaz-sgi — 판독 구간 기록

구간은 1행부터 106행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–4 | 시작 주석 뒤에서 셸(shell), 전처리(preprocessing) 옵션과 실행 파일 이름을 설정한다. 원문: `#-----------BEGIN MAKEFILE-------------------------------------------------` (1); `SHELL         = /bin/sh` (2); `DEF_FLAGS     = -P -traditional` (3); `EXEC          = funwave_sgi` (4). |
| 5–22 | 정밀도(precision) 안내 뒤에서 -DDOUBLE_PRECISION·-DPARALLEL·-DSAMPLES·-DCARTESIAN·-DINTEL을 활성화한다. FLAG_5·7·8·9·10·15 설정은 주석이다. 원문: `#        PRECISION          DEFAULT PRECISION: SINGLE` (7); `#                           UNCOMMENT TO SELECT DOUBLE PRECISION` (8); `FLAG_1 = -DDOUBLE_PRECISION` (11); `FLAG_2 = -DPARALLEL` (12); `FLAG_3 = -DSAMPLES` (13); `FLAG_4 = -DCARTESIAN` (14); `#	    FLAG_5 = -DVESSEL` (15); `FLAG_6 = -DINTEL` (16); `#             FLAG_7 = -DMIXING` (17); `#             FLAG_8 = -DCOUPLING` (18); `#             FLAG_9 = -DZALPHA` (19); `#             FLAG_10 = -DMANNING` (20); `#               FLAG_15 = -DTRACKING` (21). |
| 23–37 | MPI 설정 주석 뒤에서 전처리기(preprocessor)는 /usr/bin/cpp, 컴파일러(compiler)는 ifort로 지정한다. DEBFLGS·OPT·CLIB는 빈 값이다. FFLAGS의 -fPIC·-g·-O2는 인라인 주석이다. MPILIB의 -lmpi는 활성이다. 의존성 옵션과 RANLIB도 정의한다. 원문: `#  mpi defs` (24); `CPP      = /usr/bin/cpp` (26); `CPPFLAGS = $(DEF_FLAGS)` (27); `FC       = ifort` (28); `DEBFLGS  =` (29); `OPT      =` (30); `CLIB     =` (31); `FFLAGS = $(DEBFLGS) $(OPT) #-fPIC -g -O2` (34); `MDEPFLAGS = --cpp --fext=f90 --file=-` (35); `RANLIB = ranlib` (36); `MPILIB = -lmpi` (37). |
| 38–55 | CPPARGS는 CPPFLAGS·DEF_FLAGS와 FLAG_1부터 FLAG_24까지 결합한다. LIBS는 라이브러리 변수를 모은다. INCS 설정은 주석이다. 원문: `#  CAT Preprocessing Flags` (39); `CPPARGS = $(CPPFLAGS) $(DEF_FLAGS) $(FLAG_1) $(FLAG_2) \` (41); `$(FLAG_3) $(FLAG_4) $(FLAG_5) $(FLAG_6) \` (42); `$(FLAG_7) $(FLAG_8) $(FLAG_9) $(FLAG_10)  \` (43); `$(FLAG_11) $(FLAG_12) $(FLAG_13) $(FLAG_14) \` (44); `$(FLAG_15) $(FLAG_16) $(FLAG_17) $(FLAG_18) \` (45); `$(FLAG_19) $(FLAG_20) $(FLAG_21) $(FLAG_22) \` (46); `$(FLAG_23) $(FLAG_24)` (47); `#  Libraries` (49); `LIBS  = $(PV3LIB) $(CLIB)  $(PARLIB) $(IOLIBS) $(MPILIB) $(GOTMLIB)` (52); `#            INCS  = $(IOINCS) $(GOTMINCS)` (53). |
| 56–65 | 접미사 규칙(suffix rule)은 .F를 .f90으로 전처리하고 목적 파일(object file)로 컴파일한다. 중간 .f90 삭제 명령은 주석이다. 원문: `#  Preprocessing and Compilation Directives` (57); `.SUFFIXES: .o .f90 .F .F90` (59); `.F.o:` (61); `$(CPP) $(CPPARGS) $*.F > $*.f90` (62); `$(FC)  -c $(FFLAGS) $(INCS) $*.f90` (63); `#	\rm $*.f90` (64). |
| 66–81 | MODS에는 매개변수·전역·입력·선박(vessel)·수심 보정·병렬 필드 입출력·기상(meteorology)·퇴적물(sediment)·추적자(tracer) 모듈 소스를 나열한다. MAIN과 결합해 SRCS를 만들고 .F를 .o로 치환해 OBJS를 만든다. MAIN 마지막 줄은 역슬래시로 다음 빈 줄에 이어진다. 원문: `#  FUNWAVE-TVD Source Code.` (66); `MODS  = mod_param.F	mod_global.F	mod_input.F mod_vessel.F  mod_bathy_correction.F \` (69); `mod_parallel_field_io.F mod_meteo.F mod_sediment.F \` (70); `mod_tracer.F` (71); `MAIN  = main.F bc.F fluxes.F init.F io.F tridiagnal.F       \` (73); `breaker.F derivatives.F dispersion.F etauv_solver.F \` (74); `sponge.F sources.F masks.F parallel.F statistics.F \` (75); `wavemaker.F mixing.F nesting.F misc.F samples.F\` (76); `SRCS = $(MODS)  $(MAIN)` (78); `OBJS = $(SRCS:.F=.o)` (80). |
| 82–89 | 연결(linking) 대상은 OBJS에 의존한다. 연결 명령은 -Bdynamic을 활성 옵션으로 사용한다. 실행 파일을 ../bin/으로 이동한다. 원문: `#  Linking Directives` (83); `$(EXEC):	$(OBJS)` (86); `$(FC) $(FFLAGS) $(LDFLAGS) -o $(EXEC) $(OBJS) $(LIBS) -Bdynamic` (87); `mv $(EXEC) ../bin/` (88). |
| 90–106 | 주석과 빈 줄을 포함한다. tarfile은 .F 소스와 Makefile을 묶는다. clean은 .o·.mod를 삭제한다. clobber는 clean을 선행한 뒤 .f90·.o·현재 디렉터리의 실행 파일을 삭제한다. 원문: `#  Tar Up Code` (92); `tarfile:` (95); `tar cvf funwave_tvd.tar *.F  Makefile` (96); `#  Cleaning targets.` (99); `clean:` (102); `/bin/rm -f *.o *.mod` (103); `clobber:	clean` (105); `/bin/rm -f *.f90 *.o $(EXEC)` (106). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 7–11: 정밀도 안내 주석은 `DEFAULT PRECISION: SINGLE`이라고 적는다. 활성 설정에는 `FLAG_1 = -DDOUBLE_PRECISION`이 있다.
- 27·41: CPPFLAGS는 DEF_FLAGS를 참조한다. CPPARGS는 CPPFLAGS와 DEF_FLAGS를 각각 나열한다.
- 88·105–106: 연결 뒤 실행 파일을 ../bin/으로 이동한다. clobber는 현재 디렉터리의 `$(EXEC)`를 삭제 대상으로 지정한다.
