---
title: "SWAN 공식 자료 — sourceforge·핵심 논문·커뮤니티 큐레이션"
topic: swan-web-refs
canonical_source: self
citation_status: verified
verification_method: "공식 도메인 swanmodel.sourceforge.io + Holthuijsen 2007 (source_id: holthuijsen2007) Ch 9 SWAN 발췌 ([textbook/notes/waves-holthuijsen-toc.md](../../../textbook/notes/waves-holthuijsen-toc.md)). 핵심 논문 인용은 publicly-known canonical works."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-24
verification_by: "Claude Opus 4.7 (1M context) — URL + 공인 논문 인용"
verification_date: 2026-05-24
related:
  - models/SWAN/README.md
  - textbook/notes/waves-holthuijsen-toc.md
---

# SWAN 공식 자료 큐레이션

> [`models/SWAN/README.md`](../README.md) 의 정체 카드 외부 references 확장.

## 1. 공식 사이트

| 자원 | URL | 활용 |
|---|---|---|
| **swanmodel.sourceforge.io** | [https://swanmodel.sourceforge.io/](https://swanmodel.sourceforge.io/) | 공식 홈 — TU Delft |
| SourceForge SVN | svn://swanmodel.sourceforge.net/swan | 소스 + 빌드 |
| Documentation | sourceforge 사이트 내 — Scientific/Technical, Implementation, User Manual 별도 다운로드 |
| Holthuijsen Ch 9 | 본 위키 [`textbook/notes/waves-holthuijsen-toc.md`](../../../textbook/notes/waves-holthuijsen-toc.md) — Holthuijsen 2007 (source_id: holthuijsen2007) Ch 9 SWAN 직접 발췌 |

## 2. Code repository

| Repo | 역할 |
|---|---|
| SourceForge SVN | 공식 — Fortran source |

## 3. 핵심 논문 — 시초부터 현재까지

### 3.1 Foundation (1999) — 3 generation wave model

- **Booij, N., Ris, R.C., Holthuijsen, L.H. (1999)** "A third-generation wave model for coastal regions: 1. Model description and validation" *J. Geophys. Res. Oceans* 104(C4):7649-7666 — **SWAN 시초 paper**
- **Ris, R.C., Holthuijsen, L.H., Booij, N. (1999)** "A third-generation wave model for coastal regions: 2. Verification" *J. Geophys. Res. Oceans* 104(C4):7667-7681

### 3.2 Modern operational

- **Zijlema, M. (2010)** "Computation of wind-wave spectra in coastal waters with SWAN on unstructured grids" *Coastal Engineering* 57(3):267-277 — unstructured grid
- **Rogers, W.E., Hwang, P.A., Wang, D.W. (2003)** "Investigation of wave growth and decay in the SWAN model: Three regional-scale applications" *J. Phys. Oceanogr.* 33:366-389
- **van der Westhuysen, A.J., Zijlema, M., Battjes, J.A. (2007)** "Nonlinear saturation-based whitecapping dissipation in SWAN for deep and shallow water" *Coastal Engineering* 54(2):151-170

### 3.3 Coupled (SWAN + ADCIRC, SWAN + Delft3D)

- **Dietrich, J.C. et al. (2011)** "Modeling hurricane waves and storm surge using integrally-coupled, scalable computations" *Coastal Engineering* 58:45-65 — ADCIRC+SWAN
- **Lesser, G.R., Roelvink, J.A., van Kester, J.A.T.M., Stelling, G.S. (2004)** "Development and validation of a three-dimensional morphological model" *Coastal Engineering* 51:883-915 — Delft3D 통합

## 4. 표준 교과서 — 본 위키 verified source

- **Holthuijsen, L.H. (2007)** *Waves in Oceanic and Coastal Waters* Cambridge University Press (source_id: holthuijsen2007)
  - **Ch 9** SWAN-specific — Action balance equation + Source terms + DIA + Triad + Frequency shifting
  - 본 위키 발췌: [`textbook/notes/waves-holthuijsen-toc.md`](../../../textbook/notes/waves-holthuijsen-toc.md)
  - 본 위키 source-analysis: [`models/SWAN/source-analysis/`](../source-analysis/) (21 노트, action balance 등)

## 5. 한국 적용

- 한국 해역 SWAN 적용 사례(WINK 도메인·축산항 검증·JMA-MSM 바람 등)는 외부 개인 환경 자료로 canonical 미수록. 바이블 검증 통과 시 `experience/` 로 카테고리화 (source-needed).
- 일반 적용 가이드 → [`concepts/waves/06-model-application.md`](../../../concepts/waves/06-model-application.md)

## 6. 운영 자원

| 자원 | 비고 |
|---|---|
| SWAN User Discussion | sourceforge 의 사용자 메일링 리스트 |
| Implementation Manual | 빌드·MPI·OpenMP 설정 |
| Scientific/Technical Doc | 이론서 (Holthuijsen Ch 9 동일 내용) |

## 7. 본 위키 내 cross-ref

- [`concepts/waves/06-model-application.md`](../../../concepts/waves/06-model-application.md) — 본 디렉토리 canonical 인용
- [`concepts/littoral-drift/02-theory.md`](../../../concepts/littoral-drift/02-theory.md) — Holthuijsen §7.4 radiation stress (SWAN 의 source term)
- [`models/SWAN/source-analysis/`](../source-analysis/) — 21 verified 노트 (action balance, WINK, JMA-MSM, source terms)
- [`models/SWAN/manual-notes/swan-action-balance.md`](../manual-notes/swan-action-balance.md) (예정) — Holthuijsen Ch 9 §9.3
