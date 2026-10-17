---
file: models/FUNWAVE/raw/source_code/FUNWAVE-GPU/src/Makefile
lines: 111
sha256: 0059e5ae933deda73060988669822b825fd3e6ccba4cc3d874aca1fab556a04c
reader: codex gpt-6.1-sol
read_date: 2026-10-17
---

# Makefile — 판독 구간 기록

구간은 1행부터 111행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–4 | 시작 주석 뒤에서 셸(shell), 전처리(preprocessing) 옵션과 실행 파일 이름을 설정한다. 원문: `#-----------BEGIN MAKEFILE-------------------------------------------------` (1); `SHELL         = /bin/sh` (2); `DEF_FLAGS     = -P -traditional` (3); `EXEC          = funwave_mpi` (4). |
| 5–29 | 정밀도(precision) 안내 뒤에서 -DDOUBLE_PRECISION·-DPARALLEL·-DCARTESIAN·-DPGI·-DTIMING을 활성화한다. FLAG_4·6부터 FLAG_18까지의 설정은 주석이다. 주석에는 선박(vessel)·기상(meteorology)·CUDA 관련 선택 항목이 들어 있다. 원문: `#        PRECISION          DEFAULT PRECISION: SINGLE` (7); `#                           UNCOMMENT TO SELECT DOUBLE PRECISION` (8); `FLAG_1 = -DDOUBLE_PRECISION` (11); `FLAG_2 = -DPARALLEL` (12); `FLAG_3 = -DCARTESIAN` (13); `#            FLAG_4 = -DSAMPLES` (14); `#              FLAG_6 = -DINTEL` (15); `#             FLAG_7 = -DMIXING` (16); `#              FLAG_8 = -DCOUPLING` (17); `#             FLAG_9 = -DZALPHA` (18); `#             FLAG_10 = -DMANNING` (19); `#             FLAG_11 = -DSPHERICAL_IJ_STATION` (20); `#               FLAG_12 = -DVESSEL` (21); `#              FLAG_13 = -DVIS_KENNEDY` (22); `#              FLAG_14 = -DVESSEL_PANEL_SOURCE` (23); `#              FLAG_15 = -DREALISTIC_VESSEL_BODY` (24); `#              FLAG_16 = -DMETEO` (25); `#              FLAG_17 = -DWIND` (26); `#              FLAG_18 = -DUSE_CUDA` (27); `FLAG_19 = -DPGI` (28); `FLAG_20 = -DTIMING` (29). |
| 30–43 | MPI 설정 주석 아래 전처리기(preprocessor)와 mpif90 컴파일러(compiler)를 지정한다. DEBFLGS·CLIB는 빈 값이다. OPT는 -Mcuda·-Mcudalib=cusparse를 활성화한다. FFLAGS·의존성 옵션·RANLIB를 정의한다. 원문: `#  mpi defs` (31); `CPP      = /usr/bin/cpp` (33); `CPPFLAGS = $(DEF_FLAGS)` (34); `FC       = mpif90` (35); `DEBFLGS  =` (36); `OPT      = -Mcuda -Mcudalib=cusparse` (37); `CLIB     =` (38); `FFLAGS = $(DEBFLGS) $(OPT)` (41); `MDEPFLAGS = --cpp --fext=f90 --file=-` (42); `RANLIB = ranlib` (43). |
| 44–61 | CPPARGS는 CPPFLAGS·DEF_FLAGS와 FLAG_1부터 FLAG_24까지 결합한다. LIBS·INCS 설정은 주석이다. 원문: `#  CAT Preprocessing Flags` (45); `CPPARGS = $(CPPFLAGS) $(DEF_FLAGS) $(FLAG_1) $(FLAG_2) \` (47); `$(FLAG_3) $(FLAG_4) $(FLAG_5) $(FLAG_6) \` (48); `$(FLAG_7) $(FLAG_8) $(FLAG_9) $(FLAG_10)  \` (49); `$(FLAG_11) $(FLAG_12) $(FLAG_13) $(FLAG_14) \` (50); `$(FLAG_15) $(FLAG_16) $(FLAG_17) $(FLAG_18) \` (51); `$(FLAG_19) $(FLAG_20) $(FLAG_21) $(FLAG_22) \` (52); `$(FLAG_23) $(FLAG_24)` (53); `#  Libraries` (55); `#            LIBS  = $(PV3LIB) $(CLIB)  $(PARLIB) $(IOLIBS) $(MPILIB) $(GOTMLIB)` (58); `#            INCS  = $(IOINCS) $(GOTMINCS)` (59). |
| 62–71 | 접미사 규칙(suffix rule)은 .F를 .f90으로 전처리하고 목적 파일(object file)로 컴파일한다. 컴파일 다음 명령은 중간 .f90을 삭제한다. 원문: `#  Preprocessing and Compilation Directives` (63); `.SUFFIXES: .o .f90 .F .F90` (65); `.F.o:` (67); `$(CPP) $(CPPARGS) $*.F > $*.f90` (68); `$(FC)  -c $(FFLAGS) $(INCS) $*.f90` (69); `/bin/rm $*.f90` (70). |
| 72–86 | FUNWAVE-TVD 소스 목록 주석 아래 MODS와 MAIN을 정의한다. 모듈 목록에는 선박·수심 보정·기상·병렬 필드 입출력·퇴적물(sediment) 소스가 포함된다. SRCS를 결합하고 OBJS를 접미사 치환으로 만든다. MAIN 마지막 줄은 역슬래시로 다음 빈 줄에 이어진다. 원문: `#  FUNWAVE-TVD Source Code.` (72); `MODS  = mod_param.F mod_global.F mod_input.F mod_vessel.F mod_bathy_correction.F \` (75); `mod_meteo.F mod_parallel_field_io.F mod_sediment.F` (76); `MAIN  = main.F bc.F fluxes.F init.F io.F tridiagnal.F       \` (78); `breaker.F derivatives.F dispersion.F etauv_solver.F \` (79); `sponge.F sources.F masks.F parallel.F statistics.F \` (80); `wavemaker.F mixing.F nesting.F misc.F samples.F\` (81); `SRCS = $(MODS)  $(MAIN)` (83); `OBJS = $(SRCS:.F=.o)` (85). |
| 87–94 | 연결(linking) 대상은 OBJS에 의존한다. 실행 파일 연결 명령은 활성이다. ../bin/ 이동 명령은 주석이다. 원문: `#  Linking Directives` (88); `$(EXEC):	$(OBJS)` (91); `$(FC) $(FFLAGS) $(LDFLAGS) -o $(EXEC) $(OBJS) $(LIBS)` (92); `#		mv $(EXEC) ../bin/` (93). |
| 95–111 | 주석과 빈 줄을 포함한다. tarfile은 .F 소스와 Makefile_cuda를 묶는다. clean은 .o·.mod를 삭제한다. clobber는 clean을 선행한 뒤 .f90·.o·실행 파일을 삭제한다. 원문: `#  Tar Up Code` (97); `tarfile:` (100); `tar cvf funwave_tvd.tar *.F Makefile_cuda` (101); `#  Cleaning targets.` (104); `clean:` (107); `/bin/rm -f *.o *.mod` (108); `clobber:	clean` (110); `/bin/rm -f *.f90 *.o $(EXEC)` (111). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 7–11: 정밀도 안내 주석은 `DEFAULT PRECISION: SINGLE`이라고 적는다. 활성 설정에는 `FLAG_1 = -DDOUBLE_PRECISION`이 있다.
- 27·37: -DUSE_CUDA 설정은 주석이다. OPT의 -Mcuda와 -Mcudalib=cusparse는 활성이다.
- 34·47: CPPFLAGS는 DEF_FLAGS를 참조한다. CPPARGS는 CPPFLAGS와 DEF_FLAGS를 각각 나열한다.
- 100–101: 이 파일 이름은 Makefile이다. tarfile 명령이 지정하는 빌드 설정 파일 이름은 Makefile_cuda이다.
