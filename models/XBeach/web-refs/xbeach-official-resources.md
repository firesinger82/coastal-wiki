---
title: "XBeach 공식 자료 — Deltares OpenEarth·SVN·핵심 논문 (Roelvink 2009 등) 큐레이션"
topic: xbeach-web-refs
canonical_source: self
citation_status: verified
verification_method: "Deltares 공식 도메인 (oss.deltares.nl, openearth.eu) + OpenEarth SVN + GitHub mirror (openearth/xbeach). 핵심 논문 인용은 publicly-known canonical works (Roelvink et al. 2009 Coastal Engineering)."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-24
verification_by: "Claude Opus 4.7 (1M context) — URL + 공인 논문 인용"
verification_date: 2026-05-24
related:
  - models/XBeach/README.md
---

# XBeach 공식 자료 큐레이션

> [`models/XBeach/README.md`](../README.md) 의 정체 카드 외부 references 확장.

## 1. 공식 사이트

| 자원 | URL | 활용 |
|---|---|---|
| **Deltares XBeach** | [https://oss.deltares.nl/web/xbeach](https://oss.deltares.nl/web/xbeach) | 공식 홈 |
| **XBeach Manual (online)** | [xbeach.readthedocs.io](https://xbeach.readthedocs.io/) | 운영 매뉴얼 |
| **OpenEarth XBeach** | [openearth.eu/xbeach](https://xbeach.readthedocs.io/ ⚠**구 openearth.eu/xbeach 는 도메인 사망(404, 2026-07-19 확인)**) | community + tools |

## 2. Code repository

| Repo | 역할 |
|---|---|
| **Deltares SVN** | [svn.oss.deltares.nl/repos/xbeach/](https://svn.oss.deltares.nl/repos/xbeach/) | 공식 (master + kingsday branches) |
| **GitHub mirror** | [openearth/xbeach](https://github.com/openearth/xbeach) | mirror, community contributions |

## 3. 핵심 논문 — 시초부터 현재까지

### 3.1 Foundation (2009)

- **Roelvink, D., Reniers, A., van Dongeren, A., van Thiel de Vries, J., McCall, R., Lescinski, J. (2009)** "Modelling storm impacts on beaches, dunes and barrier islands" *Coastal Engineering* 56(11-12):1133-1152 — **XBeach 시초 paper** (Katrina 후 (★구판 "Katrina/**Sandy**"는 시대착오 — Roelvink et al. 2009 는 2009 게재, Sandy 는 2012-10) dune erosion 대응)

### 3.2 운영 확장

- **McCall, R.T., Van Thiel de Vries, J.S.M., Plant, N.G., Van Dongeren, A.R., Roelvink, J.A., Thompson, D.M., Reniers, A.J.H.M. (2010)** "Two-dimensional time dependent hurricane overwash and erosion modeling at Santa Rosa Island" *Coastal Engineering* 57:668-683 — Hurricane Ivan
- **Smit, P., Stelling, G., Roelvink, D., Van Thiel de Vries, J., McCall, R., Van Dongeren, A., et al. (2010)** "XBeach: Non-hydrostatic model — Validation, verification and model description" *Delft Univ. Technol. tech report* — non-hydrostatic 모드
- **van Dongeren, A., Lowe, R., Pomeroy, A., Trang, D.M., Roelvink, D., Symonds, G., Ranasinghe, R. (2013)** "Numerical modeling of low-frequency wave dynamics over a fringing coral reef" *Coastal Engineering* 73:178-190 — coral reef + lagoon 적용

### 3.3 단기 vs 장기 morphology

- **Roelvink, D., Reniers, A. (2011)** *A Guide to Modeling Coastal Morphology* World Scientific — XBeach 운영 reference textbook

## 4. 운영 모드 — 3 variants

| 모드 | 사용 시점 | 참조 paper |
|---|---|---|
| **surfbeat** (default) | Storm impact, dune erosion, infragravity | Roelvink 2009 |
| **non-hydrostatic** | Boussinesq, depth-averaged | Smit et al. 2010 |
| **single-layer (stationary)** | 평균 wave climate | Roelvink 2011 |

본 위키 [[../source-analysis/xbeach_mode_dispatch]] — dispatcher 분석.

## 5. 한국 적용

- (예정) 한국 동해안 (강원도 안목항·낙산·속초) 폭풍 dune erosion 적용
- (별도 작업) XBeach 의 한국 모래 입경 (D50) calibration

## 6. 운영 자원

| 자원 | 비고 |
|---|---|
| **XBeach Tutorial** | xbeach.readthedocs.io/en/latest/tutorials/ — surfbeat·non-hydrostatic 운영 예제 |
| **GitHub Issues** | [openearth/xbeach/issues](https://github.com/openearth/xbeach/issues) |
| **Mailing list** | OpenEarth XBeach 사용자 메일링 |
| **Roelvink workshops** | Deltares 주관 정기 트레이닝 |

## 7. 본 위키 내 cross-ref

- [`concepts/littoral-drift/01-concept.md`](../../../concepts/littoral-drift/01-concept.md) §9 — XBeach surf module
- [`concepts/littoral-drift/02-theory.md`](../../../concepts/littoral-drift/02-theory.md) — Holthuijsen §7.4 radiation stress (XBeach surf zone 근간)
- [`concepts/sediment-transport/06-model-application.md`](../../../concepts/sediment-transport/06-model-application.md) — XBeach Soulsby-van Rijn + avalanching
- [`concepts/storm-surge/`](../../../concepts/storm-surge/) — storm 시 inundation + dune erosion 결합
- [`models/XBeach/source-analysis/`](../source-analysis/) — **33 verified**(2026-07-19 실측) 노트
- [`models/XBeach/manual-notes/`](../manual-notes/) — **4개 전량 verified** (2026-07-19 실측 — 구판 "3 source-needed"는 개수·상태 모두 stale)
