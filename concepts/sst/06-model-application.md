---
title: "SST 모델 적용 — boundary forcing · thermal module · 모델별 입력 형식"
topic: sst
canonical_source: self
citation_status: verified
verification_method: "모델별 표층 열수지 구현 claim 을 검수완료 source-analysis 노트로 cross-link verified: (1) ROMS COARE bulk flux 4-항 + cool-skin → models/ROMS/source-analysis/roms_bulk_flux_coare.md (bulk_flux.F 1623줄 직접 read, COARE 1996/2003/Edson2013 8 paper) + roms_atmospheric_forcing.md (COARE 3.0 3-iter loop, longwave 3 옵션, shortwave penetration SOLAR_SOURCE, file:line 인용). (2) Delft3D heat KTEMP 5 dispatch + ocean/Proctor COARE-style bulk + Murakami 4-항 → models/Delft3D/source-analysis/delft3d_heat.md (heatu.f90:162-1276 직접 분석). (3) EFDC 연직 수온 transport/layering(sigma·SGZ)·vertical advection → models/EFDC/source-analysis/efdc_vertical.md (caltran.f90·caluvw.f90 file:line). \n여전히 source-needed: EFDC 표층 heat budget 커널(calheat.f90)·EFDC aser.inp bulk 계수, Delft3D §4.1 입력 파일 형식, 각 모델 한국 적용 paper(NIFS/KMOU), SWAN stability correction(Tolman 1991, 미수록), SST forcing 데이터셋 endpoint(외부)."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-23
verification_by: "Claude Opus 4.8 (1M context) — 모델 source-analysis 노트 cross-link verify 2026-06-18"
verification_date: 2026-06-18
related:
  - concepts/sst/02-theory.md
  - models/ROMS/source-analysis/roms_bulk_flux_coare.md
  - models/Delft3D/source-analysis/delft3d_heat.md
  - models/EFDC/source-analysis/efdc_vertical.md
---

# SST 모델 적용

> 본 §는 SST(또는 수온 일반) 가 연안 수치모델에 어떻게 들어가는지·어떻게 나오는지 정리. EFDC·Delft3D·ROMS·ADCIRC·XBeach·SWAN 모델별 차이.

> **citation_status: verified** (모델 source-analysis cross-link 기반) — ROMS COARE bulk flux·Delft3D heat KTEMP·EFDC 연직 수온 transport 의 구현은 검수완료 source-analysis 노트(아래 링크)로 뒷받침. **여전히 source-needed**: EFDC 표층 heat budget 커널(calheat.f90), 각 모델 입력 파일 형식·한국 적용 paper, SWAN stability correction(미수록 모델·외부 논문).

## 1. SST 의 역할 — 입력 vs 출력

수치모델에서 SST 는 다음 중 하나:

| 역할 | 모델 종류 | 예 |
|---|---|---|
| **boundary condition** (입력) | barotropic ocean (조위·조류) | ADCIRC, SWAN, XBeach (1D barotropic) |
| **prognostic 변수** (모델이 계산) | baroclinic ocean (3D) | EFDC, Delft3D-FLOW, ROMS, HYCOM |
| **forcing 입력** | wave·sediment 모델 (열적 stratification 영향) | SWAN+ADCIRC coupled, Delft3D wave-flow |

본 위키 사용자 주력 모델 (EFDC, Delft3D, ROMS) 은 **prognostic 3D** 그룹 — SST 를 boundary/forcing 입력 + 내부 계산 + 출력 모두.

## 2. Prognostic 3D 모델의 SST 처리

### 2.1 표층 열수지 방정식

수치모델 내부 표층 열수지 ([`02-theory.md`](02-theory.md) §1 eq. 5.1):

$$\rho C_p \frac{\partial T}{\partial t}\bigg|_{\text{surface}} = Q_{SW} - Q_{LW} - Q_S - Q_L$$

(advection $Q_V$ 는 별도 수송 방정식에서 처리)

각 항을 **bulk formula** 로 계산:
- $Q_{SW}$ = solar radiation (외부 forcing, 또는 cloud cover 로부터 계산)
- $Q_{LW}$ = $\varepsilon \sigma (T_s^4 - T_a^4)$ (대기 온도 forcing 필요)
- $Q_S = \rho_a c_{p,a} C_S U (T_a - T_s)$ (sensible)
- $Q_L = \rho_a L_v C_L U (q_a - q_s)$ (latent)

필요 forcing 입력:
- 단파복사 $Q_{SW}$ (W/m²) — 위성 또는 계산
- 기온 $T_a$ (°C)
- 풍속 $U$ (m/s, 보통 10m)
- 상대습도 또는 dew point
- 운량 (cloud cover, optional)
- 기압 (필수 아님)

## 3. EFDC 의 SST 처리

### 3.1 입력 파일 (EFDC+, Tetra Tech)

| 파일 | 변수 |
|---|---|
| `aser.inp` | atmospheric series — $T_a$, $U$, RH, $Q_{SW}$, 기압, 운량 |
| `tser.inp` | open boundary temperature (수온 boundary) |
| `efdc.inp` §C8 | physical constants — α, ε, C_S, C_L 등 |

### 3.2 알고리즘

EFDC 의 heat budget 계산:
- **표층 bulk flux 4개 항** (`calheat.f90`) — **source-needed** (본 위키 calheat.f90 source-analysis 미작성; EFDC v12 는 COARE 3.6 사용, [`models/EFDC/manual-notes/efdc-theory-doc-v12.md`](../../models/EFDC/manual-notes/efdc-theory-doc-v12.md) §4.2 Ch 5.1.2 참조 — manual-notes 확인 권장)
- **연직 thermal transport / advection** — 수온은 EFDC 의 일반 tracer 로 연직 upwind advection (`caltran.f90:152-183`) 되며, sigma/Sigma-Zed(SGZ) 연직 격자(`KC`·`IGRIDV`)에 따라 layer thickness `HPK = HP·DZC` 로 분배됨. **verified**: [`models/EFDC/source-analysis/efdc_vertical.md`](../../models/EFDC/source-analysis/efdc_vertical.md) §A·§D (sigma layers·vertical advection). 가파른 지형에서 sigma 좌표 spurious diapycnal mixing 이 인공 성층(SST 연직 구조 왜곡)을 만들 수 있어 `IINTPG=1/2` 권장 (efdc_vertical.md §E·Working Rules).
- horizontal advection

**한국 적용 권장 값** (citation TODO — `models/EFDC/manual-notes/heat-bulk-flux.md` 작성 시):
- $C_S, C_L \sim 1.0 \times 10^{-3}$ (중립)
- albedo $\sim 0.06$ (해수 표면)
- $\varepsilon \sim 0.97$

### 3.3 출력

EFDC 의 SST 출력:
- `wsec.out` 또는 `EE_WS.OUT` — 표층 수온 시계열
- NetCDF (`OUT_NCDF`) — 격자 SST

## 4. Delft3D-FLOW 의 SST 처리

### 4.1 입력 (Delft3D-FLOW 4.x)

| 파일 | 변수 |
|---|---|
| `*.bct` | open boundary forcing — temperature time series 옵션 |
| `*.bcc` | 3D boundary condition (수온 vertical profile) |
| `*.ext` | external forcing — meteo block (heat flux 옵션) |
| `*.mdf` | master file — heat model 활성화 (Sub1 = 'temp') |

### 4.2 Heat module

**verified** ([`models/Delft3D/source-analysis/delft3d_heat.md`](../../models/Delft3D/source-analysis/delft3d_heat.md), `heatu.f90:162-1276` 직접 분석): source code 의 실제 `KTEMP` dispatch 는 manual 라벨과 **다를 수 있음** — 코드 기준:

| `KTEMP` | 모델 | 구현 |
|---|---|---|
| 1 | absolute | 내부 solar + atmospheric radiation (`heatu.f90:381`) |
| 2 | composite | 입력 total radiation `qin = qradin`, 나머지 항 내부 계산 (`:510`) |
| 3 | excess-temperature | `hlc·(T − tback)` heat-loss 계수 (`:633`) |
| 4 | **Murakami** | 4-항 full 절대 열수지 (latent·sensible Bowen·Berliand longwave·shortwave Secchi 감쇠) (`:716-826`) — 가장 물리적으로 완전 |
| 5 | **ocean / Proctor** | COARE-style bulk (Dalton latent·Stanton sensible·자유대류) (`:925-1179`) — open-ocean 연안 권장 |

표층 열은 별도 boundary 가 아니라 **top-layer source/sink** 로 주입되고, shortwave 는 Secchi extinction 으로 연직 침투 (delft3d_heat.md §H). 한국 연안 storm-surge 는 `KTEMP=5` (ocean/Proctor) 가 가장 물리적 (delft3d_heat.md Decision Guide).

### 4.3 한국 적용

Delft3D-FLOW 의 한국 연안 적용 예 (citation TODO):
- 영산강 하구 thermal stratification (Lee et al. 한국해양환경학회)
- 시화호 thermal model (Choi et al.)

## 5. ROMS 의 SST 처리

### 5.1 입력 (ROMS Rutgers)

| 파일 | 변수 |
|---|---|
| `frc_*.nc` | forcing NetCDF — Uwind, Vwind, Tair, Pair, Qair, swrad, lwrad |
| `clm_*.nc` | climatology — open boundary 수온·염분 |
| `init_*.nc` | initial condition — 3D temperature field |
| `roms.in` (param file) | physical constants, scheme 선택 |

### 5.2 Bulk flux algorithm

**verified** ([`models/ROMS/source-analysis/roms_bulk_flux_coare.md`](../../models/ROMS/source-analysis/roms_bulk_flux_coare.md), `bulk_flux.F` 1623줄 직접 read + [`roms_atmospheric_forcing.md`](../../models/ROMS/source-analysis/roms_atmospheric_forcing.md) file:line):

ROMS 는 `BULK_FLUXES` CPP option 활성 시 **COARE algorithm** (Fairall 1996/2003 COARE 3.0, Edson 2013 COARE 3.5; bulk_flux.F header 8 paper) 사용:
- 4개 항 분리 출력 — `stflux(itemp) = srflx + lrflx + lhflx + shflx` (roms_atmospheric_forcing.md §D, `bulk_flux.F:1276`)
- Monin-Obukhov stability loop **고정 3-iteration** (`IterMax=3`, bulk_flux.F:429,830) + gustiness factor
- longwave 3 옵션: Berliand(`LONGWAVE`) / downwelling(`LONGWAVE_OUT`) / direct net (roms_atmospheric_forcing.md §D)
- **cool-skin (`COOL_SKIN`) 만 구현; 별도 warm-layer 없음** (roms_atmospheric_forcing.md §F) — diurnal warm-layer 는 외부 SST forcing 전처리 필요
- shortwave 는 `SOLAR_SOURCE` 로 Jerlov 수종별 연직 침투(연안 = Jerlov II/III) (roms_atmospheric_forcing.md §G)

bulk_flux 출력 `shflux/srflux` 가 baroclinic 3D mode 의 tracer(T) surface BC 로 주입 (roms_bulk_flux_coare.md §5·§7). **EFDC v12 + ROMS 둘 다 COARE 3.x** 를 써서 air-sea flux 알고리즘이 일관 (roms_bulk_flux_coare.md §8).

### 5.3 한국 적용

- _staging/from-modeling-wiki/knowledge/methods/roms_atmospheric_forcing.md (at commit a9618df^) (modeling-wiki 흡수) — ROMS forcing 일반론
- ROMS 한국 동해 모델 (NIFS 동해예측시스템 KOOS-EJS 기반) — citation TODO

## 6. ADCIRC 의 SST 처리

### 6.1 ADCIRC v55 은 barotropic 우선

ADCIRC 기본 모드: 2DDI (depth-integrated) → 수온 무관. 그러나:

- **NWS=13 baroclinic** — 일부 버전에서 baroclinic 옵션, SST input 가능 (드물게 사용)
- **Coupled SWAN+ADCIRC** — wave 만 결합, SST 직접 forcing 없음
- **Hot-start temperature** — initial T field 옵션

대부분의 한국 ADCIRC 적용 (storm surge) 은 SST 무관.

## 7. XBeach 의 SST 처리

XBeach: 단기 (storm) 사건 surf zone 모델 — **SST 무관**.

XBeach 에 수온은 입력하지 않음. 다만 wave dissipation 의 viscosity 계산에 수온 영향 가능 (보통 무시).

## 8. SWAN 의 SST 처리

SWAN: spectral wave 모델 — **SST 직접 사용 안 함**, 그러나:

- **Wind input source term** ($S_{in}$) 는 air-sea stability 영향 받음 — stability correction 에 $T_a - T_s$ 가 들어감 (Tolman 1991)
- 대부분 SWAN 한국 적용은 stability correction 기본값 사용 (`SET LEVel=auto`)

## 9. SST forcing 입력 source 권장

수치모델 forcing 으로 사용 시:

| 모델 종류 | 권장 SST source | 시간·공간 해상도 |
|---|---|---|
| 단기 hindcast (수일~수주) | OISST v2.1 daily | 0.25° daily |
| 장기 climate (수십년) | HadISST 또는 COBE-SST2 | 1° monthly |
| 운영 forecast | NOAA NCEP RTG-SST 또는 OSTIA | 0.25°-0.05° daily |
| 정밀 nowcast (≤1주) | MUR L4 | 0.01° daily |
| in-situ validation | KHOA 또는 NIFS 정선 | 점·1분 |

본 위키 [`04-code-and-tools.md`](04-code-and-tools.md) §3-6 에 각 데이터셋 endpoint·접근법.

## 10. 한국 SST 가속이 모델에 미치는 영향

[`experience/khoa-sst-warming-trend.md`](../../experience/khoa-sst-warming-trend.md) §8.1 에서 지적:

- 한국 평균 SST 가 1968-2012 보다 ~10× 가속 (최근 9년)
- 모델 boundary 입력값을 ~2010 climatology 로 사용 시 **+0.7~1.4 °C 보정 필요** (2025 기준)
- thermal stratification·산소 용해도·생물지화학 반응 속도 모두 영향

권장:
- **2025+ 모델 적용 시 climatology 를 1991-2020 또는 더 최근으로 갱신** (NIFS·KHOA·OISST)
- climatology + 최근 anomaly forecast (e.g., KMA 기후 예측) 조합

## 11. TODO (잔존 source-needed — verified 부분은 §3-5 cross-link 참조)

verified 완료 (모델 source-analysis cross-link):
- ☑ ROMS COARE bulk flux — [`roms_bulk_flux_coare.md`](../../models/ROMS/source-analysis/roms_bulk_flux_coare.md) + [`roms_atmospheric_forcing.md`](../../models/ROMS/source-analysis/roms_atmospheric_forcing.md)
- ☑ Delft3D heat KTEMP dispatch — [`delft3d_heat.md`](../../models/Delft3D/source-analysis/delft3d_heat.md)
- ☑ EFDC 연직 수온 transport/layering — [`efdc_vertical.md`](../../models/EFDC/source-analysis/efdc_vertical.md)

잔존:
1. ☐ EFDC 표층 heat budget 커널 (`calheat.f90`) source-analysis — 현재 efdc_vertical.md 는 연직 transport 만 커버
2. ☐ `models/Delft3D/manual-notes/heat-module.md` — Manual KTEMP 라벨 vs 코드 dispatch 대조 (heatu.f90 가 manual 과 다름)
3. ☐ 각 모델의 한국 적용 paper citation (NIFS, KMOU, 해양과학기술원)
4. ☐ 실제 모델 입력 파일 예제 (EFDC `aser.inp`, Delft3D `*.bcc` 등) — `examples/` 폴더
5. ☐ SWAN stability correction (Tolman 1991) source — 미수록

## 12. 연결

- [`01-concept.md`](01-concept.md) — SST 정의
- [`02-theory.md`](02-theory.md) — 열수지 방정식
- [`03-analysis-methods.md`](03-analysis-methods.md) — climatology·anomaly
- [`04-code-and-tools.md`](04-code-and-tools.md) — SST 데이터 source
- [`models/EFDC/`](../../models/EFDC/), [`models/Delft3D/`](../../models/Delft3D/), [`models/ROMS/`](../../models/ROMS/) — 모델별 source/manual
- 검수완료 모델 source-analysis (본 §의 verified 근거):
  - [`roms_bulk_flux_coare.md`](../../models/ROMS/source-analysis/roms_bulk_flux_coare.md) — COARE bulk flux 열속
  - [`roms_atmospheric_forcing.md`](../../models/ROMS/source-analysis/roms_atmospheric_forcing.md) — 대기 강제·COARE 3.0 loop
  - [`delft3d_heat.md`](../../models/Delft3D/source-analysis/delft3d_heat.md) — heat KTEMP 5 dispatch
  - [`efdc_vertical.md`](../../models/EFDC/source-analysis/efdc_vertical.md) — EFDC 연직 수온 transport·layering
- 외부:
  - Fairall et al. 1996 — Bulk parameterization air-sea fluxes (J. Climate 9:1747-1768)
  - Lesser et al. 2004 — Delft3D-FLOW 3D modeling (Coastal Engineering 51:883-915)
  - Tolman 1991 — wind input stability correction (J Phys Oceanogr 21:782-797)
