---
file: models/FUNWAVE/raw/source_code/FUNWAVE-TVD/Makefile
lines: 119
sha256: 290c32c85a8aea41063fdb9cd3112832eafcd09bbb217dd13b119a25d78a2cfa
reader: codex gpt-6.1-sol
read_date: 2026-10-17
---

# Makefile — 판독 구간 기록

구간은 1행부터 119행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | 시작 구분 주석(1). 작업 경로·컴파일러(compiler)·병렬 실행·실행 파일 이름·정밀도 기본 설정은 `FUNWAVE_DIR = .` (2), `WORK_DIR    = funwave-work` (3), `COMPILER    = intel` (4), `PARALLEL    = true` (5), `EXEC        = funwave` (6), `PRECISION   = single` (7). 끝 빈 줄(8). |
| 9–21 | 플래그 선택 안내는 `uncomment to choose the model`(10). 다음 플래그 줄은 모두 주석 처리되어 있다: `#  FLAG_1  = -DCOUPLING` (11), `# FLAG_2  = -DZALPHA` (12), `# FLAG_3  = -DMANNING` (13), `#  FLAG_4  = -DVESSEL` (14), `# FLAG_5  = -DMETEO` (15), `# FLAG_6  = -DWIND` (16), `# FLAG_7  = -DSEDIMENT` (17), `# FLAG_8  = -DCHECK_MASS_CONSERVATION` (18), `# FLAG_9  = -DTMP` (19), `# FLAG_10 = -DTRACKING` (20), `#  FLAG_11 = -DDEEP_DRAFT_VESSEL` (21). 9행은 구분 주석. |
| 22–36 | 추가 설정 구분 주석(22). 사용자 지정 컴파일러와 빈 추가 옵션은 `DEF_FC      = mpif90` (23), `DEF_FC_FLAG =` (24). 좌표·MPI·디버그(debug) 설정은 `SPHERICAL   = false` (25), `MPI         = openmpi` (26), `DEBUG       = false` (27). 포함 경로와 링크 라이브러리 설정은 `INCS        = $(IOINCS) $(GOTMINCS)` (28), `LIBS        = $(PV3LIB) $(CLIB)  $(PARLIB) $(IOLIBS) $(MPILIB) $(GOTMLIB)` (29), `CLIB        =` (30). 의존성 도구 옵션과 인덱스 도구는 `MDEPFLAGS   = --cpp --fext=f90 --file=-` (31), `RANLIB      = ranlib` (32). 빈 줄·포함 안내 주석을 거쳐 `include $(FUNWAVE_DIR)/GNUMake/Essential/Make_Essential` (35)로 공통 빌드 규칙을 포함한다. 끝 빈 줄(36). |
| 37–55 | 설명 머리말·빈 줄(37–41). 다음은 실행한 명령이 아니라 사용법 주석이다. `# make:` (42)는 작업 디렉터리와 실행 파일 생성, `# make clean:` (44)는 작업 디렉터리 아래 `build` 정리, `# make clean-exe:` (46)는 `build`와 실행 파일 정리, `# make clobber:` (48)는 작업 디렉터리 전체 정리를 설명한다. `# make chec-env:` (50)는 컴파일러·MPI 버전 출력, `# make print-foo` (52)는 변수 값 출력을 설명한다. 예시 주석은 `#      For example, "make print $(EXEC)" and you will see the final $(EXEC) name` (54). 각 설명 사이 줄과 끝 빈 줄을 포함한다. |
| 56–72 | 변수 설명 주석. `FUNWAVE_DIR`은 절대·상대 경로를 받으며 현재 디렉터리 예시는 `#      To set to current directory, set      FUNWAVE_DIR = .` (59). `WORK_DIR`은 새 작업 디렉터리를 설명하지만 현재 디렉터리 예시에도 `#      To set to current directory, set      FUNWAVE_DIR = .` (62)를 적는다. 지원 컴파일러는 `#      Support list: "gnu", "intel"` (64). 병렬 실행 값은 `#      eithrt "true" or "false"` (66). 실행 이름·접미사는 `#      The name for exectutable. By default, the name of the executable will be "funwave+$(SUFFIX)".` (68), `#      SUFFIX is a self-explainary string depending on the options above` (69). 정밀도 키워드는 원문의 `PRESICION`(70)이며 값 설명은 `#      either "single" or "double"` (71). 구분·빈 주석(56·72)을 포함한다. |
| 73–89 | 사용자 지정 컴파일러 설명 주석(73–78). 빈 값에 대한 설명은 `#      Left for empty for dafault.` (75), `#      Left for empty for dafault.` (78)이며 추가 옵션 설명의 변수 표기는 `#      User Defined comiler flags for $(DEF_FFC)` (77). 좌표 설명 키워드는 `SPHIRICAL`(79)이고 값 설명은 `#      "true" or "false". set to "true" to enable SPHERICAL coordinate.` (80). MPI 선택 규칙을 설명하는 주석은 `#      if PARALLEL=true, MPI=openmpi or MPImpich, FC = mpif90 (For any COMPILER)` (83), `#      if PARALLEL=true, COMPILER=intel, MPI=intelmpi, FC = mpiifort` (84). 디버그 값·옵션·최적화 옵션에 관한 주석은 `#      either "true" or "false"` (86), `#      If "true" uses some debug flags, for example -Wall for gnu compiler` (87), `#      If "false", no debug flags used. Use optimization flag (-O2 for intel, -O3 for gnu)` (88). 이 구간은 설정 분기가 아닌 주석이며 끝 빈 줄(89)을 포함한다. |
| 90–100 | 예전 사용법의 버전 표기는 `## To use like the 3.3 or earlier version of FUNWAVE-TVD` (90). `src`로 이동하여 두 경로를 `.`으로 설정한다는 주석(91)이 있다. `vessel case` 예시 주석은 아래의 모든 줄에서 주석을 해제하라고 안내한다: `# Here is an example for vessel case (uncomment all below). and you will see` (92). 아래 설정은 전부 주석이다: `# FUNWAVE_DIR = .` (94), `# WORK_DIR    = .` (95), `# COMPILER    = gnu` (96), `# PARALLEL    = true` (97), `# EXEC        = funwave` (98), `# PRECISION   = double` (99). 예시 시작 구분 주석(93)과 끝 빈 줄(100)을 포함한다. [10-17 전수 검증 보완] |
| 101–119 | 앞 구간에서 시작한 예시의 나머지이며 조건·루프 안은 아니다. 플래그 설정은 모두 주석 처리되어 있다: `# # FLAG_1  = -DCOUPLING` (103), `# # FLAG_2  = -DZALPHA` (104), `# # FLAG_3  = -DMANNING` (105), `# # FLAG_4  = -DVESSEL` (106), `# # FLAG_5  = -DMETEO` (107), `# # FLAG_6  = -DWIND` (108), `# # FLAG_7  = -DSEDIMENT` (109), `# FLAG_8  = -DCHECK_MASS_CONSERVATION` (110), `# # FLAG_9  = -DTMP` (111), `# # FLAG_10 = -DTRACKING` (112). 추가 옵션도 주석이다: `# SPHERICAL = false` (115), `# MPI       = openmpi` (116), `# DEBUG     = false` (117), `# MDEPFLAGS = --cpp --fext=f90 --file=-` (118), `# RANLIB = ranlib` (119). 안내·구분 주석(101–102·114)과 빈 줄(113)을 포함한다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 60–62: `WORK_DIR` 설명 아래 현재 디렉터리 설정 예시는 `FUNWAVE_DIR = .`로 적혀 있다.
- 92·106·110: 주석은 이 블록을 `vessel case` 예시로 소개한다. 선박 플래그 줄은 `# # FLAG_4  = -DVESSEL` (106)로 이중 주석이며 질량 보존 확인 플래그 줄은 `# FLAG_8  = -DCHECK_MASS_CONSERVATION` (110)로 단일 주석이다.
