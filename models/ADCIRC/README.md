# models/ADCIRC

> **Canonical source**: 이 디렉토리(`models/ADCIRC/`)가 ADCIRC 모델의 구현·메커닉에 대한 진실의 원천.

## 정체 카드

- **이름**: ADCIRC (ADvanced CIRCulation Model)
- **저자/관리주체**: R. Luettich (UNC), J. Westerink (Notre Dame) 외. 1990년대 ~ 현재
- **라이선스**: 학술/연구 무료 사용, 상업 라이선스 별도 (adcirc.org/license)
- **공식 사이트**: [https://adcirc.org/](https://adcirc.org/) (raw/manuals/website 에 1086 HTML mirror)
- **GitHub**: [adcirc/adcirc](https://github.com/adcirc/adcirc), [adcirc/adcircpy](https://github.com/adcirc/adcircpy), [adcirc/adcirc-testsuite](https://github.com/adcirc/adcirc-testsuite)
- **소스 위치 (본 위키)**: `raw/source_code/adcirc/` (Fortran core) + `adcirc-testsuite` + `adcircpy` (Python) + `gahm` (vortex parametrization) + `asgs` (forecast system) + `StormEvents` + `FigureGen`
- **공식 메뉴얼**: `raw/manuals/pdfs/` 98 PDFs (workshops, papers, theory) + Luettich & Westerink (2004) "Formulation and Numerical Implementation of the 2D/3D ADCIRC" + 공식 wiki mirror
- **공식 교과서**: Pugh "Tides, Surges and Mean Sea-Level" (`source_id: sea-level`, [`textbook/md/sea-level.md`](../../textbook/md/sea-level.md)) — storm surge 이론 기반
- **사용 도메인**: 2D/3D barotropic ocean circulation — 조석·폭풍해일·연안 흐름
- **격자**: unstructured triangular finite element mesh (`fort.14`)
- **수치 기법**: Generalized Wave Continuity Equation (GWCE), explicit time stepping, parallel (MPI)

## 하위 디렉토리 현황

| 경로 | 노트 수 | 상태 | 비고 |
|---|---:|---|---|
| `source-analysis/` | 41 + 11 local-workflow source-needed | 활발 | NWS modes·GAHM·mesh tools·source-code 분석. `storm-surge/` subdir 7 노트 + `tide/` subdir + **신설 `local-workflow/` 11 노트** (2026-05-24 manual-notes/ 에서 이관) |
| `manual-notes/` | 21 verified | **M-B audit done 2026-05-24** + local 11 이관 완료 | 21 외부 docs catalog (adcirc.github.io/adcirc.org/github.com URL 검증, WebFetch 03+06 sampling) verified. 11 local-workflow 는 `source-analysis/local-workflow/` 로 이관 (디렉토리 의미 정합성) |
| `web-refs/` | 1 verified | **신설 2026-05-24** | adcirc-official-resources.md — 공식 사이트·GitHub repos (adcirc/adcirc·adcircpy·gahm·asgs·OceanMesh2D)·핵심 논문 (Luettich 1991-92·Westerink 1992·Dietrich 2010-11·Holland 1980) |
| `raw/` | 1090 .md + 98 pdf + 140 fortran (16.9 GB) | archive | source_code + manuals + website mirror |

## 본 위키에서의 핵심 활용

- [`concepts/storm-surge/02-theory.md`](../../concepts/storm-surge/02-theory.md) — Pugh §6-7 + ADCIRC GWCE 정형
- [`concepts/storm-surge/04-code-and-tools.md`](../../concepts/storm-surge/04-code-and-tools.md) — NWS modes (0/6/12/13/14/19/20/29/30) 운영 워크플로
- [`concepts/storm-surge/03-analysis-methods.md`](../../concepts/storm-surge/03-analysis-methods.md) — surge separation·return period (Pugh §6:1·§7:8·§8:3:2-3)
- [`concepts/tides/06-model-application.md`](../../concepts/tides/06-model-application.md) — 조석 forcing
- [[khoa-tide-surge-coupling]] (예정) — KHOA 실측 tide-surge separation 검증

## 작성 우선순위 (남은 작업)

1. ✅ **M-B**: `manual-notes/` 32 audit 완료 2026-05-24 — 21 verified (external URL catalog) + 11 reclassified as local-workflow-notes
2. ✅ **M-E**: `web-refs/` 신설 2026-05-24 — adcirc-official-resources.md
3. ✅ Local-workflow 11 노트 (19-26, 30-32) 이관 완료 2026-05-24 → `source-analysis/local-workflow/` ([README](source-analysis/local-workflow/README.md))
4. Hinnamnor 2022 / Maemi 2003 case 추가 (storm-surge/05 + KHOA cross-ref)
5. Local-workflow 11 노트 일부 (wide6 mesh evidence 등) experience/ 정식 승격 후보 — raw 파일 일부 본 위키 이관 후
