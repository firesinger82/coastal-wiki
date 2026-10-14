---
file: models/SWASH/raw/source_code/swash/bin/swashrun.bat
lines: 86
sha256: 406c0026f9a4456af72cb3b269a9d491f5ee3b59da5fb999f6ed985dc8e072c3
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# swashrun.bat — 판독 구간 기록

구간은 1행부터 86행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 명령 표시 억제 명령은 `@echo off` (1)이다. `rem` 머리말은 SWASH 입력 파일을 이용해 실행한다고 적는다(2–5). 입력 확장자 가정은 `'.sws'`이다(6). 사용법 주석은 `swashrun inputfile [nprocs]`이다(8). 기본 프로세스(process) 수 설정은 `set nprocs=1` (11)이다. 나머지 `rem` 줄과 빈 줄을 포함한다(7·9–10·12). |
| 13–30 | 첫 인수 검사 명령은 `if not "%1"=="" goto OK1` (13)이다. 인수가 없으면 `  echo.` (14), `  echo Usage: swashrun inputfile [nprocs]` (15), `  goto END` (16)을 실행한다. 인수가 있으면 표지(label) `:OK1` (17)로 이동한다. 입력 이름 설정과 인수 이동 명령은 `set inputfile=%1` (19)와 `shift` (20)이다. 파일 존재 검사 명령은 `if exist %inputfile%.sws goto OK2` (22)이다. 파일이 없으면 `  echo.` (23), `  echo Error: file %inputfile%.sws does not exist` (24), `  goto END` (25)를 실행한다. 파일이 있으면 표지 `:OK2` (26)로 이동한다. 프로세스 수 인수 검사 명령은 `if "%1"=="" goto OK3` (28)이다. 인수가 있으면 `  set nprocs=%1` (29)로 기본값을 대체한다. 표지 `:OK3` (30)에서 실행 준비로 이어진다. 빈 줄을 포함한다(18·21·27). |
| 31–43 | 입력 복사 명령은 `copy %inputfile%.sws INPUT >> nul` (32)이다. 실행 분기 명령은 `if not %nprocs%==1 goto PARALLEL1` (34)이다. `nprocs`가 1이면 `swash.exe` (35)로 직렬 실행한 뒤 `goto OK4` (36)으로 이동한다. 다른 값이면 표지 `:PARALLEL1` (38)에서 `mpiexec -n %nprocs% swash.exe` (39)로 병렬 실행한다. 합류 표지는 `:OK4` (41)이다. 실행 후 오류 검사 명령은 `if errorlevel 1 goto END` (42)이다. 오류 수준(error level)이 1 이상이면 `END`로 이동한다(42). 빈 줄을 포함한다(31·33·37·40·43). |
| 44–53 | 시작 시 41행 `:OK4` 실행 경로이며 42행 오류 종료 검사를 지난 상태이다. 출력 처리 분기 명령은 `if not %nprocs%==1 goto PARALLEL2` (44)이다. 직렬 경로는 `  if exist PRINT copy PRINT %inputfile%.prt >> nul` (45)와 `  if exist PRINT del PRINT` (46)으로 `PRINT`를 복사·삭제한 뒤 `  goto OK5` (47)로 이동한다. 병렬 경로 표지는 `:PARALLEL2` (48)이다. 첫 병렬 출력 존재 검사 명령은 `if not exist PRINT-001 goto OK5` (49)이다. 프로세스 수 자릿수 분기 명령은 `if %nprocs% GTR 9 goto RANGE1` (50)이다. 9 이하 경로의 반복 명령은 `  for /L %%i in (1,1,%nprocs%) do copy PRINT-00%%i %inputfile%.prt-00%%i >> nul` (51)과 `  for /L %%i in (1,1,%nprocs%) do del PRINT-00%%i` (52)이다. 이 경로는 `PRINT-00%%i`를 복사·삭제한다(51–52). 다음 이동 명령은 `  goto OK5` (53)이다. |
| 54–60 | 시작 시 50행 `if %nprocs% GTR 9 goto RANGE1`을 통해 이동한 경로이다. 표지는 `:RANGE1` (54)이다. 다음 자릿수 분기 명령은 `if %nprocs% GTR 99 goto RANGE2` (55)이다. 99 이하 경로는 `  for /L %%i in (1,1,9) do copy PRINT-00%%i %inputfile%.prt-00%%i >> nul` (56)과 `  for /L %%i in (1,1,9) do del PRINT-00%%i` (57)로 1부터 9까지 복사·삭제한다. 이어 `  for /L %%i in (10,1,%nprocs%) do copy PRINT-0%%i %inputfile%.prt-0%%i >> nul` (58)과 `  for /L %%i in (10,1,%nprocs%) do del PRINT-0%%i` (59)로 10부터 `%nprocs%`까지 복사·삭제한다. 첫 반복은 `PRINT-00%%i`를 사용하고 두 번째 반복은 `PRINT-0%%i`를 사용한다(56–59). 다음 이동 명령은 `  goto OK5` (60)이다. |
| 61–72 | 시작 시 55행 `if %nprocs% GTR 99 goto RANGE2`를 통해 이동한 경로이다. 표지는 `:RANGE2` (61)이다. 상한 분기 명령은 `if %nprocs% GTR 999 goto ERR` (62)이다. 999 이하 경로는 `  for /L %%i in (1,1,9) do copy PRINT-00%%i %inputfile%.prt-00%%i >> nul` (63)과 `  for /L %%i in (1,1,9) do del PRINT-00%%i` (64)로 1부터 9까지 복사·삭제한다. 이어 `  for /L %%i in (10,1,99) do copy PRINT-0%%i %inputfile%.prt-0%%i >> nul` (65)와 `  for /L %%i in (10,1,99) do del PRINT-0%%i` (66)으로 10부터 99까지 복사·삭제한다. 마지막 반복은 `  for /L %%i in (100,1,%nprocs%) do copy PRINT-%%i %inputfile%.prt-%%i >> nul` (67)과 `  for /L %%i in (100,1,%nprocs%) do del PRINT-%%i` (68)로 100부터 `%nprocs%`까지 복사·삭제한다. 이 반복은 `PRINT-%%i`를 사용한다(67–68). 정상 이동 명령은 `  goto OK5` (69)이다. 초과 경로 표지는 `:ERR` (70)이며 `  echo Error: too many processes` (71)과 `  goto END` (72)로 오류 메시지를 출력하고 종료 경로로 이동한다. |
| 73–86 | 출력 처리 합류 표지는 `:OK5` (73)이다. 오류 파일 처리 명령은 `if exist Errfile copy Errfile %inputfile%.erf >> nul` (75), `if exist Errfile del Errfile` (76), `if exist ERRPTS copy ERRPTS %inputfile%.erp >> nul` (77), `if exist ERRPTS del ERRPTS` (78)이다. 이 명령들은 존재하는 `Errfile`을 `.erf`로, `ERRPTS`를 `.erp`로 복사한 뒤 각각 원본을 삭제한다(75–78). 입력 정리 명령은 `del INPUT` (79)이다. 종료 표지 파일 검사 명령은 `if not exist norm_end goto END` (80)이다. `norm_end`가 있으면 `  type norm_end` (81)로 내용을 출력한다. 종료 경로 표지는 `:END` (83)이다. 환경 변수 정리 명령은 `set inputfile=` (85)와 `set nprocs=` (86)이다. 빈 줄을 포함한다(74·82·84). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11·28–39: `nprocs` 기본값은 `1`이다. 선택 인수가 있으면 `set nprocs=%1`로 대체한다. 실행 명령 전에 숫자 형식이나 양수 범위를 검사하는 문장은 이 파일에 없다.
- 39·49–62: `nprocs`가 `999`보다 큰지 검사하는 문장은 병렬 실행 이후의 `PRINT` 처리 경로에 있다. `PRINT-001`이 없으면 49행에서 `OK5`로 이동하므로 이 상한 검사도 건너뛴다.
- 42·44–83: `if errorlevel 1 goto END`가 이동하는 종료 표지는 83행이다. 이 이동은 `PRINT` 처리, 오류 파일 복사·삭제, `del INPUT`, `norm_end` 출력을 건너뛴다.
- 80–86: `norm_end`는 존재 검사와 내용 출력에 사용된다. 이 파일에는 `norm_end`를 삭제하거나 초기화하는 명령이 없다.
