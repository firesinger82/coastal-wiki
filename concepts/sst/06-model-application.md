---
title: "SST 모델 적용 — boundary forcing · thermal module · 모델별 입력 형식"
topic: sst
canonical_source: self
citation_status: verified
has_source_needed: true
verification_method: "모델별 표층 열수지 구현 claim 을 검수완료 source-analysis 노트로 cross-link verified: (1) ROMS COARE bulk flux 4-항 + cool-skin → models/ROMS/source-analysis/roms_bulk_flux_coare.md (bulk_flux.F 1623줄 직접 read, COARE 1996/2003/Edson2013 8 paper) + roms_atmospheric_forcing.md (COARE 3.0 3-iter loop, longwave 3 옵션, shortwave penetration SOLAR_SOURCE, file:line 인용). (2) Delft3D heat KTEMP 5 dispatch + ocean/Proctor COARE-style bulk + Murakami 4-항 → models/Delft3D/source-analysis/delft3d_heat.md (heatu.f90:162-1276 직접 분석). (3) EFDC 연직 수온 transport/layering(sigma·SGZ)·vertical advection → models/EFDC/source-analysis/efdc_vertical.md (caltran.f90·caluvw.f90 file:line). \n**2026-09-28 토큰 재분류·정정**: (4) EFDC 표층 heat budget → models/EFDC/source-analysis/efdc_heat_temperature.md (EFDC+ mod_heat.f90 CALHEAT :52-1093, ISTOPT(2) 5 분기, Full Heat Balance 3 flux 하드코딩 :648-651, COARE 3.6 :691-773) + efdc_surface_forcing.md §4 (ASER :332-470) 로 이미 verified 였음 — 'calheat source-analysis 미작성' 은 stale. (5) ★§8 SWAN 정정: 구 서술 'S_in 에 Tolman(1991) stability correction, SET LEVel=auto' 는 틀림. SET [level] 은 수위 증분(swanuse.pdf PDF p.35, swanpre1.ftn:2170 INREAL('LEVEL',WLEV)). ASTD(기온-수온차)는 INPGRID ASTD(swanpre1.ftn:1388-1391)·WIND ASTD(:2780, CASTD) 로 읽혀 보간·저장·출력(swanmain.ftn:4972-4974, swanout1.ftn:2714)만 되고 swancom1-5.ftn·SdsBabanin.ftn90 의 ASTD 참조 0건, CASTD 는 초기화·읽기·0 대입 외 사용 0건 — 본 스냅샷 SWAN 풍입력 항은 안정도 보정을 하지 않는다. 여전히 source-needed: 각 모델 한국 적용 paper(NIFS/KMOU — experience/ 정책), SST forcing 데이터셋 endpoint(외부). §4.1 (2026-09-28): Delft3D-FLOW User Manual (models/Delft3D/raw/manuals/pdfs, pdftotext) App A.2.17 <name.bcc> p.467·A.2.18 <name.tem> p.472·MDF 예시 Sub1/Ktemp PDF p.451 + dimpro.f90:146-169 Sub1 파싱 직독 — .bct·.ext·Sub1=temp 서술 정정."
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

> **citation_status: verified** (모델 source-analysis cross-link 기반) — ROMS COARE bulk flux·Delft3D heat KTEMP·EFDC 연직 수온 transport 의 구현은 검수완료 source-analysis 노트(아래 링크)로 뒷받침. EFDC 표층 heat budget 커널도 검수완료 노트로 뒷받침(§3.2). **여전히 source-needed**: 한국 적용 paper(`experience/` 정책), SST forcing endpoint(외부).

## 1. SST 의 역할 — 입력 vs 출력

수치모델에서 SST 는 다음 중 하나:

| 역할 | 모델 종류 | 예 |
|---|---|---|
| **boundary condition** (입력) | barotropic ocean (조위·조류) | ADCIRC, SWAN, XBeach (1D barotropic) |
| **prognostic 변수** (모델이 계산) | baroclinic ocean (3D) | EFDC, Delft3D-FLOW, ROMS, HYCOM |
| **forcing 입력** | wave·sediment 모델 (열적 stratification 영향) | SWAN+ADCIRC coupled, Delft3D wave-flow |

EFDC·Delft3D-FLOW·ROMS 는 **prognostic 3D** 그룹 — SST 를 boundary/forcing 입력 + 내부 계산 + 출력 모두 다룬다.

## 2. Prognostic 3D 모델의 SST 처리

### 2.1 표층 열수지 방정식

수치모델 내부 표층 열수지 ([`02-theory.md`](02-theory.md) §1 eq. 5.1):

$$\rho C_p h \frac{\partial T}{\partial t}\bigg|_{\text{surface layer}} = Q_{SW} - Q_{LW} + Q_S + Q_L$$

($h$ = 표층 두께. 아래 bulk 식에서 $Q_S$·$Q_L$ 은 공기−해수 차이로 부호를 포함하고 $Q_{LW}$ 는 해양 손실을 양으로 둔다.)

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
- **표층 열교환** — **verified**: [`efdc_heat_temperature.md`](../../models/EFDC/source-analysis/efdc_heat_temperature.md) §0·§1. EFDC+ 에서는 별도 `calheat.f90` 이 아니라 `mod_heat.f90` 의 `CALHEAT`(:52-1093)이며, `ISTOPT(2)` 로 0 무 · 1 Full Heat Balance · 2 COARE 3.6 · 3 W2 평형온도 · 4 외부 평형온도 5 분기(:629-863). 이론 짝은 [`efdc-theory-v12-ch5-temperature-heat.md`](../../models/EFDC/manual-notes/efdc-theory-v12-ch5-temperature-heat.md).
- **연직 thermal transport / advection** — 수온은 EFDC 의 일반 tracer 로 연직 upwind advection (`caltran.f90:152-183`) 되며, sigma/Sigma-Zed(SGZ) 연직 격자(`KC`·`IGRIDV`)에 따라 layer thickness `HPK = HP·DZC` 로 분배됨. **verified**: [`models/EFDC/source-analysis/efdc_vertical.md`](../../models/EFDC/source-analysis/efdc_vertical.md) §A·§D (sigma layers·vertical advection). 가파른 지형에서 sigma 좌표 spurious diapycnal mixing 이 인공 성층(SST 연직 구조 왜곡)을 만들 수 있다. **EFDC+ Stable 12.5 기준**으로는 `IINTPG` buoyancy shear 분기가 제거됐으며 급경사 대응은 `IGRIDV>0`(SGZ)을 사용한다. `IINTPG /= 0`은 `setbcs.f90:449`의 2-cell-wide 수로 external density gradient cell-face flag 처리를 끄는 부작용이 있다 (efdc_vertical.md §E·Working Rules).
- horizontal advection

> 표층 열수지 상수: Full Heat Balance 의 장파·현열·잠열 계수는 소스 하드코딩(`mod_heat.f90:648-651`, [`efdc_heat_temperature.md`](../../models/EFDC/source-analysis/efdc_heat_temperature.md) §1.1), 방사율 ε = 0.97(Theory v12 Ch5 노트 표), `aser.inp` 대기강제 보간·포화증기압·증발 wind function 은 [`efdc_surface_forcing.md`](../../models/EFDC/source-analysis/efdc_surface_forcing.md) §4. 구름 인자는 이론식 인쇄 `(1+0.8C)` 와 소스 `(1-0.8C)` 가 다르다(heat 노트 §1.1 ⚠).

### 3.3 출력

EFDC 의 SST 출력:
- `wsec.out` 또는 `EE_WS.OUT` — 표층 수온 시계열
- NetCDF (`OUT_NCDF`) — 격자 SST

## 4. Delft3D-FLOW 의 SST 처리

### 4.1 입력 (Delft3D-FLOW 4.x)

| 파일 | 역할 | 근거 |
|---|---|---|
| `*.mdf` `Sub1` | 앞 4글자 중 **어느 자리든 `T`(대소문자 무관)** 가 있으면 수온 활성 (`S` 염분·`I` 이차류·`W` 바람도 같은 방식, 예 `Sub1 = #ST W#`) | `dimpro.f90:146-169` (`models/Delft3D/raw/source_code/Delft3D/src/engines_gpl/flow2d3d/packages/flow2d3d_io/src/input/`) · FLOW User Manual MDF 예시 PDF p.451 |
| `*.mdf` `Ktemp` | heat flux 모델 선택 (0 = 없음) | 같은 MDF 예시 · 분기 구현은 §4.2 [`delft3d_heat.md`](../../models/Delft3D/source-analysis/delft3d_heat.md) |
| `*.bcc` | **수송 경계(염분·수온) 시계열** — 경계 구간별 header + data 블록, 연직 분포 `Uniform`·`Linear`·`Step`·`3d-profile` | FLOW User Manual App A.2.17 p.467 |
| `*.tem` | heat flux 모델 시간 입력(기온·상대습도·운량·일사 등, 모델 번호별 레코드) | 같은 매뉴얼 App A.2.18 p.472 |
| `*.bct` | 수리(수위·유량) 경계 시계열 — **수온 입력 아님** | [`delft3d-flow-boundary-forcing.md`](../../models/Delft3D/manual-notes/delft3d-flow-boundary-forcing.md) §6 |

> ★정정 (2026-09-28): 구판은 `.bct` 를 "수온 시계열 옵션", `.ext` 를 D3D-4 FLOW 의 meteo 입력, 활성화를 `Sub1 = 'temp'` 로 적었다.
> 수온 경계는 `.bcc`, heat 강제는 `.tem` 이다. `.ext` 는 D-Flow FM 의 외부 강제 파일이다. `'temp'` 는 `t` 를 포함해 우연히 동작할 뿐 문서 규약이 아니다.

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

> 한국 적용 사례는 바이블 검증(객관 데이터·출처 인용 paper) 후 experience/ 에 카테고리화 — 본 canonical 미수록 (source-needed).

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
- ROMS 한국 동해 적용(예: NIFS 동해예측시스템 KOOS-EJS) — 출처 인용 paper 확보 후 experience/ 카테고리화, 본 canonical 미수록 (source-needed)

## 6. ADCIRC 의 SST 처리

### 6.1 ADCIRC v55 은 barotropic 우선

ADCIRC 기본 모드: 2DDI (depth-integrated) → 수온 무관. 그러나:

- **baroclinic 모드** — baroclinic 빌드에서 수온 입력 가능 (드물게 사용; 예: `models/ADCIRC/raw/source_code/adcirc-testsuite/adcirc/adcirc_baroclinic_2d_serial/`). ※ `NWS=13` 은 baroclinic 옵션이 아니라 OWI NetCDF wind/pressure forcing 포맷 — [`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md`](../../models/ADCIRC/source-analysis/adcirc-fort-files-reference.md) fort.22 항목 참조
- **Coupled SWAN+ADCIRC** — wave 만 결합, SST 직접 forcing 없음
- **Hot-start temperature** — initial T field 옵션

대부분의 한국 ADCIRC 적용 (storm surge) 은 SST 무관.

## 7. XBeach 의 SST 처리

XBeach: 단기 (storm) 사건 surf zone 모델 — **SST 무관**.

XBeach 에는 수온 변수가 없다 — `src/xbeachlibrary/*.F90` 전체에서 `temperature` 0 건(2026-09-29 grep). 밀도는 사용자 상수 `rho`(기본 1025, `params.F90:295`), 수평점성도 사용자 상수 `nuh`(기본 0.1, `:744`)라 수온이 들어갈 경로가 없다. ★정정: 구판의 "viscosity 계산에 수온 영향 가능" 은 근거가 없어 뺐다.

## 8. SWAN 의 SST 처리

SWAN: spectral wave 모델 — **SST 직접 사용 안 함.** 기온-수온차도 풍입력에 쓰이지 않는다.

- SWAN 은 기온-수온차 `ASTD` 를 **읽기는 한다** — 공간장 `INPGRID ASTD`(`swanpre1.ftn:1388-1391`), 상수 `WIND ... ASTD`(`:2780`, `CASTD`).
  그러나 값은 보간·저장·출력(`swanmain.ftn:4972-4974`, `swanout1.ftn:2714`)만 되고, 풍입력·소스항 파일
  (`swancom1-5.ftn`, `SdsBabanin.ftn90`)에 `ASTD` 참조가 **0 건**, `CASTD` 도 초기화·읽기·0 대입 외 사용이 없다.
  → 본 위키 스냅샷의 SWAN $S_{in}$ 에는 **대기 안정도 보정이 없다**. 사용자 매뉴얼도 `ASTD` 를 기술하지 않는다.
- ★정정 (2026-09-28): 구판은 "$S_{in}$ 에 Tolman(1991) stability correction, 기본값 `SET LEVel=auto`" 라 적었다.
  `SET [level]` 은 **공간·시간 상수 수위 증분(m), 기본 0** 이다(swanuse.pdf PDF p.35; `swanpre1.ftn:2170` `INREAL('LEVEL',WLEV)`).
  Tolman(1991) 은 SWAN 기술매뉴얼에서 WAVEWATCH III 모델 자체의 인용으로 등장할 뿐이다(swantech.pdf §1.1 Historical background, PDF p.9) — SWAN 풍입력 근거로 인용하지 말 것.

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

## 10. SST 경계 입력의 기준기간 검토

검토 항목: SST 경계 입력에 사용한 climatology의 기준기간과 모델 적용 기간을 기록하고 비교한다.

입력자료의 갱신 여부와 anomaly 반영 방법은 적용 해역·기간에 맞춰 검토한다. 관련 사례는 [`experience/khoa-sst-warming-trend.md`](../../experience/khoa-sst-warming-trend.md) §8.1을 탐색용으로 참조한다.

## 11. TODO (잔존 source-needed — verified 부분은 §3-5 cross-link 참조)

verified 완료 (모델 source-analysis cross-link):
- ☑ ROMS COARE bulk flux — [`roms_bulk_flux_coare.md`](../../models/ROMS/source-analysis/roms_bulk_flux_coare.md) + [`roms_atmospheric_forcing.md`](../../models/ROMS/source-analysis/roms_atmospheric_forcing.md)
- ☑ Delft3D heat KTEMP dispatch — [`delft3d_heat.md`](../../models/Delft3D/source-analysis/delft3d_heat.md)
- ☑ EFDC 연직 수온 transport/layering — [`efdc_vertical.md`](../../models/EFDC/source-analysis/efdc_vertical.md)

잔존:
1. ☑ EFDC 표층 heat budget — [`efdc_heat_temperature.md`](../../models/EFDC/source-analysis/efdc_heat_temperature.md) (EFDC+ `mod_heat.f90` `CALHEAT`), 이미 verified 였음(2026-09-28 확인)
2. ☑ Delft3D heat 매뉴얼 — [`delft3d-flow-physics-numerics.md`](../../models/Delft3D/manual-notes/delft3d-flow-physics-numerics.md) §10 (Manual §9.8 heat flux 5 모델) + [`delft3d-flow-user-manual.md`](../../models/Delft3D/manual-notes/delft3d-flow-user-manual.md) §4.5.7.3 ↔ [`delft3d_heat.md`](../../models/Delft3D/source-analysis/delft3d_heat.md)
3. ☐ 각 모델의 한국 적용 paper citation (NIFS, KMOU, 해양과학기술원)
4. ☐ 실제 모델 입력 파일 예제 (EFDC `aser.inp`, Delft3D `*.bcc` 등) — `examples/` 폴더
5. ☑ SWAN stability correction — 소스 직독 결과 **SWAN 풍입력에 없음**, §8 정정(2026-09-28)

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
