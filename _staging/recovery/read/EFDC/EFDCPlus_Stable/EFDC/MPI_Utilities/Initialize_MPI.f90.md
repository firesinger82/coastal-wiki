---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/MPI_Utilities/Initialize_MPI.f90
lines: 80
sha256: 06a30d936264dee4b849c1d8efef6da2dbc26e894d26886fe69012ff659c8052
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Initialize_MPI.f90 — 판독 구간 기록

구간은 1행부터 80행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–30 | EFDC+ 표제·저작권·GPLv2·개발사 안내(1–11). MPI 환경과 통신자(communicator) 초기화 설명·저자·날짜(12–15). Initialize_MPI 입구(16). GLOBAL·MPI·Variables_MPI 사용·implicit none(18–22). ierr·required_thread·provided_thread_sup 정수를 선언한다(26–29). 구분 주석·빈 줄 포함(17·21·23–25·30). |
| 31–59 | 시작 시 16행 Initialize_MPI 안. MPI_INIT 호출은 주석이다(33). `required_thread = MPI_Thread_Funneled` (37)로 스레드(thread) 지원 수준을 정하고 MPI_Init_thread를 호출한다(38). MPI_COMM_RANK는 MPI_Comm_World 내 process_id를 받는다(41). MPI_COMM_SIZE는 num_Processors를 받는다(44). 스레드 수준 검사 전체가 주석이다(46–58). 주석 조건은 `!    if( provided_thread_sup .lt. required_thread )then` (47)와 그 안 `!         if( process_id .eq. 0 )then` (51)이다. 경고 출력·omp_set_num_threads(1) 호출도 주석이다(52–56). |
| 60–80 | 시작 시 16행 Initialize_MPI 안. MPI 실수 정의 주석과 다시 주석 처리된 MPI_INIT 호출(60–63). MPI_COMM_RANK를 다시 호출한다(66). Setup_MPI_Debug_File 호출(69). WriteBreak 호출 사이에 process_id·master_id·num_Processors를 mpi_log_unit에 출력한다(71–75). `DoublePrecision = KIND(DXU) == 8` (77)로 DXU의 kind 값이 8인지 논리값을 설정한다. 루틴 종료·마지막 빈 줄(79–80). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 37–58: MPI_Init_thread에서 provided_thread_sup를 받는다. 지원 수준 검사·경고·단일 스레드로 낮추는 블록은 모두 주석이다.
- 41·66: 동일한 MPI_Comm_World의 process_id를 얻는 MPI_COMM_RANK 호출이 두 번 있다.
- 27·38·41·44·66: MPI 호출들은 ierr를 받는다. 이 파일에는 ierr 값을 검사하는 실행 조건이 없다.
- 77: DoublePrecision은 KIND(DXU)==8로 설정된다. kind 값 8을 직접 비교한다.
