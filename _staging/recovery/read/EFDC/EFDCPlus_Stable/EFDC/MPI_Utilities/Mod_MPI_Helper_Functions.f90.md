---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/MPI_Utilities/Mod_MPI_Helper_Functions.f90
lines: 242
sha256: a807bcbde25370b48824ea6bb2dabbf0ce10c1fd881f3dad8620e179001d56ab
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Mod_MPI_Helper_Functions.f90 — 판독 구간 기록

구간은 1행부터 242행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–29 | EFDC+ 표제·저작권·GPLv2 안내(1–8). Mod_MPI_Helper_Functions는 MPI 변수·매핑(mapping)·Variables_Propwash·GLOBAL의 KC/ISDRY/HDRY/HP·XYIJCONV를 사용한다(9–15). implicit none·기본 private·공개 get_nearest_cell/get_subdomain_id/r8_atan/Get_Cell 선언(17–20). get_nearest_cell 인터페이스(interface)는 주석이다(23–26). contains·빈 줄(28–29). |
| 30–68 | get_nearest_cell의 설명·인수·변수 선언(30–45). 입력 좌표는 real(kind=RKD)이고 결과는 정수이다. Distance_to_Cells를 LA_Global 크기로 할당하고 0 초기화한다(47–48). 거리(distance) 계산은 `Distance_to_Cells(2:LA_Global) = SQRT((x_position - XCOR_Global(2:LA_Global,5))**2 + &` (52); `(y_position - YCOR_Global(2:LA_Global,5))**2)` (53)이다. `Min_L_loc_index = minloc(Distance_to_Cells(2:LA_Global)) + 1` (55)로 2..LA_Global 부분 배열의 최소 거리 위치를 원래 인덱스로 옮긴다. `cell_index = Map2Local(Min_L_loc_index(1)).LL` (58)로 전역(global) 위치를 지역(local) 셀 번호로 옮긴다. `if( ISDRY > 0 .and. HP(cell_index) < HDRY  )then` (61)이면 STOPP 경고를 호출한다(62). 거리 배열 해제·함수 종료·빈 줄(65–68). |
| 69–86 | get_subdomain_id 설명·pure 함수 입구·정수 인수와 결과 선언(69–80). `subdomain_id = sorted_loc_to_glob(cell_index).process` (82)로 sorted_loc_to_glob의 process 필드를 반환한다. 설명은 유령 셀(ghost cells)을 제외한 부분 영역(subdomain)의 프로세스 번호라고 적는다(70). 함수 종료·빈 줄(84–86). |
| 87–141 | r8_atan 함수 시작(87). 주석은 Y/X 역탄젠트(inverse tangent), ATAN/ATAN2와의 반환 범위 비교, 사분면(quadrant) 처리, LGPL, 1999-04-14 수정, John Burkardt 저자와 인수를 설명한다(89–128). 출력 범위는 주석상 0..2*PI이다(100·125–127). implicit none·kind=8 실수 선언(129–138). 상수는 `real ( kind = 8 ), parameter :: r8_pi = 3.141592653589793D+00` (134)이다. 특수 경우 주석·빈 줄(139–141). |
| 142–185 | 시작 시 87행 r8_atan 안. `if( x == 0.0D+00  )then` (142)이면 `if( 0.0D+00 < y  )then` (144)에서 `value = r8_pi / 2.0D+00` (145), `elseif(  y < 0.0D+00  )then` (146)에서 `value = 3.0D+00 * r8_pi / 2.0D+00` (147), `elseif(  y == 0.0D+00  )then` (148)에서 `value = 0.0D+00` (149)를 실행한다. 바깥 `elseif(  y == 0.0D+00  )then` (152)이면 `if( 0.0D+00 < x  )then` (154)에서 value=0(155), `elseif(  x < 0.0D+00  )then` (156)에서 value=r8_pi(157). 바깥 else(162)는 `abs_y = abs ( y )` (164), `abs_x = abs ( x )` (165), `theta_0 = atan2 ( abs_y, abs_x )` (167)로 양수 절댓값의 atan2를 구한다. 사분면 조건은 `if( 0.0D+00 < x .and. 0.0D+00 < y  )then` (169), `elseif(  x < 0.0D+00 .and. 0.0D+00 < y  )then` (171), `elseif(  x < 0.0D+00 .and. y < 0.0D+00  )then` (173), `elseif(  0.0D+00 < x .and. y < 0.0D+00  )then` (175)이다. 대응 결과는 value=theta_0(170), `value = r8_pi - theta_0` (172), `value = r8_pi + theta_0` (174), `value = 2.0D+00 * r8_pi - theta_0` (176)이다. value 반환·return·함수 종료·빈 줄(181–185). |
| 186–224 | get_cell 설명·인수 선언(186–199). 좌표는 m, 주석의 유효 결과는 Cell Index>1이다(190–192). `if( L > 1 )then` (202) 안 `if( insidecell(L, x_position, y_position) )then` (203)이면 L을 반환하고 조기 return한다(204–205). 같은 바깥 조건 안에서 1..9 루프(213)는 adjacent_l(i,L)을 L1에 복사한다(214). `if( L1 > 0 )then` (215) 안 `if( insidecell(L1, x_position, y_position) )then` (216)이면 L1을 반환하고 return한다(217–218). 이웃 순서 3×3 표는 주석이다(209–212). 루프·조건 종료와 빈 줄(219–224). |
| 225–242 | 시작 시 194행 get_cell 안이며 202행 조건 밖. cell_index=0 초기화(226). OpenMP 병렬 루프(parallel loop)는 DEFAULT(SHARED), PRIVATE(L1), REDUCTION(MAX:cell_index)를 지정한다(229). L1=2..LA 루프(230)에서 `if( cell_index > 0 ) cycle       ! *** Once cell_index is defined fast forward as quickly as possible for all domains` (231)를 실행한다. `if( insidecell(L1, x_position, y_position) )then` (232)이면 cell_index=L1(233). 루프와 OpenMP 구간 종료(235–236). return·함수·모듈 종료·빈 줄(238–242). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 14: 가져온 KC는 이 파일의 다른 선언·실행식에 등장하지 않는다.
- 47·52–58·61: get_nearest_cell은 전역 2..LA_Global 전체에서 가장 가까운 중심 좌표를 찾는다. Map2Local 결과를 HP 인덱스로 사용하기 전에 cell_index의 범위를 검사하는 별도 조건은 이 함수에 없다.
- 131–138: r8_atan의 실수 선언은 kind=8이고 PI 상수도 직접 적혀 있다. 좌표 함수의 입력 선언은 kind=RKD이다(39–40·197–198).
- 192·215–218: get_cell 설명은 유효 셀 번호를 >1이라고 적는다. 이웃 셀을 insidecell에 전달하는 실행 조건은 L1>0이다.
- 229–235: 전체 영역 검색은 MAX:cell_index 축약(reduction)을 지정한다. 루프는 cell_index>0이면 cycle하고, insidecell이 참인 L1을 cell_index에 대입한다.

