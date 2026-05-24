# models/ROMS

> **Canonical source**: 이 디렉토리(`models/ROMS/`)가 ROMS 모델의 구현·메커닉에 대한 진실의 원천.

## 정체 카드

- **이름**: ROMS (Regional Ocean Modeling System)
- **저자/관리주체**: Hernan Arango (Rutgers), Alexander Shchepetkin (UCLA) 외. 1990년대 후반 ~ 현재
- **라이선스**: MIT-style — [License_ROMS.md](raw/source_code/roms/License_ROMS.md)
- **공식 사이트**: [https://www.myroms.org/](https://www.myroms.org/), 커뮤니티 [https://www.myroms.org/forum/](https://www.myroms.org/forum/)
- **GitHub**: [myroms/roms](https://github.com/myroms/roms), [myroms/roms-jedi](https://github.com/myroms/roms-jedi)
- **소스 위치 (본 위키)**:
  - `raw/source_code/roms/` — 본체 (Fortran 약 1373 files, CMake/makefile 빌드)
  - `raw/source_code/roms-jedi/` — JEDI 데이터 동화 통합
  - `raw/source_code/roms_eccofs/` — ECCO-style 동화
  - `raw/source_code/roms_libs/` — 공통 라이브러리
  - `raw/source_code/roms_matlab/` — MATLAB 후처리
  - `raw/source_code/roms_test/` — 테스트 케이스
  - `raw/source_code/WRF/` — WRF (대기) coupling 참고
- **공식 메뉴얼**: `raw/manuals/wiki/` (myroms.org wiki mirror — 1161 HTML/markdown) + `raw/manuals/website/` (블로그·wiki 페이지) + `raw/manuals/refs/`
- **사용 도메인**: 3D regional ocean — baroclinic (수온·염분) + biogeochemistry + sea-ice + data assimilation
- **격자**: orthogonal curvilinear horizontal + terrain-following sigma vertical
- **수치 기법**: split-explicit time stepping (barotropic + baroclinic), 3rd/4th order advection, K-profile parametrization (KPP) + Mellor-Yamada (MY2.5) 등 다수 vertical mixing

## 하위 디렉토리 현황

| 경로 | 노트 수 | 상태 | 비고 |
|---|---:|---|---|
| `source-analysis/` | 14 verified | **M-D 1차+2차 진행** | 기존 11 + M-D 1차 2 (main_driver_dispatch·nonlinear_physics_modules) + M-D 2차 1 (bulk_flux_coare 1623 lines Fairall 1996/2003·Edson 2013). 1373 Fortran 대비 여전히 sparse — main3d_loop·KPP walkthrough 후속 |
| `manual-notes/` | 3 verified | **M-C 2차 진행** | wiki-overview (326 pages 인덱스) + wiki-getting-started (디렉토리 구조) + wiki-cppdefs-options (32 CPP category 운영 결정 매트릭스). vertical-mixing·tidal-forcing 후속 |
| `web-refs/` | 1 verified | **신설 2026-05-24** | roms-official-resources.md — myroms.org·forum·GitHub myroms/roms·myroms/roms-jedi·핵심 논문 (Shchepetkin-McWilliams 2005·Haidvogel 2008·Warner 2008 CSTMS·Large 1994 KPP) |
| `raw/` | 1221 .md + 10 pdf + 1373 fortran (583 MB) | archive | roms 본체 + 6 variants + WRF coupling |

## 본 위키에서의 핵심 활용

- [`concepts/sst/06-model-application.md`](../../concepts/sst/06-model-application.md) — ROMS 해수온 module + 한국 동해 NIFS 동해예측시스템 (KOOS-EJS) 기반
- [`concepts/sediment-transport/06-model-application.md`](../../concepts/sediment-transport/06-model-application.md) — ROMS-CSTMS 통합 (Community Sediment Transport Modeling System)
- [`concepts/currents/`](../../concepts/currents/) — baroclinic regional current modeling
- `source-analysis/roms_atmospheric_forcing.md` — 대기 forcing 일반론 (a9618df promote)

## 작성 우선순위 (남은 작업)

1. **M-C**: `manual-notes/` 핵심 wiki 페이지 정리 — Getting Started, CPP options, Input/Output, Vertical Mixing, Boundary Conditions (5 노트)
2. **M-D**: `source-analysis/` 보강 — split-explicit 2D/3D 결합, KPP/MY2.5 dispatcher, 한국 KOOS-EJS 운영 모드
3. **M-E**: `web-refs/` — myroms.org 핵심 + Shchepetkin & McWilliams (2005) Ocean Modelling + CSTMS Warner et al. (2008)
