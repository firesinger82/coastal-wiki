---
file: models/ROMS/raw/source_code/roms/ROMS/Nonlinear/lmd_swfrac.F
lines: 91
sha256: 1dfd23657030e2c152b9a16a370c447fda70cf51d5b0c1d5c47f803fc22b1899
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# lmd_swfrac.F — 판독 구간 기록

구간은 1행부터 91행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–40 | 시작 시 열린 전처리 조건 없음. cppdefs.h를 포함한다(1). NONLINEAR·SOLVE3D와 LMD_SKPP 또는 SOLAR_SOURCE가 함께 정의될 때 lmd_swfrac_tile 루틴을 제공한다(3–9). MIT/X 머리말과 입력·출력·참고문헌 주석을 포함한다(11–39). 목적은 Jerlov 수형(Jerlov water type)의 지수 감쇠(exponential decay)로 특정 깊이에 침투한 태양 단파 플럭스(flux)(solar shortwave flux) 비율을 계산하는 것이다(18–20). Zscale은 깊이 배율이고 Z 입력 주석은 m 단위 음수 수직 높이다(24–26). 참고문헌은 Paulson·Simpson 1977이며 Bill Large 1995 코드에서 가져왔다고 적는다(34–37). 원문 조건·계산·전처리: `#include "cppdefs.h"` (1); `#if defined NONLINEAR && (defined LMD_SKPP \|\| defined SOLAR_SOURCE) && \` (3); `defined SOLVE3D` (4). |
| 41–65 | 시작 시 `#if defined NONLINEAR && (defined LMD_SKPP \|\| defined SOLAR_SOURCE) && \` (3) / `defined SOLVE3D` (4) 안. 시작 시 6행 lmd_swfrac_tile 루틴 안. mod_param·mod_mixing·mod_scalars를 가져온다(41–43). 격자·타일·작업 경계 인수, 입력 Zscale·Z와 출력 swdk를 선언한다(49–56). Jindex·i·j와 IminS:ImaxS의 fac1·fac2·fac3 작업 배열(work array)을 선언하고 set_bounds.h를 포함한다(60–64). 원문 조건·계산·전처리: `# include "set_bounds.h"` (64). |
| 66–85 | 시작 시 `#if defined NONLINEAR && (defined LMD_SKPP \|\| defined SOLAR_SOURCE) && \` (3) / `defined SOLVE3D` (4) 안. 시작 시 6행 lmd_swfrac_tile 루틴 안. 주석은 두 파장 대역(two wavelength bands)의 태양 흡수 모델과 Jwtype의 1:9 범위를 설명한다(67–68). j·i 루프에서 Jwtype을 1:9로 제한한다(71–73). fac1=Zscale/lmd_mu1·fac2=Zscale/lmd_mu2·fac3=lmd_r1을 수형별로 정한다(74–76). 다음 i 루프에서 두 지수항을 fac3와 1-fac3로 가중하여 swdk를 계산한다(79–81). VECTOR ALWAYS 줄은 이중 느낌표 주석이다(78). 루틴 종료까지 포함한다(82–85). 원문 조건·계산·전처리: `DO j=Jstr,Jend` (71); `DO i=Istr,Iend` (72); `Jindex=MAX(1, MIN(MIXING(ng)%Jwtype(i,j), 9))` (73); `fac1(i)=Zscale/lmd_mu1(Jindex)` (74); `fac2(i)=Zscale/lmd_mu2(Jindex)` (75); `fac3(i)=lmd_r1(Jindex)` (76); `DO i=Istr,Iend` (79); `swdk(i,j)=EXP(Z(i,j)*fac1(i))*fac3(i)+                        &` (80); `&              EXP(Z(i,j)*fac2(i))*(1.0_r8-fac3(i))` (81). |
| 86–91 | 시작 시 `#if defined NONLINEAR && (defined LMD_SKPP \|\| defined SOLAR_SOURCE) && \` (3) / `defined SOLVE3D` (4) 안. 시작 시 3–4행 전처리 조건 안. 86행 ELSE는 인수 없는 lmd_swfrac 루틴을 제공하며 RETURN만 실행한다(87–89). 전처리 조건을 닫고 마지막 빈 줄까지 포함한다(90–91). 원문 조건·계산·전처리: `#else` (86); `#endif` (90). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 3–4·6·86–89: 계산 루틴의 전처리 조건은 LMD_SKPP 또는 SOLAR_SOURCE를 요구한다. 이 조건에는 LMD_BKPP가 없다. else의 빈 루틴 이름은 lmd_swfrac이며 계산 루틴 이름 lmd_swfrac_tile과 다르다.
