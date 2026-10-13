---
file: models/ROMS/raw/source_code/roms/ROMS/Nonlinear/Vegetation/vegetation_turb.F
lines: 261
sha256: 3b21ac51e018360a02148b5bdc4959f8077f78d74e16e274ff292b4ee53ed9b0
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# vegetation_turb.F — 판독 구간 기록

구간은 1행부터 261행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–41 | cppdefs.h를 포함하고 vegetation_turb_mod를 시작한다(1–2). VEGETATION과 VEG_TURB가 모두 정의되면 구현을 넣는다(4). gls_corstep.F용 식생 난류 운동 에너지(turbulent kinetic energy)와 길이 척도(length scale) 수정을 계산한다는 주석이다(13–14). Uittenbogaard 2003과 Warner 등 2005의 난류 폐쇄(turbulence closure) 문헌을 적는다(18–25). 상태 모듈을 가져오고 vegetation_turb를 공개한다(29–40). 조건·전처리 원문: `#include "cppdefs.h"` (1). `#if defined VEGETATION && defined VEG_TURB` (4). |
| 42–84 | 시작 시 전처리 `#if defined VEGETATION && defined VEG_TURB` (4) 안. vegetation_turb(ng,tile)은 mod_stepping을 가져오고 tile.h를 포함한다(43–57). PROFILE에서 wclock_on/off를 호출한다(59–61·78–80). vegetation_turb_tile에 nstp·nnew·u/v·종별 항력(vegetation drag)·plant·gls·tke·gls_veg·tke_veg를 전달한다(62–77). VEG_FLEX이면 bend를 전달한다(71–73). RETURN과 루틴 종료를 포함한다(82–84). 조건·전처리 원문: `# include "tile.h"` (57). `# ifdef PROFILE` (59). `# endif` (61). `# ifdef VEG_FLEX` (71). `# endif` (73). `# ifdef PROFILE` (78). `# endif` (80). |
| 85–133 | 시작 시 전처리 `#if defined VEGETATION && defined VEG_TURB` (4) 안. vegetation_turb_tile의 인수 목록과 선언이다(86–132). ASSUMED_SHAPE에서 gls·tke·gls_veg·tke_veg의 수직 하한을 0으로 지정한다(107–119). 명시 크기 분기에서 u/v의 마지막 크기는 nstp, 종별 항력의 마지막 크기는 NVEG, plant는 NVEG·NVEGP, bend는 NVEG이다(120–128). gls·tke는 0:N(ng)·nnew, 두 출력 배열은 0:N(ng)이다(129–132). 조건·전처리 원문: `# ifdef VEG_FLEX` (93). `# endif` (95). `# ifdef ASSUMED_SHAPE` (107). `# ifdef VEG_FLEX` (113). `# endif` (115). `# else` (120). `# ifdef VEG_FLEX` (126). `# endif` (128). `# endif` (133). |
| 134–175 | 시작 시 전처리 `#if defined VEGETATION && defined VEG_TURB` (4) 안. 시작 시 86행 vegetation_turb_tile 안. 상수 원문은 `real(r8), parameter :: one_half=1.0_r8/2.0_r8` (139); `real(r8), parameter :: one_third=1.0_r8/3.0_r8` (140); `real(r8), parameter :: Inival=0.0_r8` (141); `real(r8), parameter :: cl_veg=1.0_r8, ck=0.09_r8` (142); `real(r8), parameter :: max_L=10.0e10_r8` (143); `real(r8), parameter :: min_eps=1.0e-12_r8` (144); `real(r8), parameter :: max_eps=1.0e14_r8` (145). 지역 유속 작업·소산(dissipation)·고체 면적비(solidity)·와류(eddy) 길이·시간 척도(time scale)·종별 난류와 vegu/vegv 작업 배열을 선언한다(147–155). set_bounds.h를 포함한다(157). k=1..N(ng)-1·j/i 루프에서 tke_veg·gls_veg를 Inival로 초기화한다(163–170). 일반 길이 척도(generic length scale, GLS) 소산 지수는 `cff1=3.0_r8+gls_p(ng)/gls_n(ng)` (172); `cff2=1.5_r8+gls_m(ng)/gls_n(ng)` (173); `cff3=-1.0_r8/gls_n(ng)` (174). 조건·전처리 원문: `# include "set_bounds.h"` (157). |
| 176–200 | 시작 시 전처리 `#if defined VEGETATION && defined VEG_TURB` (4) 안. 시작 시 86행 타일 루틴 안. VEG_LOOP의 iveg=1..NVEG와 k=1..N(ng)-1·j/i 루프를 연다(176–179). 식생에 대한 흐름의 일이 추가 난류를 만든다는 주석이다(182–183). u 방향 네 위치의 항력과 유속 곱, 평균은 `wrku1=ru_loc_veg(i,j,k,iveg)*u(i,j,k,nstp)` (186); `wrku2=ru_loc_veg(i,j,k+1,iveg)*u(i,j,k+1,nstp)` (187); `wrku3=ru_loc_veg(i+1,j,k,iveg)*u(i+1,j,k,nstp)` (188); `wrku4=ru_loc_veg(i+1,j,k+1,iveg)*u(i+1,j,k+1,nstp)` (189); `wrku=0.25_r8*(wrku1+wrku2+wrku3+wrku4)` (190). v 방향은 `wrkv1=rv_loc_veg(i,j,k,iveg)*v(i,j,k,nstp)` (191); `wrkv2=rv_loc_veg(i,j,k+1,iveg)*v(i,j,k+1,nstp)` (192); `wrkv3=rv_loc_veg(i,j+1,k,iveg)*v(i,j+1,k,nstp)` (193); `wrkv4=rv_loc_veg(i,j+1,k+1,iveg)*v(i,j+1,k+1,nstp)` (194); `wrkv=0.25_r8*(wrkv1+wrkv2+wrkv3+wrkv4)` (195). 종별 난류 운동 에너지 생성은 `tke_loc_veg=sqrt(wrku*wrku+wrkv*wrkv)` (196). |
| 201–228 | 시작 시 전처리 `#if defined VEGETATION && defined VEG_TURB` (4) 안. 시작 시 86행 타일 루틴·176행 VEG_LOOP·177행 k 루프·178행 j 루프·179행 i 루프 안. GLS 소산 식은 `wrk=MAX(tke(i,j,k,nstp),gls_Kmin(ng))` (203); `dissip=(gls_cmu0(ng)**cff1)*(wrk**cff2)*                  &` (204); `&                 (gls(i,j,k,nstp)**cff3)` (205); `inverse_dissip=MAX( (1.0_r8/dissip), max_eps)` (207). 역소산의 min_eps 제한 대체식은 주석이다(206). 자유 난류 시간 척도는 `taufree=wrk*inverse_dissip` (211). 굽힘 식생의 수평 투영을 쓰는 VEG_FLEX/else와 식은 모두 주석이다(213·217–219·221). 활성 등가 두께(equivalent thickness)는 `eqvegT=plant(i,j,iveg,isThck)` (220). 고체 면적비는 `solid=plant(i,j,iveg,isDiam)*eqvegT*plant(i,j,iveg,isDens)` (227). |
| 229–261 | 시작 시 전처리 `#if defined VEGETATION && defined VEG_TURB` (4) 안. 시작 시 86행 타일 루틴·176행 VEG_LOOP·177행 k 루프·178행 j 루프·179행 i 루프 안. 식생 간격으로 제한한 와류 크기는 `L=cl_veg*((1.0_r8-MIN(solid,1.0_r8))/                     &` (231); `&                 plant(i,j,iveg,isDens))**one_half` (232); `L=MIN(L,max_L)` (233). 식생 사이 소산 시간 척도는 `cff2=MIN( (1.0_r8/(ck**2.0_r8*tke_loc_veg)), max_eps )` (237); `tauveg=(L**2.0_r8*cff2)**one_third` (238). 239행 직접 나눗셈 대체식은 주석이다. 유효 시간 척도와 GLS 추가 항은 `taueff=MIN(taufree,tauveg)` (243); `gls_loc_veg=gls_c2(ng)*tke_loc_veg/taueff` (244). 모든 종의 합산은 `tke_veg(i,j,k)=tke_loc_veg + tke_veg(i,j,k)` (250); `gls_veg(i,j,k)=gls_loc_veg + gls_veg(i,j,k)` (251). 네 루프·RETURN·타일 루틴·cpp 조건·모듈 종료와 빈 줄을 포함한다(253–261). 조건·전처리 원문: `#endif` (260). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 173·204–205·237: cff2는 루프 전에 GLS 소산 지수로 설정한다. 종/격자 루프 안에서 와류 시간 척도 계수로 다시 대입한다. 다음 반복의 dissip 식도 같은 cff2 변수를 사용한다.
- 206–207·145: inverse_dissip의 활성 식은 MAX(1/dissip,max_eps)이다. max_eps는 1.0e14_r8이다. min_eps로 분모를 제한하는 식은 주석이다.
- 71–73·93–95·114·127·213–221: VEG_FLEX이면 bend를 전달·선언한다. bend를 사용하는 두께 식은 주석이고 활성 eqvegT는 plant의 isThck를 복사한다.
- 144·154–155·163–251: min_eps·vegu·vegv는 선언 이후 활성 실행문에 사용되지 않는다.
- 118–119·131–132·163–177·250–251: 두 출력 배열은 수직 하한 0을 갖는다. 이 루틴의 초기화와 계산 루프는 1..N(ng)-1만 대입한다. 끝 인덱스 0과 N(ng)의 대입은 이 파일에 없다.
- 129–130·203–205: 명시 크기 gls·tke의 마지막 차원은 nnew이다. 활성 소산 식은 마지막 인덱스로 nstp를 사용한다.
- 172–174·207·231–244: gls_n·dissip·plant의 밀도·tke_loc_veg·taueff를 분모로 사용하는 식이 있다. 이 계산 루프에는 이 값들이 0인지 검사하는 IF 조건이 없다.
