---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/MPI_Utilities/Report_Max_Min_Timing.f90
lines: 98
sha256: a519e112838df31f2f9f8bcc5506016e90cac08b4ad23d3f93453dc69b243004
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Report_Max_Min_Timing.f90 — 판독 구간 기록

구간은 1행부터 98행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–39 | EFDC+ 표제·저작권·GPLv2·개발사 안내(1–11). 모든 프로세스(process)의 시간 최소·최대·비율을 TIME.LOG에 쓴다는 설명·저자·날짜(12–16). Report_Max_Min_Timing 입구·GLOBAL/MPI 변수/MPI 사용(18–22). routine_time은 real(RKD), time_id는 길이 8 문자열(27–28). 시간 수집 배열·최소/최대·비율·프로세스 위치·유닛·ierr 선언(31–37). 기본값은 `logical, Save :: first_time = .TRUE.` (38)이다. |
| 40–63 | 시작 시 18행 Report_Max_Min_Timing 안. `time_log_unit = 9 ! this is the unit for the TIME.LOG file` (40)로 유닛(file unit)을 9로 정한다. `if(process_id == master_id )then` (43)이면 OUTDIR//'TIME.LOG'를 APPEND로 연다(44). `if( first_time  )then` (47) 안 `if(process_id == master_id )then` (48)이면 WriteBreak와 부하 균형(load balancing) 안내를 출력한다(49–50). 첫 호출 분기에서 first_time=.FALSE.로 바꾼다(53). num_Processors 크기 수집 배열 할당·0 초기화(57–58). MPI_AllGather는 routine_time 1개를 MPI_Real8로 DSIcomm 전체에서 수집한다(62). |
| 64–81 | 시작 시 18행 Report_Max_Min_Timing 안. `if(process_id == master_id )then` (65)이면 `min_time = minval(timing_frm_all_procs, 1)` (67), `max_time = maxval(timing_frm_all_procs, 1)` (68)로 최소·최대를 구한다. `process_min = findloc(timing_frm_all_procs, min_time, 1)` (71), `process_max = findloc(timing_frm_all_procs, max_time, 1)` (72)로 해당 값의 배열 위치를 얻는다. `if(max_time > 1E-8 .and. min_time > 1E-8 )then` (76)이면 `ratio_max_min = max_time/min_time` (77)로 비율을 구한다. else(78)의 기본값은 `ratio_max_min = 0.0` (79)이다. 내부 조건 종료·빈 줄(80–81). |
| 82–98 | 시작 시 18행 Report_Max_Min_Timing·65행 master 참 분기 안. 1..num_Processors 루프는 수집 시간과 i를 “in process” 값으로 출력한다(82–84). 최소·최대와 process_min/process_max, 비율을 출력한다(86–88). 경과시간 대비 비율 식이 들어 있는 출력문은 `write(time_log_unit, '(a,f8.3,a)')'Percent of max time to elapsed time = ', (max_time/TIME_END)*100., '%'` (89)이다. WriteBreak 호출·master 조건 종료(90–92). 조건 밖에서 time_log_unit close(94), 배열 deallocate(96), 루틴 종료(98). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 62·71–72·82–87: 시간 수집은 MPI_AllGather를 사용한다. 출력 프로세스 번호는 1부터 시작하는 배열 위치 i와 findloc 결과이다. 이 파일에는 해당 위치에서 1을 빼는 문장이 없다.
- 43–45·65–94: TIME.LOG open과 출력은 master 조건 안에 있다. close(time_log_unit)는 그 조건 밖에서 실행된다.
- 76–89: max/min 비율에는 1E-8 하한 조건이 있다. 경과시간 대비 백분율 식의 TIME_END 분모에는 이 블록 내 별도 0 검사가 없다.
- 27·62: 입력 시간은 real(RKD)이다. MPI_AllGather의 송수신 자료형은 MPI_Real8로 고정되어 있다.

