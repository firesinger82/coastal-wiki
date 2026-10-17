---
file: models/FUNWAVE/raw/source_code/FUNWAVE-TVD/GNUMake/Makefile
lines: 104
sha256: 0ebe5ff6291224ae0116ab270d9da59e6e1df9bcbacce4fbc81f864da90ef3d1
reader: codex gpt-6.1-sol
read_date: 2026-10-17
---

# Makefile — 판독 구간 기록

구간은 1행부터 104행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | 시작 구분 주석(1). 경로·컴파일러·병렬 실행·실행 이름·정밀도 기본 설정은 `FUNWAVE_DIR = ..` (2), `WORK_DIR    = .` (3), `COMPILER    = gnu` (4), `PARALLEL    = false` (5), `EXEC        = funwave` (6), `PRECISION   = double` (7). 끝 빈 줄(8). |
| 9–21 | 선택 안내 `uncomment to choose the model`(10). 전처리 플래그 설정은 모두 주석이다: `# FLAG_1  = -DCOUPLING` (11), `# FLAG_2  = -DZALPHA` (12), `# FLAG_3  = -DMANNING` (13), `# FLAG_4  = -DVESSEL` (14), `# FLAG_5  = -DMETEO` (15), `# FLAG_6  = -DWIND` (16), `# FLAG_7  = -DSEDIMENT` (17), `# FLAG_8  = -DCHECK_MASS_CONSERVATION` (18), `# FLAG_9  = -DTMP` (19), `# FLAG_10 = -DTRACKING` (20). 구분 주석(9)과 끝 빈 줄(21)을 포함한다. |
| 22–31 | 추가 옵션 설정은 `SPHERICAL = false` (23), `MPI       = openmpi` (24), `DEBUG     = false` (25), `MDEPFLAGS = --cpp --fext=f90 --file=-` (26), `RANLIB = ranlib` (27). 구분 주석·빈 줄(22·28–29)을 거쳐 `include $(FUNWAVE_DIR)/GNUMake/Essential/Make_Essential` (30)으로 공통 빌드 규칙을 포함한다. 끝 빈 줄(31). |
| 32–46 | 사용법은 전부 주석이다. `# make:` (33)는 작업 디렉터리·실행 파일 생성, `# make clean:` (35)는 `build` 정리, `# make clean-exe:` (37)는 `build`와 실행 파일 정리, `# make clobber:` (39)는 작업 디렉터리 전체 정리를 설명한다. `# make chec-env:` (41)는 컴파일러·MPI 버전 출력, `# make print-foo` (43)는 변수 값 출력을 설명한다. 예시 주석은 `#      For example, "make print $(EXEC)" and you will see the final $(EXEC) name` (45). 구분 주석(32)과 끝 빈 줄(46)을 포함한다. |
| 47–63 | 변수 설명 주석. `FUNWAVE_DIR`은 절대·상대 경로를 받으며 현재 디렉터리 예시는 `#      To set to current directory, set      FUNWAVE_DIR = .` (50). `WORK_DIR`은 새 작업 디렉터리라고 설명하지만 현재 디렉터리 예시에도 `#      To set to current directory, set      FUNWAVE_DIR = .` (53)를 적는다. 지원 컴파일러는 `#      Support list: "gnu", "intel"` (55), 병렬 값은 `#      eithrt "true" or "false"` (57), 실행 이름·접미사 설명은 `#      The name for exectutable. By default, the name of the executable will be "funwave+$(SUFFIX)".` (59), `#      SUFFIX is a self-explainary string depending on the options above` (60). 정밀도 키워드는 `PRESICION`(61), 값 설명은 `#      either "single" or "double"` (62). 구분·빈 주석(47·63)을 포함한다. |
| 64–74 | 좌표 설명 키워드는 `SPHIRICAL`(64), 값 설명은 `#      "true" or "false". set to "true" to enable SPHERICAL coordinate.` (65). MPI 선택 규칙 주석은 `#      if PARALLEL=true, MPI=openmpi or MPImpich, FC = mpif90 (For any COMPILER)` (68), `#      if PARALLEL=true, COMPILER=intel, MPI=intelmpi, FC = mpiifort` (69). 디버그 값·컴파일러 옵션·최적화 옵션 주석은 `#      either "true" or "false"` (71), `#      If "true" uses some debug flags, for example -Wall for gnu compiler` (72), `#      If "false", no debug flags used. Use optimization flag (-O2 for intel, -O3 for gnu)` (73). 끝 빈 줄(74). 이 구간에 실행 조건 분기는 없다. |
| 75–85 | 예전 사용법의 버전 표기는 `## To use like the 3.3 or earlier version of FUNWAVE-TVD` (75). `src`로 이동하여 `FUNWAVE_DIR=..`·`WORK_DIR=.`로 설정한다는 주석(76)과 `vessel case` 예시 안내(77)가 있다. 예시 설정은 전부 주석이다: `# FUNWAVE_DIR = ..` (79), `# WORK_DIR    = .` (80), `# COMPILER    = gnu` (81), `# PARALLEL    = true` (82), `# EXEC        = funwave` (83), `# PRECISION   = double` (84). 구분 주석(78)과 빈 줄(85)을 포함한다. |
| 86–104 | 앞 구간 예시의 나머지이며 조건·루프 안은 아니다. 플래그 줄은 모두 주석이다: `# # FLAG_1  = -DCOUPLING` (88), `# # FLAG_2  = -DZALPHA` (89), `# # FLAG_3  = -DMANNING` (90), `# # FLAG_4  = -DVESSEL` (91), `# # FLAG_5  = -DMETEO` (92), `# # FLAG_6  = -DWIND` (93), `# # FLAG_7  = -DSEDIMENT` (94), `# FLAG_8  = -DCHECK_MASS_CONSERVATION` (95), `# # FLAG_9  = -DTMP` (96), `# # FLAG_10 = -DTRACKING` (97). 추가 옵션도 주석이다: `# SPHERICAL = false` (100), `# MPI       = openmpi` (101), `# DEBUG     = false` (102), `# MDEPFLAGS = --cpp --fext=f90 --file=-` (103), `# RANLIB = ranlib` (104). 구분·안내 주석(86–87·99)과 빈 줄(98)을 포함한다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 51–53: `WORK_DIR` 설명 아래 현재 디렉터리 설정 예시는 `FUNWAVE_DIR = .`로 적혀 있다.
- 77·91·95: 주석은 예시를 `vessel case`라고 소개한다. 선박 플래그 줄은 `# # FLAG_4  = -DVESSEL` (91)로 이중 주석이며 질량 보존 확인 플래그 줄은 `# FLAG_8  = -DCHECK_MASS_CONSERVATION` (95)로 단일 주석이다.
