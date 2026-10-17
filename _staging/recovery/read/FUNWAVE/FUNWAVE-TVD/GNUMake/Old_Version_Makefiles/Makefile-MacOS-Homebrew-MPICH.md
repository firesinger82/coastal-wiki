---
file: models/FUNWAVE/raw/source_code/FUNWAVE-TVD/GNUMake/Old_Version_Makefiles/Makefile-MacOS-Homebrew-MPICH
lines: 108
sha256: 8c09172d341a497894babe22705eb915ac750c1d141396465d42adf0a7d907b9
reader: codex gpt-6.1-sol
read_date: 2026-10-17
---

# Makefile-MacOS-Homebrew-MPICH — 판독 구간 기록

구간은 1행부터 108행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–4 | 시작 주석 뒤에서 셸(shell), 전처리(preprocessing) 옵션과 실행 파일 이름을 설정한다. 원문: `#-----------BEGIN MAKEFILE-------------------------------------------------` (1); `SHELL         = /bin/sh` (2); `DEF_FLAGS     = -P -traditional` (3); `EXEC          = funwave_gnu` (4). |
| 5–26 | 정밀도(precision) 안내와 빈 줄 뒤에서 병렬·직교좌표·선박 전처리 플래그를 활성화한다. FLAG_1·4·5·6·7·9부터 FLAG_15까지의 설정은 주석이다. 원문: `#        PRECISION          DEFAULT PRECISION: SINGLE` (7); `#                           UNCOMMENT TO SELECT DOUBLE PRECISION` (8); `#            FLAG_1 = -DDOUBLE_PRECISION` (12); `FLAG_2 = -DPARALLEL` (13); `FLAG_3 = -DCARTESIAN` (14); `#              FLAG_4 = -DINTEL` (15); `#               FLAG_5 = -DCOUPLING` (16); `#             FLAG_6 = -DZALPHA` (17); `#              FLAG_7 = -DMANNING` (18); `FLAG_8 = -DVESSEL` (19); `#               FLAG_9 = -DMETEO` (20); `#              FLAG_10 = -DWIND` (21); `#               FLAG_11 = -DSEDIMENT` (22); `#               FLAG_12 = -DCHECK_MASS_CONSERVATION` (23); `#               FLAG_13 = -DDEBUG` (24); `#               FLAG_14 = -DTMP` (25); `#               FLAG_15 = -DTRACKING` (26). |
| 27–40 | MPI 설정 주석 뒤에서 전처리기(preprocessor)와 /usr/local/bin/mpif90 컴파일러(compiler)를 지정한다. DEBFLGS·OPT·CLIB는 빈 값이다. FFLAGS·의존성 옵션·RANLIB를 설정한다. 원문: `#  mpi defs` (28); `CPP      = /usr/bin/cpp` (30); `CPPFLAGS = $(DEF_FLAGS)` (31); `FC       = /usr/local/bin/mpif90` (32); `DEBFLGS  =` (33); `OPT      =` (34); `CLIB     =` (35); `FFLAGS = $(DEBFLGS) $(OPT)` (38); `MDEPFLAGS = --cpp --fext=f90 --file=-` (39); `RANLIB = ranlib` (40). |
| 41–58 | CPPARGS는 CPPFLAGS와 FLAG_1부터 FLAG_24까지 결합한다. LIBS와 INCS 설정 줄은 모두 주석이다. 원문: `#  CAT Preprocessing Flags` (42); `CPPARGS = $(CPPFLAGS)  $(FLAG_1) $(FLAG_2) \` (44); `$(FLAG_3) $(FLAG_4) $(FLAG_5) $(FLAG_6) \` (45); `$(FLAG_7) $(FLAG_8) $(FLAG_9) $(FLAG_10)  \` (46); `$(FLAG_11) $(FLAG_12) $(FLAG_13) $(FLAG_14) \` (47); `$(FLAG_15) $(FLAG_16) $(FLAG_17) $(FLAG_18) \` (48); `$(FLAG_19) $(FLAG_20) $(FLAG_21) $(FLAG_22) \` (49); `$(FLAG_23) $(FLAG_24)` (50); `#  Libraries` (52); `#            LIBS  = $(PV3LIB) $(CLIB)  $(PARLIB) $(IOLIBS) $(MPILIB) $(GOTMLIB)` (55); `#            INCS  = $(IOINCS) $(GOTMINCS)` (56). |
| 59–68 | 접미사 규칙(suffix rule)은 .F를 .f90으로 전처리하고 목적 파일(object file)로 컴파일한다. /bin/rm 중간 파일 삭제 명령은 주석이다. 원문: `#  Preprocessing and Compilation Directives` (60); `.SUFFIXES: .o .f90 .F .F90` (62); `.F.o:` (64); `$(CPP) $(CPPARGS) $*.F > $*.f90` (65); `$(FC)  -c $(FFLAGS) $(INCS) $*.f90` (66); `#	/bin/rm $*.f90` (67). |
| 69–83 | 모듈 목록에는 mod_vessel.F·mod_bathy_correction.F·mod_meteo.F·mod_parallel_field_io.F·mod_sediment.F·mod_tracer.F가 포함된다. MAIN을 별도로 나열하고 SRCS를 결합한 뒤 OBJS 접미사를 치환한다. 원문: `#  FUNWAVE-TVD Source Code.` (69); `MODS  = mod_param.F mod_global.F mod_input.F mod_vessel.F mod_bathy_correction.F \` (72); `mod_meteo.F mod_parallel_field_io.F mod_sediment.F  mod_tracer.F` (73); `MAIN  = main.F bc.F fluxes.F init.F io.F tridiagnal.F       \` (75); `breaker.F derivatives.F dispersion.F etauv_solver.F \` (76); `sponge.F sources.F masks.F parallel.F statistics.F \` (77); `wavemaker.F mixing.F nesting.F misc.F samples.F` (78); `SRCS = $(MODS)  $(MAIN)` (80); `OBJS = $(SRCS:.F=.o)` (82). |
| 84–91 | 연결(linking) 대상은 OBJS에 의존한다. 실행 파일을 연결한 뒤 ../bin/으로 이동한다. 원문: `#  Linking Directives` (85); `$(EXEC):	$(OBJS)` (88); `$(FC) $(FFLAGS) $(LDFLAGS) -o $(EXEC) $(OBJS) $(LIBS)` (89); `mv $(EXEC) ../bin/` (90). |
| 92–108 | 주석과 빈 줄을 포함한다. tarfile은 소스와 Makefile을 묶는다. clean은 .o·.mod를 삭제한다. clobber는 clean을 선행한 뒤 .f90·.o·현재 디렉터리의 실행 파일을 삭제한다. 원문: `#  Tar Up Code` (94); `tarfile:` (97); `tar cvf funwave_tvd.tar *.F  Makefile` (98); `#  Cleaning targets.` (101); `clean:` (104); `/bin/rm -f *.o *.mod` (105); `clobber:	clean` (107); `/bin/rm -f *.f90 *.o $(EXEC)` (108). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 19–22·72–73: -DVESSEL은 활성이다. -DMETEO·-DWIND·-DSEDIMENT는 주석이다. 모듈 목록에는 mod_meteo.F·mod_sediment.F·mod_tracer.F가 들어 있다.
- 39–40: MDEPFLAGS와 RANLIB는 정의되어 있다. 이 파일의 명령 줄은 두 변수를 참조하지 않는다.
- 90·107–108: 연결 뒤 실행 파일을 ../bin/으로 이동한다. clobber는 현재 디렉터리의 `$(EXEC)`를 삭제 대상으로 지정한다.
