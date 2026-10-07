---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/MPI_Utilities/Setup_MPI_Debug_File.f90
lines: 99
sha256: 0b75a5737077701b1f5698125ba83e1024e98debfc42b3d867cb1d873205dd19
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Setup_MPI_Debug_File.f90 — 판독 구간 기록

구간은 1행부터 99행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–34 | EFDC+ 표제·저작권·GPLv2·개발사 안내(1–11). 프로세스(process)별 디버그(debug) 파일 설정 설명·날짜·저자(12–16). Setup_MPI_Debug_File 입구(18). GLOBAL·MPI·Variables_MPI·Variables_MPI_Write_Out 사용(20–23). 전처리(preprocessor) 조건 `#ifndef GNU` (24)에서 IFPORT를 사용하고 #endif로 닫는다(25–26). implicit none·정수 ierr/RES·길이 24 mpi_filename·길이 200 STR 선언(28–33). 빈 줄 포함. |
| 35–64 | 시작 시 18행 Setup_MPI_Debug_File 안. 유닛(file unit) 계산은 `mpi_efdc_out_unit = mpi_efdc_out_unit + process_id` (36), `mpi_log_unit = mpi_log_unit + process_id` (37), `mpi_comm_unit = mpi_comm_unit + process_id` (38), `mpi_mapping_unit = mpi_mapping_unit + process_id` (39), `mpi_qdwaste_unit = mpi_qdwaste_unit + process_id` (40), `mpi_error_unit = mpi_error_unit + process_id` (41)이다. `#ifdef _WIN` (43)이면 `OUTDIR = '#output\'` (44), 전처리 else(45)는 `OUTDIR = '#output/'` (46)로 출력 디렉터리를 정한다. `if( process_id == master_id )then` (48) 안 `#ifdef GNU` (49)이면 `RES = SYSTEM( 'mkdir -p ./' // trim(OUTDIR))` (50)로 디렉터리를 만든다. 전처리 else(51)는 `RES = MAKEDIRQQ('#output')` (52)를 실행한다. 그 경로에서 `if( .not. RES )then` (53)이면 `RES = GETLASTERRORQQ( )` (54) 뒤 `if( RES == ERR$NOENT )then` (55)에서 STOPP 경로 오류 호출(56), `elseif( RES == ERR$ACCES )then` (57)에서 STOPP 권한 오류 호출(58). 조건들 종료(59–62). MPI_barrier(MPI_Comm_World,ierr)로 동기화한다(63). |
| 65–84 | 시작 시 18행 Setup_MPI_Debug_File 안. 실행 파일명·버전의 STR 표제 생성(65). 프로세스 번호 I3.3과 .log를 붙여 EFDC_out_proc_, log_mpi_proc_, log_error_proc_ 이름을 만든다(68·74·80). 각각 mpi_efdc_out_unit·mpi_log_unit·mpi_error_unit에 status='replace'로 연다(69·75·81). 파일명을 대응 모듈 변수에 복사한다(70·76·82). 각 파일에 별표·표제를 출력한다(71·77·83). 빈 줄 포함(66·72·78·84). |
| 85–99 | 시작 시 18행 Setup_MPI_Debug_File 안. `if( MPI_DEBUG_FLAG )then` (86)이면 comm_mpi_proc_와 I3.3 번호로 통신(communication) 로그 이름을 만들고 replace로 열어 표제를 출력한다(87–89). 이 조건 밖에서 map_mpi_proc_와 I3.3 번호로 매핑(mapping) 로그를 replace로 열고 표제를 출력한다(93–95). 루틴 종료·마지막 빈 줄(97–99). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 36–41: 유닛 번호는 현재 모듈 변수값에 process_id를 더한다. 이 루틴 안에는 이 덧셈 전 기준값으로 되돌리는 대입이 없다.
- 31·52–55: RES는 integer로 선언한다. 비-GNU 경로에서 MAKEDIRQQ 결과를 RES에 받고 .not. RES 조건을 사용한 뒤 GETLASTERRORQQ 결과를 같은 RES에 받는다. 컴파일러의 처리 여부는 판독하지 않았다.
- 49–61: GNU 경로의 SYSTEM 반환값도 RES에 받는다. 오류 코드 검사와 STOPP 호출은 전처리 else 경로에만 있다.
- 40·67–95: mpi_qdwaste_unit을 계산한다. 이 루틴에는 해당 유닛으로 파일을 여는 문장이 없다.

