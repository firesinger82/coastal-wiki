---
file: models/ROMS/raw/source_code/roms/ROMS/Utility/stdout_mod.F
lines: 134
sha256: 1b483578bf2d502c2ef28d1786845de776287539d116999f2838c485c55442c5
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# stdout_mod.F — 판독 구간 기록

구간은 1행부터 134행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–46 | `#include "cppdefs.h"` (1)로 cppdefs.h를 포함한다. stdout_mod 시작·저작권과 표준 출력 장치 및 파일 출력 설명(2–20). mod_parallel·mod_iounits·mod_scalars·FoundError 사용과 implicit none(22–28). stdout_unit 공개(30). 한 번만 설정한다는 주석(36–39)과 `logical, save :: Set_StdOutUnit = .TRUE.` (41). CONTAINS·구분 주석·빈 줄(43–46). |
| 47–84 | stdout_unit 함수 시작(47). MyMaster 입력·StdOutUnit 출력 설명과 선언(49–71). stdout_file 길이 10·오류 문자열 길이 256(73–74). 식별 문자열은 `character (len=*), parameter :: MyFile =                          &` (75), `&  __FILE__//", stdout_unit"` (76). SourceFile 복사와 장치 설정 주석(78–84). |
| 85–105 | 시작 시 47행 stdout_unit 안. `#ifdef ROMS_STDOUT` (85), `# if defined DISTRIBUTE && defined DISJOINTED` (92)에서는 `StdOutUnit=60+ForkColor` (93), WRITE로 log와 ForkColor+1의 두 자리 숫자 및 .roms를 결합한다(94). `# else` (95)는 `StdOutUnit=60` (96), `stdout_file='log.roms'` (97). `# endif` (98). 바깥 `#else` (99)는 `StdOutUnit=6` (103). `#endif` (104)·빈 줄(105). |
| 106–121 | 시작 시 47행 stdout_unit 안. `#ifdef ROMS_STDOUT` (106). 파일 열기 주석·io_err=0(108–112). `IF (Lappend) THEN` (113)은 formatted·old·append·write로 연다(114–116). `ELSE` (117)는 formatted·replace로 연다(118–120). 조건 종료(121). 두 OPEN 모두 IOSTAT·IOMSG를 받는다. |
| 122–134 | 시작 시 47행 stdout_unit·106행 `#ifdef ROMS_STDOUT` 안. `IF (io_err.ne.0) THEN` (122) 안에서 `IF (MyMaster) WRITE (StdOutUnit,10) TRIM(stdout_file),          &` (123), `&                                      TRIM(io_errmsg)` (124). exit_flag=5와 오류 출력 형식(125–127). `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (128). 조건 종료·`#endif` (130)·함수 및 모듈 종료(132–134). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 36–41·85–130: Set_StdOutUnit은 참으로 선언되지만 함수 본문에서 참조하거나 갱신하지 않는다. 함수의 OPEN 앞에는 이 스위치 검사가 없다.
- 113–123: OPEN은 MyMaster 조건 밖에 있다. MyMaster 조건은 열기 실패 메시지 출력에만 붙는다.
- 114–124: 파일 열기 실패 메시지의 WRITE 대상은 OPEN에 사용한 StdOutUnit과 같다.
