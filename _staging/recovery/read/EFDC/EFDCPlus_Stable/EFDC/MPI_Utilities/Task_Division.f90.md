---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/MPI_Utilities/Task_Division.f90
lines: 240
sha256: b9ee59c0690857f0125386ea012eb9da754a8568dd57b7ba8fe1c67693f2e1e1
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Task_Division.f90 — 판독 구간 기록

구간은 1행부터 240행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–40 | EFDC+ 표제·저작권 2021–2022·GPLv2 안내(1–8). T 작업을 P 프로세스(process)에 비슷한 개수의 연속 구간으로 미리 배분한다는 설명(9–21). LGPL 안내·2007-10-20 수정·John Burkardt 저자(23–33). task_number와 proc_first/proc_last 인수 설명 및 빈 주석(35–40). |
| 41–85 | 전처리 조건은 `#ifdef ENABLE_MPI` (41)이다. Task_Division 입구(42). GLOBAL·Variables_MPI·Broadcast_Routines·MPI 사용·implicit none(44–49). 작업 구간·프로세스 수·반올림 함수·남은 작업 수·출력 변수 선언(51–67). `cur_p = proc_last + 1 - proc_first` (69)로 대상 프로세스 수를 계산한다. `if(process_id == master_id) then` (71)이면 작업 수·프로세스 수·첫/마지막 번호·배분표 머리글을 표준 출력에 쓴다(72–84). 조건 종료(85). |
| 86–105 | 시작 시 41행 ENABLE_MPI 전처리 구간·42행 Task_Division 안. writeoutid=process_id(87). 길이 3 outfilename에 I3 형식으로 번호를 쓴다(88). unit_num_MPI+writeoutid로 MPI_info_proc_ 번호 .txt 파일을 열고 status='Delete'로 닫은 뒤 APPEND로 다시 연다(89–91). 파일에 작업 수·프로세스 수·첫/마지막 번호·배분표 머리글을 출력한다(93–104). 빈 줄 포함. |
| 106–129 | 시작 시 41행 ENABLE_MPI 전처리 구간·42행 Task_Division 안. i_hi=0, task_remain=task_number, proc_remain=cur_p(106–109). proc=proc_first..proc_last 루프(111)에서 `task_proc = i4_div_rounded ( task_remain, proc_remain )` (112)로 이번 작업 수를 구한다. 계산식은 `proc_remain = proc_remain - 1` (114), `task_remain = task_remain - task_proc` (115), `i_lo = i_hi + 1` (116), `i_hi = i_hi + task_proc` (117)이다. lower_task_bound(proc+1)와 upper_task_bound(proc+1)에 i_lo/i_hi를 복사한다(119–120). `if(process_id == master_id) then` (122)이면 표준 출력에 배분 결과를 쓴다(123). num_task_per_process(proc+1)=task_proc(125), 각 프로세스 로그에 같은 결과 출력(127). 루프 종료·빈 줄(128–129). |
| 130–156 | 시작 시 41행 ENABLE_MPI 전처리 구간·42행 Task_Division 안. `total_num_constituents = upper_task_bound(num_proc) - lower_task_bound(0)` (131)로 total_num_constituents를 구한다. i=1..num_proc 루프(134)에서 `num_elem_to_each_array(i) = LCM*KCM*num_task_per_process(i)` (135)로 전송 수를 구한다. `If(i == 1) then ! Starting displacement should be zero` (136)이면 `displacements_L_index(i) = 0` (137)로 시작 변위를 0으로 정한다. else(138)는 `displacements_L_index(i) = displacements_L_index(i-1) + num_task_per_process(i-1)` (139)로 작업 수를 누적한다. 변위(displacement) 배열 로그 출력(143–144). 다음 1..num_proc 루프에서 `recv_counts_array(i) = LCM*KCM*num_task_per_process(i)` (147)로 수신 수를 계산하고 로그에 출력한다(146–151). return·루틴 종료·빈 줄(153–156). |
| 157–198 | 시작 시 41행 ENABLE_MPI 전처리 구간 안. i4_div_rounded 함수 시작(157). 정수 A/B의 가장 가까운 정수 결과를 계산한다는 설명(159–166). LGPL·2011-10-23 수정·John Burkardt 저자·인수/결과 설명(168–188). implicit none·정수 a/a_abs/b/b_abs/result/value 선언(189–197). 상수 선언은 `integer , parameter :: i4_huge = 2147483647` (196)이다. 빈 줄 포함(158·190·198). |
| 199–240 | 시작 시 41행 ENABLE_MPI 전처리 구간·157행 i4_div_rounded 안. `if ( a == 0 .and. b == 0 ) then` (199)이면 value=i4_huge(201). `else if ( a == 0 ) then` (203)이면 value=0(205). `else if ( b == 0 ) then` (207) 안 `if ( a < 0 ) then` (209)이면 `value = - i4_huge` (210), else(211)는 `value = + i4_huge` (212)이다. 바깥 else(215)는 `a_abs = abs ( a )` (217), `b_abs = abs ( b )` (218), `value = a_abs / b_abs` (220)로 절댓값 정수 몫을 구한다. `if ( ( 2 * value + 1 ) * b_abs < 2 * a_abs ) then` (224)이면 `value = value + 1` (225)로 몫을 1 증가시킨다. `if ( ( a < 0 .and. 0 < b ) .or. ( 0 < a .and. b < 0 ) ) then` (230)이면 `value = - value` (231)로 부호를 바꾼다. value를 함수 결과에 복사(236), return·함수 종료·전처리 #endif(238–240). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 64·131: total_num_constituents는 선언과 대입 이후 이 파일에서 사용되지 않는다.
- 119–120·131: 작업 경계 대입의 인덱스는 proc+1이다. total_num_constituents 계산은 upper_task_bound(num_proc)와 lower_task_bound(0)를 참조한다. 배열 선언과 호출 인수의 범위는 이 파일에 없다.
- 87–91·153–155: 로그 파일을 삭제 후 APPEND로 다시 연다. 다시 연 유닛의 명시적 close는 루틴 종료 전에 없다.
- 67·88–91: 프로세스 번호 문자열은 길이 3과 I3 형식이다. trim은 문자열 뒤 공백을 제거하며 파일명 조합에는 앞 공백을 제거하는 호출이 없다.
- 196·199–212: i4_huge 상수는 2147483647이다. 0/0과 0이 아닌 값/0의 경우 이 상수 또는 부호를 바꾼 상수를 반환한다.
- 220–225: 반올림 조건은 엄격한 < 비교이다. 정확히 절반인 경우에는 value+1 대입이 실행되지 않는다.

