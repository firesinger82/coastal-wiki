---
file: models/ROMS/raw/source_code/roms/ROMS/Utility/sum_imp.F
lines: 197
sha256: c0187ed252e176956248aa71366e6046235b3f054cc839b43e726ad8b1d2e3b9
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# sum_imp.F — 판독 구간 기록

구간은 1행부터 197행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | `#include "cppdefs.h"` (1)로 cppdefs.h를 포함한다. sum_imp_mod 시작(2). WEAK_CONSTRAINT와 RPCG가 모두 정의된 조건(3) 안에 저작권·implicit none·PRIVATE·sum_imp 공개·CONTAINS를 둔다(4–19). 원문 조건·루프·대입식·전처리: `#include "cppdefs.h"` (1); `#if defined WEAK_CONSTRAINT && defined RPCG` (3). |
| 20–39 | 시작 시 3행 `#if defined WEAK_CONSTRAINT && defined RPCG` 안. sum_imp 시작(20). mod_param·mod_ocean 사용(23·30). ADJUST_BOUNDARY에서 mod_boundary, ADJUST_STFLUX 또는 ADJUST_WSTRESS에서 mod_forces 사용(24–29). ng·tile·Lout 입력 선언(34). tile.h를 포함한다(38). 원문 조건·루프·대입식·전처리: `# ifdef ADJUST_BOUNDARY` (24); `# endif` (26); `# if defined ADJUST_STFLUX \|\| defined ADJUST_WSTRESS` (27); `# endif` (29); `# include "tile.h"` (38). |
| 40–62 | 시작 시 3행 `#if defined WEAK_CONSTRAINT && defined RPCG`·20행 sum_imp 안. sum_imp_tile에 공간 경계·Lout을 전달한다(40–58). SOLVE3D는 tl_t/u/v와 f_t/u/v, 그 외에는 tl_ubar/vbar와 f_ubar/vbar를 전달한다. tl_zeta·f_zeta는 공통이다. RETURN·루틴 종료·다음 구분 주석(59–62). 원문 조건·루프·대입식·전처리: `# ifdef SOLVE3D` (44); `# else` (51); `# endif` (56). |
| 63–86 | 시작 시 3행 `#if defined WEAK_CONSTRAINT && defined RPCG` 안. sum_imp_tile 시작과 전처리별 인수 선언(63–74). mod_param·mod_ncparam 사용(77–78). ng·tile·공간 경계·Lout 정수 입력 선언(82–85). 원문 조건·루프·대입식·전처리: `# ifdef SOLVE3D` (67); `# else` (70); `# endif` (73). |
| 87–120 | 시작 시 3행 `#if defined WEAK_CONSTRAINT && defined RPCG`·63행 sum_imp_tile 안. ASSUMED_SHAPE에서는 하한만 지정한 배열, else에서는 명시적 수평·수직·추적자 크기를 선언한다(87–119). 모든 배열은 intent(inout)이다. SOLVE3D의 tl_t는 N(ng)·시간 슬롯 3·NT(ng), tl_u/v는 N(ng)·시간 슬롯 2, f_t는 N(ng)·NT(ng), f_u/v는 N(ng) 크기이다(105–110). 2차원 tl_ubar/vbar·tl_zeta의 마지막 차원은 두 경로 모두 콜론이다. 원문 조건·루프·대입식·전처리: `# ifdef ASSUMED_SHAPE` (87); `#  ifdef SOLVE3D` (88); `#  else` (95); `#  endif` (100); `# else` (103); `#  ifdef SOLVE3D` (104); `#  else` (111); `#  endif` (116); `# endif` (119). |
| 121–137 | 시작 시 3행 `#if defined WEAK_CONSTRAINT && defined RPCG`·63행 sum_imp_tile 안. i·ib·ir·j·k와 SOLVE3D의 itrc 선언(123–126). set_bounds.h를 포함한다(128). 자유수면(free surface)은 j=JstrR:JendR·i=IstrR:IendR에서 f_zeta를 기존 tl_zeta의 Lout에 더한다(130–136). 원문 조건·루프·대입식·전처리: `# ifdef SOLVE3D` (124); `# endif` (126); `# include "set_bounds.h"` (128); `DO j=JstrR,JendR` (132); `DO i=IstrR,IendR` (133); `tl_zeta(i,j,Lout)=f_zeta(i,j)+tl_zeta(i,j,Lout)` (134). |
| 138–156 | 시작 시 3행 `#if defined WEAK_CONSTRAINT && defined RPCG`·63행 sum_imp_tile 안. SOLVE3D가 정의되지 않으면 2차원 운동량(momentum)을 합산한다(138–155). U는 j=JstrR:JendR·i=Istr:IendR의 f_ubar와 tl_ubar, V는 j=Jstr:JendR·i=IstrR:IendR의 f_vbar와 tl_vbar이다(142–154). 원문 조건·루프·대입식·전처리: `# ifndef SOLVE3D` (138); `DO j=JstrR,JendR` (142); `DO i=Istr,IendR` (143); `tl_ubar(i,j,Lout)=f_ubar(i,j)+tl_ubar(i,j,Lout)` (144); `DO j=Jstr,JendR` (150); `DO i=IstrR,IendR` (151); `tl_vbar(i,j,Lout)=f_vbar(i,j)+tl_vbar(i,j,Lout)` (152); `# endif` (155). |
| 157–179 | 시작 시 3행 `#if defined WEAK_CONSTRAINT && defined RPCG`·63행 sum_imp_tile 안. SOLVE3D에서 k=1:N(ng)의 3차원 속도 값을 합산한다(157–178). U는 j=JstrR:JendR·i=Istr:IendR의 f_u와 tl_u, V는 j=Jstr:JendR·i=IstrR:IendR의 f_v와 tl_v이다. 원문 조건·루프·대입식·전처리: `# ifdef SOLVE3D` (157); `DO k=1,N(ng)` (161); `DO j=JstrR,JendR` (162); `DO i=Istr,IendR` (163); `tl_u(i,j,k,Lout)=f_u(i,j,k)+tl_u(i,j,k,Lout)` (164); `DO k=1,N(ng)` (172); `DO j=Jstr,JendR` (173); `DO i=IstrR,IendR` (174); `tl_v(i,j,k,Lout)=f_v(i,j,k)+tl_v(i,j,k,Lout)` (175). |
| 180–197 | 시작 시 3행 `#if defined WEAK_CONSTRAINT && defined RPCG`·157행 `# ifdef SOLVE3D`·63행 sum_imp_tile 안. 추적자(tracer)는 itrc=1:NT(ng)·k=1:N(ng)·j=JstrR:JendR·i=IstrR:IendR의 f_t와 기존 tl_t의 Lout을 더한다(183–191). SOLVE3D 종료(192). RETURN·루틴 종료(194–195), 파일 최상위 조건 종료(196)·모듈 종료(197). 원문 조건·루프·대입식·전처리: `DO itrc=1,NT(ng)` (183); `DO k=1,N(ng)` (184); `DO j=JstrR,JendR` (185); `DO i=IstrR,IendR` (186); `tl_t(i,j,k,Lout,itrc)=f_t(i,j,k,itrc)+tl_t(i,j,k,Lout,itrc)` (187); `# endif` (192); `#endif` (196). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 24–29·40–58: mod_boundary·mod_forces를 조건부로 가져오지만 sum_imp_tile 호출에는 경계 배열이나 표면 응력·플럭스 배열을 전달하지 않는다.
- 123·132–191: 지역 정수 ib·ir는 선언 이후 실행문에서 사용되지 않는다.
- 92–118·134–187: f_zeta·f_ubar/vbar·f_u/v·f_t는 intent(inout)으로 선언되어 있다. 합산 실행문은 이 배열을 읽기만 한다.
