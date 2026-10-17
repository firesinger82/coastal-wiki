---
file: models/FUNWAVE/raw/source_code/FUNWAVE-TVD/Makefile_mac_single
lines: 120
sha256: 5a8bd2207231f80dc4510556bf040441deb98451978be513dc590506b339a6d5
reader: codex gpt-6.1-sol
read_date: 2026-10-17
---

# Makefile_mac_single — 판독 구간 기록

구간은 1행부터 120행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | 시작 구분 주석(1). 작업 경로·컴파일러(compiler)·병렬 실행·실행 파일 이름·정밀도 기본 설정은 `FUNWAVE_DIR = .` (2), `WORK_DIR    = funwave-work` (3), `COMPILER    = gnu` (4), `PARALLEL    = false` (5), `EXEC        = funwave` (6), `PRECISION   = single` (7). 끝 빈 줄(8). |
| 9–22 | 플래그 선택 안내는 `uncomment to choose the model`(10). 활성 전처리 플래그(preprocessor flag)는 `FLAG_12 = -DDEBUG` (22). 다음 플래그 줄은 모두 주석 처리되어 있다: `#  FLAG_1  = -DCOUPLING` (11), `# FLAG_2  = -DZALPHA` (12), `# FLAG_3  = -DMANNING` (13), `#  FLAG_4  = -DVESSEL` (14), `# FLAG_5  = -DMETEO` (15), `# FLAG_6  = -DWIND` (16), `# FLAG_7  = -DSEDIMENT` (17), `# FLAG_8  = -DCHECK_MASS_CONSERVATION` (18), `# FLAG_9  = -DTMP` (19), `# FLAG_10 = -DTRACKING` (20), `#  FLAG_11 = -DDEEP_DRAFT_VESSEL` (21). 9행은 구분 주석. |
| 23–37 | 추가 설정 구분 주석(23). 사용자 지정 컴파일러와 빈 추가 옵션은 `DEF_FC      = gfortran` (24), `DEF_FC_FLAG =` (25). 좌표·MPI·디버그(debug) 설정은 `SPHERICAL   = false` (26), `MPI         = openmpi` (27), `DEBUG       = true` (28). 포함 경로와 링크 라이브러리 설정은 `INCS        = $(IOINCS) $(GOTMINCS)` (29), `LIBS        = $(PV3LIB) $(CLIB)  $(PARLIB) $(IOLIBS) $(MPILIB) $(GOTMLIB)` (30), `CLIB        =` (31). 의존성 도구 옵션과 인덱스 도구는 `MDEPFLAGS   = --cpp --fext=f90 --file=-` (32), `RANLIB      = ranlib` (33). 빈 줄·포함 안내 주석을 거쳐 `include $(FUNWAVE_DIR)/GNUMake/Essential/Make_Essential` (36)로 공통 빌드 규칙을 포함한다. 끝 빈 줄(37). |
| 38–56 | 설명 머리말·빈 줄(38–42). 다음은 실행한 명령이 아니라 사용법 주석이다. `# make:` (43)는 작업 디렉터리와 실행 파일 생성, `# make clean:` (45)는 작업 디렉터리 아래 `build` 정리, `# make clean-exe:` (47)는 `build`와 실행 파일 정리, `# make clobber:` (49)는 작업 디렉터리 전체 정리를 설명한다. `# make chec-env:` (51)는 컴파일러·MPI 버전 출력, `# make print-foo` (53)는 변수 값 출력을 설명한다. 예시 주석은 `#      For example, "make print $(EXEC)" and you will see the final $(EXEC) name` (55). 각 설명 사이 줄과 끝 빈 줄을 포함한다. |
| 57–73 | 변수 설명 주석. `FUNWAVE_DIR`은 절대·상대 경로를 받으며 현재 디렉터리 예시는 `#      To set to current directory, set      FUNWAVE_DIR = .` (60). `WORK_DIR`은 새 작업 디렉터리를 설명하지만 현재 디렉터리 예시에도 `#      To set to current directory, set      FUNWAVE_DIR = .` (63)를 적는다. 지원 컴파일러는 `#      Support list: "gnu", "intel"` (65). 병렬 실행 값은 `#      eithrt "true" or "false"` (67). 실행 이름·접미사는 `#      The name for exectutable. By default, the name of the executable will be "funwave+$(SUFFIX)".` (69), `#      SUFFIX is a self-explainary string depending on the options above` (70). 정밀도 키워드는 원문의 `PRESICION`(71)이며 값 설명은 `#      either "single" or "double"` (72). 구분·빈 주석(57·73)을 포함한다. |
| 74–90 | 사용자 지정 컴파일러 설명 주석(74–79). 빈 값에 대한 설명은 `#      Left for empty for dafault.` (76), `#      Left for empty for dafault.` (79)이며 추가 옵션 설명의 변수 표기는 `#      User Defined comiler flags for $(DEF_FFC)` (78). 좌표 설명 키워드는 `SPHIRICAL`(80)이고 값 설명은 `#      "true" or "false". set to "true" to enable SPHERICAL coordinate.` (81). MPI 선택 규칙을 설명하는 주석은 `#      if PARALLEL=true, MPI=openmpi or MPImpich, FC = mpif90 (For any COMPILER)` (84), `#      if PARALLEL=true, COMPILER=intel, MPI=intelmpi, FC = mpiifort` (85). 디버그 값·옵션·최적화 옵션에 관한 주석은 `#      either "true" or "false"` (87), `#      If "true" uses some debug flags, for example -Wall for gnu compiler` (88), `#      If "false", no debug flags used. Use optimization flag (-O2 for intel, -O3 for gnu)` (89). 이 구간은 설정 분기가 아닌 주석이며 끝 빈 줄(90)을 포함한다. |
| 91–101 | 예전 사용법의 버전 표기는 `## To use like the 3.3 or earlier version of FUNWAVE-TVD` (91). `src`로 이동하여 두 경로를 `.`으로 설정한다는 주석(92)이 있다. `vessel case` 예시 주석은 아래의 모든 줄에서 주석을 해제하라고 안내한다: `# Here is an example for vessel case (uncomment all below). and you will see` (93). 아래 설정은 전부 주석이다: `# FUNWAVE_DIR = .` (95), `# WORK_DIR    = .` (96), `# COMPILER    = gnu` (97), `# PARALLEL    = true` (98), `# EXEC        = funwave` (99), `# PRECISION   = double` (100). 예시 시작 구분 주석(94)과 끝 빈 줄(101)을 포함한다. [10-17 전수 검증 보완] |
| 102–120 | 앞 구간에서 시작한 예시의 나머지이며 조건·루프 안은 아니다. 플래그 설정은 모두 주석 처리되어 있다: `# # FLAG_1  = -DCOUPLING` (104), `# # FLAG_2  = -DZALPHA` (105), `# # FLAG_3  = -DMANNING` (106), `# # FLAG_4  = -DVESSEL` (107), `# # FLAG_5  = -DMETEO` (108), `# # FLAG_6  = -DWIND` (109), `# # FLAG_7  = -DSEDIMENT` (110), `# FLAG_8  = -DCHECK_MASS_CONSERVATION` (111), `# # FLAG_9  = -DTMP` (112), `# # FLAG_10 = -DTRACKING` (113). 추가 옵션도 주석이다: `# SPHERICAL = false` (116), `# MPI       = openmpi` (117), `# DEBUG     = false` (118), `# MDEPFLAGS = --cpp --fext=f90 --file=-` (119), `# RANLIB = ranlib` (120). 안내·구분 주석(102–103·115)과 빈 줄(114)을 포함한다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 61–63: `WORK_DIR` 설명 아래 현재 디렉터리 설정 예시는 `FUNWAVE_DIR = .`로 적혀 있다.
- 93·107·111: 주석은 이 블록을 `vessel case` 예시로 소개한다. 선박 플래그 줄은 `# # FLAG_4  = -DVESSEL` (107)로 이중 주석이며 질량 보존 확인 플래그 줄은 `# FLAG_8  = -DCHECK_MASS_CONSERVATION` (111)로 단일 주석이다.
