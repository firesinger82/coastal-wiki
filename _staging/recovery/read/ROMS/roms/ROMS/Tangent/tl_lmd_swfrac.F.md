---
file: models/ROMS/raw/source_code/roms/ROMS/Tangent/tl_lmd_swfrac.F
lines: 104
sha256: dd3188a95ec217e9da4ea0fabaf4c5277b42640820ee26dd00a7c278209c2ed2
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# tl_lmd_swfrac.F — 판독 구간 기록

구간은 1행부터 104행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–42 | `#include "cppdefs.h"` (1)로 cppdefs.h를 포함한다. `#if defined TANGENT  && defined SOLVE3D       && \` (3); `(defined LMD_SKPP_NOT_YET \|\| defined SOLAR_SOURCE)` (4)이면 tl_lmd_swfrac_tile(ng,tile,경계,Zscale,Z,tl_Z,tl_swdk)을 정의한다(6–9). 저작권·MIT/X 라이선스·주석(10–42). 접선 선형(tangent linear) 태양 단파 플럭스(solar shortwave flux)의 깊이별 침투 비율을 Jerlov 수형(Jerlov water type)의 지수 감쇠(exponential decay)로 계산한다는 설명(18–20). Zscale은 깊이 배율, Z는 음의 수직 높이(m), tl_Z는 그 섭동, tl_swdk는 출력 감쇠 비율(24–32). Paulson and Simpson 1977·Bill Large 1995 코드 출처 주석(34–39). 빈 줄(2·5)도 포함한다. |
| 43–77 | 시작 시 6행 tl_lmd_swfrac_tile·3–4행 `#if defined TANGENT  && defined SOLVE3D       && \` (3); `(defined LMD_SKPP_NOT_YET \|\| defined SOLAR_SOURCE)` (4) 안. mod_param·mod_mixing·mod_scalars와 implicit none(43–47). ng/tile·배열/작업 경계 정수, Zscale 및 Z/tl_Z는 intent(in), tl_swdk는 intent(out)(51–60). Z/tl_Z/tl_swdk의 수평 크기는 IminS:ImaxS,JminS:JmaxS다. Jindex/i/j·cff1/cff2·tl_cff1/tl_cff2·fac1/fac2/fac3 선언(64–69). `# include "set_bounds.h"` (71)로 set_bounds.h를 포함한다. 두 파장 대역(two wavelength band) 태양 흡수 모델·Jwtype 범위 1:9 설명 주석(73–77). |
| 78–99 | 시작 시 6행 루틴·3–4행 `#if defined TANGENT  && defined SOLVE3D       && \` (3); `(defined LMD_SKPP_NOT_YET \|\| defined SOLAR_SOURCE)` (4) 안. j=Jstr:Jend·i=Istr:Iend 루프(78–79)에서 `Jindex=MAX(1, MIN(MIXING(ng)%Jwtype(i,j), 9))` (80)로 수형 인덱스를 1:9로 제한한다. 계수는 `fac1(i)=Zscale/lmd_mu1(Jindex)` (81); `fac2(i)=Zscale/lmd_mu2(Jindex)` (82); `fac3(i)=lmd_r1(Jindex)` (83). 첫 i 루프 종료(84), !!DIR$ VECTOR ALWAYS 주석(85). 같은 j 루프의 다음 i=Istr:Iend 루프(86)에서 `cff1=EXP(Z(i,j)*fac1(i))` (87); `tl_cff1=fac1(i)*tl_Z(i,j)*cff1` (88); `cff2=EXP(Z(i,j)*fac2(i))` (89); `tl_cff2=fac2(i)*tl_Z(i,j)*cff2` (90)로 두 지수 항과 접선 선형 항을 계산한다. !^의 비선형 swdk 식은 주석(91–93). 출력은 `tl_swdk(i,j)=tl_cff1*fac3(i)+                                 &` (94); `&                 tl_cff2*(1.0_r8-fac3(i))` (95). 두 루프 종료(96–97), RETURN·루틴 종료(98–99). 외부 루틴 호출은 없다. |
| 100–104 | 시작 시 3–4행 전처리 조건의 참 분기 안에서 `#else` (100)로 전환한다. 인수 없는 tl_lmd_swfrac(101)은 RETURN(102)만 수행하고 종료(103)한다. `#endif` (104)로 전처리 조건을 닫는다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6–9 및 100–103: 활성 전처리 분기는 tl_lmd_swfrac_tile을 정의한다. else 분기는 이름이 다른 인수 없는 tl_lmd_swfrac을 정의한다.
- 60·78–97: tl_swdk는 IminS:ImaxS,JminS:JmaxS 전체 작업 배열로 선언된다. 이 파일의 출력 대입 루프는 Istr:Iend,Jstr:Jend에만 값을 쓴다.
