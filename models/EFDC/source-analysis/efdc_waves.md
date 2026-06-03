---
title: "EFDC+ Waves 모듈 — 내부 wind-wave(SPM fetch) + SWAN 결합(GETSWAN) + dispersion(Doppler) + wave BL + radiation stress 강제(WAVESXY)"
topic: efdc
canonical_source: self
citation_status: verified
verification_method: "models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Waves/ mod_windwave.f90(1009) + mod_getswan.f90(411) + mod_wavelength.f90(95) + wavebl.f90(235) + wavesxy.f90(582) 직접 read. SPM fetch growth 상수(0.283/0.530/0.0125/0.42 + shallow 0.077/0.25/0.833/0.375) + dispersion DISRELATION + radiation stress Sxx/Syy/Sxy + WVDISV TKE source + IFWAVE/SWANGRP dispatch file:line 인용. Dang Chung 2010-17."
note_author: "Claude Opus 4.8 (1M context) source-code direct read"
note_date: 2026-06-03
verification_by: "Claude Opus 4.8 (1M context) — wind-wave/SWAN결합/radiation stress 알고리즘 verbatim"
verification_date: 2026-06-03
related:
  - models/EFDC/source-analysis/sediment/efdc_sediment.md
  - models/EFDC/source-analysis/efdc_turbulence.md
  - models/EFDC/manual-notes/efdc-theory-v12-ch2-hydrodynamics.md
  - models/SWAN/source-analysis/swan-foundation.md
---

# EFDC+ Waves 모듈 — wind-wave / SWAN 결합 / radiation stress

> `Waves/` 5 파일 직접 read (Dang Chung 2010-17). EFDC+ 의 **파랑장 산출·결합**: 내부 wind-wave 생성 또는 외부(wave.inp / SWAN) → wave-current bottom shear([[efdc_sediment]] §F) + radiation stress 운동량 강제 + wave dissipation → 난류 TKE source([[efdc_turbulence]]). SWAN([[swan-foundation]])과의 EFDC 측 결합점.

## 1. 3 파랑 입력 경로 (IFWAVE / SWANGRP, wavebl.f90)

| 경로 | 플래그 | 소스 |
|---|---|---|
| **내부 wind-wave** (fetch 기반 생성) | `IFWAVE=0` + `WVLCAL=1` | `mod_windwave.f90` |
| **외부 wave.inp** | `IFWAVE=0` (WVLCAL=0) | `wavesxy.f90` |
| **외부 SWAN 결합** | `IFWAVE=1`, `SWANGRP=1`(grid)/`0`(point) | `mod_getswan.f90` |

입력 카드: C14A(IFWAVE/SWANGRP), C14B(파라미터). 공통 산출 → `wavesxy.f90` 가 radiation stress·forcing 처리.

## 2. 내부 wind-wave — CERC SPM fetch 성장식 (mod_windwave.f90) ★

local wind + fetch 로 파고/주기 산출 (16 zone fetch, `NZONE=16`). **CERC Shore Protection Manual(SPM 1984)** 파라메트릭 식:

### 2.1 deep-water (line 217-218)
```fortran
FC1 = TANH(0.530*FC0)                              ! FC0=(g·d/U²)^0.75 깊이항
FC2 = WINDVEL2*GI*0.283*FC1                        ! Hmo = 0.283·(U²/g)·tanh(0.530·(gd/U²)^0.75)·tanh(...)
FC3 = TANH(0.0125*(G*FWDIR(L,ZONE)/WINDVEL2)**0.42/FC1)   ! fetch 항 (FWDIR=fetch 거리)
```
### 2.2 shallow-water 주기 (line 235-237)
```fortran
FC0 = TANH(0.833*(G*AVEDEP/WINDVEL2)**0.375)       ! 수심 제한항
FC2 = TANH(0.077*(G*FWDIR/WINDVEL2)**0.25/FC0)     ! Tp = ...·(gF/U²)^0.25
```
- 상수 `0.283·0.530·0.0125·0.42`(Hmo) + `0.077·0.25·0.833·0.375`(Tp) = **SPM 천해 파랑예측식** verbatim.
- `FWDIR(L,ZONE)` = zone별 fetch 거리, `AVEDEP=Fetch_Depth` = fetch 따라 평균수심, `ROTAT` = 도메인 회전각.
- **fetch 계산** (`FETCH_Global`, line 390+): 각 cell 에서 풍상방향으로 `RL0=min(DX,DY)/4` 씩 전진하며 wet cell 추적 → fetch 길이·평균수심. 출력 FETCH.OUT/TAUW.OUT.

## 3. Dispersion relation — Doppler 포함 (mod_wavelength.f90)

```fortran
FWL = (RLS/TP - U*COS(PHI)) - SQRT(G*RLS/2π * TANH(2π*HD/RLS))    ! DISRELATION (line 28)
```
- 파장 `RLS` 를 **흐름(U) 포함 dispersion** `(L/T − U·cosφ) = √(gL/2π·tanh(2πd/L))` 의 근으로 — `BISEC`(이분법, 재귀) / `RTBIS` 로 해. `PHI`=파-흐름 각, Doppler shift 반영.

## 4. Wave boundary layer (wavebl.f90)

- `WVLCAL` = wave length 계산(1) vs wave.inp(0). `ISDZBR` = 유효 wave-current BL roughness 진단 출력.
- wave-current bottom shear → [[efdc_sediment]] §F (Christoffersen-Jonsson 형식, sediment 침식 임계와 결합). [[efdc_sedzlj]] s_shear 의 wave 입력측.

## 5. Radiation stress + wave 강제 (wavesxy.f90) ★

외부/내부 wave data → 운동량·난류 강제:
- **wave energy**: `ENE = 0.5·g·|a|²` (m³/s²), `WVDISP` = dissipation (m³/s³, SWAN INRHOG W/m²).
- **radiation stress** `SXX/SYY/SXY` (kg/s²) → **wave-induced force** `FXWAVE/FYWAVE` + `WVHUU/WVHVV/WVHUV`(운동량 항). 
  - `ISWRSR` = 회전(rotational) 성분 / `ISWRSI` = 비회전(irrotational) 성분 포함 토글.
- **wave dissipation → 난류 source**: `WVDISV` = TKE(q²) closure source 분율 → `WVDTKEP/WVDTKEM`(층별 0.5·WVDISV 분배, line 109-120). `WVDISH`(Smagorinsky 수평) = **NOT USED**.
- `ISWCBL=1` wave-current BL 활성, `NTSWV` = wave forcing 점진 도입 step 수.

→ radiation stress 이론은 [[efdc-theory-v12-ch2-hydrodynamics]] (Longuet-Higgins-Stewart 1964) 대응. wave→current setup·longshore 구동.

## 6. SWAN 결합 (mod_getswan.f90)

- SWAN 출력 직접 read: `GETSWAN_GRP`(FRM/GRP 전체 격자) / TBL(LOC point 파일). `SWN INRHOG=1` → dissipation W/m².
- EFDC ↔ SWAN **one-way**(SWAN 파랑 → EFDC 흐름/sediment). SWAN spectral 파일 포맷은 [[swan-spectral-file-format]] 참조.
- `SHLIM`(shallow limit)·`WHMI`(min wave height) 등 WINDWAVE 모듈 상수 공유.

## 7. 연결

- [[efdc_sediment]] §F / [[efdc_sedzlj]] — wave-current bottom shear (파랑이 sediment 침식 구동)
- [[efdc_turbulence]] — WVDISV wave dissipation → TKE(q²) source
- [[efdc_hydro_core]] — FXWAVE/FYWAVE radiation stress 운동량 강제
- [[efdc-theory-v12-ch2-hydrodynamics]] — radiation stress 이론(Longuet-Higgins-Stewart)
- [[swan-foundation]] / [[swan-spectral-file-format]] — 외부 SWAN 결합(GETSWAN)
- CERC Shore Protection Manual 1984 — §2 fetch wave growth 식 (코드 상수 출처, 주석 미명시·식 구조 식별)
