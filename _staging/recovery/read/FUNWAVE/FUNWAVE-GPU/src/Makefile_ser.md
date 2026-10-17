---
file: models/FUNWAVE/raw/source_code/FUNWAVE-GPU/src/Makefile_ser
lines: 112
sha256: 37fb61cf10bc2f8e2efdc3869d2b0c43504108b3bf738c6f8517d4ef8bf7a17c
reader: codex gpt-6.1-sol
read_date: 2026-10-17
---

# Makefile_ser — 판독 구간 기록

구간은 1행부터 112행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–4 | 시작 주석 뒤에서 셸(shell), 전처리(preprocessing) 옵션과 실행 파일 이름을 설정한다. 원문: `#-----------BEGIN MAKEFILE-------------------------------------------------` (1); `SHELL         = /bin/sh` (2); `DEF_FLAGS     = -P -traditional` (3); `EXEC          = funwave_ser` (4). |
| 5–30 | 정밀도(precision) 안내 뒤에서 -DCARTESIAN·-DPGI를 활성화한다. FLAG_1·2·4·6부터 FLAG_18까지·FLAG_20·21의 설정은 주석이다. -DDOUBLE_PRECISION·-DPARALLEL·-DZALPHA·-DUSE_CUDA·-DTIMING·-DGPU_CHECK도 주석에 포함된다. 원문: `#        PRECISION          DEFAULT PRECISION: SINGLE` (7); `#                           UNCOMMENT TO SELECT DOUBLE PRECISION` (8); `#            FLAG_1 = -DDOUBLE_PRECISION` (11); `#            FLAG_2 = -DPARALLEL` (12); `FLAG_3 = -DCARTESIAN` (13); `#            FLAG_4 = -DSAMPLES` (14); `#              FLAG_6 = -DINTEL` (15); `#             FLAG_7 = -DMIXING` (16); `#              FLAG_8 = -DCOUPLING` (17); `#             FLAG_9 = -DZALPHA` (18); `#             FLAG_10 = -DMANNING` (19); `#             FLAG_11 = -DSPHERICAL_IJ_STATION` (20); `#               FLAG_12 = -DVESSEL` (21); `#              FLAG_13 = -DVIS_KENNEDY` (22); `#              FLAG_14 = -DVESSEL_PANEL_SOURCE` (23); `#              FLAG_15 = -DREALISTIC_VESSEL_BODY` (24); `#              FLAG_16 = -DMETEO` (25); `#              FLAG_17 = -DWIND` (26); `#              FLAG_18 = -DUSE_CUDA` (27); `FLAG_19 = -DPGI` (28); `#              FLAG_20 = -DTIMING` (29); `#              FLAG_21 = -DGPU_CHECK` (30). |
| 31–44 | MPI 설정 주석 아래 전처리기(preprocessor)와 mpif90 컴파일러(compiler)를 지정한다. DEBFLGS·OPT·CLIB는 빈 값이다. FFLAGS·의존성 옵션·RANLIB를 정의한다. 원문: `#  mpi defs` (32); `CPP      = /usr/bin/cpp` (34); `CPPFLAGS = $(DEF_FLAGS)` (35); `FC       = mpif90` (36); `DEBFLGS  =` (37); `OPT      =` (38); `CLIB     =` (39); `FFLAGS = $(DEBFLGS) $(OPT)` (42); `MDEPFLAGS = --cpp --fext=f90 --file=-` (43); `RANLIB = ranlib` (44). |
| 45–62 | CPPARGS는 CPPFLAGS·DEF_FLAGS와 FLAG_1부터 FLAG_24까지 결합한다. LIBS·INCS 설정은 주석이다. 원문: `#  CAT Preprocessing Flags` (46); `CPPARGS = $(CPPFLAGS) $(DEF_FLAGS) $(FLAG_1) $(FLAG_2) \` (48); `$(FLAG_3) $(FLAG_4) $(FLAG_5) $(FLAG_6) \` (49); `$(FLAG_7) $(FLAG_8) $(FLAG_9) $(FLAG_10)  \` (50); `$(FLAG_11) $(FLAG_12) $(FLAG_13) $(FLAG_14) \` (51); `$(FLAG_15) $(FLAG_16) $(FLAG_17) $(FLAG_18) \` (52); `$(FLAG_19) $(FLAG_20) $(FLAG_21) $(FLAG_22) \` (53); `$(FLAG_23) $(FLAG_24)` (54); `#  Libraries` (56); `#            LIBS  = $(PV3LIB) $(CLIB)  $(PARLIB) $(IOLIBS) $(MPILIB) $(GOTMLIB)` (59); `#            INCS  = $(IOINCS) $(GOTMINCS)` (60). |
| 63–72 | 접미사 규칙(suffix rule)은 .F를 .f90으로 전처리하고 목적 파일(object file)로 컴파일한 뒤 중간 .f90을 삭제한다. 원문: `#  Preprocessing and Compilation Directives` (64); `.SUFFIXES: .o .f90 .F .F90` (66); `.F.o:` (68); `$(CPP) $(CPPARGS) $*.F > $*.f90` (69); `$(FC)  -c $(FFLAGS) $(INCS) $*.f90` (70); `/bin/rm $*.f90` (71). |
| 73–87 | MODS에는 매개변수·전역·입력·선박(vessel)·수심 보정·기상(meteorology)·병렬 필드 입출력·퇴적물(sediment) 소스를 나열한다. MAIN에는 본체 소스를 나열한다. SRCS는 두 목록을 결합한다. OBJS는 .F를 .o로 치환한다. MAIN 마지막 줄은 역슬래시로 다음 빈 줄에 이어진다. 원문: `#  FUNWAVE-TVD Source Code.` (73); `MODS  = mod_param.F mod_global.F mod_input.F mod_vessel.F mod_bathy_correction.F \` (76); `mod_meteo.F mod_parallel_field_io.F mod_sediment.F` (77); `MAIN  = main.F bc.F fluxes.F init.F io.F tridiagnal.F       \` (79); `breaker.F derivatives.F dispersion.F etauv_solver.F \` (80); `sponge.F sources.F masks.F parallel.F statistics.F \` (81); `wavemaker.F mixing.F nesting.F misc.F samples.F\` (82); `SRCS = $(MODS)  $(MAIN)` (84); `OBJS = $(SRCS:.F=.o)` (86). |
| 88–95 | 연결(linking) 대상은 OBJS에 의존한다. 실행 파일 연결 명령은 활성이다. ../bin/ 이동 명령은 주석이다. 원문: `#  Linking Directives` (89); `$(EXEC):	$(OBJS)` (92); `$(FC) $(FFLAGS) $(LDFLAGS) -o $(EXEC) $(OBJS) $(LIBS)` (93); `#		mv $(EXEC) ../bin/` (94). |
| 96–112 | 주석과 빈 줄을 포함한다. tarfile은 .F 소스와 Makefile을 묶는다. clean은 .o·.mod를 삭제한다. clobber는 clean을 선행한 뒤 .f90·.o·실행 파일을 삭제한다. 원문: `#  Tar Up Code` (98); `tarfile:` (101); `tar cvf funwave_tvd.tar *.F  Makefile` (102); `#  Cleaning targets.` (105); `clean:` (108); `/bin/rm -f *.o *.mod` (109); `clobber:	clean` (111); `/bin/rm -f *.f90 *.o $(EXEC)` (112). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 12·36: -DPARALLEL 설정은 주석이다. 컴파일러 이름은 mpif90이다.
- 35·48: CPPFLAGS는 DEF_FLAGS를 참조한다. CPPARGS는 CPPFLAGS와 DEF_FLAGS를 각각 나열한다.
- 101–102: 이 파일 이름은 Makefile_ser이다. tarfile 명령이 지정하는 빌드 설정 파일 이름은 Makefile이다.
