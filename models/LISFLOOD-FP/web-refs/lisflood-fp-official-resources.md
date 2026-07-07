---
title: "LISFLOOD-FP 공식 자료 — Bristol·SEAMLESS-WAVE·Zenodo v8.2·핵심 논문"
model: LISFLOOD-FP
canonical_source: external
external_source: "Zenodo API(record 13121102) 직접 query(2026-06-18) 로 v8.2 메타·라이선스·doi 확인 + WebSearch(2026-06-18) 로 Bristol/SEAMLESS-WAVE 공식 페이지 확인. 핵심 논문은 bibliographic."
citation_status: verified
verification_method: "Zenodo API 직접 query verbatim(title·version 8.2·doi:10.5281/zenodo.13121102·license gpl-2.0·pub 2024-07-29·LISFLOOD-FP-v8.2.zip 348MB). 공식 URL 은 WebSearch landing. 핵심 논문 서지는 bibliographic(원문 미fetch — DOI 교차확인 권장)."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - models/LISFLOOD-FP/README.md
  - models/LISFLOOD-FP/source-analysis/lisflood-fp-architecture-source-map.md
---

# LISFLOOD-FP 공식 자료

> ⚠ **LISFLOOD-FP**(Bristol/Sheffield 수리 침수) ≠ **LISFLOOD**(EC-JRC 분포형 강우-유출). 별개 모델.

## 1. 공식 채널

| 자료 | URL |
|---|---|
| Bristol 페이지 | <https://www.bristol.ac.uk/geography/research/hydrology/models/lisflood/> |
| SEAMLESS-WAVE (v8.x) | <https://www.seamlesswave.com/LISFLOOD8.0.html> |
| **v8.2 정본 소스** | Zenodo **doi:10.5281/zenodo.13121102** (<https://zenodo.org/records/13121102>) |

## 2. v8.2 메타 (Zenodo API verbatim)

- title: "LISFLOOD-FP v8.2 hydrodynamic model" · version **8.2** · pub **2024-07-29**
- doi: **10.5281/zenodo.13121102** · creators: "LISFLOOD-FP developers"
- license: **GPL-2.0** · file: LISFLOOD-FP-v8.2.zip (348 MB, 3170 files)
- 빌드: CMake ≥3.13, Windows(MSVC/Intel)·Linux. netCDF·libnuma 의존.

## 3. 핵심 논문 (bibliographic — DOI 교차확인 권장)

- **Bates, Horritt, Fewtrell (2010)** — "A simple inertial formulation of the shallow water equations for efficient two-dimensional flood inundation modelling." *J. Hydrology* 387:33-45. → **ACC(local inertia) 솔버**(`fp_acc.cpp`)의 정식 근거.
- **Neal, Schumann, Bates (2012)** — sub-grid channel(SGC) 정식화. → `sgc.cpp`.
- **Shaw, Sharma, Bates (2021)** — "LISFLOOD-FP 8.0: the new model release including FV1/DG2 solvers and GPU." *Geosci. Model Dev.* → swe/ FV1·DG2·GPU 도입.
- **Kesserwani & Sharifian (2020)** — DG2 + **multiwavelet 적응 격자**(SEAMLESS-WAVE). → 실구현은 `cuda/adaptive/`(hwfv1/mwdg2, [[lisflood-fp-mwdg2-adaptive-mra]]) — ~~`swe/dg2new.cpp`~~ 는 비가동 CPU 리팩터([[lisflood-fp-swe-fv1-dg2]] 정정). 코드 내 인용 `cuda/adaptive/cuda_adaptive_simulate.cu:104`.
- ⚠ 위 4편 원문 미fetch, 인용 시 DOI/페이지 cross-check.

## 4. 연결

- [[../README]] · [[../source-analysis/lisflood-fp-architecture-source-map]]
- 자매: [[../../SFINCS/README]] (Deltares reduced-complexity compound flooding) — ACC 계열과 동류 reduced-physics
- 개념: [[../../../concepts/storm-surge/07-ml-emulators]] (고속 침수 계열 비교)
