---
title: "Booij, Ris, Holthuijsen 1999 JGR — SWAN foundational paper (Part 1 + Part 2 cross-ref)"
topic: swan
canonical_source: external
external_source: "Booij N, Ris RC, Holthuijsen LH (1999), 'A third-generation wave model for coastal regions: 1. Model description and validation', JGR-Oceans 104(C4), 7649-7666, doi:10.1029/98JC02622 + Ris RC, Holthuijsen LH, Booij N (1999), 'A third-generation wave model for coastal regions: 2. Verification', JGR-Oceans 104(C4), 7667-7681, doi:10.1029/1998JC900123"
citation_status: verified
verification_method: "WebSearch + AGU/Wiley landing page metadata 직접 fetch (2026-06-01) — Part 1 DOI:10.1029/98JC02622 JGR 104 pp.7649-7666 abstract + bibliographic; Part 2 DOI:10.1029/1998JC900123 pp.7667-7681. Full text paywalled (HTTP 402 Wiley). Abstract 정확 인용 + scirp.org/ADS/Mendeley/Semantic Scholar 메타데이터 cross-check."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-06-01
verification_by: "Claude Opus 4.7 (1M context) — WebSearch + WebFetch attempt"
verification_date: 2026-06-01
related:
  - models/SWAN/manual-notes/swan-action-balance.md
  - models/SWAN/source-analysis/swan-foundation.md
  - models/SWAN/source-analysis/swan-source-terms-implementation.md
  - models/SWAN/source-analysis/wave/swan-source-terms-implementation.md
---

# Booij, Ris, Holthuijsen 1999 JGR — SWAN foundational paper

> 본 노트는 **SWAN 의 두 part 원논문 (Part 1 model + Part 2 verification)** 의 verified bibliographic + abstract 발췌. 본 위키 [[swan-action-balance]] 이 식 인용한 1차 출처. **Full text paywalled (Wiley HTTP 402)** — 본 노트는 abstract + bibliographic 기준 (compact).

## 1. Part 1 — Model description and validation

| 항목 | 값 | 출처 |
|---|---|---|
| Authors | N. Booij, R. C. Ris, L. H. Holthuijsen | 모든 인용처 일치 |
| Title | "A third-generation wave model for coastal regions: 1. Model description and validation" | Wiley + ADS |
| Journal | Journal of Geophysical Research: Oceans | AGU |
| Volume | 104, Issue C4 | ADS + Wiley |
| Pages | **7649-7666** | scirp.org + Google Scholar |
| Year | 1999 | 모든 인용처 |
| DOI | **10.1029/98JC02622** | Wiley + ADS |
| URL | https://agupubs.onlinelibrary.wiley.com/doi/10.1029/98JC02622 | Wiley |

### 1.1 Abstract (verified verbatim, WebSearch)

> "A third-generation numerical wave model to compute random, short-crested waves in coastal regions with shallow water and ambient currents (**Simulating Waves Nearshore (SWAN)**) has been developed, implemented, and validated."

### 1.2 Model description (verified verbatim, WebSearch)

> "The model is based on a **Eulerian formulation of the discrete spectral balance of action density** that accounts for refractive propagation over arbitrary bathymetry and current fields. As in other third-generation wave models, the processes of **wind generation, whitecapping, quadruplet wave-wave interactions, and bottom dissipation** are represented explicitly."

### 1.3 본 위키 [[swan-action-balance]] 와의 연결

- **Eulerian discrete spectral balance** → [[swan-action-balance]] 의 action balance equation $\partial N/\partial t + \nabla \cdot (\vec{c} N) = S_{tot}/\sigma$ 의 원논문
- **Refractive propagation** → [[swan-propagation-implementation]] 의 c_θ refraction speed 식 출처
- **Quadruplet wave-wave** → [[swan-source-terms-implementation]] / [[wave/swan-source-terms-implementation]] 의 DIA approximation 출처
- **Wind generation** → [[swan-wind-formulations-implementation]] (Komen / Yan / Janssen)
- **Whitecapping** → [[swan-whitecapping]] (Komen WCAP)
- **Bottom dissipation** → SWAN command `FRICTION` (JONSWAP / Madsen / Collins)

## 2. Part 2 — Verification

| 항목 | 값 |
|---|---|
| Authors | R. C. Ris, L. H. Holthuijsen, N. Booij |
| Title | "A third-generation wave model for coastal regions: 2. Verification" |
| Journal / Vol | JGR-Oceans, 104, C4 |
| Pages | **7667-7681** (Part 1 직후 paginated) |
| DOI | **10.1029/1998JC900123** |
| URL | https://agupubs.onlinelibrary.wiley.com/doi/10.1029/1998JC900123 |

→ Part 2 는 SWAN 검증 사례 (실측 정점·실험실 시험·다른 모델 비교).

## 3. 인용 정형 (본 위키 사용)

### 3.1 본문 단락 안

- `(Booij et al. 1999, JGR 104 pp.7649-7666, doi:10.1029/98JC02622)` — Part 1 model
- `(Ris et al. 1999, JGR 104 pp.7667-7681, doi:10.1029/1998JC900123)` — Part 2 verification

### 3.2 시카고 / 학술 인용 (긴 형식)

> Booij, N., R. C. Ris, and L. H. Holthuijsen (1999). "A third-generation wave model for coastal regions: 1. Model description and validation." *Journal of Geophysical Research: Oceans*, 104(C4), 7649-7666. doi:10.1029/98JC02622

> Ris, R. C., L. H. Holthuijsen, and N. Booij (1999). "A third-generation wave model for coastal regions: 2. Verification." *Journal of Geophysical Research: Oceans*, 104(C4), 7667-7681. doi:10.1029/1998JC900123

## 4. SWAN release history (선행 + 후속, citation_status: source-needed)

본 1999 paper 는 SWAN 1.0 가량 시기. 후속:
- 후속 paper 2x: Holthuijsen-Herman-Booij 2003 (diffraction) → [[swan-diffraction-obstacles]]
- ST6 source-term: Babanin / Rogers / Zieger 2010s → [[swan-st6-babanin-implementation]]
- Current SWAN 41.x 매뉴얼: [`models/SWAN/web-refs/swan-official-resources.md`](../web-refs/swan-official-resources.md)

## 5. Full text 미보유 — 후속 보강 가능 항목

- **Action balance equation (1) 의 정확한 LaTeX form** (현재 [[swan-action-balance]] 의 식 출처는 SWAN 매뉴얼 verbatim) — Part 1 §2 직접 인용 시 LaTeX 일치 검증
- **Eq 번호 cross-walk** Part 1 §2-3 (propagation + source term) ↔ SWAN 매뉴얼 ↔ 본 위키 노트
- **검증 case (Part 2)**: ★2026-07-19 원문(Ris et al. 1999 Part 2) 직접 대조 — 초록 "verified in stationary mode with measurements in **five real field cases**", §3 = **Haringvliet 1 + Norderneyer Seegat 2(저조·고조) + Friesche Zeegat 2**. 구판의 "NMI"·"Lake George Wave Tank"는 **원문에 문자열 자체가 부재**(Lake George 는 Part 2 가 아니며 수조가 아니라 천해 호수 현장) — 삭제
- DOI를 통한 Springer/AGU institutional access 시 full PDF read 가능 (사용자 환경)

## 6. 연결

- [[swan-action-balance]] — 본 paper 의 핵심 식 (action balance)
- [[swan-foundation]] — SWAN module 구조
- [[swan-source-terms-implementation]] / [[wave/swan-source-terms-implementation]] — source terms (Sin/Snl/Sds/Sbot)
- [[swan-propagation-implementation]] — c_θ refraction
- [[swan-wind-formulations-implementation]] — wind input
- [[swan-whitecapping]] — whitecapping
- [[swan-diffraction-obstacles]] — Holthuijsen 2003 후속
- [[swan-st6-babanin-implementation]] — Babanin physics (ST6)
- [`models/SWAN/web-refs/swan-official-resources.md`](../web-refs/swan-official-resources.md) — 공식 SWAN 자료
