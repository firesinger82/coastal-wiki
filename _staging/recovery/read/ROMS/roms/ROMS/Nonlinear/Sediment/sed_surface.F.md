---
file: models/ROMS/raw/source_code/roms/ROMS/Nonlinear/Sediment/sed_surface.F
lines: 156
sha256: fd1bb0056478e63051a239701e58e92e7da75e29db18a48e58d0f4f3bc068907
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# sed_surface.F — 판독 구간 기록

구간은 1행부터 156행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–32 | 시작 시 열린 전처리 블록 없음. `cppdefs.h`를 포함하고 모듈을 연다(1–3). NONLINEAR·SEDIMENT 조건의 구현이다(5). 저작권·MIT/X 라이선스·저질과 물 사이의 표면층 속성(surface layer properties) 목적·Warner(2008) 문헌 주석(7–24). implicit none·PRIVATE·공개 sed_surface·CONTAINS(26–31)와 구분 주석·빈 줄을 포함한다. 원문 조건·계산식·호출·전처리(이어지는 줄도 각각 인용): `#include "cppdefs.h"` (1); `#if defined NONLINEAR && defined SEDIMENT` (5). |
| 33–68 | 시작 시 열린 전처리 블록: `#if defined NONLINEAR && defined SEDIMENT` (5) 안. 시작 시 3행 모듈 안. sed_surface(ng,tile) 진입점, 모델 매개변수·수주·저질·시간 모듈 사용문과 정수·MyFile 선언(34–49). `tile.h`를 포함한다(51). PROFILE의 wclock_on/off 호출(53–55·62–64). sed_surface_tile에 경계·작업 범위·시간 인덱스·bed_frac·bottom을 넘긴다(56–61). RETURN·진입점 종료(66–67), 주석·빈 줄을 포함한다. 원문 조건·계산식·호출·전처리(이어지는 줄도 각각 인용): `      character (len=*), parameter :: MyFile =                          &` (48); `     &  __FILE__` (49); `# include "tile.h"` (51); `# ifdef PROFILE` (53); `      CALL wclock_on (ng, iNLM, 16, __LINE__, MyFile)` (54); `# endif` (55); `      CALL sed_surface_tile (ng, tile,                                  &` (56); `     &                       LBi, UBi, LBj, UBj,                        &` (57); `     &                       IminS, ImaxS, JminS, JmaxS,                &` (58); `     &                       nstp(ng), nnew(ng),                        &` (59); `     &                       SEDBED(ng) % bed_frac,                     &` (60); `     &                       SEDBED(ng) % bottom)` (61); `# ifdef PROFILE` (62); `      CALL wclock_off (ng, iNLM, 16, __LINE__, MyFile)` (63); `# endif` (64). |
| 69–100 | 시작 시 열린 전처리 블록: `#if defined NONLINEAR && defined SEDIMENT` (5) 안. 시작 시 3행 모듈 안. sed_surface_tile 인수 목록(70–74), 매개변수·상수·퇴적물 모듈과 bc_r3d_tile 사용문(77–81). DISTRIBUTE에서는 mp_exchange3d/mp_exchange4d를 가져온다(82–84). 정수 인수·ASSUMED_SHAPE 및 고정 크기 bed_frac/bottom intent(inout) 배열 선언(88–99). 구분 주석·빈 줄을 포함한다. 원문 조건·계산식·호출·전처리(이어지는 줄도 각각 인용): `     &                             LBi, UBi, LBj, UBj,                  &` (71); `     &                             IminS, ImaxS, JminS, JmaxS,          &` (72); `     &                             nstp, nnew,                          &` (73); `     &                             bed_frac, bottom)` (74); `# ifdef DISTRIBUTE` (82); `# endif` (84); `# ifdef ASSUMED_SHAPE` (93); `# else` (96); `# endif` (99). |
| 101–114 | 시작 시 열린 전처리 블록: `#if defined NONLINEAR && defined SEDIMENT` (5) 안. 시작 시 70행 sed_surface_tile 안. i/ised/j·cff1/2/3/4 및 eps=1.0E-14 선언(103–106). `set_bounds.h`를 포함한다(108). 표층 평균 속성과 BBL(bottom boundary layer)의 양의 Sd50 및 Srho>1000 요구에 관한 원문 주석(111–113), 빈 줄을 포함한다. 원문 조건·계산식·호출·전처리(이어지는 줄도 각각 인용): `      real(r8), parameter :: eps = 1.0E-14_r8` (106); `# include "set_bounds.h"` (108). |
| 115–136 | 시작 시 열린 전처리 블록: `#if defined NONLINEAR && defined SEDIMENT` (5) 안. 시작 시 70행 sed_surface_tile 안. J_LOOP·i 루프에서 네 누적값을 1로 시작한다(115–120). 클래스별 표층 bed_frac를 지수로 쓰는 곱으로 임계 응력(critical shear stress)·중앙입경(median grain size)·침강속도(settling velocity)·밀도의 기하평균(geometric mean)을 계산한다(121–126). 침강속도 밑에는 eps를 더한다(124). bottom itauc/iwsed에 값을 복사하고 isd50은 Zob 이하, idens는 1050 이상으로 제한한다(127–130). 루프 종료(131–132), 저질 거칠기(bed roughness) 계산 이동에 관한 주석(133–135)과 빈 줄을 포함한다. 원문 조건·계산식·호출·전처리(이어지는 줄도 각각 인용): `      J_LOOP : DO j=Jstr,Jend` (115); `        DO i=Istr,Iend` (116); `          cff1=1.0_r8` (117); `          cff2=1.0_r8` (118); `          cff3=1.0_r8` (119); `          cff4=1.0_r8` (120); `          DO ised=1,NST` (121); `            cff1=cff1*tau_ce(ised,ng)**bed_frac(i,j,1,ised)` (122); `            cff2=cff2*Sd50(ised,ng)**bed_frac(i,j,1,ised)` (123); `            cff3=cff3*(wsed(ised,ng)+eps)**bed_frac(i,j,1,ised)` (124); `            cff4=cff4*Srho(ised,ng)**bed_frac(i,j,1,ised)` (125); `          bottom(i,j,itauc)=cff1` (127); `          bottom(i,j,isd50)=MIN(cff2,Zob(ng))` (128); `          bottom(i,j,iwsed)=cff3` (129); `          bottom(i,j,idens)=MAX(cff4,1050.0_r8)` (130). |
| 137–156 | 시작 시 열린 전처리 블록: `#if defined NONLINEAR && defined SEDIMENT` (5) 안. 시작 시 70행 sed_surface_tile 안이며 셀 루프 밖. bottom의 모든 MBOTP 속성에 bc_r3d_tile로 경계조건(boundary condition)을 적용한다(142–144). DISTRIBUTE이면 NghostPoints·주기 조건과 함께 mp_exchange3d를 호출한다(145–151). RETURN·tile 루틴 종료·전체 #endif·모듈 종료(153–156)와 경계 설명 주석을 포함한다. 원문 조건·계산식·호출·전처리(이어지는 줄도 각각 인용): `      CALL bc_r3d_tile (ng, tile,                                       &` (142); `     &                  LBi, UBi, LBj, UBj, 1, MBOTP,                   &` (143); `     &                  bottom)` (144); `# ifdef DISTRIBUTE` (145); `      CALL mp_exchange3d (ng, tile, iNLM, 1,                            &` (146); `     &                    LBi, UBi, LBj, UBj, 1, MBOTP,                 &` (147); `     &                    NghostPoints,                                 &` (148); `     &                    EWperiodic(ng), NSperiodic(ng),               &` (149); `     &                    bottom)` (150); `# endif` (151); `#endif` (155). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 91·115–151: nstp와 nnew는 입력으로 선언하지만 계산에서 사용하지 않는다. bed_frac는 intent(inout)이지만 이 루틴에서는 읽기만 한다.
- 83·145–150: DISTRIBUTE 사용문은 mp_exchange3d와 mp_exchange4d를 가져온다. 실행문은 mp_exchange3d만 호출한다.
- 121–130: 표층 클래스 비율을 지수로 쓰는 곱을 계산한다. 이 파일에는 클래스 비율의 합을 검사하거나 다시 정규화하는 문장이 없다.
- 112–113·128·130: Sd50이 양수이고 Srho>1000이어야 한다는 주석이 있다. 실제 표면 속성 대입의 입경 한계는 MIN(cff2,Zob(ng)), 밀도 하한은 1050이다. 입경 대입에 명시적인 양의 하한은 없다.
- 133–135: 저질 거칠기 계산을 BBL 루틴에서 여기로 옮긴다는 주석이 있다. 이 파일의 실행 대입 대상 bottom 속성은 itauc/isd50/iwsed/idens의 네 개이다.
