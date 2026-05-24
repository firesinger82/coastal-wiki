# models/XBeach

> **Canonical source**: 이 디렉토리(`models/XBeach/`)가 XBeach 모델의 구현·메커닉에 대한 진실의 원천.

## 정체 카드

- **이름**: XBeach
- **저자/관리주체**: Deltares (네덜란드), 원 개발자 Dano Roelvink 외. 2008~ (Katrina 후 미국 해안 대응으로 개발 시작)
- **라이선스**: GPL-3.0
- **공식 사이트**: [https://oss.deltares.nl/web/xbeach](https://oss.deltares.nl/web/xbeach)
- **GitHub/SVN**: SVN [https://svn.oss.deltares.nl/repos/xbeach/](https://svn.oss.deltares.nl/repos/xbeach/), Mirror [openearth/xbeach](https://github.com/openearth/xbeach)
- **소스 위치 (본 위키)**: `raw/source_code/trunk/` (Fortran ~90 files)
- **공식 메뉴얼**: `raw/manuals/pdfs/`:
  - `XBeach_manual_master.pdf` (master branch user manual)
  - `XBeach_manual_kingsday.pdf` (kingsday release)
  - `reports/Parallellization_report.pdf`
  - `reports/non-hydrostatic_report_draft.pdf`
- **사용 도메인**: 단기 폭풍 시 연안침식·범람·표사 (storm-driven nearshore morphology) — surf zone + swash zone + dune erosion
- **격자**: 직교/곡선 격자 (structured)
- **수치 기법**: 3 운영 모드
  - **surfbeat (default)**: wave envelope + groupiness + infragravity wave 해상
  - **non-hydrostatic**: depth-averaged Boussinesq 식
  - **single-layer (stationary)**: 단기 wave climate 평균

## 하위 디렉토리 현황

| 경로 | 노트 수 | 상태 | 비고 |
|---|---:|---|---|
| `source-analysis/` | 16 verified | 안정 | morphology · avalanching · bed_friction · wave_boundary · single_dir · q3d · mode_dispatch · groundwater · output · output · vegetation · SWAN handoff |
| `manual-notes/` | 3 source-needed | **P2 catalog** | phase 2a bulk promote, 페이지 인용 audit 보류 (M-B) |
| `web-refs/` | 1 verified | **신설 2026-05-24** | xbeach-official-resources.md — Deltares OSS·OpenEarth·xbeach.readthedocs.io·핵심 논문 (Roelvink 2009·McCall 2010·Smit 2010·van Dongeren 2013) |
| `raw/` | 17 .md + 9 pdf + 90 fortran (162 MB) | archive | trunk source + manuals + reports |

## 본 위키에서의 핵심 활용

- [`concepts/littoral-drift/01-concept.md`](../../concepts/littoral-drift/01-concept.md) §9 — XBeach surf module
- [`concepts/littoral-drift/02-theory.md`](../../concepts/littoral-drift/02-theory.md) — Holthuijsen §7.4.2-3 radiation stress (XBeach 의 surf zone 처리 근간)
- [`concepts/sediment-transport/06-model-application.md`](../../concepts/sediment-transport/06-model-application.md) — XBeach Soulsby-van Rijn + avalanching
- [`concepts/storm-surge/`](../../concepts/storm-surge/) — storm 시 inundation + littoral 결합

## 작성 우선순위 (남은 작업)

1. **M-B**: `manual-notes/` 3 source-needed → verified (페이지 인용 audit)
2. **M-E**: `web-refs/` — Deltares OpenEarth 공식 + Roelvink 2009 + Katrina/Sandy case
3. 추가 source-analysis: 3 운영 모드 dispatcher 상세 + cross-shore vs longshore balance
