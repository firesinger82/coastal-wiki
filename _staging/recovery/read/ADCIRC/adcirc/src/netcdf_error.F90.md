---
file: models/ADCIRC/raw/source_code/adcirc/src/netcdf_error.F90
lines: 59
sha256: df70397995d6e4c9c16b4a37ab26d266b5af3e572d5c67edab282845e2896efd
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# netcdf_error.F90 — 판독 구간 기록

구간은 1행부터 59행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | 구분 주석·ADCIRC 저작권·LGPL 3 이상·무보증·라이선스 안내(1–19). |
| 20–33 | 전처리(preprocessing) 조건 `#ifdef ADCNETCDF` (20)에서 이하 모듈 전체를 포함한다. `#include "logging_macros.h"` (22)로 로깅 매크로(logging macro) 헤더를 포함한다. `module netcdf_error` (24)로 모듈(module)을 연다. implicit none을 둔다(26). 기본 접근은 private이다(28). 공개 항목은 check_err이다(30). contains와 빈 줄(32–33). |
| 34–49 | 시작 시 20행 ADCNETCDF 전처리 분기·24행 netcdf_error 모듈 안. 구분선·CHECK_ERR 제목·설명 주석(34–40). 주석은 netCDF 반환값에 오류가 있으면 화면과 fort.16 파일에 오류 메시지를 쓴다고 설명한다(37–39). check_err(iret)을 연다(41). netcdf에서 NF90_NOERR·nf90_strerror를 가져온다(42). mod_terminate에서 terminate·ADCIRC_EXIT_FAILURE를 가져온다(43). mod_logging에서 allMessage·t_log_scope·init_log_scope를 가져온다(44). implicit none과 입력 정수 iret 선언(45–46). 추적 매크로 호출은 `LOG_SCOPE_TRACED("check_err", NETCDF_TRACING)` (48)이다. 선언 사이와 끝의 빈 줄도 포함한다(47·49). |
| 50–59 | 시작 시 20행 ADCNETCDF 전처리 분기·24행 netcdf_error 모듈·41행 check_err 루틴 안. 오류 조건은 `if (iret /= NF90_NOERR) then` (50)이다. 이 참 분기의 호출 원문은 `call terminate(exit_code=ADCIRC_EXIT_FAILURE, &` (51); `message=nf90_strerror(iret))` (52)이다. terminate에는 ADCIRC_EXIT_FAILURE와 nf90_strerror(iret)의 결과를 넘긴다(51–52). iret가 NF90_NOERR와 같으면 이 호출을 실행하지 않는다(50–53). 오류 조건 종료(53). 구분선·루틴 종료·구분선·빈 줄(54–57). netcdf_error 모듈을 끝낸다(58). `#endif` (59)로 ADCNETCDF 전처리 분기를 끝낸다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 37–39·50–53: 오류 설명 주석은 화면과 fort.16 출력을 적는다(37–39). 이 파일의 오류 분기에는 직접 write 문 없이 terminate 호출만 있다(50–53). terminate 내부 출력은 이 판독 대상에 포함되지 않는다.
- 22·44·48: 가져온 allMessage·t_log_scope·init_log_scope는 use 문(44) 외에 이 파일에 명시적으로 등장하지 않는다. 로깅 실행부는 LOG_SCOPE_TRACED 매크로 호출이다(48). 이 대상 파일에는 포함 헤더의 매크로 정의가 없으므로 매크로 확장 후의 참조 여부는 확인하지 않았다(22).
