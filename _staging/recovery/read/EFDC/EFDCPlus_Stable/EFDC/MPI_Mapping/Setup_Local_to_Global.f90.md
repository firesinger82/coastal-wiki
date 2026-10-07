---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/MPI_Mapping/Setup_Local_to_Global.f90
lines: 195
sha256: a2ea49b4ff6225c26ab7482d251e5f79243a44577bf2edf5619a7d411b09b220
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Setup_Local_to_Global.f90 — 판독 구간 기록

구간은 1행부터 195행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–36 | EFDC+ 출처·저작권·GPLv2 머리말(1–8). 전역(global) 좌표에 대응하는 지역(local) 좌표와 소속 프로세스(process)를 구성하여 모두에게 전달한다는 설명·저자·날짜 주석(9–17). `Setup_Local_to_Global` 시작(19). GLOBAL·MPI 변수·매핑·MPI 사용(21–24). implicit none과 지역 정수, 수집 크기 recv_size_all·변위(displacement) disps_all 배열, send_size·IERR·l_sort 선언(26–35). 구분 주석·빈 줄 포함. |
| 37–65 | 시작 시 19행 Setup_Local_to_Global 루틴 안. recv_size_all·disps_all을 num_Processors 크기로 할당한다(37–38). `allocate(loc_to_glob((ic-4)*(jc-4)))` (40). loc_to_glob의 process·local_i/j·global_i/j·local_l 필드를 0으로 초기화한다(41–46). `allocate(all_loc_to_glob(ic_global*jc_global))` (48), 수집 구조의 앞 필드들과 global_l도 0으로 초기화한다(49–55). sorted_loc_to_glob(LA_Global)를 할당하고 같은 일곱 필드를 0으로 초기화한다(57–64). |
| 66–91 | 시작 시 19행 Setup_Local_to_Global 루틴 안. `if( active_domains == 1 )then` (66). `Do i = 1, LA_Global-1` (68)에서 `l_sort = i + 1` (69), `loc_to_glob(i).process = 0` (70). local_l·global_l에 l_sort를 저장하고 IL·JL로 얻은 좌표를 지역/전역 양쪽에 저장한다(72–77). sorted_loc_to_glob(l_sort)에 일곱 필드를 복사한다(79–85). 루프 종료(86), 디버깅용 i=0(87), return(88). 조건 종료와 빈 줄(90–91). |
| 92–117 | 시작 시 19행 Setup_Local_to_Global 루틴 안이며 66행 단일 영역 분기 밖. start=0(93). `Do j = 1,jc_global` (94), `Do i = 1,ic_global` (95). `if( IG2IL(i) > 2 .and. IG2IL(i) <= ic-2 )then                ! *** exclude ghost cells` (97), `if( JG2JL(j) > 2 .and. JG2JL(j) <= jc-2 )then              ! *** exclude ghost cells` (99), `if( ijct_global(i,j) > 0 .and. ijct_global(i,j) < 9 )then` (100). 세 조건 안에서 `start = start + 1` (101). loc_to_glob(start)에 process_id, 변환된 지역 좌표, 원래 전역 좌표, lij·lij_global의 지역/전역 L을 저장한다(103–111). 조건·루프 종료와 빈 줄(112–117). |
| 118–128 | 시작 시 19행 Setup_Local_to_Global 루틴 안. send_size=start(119). `MPI_Allgather(send_size, 1, MPI_Integer4, recv_size_all, 1, MPI_Integer4, DSIcomm, ierr)` 호출(121)로 송신 개수를 공유한다. disps_all(1)=0(124). `do ii = 2, active_domains` (125)에서 `disps_all(ii) = disps_all(ii-1) + recv_size_all(ii-1)` (126). 루프 종료·빈 줄(127–128). |
| 129–144 | 시작 시 19행 Setup_Local_to_Global 루틴 안. 전처리 조건(preprocessor condition) `#ifdef GNU` (129). MPI 자료형을 따로 구성하지 않고 필드별로 모은다는 주석(130). 첫 호출은 `call MPI_AllGatherV(loc_to_glob.process,  send_size, MPI_Integer4, all_loc_to_glob.process,  recv_size_all, disps_all, MPI_Integer4, DSIcomm, ierr)` (131). 같은 수집 크기·변위·통신자(communicator)로 local_i(133), local_j(135), global_i(137), global_j(139), local_l(141), global_l(143)을 각각 `MPI_AllGatherV`로 모은다. `#else` (144)에서 다른 전처리 분기로 넘어간다. |
| 145–161 | 시작 시 19행 Setup_Local_to_Global 루틴 및 129행 #ifdef GNU의 144행 #else 안. 첫 호출은 `call MPI_AllGatherV(loc_to_glob.process,  send_size, MPI_Integer4, all_loc_to_glob.process,  recv_size_all, disps_all, MPI_Integer4, DSIcomm, master_id, ierr)` (146). 같은 형태로 local_i(148), local_j(150), global_i(152), global_j(154), local_l(156), global_l(158)을 각각 수집한다. 이 일곱 호출은 DSIcomm과 ierr 사이에 master_id를 전달한다. `#endif` (159), 구분 주석·빈 줄(160–161). |
| 162–176 | 시작 시 19행 Setup_Local_to_Global 루틴 안이며 GNU 전처리 분기 밖. 전역 L 기준 재배열 설명(162). `Do i = 1, LA_Global-1` (163)에서 l_sort=all_loc_to_glob(i).global_l(165). sorted_loc_to_glob(l_sort)에 process·local_i/j·global_i/j·local_l·global_l의 일곱 필드를 복사한다(167–173). 루프 종료·빈 줄(174–176). |
| 177–195 | 시작 시 19행 Setup_Local_to_Global 루틴 안. `#ifdef DEBUGGING` (177)에서 `WriteBreak(mpi_log_unit)` 호출(179). `if( MPI_Write_Flag )then` (180)이면 설명·열 제목 로그(181–182), `do i = 2, LA_Global` (183)에서 정렬된 구조의 소속 프로세스·전역 L·지역 L·지역/전역 좌표를 출력한다(184–185). `WriteBreak` 호출 뒤 해당 조건 종료(187–188). MPI_Write_Flag 조건 밖이지만 DEBUGGING 안에서 recv_size_all·sum(recv_size_all)·ic_global*jc_global·disps_all을 출력한다(190–192). `#endif` (193), 루틴 종료·빈 줄(194–195). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 28·33: ll·i_tmp·j_tmp·displacement는 선언 후 이 파일에서 사용되지 않는다.
- 40–46·103–111: loc_to_glob의 초기화 목록에는 global_l이 없다. global_l 대입은 단일 영역 분기의 반복 및 다중 영역에서 채택된 셀의 start 위치에 있다(73·111).
- 37–38·121·124–127: recv_size_all·disps_all의 할당 크기는 num_Processors이다. disps_all의 대입 범위는 1과 2..active_domains이며 배열 전체 초기화는 이 파일에 없다.
- 66–88: 단일 활성 영역 경로는 process 필드를 상수 0으로 저장한다. 이 경로는 return으로 끝나므로 뒤의 MPI 수집과 DEBUGGING 블록을 실행하지 않는다.
- 131–143·146–158: GNU 분기의 MPI_AllGatherV 호출은 DSIcomm 뒤에 ierr를 전달한다. 다른 분기의 호출은 DSIcomm 뒤에 master_id와 ierr를 전달한다. MPI 루틴의 인수 정의는 이 파일 판독 범위에 포함하지 않았다.
- 163–173: 재배열은 LA_Global-1개 수집 항목을 순회한다. l_sort를 배열 인덱스로 사용하기 전에 양수·상한을 검사하는 문장은 이 블록에 없다.
- 121·131–143·146–158: MPI 호출은 ierr를 받는다. 이 파일에는 ierr에 대한 조건 검사나 후속 참조가 없다.
