---
file: models/FUNWAVE/raw/source_code/FUNWAVE-TVD/GNUMake/Old_Version_Makefiles/Makefile-Koehr-Sediment-intel
lines: 112
sha256: 6878c99aab08703175f4825176363f85fb78c335ae7cc1ec49de5c8fff3bd46d
reader: codex gpt-6.1-sol
read_date: 2026-10-17
---

# Makefile-Koehr-Sediment-intel — 판독 구간 기록

구간은 1행부터 112행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | 시작 구분 주석(1). 셸(shell)·전처리 기본 옵션·실행 이름은 `SHELL         = /bin/sh` (2), `DEF_FLAGS     = -P -traditional` (3), `EXEC          = funwave_sediment` (4). 정밀도(precision) 안내는 주석 `#        PRECISION          DEFAULT PRECISION: SINGLE` (7), `#                           UNCOMMENT TO SELECT DOUBLE PRECISION` (8). 구분 주석(5–6·9)과 빈 줄(10)을 포함한다. |
| 11–25 | 활성 전처리 플래그(preprocessor flag)는 `FLAG_2 = -DPARALLEL` (12), `FLAG_3 = -DSAMPLES` (13), `FLAG_4 = -DCARTESIAN` (14), `FLAG_6 = -DINTEL` (16), `FLAG_11 = -DSEDIMENT` (21), `FLAG_12 = -DCHECK_MASS_CONSERVATION` (22). 다음 플래그 설정은 모두 주석이다: `#            FLAG_1 = -DDOUBLE_PRECISION` (11), `#	    FLAG_5 = -DVESSEL` (15), `#             FLAG_7 = -DMIXING` (17), `#             FLAG_8 = -DCOUPLING` (18), `#             FLAG_9 = -DZALPHA` (19), `#             FLAG_10 = -DMANNING` (20), `#	      FLAG_13 = -DWIND` (23), `#	      FLAG_14 = -DMETEO` (24). 끝 빈 줄(25). 조건 분기는 없다. |
| 26–40 | MPI 설정 안내 주석(26–28). 전처리기·컴파일러 설정은 `CPP      = /usr/bin/cpp` (29), `CPPFLAGS = $(DEF_FLAGS)` (30), `FC       = ifort` (31). 디버그(debug)·최적화·C 라이브러리 값은 빈 설정 `DEBFLGS  =` (32), `OPT      =` (33), `CLIB     =` (34). 컴파일 옵션 구성식은 `FFLAGS = $(DEBFLGS) $(OPT) -fPIC` (37)이며 `-fPIC`을 활성 옵션으로 넣는다. 의존성 옵션·인덱스 도구·MPI 링크 설정은 `MDEPFLAGS = --cpp --fext=f90 --file=-` (38), `RANLIB = ranlib` (39), `MPILIB = -lmpi` (40). 구분 주석·빈 줄(35–36)을 포함한다. |
| 41–58 | 전처리 인수 연결식은 `CPPARGS = $(CPPFLAGS) $(DEF_FLAGS) $(FLAG_1) $(FLAG_2) \` (44), `$(FLAG_3) $(FLAG_4) $(FLAG_5) $(FLAG_6) \` (45), `$(FLAG_7) $(FLAG_8) $(FLAG_9) $(FLAG_10)  \` (46), `$(FLAG_11) $(FLAG_12) $(FLAG_13) $(FLAG_14) \` (47), `$(FLAG_15) $(FLAG_16) $(FLAG_17) $(FLAG_18) \` (48), `$(FLAG_19) $(FLAG_20) $(FLAG_21) $(FLAG_22) \` (49), `$(FLAG_23) $(FLAG_24)` (50). 라이브러리 구성식은 `LIBS  = $(PV3LIB) $(CLIB)  $(PARLIB) $(IOLIBS) $(MPILIB) $(GOTMLIB)` (55). 포함 경로 설정 `#            INCS  = $(IOINCS) $(GOTMINCS)` (56)는 주석이다. 전처리·라이브러리 안내 주석(41–43·51–53), 빈 줄(54·57–58)을 포함한다. |
| 59–71 | 접미사 규칙 선언은 `.SUFFIXES: .o .f90 .F .F90` (62). `.F.o:` (64) 규칙의 실행 명령은 `$(CPP) $(CPPARGS) $*.F > $*.f90` (65)와 `$(FC)  -c $(FFLAGS) $(INCS) $*.f90` (66)이며 전처리 뒤 컴파일한다. `#	\rm $*.f90` (67)는 중간 파일 삭제를 적은 주석이다. 전처리·컴파일 및 소스 목록 안내 주석(59–61·68–70), 빈 줄(63·71)을 포함한다. |
| 72–87 | 모듈 목록 원문은 `MODS  = mod_param.F	mod_global.F	mod_input.F mod_vessel.F  mod_bathy_correction.F \` (72), `mod_parallel_field_io.F mod_meteo.F mod_sediment.F mod_tracer.F` (73). 주요 소스 목록 원문은 `MAIN  = main.F bc.F fluxes.F init.F io.F tridiagnal.F       \` (75), `breaker.F derivatives.F dispersion.F etauv_solver.F \` (76), `sponge.F sources.F masks.F parallel.F statistics.F  \` (77), `wavemaker.F mixing.F nesting.F misc.F samples.F` (78). 소스 목록 결합식은 `SRCS = $(MODS)  $(MAIN)` (80). 오브젝트(object) 목록 변환식은 `OBJS = $(SRCS:.F=.o)` (82). 구분 주석(84), 목록 사이와 끝 빈 줄(74·79·81·83·85–87)을 포함한다. |
| 88–100 | 링크(link) 대상은 `$(EXEC):	$(OBJS)` (91). 실행 명령은 `$(FC) $(FFLAGS) $(LDFLAGS) -o $(EXEC) $(OBJS) $(LIBS)` (92). 이어 `mkdir -p ../bin` (93)으로 `../bin`을 만들고 `mv $(EXEC) ../bin/` (94)로 실행 파일을 옮긴다. 링크·아카이브(archive) 안내 주석(88–89·95·97–99), 빈 줄(90·96·100)을 포함한다. |
| 101–112 | `tarfile:` (101) 대상의 실행 명령은 `tar cvf funwave_tvd.tar *.F  Makefile` (102). 정리 구분·설명 주석(104–106)과 빈 줄(103·107) 뒤 `clean:` (108)는 `/bin/rm -f *.o *.mod *.f90` (109)를 실행한다. `clobber:	clean` (111)는 `clean`을 선행 조건으로 두고 `/bin/rm -f *.f90 *.o $(EXEC)` (112)를 실행한다. 대상 사이 빈 줄(110)을 포함한다. 명령은 판독만 했다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 12·31·40: 병렬 전처리 플래그는 `FLAG_2 = -DPARALLEL` (12)이다. 컴파일러 이름은 `FC       = ifort` (31)이다. MPI 라이브러리 설정은 `MPILIB = -lmpi` (40)이다.
- 3·30·44: `CPPFLAGS`는 `$(DEF_FLAGS)`로 설정된다. `CPPARGS`는 `$(CPPFLAGS)`와 `$(DEF_FLAGS)`를 모두 참조한다.
- 91–94·111–112: 링크 대상은 `$(EXEC)`이며 링크 뒤 실행 파일을 `../bin/`으로 옮긴다. `clobber`의 삭제 명령은 현재 디렉터리의 `$(EXEC)`를 지정한다.
