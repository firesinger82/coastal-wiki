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
| `source-analysis/` | 37 verified | **종결 2026-07-12** ([AUDIT-LEDGER §3](../AUDIT-LEDGER.md)) | nonlinear 코어·4D-Var suite(TLM/ADM/RPM)·GST·sea-ice·BBL·biology·KPP·EOS·wetdry·tracer timestep 등 전수. cross-model 대조노트 flag 0건 |
| `manual-notes/` | 4 verified | **M-C 완료** | wiki-overview (326 pages 인덱스) + wiki-getting-started (디렉토리 구조) + wiki-cppdefs-options (32 CPP category 운영 결정 매트릭스) + roms-exercises-catalog |
| `web-refs/` | 4 verified | **신설 2026-05-24 · COAWST 보강 2026-07-19** | roms-official-resources.md (myroms.org·forum·GitHub·핵심 논문 Shchepetkin-McWilliams 2005·Haidvogel 2008·Warner 2008 CSTMS·Large 1994 KPP) + roms-coawst-applications-review.md + **roms-coawst-adriatic-applications.md** (Carniel et al. 2013 full-PDF — AdriaROMS 2 km·NA-COAWST 0.5 km 운영구성) + **roms-coawst-wci-benetazzo-2013.md** (Ocean Modelling 70:152-165 full-PDF — WCI 정량검증 Table 1·2WC/UNC ΔHs·Kirby-Chen 결합 유속평균) |
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
