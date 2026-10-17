---
file: models/FUNWAVE/raw/source_code/FUNWAVE-GPU/src/Makefile_mgpu
lines: 116
sha256: 1c30ddcdc6caf588d969ac5f39035883bf0a1183e0a693283cf0b9440c8cc9c8
reader: codex gpt-6.1-sol
read_date: 2026-10-17
---

# Makefile_mgpu — 판독 구간 기록

구간은 1행부터 116행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–4 | 시작 주석 뒤에서 셸(shell), 전처리(preprocessing) 옵션과 실행 파일 이름을 설정한다. 원문: `#-----------BEGIN MAKEFILE-------------------------------------------------` (1); `SHELL         = /bin/sh` (2); `DEF_FLAGS     = -P -traditional` (3); `EXEC          = funwave_mtsu` (4). |
| 5–31 | 정밀도(precision) 안내 뒤에서 -DZALPHA·-DUSE_CUDA·-DPGI·-DMGPU를 활성화한다. FLAG_1·2·3·4·6·7·8·10부터 FLAG_17까지·FLAG_21·22의 설정은 주석이다. -DDOUBLE_PRECISION·-DPARALLEL·-DCARTESIAN·-DTIMING·-DGPU_CHECK도 주석에 포함된다. 원문: `#        PRECISION          DEFAULT PRECISION: SINGLE` (7); `#                           UNCOMMENT TO SELECT DOUBLE PRECISION` (8); `#            FLAG_1 = -DDOUBLE_PRECISION` (11); `#            FLAG_2 = -DPARALLEL` (12); `#            FLAG_3 = -DCARTESIAN` (13); `#            FLAG_4 = -DSAMPLES` (14); `#              FLAG_6 = -DINTEL` (15); `#             FLAG_7 = -DMIXING` (16); `#              FLAG_8 = -DCOUPLING` (17); `FLAG_9 = -DZALPHA` (18); `#             FLAG_10 = -DMANNING` (19); `#             FLAG_11 = -DSPHERICAL_IJ_STATION` (20); `#               FLAG_12 = -DVESSEL` (21); `#              FLAG_13 = -DVIS_KENNEDY` (22); `#              FLAG_14 = -DVESSEL_PANEL_SOURCE` (23); `#              FLAG_15 = -DREALISTIC_VESSEL_BODY` (24); `#              FLAG_16 = -DMETEO` (25); `#              FLAG_17 = -DWIND` (26); `FLAG_18 = -DUSE_CUDA` (27); `FLAG_19 = -DPGI` (28); `FLAG_20 = -DMGPU` (29); `#              FLAG_21 = -DTIMING` (30); `#              FLAG_22 = -DGPU_CHECK` (31). |
| 32–46 | MPI 설정 주석 아래 전처리기(preprocessor)와 mpif90 컴파일러(compiler)를 지정한다. DEBFLGS·CLIB는 빈 값이다. OPT의 -Mcuda=cuda10.1·-Mcudalib=cusparse는 활성이다. 다음 OPT 대안은 주석이다. FFLAGS·의존성 옵션·RANLIB를 정의한다. 원문: `#  mpi defs` (33); `CPP      = /usr/bin/cpp` (35); `CPPFLAGS = $(DEF_FLAGS)` (36); `FC       = mpif90` (37); `DEBFLGS  =` (38); `OPT      = -Mcuda=cuda10.1 -Mcudalib=cusparse` (39); `#         OPT      = -Mcuda` (40); `CLIB     =` (41); `FFLAGS = $(DEBFLGS) $(OPT)` (44); `MDEPFLAGS = --cpp --fext=f90 --file=-` (45); `RANLIB = ranlib` (46). |
| 47–64 | CPPARGS는 CPPFLAGS·DEF_FLAGS와 FLAG_1부터 FLAG_24까지 결합한다. LIBS·INCS 설정은 주석이다. 원문: `#  CAT Preprocessing Flags` (48); `CPPARGS = $(CPPFLAGS) $(DEF_FLAGS) $(FLAG_1) $(FLAG_2) \` (50); `$(FLAG_3) $(FLAG_4) $(FLAG_5) $(FLAG_6) \` (51); `$(FLAG_7) $(FLAG_8) $(FLAG_9) $(FLAG_10)  \` (52); `$(FLAG_11) $(FLAG_12) $(FLAG_13) $(FLAG_14) \` (53); `$(FLAG_15) $(FLAG_16) $(FLAG_17) $(FLAG_18) \` (54); `$(FLAG_19) $(FLAG_20) $(FLAG_21) $(FLAG_22) \` (55); `$(FLAG_23) $(FLAG_24)` (56); `#  Libraries` (58); `#            LIBS  = $(PV3LIB) $(CLIB)  $(PARLIB) $(IOLIBS) $(MPILIB) $(GOTMLIB)` (61); `#            INCS  = $(IOINCS) $(GOTMINCS)` (62). |
| 65–74 | 접미사 규칙(suffix rule)은 .F를 .f90으로 전처리하고 목적 파일(object file)로 컴파일한 뒤 중간 .f90을 삭제한다. 원문: `#  Preprocessing and Compilation Directives` (66); `.SUFFIXES: .o .f90 .F .F90` (68); `.F.o:` (70); `$(CPP) $(CPPARGS) $*.F > $*.f90` (71); `$(FC)  -c $(FFLAGS) $(INCS) $*.f90` (72); `/bin/rm $*.f90` (73). |
| 75–91 | MODS에는 mod_cuda.F·mgpu_utilities.F와 교환·쇄파(breaking)·운동량(momentum)·초기화·수위 및 속도 해석·마스크·혼합·스펀지층(sponge layer) GPU 소스가 들어 있다. 일반 모듈과 MAIN의 본체 소스도 나열한다. SRCS를 결합하고 OBJS를 접미사 치환으로 만든다. 원문: `#  FUNWAVE-TVD Source Code.` (75); `MODS  = mod_param.F mod_global.F mod_input.F mod_cuda.F mgpu_utilities.F mod_vessel.F mod_bathy_correction.F \` (78); `mod_meteo.F mod_parallel_field_io.F mod_sediment.F \` (79); `exchange_gpu.F breaker_gpu.F moment_gpu.F init_gpu.F etauv_solver_gpu.F \` (80); `masks_gpu.F mixing_gpu.F sponge_gpu.F` (81); `MAIN  = main.F bc.F fluxes.F init.F io.F tridiagnal.F       \` (83); `breaker.F  derivatives.F dispersion.F etauv_solver.F \` (84); `sponge.F sources.F masks.F parallel.F statistics.F \` (85); `wavemaker.F mixing.F nesting.F misc.F samples.F` (86); `SRCS = $(MODS)  $(MAIN)` (88); `OBJS = $(SRCS:.F=.o)` (90). |
| 92–99 | 연결(linking) 대상은 OBJS에 의존한다. 실행 파일 연결 명령은 활성이다. ../bin/ 이동 명령은 주석이다. 원문: `#  Linking Directives` (93); `$(EXEC):	$(OBJS)` (96); `$(FC) $(FFLAGS) $(LDFLAGS) -o $(EXEC) $(OBJS) $(LIBS)` (97); `#		mv $(EXEC) ../bin/` (98). |
| 100–116 | 주석과 빈 줄을 포함한다. tarfile은 .F 소스와 Makefile을 묶는다. clean은 .o·.mod를 삭제한다. clobber는 clean을 선행한 뒤 .f90·.o·실행 파일을 삭제한다. 원문: `#  Tar Up Code` (102); `tarfile:` (105); `tar cvf funwave_tvd.tar *.F  Makefile` (106); `#  Cleaning targets.` (109); `clean:` (112); `/bin/rm -f *.o *.mod` (113); `clobber:	clean` (115); `/bin/rm -f *.f90 *.o $(EXEC)` (116). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 12·29·37: -DPARALLEL 설정은 주석이다. -DMGPU는 활성이다. 컴파일러 이름은 mpif90이다.
- 39: 활성 CUDA 옵션에는 버전 문자열 `cuda10.1`이 들어 있다.
- 36·50: CPPFLAGS는 DEF_FLAGS를 참조한다. CPPARGS는 CPPFLAGS와 DEF_FLAGS를 각각 나열한다.
- 105–106: 이 파일 이름은 Makefile_mgpu이다. tarfile 명령이 지정하는 빌드 설정 파일 이름은 Makefile이다.
