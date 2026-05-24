---
title: "ROMS bulk_flux.F (1623 lines) — COARE bulk parameterization (Fairall 1996/2003·Edson 2013)"
topic: roms-bulk-flux-coare
canonical_source: self
citation_status: verified
verification_method: "models/ROMS/raw/source_code/roms/ROMS/Nonlinear/bulk_flux.F 직접 read (head 50 lines, 1623 total lines, MODULE bulk_flux_mod under BULK_FLUXES CPP option, Copyright Hernan Arango 2002-2026). 인용 paper 8 개 (Fairall 1996·2003 COARE, Liu-Katsaros-Businger 1979, Taylor-Yelland 2001, Oost 2002, Drennan 2003, Edson 2013) Fortran header 주석에서 직접 추출."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-24
verification_by: "Claude Opus 4.7 (1M context) — Fortran source 직접 read"
verification_date: 2026-05-24
related:
  - models/ROMS/source-analysis/roms_atmospheric_forcing.md
  - models/ROMS/source-analysis/roms_nonlinear_physics_modules.md
  - models/ROMS/manual-notes/roms-wiki-cppdefs-options.md
  - concepts/sst/02-theory.md
---

# ROMS `bulk_flux.F` — COARE Bulk Parameterization

> 출처: [`models/ROMS/raw/source_code/roms/ROMS/Nonlinear/bulk_flux.F`](../raw/source_code/roms/ROMS/Nonlinear/bulk_flux.F) — 1623 줄. CPP option `BULK_FLUXES` 활성 시 사용.

## 1. 파일 식별

| 항목 | 값 |
|---|---|
| 경로 | `ROMS/Nonlinear/bulk_flux.F` |
| 라인 수 | 1623 |
| Module 명 | `bulk_flux_mod` |
| CPP guard | `#ifdef BULK_FLUXES` |
| Copyright | 2002-2026 The ROMS Group (Hernan G. Arango) |
| License | MIT/X style ([License_ROMS.md](../raw/source_code/roms/License_ROMS.md)) |
| Git ID | (`!git $Id$`) |

## 2. 역할 (Fortran header 주석 직접 인용)

> "This routine computes the bulk parameterization of surface wind stress and surface net heat fluxes." (bulk_flux.F line 12-14)

→ ROMS 의 air-sea flux 계산 핵심. 다음 4 출력:
- **Wind stress** ($\tau_x$, $\tau_y$)
- **Sensible heat flux** ($Q_{\text{sensible}}$)
- **Latent heat flux** ($Q_{\text{latent}}$)
- **Net heat balance** ($Q_{\text{net}}$ — 위 + shortwave + longwave)

이 출력이 baroclinic 3D mode 의 surface BC 로 주입됨.

## 3. 알고리즘 — COARE 계열

bulk_flux.F header (line 14-50) 직접 인용한 8 paper:

### 3.1 시초 — COARE (1996)

- **Fairall, C.W., E.F. Bradley, D.P. Rogers, J.B. Edson, G.S. Young (1996)** "Bulk parameterization of air-sea fluxes for tropical ocean-global atmosphere Coupled-Ocean Atmosphere Response Experiment" *J. Geophys. Res.* 101:3747-3764 — **COARE 알고리즘 시초**
- **Fairall, C.W., E.F. Bradley, J.S. Godfrey, G.A. Wick, J.B. Edson, G.S. Young (1996)** "Cool-skin and warm-layer effects on sea surface temperature" *J. Geophys. Res.* 101:1295-1308

### 3.2 Foundation

- **Liu, W.T., K.B. Katsaros, J.A. Businger (1979)** "Bulk parameterization of the air-sea exchange of heat and water vapor including the molecular constraints at the interface" *J. Atmos. Sci.* 36:1722-1735 — 초기 bulk theory

### 3.3 Wave-roughness 의존성

- **Taylor, P.K., M.A. Yelland (2001)** "The dependence of sea surface roughness on the height and steepness of the waves" *J. Phys. Oceanogr.* 31:572-590
- **Oost, W.A., G.J. Komen, C.M.J. Jacobs, C. van Oort (2002)** "New evidence for a relation between wind stress and wave age from measurements during ASGAMAGE" *Bound.-Layer Meteor.* 103:409-438
- **Drennan, W.M., H.C. Graber, D. Hauser, C. Quentin (2003)** "On the wave age dependence of wind stress over pure wind seas" *J. Geophys. Res. Oceans* 108(C3)

→ ROMS cppdefs §8 "wave roughness formulation in bulk fluxes" 에서 활성 옵션 선택.

### 3.4 COARE 3.0 / 3.5 update

- **Fairall, C.W., E.F. Bradley, J.E. Hare, A.A. Grachev, J.B. Edson (2003)** "Bulk parameterization of air-sea fluxes: Updates and verification for the COARE algorithm" *J. Climate* 16:571-591 — **COARE 3.0**
- **Edson, J.B., V. Jampana, R.A. Weller, S.P. Bigorre, A.J. Plueddemann, C.W. Fairall, S.D. Miller, L. Mahrt, D. Vickers, H. Hersbach (2013)** "On the exchange of momentum over the open ocean" *J. Phys. Oceanogr.* — **COARE 3.5**

→ 본 위키 verified bulk_flux.F 가 위 8 paper 의 implementation 합본.

## 4. 입력 변수 (대기 forcing)

ROMS bulk_flux 는 다음 surface forcing 입력 받음 (NetCDF 또는 analytical):

| 변수 | 단위 | 출처 |
|---|---|---|
| **Tair** | °C | 대기 모델 (WRF) 또는 reanalysis (NCEP/ERA5) |
| **Pair** | mb | same |
| **Qair** | % (relative humidity) 또는 kg/kg | same |
| **Uwind, Vwind** | m/s (10m wind) | same |
| **rain** | kg/m²/s | same |
| **swrad** | W/m² (shortwave radiation) | same |
| **lwrad** 또는 lwrad_down | W/m² (longwave radiation) | same |
| **cloud** | fraction (선택) | same |

## 5. 출력 변수 → ROMS 운동량·열 BC

| 출력 | 단위 | 용도 |
|---|---|---|
| `sustr`, `svstr` | N/m² | wind stress → momentum BC |
| `shflux` | W/m² | net surface heat flux → tracer (T) BC |
| `ssflux` | (psu·m/s) | surface salt flux (evaporation - precipitation) |
| `srflux` | W/m² | shortwave radiation (separate, light penetration) |
| `sensible` | W/m² | (diagnostics) |
| `latent` | W/m² | (diagnostics) |
| `evap` | kg/m²/s | (diagnostics) |

## 6. 활성 옵션 (cppdefs.h §7-9 연결)

| CPP option | 효과 |
|---|---|
| `BULK_FLUXES` | bulk_flux.F 활성 (master switch) |
| `LONGWAVE_OUT` | longwave 계산 mode (NCEP-style vs DOWN-style) |
| `EMINUSP` | evaporation - precipitation (salt budget) |
| `COOL_SKIN` | Fairall 1996 cool-skin 효과 |
| `WIND_MINUS_CURRENT` | relative wind (current 대비) |
| `SPECIFIC_HUMIDITY` | Qair = specific humidity (vs relative humidity) |
| Wave-roughness sub-options | Taylor-Yelland·Oost·Drennan 활성 (cppdefs §8) |

→ 운영 결정 — KOOS-EJS 류는 보통 `BULK_FLUXES + LONGWAVE_OUT + EMINUSP + COOL_SKIN` 활성.

## 7. 사용 흐름 (main3d 호출 순서)

`main3d.F` baroclinic loop 매 step:
1. **NetCDF 외부 forcing read** (Tair·Pair·Qair·wind 등)
2. **bulk_flux.F 호출** → sustr/svstr/shflux/ssflux 계산
3. **운동량 surface BC 적용** (Nonlinear/u3dbc, v3dbc 등)
4. **Tracer surface BC 적용** (Nonlinear/t3dbc)
5. 다음 step

## 8. 본 위키 cross-ref

| 주제 | 위치 |
|---|---|
| 대기 forcing 일반론 | [[roms_atmospheric_forcing]] (a9618df promote) |
| Nonlinear/ 전체 dispatcher | [[roms_nonlinear_physics_modules]] |
| CPP options 운영 결정 | [[../manual-notes/roms-wiki-cppdefs-options]] §7 BULK_FLUXES |
| Vertical mixing (보완) | [[roms_vertical_mixing]] |
| 한국 적용 — concepts/sst | [`concepts/sst/02-theory.md`](../../../concepts/sst/02-theory.md) §3 heat budget |
| 한국 적용 — EFDC COARE | [`models/EFDC/manual-notes/efdc-theory-doc-v12.md`](../../EFDC/manual-notes/efdc-theory-doc-v12.md) §4.2 Ch 5.1.2 COARE 3.6 |

→ **EFDC v12 + ROMS 둘 다 COARE 3.x 사용** — 같은 air-sea flux 알고리즘, 다른 모델 적용 (concepts/sst 와의 일관성).

## 9. 작성 우선순위 (남은 M-D)

- `roms_main3d_loop_order.md` — main3d.F time-step loop (bulk_flux 호출 위치 정확 확인)
- `roms_atmospheric_forcing_netcdf.md` — forcing NetCDF format (existing roms_atmospheric_forcing.md 의 deep 후속)
- `roms_kpp_mixing_walkthrough.md` — Nonlinear/KPP scheme 의 Fortran 구현 상세 (LMD 1994)

## 10. 관련 자료

- [[roms_atmospheric_forcing]] — 대기 forcing 일반론 (a9618df promote)
- [[roms_nonlinear_physics_modules]] — Nonlinear/ 6 subdirs + core Fortran
- [[roms_main_driver_dispatch]] — Drivers/ + Master/ ESMF (WRF coupling 대안)
- [[../manual-notes/roms-wiki-cppdefs-options]] §7 BULK_FLUXES
- [[../web-refs/roms-official-resources]] — Large 1994 KPP·Fairall COARE 인용 (web-refs §3)
- [`concepts/sst/02-theory.md`](../../../concepts/sst/02-theory.md) §3 heat budget (개념 cross-ref)
- 외부: [Fairall et al. 2003 COARE 3.0 paper](https://doi.org/10.1175/1520-0442(2003)016<0571:BPOASF>2.0.CO;2)
