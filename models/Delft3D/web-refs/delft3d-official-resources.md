---
title: "Delft3D 공식 자료 — Deltares·GitHub·핵심 논문 (Lesser 2004 등) 큐레이션"
topic: delft3d-web-refs
canonical_source: self
citation_status: verified
verification_method: "Deltares 공식 도메인 (oss.deltares.nl) + GitHub 공개 repo (Deltares/delft3d). 핵심 논문 인용은 publicly-known canonical works (Lesser et al. 2004, Stelling & Duinmeijer 2003)."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-24
verification_by: "Claude Opus 4.7 (1M context) — URL + 공인 논문 인용"
verification_date: 2026-05-24
related:
  - models/Delft3D/README.md
---

# Delft3D 공식 자료 큐레이션

> [`models/Delft3D/README.md`](../README.md) 의 정체 카드 외부 references 확장.

## 1. 공식 사이트

| 자원 | URL | 활용 |
|---|---|---|
| **Deltares Delft3D** | [https://oss.deltares.nl/web/delft3d](https://oss.deltares.nl/web/delft3d) | 공식 홈 — Delft3D 4 + Delft3D FM |
| **Delft3D-FM** | [oss.deltares.nl/web/delft3dfm](https://oss.deltares.nl/web/delft3dfm) | Flexible Mesh variant |
| **Manuals download** | Deltares 공식 사이트 내 (PDF download) | FLOW + WAVE + SED + WAQ 각 user manuals |

## 2. Code repository

| Repo | 역할 |
|---|---|
| **Deltares/delft3d** | [github.com/Deltares/delft3d](https://github.com/Deltares/delft3d) | Delft3D 4 (structured) + 일부 도구 |
| **Deltares/Delft-FIAT** | [github.com/Deltares/Delft-FIAT](https://github.com/Deltares/Delft-FIAT) | Flood Impact Assessment Tool |
| **Deltares/hydromt_delft3dfm** | [github.com/Deltares/hydromt_delft3dfm](https://github.com/Deltares/hydromt_delft3dfm) | Python HydroMT D3D-FM 설정 자동화 |

## 3. 핵심 논문 — 시초부터 현재까지

### 3.1 Foundation — FLOW + Morphology

- **Lesser, G.R., Roelvink, J.A., van Kester, J.A.T.M., Stelling, G.S. (2004)** "Development and validation of a three-dimensional morphological model" *Coastal Engineering* 51(8-9):883-915 — **Delft3D-FLOW + SED 통합 시초 paper**

### 3.2 수치 기법

- **Stelling, G.S., Duinmeijer, S.P.A. (2003)** "A staggered conservative scheme for every Froude number in rapidly varied shallow water flows" *Int. J. Numer. Meth. Fluids* 43:1329-1354 — D3D-FM staggered scheme
- **Kernkamp, H.W.J., Van Dam, A., Stelling, G.S., De Goede, E.D. (2011)** "Efficient scheme for the shallow water equations on unstructured grids with application to the Continental Shelf" *Ocean Dynamics* 61:1175-1188 — D3D-FM

### 3.3 모듈별 — WAVE / WAQ / PART

- **Delft3D-WAVE** = SWAN integration (Booij·Ris·Holthuijsen 1999 인용, [[../../SWAN/web-refs/swan-official-resources.md]])
- **Delft3D-WAQ** — Smits, J.G.C., Van Beek, J.K.L. (2013) "ECO: a generic eutrophication model" 등 다수
- **Delft3D-PART** — particle tracking module

### 3.4 Modern operational

- **van der Wegen, M., Roelvink, J.A. (2008)** "Long-term morphodynamic evolution of a tidal embayment using a two-dimensional, process-based model" *J. Geophys. Res. Earth Surface* 113:F03001 — 장기 morphology
- **Deltares (continual)** — Delft3D FM unstructured mesh modernization

## 4. 모듈별 활용

| 모듈 | 활용 | 본 위키 cross-ref |
|---|---|---|
| **Delft3D-FLOW** | 3D hydro (수온·염분·tide·current) | [[../source-analysis/]] 일부 |
| **Delft3D-WAVE** | SWAN 통합 (flow-wave 양방향 coupling) | [[../source-analysis/]] flow-wave coupling 노트 |
| **Delft3D-SED** | 표사 (Van Rijn + Partheniades-Krone) | [`concepts/sediment-transport/06-model-application.md`](../../../concepts/sediment-transport/06-model-application.md) |
| **Delft3D-WAQ** | 수질·eutrophication | (별도 작업) |
| **Delft3D-PART** | 입자 추적 (oil spill, dispersant) | `raw/manuals/pdfs/Delft3D-PART_*.pdf` |
| **Delft3D-WES** | Wind Enhanced Scheme | `raw/manuals/pdfs/Delft3D-WES_User_Manual.pdf` |

## 5. 한국 적용

- (별도 큐레이션 필요) 한국 항만·하구 D3D 적용 사례
- Delft3D 의 동중국해 + 황해 적용 — 다수 한국 학술 paper

## 6. 운영 자원

| 자원 | 비고 |
|---|---|
| **Deltares Public Wiki** | Delft3D 사용 안내, FAQ |
| **GitHub Issues** | [github.com/Deltares/delft3d/issues](https://github.com/Deltares/delft3d/issues) |
| **GitHub Discussions** | 사용자 Q&A |
| **Deltares Academy** | 정기 트레이닝 (FLOW·SED·WAVE 별) |
| Delft3D-PART memos | Dispersant·booms 운영 |

## 7. 본 위키 내 cross-ref

- [`concepts/sediment-transport/06-model-application.md`](../../../concepts/sediment-transport/06-model-application.md) — Delft3D-SED Van Rijn + Partheniades-Krone
- [`concepts/waves/`](../../../concepts/waves/) — Delft3D-WAVE (SWAN 통합)
- [`concepts/littoral-drift/`](../../../concepts/littoral-drift/) — surf zone + cross-shore profile
- [`models/Delft3D/source-analysis/`](../source-analysis/) — 10 verified 노트 (sparse, M-D 보강 후보)
- [`models/SWAN/`](../../SWAN/) — Delft3D-WAVE 의 backend (관련 모델)
