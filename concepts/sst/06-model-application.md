---
title: "SST 모델 적용 — boundary forcing · thermal module · 모델별 입력 형식"
topic: sst
canonical_source: self
citation_status: source-needed
verification_method: "각 모델의 공식 manual·source code 인용 — EFDC heat module (EFDC+ Theory Manual §3.x), Delft3D-FLOW thermal source (Lesser 2004), ROMS bulk flux module (Fairall et al. 1996, Large 2006). 본 위키의 models/<MODEL>/manual-notes/ 가 채워지면 verified 승급."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-23
verification_by: "Claude Opus 4.7 (1M context) — 골격 작성, 각 모델 manual cross-ref 대기"
verification_date: 2026-05-23
related:
  - concepts/sst/02-theory.md
  - models/EFDC/
  - models/Delft3D/
  - models/ROMS/
---

# SST 모델 적용

> 본 §는 SST(또는 수온 일반) 가 연안 수치모델에 어떻게 들어가는지·어떻게 나오는지 정리. EFDC·Delft3D·ROMS·ADCIRC·XBeach·SWAN 모델별 차이.

> **citation_status: source-needed** — 각 모델 manual 의 정확한 equation·파일 형식 인용은 `models/<MODEL>/manual-notes/` 작업 후 verified. 본 노트는 표준 oceanographic 모델 관행 기반 골격.

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

EFDC 의 heat budget 계산 (`calheat.f90`, citation TODO):
- bulk flux 4개 항 매 timestep 계산
- vertical thermal diffusion (Mellor-Yamada 또는 k-ε)
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

Delft3D-FLOW heat model 5 옵션 (Manual, Lesser 2004):
1. **No heat** — passive temperature transport
2. **Absolute** — $Q_{tot}$ 직접 입력
3. **Murakami** — 1.5-D parameterization
4. **Ocean** — Octavio (Octavio et al. 1977) bulk
5. **Composite** — 4 항 (Q_SW + Q_LW + Q_S + Q_L) 분리 계산 — **권장**

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

ROMS 는 **COARE 3.0 algorithm** (Fairall et al. 1996) 사용:
- 4개 항 + stability correction
- gustiness factor for low-wind cases
- iterative solution for cool-skin and warm-layer

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

## 11. TODO (verified 승급 조건)

1. ☐ `models/EFDC/manual-notes/heat-bulk-flux.md` — EFDC+ Manual §3 인용
2. ☐ `models/Delft3D/manual-notes/heat-module.md` — Delft3D-FLOW Manual heat 5 옵션 비교
3. ☐ `models/ROMS/manual-notes/coare30-bulk.md` — Fairall 1996 COARE 3.0
4. ☐ 각 모델의 한국 적용 paper citation (NIFS, KMOU, 해양과학기술원)
5. ☐ 실제 모델 입력 파일 예제 (EFDC `aser.inp`, Delft3D `*.bcc` 등) — `examples/` 폴더

## 12. 연결

- [`01-concept.md`](01-concept.md) — SST 정의
- [`02-theory.md`](02-theory.md) — 열수지 방정식
- [`03-analysis-methods.md`](03-analysis-methods.md) — climatology·anomaly
- [`04-code-and-tools.md`](04-code-and-tools.md) — SST 데이터 source
- [`models/EFDC/`](../../models/EFDC/), [`models/Delft3D/`](../../models/Delft3D/), [`models/ROMS/`](../../models/ROMS/) — 모델별 source/manual
- 외부:
  - Fairall et al. 1996 — Bulk parameterization air-sea fluxes (J. Climate 9:1747-1768)
  - Lesser et al. 2004 — Delft3D-FLOW 3D modeling (Coastal Engineering 51:883-915)
  - Tolman 1991 — wind input stability correction (J Phys Oceanogr 21:782-797)
