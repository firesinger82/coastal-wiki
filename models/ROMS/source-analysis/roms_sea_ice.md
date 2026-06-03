---
title: "ROMS sea-ice 모델(Budgell) — thermodynamics(Mellor-Kantha ice_mk.h: 성장/소멸·frazil·albedo) + EVP dynamics(Elastic-Viscous-Plastic rheology Hunke-Dukowicz) + Smolarkiewicz ice advection + ice-ocean stress/brine"
topic: roms
canonical_source: self
citation_status: verified
verification_method: "models/ROMS/raw/source_code/roms/ROMS/Nonlinear/SeaIce/ 직접 read — 파일 인벤토리(7682 라인: ice_thermo.F/ice_mk.h Mellor-Kantha + ice_evp.F EVP + ice_advect/ice_smolar.h Smolarkiewicz + ice_frazil/enthalpy/albedo + ice_spdiw ice-water stress + BC ice_tibc/uibc/vibc) + 헤더(Paul Budgell, MIT/X, ICE_MODEL/ICE_THERMO/ICE_MOMENTUM CPP) file:line 인용."
note_author: "Claude Opus 4.8 (1M context) source-code direct read"
note_date: 2026-06-03
verification_by: "Claude Opus 4.8 (1M context) — 해빙 thermodynamics/EVP dynamics/advection 구조 verbatim"
verification_date: 2026-06-03
related:
  - models/ROMS/source-analysis/roms_bulk_flux_coare.md
  - models/ROMS/source-analysis/roms_baroclinic_3d.md
  - models/ROMS/source-analysis/roms_advection.md
---

# ROMS sea-ice 모델 (Budgell)

> `ROMS/Nonlinear/SeaIce/`(7682 라인) 직접 read. ROMS 의 **동적-열역학 해빙(sea-ice) 모델** (W. Paul Budgell 2002-2026, MIT/X license, ROMS Group). `ICE_MODEL` CPP 활성. thermodynamics(성장/소멸) + dynamics(EVP rheology) + 해빙-해양 결합(stress·brine). 고위도 해역용 — 한국 연안엔 비핵심이나 ROMS 의 완전한 도메인.

## 1. 구성 — 2 축

| 축 | CPP | 핵심 파일 |
|---|---|---|
| **thermodynamics** | `ICE_THERMO` | `ice_thermo.F`/`ice_mk.h`(Mellor-Kantha), `ice_frazil.F`, `ice_enthalpy.F`, `ice_albedo.F` |
| **dynamics** | `ICE_MOMENTUM` | `ice_evp.F`(EVP), `ice_elastic.F`, `ice_evp_sig.F`(stress), `ice_advect.F`/`ice_smolar.h`(advection), `ice_limit.F` |
| 결합 | | `ice_spdiw.F`(ice-water stress), BC `ice_tibc/uibc/vibc.F`, `ice_bc2d.F` |

상태변수: 빙 두께 `hi`·농도(concentration) `ai`·snow·빙 속도 `ui/vi`·enthalpy/온도.

## 2. Thermodynamics — Mellor-Kantha (ice_mk.h) ★

`ice_thermo`(ice_mk.h:108) = **빙 성장/소멸**(growth/decay)을 표면·저면 열속으로 계산:
- 표면 열수지(net heat flux, [[roms_bulk_flux_coare]] 의 빙 표면 버전 + `ice_albedo` 반사) → 빙 상부 융해/적설.
- 저면: 해양↔빙 열속(ocean heat flux) → 저면 성장/융해. 빙 내부 열전도(enthalpy `ice_enthalpy.F`, multi-layer 온도).
- **frazil ice**(`ice_frazil.F`): 과냉각(supercooled) 해수에서 frazil 빙 생성 → 표층 빙 추가, 잠열 해방.
- **brine rejection**: 빙 결빙 시 염 배출 → 해양 표층 salt flux(밀도↑, 대류). 융해 시 담수 flux.
- Mellor & Kantha 1989 빙 열역학.

## 3. Dynamics — EVP rheology (ice_evp.F)

빙 운동량 = **Elastic-Viscous-Plastic(EVP) rheology**(Hunke & Dukowicz 1997):
- 빙 momentum: wind stress + ocean-ice stress(`ice_spdiw`) + Coriolis + sea-surface tilt + **internal ice stress**(rheology).
- **EVP**: 빙을 viscous-plastic(Hibler 1979) 으로 모델링하되 elastic 항을 추가해 explicit subcycling 으로 효율 해(원 VP 의 implicit 회피). `ice_evp_sig.F` = stress tensor(σ) 진화.
- **advection**(`ice_advect.F`/`ice_smolar.h`): 빙 두께·농도를 **Smolarkiewicz MPDATA**([[roms_advection]] 와 동족) positive-definite advection. `ice_limit.F` = 농도 [0,1]·두께 한계.

## 4. 해빙-해양 결합

- **ice-water stress** `ice_spdiw.F`: 빙-해양 상대속도 × drag → 해양 표층 운동량(빙이 표층류 구동/감쇠).
- **표면 flux 변조**: 빙 농도 `ai` 가 해양 표면 heat/momentum/salt flux 를 (1-ai) 비율로 차단(빙 아래는 빙-해양 flux). [[roms_baroclinic_3d]] surface BC 수정.
- brine/freshwater flux → 표층 염분·밀도 → 대류·성층.

## 5. 한계·범위

- 본 노트 = 구조(thermodynamics/dynamics/advection/결합) 레벨. EVP subcycling·Mellor-Kantha 다층 열전도 식 line-by-line 은 후속.
- 한국 연안(비결빙)엔 비활성; 고위도(북극·남극·오호츠크) 적용.

## 6. 연결

- [[roms_bulk_flux_coare]] — 빙 표면 열수지(albedo 변조)
- [[roms_baroclinic_3d]] — 빙 농도가 해양 surface flux(heat/salt/momentum) 차단
- [[roms_advection]] — Smolarkiewicz MPDATA(빙 advection 동족)
- Budgell 2005 / Mellor-Kantha 1989(thermo) / Hunke-Dukowicz 1997(EVP) / Hibler 1979(VP rheology)
