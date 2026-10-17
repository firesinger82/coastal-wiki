---
file: models/FUNWAVE/raw/source_code/FUNWAVE-GPU/src/Makefile_paral
lines: 113
sha256: 55a87091762ab7400a8c0c11672c37fcb1304890d902a5ee224653793593b82d
reader: codex gpt-6.1-sol
read_date: 2026-10-17
---

# Makefile_paral — 판독 구간 기록

구간은 1행부터 113행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–4 | 시작 주석 뒤에서 셸(shell), 전처리(preprocessing) 옵션과 실행 파일 이름을 설정한다. 원문: `#-----------BEGIN MAKEFILE-------------------------------------------------` (1); `SHELL         = /bin/sh` (2); `DEF_FLAGS     = -P -traditional` (3); `EXEC          = funwave_paral` (4). |
| 5–29 | 정밀도(precision) 안내 뒤에서 -DPARALLEL·-DZALPHA·-DPGI를 활성화한다. FLAG_1·3·4·6·7·8·10부터 FLAG_18까지·FLAG_20의 설정은 주석이다. -DDOUBLE_PRECISION·-DCARTESIAN·-DUSE_CUDA도 주석에 포함된다. 원문: `#        PRECISION          DEFAULT PRECISION: SINGLE` (7); `#                           UNCOMMENT TO SELECT DOUBLE PRECISION` (8); `#            FLAG_1 = -DDOUBLE_PRECISION` (11); `FLAG_2 = -DPARALLEL` (12); `#            FLAG_3 = -DCARTESIAN` (13); `#            FLAG_4 = -DSAMPLES` (14); `#              FLAG_6 = -DINTEL` (15); `#             FLAG_7 = -DMIXING` (16); `#              FLAG_8 = -DCOUPLING` (17); `FLAG_9 = -DZALPHA` (18); `#             FLAG_10 = -DMANNING` (19); `#             FLAG_11 = -DSPHERICAL_IJ_STATION` (20); `#               FLAG_12 = -DVESSEL` (21); `#              FLAG_13 = -DVIS_KENNEDY` (22); `#              FLAG_14 = -DVESSEL_PANEL_SOURCE` (23); `#              FLAG_15 = -DREALISTIC_VESSEL_BODY` (24); `#              FLAG_16 = -DMETEO` (25); `#              FLAG_17 = -DWIND` (26); `#              FLAG_18 = -DUSE_CUDA` (27); `FLAG_19 = -DPGI` (28); `#              FLAG_20 = -DTIMING` (29). |
| 30–45 | MPI 설정 주석 아래 전처리기(preprocessor)와 mpif90 컴파일러(compiler)를 지정한다. DEBFLGS·CLIB는 빈 값이다. 활성 OPT는 -O2이다. CUDA 버전 cuda10.0이 들어 있는 OPT 대안과 -Mcuda 대안은 주석이다. FFLAGS·의존성 옵션·RANLIB를 정의한다. 원문: `#  mpi defs` (31); `CPP      = /usr/bin/cpp` (33); `CPPFLAGS = $(DEF_FLAGS)` (34); `FC       = mpif90` (35); `DEBFLGS  =` (36); `OPT      = -O2` (37); `#         OPT      = -fast -Mcuda=cuda10.0 -Mcudalib=cusparse` (38); `#         OPT      = -Mcuda` (39); `CLIB     =` (40); `FFLAGS = $(DEBFLGS) $(OPT)` (43); `MDEPFLAGS = --cpp --fext=f90 --file=-` (44); `RANLIB = ranlib` (45). |
| 46–63 | CPPARGS는 CPPFLAGS·DEF_FLAGS와 FLAG_1부터 FLAG_24까지 결합한다. LIBS·INCS 설정은 주석이다. 원문: `#  CAT Preprocessing Flags` (47); `CPPARGS = $(CPPFLAGS) $(DEF_FLAGS) $(FLAG_1) $(FLAG_2) \` (49); `$(FLAG_3) $(FLAG_4) $(FLAG_5) $(FLAG_6) \` (50); `$(FLAG_7) $(FLAG_8) $(FLAG_9) $(FLAG_10)  \` (51); `$(FLAG_11) $(FLAG_12) $(FLAG_13) $(FLAG_14) \` (52); `$(FLAG_15) $(FLAG_16) $(FLAG_17) $(FLAG_18) \` (53); `$(FLAG_19) $(FLAG_20) $(FLAG_21) $(FLAG_22) \` (54); `$(FLAG_23) $(FLAG_24)` (55); `#  Libraries` (57); `#            LIBS  = $(PV3LIB) $(CLIB)  $(PARLIB) $(IOLIBS) $(MPILIB) $(GOTMLIB)` (60); `#            INCS  = $(IOINCS) $(GOTMINCS)` (61). |
| 64–73 | 접미사 규칙(suffix rule)은 .F를 .f90으로 전처리하고 목적 파일(object file)로 컴파일한 뒤 중간 .f90을 삭제한다. 원문: `#  Preprocessing and Compilation Directives` (65); `.SUFFIXES: .o .f90 .F .F90` (67); `.F.o:` (69); `$(CPP) $(CPPARGS) $*.F > $*.f90` (70); `$(FC)  -c $(FFLAGS) $(INCS) $*.f90` (71); `/bin/rm $*.f90` (72). |
| 74–88 | MODS에는 매개변수·전역·입력·선박(vessel)·수심 보정·기상(meteorology)·병렬 필드 입출력·퇴적물(sediment) 소스를 나열한다. MAIN에는 본체 소스를 나열한다. SRCS는 두 목록을 결합한다. OBJS는 .F를 .o로 치환한다. MAIN 마지막 줄은 역슬래시로 다음 빈 줄에 이어진다. 원문: `#  FUNWAVE-TVD Source Code.` (74); `MODS  = mod_param.F mod_global.F mod_input.F mod_vessel.F mod_bathy_correction.F \` (77); `mod_meteo.F mod_parallel_field_io.F mod_sediment.F` (78); `MAIN  = main.F bc.F fluxes.F init.F io.F tridiagnal.F       \` (80); `breaker.F derivatives.F dispersion.F etauv_solver.F \` (81); `sponge.F sources.F masks.F parallel.F statistics.F \` (82); `wavemaker.F mixing.F nesting.F misc.F samples.F\` (83); `SRCS = $(MODS)  $(MAIN)` (85); `OBJS = $(SRCS:.F=.o)` (87). |
| 89–96 | 연결(linking) 대상은 OBJS에 의존한다. 실행 파일 연결 명령은 활성이다. ../bin/ 이동 명령은 주석이다. 원문: `#  Linking Directives` (90); `$(EXEC):	$(OBJS)` (93); `$(FC) $(FFLAGS) $(LDFLAGS) -o $(EXEC) $(OBJS) $(LIBS)` (94); `#		mv $(EXEC) ../bin/` (95). |
| 97–113 | 주석과 빈 줄을 포함한다. tarfile은 .F 소스와 Makefile을 묶는다. clean은 .o·.mod를 삭제한다. clobber는 clean을 선행한 뒤 .f90·.o·실행 파일을 삭제한다. 원문: `#  Tar Up Code` (99); `tarfile:` (102); `tar cvf funwave_tvd.tar *.F  Makefile` (103); `#  Cleaning targets.` (106); `clean:` (109); `/bin/rm -f *.o *.mod` (110); `clobber:	clean` (112); `/bin/rm -f *.f90 *.o $(EXEC)` (113). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 34·49: CPPFLAGS는 DEF_FLAGS를 참조한다. CPPARGS는 CPPFLAGS와 DEF_FLAGS를 각각 나열한다.
- 44–45: MDEPFLAGS와 RANLIB는 정의되어 있다. 이 파일의 명령 줄은 두 변수를 참조하지 않는다.
- 102–103: 이 파일 이름은 Makefile_paral이다. tarfile 명령이 지정하는 빌드 설정 파일 이름은 Makefile이다.
