---
title: "Delft3D 공식 자료 — Deltares·GitHub·핵심 논문 (Lesser 2004 등) 큐레이션"
topic: delft3d-web-refs
canonical_source: self
citation_status: verified
verification_method: "Deltares 공식 도메인 (oss.deltares.nl) + GitHub 공개 repo (Deltares/delft3d). 핵심 논문 인용은 publicly-known canonical works (Lesser et al. 2004, Stelling & Duinmeijer 2003). §8 추가 (2026-05-26): GitHub API `gh release view DIMRset_2026.02 -R Deltares/Delft3D` + `gh api repos/Deltares/Delft3D/compare/DIMRset_2026.01...DIMRset_2026.02` (1067 commits / 300 files / 6개월) + `gh pr view 900 -R Deltares/Delft3D` 직접 fetch (2026-05-26). PR body verbatim + 변경 파일 4개 직접 확인 + release commit log 주요 UNST-\*/DELWAQ-\* 카테고리 추출. release notes body 자체는 비어있어 GitHub commit log 가 first-party authoritative source."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-26
verification_by: "Claude Opus 4.7 (1M context) — URL + 공인 논문 인용 + §8 GitHub API 직접 fetch"
verification_date: 2026-05-26
related:
  - models/Delft3D/README.md
---

# Delft3D 공식 자료 큐레이션

> [`models/Delft3D/README.md`](../README.md) 의 정체 카드 외부 references 확장.

## 1. 공식 사이트

| 자원 | URL | 활용 |
|---|---|---|
| **Deltares Delft3D** | [https://oss.deltares.nl/web/delft3d](https://oss.deltares.nl/web/delft3d) | 공식 홈 — Delft3D 4 + Delft3D FM |
| **Delft3D-FM** | [oss.deltares.nl/web/delft3dfm](https://oss.deltares.nl/web/delft3dfm) | Flexible Mesh variant |
| **Manuals download** | Deltares 공식 사이트 내 (PDF download) | FLOW + WAVE + SED + WAQ 각 user manuals |

## 2. Code repository

| Repo | 역할 |
|---|---|
| **Deltares/delft3d** | [github.com/Deltares/delft3d](https://github.com/Deltares/delft3d) | Delft3D 4 (structured) + 일부 도구 |
| **Deltares/Delft-FIAT** | [github.com/Deltares/Delft-FIAT](https://github.com/Deltares/Delft-FIAT) | Flood Impact Assessment Tool |
| **Deltares/hydromt_delft3dfm** | [github.com/Deltares/hydromt_delft3dfm](https://github.com/Deltares/hydromt_delft3dfm) | Python HydroMT D3D-FM 설정 자동화 |

### 2.1 D-HYDRO 생태계 모델 빌더 (source-needed)

D-Flow FM(=Delft3D FM)은 차세대 **D-HYDRO Suite** 의 엔진. 데이터모델→모델 자동생성 도구 계열:

- **D-HyDAMO** — [HKV Confluence DHYD space](https://hkvconfluence.atlassian.net/wiki/spaces/DHYD/overview) (사용자 제공). **HyDAMO**(네덜란드 수계 표준 교환 데이터모델)로부터 **D-HYDRO(D-Flow FM) 1D2D 모델 자동 생성** Python 도구. 문서(HKV 발행, 네덜란드어, ~2026 갱신): Installatie·Genereren van deelmodellen(부분모델 생성)·Meteo-data·Dwarsprofiel(횡단면)·Koppelmethodes(geometrie↔waterlooptak 결합). `hydromt_delft3dfm`(HydroMT 기반)과 동류 — 입력 데이터모델만 다름(HyDAMO vs HydroMT).
- 적용 맥락: 주로 **내륙 수계(1D 하천망·수로 + 2D 범람)** — 네덜란드 water board 운영. 연안 surge/morphology 보다 riverine/pluvial flood 지향(coastal 직접성 낮음, D-Flow FM 엔진 공유로 본 위키 ecosystem 참조).
- citation_status: source-needed (Confluence REST API overview 수준 — 스페이스명·페이지·발행주체 verified, 기능 상세는 네덜란드어 문서 deep read TODO).

## 3. 핵심 논문 — 시초부터 현재까지

### 3.1 Foundation — FLOW + Morphology

- **Lesser, G.R., Roelvink, J.A., van Kester, J.A.T.M., Stelling, G.S. (2004)** "Development and validation of a three-dimensional morphological model" *Coastal Engineering* 51(8-9):883-915 — **Delft3D-FLOW + SED 통합 시초 paper**

### 3.2 수치 기법

- **Stelling, G.S., Duinmeijer, S.P.A. (2003)** "A staggered conservative scheme for every Froude number in rapidly varied shallow water flows" *Int. J. Numer. Meth. Fluids* 43:1329-1354 — D3D-FM staggered scheme
- **Kernkamp, H.W.J., Van Dam, A., Stelling, G.S., De Goede, E.D. (2011)** "Efficient scheme for the shallow water equations on unstructured grids with application to the Continental Shelf" *Ocean Dynamics* 61:1175-1188 — D3D-FM

### 3.3 모듈별 — WAVE / WAQ / PART

- **Delft3D-WAVE** = SWAN integration (Booij·Ris·Holthuijsen 1999 인용, [[../../SWAN/web-refs/swan-official-resources]])
- **Delft3D-WAQ** — Smits, J.G.C., Van Beek, J.K.L. (2013) "ECO: a generic eutrophication model" 등 다수
- **Delft3D-PART** — particle tracking module

### 3.4 Modern operational

- **van der Wegen, M., Roelvink, J.A. (2008)** "Long-term morphodynamic evolution of a tidal embayment using a two-dimensional, process-based model" *J. Geophys. Res. Earth Surface* 113:F03001 — 장기 morphology
- **Deltares (continual)** — Delft3D FM unstructured mesh modernization

## 4. 모듈별 활용

| 모듈 | 활용 | 본 위키 cross-ref |
|---|---|---|
| **Delft3D-FLOW** | 3D hydro (수온·염분·tide·current) | [[../source-analysis/]] 일부 |
| **Delft3D-WAVE** | SWAN 통합 (flow-wave 양방향 coupling) | [[../source-analysis/]] flow-wave coupling 노트 |
| **Delft3D-SED** | 표사 (Van Rijn + Partheniades-Krone) | [`concepts/sediment-transport/06-model-application.md`](../../../concepts/sediment-transport/06-model-application.md) |
| **Delft3D-WAQ** | 수질·eutrophication | (별도 작업) |
| **Delft3D-PART** | 입자 추적 (oil spill, dispersant) | `raw/manuals/pdfs/Delft3D-PART_*.pdf` |
| **Delft3D-WES** | Wind Enhanced Scheme | `raw/manuals/pdfs/Delft3D-WES_User_Manual.pdf` |

## 5. 한국 적용

- (별도 큐레이션 필요) 한국 항만·하구 D3D 적용 사례
- Delft3D 의 동중국해 + 황해 적용 — 다수 한국 학술 paper

## 6. 운영 자원

| 자원 | 비고 |
|---|---|
| **Deltares Public Wiki** | Delft3D 사용 안내, FAQ |
| **GitHub Issues** | [github.com/Deltares/delft3d/issues](https://github.com/Deltares/delft3d/issues) |
| **GitHub Discussions** | 사용자 Q&A |
| **Deltares Academy** | 정기 트레이닝 (FLOW·SED·WAVE 별) |
| Delft3D-PART memos | Dispersant·booms 운영 |

## 7. 본 위키 내 cross-ref

- [`concepts/sediment-transport/06-model-application.md`](../../../concepts/sediment-transport/06-model-application.md) — Delft3D-SED Van Rijn + Partheniades-Krone
- [`concepts/waves/`](../../../concepts/waves/) — Delft3D-WAVE (SWAN 통합)
- [`concepts/littoral-drift/`](../../../concepts/littoral-drift/) — surf zone + cross-shore profile
- [`models/Delft3D/source-analysis/`](../source-analysis/) — 10 verified 노트 (sparse, M-D 보강 후보)
- [`models/SWAN/`](../../SWAN/) — Delft3D-WAVE 의 backend (관련 모델)

## 8. Recent releases & updates

GitHub API 직접 fetch (`gh release view` + `gh api compare` + `gh pr view`, 2026-05-26).

### 8.1 Delft3D 2026.02 release — DIMRset_2026.02 (2026-04-28)

- 출처: [github.com/Deltares/Delft3D/releases/tag/DIMRset_2026.02](https://github.com/Deltares/Delft3D/releases/tag/DIMRset_2026.02)
- author: matthijs-deltares · created 2026-04-15 · **published 2026-04-28T12:54:47Z**
- **release notes body empty** — Deltares 가 GitHub release page 에 본문 미작성. 변경 사항의 first-party authoritative source 는 GitHub commit log.

#### 8.1.1 변경 규모 (gh api compare DIMRset_2026.01...DIMRset_2026.02)

| 항목 | 값 |
|---|---|
| 이전 release | DIMRset_2026.01 (2025-10-24) |
| Total commits | **1067** |
| Files changed | **300** |
| 기간 | ~6개월 |

#### 8.1.2 주요 변경 카테고리 (commit message verbatim 추출)

**DFLOWFM (UNST-\* 시리즈)** — unstructured engine 다수 변경:

- **UNST-9480**: "1d initial waterdepth causes 2d waterdepth" — 1D-2D coupling bug fix
- **UNST-8857**: "update circumcenterMethod default to ALL_NETLINKS_LOOP and use dbdistance" — grid metric default 변경
- **UNST-9617**: "Changed readout of [Bubblescreen] object in extfile"
- **UNST-9576**: coupling docs 업데이트
- **UNST-9525**: OneAPI 2025 Linux 빌드
- **UNST-9656**: "Switched to the C++ 20 standard"

**MDU keyword 변경**:

- "Move MDU-keyword 'circumcenter' from DEPRECATED to OBSOLETE" — 기존 `.mdu` 파일에서 `circumcenter` 사용 중이면 강제 변경 필요

**WAQ (water quality)**:

- **DELWAQ-1232**: "improve settling deposition"
- **DELWAQ-1146**: "yyy-mm-dd fix for apptainer smoketest configs"

**DELFT3D 4 (structured)**:

- **DELFT3D-37920**: "CSUMO add source weight"

**외부 의존성**:

- "Update PETSc calls to use new 3.24 interface" — PETSc 3.24 호환
- C++20 standard 전환
- OneAPI 2025 Linux 빌드

**DEVOPS**: DEVOPSDSC-\* 시리즈 — CI 인프라 다수.

#### 8.1.3 사용자 영향

- **재컴파일 필수** (PETSc 3.24 / C++20 / OneAPI 2025 의존성 변경)
- **MDU 파일 점검**: `circumcenter` keyword OBSOLETE — 사용 중이면 제거. 새 default `ALL_NETLINKS_LOOP` 영향 가능
- **1D-2D coupling 모델**: UNST-9480 bug 영향 받았다면 기존 결과와 차이 점검 필요
- **D3D 4 사용자**: CSUMO source weight 새 옵션 인지

#### 8.1.4 검증 한계

- 1067 commits 전체의 사용자 영향 평가는 표본 — 위 list 는 commit message 의 main category 추출, 세부는 각 UNST/DELWAQ issue tracker 추가 확인 후 보강 가능
- Deltares 공식 release notes 문서 (oss.deltares.nl) 가 별도 공개되면 본 § 추가 보강

### 8.2 PR #900 — UNST-9952 fix time reading from mdu (OPEN, 2026-05-22)

- 출처: [github.com/Deltares/Delft3D/pull/900](https://github.com/Deltares/Delft3D/pull/900)
- status: **OPEN** (mergedAt: null) — main branch 미반영, **2026.02 release 미포함** (다음 release 예정)
- Issue link: **UNST-9952**
- branch: `fm/bugfix/UNST-9952_fix_time_reading_from_mdu` → `main`
- changes: 185 additions / 120 deletions / 4 files
- 회귀 테스트 추가: `e02_f042_c01` 및 `c02`

#### 8.2.1 변경 설명 (PR body verbatim)

> "Moved the [time] read block in readMDU up in the routine, behind the geometry block. Some output fields use tstart_user and tstop_user, which was modified by the [time] read after fields were already set based on the m_flowtimes defaults."

→ `readMDU` 함수 read order bug: `[time]` 블록을 geometry 블록 뒤로 이동. 이전에는 output fields 가 `m_flowtimes` defaults 로 먼저 셋업된 후 `[time]` 블록의 `tstart_user` · `tstop_user` 로 재설정 → output time inconsistency.

#### 8.2.2 실제 변경 파일

| 파일 | additions | deletions | 역할 |
|---|---:|---:|---|
| `src/engines_gpl/dflowfm/packages/dflowfm_kernel/src/dflowfm_data/unstruc_model.f90` | +113 | -112 | **핵심 fix — readMDU 함수 reorganization** |
| `src/engines_gpl/dflowfm/packages/dflowfm_kernel/src/dflowfm_io/sedtrails_netcdf.f90` | +10 | -6 | sedtrails NetCDF I/O 부수 영향 |
| `test/deltares_testbench/configs/include/dimr_dflowfm_all_but_validation_cases.xml` | +14 | 0 | 회귀 테스트 추가 |
| `test/deltares_testbench/configs/include/dimr_dflowfm_parallel.xml` | +48 | -2 | parallel 테스트 케이스 보강 |

#### 8.2.3 사용자 영향

- DFLOWFM 사용자: 기존 `.mdu` 파일의 `tstart_user` · `tstop_user` 가 `m_flowtimes` defaults 와 다르면 output time 차이 가능 (PR merge 후 정정)
- **sedtrails 모듈**: NetCDF I/O 부수 영향 — sedtrails 사용 시 별도 검증 권장
- merge 후 다음 release 에 포함 예정

#### 8.2.4 검증 한계

- PR open 상태 — 최종 merge 형식 변경 가능 (squash · 추가 commit 등)
- ✅ `unstruc_model.f90` +113 -112 diff 직접 read 완료 (2026-05-28) → [`source-analysis/delft3d_dflowfm_mdu_input.md`](../source-analysis/delft3d_dflowfm_mdu_input.md). `[Time]` block 18 파라미터 verbatim + reorder 위치 (line 1045 ↔ line 1768) + m_flowtimes lifecycle 도해 정리
