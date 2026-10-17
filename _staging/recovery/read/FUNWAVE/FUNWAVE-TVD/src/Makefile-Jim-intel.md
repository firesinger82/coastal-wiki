---
file: models/FUNWAVE/raw/source_code/FUNWAVE-TVD/src/Makefile-Jim-intel
lines: 111
sha256: 5aca9f12769060a12442fb66f6fe633bc12b01864b9b1f6dadd216b261a6f342
reader: codex gpt-6.1-sol
read_date: 2026-10-17
---

# Makefile-Jim-intel — 판독 구간 기록

구간은 1행부터 111행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | 시작 구분 주석(1). 셸(shell)·전처리 기본 옵션·실행 이름은 `SHELL         = /bin/sh` (2), `DEF_FLAGS     = -P -traditional` (3), `EXEC          = funwave_intel` (4). 정밀도(precision) 안내는 주석 `#        PRECISION          DEFAULT PRECISION: SINGLE` (7), `#                           UNCOMMENT TO SELECT DOUBLE PRECISION` (8). 구분 주석(5–6·9)과 빈 줄(10)을 포함한다. |
| 11–27 | 활성 전처리 플래그(preprocessor flag)는 `FLAG_1 = -DDOUBLE_PRECISION` (11), `FLAG_2 = -DPARALLEL` (12), `FLAG_3 = -DSAMPLES` (13), `FLAG_4 = -DCARTESIAN` (14), `FLAG_6 = -DINTEL` (16). 다음 플래그 설정은 모두 주석이다: `#	    FLAG_5 = -DMETEO` (15), `#             FLAG_7 = -DMIXING` (17), `#             FLAG_8 = -DCOUPLING` (18), `#             FLAG_9 = -DZALPHA` (19), `#             FLAG_10 = -DMANNING` (20), `#	      FLAG_11 = -DSEDIMENT` (21), `#	      FLAG_12 = -DVESSEL` (22), `#	      FLAG_13 = -DWIND` (23), `#	      FLAG_14 = -DTMP` (24), `#	      FLAG_15 = -DTRACKING` (25), `#	      FLAG_16 = -DDEEP_DRAFT_VESSEL` (26). 끝 빈 줄(27). 조건 분기는 없다. |
| 28–42 | MPI 설정 구분·안내 주석(28–30). 전처리기·컴파일러 설정은 `CPP      = /usr/bin/cpp` (31), `CPPFLAGS = $(DEF_FLAGS)` (32), `FC       = mpiifort` (33). 디버그(debug)·최적화·C 라이브러리 값은 빈 설정 `DEBFLGS  =` (34), `OPT      =` (35), `CLIB     =` (36). 컴파일 옵션 구성식은 `FFLAGS = $(DEBFLGS) $(OPT) #-fPIC -g -O2` (39)이며 줄 끝 `#-fPIC -g -O2`는 주석이다. 의존성 옵션·인덱스 도구·MPI 링크 설정은 `MDEPFLAGS = --cpp --fext=f90 --file=-` (40), `RANLIB = ranlib` (41), `MPILIB = # -lmpi` (42). 구분 주석·빈 줄(37–38)을 포함한다. 42행은 `MPILIB`를 빈 값으로 두며 `-lmpi`를 줄 끝 주석으로 적는다. |
| 43–60 | 전처리 인수 연결식은 `CPPARGS = $(CPPFLAGS) $(DEF_FLAGS) $(FLAG_1) $(FLAG_2) \` (46), `$(FLAG_3) $(FLAG_4) $(FLAG_5) $(FLAG_6) \` (47), `$(FLAG_7) $(FLAG_8) $(FLAG_9) $(FLAG_10)  \` (48), `$(FLAG_11) $(FLAG_12) $(FLAG_13) $(FLAG_14) \` (49), `$(FLAG_15) $(FLAG_16) $(FLAG_17) $(FLAG_18) \` (50), `$(FLAG_19) $(FLAG_20) $(FLAG_21) $(FLAG_22) \` (51), `$(FLAG_23) $(FLAG_24)` (52). 라이브러리 구성식은 `LIBS  = $(PV3LIB) $(CLIB)  $(PARLIB) $(IOLIBS) $(MPILIB) $(GOTMLIB)` (57). 포함 경로 설정 `#            INCS  = $(IOINCS) $(GOTMINCS)` (58)는 주석이다. 전처리·라이브러리 안내 및 구분 주석(43–45·53–55), 빈 줄(56·59–60)을 포함한다. |
| 61–73 | 접미사 규칙 선언은 `.SUFFIXES: .o .f90 .F .F90` (64). `.F.o:` (66) 규칙은 `$(CPP) $(CPPARGS) $*.F > $*.f90` (67)로 전처리 파일을 만들고 `$(FC)  -c $(FFLAGS) $(INCS) $*.f90` (68)로 컴파일한다. `#	\rm $*.f90` (69)는 중간 파일 삭제를 적은 주석이며 실행 명령이 아니다. 전처리·컴파일 및 소스 목록 안내 주석(61–63·70–72), 빈 줄(65·73)을 포함한다. |
| 74–86 | 모듈 목록 원문은 `MODS  = mod_param.F	mod_global.F	mod_input.F mod_vessel.F  mod_bathy_correction.F \` (74), `mod_parallel_field_io.F mod_meteo.F mod_sediment.F mod_tide.F mod_tracer.F` (75). 주요 소스 목록 원문은 `MAIN  = main.F bc.F fluxes.F init.F io.F tridiagnal.F       \` (77), `breaker.F derivatives.F dispersion.F etauv_solver.F \` (78), `sponge.F sources.F masks.F parallel.F statistics.F \` (79), `wavemaker.F mixing.F nesting.F misc.F samples.F \` (80). 소스 목록 결합식은 `SRCS = $(MODS)  $(MAIN)` (83). 오브젝트(object) 목록 변환식은 `OBJS = $(SRCS:.F=.o)` (85). 목록 사이·끝 빈 줄과 공백 줄(76·81–82·84·86)을 포함한다. |
| 87–99 | 링크(link) 대상은 `$(EXEC):	$(OBJS)` (91). 실행 명령은 `$(FC) $(FFLAGS) $(LDFLAGS) -o $(EXEC) $(OBJS) $(LIBS) -Bdynamic` (92)이며 `-Bdynamic`을 포함한다. 다음 명령은 `mv $(EXEC) ../bin/` (93)으로 실행 파일을 옮긴다. 링크·아카이브(archive) 안내 주석(87–89·94·96–98), 빈 줄(90·95·99)을 포함한다. |
| 100–111 | `tarfile:` (100) 대상의 실행 명령은 `tar cvf funwave_tvd.tar *.F  Makefile` (101). 정리 구분·설명 주석(103–105)과 빈 줄(102·106) 뒤 `clean:` (107)는 `/bin/rm -f *.o *.mod` (108)을 실행한다. `clobber:	clean` (110)는 `clean`을 선행 조건으로 두고 `/bin/rm -f *.f90 *.o $(EXEC)` (111)을 실행한다. 대상 사이 빈 줄(109)을 포함한다. 이 파일의 명령은 판독만 했다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 7–11: 정밀도 안내 주석은 `DEFAULT PRECISION: SINGLE`이라고 적는다. 실제 활성 플래그는 `FLAG_1 = -DDOUBLE_PRECISION` (11)이다.
- 3·32·46: `CPPFLAGS`는 `$(DEF_FLAGS)`로 설정된다. `CPPARGS`는 `$(CPPFLAGS)`와 `$(DEF_FLAGS)`를 모두 참조한다.
- 91–93·110–111: 링크 대상은 `$(EXEC)`이며 링크 뒤 실행 파일을 `../bin/`으로 옮긴다. `clobber`의 삭제 명령은 현재 디렉터리의 `$(EXEC)`를 지정한다.
