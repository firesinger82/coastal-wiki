---
title: "SFINCS 공식 자료 — Deltares 사이트·readthedocs·GitHub·핵심 논문"
model: SFINCS
canonical_source: external
external_source: "SFINCS GitHub README.rst 직접 read (raw/source_code/sfincs/README.rst, 2026-06-18) 에서 공식 URL·라이선스 직접 인용. 핵심 논문은 bibliographic."
citation_status: verified
verification_method: "README.rst verbatim (공식 URL·GPL-3.0/Deltares Freeware 라이선스 조건). 핵심 논문 서지는 bibliographic(원문 미fetch — DOI 교차확인 권장)."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - models/SFINCS/README.md
  - models/SFINCS/source-analysis/sfincs-architecture-source-map.md
---

# SFINCS 공식 자료

> Deltares SFINCS 공식 리소스. URL·라이선스는 GitHub `README.rst` 직접 인용(verified).

## 1. 공식 채널 (README.rst verbatim)

| 자료 | URL |
|---|---|
| 제품 페이지 | <https://www.deltares.nl/en/software/sfincs/> |
| User manual (문서) | <https://sfincs.readthedocs.io/en/latest/> |
| 소스 (GPL-3.0) | <https://github.com/Deltares/SFINCS> |
| 실행파일 다운로드 | <https://download.deltares.nl/sfincs> |
| Docker (Mac/Linux/HPC) | `deltares/sfincs-cpu` (<https://hub.docker.com/r/deltares/sfincs-cpu>) |
| Python 모델빌더 | HydroMT-SFINCS <https://github.com/Deltares/hydromt_sfincs> |
| 사용자 Q&A | GitHub Discussions <https://github.com/Deltares/SFINCS/discussions> |
| 문의 | sfincs@deltares.nl |

## 2. 라이선스 (README.rst §Licensing)

- **소스**: GNU **GPL-3.0** — 상업이용·배포·수정·특허·사적이용 허용. 조건: 소스공개·라이선스/저작권 고지·동일 라이선스(closed-source 배포 불가)·변경 명시. 무보증.
- **사전컴파일 실행파일**(Windows/Docker): **Deltares Freeware** — 상업이용·연구출판 허용, **재배포·수정 불가**, Deltares 저작권 소유.

## 3. 핵심 논문 (bibliographic — DOI 교차확인 권장)

- **Leijnse, T., van Ormondt, M., Nederhoff, K., van Dongeren, A. (2021)** — "Modeling compound flooding in coastal systems using a computationally efficient reduced-physics solver: Including fluvial, pluvial, tidal, wind- and wave-driven processes." *Coastal Engineering* **163**, 103796. (SFINCS 정식 reference 논문 — reduced-physics compound flooding) ⚠ DOI·페이지 원문 미fetch, 인용 시 cross-check.
- 후속: subgrid·quadtree·SnapWave 관련 Deltares 논문 — readthedocs §References 에서 추적(후속 web-refs).

## 4. 정체 (README.rst §What is SFINCS, verbatim)

> "SFINCS is Deltares' new open-source, open-access **reduced-complexity model** designed for super-fast modelling of **compound flooding** events in a dynamic way!" — early warning·multi-hazard risk 에 full-physics 대비 계산효율 + good accuracy 균형.

## 5. 연결

- [[../README]] · [[../source-analysis/sfincs-architecture-source-map]]
- 자매: [[../../LISFLOOD-FP/README]] (reduced-complexity flood)
- 개념: [[../../../concepts/storm-surge/07-ml-emulators]] (고속 침수 계열 비교)
