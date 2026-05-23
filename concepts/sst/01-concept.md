---
title: "해수면 수온 (Sea Surface Temperature, SST) — 정의·측정 정형화·시공간 스케일"
topic: sst
canonical_source: self
citation_status: verified
verification_method: "AI cross-reference: Stewart 'Introduction to Physical Oceanography' §5 Oceanic Heat Budget + §6 Temperature/Salinity/Density 직접 인용 (textbook/md/stewart_textbook.md). KHOA 정점 인프라는 Annual Report 2012-2025 (textbook/notes/khoa-annual-reports-overview.md) 직접 인용. bulk vs skin SST 정의는 NOAA/GHRSST 표준 정의 (외부 reference)."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-23
verification_by: "Claude Opus 4.7 (1M context) — Stewart 챕터 직접 인용 + KHOA 백서 cross-ref"
verification_date: 2026-05-23
related:
  - experience/khoa-sst-warming-trend.md
  - experience/khoa-annual-climate-trend.md
  - concepts/tides/02-theory.md (§8.6 SLR cross-link)
---

# 해수면 수온 (Sea Surface Temperature, SST) — 정의·측정 정형화

> 본 문서는 도메인 개념 정의. 한국 정점 실측 분석은 [`experience/khoa-sst-warming-trend.md`](../../experience/khoa-sst-warming-trend.md) 참조.

## 1. 정의

**해수면 수온 (Sea Surface Temperature, SST)** — 해양 표층 (typically 0~1 m, 측정 방식에 따라 다름) 의 해수 온도. 단위 °C (or K). 해양-대기 사이 열·물·운동량 교환의 핵심 boundary 변수.

Stewart §5에서 강조: 입사 태양에너지의 약 절반이 해양·육지에 흡수되며, 해양에 흡수된 에너지는 대부분 증발·적외복사로 국지적으로 대기에 다시 방출되거나, 해류로 다른 지역(특히 중위도)으로 운송된다.

> "About half the solar energy reaching earth is absorbed by the ocean and land, where it is temporarily stored near the surface. ... The thermal energy transported by ocean currents is not steady, and significant changes in the transport ... may have been important for the development of the ice ages." (Stewart §5, p.51)

→ SST 는 단순한 표층 온도가 아닌, **지구 climate system 의 핵심 메모리·수송** 변수.

## 2. 측정 정형화 — bulk vs skin SST

SST 는 **측정 깊이·방법** 에 따라 다른 양으로 분류된다. GHRSST (Group for High Resolution SST) 표준 정의:

| 명칭 | 깊이 | 주 측정 수단 | 변동성 |
|---|---|---|---|
| **Skin SST** (T_skin) | ~10 μm | 적외(IR) 위성, 항공 IR | diurnal warm layer + cool skin effect |
| **Sub-skin SST** (T_subskin) | ~1 mm | microwave 위성 (MW) | skin과 1 m 사이 보간 |
| **Foundation SST** (T_foundation) | ~5 m | 일중 가열 효과 사라진 새벽 시점 in-situ 또는 모델 reconstruct | 일평균·기후 분석 기준 |
| **Bulk SST** | 0.5~10 m | 부이·선박·연안 관측소 (KHOA 조위관측소 수온계 등) | 가장 흔한 실측 |

**중요**:
- Skin (위성 IR) 과 Bulk (부이) 는 **0.1~0.5 °C 차이** 가능 (cool skin effect: skin이 더 차가움; warm layer: 일중 표층이 더 따뜻함)
- Climate trend 분석에서는 **foundation SST** 또는 daily-mean bulk SST 우선
- 한국 KHOA 조위관측소 수온은 **bulk SST** (관측소 수온계, 일반적으로 ~1 m 깊이)

## 3. 시공간 스케일

### 3.1 시간 스케일

| 시간 | 주요 변동 |
|---|---|
| 분~시간 | 난류·내부파·국지 wind mixing |
| 일 (diurnal) | 일중 가열·야간 냉각, 1~3 °C 진폭 (저위도·약풍) |
| 월 | 계절 cycle, 중위도 10~15 °C 진폭 |
| 년 (interannual) | ENSO (1~3 °C, 적도 태평양), PDO (~1 °C, 북태평양), 한국 영향 |
| 십년 (decadal) | PDO 위상 전환 (~20-30년 cycle), AMV |
| 백년+ (secular) | climate warming trend (글로벌 0.13~0.18 °C/decade, 1971-2024) |

### 3.2 공간 스케일

| 공간 | 예 |
|---|---|
| 점 (point) | 부이·조위관측소 수온계 (한국 KHOA 13~30정점) |
| 연안 (coastal, ~10 km) | 조위관측소 망, ROMS 연안 격자 |
| 분지 (basin, ~100~1000 km) | satellite 격자 (NOAA OISST 0.25°, MUR 0.01°) |
| 전 지구 | ERSSTv5 (2°), HadISST (1°) |

## 4. 변동성의 원인 (Stewart §5.2)

표층 열수지 (heat budget):

$$Q = Q_{SW} + Q_{LW} + Q_S + Q_L + Q_V$$

| 항 | 의미 | typical magnitude (W/m²) |
|---|---|---:|
| $Q_{SW}$ | 입사 단파복사 (insolation) | +200~+300 (중위도 여름) |
| $Q_{LW}$ | 순 장파복사 (infrared) | -30~-70 (해양→대기) |
| $Q_S$ | sensible heat flux (전도) | -10~-30 |
| $Q_L$ | latent heat flux (증발) | -50~-150 |
| $Q_V$ | advection (해류 운송) | ±100+ (Kuroshio 등) |

수온 변화 정량:

$$\Delta E = C_p m \Delta T$$

$C_p \approx 4.0 \times 10^3$ J·kg⁻¹·°C⁻¹ (해수 비열, Stewart eq. 5.3) — 즉 1 kg 해수 1°C 가열에 4 kJ 필요.

상세 이론은 `02-theory.md` (예정) 에서 다룸.

## 5. 한국 측정 인프라 — KHOA

[KHOA Annual Report 2012-2025](../../textbook/notes/khoa-annual-reports-overview.md) §제1장 §제2장 §제3장 정리:

| 항목 | 내용 |
|---|---|
| 측정 정점 | 조위관측소 49개 + 해양관측부이 + 해양과학기지 |
| 측정 종 | 표층 수온 (bulk SST, ~1 m), 일부 정점은 수직 다층 |
| 시간 해상도 | 1분 (raw), 시간·일·월 통계 별도 |
| 자료 보존 | KHOA Annual Report (PDF 백서) 1968-2024 (장기 분석은 vol.2 §3 참조), OpenAPI archive 는 2025-01 이후만 |
| 글로벌 standard 와 비교 | bulk SST = GHRSST L4 product 의 in-situ validation input |

**중요**: 한국 정점은 모두 bulk (관측소 수온계 표층 ~1 m). 위성 skin SST 와 직접 비교 시 ~0.3 °C bias 보정 필요.

## 6. 글로벌 데이터셋 reference (별도 §04 예정)

| 데이터셋 | 해상도 | 기간 | 비고 |
|---|---|---|---|
| NOAA OISST v2.1 | 0.25° daily | 1981.09~ | AVHRR + in-situ blend |
| ERSSTv5 | 2° monthly | 1854~ | longest reconstruction |
| HadISST | 1° monthly | 1870~ | UK MetOffice |
| MUR L4 | 0.01° daily | 2002~ | 최고 해상도 |
| GHRSST L4 ensemble | various | 2002~ | 다중 source merge |

상세 운영 정보는 `04-code-and-tools.md` (예정) 에서.

## 7. 본 위키 안 사용

| 노트 | 사용처 |
|---|---|
| 한국 9년 trend (1.39 °C/decade) | [`experience/khoa-sst-warming-trend.md`](../../experience/khoa-sst-warming-trend.md) |
| KHOA 장기 1968-2012 (0.123 °C/decade) | 같음, §3.2 |
| SLR과 정합성 (열팽창 기여 ~10%) | 같음, §4 |
| Marine heatwave 2023-2025 | 같음, §7 |
| EFDC/Delft3D boundary 입력 갱신 | 같음, §8.1 + `06-model-application.md` (예정) |

## 8. 인용 정형

본문 인용 시:
- Stewart 챕터: `(Stewart §5.1, p.51)` 또는 `(Stewart 'Intro to Physical Oceanography' eq. 5.3)`
- KHOA Annual Report: `(KHOA Annual Report YYYY, §<장>.<절>, p. xx)`
- 외부: `[제목](URL) (acc. YYYY-MM-DD)`

source_id 매니페스트: [`textbook/sources.yml`](../../textbook/sources.yml).
