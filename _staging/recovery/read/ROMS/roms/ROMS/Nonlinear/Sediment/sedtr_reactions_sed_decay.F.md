---
file: models/ROMS/raw/source_code/roms/ROMS/Nonlinear/Sediment/sedtr_reactions_sed_decay.F
lines: 248
sha256: 3b489999e765eae512471b6873ccde6ca06a3d384935b0e8ff4412b98e0a3967
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# sedtr_reactions_sed_decay.F — 판독 구간 기록

구간은 1행부터 248행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–48 | 파일 내부에서 열린 전처리 조건 없음. `#include "cppdefs.h"` (1)로 cppdefs.h 포함, MODULE sedtr_reactions_sed_decay_mod(3). `#if defined NONLINEAR && defined SEDIMENT  && defined SEDTR_REACTIONS \` (5); `                     && defined SEDTR_SED_DECAY` (6). 저작권·MIT/X 주석(8–13). 입자·입자 부착 물질의 반응항(reaction term), Soetaert 계열 구현과 Moriarty 등 2017 문헌(15–25). 입자성 유기물(particulate organic matter, POM), 영양염·산소 요구량 단위(oxygen demand unit, ODU), 재광물화(remineralization)·질산화(nitrification)·탈질(denitrification), 공극률(porosity) 변화 무시라는 머리말(27–37). implicit none·PRIVATE·공개 sedtr_reactions_sed_decay·CONTAINS(41–46), 주석·빈 줄(47–48). 기능 설명은 머리말 주석으로 구분한다. |
| 49–83 | 시작 시 5행 `#if defined NONLINEAR && defined SEDIMENT  && defined SEDTR_REACTIONS \`·6행 `                     && defined SEDTR_SED_DECAY` 안. sedtr_reactions_sed_decay(ng,tile) 선언(49), mod_param/forces/grid/ocean/sedbed/stepping 사용(52–57), 정수 인수(61). `# include "tile.h"` (65)로 tile.h 포함. `# ifdef PROFILE` (67)에서 `wclock_on`에 ng·iNLM·16 전달(68), `# endif` (69). `sedtr_reactions_sed_decay_tile`에 타일·작업 경계·nstp/nnew·OCEAN%t·SEDBED%bed_mass/bed_frac/bed 전달(70–77). `# ifdef PROFILE` (78)에서 `wclock_off` 호출(79), `# endif` (80). RETURN·wrapper 종료·주석(81–83). |
| 84–120 | 시작 시 5행 `#if defined NONLINEAR && defined SEDIMENT  && defined SEDTR_REACTIONS \`·6행 `                     && defined SEDTR_SED_DECAY` 안. sedtr_reactions_sed_decay_tile 선언(85–90), mod_param/scalars/sediment, bc_r3d_tile·exchange_r2d_tile 사용(93–98). `# ifdef DISTRIBUTE` (99)에서 mp_exchange3d·mp_exchange4d USE(100), `# endif` (101). ng/tile·타일 및 작업 경계·nstp/nnew 선언(105–108). `# ifdef ASSUMED_SHAPE` (110)은 열린 상한 t·bed_mass·bed_frac·bed(111–114), `# else` (115)는 t=(...,N(ng),3,NT(ng)), bed_mass=(...,Nbed,1:2,NST), bed_frac=(...,Nbed,NST), bed=(...,Nbed,MBEDP)(116–119), `# endif` (120). |
| 121–147 | 시작 시 5행 `#if defined NONLINEAR && defined SEDIMENT  && defined SEDTR_REACTIONS \`·6행 `                     && defined SEDTR_SED_DECAY` 안, 85행 tile 루틴 안. i/ised/j/k(124), `real(r8), parameter :: eps = 1.0E-14_r8` (126), `real(r8), parameter :: zeros = 0.0_r8` (127), `real(r8), parameter :: ones = 1.0_r8` (128). cff·oc(NST)·docdt(NST)·rem 선언(129–133). `real(r8) :: r_om=0.15_r8             !ratio mol N: mol C for POM` (136), `real(r8) :: kg2mmolC = 1000.0_r8/12.0107_r8 !ratio of` (137), 단위 주석(138–139). `# include "set_bounds.h"` (140)로 set_bounds.h 포함, POM·퇴적층 질량 갱신 구분 주석(142–147), 빈 줄 포함. |
| 148–188 | 시작 시 5행 `#if defined NONLINEAR && defined SEDIMENT  && defined SEDTR_REACTIONS \`·6행 `                     && defined SEDTR_SED_DECAY` 안, 85행 tile 루틴 안. `J_LOOP : DO j=Jstr,Jend` (148), `I_LOOP : DO i=Istr,Iend` (149), `K_LOOP : DO k=1,Nbed` (150). Soetaert 단위 변환 주석(153–160). `DO ised=1,NST` (162), `IF (sed_rxn(ised,ng).ne.0.0_r8) THEN` (164). `                rem=(sed_rxn(ised,ng)                                   &` (168), `# ifdef SEDBIO_POM_TVAR` (169) 아래 `     &            + 1.0_r8**(t(i,j,1,nstp,itemp)-20.0_r8)               &` (170), `# endif` (171), `     &            )/24.0_r8/3600.0_r8` (172). `docdt(ised) = 0.0_r8 + bed_mass(i,j,k,nnew,ised)*rem` (173). `                bed_mass(i,j,k,nnew,ised) = MAX(0.0_r8,                 &` (176); `     &             bed_mass(i,j,k,nnew,ised) - dt(ng)*docdt(ised))` (177). `                t(i,j,k,nnew,ised) = MAX(0.0_r8,                 &` (178); `     &             t(i,j,k,nnew,ised)*(1.0_r8 - dt(ng)*rem))` (179). 두 값은 하한 0.0_r8로 제한. ELSE·oc·질량 자기 대입은 주석(183–185). IF 종료(186), ised 루프 종료(188), 빈 줄 포함. |
| 189–210 | 시작 시 5행 `#if defined NONLINEAR && defined SEDIMENT  && defined SEDTR_REACTIONS \`·6행 `                     && defined SEDTR_SED_DECAY` 안, 85행 tile 루틴·148행 j·149행 i·150행 k 루프 안. 퇴적층 속성 갱신 주석(190–194), 두께·cff=0 초기화(195–196). `DO ised=1,NST` (197), `cff=cff+bed_mass(i,j,k,nnew,ised)` (198), 루프 종료(199), `cff=MAX(eps,cff)` (200). `DO ised=1,NST` (201), `bed_frac(i,j,k,ised)=bed_mass(i,j,k,nnew,ised)/cff` (202). 두께 누적식 원문은 `              bed(i,j,k,ithck)=bed(i,j,k,ithck)+                        &` (203); `     &            bed_mass(i,j,k,nnew,ised)/(Srho(ised,ng)*             &` (204); `     &            (ones-bed(i,j,k,iporo)))  ` (205). ised·k·i·j 루프 종료(206·208–210), 빈 줄 포함. cff 하한은 eps=1.0E-14_r8이며 공극률은 기존 값을 사용. |
| 211–248 | 시작 시 5행 `#if defined NONLINEAR && defined SEDIMENT  && defined SEDTR_REACTIONS \`·6행 `                     && defined SEDTR_SED_DECAY` 안, 85행 tile 루틴 안, 공간 루프 밖. 경계 조건(boundary condition) 구분 주석(212–214). ised=1..NST에서 `bc_r3d_tile`에 층 1..Nbed·bed_frac(:,:,:,ised)와 bed_mass(:,:,:,nnew,ised) 전달(216–223). `# ifdef DISTRIBUTE` (224)에서 `mp_exchange4d`에 배열 수 2·층 1..Nbed·입도 1..NST·NghostPoints·EWperiodic/NSperiodic·bed_frac·bed_mass의 nnew 슬라이스 전달(225–230), `# endif` (231). i=1..MBEDP에서 `bc_r3d_tile`에 bed(:,:,:,i) 전달(233–237). `# ifdef DISTRIBUTE` (238)에서 `mp_exchange4d`에 배열 수 1·층 1..Nbed·속성 1..MBEDP·bed 전달(239–243), `# endif` (244). RETURN·tile 루틴 종료(245–246), `#endif` (247), MODULE 종료(248). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 169–172: SEDBIO_POM_TVAR의 실행 항은 밑이 1.0_r8인 온도 차 거듭제곱이다. 이 항을 sed_rxn에 더한다.
- 116·150·178–179: t의 수직 차원은 N(ng)이다. t 갱신의 k 루프는 Nbed까지 돈다. 마지막 인덱스는 ised를 직접 사용하며, 이 대입에 추적자 매핑 인덱스는 없다.
- 131·136–139·168–179: oc·r_om·kg2mmolC는 선언 후 실행식에서 참조되지 않는다. docdt는 단위 변환 주석과 함께 놓여 있으나 실행식은 bed_mass*rem이며 해당 변환 계수를 사용하지 않는다.
- 98–100·216–243: exchange_r2d_tile·mp_exchange3d를 USE하지만 이 파일에서 호출하지 않는다.
- 178–179·216–243: t 갱신문이 있다. 이후 경계 조건·병렬 교환은 bed_frac·bed_mass·bed에 적용하며 t를 인수로 전달하는 호출은 이 파일에 없다.
