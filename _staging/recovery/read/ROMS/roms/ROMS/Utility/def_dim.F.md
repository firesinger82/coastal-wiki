---
file: models/ROMS/raw/source_code/roms/ROMS/Utility/def_dim.F
lines: 192
sha256: 88e617a05081444b3b52ab8f2fbd9d6cb0bfc9e39787d7ead99c38822749207e
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# def_dim.F — 판독 구간 기록

구간은 1행부터 192행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–32 | `#include "cppdefs.h"` (1)로 cppdefs.h를 포함하고 def_dim_mod 모듈을 연다(2). 저작권·MIT/X 라이선스·요청된 NetCDF 차원 정의 목적 주석을 포함한다(4–13). mod_param·mod_parallel·mod_iounits·mod_scalars와 FoundError를 사용하고 implicit none을 둔다(15–22). `INTERFACE def_dim` (24)은 def_dim_nf90을 등록한다(25). `#if defined PIO_LIB && defined DISTRIBUTE` (26)·`#endif` (28)는 def_dim_pio 등록을 감싼다(27). 인터페이스 종료·CONTAINS·주석을 포함한다(29–32). |
| 33–87 | def_dim_nf90 함수 선언과 표준 NetCDF-3/4 차원 정의 목적을 적는다(34–39). 입력 ng는 중첩 격자(nested grid) 번호, model은 모델 식별자(identifier), ncid는 파일 식별자, ncname·DimName은 파일·차원 이름, DimSize는 크기이다(43–48·68–73). 출력은 status와 DimId이다(52–53·70·77). mod_netcdf를 사용한다(57). `#if !defined PARALLEL_IO  && defined DISTRIBUTE` (59)·`#endif` (62)는 distribute_mod의 mp_bcasti 사용을 감싼다(61). `#if !defined PARALLEL_IO  && defined DISTRIBUTE` (79)·`#endif` (81)는 정수 ibuffer(3) 선언을 감싼다(80). implicit none·지역 선언·MyFile·SourceFile 설정과 빈 줄·주석을 포함한다(64–87). 구간 시작에는 열린 전처리 조건이나 바깥 루틴이 없다. |
| 88–121 | 시작 시 34행 def_dim_nf90 함수 안. `status=nf90_noerr` (92)로 시작한다. `IF (OutThread) THEN` (94)에서 `status=nf90_def_dim(ncid, TRIM(DimName), DimSize, DimId)` (95)를 실행한다. `IF (FoundError(status, nf90_noerr, __LINE__, MyFile)) THEN` (96)이면 `IF (Master) WRITE (stdout,10) TRIM(DimName), TRIM(ncname)` (97)를 실행하고 exit_flag=3·ioerror=status로 둔다(98–99). `#if !defined PARALLEL_IO  && defined DISTRIBUTE` (103)·`#endif` (114)에서 DimID·status·exit_flag를 ibuffer(1:3)에 복사하고 mp_bcasti로 그룹의 모든 스레드(thread)에 방송(broadcast)한다(107–110). 방송 후 세 값을 복원한다(111–113). FORMAT 10의 차원·파일명 오류 출력, RETURN·함수 종료·빈 줄을 포함한다(116–121). |
| 122–171 | `#if defined PIO_LIB && defined DISTRIBUTE` (122)에서 def_dim_pio 함수를 연다(125–126). 병렬 입출력(Parallel-IO, PIO) 라이브러리로 요청한 차원을 정의한다는 목적 주석이다(129–130). 입력 ng·model·ncname·DimName·DimSize와 file_desc_t형 pioFile, 출력 status·DimId를 설명한다(134–146). pioFile 주석은 fh를 파일 핸들러(file handler), iosystem을 입출력 시스템 기술자(descriptor)로 적는다(136–138). pio를 사용하며 인수·지역 status·MyFile을 선언하고 SourceFile을 설정한다(150–170). 시작에는 열린 바깥 함수나 전처리 조건이 없다. 주석·빈 줄을 포함한다. |
| 172–192 | 시작 시 122행 `#if defined PIO_LIB && defined DISTRIBUTE`, 125행 def_dim_pio 함수 안. `status=PIO_noerr` (176)로 시작한 뒤 `status=PIO_def_dim(pioFile, TRIM(DimName), DimSize, DimId)` (178)를 실행한다. 조건 원문은 `IF (FoundError(status, PIO_noerr, __LINE__,                       &` (179), `&                 __FILE__)) THEN` (180)이다. 참이면 `IF (Master) WRITE (stdout,10) TRIM(DimName), TRIM(ncname)` (181)를 실행하고 exit_flag=3·ioerror=status로 둔다(182–183). FORMAT 10은 차원·파일명 오류 메시지를 정의한다(186–187). RETURN·함수 종료(189–190), `#endif` (191), 모듈 종료(192)를 포함한다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 70·94–95·103–110: DimId는 intent(out) 인수이다. nf90_def_dim 호출은 OutThread 참 분기 안에 있다. 방송 분기의 ibuffer(1)=DimID 대입은 그 분기 밖에 있다. 이 함수에는 DimId를 별도로 초기화하는 대입이 없다.
- 98–99·107–113: NetCDF 오류 처리에서 exit_flag와 ioerror를 설정한다. 방송 버퍼에는 DimID·status·exit_flag만 넣으며 ioerror는 넣지 않는다.
