---
file: models/ROMS/raw/source_code/roms/ROMS/Adjoint/ad_lmd_swfrac.F
lines: 119
sha256: f1506f90566b2a251d90d63a02ce25095536e12114dec9a6f9d5e2bc74136bed
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# ad_lmd_swfrac.F — 판독 구간 기록

구간은 1행부터 119행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–42 | 시작 시 열린 전처리 조건 없음. cppdefs.h를 포함한다(1). ADJOINT·SOLVE3D와 LMD_SKPP_NOT_YET 또는 SOLAR_SOURCE의 전처리 조건 아래 ad_lmd_swfrac_tile을 선언한다(3–9). 머리말은 Jerlov 수형(Jerlov water type)의 지수 감쇠(exponential decay)로 지정 깊이에 도달하는 태양 단파 플럭스(solar shortwave flux) 비율의 수반을 계산한다고 설명한다(18–20). Zscale은 깊이 배율, Z는 음수인 높이이며 단위는 m이다(24–28). ad_swdk를 출력 수반 비율로 설명한다(30–32). Paulson·Simpson 1977 논문과 Bill Large 1995 코드에서 가져왔다는 주석이 있다(34–39). 조건·반복·대입·전처리 원문: `#include "cppdefs.h"` (1); `#if defined ADJOINT  && defined SOLVE3D       && \` (3); `(defined LMD_SKPP_NOT_YET \|\| defined SOLAR_SOURCE)` (4). |
| 43–71 | 시작 시 `#if defined ADJOINT  && defined SOLVE3D       && \` (3) `(defined LMD_SKPP_NOT_YET \|\| defined SOLAR_SOURCE)` (4) 안. 6행 ad_lmd_swfrac_tile 루틴 안. mod_param·mod_mixing·mod_scalars를 사용하고 implicit none을 적용한다(43–47). 정수 범위·Zscale·Z는 intent(in), ad_Z·ad_swdk는 intent(inout)이다(51–60). Z·수반 배열 범위는 IminS:ImaxS·JminS:JmaxS이다(57–60). 지역 Jindex·i·j·스칼라와 i방향 fac1·fac2·fac3 배열을 선언한다(64–69). set_bounds.h를 포함한다(71). 조건·반복·대입·전처리 원문: `# include "set_bounds.h"` (71). |
| 72–91 | 시작 시 `#if defined ADJOINT  && defined SOLVE3D       && \` (3) `(defined LMD_SKPP_NOT_YET \|\| defined SOLAR_SOURCE)` (4) 안. 6행 루틴 안. ad_cff1·ad_cff2를 0으로 초기화한다(77–78). 주석은 Paulson·Simpson의 두 파장 대역(two wavelength band) 흡수 모형이며 Jwtype 범위가 1:9라고 적는다(81–82). j=Jstr:Jend·i=Istr:Iend에서 Jindex를 1:9로 제한한다(85–87). fac1·fac2는 Zscale을 각 lmd_mu로 나눈 값이며 fac3는 lmd_r1 값이다(88–90). 첫 i 루프를 닫는다(91). 조건·반복·대입·전처리 원문: `ad_cff1=0.0_r8` (77); `ad_cff2=0.0_r8` (78); `DO j=Jstr,Jend` (85); `DO i=Istr,Iend` (86); `Jindex=MAX(1, MIN(MIXING(ng)%Jwtype(i,j), 9))` (87); `fac1(i)=Zscale/lmd_mu1(Jindex)` (88); `fac2(i)=Zscale/lmd_mu2(Jindex)` (89); `fac3(i)=lmd_r1(Jindex)` (90). |
| 92–119 | 시작 시 `#if defined ADJOINT  && defined SOLVE3D       && \` (3) `(defined LMD_SKPP_NOT_YET \|\| defined SOLAR_SOURCE)` (4) 안. 6행 루틴·85행 j 루프 안. 벡터화 지시문 형태의 `!!DIR$ VECTOR ALWAYS`는 주석이다(92). 두 번째 i 루프에서 cff1·cff2는 Z와 fac1·fac2의 곱에 EXP를 적용한 값이다(93–95). fac3 및 1−fac3로 ad_swdk를 두 스칼라 수반에 분배하고 ad_swdk를 0으로 만든다(99–101). 두 지수함수의 높이 수반 기여를 ad_Z에 합하고 스칼라 수반을 0으로 만든다(105–109). i·j 루프·RETURN·활성 루틴을 닫는다(110–113). 전처리 else는 이름이 ad_lmd_swfrac인 인수 없는 루틴이며 즉시 반환한다(114–117). endif·마지막 빈 줄이 이어진다(118–119). 조건·반복·대입·전처리 원문: `DO i=Istr,Iend` (93); `cff1=EXP(Z(i,j)*fac1(i))` (94); `cff2=EXP(Z(i,j)*fac2(i))` (95); `ad_cff1=ad_cff1+fac3(i)*ad_swdk(i,j)` (99); `ad_cff2=ad_cff2+(1.0_r8-fac3(i))*ad_swdk(i,j)` (100); `ad_swdk(i,j)=0.0_r8` (101); `ad_Z(i,j)=ad_Z(i,j)+                                          &` (105); `&              fac1(i)*cff1*ad_cff1+                               &` (106); `&              fac2(i)*cff2*ad_cff2` (107); `ad_cff2=0.0_r8` (108); `ad_cff1=0.0_r8` (109); `#else` (114); `#endif` (118). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 30–32·60·99–101: 머리말은 ad_swdk를 출력이라고 설명한다. 선언은 intent(inout)이다. 실행문은 들어온 ad_swdk를 ad_cff1·ad_cff2에 반영한 뒤 0으로 만든다.
- 82·87: 주석과 Jindex 제한식은 Jerlov 수형의 범위를 1:9로 고정한다. 범위를 벗어난 입력은 MAX·MIN으로 제한하며 이 블록에는 별도 범위 오류 보고가 없다.
- 6·113·115–117: 활성 분기 루틴 이름은 ad_lmd_swfrac_tile이다. 전처리 else의 즉시 반환 루틴 이름은 ad_lmd_swfrac이며 인수가 없다.
