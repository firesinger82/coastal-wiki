---
file: models/SWAN/raw/source_code/swan/bin/swanrun.bat
lines: 86
sha256: 6b856cbd39d404f07fff899fd77e9a8a07067dd313ad86dcbf55bb16f28dbf19
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# swanrun.bat — 판독 구간 기록

구간은 1행부터 86행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | 파일 안내 — Windows 배치 파일(batch file)은 SWAN 입력 파일로 프로그램을 실행한다고 설명한다(3–5). 입력 확장자는 `.swn`이라고 가정한다(6). 호출 예시는 선택적 프로세스 수(number of processes)를 포함한다(8). 주석과 빈 줄도 포함한다. 원문: `@echo off` (1); `rem    swanrun.bat` (3); `rem    Run the SWAN program by means of the SWAN input file` (5); `rem    Note: it is assumed that the extension of the input file is '.swn'` (6); `rem    Usage: swanrun inputfile [nprocs]` (8). |
| 11–30 | 기본값과 인수 검사 — `nprocs`를 1로 설정한다(11). 첫 인수가 없으면 사용법을 출력하고 END로 이동한다(13–17). 첫 인수를 `inputfile`에 넣고 SHIFT한 뒤 `.swn` 파일 존재를 검사한다(19–26). SHIFT 후 인수가 있으면 `nprocs`를 그 값으로 바꾼다(28–30). 원문: `set nprocs=1` (11); `if not "%1"=="" goto OK1` (13); `  echo.` (14); `  echo Usage: swanrun inputfile [nprocs]` (15); `  goto END` (16); `:OK1` (17); `set inputfile=%1` (19); `shift` (20); `if exist %inputfile%.swn goto OK2` (22); `  echo.` (23); `  echo Error: file %inputfile%.swn does not exist` (24); `  goto END` (25); `:OK2` (26); `if "%1"=="" goto OK3` (28); `  set nprocs=%1` (29); `:OK3` (30). |
| 31–43 | 입력 복사와 실행 — 원문은 입력 파일을 `INPUT`으로 복사한다(32). `nprocs`가 1이면 `swan.exe`, 1이 아니면 `mpiexec`로 실행한다(34–39). 실행 뒤 `errorlevel`이 1 이상이면 END로 이동한다(42). 복사와 실행 구문을 원문 그대로 옮긴다. 원문: `copy %inputfile%.swn INPUT >> nul` (32); `if not %nprocs%==1 goto PARALLEL1` (34); `swan.exe` (35); `goto OK4` (36); `:PARALLEL1` (38); `mpiexec -n %nprocs% swan.exe` (39); `:OK4` (41); `if errorlevel 1 goto END` (42). |
| 44–60 | PRINT 출력 정리 / 1자리·2자리 번호 — 단일 프로세스일 때 존재하는 PRINT를 `.prt`로 복사하고 삭제한다(44–47). 병렬 분기는 PRINT-001이 없으면 OK5로 이동한다(48–49). 이후 `GTR 9`, `GTR 99` 조건에 따라 PRINT-00번호와 PRINT-0번호를 복사·삭제한다(50–60). 원문: `if not %nprocs%==1 goto PARALLEL2` (44); `  if exist PRINT copy PRINT %inputfile%.prt >> nul` (45); `  if exist PRINT del PRINT` (46); `  goto OK5` (47); `:PARALLEL2` (48); `if not exist PRINT-001 goto OK5` (49); `if %nprocs% GTR 9 goto RANGE1` (50); `  for /L %%i in (1,1,%nprocs%) do copy PRINT-00%%i %inputfile%.prt-00%%i >> nul` (51); `  for /L %%i in (1,1,%nprocs%) do del PRINT-00%%i` (52); `  goto OK5` (53); `:RANGE1` (54); `if %nprocs% GTR 99 goto RANGE2` (55); `  for /L %%i in (1,1,9) do copy PRINT-00%%i %inputfile%.prt-00%%i >> nul` (56); `  for /L %%i in (1,1,9) do del PRINT-00%%i` (57); `  for /L %%i in (10,1,%nprocs%) do copy PRINT-0%%i %inputfile%.prt-0%%i >> nul` (58); `  for /L %%i in (10,1,%nprocs%) do del PRINT-0%%i` (59); `  goto OK5` (60). |
| 61–73 | PRINT 출력 정리 / 3자리 번호와 오류 — `GTR 999`이면 ERR로 이동한다(62). 그 밖에는 1–9, 10–99, 100–nprocs에 각각 다른 자릿수의 파일명을 사용해 복사·삭제한다(63–69). ERR는 프로세스가 너무 많다는 메시지를 출력한 뒤 END로 이동한다(70–72). 원문: `:RANGE2` (61); `if %nprocs% GTR 999 goto ERR` (62); `  for /L %%i in (1,1,9) do copy PRINT-00%%i %inputfile%.prt-00%%i >> nul` (63); `  for /L %%i in (1,1,9) do del PRINT-00%%i` (64); `  for /L %%i in (10,1,99) do copy PRINT-0%%i %inputfile%.prt-0%%i >> nul` (65); `  for /L %%i in (10,1,99) do del PRINT-0%%i` (66); `  for /L %%i in (100,1,%nprocs%) do copy PRINT-%%i %inputfile%.prt-%%i >> nul` (67); `  for /L %%i in (100,1,%nprocs%) do del PRINT-%%i` (68); `  goto OK5` (69); `:ERR` (70); `  echo Error: too many processes` (71); `  goto END` (72); `:OK5` (73). |
| 74–86 | 오류 파일과 종료 — Errfile과 ERRPTS가 존재하면 각각 `.erf`, `.erp`로 복사하고 삭제한다(75–78). INPUT을 삭제한다(79). norm_end가 없으면 END로 이동하고, 있으면 내용을 출력한다(80–81). END에서 두 환경 변수(environment variable)를 비운다(83–86). 원문: `if exist Errfile copy Errfile %inputfile%.erf >> nul` (75); `if exist Errfile del Errfile` (76); `if exist ERRPTS copy ERRPTS %inputfile%.erp >> nul` (77); `if exist ERRPTS del ERRPTS` (78); `del INPUT` (79); `if not exist norm_end goto END` (80); `  type norm_end` (81); `:END` (83); `set inputfile=` (85); `set nprocs=` (86). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 34–39·62행: `nprocs GTR 999` 검사는 SWAN 실행 뒤 PRINT 출력 정리 분기에 있다. 실행 전 인수 검사에는 프로세스 수의 상한 검사가 없다(11–30).
- 42·75–79·85–86행: `if errorlevel 1 goto END` 분기는 오류 파일 복사·삭제와 INPUT 삭제를 건너뛴다. END는 `inputfile`과 `nprocs`만 비운다.
