---
file: models/FUNWAVE/raw/source_code/FUNWAVE-GPU/src/Makefile_cuda
lines: 119
sha256: f85c5ef9a1a4853c77fc4f22a31099f4986a247e9d4d868dd6d3fa0866762ed4
reader: codex gpt-6.1-sol
read_date: 2026-10-17
---

# Makefile_cuda — 판독 구간 기록

구간은 1행부터 119행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–4 | 시작 주석 뒤에서 셸(shell), 전처리(preprocessing) 옵션과 실행 파일 이름을 설정한다. 원문: `#-----------BEGIN MAKEFILE-------------------------------------------------` (1); `SHELL         = /bin/sh` (2); `DEF_FLAGS     = -P -traditional` (3); `EXEC          = funwave_fullcuda` (4). |
| 5–30 | 정밀도(precision) 안내 뒤에서 -DCARTESIAN·-DUSE_CUDA·-DPGI를 활성화한다. FLAG_1·2·4·6부터 FLAG_17까지·FLAG_20·21의 설정은 주석이다. -DDOUBLE_PRECISION·-DPARALLEL·-DTIMING·-DGPU_CHECK도 주석에 포함된다. 원문: `#        PRECISION          DEFAULT PRECISION: SINGLE` (7); `#                           UNCOMMENT TO SELECT DOUBLE PRECISION` (8); `#            FLAG_1 = -DDOUBLE_PRECISION` (11); `#            FLAG_2 = -DPARALLEL` (12); `FLAG_3 = -DCARTESIAN` (13); `#            FLAG_4 = -DSAMPLES` (14); `#              FLAG_6 = -DINTEL` (15); `#             FLAG_7 = -DMIXING` (16); `#              FLAG_8 = -DCOUPLING` (17); `#             FLAG_9 = -DZALPHA` (18); `#             FLAG_10 = -DMANNING` (19); `#             FLAG_11 = -DSPHERICAL_IJ_STATION` (20); `#               FLAG_12 = -DVESSEL` (21); `#              FLAG_13 = -DVIS_KENNEDY` (22); `#              FLAG_14 = -DVESSEL_PANEL_SOURCE` (23); `#              FLAG_15 = -DREALISTIC_VESSEL_BODY` (24); `#              FLAG_16 = -DMETEO` (25); `#              FLAG_17 = -DWIND` (26); `FLAG_18 = -DUSE_CUDA` (27); `FLAG_19 = -DPGI` (28); `#              FLAG_20 = -DTIMING` (29); `#			  FLAG_21 = -DGPU_CHECK` (30). |
| 31–47 | MPI 설정 주석 아래 전처리기(preprocessor)와 nvfortran 컴파일러(compiler)를 지정한다. DEBFLGS·CLIB는 빈 값이다. OPT의 -cuda·-gpu=cc120·-cudalib=cusparse는 활성이다. 이어지는 OPT 대안 세 줄은 주석이다. FFLAGS·의존성 옵션·RANLIB를 정의한다. 원문: `#  mpi defs` (32); `CPP      = /usr/bin/cpp` (34); `CPPFLAGS = $(DEF_FLAGS)` (35); `FC       = nvfortran` (36); `DEBFLGS  =` (37); `OPT      = -cuda -gpu=cc120 -cudalib=cusparse` (38); `#         OPT      = -Mcuda -Mcudalib=cusparse` (39); `#         OPT      = -Mcuda=ptxinfo` (40); `#         OPT      = -Mcuda` (41); `CLIB     =` (42); `FFLAGS = $(DEBFLGS) $(OPT)` (45); `MDEPFLAGS = --cpp --fext=f90 --file=-` (46); `RANLIB = ranlib` (47). |
| 48–65 | CPPARGS는 CPPFLAGS·DEF_FLAGS와 FLAG_1부터 FLAG_24까지 결합한다. LIBS·INCS 설정은 주석이다. 원문: `#  CAT Preprocessing Flags` (49); `CPPARGS = $(CPPFLAGS) $(DEF_FLAGS) $(FLAG_1) $(FLAG_2) \` (51); `$(FLAG_3) $(FLAG_4) $(FLAG_5) $(FLAG_6) \` (52); `$(FLAG_7) $(FLAG_8) $(FLAG_9) $(FLAG_10)  \` (53); `$(FLAG_11) $(FLAG_12) $(FLAG_13) $(FLAG_14) \` (54); `$(FLAG_15) $(FLAG_16) $(FLAG_17) $(FLAG_18) \` (55); `$(FLAG_19) $(FLAG_20) $(FLAG_21) $(FLAG_22) \` (56); `$(FLAG_23) $(FLAG_24)` (57); `#  Libraries` (59); `#            LIBS  = $(PV3LIB) $(CLIB)  $(PARLIB) $(IOLIBS) $(MPILIB) $(GOTMLIB)` (62); `#            INCS  = $(IOINCS) $(GOTMINCS)` (63). |
| 66–75 | 접미사 규칙(suffix rule)은 .F를 .f90으로 전처리하고 목적 파일(object file)로 컴파일한 뒤 중간 .f90을 삭제한다. 원문: `#  Preprocessing and Compilation Directives` (67); `.SUFFIXES: .o .f90 .F .F90` (69); `.F.o:` (71); `$(CPP) $(CPPARGS) $*.F > $*.f90` (72); `$(FC)  -c $(FFLAGS) $(INCS) $*.f90` (73); `/bin/rm $*.f90` (74). |
| 76–92 | MODS에는 mod_cuda.F와 교환·쇄파(breaking)·운동량(momentum)·초기화·수위 및 속도 해석·마스크·혼합·스펀지층(sponge layer) GPU 소스가 포함된다. MAIN에는 일반 본체 소스를 나열한다. SRCS는 두 목록을 결합한다. OBJS는 .F를 .o로 치환한다. 원문: `#  FUNWAVE-TVD Source Code.` (76); `MODS  = mod_param.F mod_global.F mod_input.F mod_cuda.F mod_vessel.F mod_bathy_correction.F \` (79); `mod_meteo.F mod_parallel_field_io.F mod_sediment.F \` (80); `exchange_gpu.F breaker_gpu.F moment_gpu.F init_gpu.F etauv_solver_gpu.F \` (81); `masks_gpu.F mixing_gpu.F sponge_gpu.F` (82); `MAIN  = main.F bc.F fluxes.F init.F io.F tridiagnal.F       \` (84); `breaker.F  derivatives.F dispersion.F etauv_solver.F \` (85); `sponge.F sources.F masks.F parallel.F statistics.F \` (86); `wavemaker.F mixing.F nesting.F misc.F samples.F` (87); `SRCS = $(MODS)  $(MAIN)` (89); `OBJS = $(SRCS:.F=.o)` (91). |
| 93–100 | 연결(linking) 대상은 OBJS에 의존한다. 실행 파일 연결 명령은 활성이다. ../bin/ 이동 명령은 주석이다. 원문: `#  Linking Directives` (94); `$(EXEC):	$(OBJS)` (97); `$(FC) $(FFLAGS) $(LDFLAGS) -o $(EXEC) $(OBJS) $(LIBS)` (98); `#		mv $(EXEC) ../bin/` (99). |
| 101–108 | 주석과 빈 줄을 포함한다. tarfile은 .F 소스와 Makefile_cuda를 funwave_tvd.tar로 묶는다. 원문: `#  Tar Up Code` (103); `tarfile:` (106); `tar cvf funwave_tvd.tar *.F  Makefile_cuda` (107). |
| 109–117 | 정리 주석과 빈 줄을 포함한다. clean은 .o·.mod를 삭제한다. clobber는 clean을 선행한 뒤 .f90·.o·실행 파일을 삭제한다. 원문: `#  Cleaning targets.` (110); `clean:` (113); `/bin/rm -f *.o *.mod` (114); `clobber:	clean` (116); `/bin/rm -f *.f90 *.o $(EXEC)` (117). |
| 118–119 | move 대상은 실행 파일을 ../yuan/rip_2d/work로 이동한다. 이 대상 줄에는 선행 의존 대상이 없다. 원문: `move:` (118); `/bin/mv $(EXEC) ../yuan/rip_2d/work` (119). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 35·51: CPPFLAGS는 DEF_FLAGS를 참조한다. CPPARGS는 CPPFLAGS와 DEF_FLAGS를 각각 나열한다.
- 36–38: 컴파일러는 nvfortran으로 고정되어 있다. GPU 대상 옵션에는 `-gpu=cc120`이 들어 있다.
- 118–119: move의 목적지는 `../yuan/rip_2d/work`로 고정되어 있다. move 대상에는 실행 파일을 먼저 만드는 의존 대상이나 목적지 생성 명령이 없다.
