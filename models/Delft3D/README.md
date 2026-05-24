# models/Delft3D

> **Canonical source**: 이 디렉토리(`models/Delft3D/`)가 Delft3D 모델군의 구현·메커닉에 대한 진실의 원천.

## 정체 카드

- **이름**: Delft3D (FLOW, WAVE, SED, WAQ, PART, WES 모듈 + Delft3D FM)
- **저자/관리주체**: Deltares (네덜란드)
- **라이선스**: 다중 — `agpl-3.0.txt` + `bsd-2.txt` + `bsd-3.txt` (LICENSE 참조). Delft3D 4 는 GPL/AGPL, Delft3D FM 별도
- **공식 사이트**: [https://oss.deltares.nl/web/delft3d](https://oss.deltares.nl/web/delft3d)
- **GitHub**: [Deltares/delft3d](https://github.com/Deltares/delft3d), Delft-FIAT, hydromt_delft3dfm
- **소스 위치 (본 위키)**:
  - `raw/source_code/Delft3D/` — 본체 (Fortran 약 4795 files, 빌드 스크립트, doc, examples)
  - `raw/source_code/Delft-FIAT/` — Flood Impact Assessment Tool
  - `raw/source_code/hydromt_delft3dfm/` — Python HydroMT D3D-FM 설정 자동화
- **공식 메뉴얼**: `raw/manuals/pdfs/` 53 PDFs — 모듈별 user manual:
  - `Delft3D-PART_User_Manual.pdf`
  - `Delft3D-WAQ_*_Manual.pdf` (open processes library 등 다수)
  - `Delft3D-WES_User_Manual.pdf` (wind enhanced scheme)
  - `rigid_3d_vegetation_model_memo.pdf`, `Delft3D-PART_dispersant_booms_memo.pdf`
  - (FLOW/WAVE/SED user manual 도 53 PDF 안에 다수)
- **사용 도메인**: 3D 수리·파랑·표사·수질·입자추적·dredge/dump
- **격자**:
  - **Delft3D 4** — structured curvilinear/orthogonal
  - **Delft3D FM (Flexible Mesh)** — unstructured triangular/quad

## 하위 디렉토리 현황

| 경로 | 노트 수 | 상태 | 비고 |
|---|---:|---|---|
| `source-analysis/` | 12 verified | **sparse (M-D 1차 진행)** | 기존 10 + 신설 2 (engines_overview·flow2d3d_dispatcher). 4795 Fortran 대비 여전히 sparse — M-D 2차 후속 (dflowfm·dimr·flow2d3d_kernel walkthrough) |
| `manual-notes/` | **0** | **미개시** | 53 PDFs 보유했으나 정리 노트 없음 (M-C 보강 후보) |
| `web-refs/` | 1 verified | **신설 2026-05-24** | delft3d-official-resources.md — Deltares OSS·GitHub Deltares/delft3d·Delft-FIAT·hydromt_delft3dfm·핵심 논문 (Lesser 2004·Stelling-Duinmeijer 2003·Kernkamp 2011·van der Wegen 2008) |
| `raw/` | 56 .md + 53 pdf + 4795 fortran (1.5 GB) | archive | Delft3D + Delft-FIAT + hydromt_delft3dfm |

## 본 위키에서의 핵심 활용

- [`concepts/sediment-transport/06-model-application.md`](../../concepts/sediment-transport/06-model-application.md) — Delft3D-SED (Van Rijn + Partheniades-Krone)
- [`concepts/waves/`](../../concepts/waves/) — Delft3D-WAVE (SWAN 통합 + flow-wave 양방향 coupling)
- [`concepts/littoral-drift/`](../../concepts/littoral-drift/) — surf zone + cross-shore profile

## 작성 우선순위 (남은 작업)

1. **M-C**: `manual-notes/` FLOW + WAVE + SED + WAQ 4 핵심 모듈 user manual 챕터별 발췌 (4 PDF * 1 노트 each)
2. **M-D**: `source-analysis/` 보강 — 현재 10 노트가 4795 Fortran 에 sparse. 우선 D3D-4 의 핵심 모듈 (TRISULA hydro, ONLINE_WAVE coupling, SEDTRANS) 추가
3. **M-E**: `web-refs/` — Deltares OpenEarth 공식 + Lesser et al. 2004 (D3D 통합 논문)
