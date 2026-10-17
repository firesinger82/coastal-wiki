---
file: models/FUNWAVE/raw/source_code/FUNWAVE-TVD/GNUMake/Old_Version_Makefiles/Makefile-funwaveRDE
lines: 104
sha256: 159cb0a647a6ffa824e687f496145bce075a0e8439b62c84daece8cb5e295d05
reader: codex gpt-6.1-sol
read_date: 2026-10-17
---

# Makefile-funwaveRDE — 판독 구간 기록

구간은 1행부터 104행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–4 | 시작 주석 뒤에서 셸(shell), 전처리(preprocessing) 옵션과 실행 파일 이름을 설정한다. 원문: `#-----------BEGIN MAKEFILE-------------------------------------------------` (1); `SHELL         = /bin/sh` (2); `DEF_FLAGS     = -P -traditional` (3); `EXEC          = funwave_gnu` (4). |
| 5–22 | 정밀도(precision) 안내 뒤에서 -DDOUBLE_PRECISION·-DPARALLEL·-DSAMPLES·-DCARTESIAN을 활성화한다. FLAG_6·7·8·9·10·11·12 설정은 주석이다. 원문: `#        PRECISION          DEFAULT PRECISION: SINGLE` (7); `#                           UNCOMMENT TO SELECT DOUBLE PRECISION` (8); `FLAG_1 = -DDOUBLE_PRECISION` (11); `FLAG_2 = -DPARALLEL` (12); `FLAG_3 = -DSAMPLES` (13); `FLAG_4 = -DCARTESIAN` (14); `#              FLAG_6 = -DINTEL` (15); `#             FLAG_7 = -DMIXING` (16); `#             FLAG_8 = -DCOUPLING` (17); `#             FLAG_9 = -DZALPHA` (18); `#             FLAG_10 = -DMANNING` (19); `#             FLAG_11 = -DSPHERICAL_IJ_STATION` (20); `#             FLAG_12 = -DVESSEL` (21). |
| 23–36 | MPI 설정 주석 아래 전처리기(preprocessor)와 /usr/local/mpich/bin/mpif90 컴파일러(compiler)를 지정한다. DEBFLGS·OPT·CLIB는 빈 값이다. FFLAGS·의존성 옵션·RANLIB를 설정한다. 원문: `#  mpi defs` (24); `CPP      = /usr/bin/cpp` (26); `CPPFLAGS = $(DEF_FLAGS)` (27); `FC       = /usr/local/mpich/bin/mpif90` (28); `DEBFLGS  =` (29); `OPT      =` (30); `CLIB     =` (31); `FFLAGS = $(DEBFLGS) $(OPT)` (34); `MDEPFLAGS = --cpp --fext=f90 --file=-` (35); `RANLIB = ranlib` (36). |
| 37–54 | CPPARGS는 CPPFLAGS·DEF_FLAGS와 FLAG_1부터 FLAG_24까지 결합한다. LIBS·INCS 설정은 주석이다. 원문: `#  CAT Preprocessing Flags` (38); `CPPARGS = $(CPPFLAGS) $(DEF_FLAGS) $(FLAG_1) $(FLAG_2) \` (40); `$(FLAG_3) $(FLAG_4) $(FLAG_5) $(FLAG_6) \` (41); `$(FLAG_7) $(FLAG_8) $(FLAG_9) $(FLAG_10)  \` (42); `$(FLAG_11) $(FLAG_12) $(FLAG_13) $(FLAG_14) \` (43); `$(FLAG_15) $(FLAG_16) $(FLAG_17) $(FLAG_18) \` (44); `$(FLAG_19) $(FLAG_20) $(FLAG_21) $(FLAG_22) \` (45); `$(FLAG_23) $(FLAG_24)` (46); `#  Libraries` (48); `#            LIBS  = $(PV3LIB) $(CLIB)  $(PARLIB) $(IOLIBS) $(MPILIB) $(GOTMLIB)` (51); `#            INCS  = $(IOINCS) $(GOTMINCS)` (52). |
| 55–64 | 접미사 규칙(suffix rule)은 전처리한 .f90을 목적 파일(object file)로 컴파일하고 /bin/rm으로 .f90을 삭제한다. 원문: `#  Preprocessing and Compilation Directives` (56); `.SUFFIXES: .o .f90 .F .F90` (58); `.F.o:` (60); `$(CPP) $(CPPARGS) $*.F > $*.f90` (61); `$(FC)  -c $(FFLAGS) $(INCS) $*.f90` (62); `/bin/rm $*.f90` (63). |
| 65–79 | 모듈 목록에는 매개변수·전역·입력·선박(vessel)·병렬 필드 입출력·수심 보정 소스가 들어 있다. MAIN에는 본체 소스를 나열한다. SRCS는 두 목록을 결합한다. OBJS는 .F를 .o로 치환한다. MAIN 마지막 줄은 역슬래시로 다음 빈 줄에 이어진다. 원문: `#  FUNWAVE-TVD Source Code.` (65); `MODS  = mod_param.F	mod_global.F	mod_input.F mod_vessel.F \` (68); `mod_parallel_field_io.F mod_bathy_correction.F` (69); `MAIN  = main.F bc.F fluxes.F init.F io.F tridiagnal.F       \` (71); `breaker.F derivatives.F dispersion.F etauv_solver.F \` (72); `sponge.F sources.F masks.F parallel.F statistics.F \` (73); `wavemaker.F mixing.F nesting.F misc.F samples.F\` (74); `SRCS = $(MODS)  $(MAIN)` (76); `OBJS = $(SRCS:.F=.o)` (78). |
| 80–87 | 연결(linking) 대상은 OBJS에 의존한다. 실행 파일을 연결한 뒤 ../bin/으로 이동한다. 원문: `#  Linking Directives` (81); `$(EXEC):	$(OBJS)` (84); `$(FC) $(FFLAGS) $(LDFLAGS) -o $(EXEC) $(OBJS) $(LIBS)` (85); `mv $(EXEC) ../bin/` (86). |
| 88–104 | 주석과 빈 줄을 포함한다. tarfile은 소스와 Makefile을 묶는다. clean은 .o·.mod를 삭제한다. clobber는 clean을 선행한 뒤 .f90·.o·실행 파일을 삭제한다. 원문: `#  Tar Up Code` (90); `tarfile:` (93); `tar cvf funwave_tvd.tar *.F  Makefile` (94); `#  Cleaning targets.` (97); `clean:` (100); `/bin/rm -f *.o *.mod` (101); `clobber:	clean` (103); `/bin/rm -f *.f90 *.o $(EXEC)` (104). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 7–11: 정밀도 안내 주석은 `DEFAULT PRECISION: SINGLE`이라고 적는다. 활성 설정에는 `FLAG_1 = -DDOUBLE_PRECISION`이 있다.
- 27·40: CPPFLAGS는 DEF_FLAGS를 참조한다. CPPARGS는 CPPFLAGS와 DEF_FLAGS를 각각 나열한다.
- 86·103–104: 연결 뒤 실행 파일을 ../bin/으로 이동한다. clobber는 현재 디렉터리의 `$(EXEC)`를 삭제 대상으로 지정한다.
