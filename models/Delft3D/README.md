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
| `source-analysis/` | 48 verified (top 46 + `sediment/` 1 + `wave/` 1) | **핵심 커널 커버 두터움** | FLOW(adi solver·difu/z_difu transport·difhor anti-creep·forfil·morphology erosed/eqtran 19종) + FM(kernel scheme·compute aux·waves) + WAQ(process library + phcarb·densed·dissi·sulfid·sedox 등) + dredge·dimr·engines. 실측 2026-07-10 (stale 14→48 정정) |
| `manual-notes/` | 11 verified | **문서잔여 종결 2026-07-04** | overview(53 PDFs 인덱스)·FLOW(user manual·physics-numerics·boundary-forcing)·WAVE·WAQ(user manual·processes tech ref·Library Tables/Input Desc/FuncSpec index)·TIDE·PART·tool manuals. 실측 2026-07-10 (stale 2→11 정정) |
| `web-refs/` | 1 verified | **신설 2026-05-24** | delft3d-official-resources.md — Deltares OSS·GitHub Deltares/delft3d·Delft-FIAT·hydromt_delft3dfm·핵심 논문 (Lesser 2004·Stelling-Duinmeijer 2003·Kernkamp 2011·van der Wegen 2008) |
| `raw/` | 56 .md + 53 pdf + 4795 fortran (1.5 GB) | archive | Delft3D + Delft-FIAT + hydromt_delft3dfm |

## 본 위키에서의 핵심 활용

- [`concepts/sediment-transport/06-model-application.md`](../../concepts/sediment-transport/06-model-application.md) — Delft3D-SED (Van Rijn + Partheniades-Krone)
- [`concepts/waves/`](../../concepts/waves/) — Delft3D-WAVE (SWAN 통합 + flow-wave 양방향 coupling)
- [`concepts/littoral-drift/`](../../concepts/littoral-drift/) — surf zone + cross-shore profile

## 작성 우선순위 (남은 작업, 2026-07-10 갱신)

1. ~~M-C: manual-notes FLOW/WAVE/SED/WAQ 발췌~~ — **완료** (11 verified, AUDIT-LEDGER §2.1 문서잔여 종결 2026-07-04)
2. ~~M-D: source-analysis 보강~~ — **핵심 커널 소진에 근접** (48 verified: ADI·transport·anti-creep·morphology·WAQ processes). 잔여는 WAQ 추가 process·개별 transport 공식(tram*/trab*)·bedcomposition 등 롱테일
3. **M-E**: `web-refs/` — Deltares OpenEarth 공식 + Lesser et al. 2004 (D3D 통합 논문)
