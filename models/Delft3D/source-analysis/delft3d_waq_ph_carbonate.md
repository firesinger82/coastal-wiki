---
title: "Delft3D WAQ pH·탄산염계·해양산성화 source-analysis — phcarb.f90 (CO2 화학종 분배 + 방해석/아라고나이트 포화도 Ω)"
model: Delft3D
component: waq-process
canonical_source: self
citation_status: verified
verification_method: "Delft3D raw 직접 read: src/engines_gpl/waq/waq_process/phcarb.f90(456) — 해리상수(Roy1993/Dickson1990/Weiss1974/Mucci1983)·solvesaphe H+ 3단 fallback·화학종 분배·Ω 포화도 file:line 전수(2026-07-07). solvesaphe 모듈(Munhoven2013 SOLVE_ACBW_*)은 phcarb.f90 에 use 문 없이 호출 — 이 raw 트리서 정의파일 미검출(빌드 링크), 함수 시그니처만 확인."
note_author: "Claude Fable 5"
note_date: 2026-07-07
related:
  - models/Delft3D/source-analysis/delft3d_waq_process_library.md
  - models/Delft3D/source-analysis/delft3d_waq_sediment_oxygen_demand.md
  - models/Delft3D/source-analysis/delft3d_waq_algae_models.md
---

# Delft3D WAQ pH·탄산염계 — `phcarb.f90` (SUBROUTINE PHCARB)

> 소스: `.../src/engines_gpl/waq/waq_process/phcarb.f90` (456줄, `module m_phcarb` 단일 subroutine).
> **정체**: 전 무기탄소(TIC)–알칼리도(ALK)로부터 **pH·CO2(aq)·pCO2·HCO3⁻·CO3²⁻·붕산염·방해석/아라고나이트 포화도 Ω** 를 폐형 계산하는 **진단(diagnostic) process**. 연안·하구 **해양산성화(acidification)**·air-sea CO2 flux·패류/산호 서식환경 지표. 기존 WAQ 노트(DO·N·조류·SOD)가 비운 **탄소계 화학 공백**을 채움.

## 0. 진단 process — flux 없음
`fl`(flux 배열)을 전혀 갱신하지 않고 출력 14 포인터(IP7-14)에만 결과 기입(:421-434). 즉 상태변수 TIC/ALK 를 바꾸지 않는 **후처리 지표 산출** — 실제 탄소 소비/생산은 조류·무기화 process 몫. active + bottom 셀만 처리(`BTEST(IKNMRK(ISEG),0)`, :162).

## 1. 입력·전처리 (robust clamp)
입력 6: SAL·TIC(gC/m³)·ALKA(gHCO3/m³)·TEMP·PH_MIN·PH_MAX (:167-171). 방어적 clamp — TIC/ALKA<1e-30, SAL∈[1e-30, 50], T<0 K → 15℃ 세팅, 각 10회 경고 상한(:181-241). `PH_OLD` 는 직전 pH 를 solver 초기값으로 쓰려 읽되 범위 밖이면 7.0(:174-178).

단위 환산: 해수 밀도 `RHOH2O=(1000+0.7·S/(1−S/1000)−0.0061(T−4)²)/1000` (:340-341) → TIC/ALK 를 [mmol/kg soln]으로. 총붕소 `BT=0.000416·S/35`(Millero, :349), 칼슘 `Ca=0.01028·S/35`(:352).

## 2. 해리·용해도 상수 (T·S 의존, Total pH scale)
| 상수 | 식·출처 | 라인 |
|---|---|---|
| K_W | DOE1994/Zeebe-Wolf-Gladrow 2001 | :249-254 |
| K1·K2 | **Roy et al. 1993** — S<5(담수) / 5–45(해수) **분기**, +Millero1995 molality→[mol/kg soln] 보정 `+ln(1−S·0.001005)` | :256-303 |
| K_B(붕산) | Dickson 1990 | :306-313 |
| K_cal·K_arg | **Mucci 1983**/Millero1995 log₁₀ 다항 → 10^LOG | :315-335 |
| K0(CO2 용해도) | Weiss 1974 [mol/(kg·atm)] | :337-340 |

★S<5 vs ≥5 로 K1/K2 식 자체가 갈림(:256,283) — 하구 mixing zone 에서 염분이 이 경계를 넘나들면 상수 식이 스위칭.

## 3. H⁺ 해 — solvesaphe 3단 fallback (Munhoven 2013)
```fortran
CALL SETUP_API4PHTOT(TEMPK, SAL, 1.0D0)            ! :360 T·S 세팅
AHPLUS = SOLVE_ACBW_POLYFAST(ALK, TICM, BT)        ! :362 빠른 다항 solver
if (AHPLUS<0) AHPLUS = SOLVE_ACBW_POLY(...)        ! :365 실패 시 일반 다항
if (AHPLUS<0) AHPLUS = SOLVE_ACBW_GENERAL(...)     ! :368 그래도 실패 시 robust
PH = -log10(AHPLUS); PH = clamp(PH_MIN, PH_MAX)    ! :371-373
```
solvesaphe(Munhoven 2013, GMD) 의 alkalinity-기반 pH 솔버 — 수렴 실패 시 점진적으로 견고한 알고리즘으로 폴백.

## 4. 화학종 분배 + 포화도 Ω
공통 분모 `D = AHPLUS² + K1·AHPLUS + K1·K2`:
```
CO2  = TICM·AHPLUS²/D            (:378)
HCO3 = TICM·K1·AHPLUS/D          (:401)
CO3  = TICM·K1·K2/D              (:405)
BOH4 = BT·KB/(AHPLUS+KB)         (:411)
```
pCO2: 용해도 K0 로 fugacity `FCO2=(molCO2/K0)·1e6`(:385) → **virial 보정** `pCO2 = FCO2/exp(P_atm·(B_v+2Δ)/(R·T))`(Weiss1974 B_v :390, Dickson2007 :397).

**해양산성화 지표**:
```
Ω_calcite   Satcal = Ca·CO3/Kcal   (:415)
Ω_aragonite Satarg = Ca·CO3/Karg   (:418)
```
Ω<1 이면 그 광물이 용해 성향(패각·산호 스트레스) — 연안 산성화 평가 핵심 산출.

## 5. ★주요 findings
- **★진단 전용(flux 0)**: 탄소 수지를 안 바꾸고 지표만 산출 — TIC/ALK 자체는 별도 process(조류·무기화·air-sea exchange)가 구동. pH 를 예후변수로 착각 금지.
- **★PH_OLD 초기값이 solver 로 안 전달**: :174 에서 "good initial value for solvers" 라 읽지만, :362 `SOLVE_ACBW_POLYFAST(ALK,TICM,BT)` 호출 인자에 PH_OLD 없음 — 주석-코드 불일치, PH_OLD 사실상 사용 안 됨(polyfast 는 매 스텝 초기값 무관 해석적 해).
- **★S<5 담수 분기**: Roy1993 K1/K2 담수식(:258)이 별도 존재 — 순수 해양탄소계 코드(해수식만)와 달리 **하구·담수 적용 가능**. 단 경계 S=5 에서 상수 불연속 가능성.
- **염분 하드 clamp S≤50**(:212): 초염수(brine)·증발지 부적용.
- **solvesaphe 외부 의존**: `SOLVE_ACBW_*`/`SETUP_API4PHTOT` 는 phcarb 에 `use` 없이 링크(이 raw 트리서 정의 모듈 미검출) — Munhoven2013 phsolvers 별도 소스. 해 안정성은 이 외부 솔버에 위임.

## 6. Primary sources (코드 in-line 인용)
- **Roy et al. 1993**(K1/K2)·**Dickson 1990**(KB)·**Weiss 1974**(K0·virial)·**Mucci 1983**·Millero 1995(Ksp calcite/aragonite)·DOE1994/Zeebe-Wolf-Gladrow 2001(KW)·**Munhoven 2013**(solvesaphe, *Geosci. Model Dev.*) — 전부 phcarb.f90 주석 명시.
- Delft3D-WAQ Processes Library 정본: [[delft3d_waq_process_library]].

## 7. 관련
- [[delft3d_waq_process_library]] — process 호출 규약(IPOINT/INCREM/IKNMRK)·인접 kinetics
- [[delft3d_waq_sediment_oxygen_demand]] — 저층 탄소 diagenesis(메탄, 인접 탄소경로)
- [[delft3d_waq_algae_models]] — 조류 생산이 TIC/ALK 를 구동(본 진단의 상류)
