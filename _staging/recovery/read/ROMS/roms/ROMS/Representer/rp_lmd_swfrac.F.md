---
file: models/ROMS/raw/source_code/roms/ROMS/Representer/rp_lmd_swfrac.F
lines: 115
sha256: 64eebb328b8ad63a303c581a0d284142e7e47432d4dd3842a54fcc299f7745e0
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# rp_lmd_swfrac.F — 판독 구간 기록

구간은 1행부터 115행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–41 | cppdefs.h를 포함한다(1). TL_IOMS·SOLVE3D와 LMD_SKPP_NOT_YET 또는 SOLAR_SOURCE의 조합에서 rp_lmd_swfrac_tile을 정의한다(3–9). 주석은 대표자(representer) 접선 선형(tangent linear) 단파(shortwave) 투과율을 Jerlov 수질의 지수 감쇠로 계산한다고 적는다(18–20). Zscale은 깊이 배율이며 Z는 음의 수직 높이(m), tl_Z는 접선 선형 높이, tl_swdk는 출력 투과율이다(22–32). Paulson·Simpson(1977)과 Bill Large(1995) 코드 출처 주석 및 저작권 머리말을 포함한다(11–41). 원문: `#include "cppdefs.h"` (1); `#if defined TL_IOMS  && defined SOLVE3D       && \` (3); `(defined LMD_SKPP_NOT_YET \|\| defined SOLAR_SOURCE)` (4). |
| 42–77 | 시작 시 전처리 조건 3행 `#if defined TL_IOMS  && defined SOLVE3D       && \` / 4행 `(defined LMD_SKPP_NOT_YET \|\| defined SOLAR_SOURCE)` 안. 시작 시 6행 rp_lmd_swfrac_tile 루틴 안. mod_param·mod_mixing·mod_scalars를 사용한다(43–45). 입력 격자 범위·Zscale·Z·tl_Z와 출력 tl_swdk를 선언하고, 지역 계수·IminS:ImaxS 작업 배열을 선언한다(51–69). set_bounds.h를 포함한다(71). 주석은 두 파장대(wavelength band)의 흡수와 Jwtype 1..9를 적는다(73–76). 원문: `# include "set_bounds.h"` (71). |
| 78–85 | 시작 시 전처리 조건 3행 `#if defined TL_IOMS  && defined SOLVE3D       && \` / 4행 `(defined LMD_SKPP_NOT_YET \|\| defined SOLAR_SOURCE)` 안. 시작 시 6행 rp_lmd_swfrac_tile 루틴 안. j=Jstr..Jend, i=Istr..Iend에서 수질 인덱스를 1..9로 제한한다(78–80). fac1·fac2에는 각각 Zscale/lmd_mu1·Zscale/lmd_mu2, fac3에는 lmd_r1을 사용한다(81–83). i 루프를 닫고 벡터화 지시 주석을 둔다(84–85). 원문: `DO j=Jstr,Jend` (78); `DO i=Istr,Iend` (79); `Jindex=MAX(1, MIN(MIXING(ng)%Jwtype(i,j), 9))` (80); `fac1(i)=Zscale/lmd_mu1(Jindex)` (81); `fac2(i)=Zscale/lmd_mu2(Jindex)` (82); `fac3(i)=lmd_r1(Jindex)` (83). |
| 86–105 | 시작 시 전처리 조건 3행 `#if defined TL_IOMS  && defined SOLVE3D       && \` / 4행 `(defined LMD_SKPP_NOT_YET \|\| defined SOLAR_SOURCE)` 안. 시작 시 6행 rp_lmd_swfrac_tile 루틴·78행 j 루프 안. 두 파장대의 EXP 감쇠와 높이 변동 계수를 계산한다(86–96). TL_IOMS 분기는 각각 cff1·cff2의 보정항을 덧붙인다(89–96). 비선형 swdk 식은 주석이다(97–99). tl_swdk는 두 파장대의 접선 선형 값을 fac3과 1−fac3으로 가중한다(100–101). i/j 루프·루틴을 종료한다(102–105). 원문: `DO i=Istr,Iend` (86); `cff1=EXP(Z(i,j)*fac1(i))` (87); `tl_cff1=fac1(i)*tl_Z(i,j)*cff1+                               &` (88); `# ifdef TL_IOMS` (89); `&            cff1*(1.0_r8-Z(i,j)*fac1(i))` (90); `# endif` (91); `cff2=EXP(Z(i,j)*fac2(i))` (92); `tl_cff2=fac2(i)*tl_Z(i,j)*cff2+                               &` (93); `# ifdef TL_IOMS` (94); `&            cff2*(1.0_r8-Z(i,j)*fac2(i))` (95); `# endif` (96); `tl_swdk(i,j)=tl_cff1*fac3(i)+                                 &` (100); `&                 tl_cff2*(1.0_r8-fac3(i))` (101). |
| 106–115 | 시작 시 전처리 조건 3행 `#if defined TL_IOMS  && defined SOLVE3D       && \` / 4행 `(defined LMD_SKPP_NOT_YET \|\| defined SOLAR_SOURCE)` 안. 3행 전처리 조건의 대체 분기를 연다(106). rp_lmd_swfrac는 인수 없이 RETURN만 실행하는 루틴이다(107–109). 전처리 조건을 닫으며 마지막 빈 줄까지 포함한다(110–115). 원문: `#else` (106); `#endif` (110). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 80: Jwtype 입력은 MAX·MIN으로 1..9 범위에 제한한다.
- 3–4·88–96: 파일 외부 조건은 TL_IOMS를 요구하며, 같은 분기 내부에 TL_IOMS 보정항 조건을 다시 둔다.
