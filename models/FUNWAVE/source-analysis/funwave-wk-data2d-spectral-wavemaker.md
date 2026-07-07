---
title: "FUNWAVE-TVD 2D 방향스펙트럼 조파 source-analysis — WK_DATA2D (SWAN→Boussinesq nesting: 내부소스 vs ABS 경계)"
topic: funwave-wk-data2d-spectral-wavemaker
canonical_source: self
citation_status: verified
verification_method: "FUNWAVE-TVD raw source 직접 read: src/wavemaker.F(3299)+sources.F+sponge.F — Wei-Kirby D_gen(:803)·±60° directional cull(:239) file:line 직접 검증. 소스주석 primary Wei-Kirby(:824)·Salatin2021(sponge.F:103). [[funwave-physics-sources]]:26,29 는 1줄 표만."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-07-07
verification_by: "Claude Opus 4.8 (1M context) — wavemaker.F:238-246·801-805 직접 read 검증"
verification_date: 2026-07-07
related:
  - models/FUNWAVE/source-analysis/funwave-physics-sources.md
  - models/FUNWAVE/source-analysis/funwave-dispersion-solver.md
  - concepts/waves/06-model-application.md
---

# FUNWAVE-TVD 2D 방향스펙트럼 조파 — `WK_DATA2D` (SWAN nesting)

> 소스: [`src/wavemaker.F`](../raw/source_code/FUNWAVE-TVD/src/wavemaker.F)(3299) + `sources.F`(:150-165) + `sponge.F`(:77-156).
> **정체**: **SWAN → Boussinesq 스펙트럼 nesting** — 2D 방향스펙트럼(NumFreq×NumDir)을 FUNWAVE 조파원으로. 정온도·항내 정밀([[concepts/waves/06-model-application]] harbor tranquility)의 광역→위상해상 연결 핵심. [[funwave-physics-sources]]:26,29 는 1줄 표만(식 無).
> **2 경로**: (A) **내부소스** `WK_WAVEMAKER_2D_SPECTRAL_DATA`→`CALCULATE_Cm_Sm` / (B) **absorbing-generating 경계** `CALCULATE_DATA2D_Cm_Sm`→`ABSORBING_GENERATING_BC`.

## 0. 구조
| 서브루틴 | 라인 | 역할 |
|---|---|---|
| WK_DATA2D reader | wavemaker.F:196-340 | WaveCompFile 읽기(NumFreq/NumDir/PeakPeriod/freq·dir축/WAVE_COMP 2D진폭/opt Phase2D) + direction cull |
| `WK_WAVEMAKER_2D_SPECTRAL_DATA` | :627-819 | 성분별 fully-dispersive wavenumber + Wei-Kirby `D_gen` + Gaussian width |
| `CALCULATE_Cm_Sm` | :831-891 | 공간 source 배열 `Cm/Sm` 조립 |
| `CALCULATE_DATA2D_Cm_Sm` | :903-1042 | 경계경로: Airy Newton + `Cm_eta/Sm_eta/Cm_u/Sm_u/Cm_v/Sm_v` |
| apply(내부소스) | sources.F:150-165 | `WaveMaker_Mass=Σ AA(Cm·cosωt+Sm·sinωt)`, ramp `AA=tanh` |
| `ABSORBING_GENERATING_BC` | sponge.F:77-156 | Ein2D/Uin2D/Vin2D 재구성 + tide relaxation |

## 1. 스펙트럼 입력 + ★±60° cull (:196-340)
```fortran
READ(1,*) NumFreq,NumDir ; PeakPeriod ; freq[]; dir[]; WAVE_COMP(J,I); opt Phase2D   ! :198-215
IF( ABS(Dire(I)) < 60.0 ) 채택 else 폐기   ! :239 ★±60° 밖 성분 무음 제거("bad from SWAN")
Phase2D = Phase2D*(π/180)                  ! :299 도→rad
```

## 2. 내부소스 경로 (A)
```fortran
! Nwogu α=-0.39 fully-dispersive wavenumber:
alpha1=α+1/3 ; tb=ω²h/g ; tc=1+tb·α ; wkn=√((tc-√(tc²-4α1·tb))/(2α1))/h   ! :774-793
! Wei-Kirby 내부소스 진폭:
D_gen = 2·AMP_WK·cosθ·(ω²-α1·g·k⁴h³)/(ω·k·rI·(1-α(kh)²))                    ! :803-805
rlamda=k·sinθ ; beta_gen=80/δ²/L² ; rI=√(π/beta)·exp(-rl_gen²/4beta)       ! :798-801, width=δL/2 :810
! 공간 조립:
Cm(i,j,kf)=Σ_θ D_gen·exp(-beta·(x-Xc)²)·cos(rlamda·y+φ)  ; Sm=sin         ! :874-882
! 시간적분(sources.F):
WaveMaker_Mass = Σ AA·(Cm·cosωt + Sm·sinωt) ; AA=tanh(π·FreqPeak·t/Time_ramp)  ! sources.F:151-163
```

## 3. 경계 경로 (B)
```fortran
! ★Airy(선형) 분산 Newton — 내부소스의 fully-dispersive 와 다름:
Fk=g·k·tanh(kh)-σ² ; k←k-Fk/Fkdif ; |Fk|≤1e-8 or Iter>1000   ! :937-943
Cm_eta=Σ_dir Amp·cos(k·sinθ·Y+k·cosθ·X) ; Sm_eta=sin          ! :1004-1009
Cm_u=Σ Amp·σ·cosh(k·Zlev)/sinh(kh)·cosθ·cos(...) ; Zlev=|1+Beta_ref|·Dep_Ser   ! :960,1010-1033
! sponge.F: Ein2D=Σ(Cm_eta·cos+Sm_eta·sin); Eta=Ein2D+(Eta-Ein2D)·SPONGE_TIDE_WEST  :115-140
```

## 4. 주요 findings (code≠manual/intent)
- **★±60° directional cull 하드코딩**(:239) — |dir|≥60° 성분을 무음 제거(입력 파라미터 아님). 사각입사 SWAN 에너지 소실.
- **★두 경로 분산관계 상이**: 내부소스=fully-dispersive Nwogu(α=-0.39, :792), 경계=선형 Airy(:937). **동일 스펙트럼이 경로 선택에 따라 다른 wavenumber**.
- **★생성경계가 η만 강제**(속도 relaxation 주석처리 sponge.F:142-143), Cm_u/Sm_u 는 계산되나 미사용 → 배열이 암시하는 full η+velocity ABS-gen BC 아니라 elevation-forced.
- **위상 처리 경로간 불일치**: 내부소스는 Phase2D 적용(:295-316), 경계는 `+Phase_Ser` 주석처리(sponge.F:113) → σt 만.
- **random-phase fallback**(:303-315, phase block 없으면 `rand()·2π`) — 비결정·컴파일러 의존(재현성 깨짐).
- **속도 평가 준위 = Nwogu reference depth**(`Zlev=|1+Beta_ref|·Dep_Ser`:960) — "depth-averaged" 단순해석과 다름.

## 5. Primary sources
- **Wei, Kirby, Grilli & Subramanya 1995 / Wei-Kirby 1999** — 내부소스 wavemaker(`D_gen` 폐형 §2, 소스주석 :824).
- **Chen et al. 2000** — fully nonlinear Boussinesq(Nwogu α=-0.39 §2).
- **Shi et al. 2012** *Ocean Modelling* 43-44 — FUNWAVE-TVD reference(source function + ABS-gen BC).
- **Salatin et al. 2021** JGR-Oceans e2021JC017641 — WK_NEW_DATA2D·ABS-gen 가속(소스 in-code sponge.F:103).

## 6. 관련
- [[funwave-physics-sources]] — wavemaker/breaker/sponge 개괄(본 노트가 WK_DATA2D 심화, :26/29 표)
- [[funwave-dispersion-solver]] — Boussinesq 분산항(내부소스 fully-dispersive 와 동류 α)
- [`concepts/waves/06-model-application.md`](../../../concepts/waves/06-model-application.md) — 정온도 SWAN→Boussinesq nesting(WK_DATA2D 가 그 연결)
