---
title: "SWAN WINK 패턴 — 사용자 본인 13 middle + 56 detail 도메인"
source_id: swan-library-firesinger
chapter: "metadata/wink_middle_areas.csv + wink_detail_areas.csv"
pages: "—"
page_offset_applied: false
topic: waves
canonical_source: self
citation_status: verified
verification_method: "AI cross-reference: D:\\Numerical_models\\01_Models\\swan\\Fin\\07_SWAN_LIBRARY\\metadata\\ 의 CSV 직접 파싱. 사용자 본인 정리한 13 middle + 56 detail 영역."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-21
verification_by: "Claude Opus 4.7 (1M context) — cross-ref"
verification_date: 2026-05-21
---

# SWAN WINK 패턴 (사용자 본인 운용)

> 출처: `swan-library-firesinger` = `D:\Numerical_models\01_Models\swan\Fin\07_SWAN_LIBRARY\metadata\`

## 1. WINK 정의

WINK = 사용자가 정의한 SWAN nested domain set. 한국 연안 spectrum 생성용 표준 영역 모음. 두 단계:

- **Middle domain (M)**: 0.005° (≈ 500 m) 격자, ~1.5° × 1° 영역. 한국 연안 전체 커버 (서·남·동해)
- **Detail domain (D)**: 0.0015° (≈ 150 m) 격자, ~0.05-0.3° 영역. 항만·정점 sub-domain

## 2. Middle Domain (13 영역, 0.005°)

서해 5 + 남해 4 + 동해 4 = 13.

### 2.1 서해 (West, 5 영역)

| Code | lon (min~max) | lat (min~max) | 면적 (°²) | 비고 |
|---|---|---|---|---|
| **MW_01** | 124.4500–125.9500 | 37.4000–38.3000 | 1.5 × 0.9 | 백령·연평·인천 외해 |
| **MW_02** | 125.6000–126.9500 | 36.5000–38.0000 | 1.35 × 1.5 | 인천·태안·서산 |
| **MW_03** | 125.3600–126.8100 | 35.3000–36.8000 | 1.45 × 1.5 | 격포·군산·법성포 |
| **MW_04** | 125.5500–127.0000 | 33.8000–35.5000 | 1.45 × 1.7 | 영광·신안·진도·완도 |
| **MW_05** | 124.7000–125.7000 | 33.8000–35.0000 | 1.0 × 1.2 | 흑산도·홍도 외해 |

### 2.2 남해 (South, 4 영역)

| Code | lon | lat | 비고 |
|---|---|---|---|
| **MS_01** | 126.4500–128.1500 | 33.8500–35.0000 | 진도·완도·여수 |
| **MS_02** | 127.5000–128.9000 | 34.0000–35.2000 | 여수·통영 |
| **MS_03** | 128.4000–129.8000 | 34.0000–35.6000 | 통영·부산·기장 |
| **MS_04** | 129.2500–130.2000 | 35.2000–36.6000 | 부산·울산·포항 입구 |

### 2.3 동해 (East, 4 영역)

| Code | lon | lat | 비고 |
|---|---|---|---|
| **ME_01** | 129.2500–130.2000 | 35.2000–36.6000 | 동해 남부 (MS_04와 동일 extent) |
| **ME_02** | 128.9000–130.0000 | 36.4000–37.9000 | 영덕·삼척·동해 |
| **ME_03** | 128.3000–129.5000 | 37.4000–38.7000 | 강릉·속초·고성 |
| **ME_04** | 130.6000–132.1000 | 37.0000–37.8000 | **울릉도** (별도) |

## 3. Detail Domain (56 영역, 0.0015°)

주요 항만·검증 정점별. 영역 크기 ~0.05-0.3°. 격자 dx=dy=0.0015° (≈ 150 m).

### 3.1 서해 detail (24개)

연평도항·용기포항·인천항/경인항·대산항·태안항·평택당진항·보령항/대천항·비인항·상왕등도항·장항항/군산항·땅끝항·목포항·송공항·진도항·화흥포항·추자항·가거항리항·홍도항·흑산도항·...

### 3.2 남해 detail (16개)

(분포 상세는 wink_detail_areas.csv 참조)

### 3.3 동해 detail (16개)

영덕(고래불)·후포항·호산항·**묵호항**·**삼척항**·주문진항·옥계항·**속초항**·**포항항**·**동해항**·**울릉항** 등.

### 3.4 사용자 주력 검증 영역 (축산항)

**축산항 (CUSTOM_CHUKSAN)** — 별도 정의 (`metadata/custom_detail_areas.csv`):
- 좌표: 약 129.45°E, 36.51°N
- 가장 가까운 검증 정점: MPT238 영덕(고래불) ~7.5 km, TW_0095 ~7.7 km
- 자료: `metadata/validation_stations_chuksan.csv`

## 4. Nesting 구조

```
Layer 0: WW3 글로벌 hindcast (NOAA 등)
   ↓ NESTOUT (boundary spectrum)
Layer 1: SWAN coarse (한국 인근)
   ↓ NESTOUT
Layer 2: SWAN middle (MW_xx · MS_xx · ME_xx, 13 영역, 0.005°)
   ↓ NESTOUT
Layer 3: SWAN detail (56 영역, 0.0015°)
   ↓
검증: MPT/TW 정점
```

각 단계 출력 NESTOUT을 다음 단계 boundary 입력으로 사용.

## 5. 입력 데이터 통합

| 입력 | 출처 | tool |
|---|---|---|
| **수심** (외해) | BADA2024/GEBCO | `build_swan_depth_from_parquet.py` (외해 영역 자동 처리) |
| **수심** (정밀, 연안) | `대표수심_MSL.parquet` | 동상 |
| **수심** (hybrid) | 두 source 합성 | `build_smooth_hybrid_middle_depth.py` |
| **수심** (AHHW 보정) | 약최고고조면 = MSL + Z₀ | `build_ahhw_depths.py` |
| **바람** | JMA-MSM (5 km, 1시간) | `build_jma_uv_monthly.py` |
| **경계 spectrum** | 상위 layer NESTOUT 또는 archive | (SWAN 입력) |
| **조류** (선택) | EFDC/ADCIRC 또는 KHOA 수치조류도 | `concepts/currents/06-model-application.md` |

### 5.1 AHHW 수심 ([`concepts/tides/02-theory.md` §8.2](../../../concepts/tides/02-theory.md))

```
AHHW = MSL + Z₀ = MSL + (H_M2 + H_S2 + H_K1 + H_O1)
```

→ SWAN 수심 입력에 AHHW 적용 (가장 보수적, 폭풍해일·태풍 시 유효). 또는 MSL·LWL·HWL 별 시나리오.

### 5.2 JMA-MSM 바람 워크플로

```
raw daily NC:    01_Make_Wind_field/JMA_NC_HANDLING/YYYY/MMDD.nc
daily u/v NC:    07_SWAN_LIBRARY/generated/jma_msm/uv_daily/YYYY/MMDD_uv.nc
monthly u/v NC:  07_SWAN_LIBRARY/generated/jma_msm/uv_monthly/YYYY/jma_msm_uv_YYYYMM.nc
yearly u/v NC:   07_SWAN_LIBRARY/generated/jma_msm/uv_yearly/jma_msm_uv_YYYY.nc
```

빌드 명령:
```bash
/mnt/d/Projects/축산항/SWAN/.venv/bin/python3 \
  07_SWAN_LIBRARY/tools/build_jma_uv_monthly.py \
  --year 2025
```

CDO 기반 NetCDF 압축·합치기.

## 6. spectrum_archive 비전 (Layer 2+ 미래)

[`swan-library-firesinger/references/spectrum_archive_roadmap.md`](본 source)에 명시:

### Layer 1 — WINK-Compatible Baseline (operational)
- 13 middle NESTOUT files
- WINK detail boundary files
- Point outputs (validation)
- 공식 reference dataset

### Layer 2 — General Coastal Spectrum Archive
- **임의** detail domain boundary 생성용 spectral DB
- 외부 SWAN 재실행 **불필요한** nesting

### Layer 3 — Suitability Checker
- 새 detail 도메인 boundary가 archive 데이터로 충분한지 자동 판정
- accept / reject 자동 결정

→ 사용자가 운용 중인 영역. wiki에서는 `experience/swan-spectrum-archive-vision.md` (작성 검토) 또는 본 노트 갱신.

## 7. 보강

- 13 middle 도메인별 typical wind·H_s climate (`concepts/waves/05-examples.md`에 통합)
- 56 detail 도메인 전체 목록 (현재 본 노트는 일부만)
- 사용자 축산항 모델 실행 결과 (RMSE·Bias) → `experience/` 별도
- spectrum_archive 3-layer 실제 구현 진척

## 8. 연결

- `concepts/waves/04-code-and-tools.md` §2.4 — WINK 패턴 개관
- `concepts/waves/06-model-application.md` §2 — Nested SWAN 워크플로
- [`models/SWAN/manual-notes/swan-action-balance.md`](../manual-notes/swan-action-balance.md) — SWAN 알고리즘
- `swan-library-firesinger` source — 모든 metadata CSV
- 외부:
  - SWAN: [https://swanmodel.sourceforge.io/](https://swanmodel.sourceforge.io/)
  - JMA-MSM: 일본기상청 MSM 5km wind
  - BADA2024/GEBCO: 외해 수심
