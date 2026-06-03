---
title: "ROMS biology(생태계) 프레임워크 — biology.F dispatcher(7-file/CPP 선택) + 모델 카탈로그(NPZD Franks/Powell/iron · Fennel C-N-O biogeochem · NEMURO · EcoSim · ECB · hypoxia · red_tide). bio tracer = T/S처럼 transport + 모델별 source/sink"
topic: roms
canonical_source: self
citation_status: verified
verification_method: "models/ROMS/raw/source_code/roms/ROMS/Nonlinear/Biology/ 직접 read — biology.F(7-file 구조·CPP dispatch 주석 11-66) + 모델 .h 인벤토리(fennel.h 2375/npzd_Franks 589/npzd_Powell 663/nemuro/ecosim/ecb/hypoxia_srm/red_tide) + fennel.h 헤더(NO3/NH4/phyto/chloro/zoo/SDeN/LDeN + CARBON DIC/TAlk + OXYGEN, nitrif/denitrif/Wanninkhof2014/Zeebe-Wolf-Gladrow2001, Nsink=6) file:line 인용."
note_author: "Claude Opus 4.8 (1M context) source-code direct read"
note_date: 2026-06-03
verification_by: "Claude Opus 4.8 (1M context) — biology 프레임워크·모델 카탈로그·Fennel 과정 verbatim"
verification_date: 2026-06-03
related:
  - models/ROMS/source-analysis/roms_baroclinic_3d.md
  - models/ROMS/source-analysis/roms_advection.md
  - models/ROMS/source-analysis/roms_nonlinear_physics_modules.md
  - models/ROMS/source-analysis/sediment/roms_sediment.md
---

# ROMS biology(생태계) 프레임워크

> `ROMS/Nonlinear/Biology/` 직접 read. ROMS 의 **생물지화학(biogeochemistry) 생태계 모델** 시스템 — 영양염·플랑크톤·탄소·산소 cycle. bio 변수는 **passive tracer 처럼 advection-diffusion**([[roms_advection]]/[[roms_baroclinic_3d]] step3d_t)되고, **source/sink(reaction) 만 모델별** 으로 추가. `BIOLOGY` CPP 정의 시 활성([[roms_nonlinear_physics_modules]]).

## 1. 프레임워크 — biology.F dispatcher (주석 11-66)

각 생태계 모델 = **7 파일** 세트:
| 파일 | 역할 |
|---|---|
| `<model>.h` | source/sink 이산 방정식(reaction kernel) |
| `<model>_mod.h` | 내부 파라미터 선언 |
| `<model>.in` | 파라미터 입력 스크립트 |
| `<model>_inp.h` | 입력 읽기 |
| `<model>_var.h` | 변수 index 할당 |
| `<model>_wrt.h` / `_def.h` | 출력 write / netCDF define |

- **CPP flag 로 1개 모델 선택**(`BIO_FENNEL`/`NPZD_FRANKS`/`NPZD_POWELL`/`NPZD_IRON`/`NEMURO`/`ECOSIM`/`ECB`/`HYPOXIA_SRM`/`RED_TIDE`). biology.F 가 dispatch.
- bio tracer 개수 `NBT` 만큼 tracer 배열(`t(:,:,:,:,iNO3_)` 등) 확장 — T/S 와 같은 transport 커널 공유, 매 step `biology` 커널이 reaction 적용.

## 2. 모델 카탈로그

| 모델 (CPP) | 파일 | 복잡도 |
|---|---|---|
| **NPZD** Franks/Powell/iron | npzd_Franks.h(589)/Powell.h(663)/iron.h | 단순 4-변수 N-P-Z-D (+iron) |
| **Fennel** (BIO_FENNEL) | fennel.h(2375) | C-N-O 완전 biogeochem (§3) |
| **NEMURO** | nemuro.h | 북태평양 11-변수(2 phyto·3 zoo·silica) |
| **EcoSim** | ecosim.h | bio-optical(Bissett, 다종·색소 spectral) |
| **ECB** | ecb.h | estuarine carbon biogeochemistry |
| **hypoxia_srm** | hypoxia_srm.h | 단순 산소 소모(저산소 진단) |
| **red_tide** | red_tide.h | 적조(Alexandrium cyst) |

## 3. Fennel 모델 (fennel.h, 2375) — 대표 biogeochem ★

Fennel et al. 2006 의 carbon/nitrogen/oxygen 모델:
- **기본 N cycle** 상태변수: `NO3`(질산), `NH4`(암모늄), `Phyt`(식물플랑크톤), `Chlo`(엽록소, variable C:Chl), `Zoop`(동물플랑크톤), `SDeN`/`LDeN`(small/large detritus N).
- **CARBON** option: + `TIC`(DIC 용존무기탄소) + `TAlk`(총 알칼리도) + large detritus C. 탄산계 `Zeebe & Wolf-Gladrow 2001`(또는 `pCO2_RZ`).
- **OXYGEN** option: + `Oxyg`(용존산소).
- **과정**: 광합성(PAR light limitation) · **nitrification**(NH4→NO3) · **denitrification**(저층 anaerobic remineralization, 질소 pool 손실) · grazing · mortality · remineralization · **sinking**(`Nsink=6` 침강 변수: phyto·detritus 등) · **air-sea O2/CO2 flux**(`Wanninkhof 2014`).
- 저층: detritus 가 최하층에서 즉시 remineralization(무기영양염 복귀, sediment interface). denitrification 시 anaerobic 경로.

## 4. NPZD (Franks/Powell) — 최소 모델

4 상태변수 `N`(nutrient)-`P`(phytoplankton)-`Z`(zooplankton)-`D`(detritus). 광합성 uptake(Michaelis-Menten N 제한 × light) → grazing → mortality → remineralization → N 복귀. Franks et al. 1986 / Powell et al. 2006. iron variant = + 철 제한(HNLC 해역).

## 5. 결합 — tracer transport 와의 관계

```
step3d_t (tracer 방정식): ∂(Hz·C)/∂t + advection + diffusion = Hz·(bio source/sink)
```
- bio tracer `C` 는 **T/S 와 동일한 advection([[roms_advection]] TVD/MPDATA/upstream)·diffusion·vertical mixing** 을 받음(passive). 차이는 **reaction 항**(`biology` 커널이 매 step 계산, 모델별 .h).
- vertical sinking 은 별도(보존 PPM/WENO sinking 알고리즘). 광합성은 PAR(수중 광 감쇠, [[roms_vertical_mixing]] 광학)에 의존.
- sediment([[sediment/roms_sediment]])·carbon flux 와 결합 가능.

## 6. 한계·범위

- 본 노트 = **프레임워크 + 모델 카탈로그 + Fennel/NPZD 구조** 레벨. 개별 모델의 reaction rate 식 line-by-line(fennel.h 2375 등)은 미포함(후속 deep 후보).
- biology_floats.F = Lagrangian float 기반 bio(별도).

## 7. 연결

- [[roms_baroclinic_3d]] — step3d_t tracer 방정식(bio tracer 가 타는 transport)
- [[roms_advection]] — bio tracer advection 스킴(T/S 공유) + WENO(biology/sediment)
- [[roms_nonlinear_physics_modules]] — BIOLOGY CPP 활성·모듈 dispatch
- [[sediment/roms_sediment]] — sediment-bio carbon 결합
- Fennel et al. 2006 / Franks 1986 / Powell 2006 / Kishi(NEMURO) / Bissett(EcoSim) / Wanninkhof 2014 / Zeebe-Wolf-Gladrow 2001
