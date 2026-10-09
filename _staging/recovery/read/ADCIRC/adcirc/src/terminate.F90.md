---
file: models/ADCIRC/raw/source_code/adcirc/src/terminate.F90
lines: 98
sha256: ab1c53e001ba8f1b25587b1c772ae44d1ce32fdd6d0c273b60259b65b916f204
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# terminate.F90 — 판독 구간 기록

구간은 1행부터 98행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–28 | 저작권·LGPL v3 이상·무보증 머리말(1–19). 종료 모듈 머리말은 종료코드(exit code), 메시지 로깅(logging), MPI 종료 처리(finalization)로 ADCIRC 실행을 끝내는 목적을 적는다(20–28). |
| 29–52 | mod_terminate 시작·implicit none(29–30). 성공코드 0, 실패코드 1을 선언한다(32–33). 기본 private이며 terminate와 두 상수를 공개한다(35–37). contains와 terminate 설명은 실패 메시지·성공 INFO·선택 MPI 종료, exit 호출을 적는다(39–47). 선택 인수 기본값은 실패 종료 및 MPI 종료 true이며 message도 선택 인수라는 주석을 포함한다(49–52). 원문: `integer, parameter :: ADCIRC_EXIT_SUCCESS = 0 !< successful exit code` (32); `integer, parameter :: ADCIRC_EXIT_FAILURE = 1 !< failure exit code` (33). |
| 53–77 | terminate 입구(53). CMPI는 subdomainFatalError/msg_fini를 가져오며 로깅은 allMessage/INFO/ERROR를 사용한다(54–58). 선택 exit_code/do_finalize_mpi/message와 길이 256 scratchMessage를 선언한다(60–65). exit_code가 있으면 복사하고 else는 ADCIRC_EXIT_FAILURE다(67–71). do_finalize_mpi가 있으면 복사하고 else는 true다(73–77). 원문: `#ifdef CMPI` (54); `if (present(exit_code)) then` (67); `exit_code_local = ADCIRC_EXIT_FAILURE` (70); `if (present(do_finalize_mpi)) then` (73); `finalize_mpi = .true.` (76). |
| 78–89 | 시작 시 53행 terminate 안. exit_code_local이 성공코드와 다르면 선택 message를 ERROR로 allMessage에 전달한다(79–82). 코드 번호 문자열을 scratchMessage에 쓰고 ERROR로 출력한다(83–84). else인 성공 경로는 message가 있을 때만 INFO로 출력한다(85–88). 조건 종료까지 포함한다(89). 원문: `if (exit_code_local /= ADCIRC_EXIT_SUCCESS) then` (79); `if (present(message)) then` (80); `if (present(message)) then` (86). |
| 90–98 | 시작 시 53행 terminate 안. CMPI에서는 실패코드일 때 subdomainFatalError=true로 설정하고 msg_fini(finalize_mpi)를 호출한다(90–93). 전처리 밖에서 exit(exit_code_local)를 호출한다(94). 빈 줄·루틴·모듈 종료를 포함한다(95–98). 원문: `#ifdef CMPI` (90); `if (exit_code_local /= ADCIRC_EXIT_SUCCESS) subdomainFatalError = .true.` (91); `call msg_fini(finalize_mpi)` (92); `call exit(exit_code_local)` (94). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 32–33·67–71·79: 공개 종료 상수는 0/1이다. 제공된 exit_code는 범위 검사 없이 복사하며 성공 여부는 0과의 비교로 나눈다.
- 90–92: CMPI의 실패 경로는 subdomainFatalError를 true로 설정한다. 성공 경로에서 그 플래그를 false로 설정하는 문장은 이 루틴에 없다.
- 73–77·90–92: CMPI에서는 finalize_mpi 값과 관계없이 msg_fini(finalize_mpi)를 호출한다. MPI 종료 수행 여부의 실제 처리는 호출된 msg_fini 내부이며 이 파일에서 판독하지 않았다.

