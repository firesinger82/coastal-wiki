---
file: models/FUNWAVE/raw/source_code/FUNWAVE-TVD/GNUMake/Old_Version_Makefiles/Makefile-Lightning-Cray
lines: 105
sha256: 4dfb48d3591d842a5e11de6ec19e7c23a1c63b9596aba85f6b102c052f895710
reader: codex gpt-6.1-sol
read_date: 2026-10-17
---

# Makefile-Lightning-Cray — 판독 구간 기록

구간은 1행부터 105행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | 시작 구분 주석(1). 셸(shell)·전처리 기본 옵션·실행 이름은 `SHELL         = /bin/sh` (2), `DEF_FLAGS     = -P -traditional` (3), `EXEC          = funwave_cray` (4). 정밀도(precision) 안내는 주석 `#        PRECISION          DEFAULT PRECISION: SINGLE` (7), `#                           UNCOMMENT TO SELECT DOUBLE PRECISION` (8). 구분 주석(5–6·9)과 빈 줄(10)을 포함한다. |
| 11–21 | 활성 전처리 플래그(preprocessor flag)는 `FLAG_1 = -DDOUBLE_PRECISION` (11), `FLAG_2 = -DPARALLEL` (12), `FLAG_3 = -DSAMPLES` (13), `FLAG_4 = -DCARTESIAN` (14), `FLAG_5 = -DCRAY` (15). 다음 플래그 설정은 모두 주석이다: `#              FLAG_6 = -DINTEL` (16), `#             FLAG_7 = -DMIXING` (17), `#             FLAG_8 = -DCOUPLING` (18), `#             FLAG_9 = -DZALPHA` (19), `#             FLAG_10 = -DMANNING` (20). 끝 빈 줄(21). 조건 분기는 없다. |
| 22–36 | MPI 설정 안내 주석(22–24). 전처리기·컴파일러 설정은 `CPP      = /usr/bin/cpp` (25), `CPPFLAGS = $(DEF_FLAGS)` (26), `FC       = ftn` (27). 디버그(debug)·최적화·C 라이브러리 값은 빈 설정 `DEBFLGS  =` (28), `OPT      =` (29), `CLIB     =` (30). 컴파일 옵션 구성식은 `FFLAGS = $(DEBFLGS) $(OPT) #-fPIC -g -O2` (33)이며 줄 끝 `#-fPIC -g -O2`는 주석이다. 의존성 옵션·인덱스 도구는 `MDEPFLAGS = --cpp --fext=f90 --file=-` (34), `RANLIB = ranlib` (35). MPI 링크 설정은 `MPILIB = # -lmpi` (36)이며 `-lmpi`는 줄 끝 주석이다. 구분 주석·빈 줄(31–32)을 포함한다. |
| 37–54 | 전처리 인수 연결식은 `CPPARGS = $(CPPFLAGS) $(DEF_FLAGS) $(FLAG_1) $(FLAG_2) \` (40), `$(FLAG_3) $(FLAG_4) $(FLAG_5) $(FLAG_6) \` (41), `$(FLAG_7) $(FLAG_8) $(FLAG_9) $(FLAG_10)  \` (42), `$(FLAG_11) $(FLAG_12) $(FLAG_13) $(FLAG_14) \` (43), `$(FLAG_15) $(FLAG_16) $(FLAG_17) $(FLAG_18) \` (44), `$(FLAG_19) $(FLAG_20) $(FLAG_21) $(FLAG_22) \` (45), `$(FLAG_23) $(FLAG_24)` (46). 라이브러리 구성식은 `LIBS  = $(PV3LIB) $(CLIB)  $(PARLIB) $(IOLIBS) $(MPILIB) $(GOTMLIB)` (51). 포함 경로 설정 `#            INCS  = $(IOINCS) $(GOTMINCS)` (52)는 주석이다. 전처리·라이브러리 안내 주석(37–39·47–49), 빈 줄(50·53–54)을 포함한다. |
| 55–67 | 접미사 규칙 선언은 `.SUFFIXES: .o .f90 .F .F90` (58). `.F.o:` (60) 규칙의 실행 명령은 `$(CPP) $(CPPARGS) $*.F > $*.f90` (61)와 `$(FC)  -c $(FFLAGS) $(INCS) $*.f90` (62)이며 전처리 뒤 컴파일한다. `#	\rm $*.f90` (63)는 중간 파일 삭제를 적은 주석이다. 전처리·컴파일 및 소스 목록 안내 주석(55–57·64–66), 빈 줄(59·67)을 포함한다. |
| 68–79 | 모듈 목록 원문은 `MODS  = mod_param.F	mod_global.F	mod_input.F mod_vessel.F  mod_bathy_correction.F \` (68), `mod_parallel_field_io.F mod_meteo.F` (69). 주요 소스 목록 원문은 `MAIN  = main.F bc.F fluxes.F init.F io.F tridiagnal.F       \` (71), `breaker.F derivatives.F dispersion.F etauv_solver.F \` (72), `sponge.F sources.F masks.F parallel.F statistics.F \` (73), `wavemaker.F mixing.F nesting.F misc.F samples.F\` (74). 소스 목록 결합식은 `SRCS = $(MODS)  $(MAIN)` (76). 오브젝트(object) 목록 변환식은 `OBJS = $(SRCS:.F=.o)` (78). 목록 사이와 끝 빈 줄(70·75·77·79)을 포함한다. |
| 80–92 | 링크(link) 대상은 `$(EXEC):	$(OBJS)` (84). 실행 명령은 `$(FC) $(FFLAGS) $(LDFLAGS) -o $(EXEC) $(OBJS) $(LIBS) -Bdynamic` (85)이며 `-Bdynamic`을 포함한다. 다음 명령은 `mv $(EXEC) ../bin/` (86)으로 실행 파일을 옮긴다. 링크·아카이브(archive) 안내 주석(80–82·87·89–91), 빈 줄(83·88·92)을 포함한다. |
| 93–105 | `tarfile:` (93) 대상의 실행 명령은 `tar cvf funwave_tvd.tar *.F  Makefile` (94). 정리 구분·설명 주석(96–98)과 빈 줄(95·99) 뒤 `clean:` (100)는 `/bin/rm -f *.o *.mod` (101)을 실행한다. `clobber:	clean` (103)는 `clean`을 선행 조건으로 두고 `/bin/rm -f *.f90 *.o $(EXEC)` (104)를 실행한다. 대상 사이·끝 빈 줄(102·105)을 포함한다. 명령은 판독만 했다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 7–11: 정밀도 안내 주석은 `DEFAULT PRECISION: SINGLE`이라고 적는다. 실제 활성 플래그는 `FLAG_1 = -DDOUBLE_PRECISION` (11)이다.
- 3·26·40: `CPPFLAGS`는 `$(DEF_FLAGS)`로 설정된다. `CPPARGS`는 `$(CPPFLAGS)`와 `$(DEF_FLAGS)`를 모두 참조한다.
- 84–86·103–104: 링크 대상은 `$(EXEC)`이며 링크 뒤 실행 파일을 `../bin/`으로 옮긴다. `clobber`의 삭제 명령은 현재 디렉터리의 `$(EXEC)`를 지정한다.
