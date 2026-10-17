---
file: models/FUNWAVE/raw/source_code/FUNWAVE-TVD/GNUMake/Old_Version_Makefiles/Makefile-Lightning-Intel
lines: 105
sha256: 463b9b16623337b01f9381928bd98e9e7dfa527335365bd076247f6262ef3640
reader: codex gpt-6.1-sol
read_date: 2026-10-17
---

# Makefile-Lightning-Intel — 판독 구간 기록

구간은 1행부터 105행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–4 | 시작 주석 뒤에서 셸(shell), 전처리(preprocessing) 기본 옵션과 실행 파일 이름을 설정한다. 원문: `#-----------BEGIN MAKEFILE-------------------------------------------------` (1); `SHELL         = /bin/sh` (2); `DEF_FLAGS     = -P -traditional` (3); `EXEC          = funwave_intel` (4). |
| 5–21 | 구분 주석과 정밀도(precision) 안내 뒤에 활성 전처리 플래그를 정의한다. FLAG_1·2·3·4·6은 활성이다. FLAG_5·7·8·9·10 줄은 주석이다. 원문: `#        PRECISION          DEFAULT PRECISION: SINGLE` (7); `#                           UNCOMMENT TO SELECT DOUBLE PRECISION` (8); `FLAG_1 = -DDOUBLE_PRECISION` (11); `FLAG_2 = -DPARALLEL` (12); `FLAG_3 = -DSAMPLES` (13); `FLAG_4 = -DCARTESIAN` (14); `#	    FLAG_5 = -DCRAY` (15); `FLAG_6 = -DINTEL` (16); `#             FLAG_7 = -DMIXING` (17); `#             FLAG_8 = -DCOUPLING` (18); `#             FLAG_9 = -DZALPHA` (19); `#             FLAG_10 = -DMANNING` (20). |
| 22–36 | MPI 설정 주석 아래 전처리기(preprocessor)와 Fortran 컴파일러(compiler)를 지정한다. DEBFLGS·OPT·CLIB는 빈 값이다. FFLAGS 뒤의 옵션과 MPILIB 뒤의 라이브러리 이름은 인라인 주석이다. 원문: `#  mpi defs` (23); `CPP      = /usr/bin/cpp` (25); `CPPFLAGS = $(DEF_FLAGS)` (26); `FC       = ftn` (27); `DEBFLGS  =` (28); `OPT      =` (29); `CLIB     =` (30); `FFLAGS = $(DEBFLGS) $(OPT) #-fPIC -g -O2` (33); `MDEPFLAGS = --cpp --fext=f90 --file=-` (34); `RANLIB = ranlib` (35); `MPILIB = # -lmpi` (36). |
| 37–54 | CPPARGS는 CPPFLAGS·DEF_FLAGS와 FLAG_1부터 FLAG_24까지 이어 붙인다. LIBS는 여섯 라이브러리 변수를 모은다. INCS 설정은 주석이다. 원문: `#  CAT Preprocessing Flags` (38); `CPPARGS = $(CPPFLAGS) $(DEF_FLAGS) $(FLAG_1) $(FLAG_2) \` (40); `$(FLAG_3) $(FLAG_4) $(FLAG_5) $(FLAG_6) \` (41); `$(FLAG_7) $(FLAG_8) $(FLAG_9) $(FLAG_10)  \` (42); `$(FLAG_11) $(FLAG_12) $(FLAG_13) $(FLAG_14) \` (43); `$(FLAG_15) $(FLAG_16) $(FLAG_17) $(FLAG_18) \` (44); `$(FLAG_19) $(FLAG_20) $(FLAG_21) $(FLAG_22) \` (45); `$(FLAG_23) $(FLAG_24)` (46); `#  Libraries` (48); `LIBS  = $(PV3LIB) $(CLIB)  $(PARLIB) $(IOLIBS) $(MPILIB) $(GOTMLIB)` (51); `#            INCS  = $(IOINCS) $(GOTMINCS)` (52). |
| 55–64 | 접미사 규칙(suffix rule)을 선언한다. .F.o 규칙은 .F를 .f90으로 전처리한 뒤 목적 파일(object file)로 컴파일한다. 중간 파일 삭제 명령은 주석이다. 원문: `#  Preprocessing and Compilation Directives` (56); `.SUFFIXES: .o .f90 .F .F90` (58); `.F.o:` (60); `$(CPP) $(CPPARGS) $*.F > $*.f90` (61); `$(FC)  -c $(FFLAGS) $(INCS) $*.f90` (62); `#	\rm $*.f90` (63). |
| 65–79 | FUNWAVE-TVD 소스 목록 주석 뒤에 모듈 소스와 본체 소스를 나열한다. SRCS는 두 목록을 결합한다. OBJS는 .F 접미사를 .o로 치환한다. MAIN의 마지막 줄도 역슬래시로 이어지며 다음 줄은 빈 줄이다. 원문: `#  FUNWAVE-TVD Source Code.` (65); `MODS  = mod_param.F	mod_global.F	mod_input.F mod_vessel.F  mod_bathy_correction.F \` (68); `mod_parallel_field_io.F mod_meteo.F` (69); `MAIN  = main.F bc.F fluxes.F init.F io.F tridiagnal.F       \` (71); `breaker.F derivatives.F dispersion.F etauv_solver.F \` (72); `sponge.F sources.F masks.F parallel.F statistics.F \` (73); `wavemaker.F mixing.F nesting.F misc.F samples.F\` (74); `SRCS = $(MODS)  $(MAIN)` (76); `OBJS = $(SRCS:.F=.o)` (78). |
| 80–87 | 연결(linking) 대상은 OBJS에 의존한다. 컴파일러로 실행 파일을 연결한 다음 ../bin/으로 이동한다. 연결 명령의 -Bdynamic은 인라인 주석이다. 원문: `#  Linking Directives` (81); `$(EXEC):	$(OBJS)` (84); `$(FC) $(FFLAGS) $(LDFLAGS) -o $(EXEC) $(OBJS) $(LIBS) #-Bdynamic` (85); `mv $(EXEC) ../bin/` (86). |
| 88–105 | 구분 주석과 빈 줄을 포함한다. tarfile은 .F 파일과 Makefile을 묶는다. clean은 .o·.mod를 삭제한다. clobber는 clean에 의존하며 .f90·.o·현재 디렉터리의 실행 파일을 삭제한다. 원문: `#  Tar Up Code` (90); `tarfile:` (93); `tar cvf funwave_tvd.tar *.F  Makefile` (94); `#  Cleaning targets.` (97); `clean:` (100); `/bin/rm -f *.o *.mod` (101); `clobber:	clean` (103); `/bin/rm -f *.f90 *.o $(EXEC)` (104). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 7–11: 정밀도 안내 주석은 `DEFAULT PRECISION: SINGLE`이라고 적는다. 활성 설정에는 `FLAG_1 = -DDOUBLE_PRECISION`이 있다.
- 26·40: CPPFLAGS는 DEF_FLAGS를 참조한다. CPPARGS는 CPPFLAGS와 DEF_FLAGS를 각각 다시 나열한다.
- 68–85: 모듈 소스 목록은 MODS에 나열되어 있다. 이 파일에는 개별 모듈 목적 파일 사이의 의존 관계 규칙이 없다.
- 86·103–104: 연결 뒤 실행 파일을 ../bin/으로 이동한다. clobber의 실행 파일 삭제 대상은 경로 접두사 없는 `$(EXEC)`이다.
