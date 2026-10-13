---
file: models/ROMS/raw/source_code/roms/ROMS/Nonlinear/Vegetation/marsh_tidal_range.F
lines: 229
sha256: ff6ffd864290f061838cac67d8195acf66ae2848cf02acaf0a24b5c162700721
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# marsh_tidal_range.F — 판독 구간 기록

구간은 1행부터 229행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–37 | 파일 내부에서 열린 전처리 조건 없음. `#include "cppdefs.h"` (1)로 cppdefs.h 포함, MODULE marsh_tidal_range_mod(2). `#if defined MARSH_TIDAL_RANGE` (4). 저작권·MIT/X 머리말(6–11). 습지(marsh) 생체량(biomass) 생산과 수직 성장(vertical growth)에 쓸 조차(tidal range)·평균 고조위(mean high water)를 계산한다는 주석(13–14). mod_param/forces/grid/ocean/scalars/vegetation 사용(18–23), bc_r2d_tile·bc_r3d_tile USE(25–26). `# ifdef DISTRIBUTE` (27)에서 mp_exchange2d·mp_exchange3d USE(28), `# endif` (29). implicit none·공개 marsh_tidal_range·PRIVATE·CONTAINS(31–36), 주석·빈 줄 포함. |
| 38–77 | 시작 시 4행 `#if defined MARSH_TIDAL_RANGE` 안. marsh_tidal_range(ng,tile) 선언(39), mod_stepping(42), 정수 인수(46), MyFile=__FILE__(50–51). `# include "tile.h"` (53)로 tile.h 포함. `# ifdef PROFILE` (55)에서 `CALL wclock_off (ng, iNLM, 44, __LINE__, MyFile)` (56), `# endif` (57). `marsh_tidal_range_tile`에 타일·작업 경계·nstp·OCEAN%zeta·VEG의 zeta_max1/zeta_min1/zeta_max_rec/zeta_min_rec/counter_loc_rl/marsh_mask/marsh_high_water/marsh_tidal_range 전달(58–70). `# ifdef PROFILE` (71)에서 다시 `CALL wclock_off (ng, iNLM, 44, __LINE__, MyFile)` (72), `# endif` (73). RETURN·wrapper 종료·주석(75–77). |
| 78–122 | 시작 시 4행 `#if defined MARSH_TIDAL_RANGE` 안. marsh_tidal_range_tile 선언과 인수(79–91), ng/tile·타일 및 작업 경계·nstp 정수 선언(96–99). counter_loc_rl은 real(r8) 스칼라 intent(inout)(101). `# ifdef ASSUMED_SHAPE` (102)에서는 zeta 열린 상한 3차원 intent(in), 극값·기록·습지 마스크·고조위·조차 배열은 intent(inout)(103–110). `# else` (111)는 zeta=(LBi:UBi,LBj:UBj,3), 극값=(LBi:UBi,LBj:UBj), 기록 배열의 마지막 차원 NTIMES_MARSH(112–118). 마지막 세 명시적 선언 원문은 `real(r8), intent(inout):: marsh_mask(LBi:UBj,LBj:UBj)` (119), `real(r8), intent(inout):: marsh_high_water(LBi:UBj,LBj:UBj)` (120), `real(r8), intent(inout):: marsh_tidal_range(LBi:UBj,LBj:UBj)` (121). `# endif` (122). |
| 123–150 | 시작 시 4행 `#if defined MARSH_TIDAL_RANGE` 안, 79행 marsh_tidal_range_tile 안. 정수 i/j/it/iic_loc·counter_new_time/counter_loc·freq, 실수 기록 수·수위·극값·합계·평균·시간·주기 변수 선언(126–134). `# include "set_bounds.h"` (136)로 set_bounds.h 포함. 실행 구분 주석(138–140). `day2sec_loc=86400.0_r8           ! 86400.0_r8` (142), `day_inp_loc=1.0_r8               ! record zeta max, min per day` (143). `time_loc=dt(ng)*iic(ng)          ! ocean time` (145), `tdays_loc=MAX((FLOOR(time_loc/(day_inp_loc*day2sec_loc))),1)` (146), `freq=CEILING(day_inp_loc*day2sec_loc/dt(ng))  ! time step freq to` (147), 이어지는 기록 설명 주석(148), `modm_freq=MOD(iic(ng),freq)                   ! and min` (149), 빈 줄(150). 하루 기록 주기는 1.0_r8로 설정되고 tdays_loc 하한은 1. |
| 151–178 | 시작 시 4행 `#if defined MARSH_TIDAL_RANGE` 안, 79행 marsh_tidal_range_tile 안. `DO j=Jstr,Jend` (151), `DO i=Istr,Iend` (152). `zeta_loc=zeta(i,j,3)          ! store zeta locally first` (153), `ntimes_marsh_rl=REAL(NTIMES_MARSH)` (155), `zeta_max1(i,j)=MAX(zeta_max1(i,j),zeta_loc)` (156), `zeta_min1(i,j)=MIN(zeta_min1(i,j),zeta_loc)` (157). `IF(modm_freq==0.and.counter_loc_rl<=ntimes_marsh_rl) THEN` (161)일 때 `counter_loc_rl=MOD(tdays_loc,ntimes_marsh_rl)` (162). `IF(counter_loc_rl.eq.0.0) THEN` (163)은 counter_loc_rl=ntimes_marsh_rl(164). 기록 인덱스에 INT(counter_loc_rl)을 사용하여 `zeta_max_rec(i,j,INT(counter_loc_rl))=(zeta_max1(i,j))` (169), `zeta_min_rec(i,j,INT(counter_loc_rl))=(zeta_min1(i,j))` (170). 다음 주기 초기값 원문은 `zeta_max1(i,j)=-10.0_r8` (175), `zeta_min1(i,j)= 10.0_r8` (176). IF 종료(177), 구분 주석·빈 줄 포함. |
| 179–194 | 시작 시 4행 `#if defined MARSH_TIDAL_RANGE` 안, 79행 marsh_tidal_range_tile 안, 151행 j·152행 i 루프 안. 평균 계산 주석(179–180), tot_zeta_max·tot_zeta_min=0 초기화(181–182). `DO it=1,NTIMES_MARSH` (183), `tot_zeta_max=zeta_max_rec(i,j,it)+tot_zeta_max` (184), `tot_zeta_min=zeta_min_rec(i,j,it)+tot_zeta_min` (185), it 종료(186). `mean_zeta_max=tot_zeta_max/NTIMES_MARSH` (187), `mean_zeta_min=tot_zeta_min/NTIMES_MARSH` (188). marsh_high_water=mean_zeta_max(190), `marsh_tidal_range(i,j)=mean_zeta_max-mean_zeta_min` (191). `marsh_tidal_range(i,j)=marsh_tidal_range(i,j)` (192)는 자기 대입. i·j 종료(193–194). 평균은 기록 배열의 1..NTIMES_MARSH 전체를 사용. |
| 195–229 | 시작 시 4행 `#if defined MARSH_TIDAL_RANGE` 안, 79행 marsh_tidal_range_tile 안, 공간 루프 밖. `bc_r2d_tile`에 marsh_tidal_range와 marsh_high_water 전달(196–201). it=1..NTIMES_MARSH(203)에서 `bc_r2d_tile`에 zeta_max_rec(:,:,it)와 zeta_min_rec(:,:,it) 전달(204–209), it 종료(210). `# ifdef DISTRIBUTE` (212)에서 `mp_exchange2d`에 배열 수 2·NghostPoints·EWperiodic/NSperiodic·marsh_tidal_range·marsh_high_water 전달(214–218), `mp_exchange3d`에 배열 수 2·세 번째 인덱스 1..NTIMES_MARSH·극값 기록 두 배열 전달(219–223). `# endif` (224), RETURN·tile 루틴 종료(226–227), `#endif` (228), MODULE 종료(229), 주석·빈 줄 포함. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 55–57·71–73: PROFILE 조건 아래에서 wrapper 호출 전과 후에 모두 wclock_off를 호출한다. 이 파일에 wclock_on 호출은 없다.
- 112–121: 명시적 크기 분기에서 zeta·극값·기록 배열의 첫 차원 상한은 UBi이다. marsh_mask·marsh_high_water·marsh_tidal_range의 첫 차원 상한은 UBj이다.
- 61·99·153: nstp를 인수로 받아 선언하지만 수위 읽기는 zeta(i,j,3)을 사용한다. 이 tile 루틴의 실행식에 nstp 참조는 없다.
- 142–149·175–176: 기록 주기는 1.0_r8일로 설정한다. 극값 저장 뒤 초기화 수위는 최대 배열에 -10.0_r8, 최소 배열에 10.0_r8로 고정한다.
- 101·151–170: counter_loc_rl은 스칼라 intent(inout)이다. 셀마다 같은 스칼라를 검사하고 기록 주기 조건 안에서 값을 바꾼다. 초기값 설정은 이 파일에 없다.
- 155–188: 기록 수 NTIMES_MARSH를 MOD의 제수와 평균의 분모로 사용한다. 기록 배열은 매 셀에서 전체 NTIMES_MARSH 슬롯을 합산한다. 이 파일 안에 기록 수의 양수 검사나 채워진 슬롯 수만 선택하는 조건은 없다.
- 192: marsh_tidal_range를 자기 자신에 대입한다.
- 26·108·119·126–130: bc_r3d_tile을 USE하지만 호출하지 않는다. marsh_mask 인수는 실행식에서 참조하거나 갱신하지 않는다. iic_loc·counter_new_time·counter_loc·zeta_max2·zeta_min·tdays_marsh는 선언 이후 실행식에 등장하지 않는다.
