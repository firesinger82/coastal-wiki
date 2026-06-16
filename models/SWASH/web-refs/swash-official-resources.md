---
title: "SWASH 공식 자료 — TU Delft GitLab·sourceforge·핵심 논문 (Zijlema-Stelling-Smit 2011) 큐레이션"
model: SWASH
topic: swash-web-refs
canonical_source: self
citation_status: verified
verification_method: "SWASH 공식 repo README(raw/source_code/swash/README.md) badge 직접 인용 — release v12.01 · DOI 10.1016/j.coastaleng.2011.05.015 · sourceforge.io · gitlab.tudelft.nl · delftwaves.github.io/swash-docs · docker delftwaves/swash · GPL v3(LICENSE 파일). 핵심 논문은 publicly-known canonical (Zijlema-Stelling-Smit 2011 Coastal Eng 58:992-1012 = repo DOI / Stelling-Zijlema 2003 IJNMF 43:1-23 / Smit-Zijlema-Stelling 2013 Coastal Eng 76:1-16)."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-15
related:
  - models/SWASH/README.md
  - models/SWAN/web-refs/swan-official-resources.md
---

# SWASH 공식 자료 큐레이션

> [`models/SWASH/README.md`](../README.md) 정체 카드의 외부 references 확장. SWASH = SWAN 과 같은 TU Delft 그룹 — 인프라·생태계 일부 공유([`models/SWAN/`](../../SWAN/)).

## 1. 공식 사이트 (repo README badge 직접)

| 자원 | URL | 비고 |
|---|---|---|
| **공식 홈** | [swash.sourceforge.io](https://swash.sourceforge.io) | 과학·기술 문서, release notes, online_doc |
| **GitLab repo** | [gitlab.tudelft.nl/citg/wavemodels/swash](https://gitlab.tudelft.nl/citg/wavemodels/swash) | 공식 소스(main), 사용자 제공 URL |
| **docs (GitHub Pages)** | [delftwaves.github.io/swash-docs](https://delftwaves.github.io/swash-docs/) | |
| **Docker image** | `delftwaves/swash` (hub.docker.com) | |
| **online manuals** | swash.sourceforge.io/online_doc/ | swashuse(User)·swashtech(Tech)·swashimp(Implementation) |

- **버전**: **12.01** (badge), **라이선스 GPL v3** (`raw/source_code/swash/LICENSE`)
- 본 위키 소스: `raw/source_code/swash/` (GitLab clone, gitignore 로컬)

## 2. 핵심 논문

### 2.1 원논문 (repo README DOI badge)

- **Zijlema, M., Stelling, G.S., Smit, P. (2011)** "SWASH: An operational public domain code for simulating wave fields and rapidly varied flows in coastal waters" *Coastal Engineering* **58**(10):992-1012. **doi:[10.1016/j.coastaleng.2011.05.015](https://doi.org/10.1016/j.coastaleng.2011.05.015)** — SWASH 정체·기능 정의 paper (repo가 직접 인용하는 canonical reference).

### 2.2 수치 시초 (publicly-known)

- **Stelling, G.S., Zijlema, M. (2003)** "An accurate and efficient finite-difference algorithm for non-hydrostatic free-surface flow with application to wave propagation" *Int. J. Numer. Methods Fluids* **43**:1-23 — **비정수압 free-surface FD 알고리즘 시초** (SWASH 수치 코어의 기반). cf. Delft3D-FM staggered scheme = Stelling-Duinmeijer 2003(다른 논문, [`Delft3D web-refs §3.2`](../../Delft3D/web-refs/delft3d-official-resources.md)).

### 2.3 쇄파 (publicly-known)

- **Smit, P., Zijlema, M., Stelling, G. (2013)** "Depth-induced wave breaking in a non-hydrostatic, near-shore wave model" *Coastal Engineering* **76**:1-16 — surf zone 쇄파(hydrostatic front approximation).

## 3. SWAN 과의 관계

- 같은 TU Delft (Zijlema) — SWASH 소스가 **SWAN OCP(Ocean Pack) 인프라 공유**: `SwanGrid*.ftn90`(unstructured grid topology), `SwanReadADCGrid`(ADCIRC fort.14 reader), `ocpcre/ocpmix`(I/O), `SWINITMPI`/`swanparll`(MPI). 상세 [`source-analysis/swash-architecture-source-map.md §3`](../source-analysis/swash-architecture-source-map.md).
- **운영 조합**: SWAN(위상평균 광역 spectral) → SWASH(위상해상 항내·swash) nesting. [`concepts/waves/04 §5.1`](../../../concepts/waves/04-code-and-tools.md) 위상평균/위상해상 종합리뷰(Ferdaus 2025)가 SWASH 를 위상해상 대표 4종 중 하나로 평가.

## 4. 본 위키 접점

- [`concepts/swash-zone/04-code-and-tools.md §3`](../../../concepts/swash-zone/04-code-and-tools.md) — swash 모델 점검에서 SWASH 신설 후보로 식별 → 본 디렉토리.
- [`concepts/waves/04-code-and-tools.md §5.1`](../../../concepts/waves/04-code-and-tools.md) — 위상해상 모델군.
- [[../../FUNWAVE/README]] · [[../../Celeris/README]] — 위상해상 Boussinesq 동료(SWASH=비정수압 천수 접근).
