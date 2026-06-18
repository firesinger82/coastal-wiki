---
title: "파랑 — 04 코드와 도구 (SWAN·WAVEWATCH III·XBeach)"
topic: waves
canonical_source: self
citation_status: verified
verification_method: "AI cross-reference: textbook/md/Waves-Holthuijsen2007.md Ch.9 (SWAN canonical) + WebSearch acc. 2026-05-21 (WW3 NOAA, XBeach Deltares) + swan-library-firesinger 사용자 자료. §3.4 추가 (2026-05-28): NOAA-EMC/WW3 Issue #1600 (UK Met Office ukmo-rwdavies, OPEN 2026-05-20) GitHub Issues API 직접 fetch — bug body verbatim 인용 (SMC nested grid boundary point mismatch → coastline spurious wave energy), 재현 절차 + 한국 SWAN nested 흐름 영향 자체 분석. Fix PR 제출 예정 (status tracking)."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-21
verification_by: "Claude Opus 4.7 (1M context) — cross-ref + WebSearch + WW3 Issue #1600 GitHub API 직접 fetch (2026-05-28)"
verification_date: 2026-05-21
---

# 파랑 — 04 코드와 도구

본 페이지: 분석·예측·예보 도구. 모델별 입력 카드·메뉴얼은 `models/<model>/`이 canonical (SWAN·XBeach·Delft3D·FUNWAVE·SWASH·Celeris 모두 source-analysis 전수 검수 완료, 2026-06).

## 1. 도구·모델 비교

| 도구 | 종류 | 라이선스 | 격자 | 도메인 |
|---|---|---|---|---|
| **SWAN** | 3rd-gen phase-averaged spectral | GPL-3.0 | 직교/곡선/비구조 | 천해·연안 |
| **WAVEWATCH III (WW3)** | 3rd-gen phase-averaged spectral | open source (NOAA) | 직교/비구조 | 대양·전 지구·연안 |
| **XBeach** | phase-resolved (surfbeat) + non-hydrostatic | GPL-3.0 | 직교/곡선 | 천해·해변·폭풍 |
| **MIKE 21 SW** | spectral (상용) | 상용 | 비구조 | 연안 |
| **TOMAWAC** | spectral (TELEMAC 가족) | open source (EDF) | 비구조 | 연안 |

## 2. SWAN — Simulating WAves Nearshore

### 2.1 인용 (canonical)

> **Holthuijsen, L. H. (2007). *Waves in Oceanic and Coastal Waters*. Cambridge University Press. Chapter 9 (전체).**
>
> Booij, N., Ris, R. C., & Holthuijsen, L. H. (1999). A third-generation wave model for coastal regions: 1. Model description and validation. *J. Geophys. Res.* **104**(C4), 7649-7666.
>
> 공식 사이트: [https://swanmodel.sourceforge.io/](https://swanmodel.sourceforge.io/)

→ 모델 메커닉 상세는 [`models/SWAN/`](../../models/SWAN/) canonical.

### 2.2 핵심 알고리즘

action balance equation (`02-theory.md` §9.2):
```
∂N/∂t + ∇_x·(c_x N) + ∂(c_θ N)/∂θ + ∂(c_σ N)/∂σ = (S_in + S_nl4 + S_nl3 + S_ds) / σ
```

Source terms (Holthuijsen Ch.9 §9.3):
- **S_in**: 생성 (Komen 1984 또는 Janssen 1991)
- **S_nl4**: quadruplet (DIA — Discrete Interaction Approximation)
- **S_nl3**: triad (천해, LTA — Lumped Triad Approximation)
- **S_ds**: dissipation
  - white-capping (Komen/van der Westhuysen)
  - bottom friction (JONSWAP/Madsen/Collins)
  - depth-induced surf-breaking (Battjes-Janssen 1978)

### 2.3 입력·출력

- **입력 카드**: `CGRID` (계산 격자), `INPGRID BOTTOM/WIND/CURRENT`, `BOUND` (경계 spectrum), `WIND`, `INIT`, `FRIC`, `BREA`, `OUTPUT SPECOUT/TABLE/BLOCK`
- **출력**: 통합 파라미터 (H_s, T_p, 방향 등) + 지점/격자 스펙트럼 (NESTOUT)

→ 정밀 카드 정리: [`models/SWAN/manual-notes/`](../../models/SWAN/manual-notes/) (작성 예정).

### 2.4 사용자 SWAN library (`swan-library-firesinger`)

`D:\Numerical_models\01_Models\swan\Fin\07_SWAN_LIBRARY\`:

| 항목 | 위치 | 역할 |
|---|---|---|
| WINK middle 도메인 | `metadata/wink_middle_areas.csv` | 13개 한국 연안 중간 도메인 (1°×0.9°, dx=0.005°) |
| WINK detail 도메인 | `metadata/wink_detail_areas.csv` | 세밀 도메인 |
| 검증 정점 | `metadata/validation_stations_chuksan.csv` | 축산항 MPT238·TW_0095 |
| 수심 생성 | `tools/build_swan_depth_from_parquet.py` | 대표수심_MSL.parquet → SWAN 격자 |
| AHHW 수심 | `tools/build_ahhw_depths.py` | 약최고고조면 보정 ([`concepts/tides/02-theory.md` §8.2](../tides/02-theory.md)) |
| Hybrid 수심 | `build_hybrid_middle_depth.py`, `build_smooth_hybrid_middle_depth.py` | BADA2024/GEBCO + parquet 합성 |
| JMA-MSM 바람 | `tools/build_jma_uv_monthly.py` | 일본기상청 5 km 격자 바람 |
| Spectrum archive | `spectrum_archive/` | 3-layer 한국 연안 spectrum DB (별도 문서) |

→ WINK 패턴 상세: [`models/SWAN/source-analysis/wink-pattern.md`](../../models/SWAN/source-analysis/wink-pattern.md) (작성 예정).

## 3. WAVEWATCH III (WW3) — NOAA

### 3.1 인용

> Tolman, H. L. et al. — WAVEWATCH III Development Group, NOAA-EMC.
>
> 공식 GitHub: [https://github.com/NOAA-EMC/WW3](https://github.com/NOAA-EMC/WW3)
> Documentation: [https://noaa-emc.github.io/WW3/](https://noaa-emc.github.io/WW3/)
> User manual: [manual.pdf](https://raw.githubusercontent.com/wiki/NOAA-EMC/WW3/files/manual.pdf)

### 3.2 특징

- 3rd-generation spectral, **wavenumber-direction spectra** 풀이
- 핵심: 대양·전 지구 → 점진적 nesting → 연안
- 천해 surf zone 옵션 + wetting/drying
- 50+ scientists/programmers 글로벌 개발 커뮤니티

### 3.3 SWAN vs WW3

| 항목 | SWAN | WW3 |
|---|---|---|
| 주 도메인 | 천해·연안 | 대양·전 지구 (천해 옵션) |
| 격자 | 직교/곡선/비구조 | 직교/비구조 (regular mesh 강점) |
| 천해 비선형 (triad) | LTA built-in | 별도 옵션 |
| GIS 통합 | 다수 도구 | NetCDF 표준 |
| 한국 사용 | 사용자 WINK 패턴 | 외해 일반 (NOAA 기반) |

→ 한국 외해 풍파 forcing은 WW3 글로벌 hindcast (예: NOAA/IOWAGA) → SWAN nested run의 표준 흐름.

### 3.4 SMC nested grid boundary issue ([Issue #1600](https://github.com/NOAA-EMC/WW3/issues/1600), OPEN 2026-05-20)

WW3 SMC (Spherical Multi-Cell) nested grid 운영 시 boundary point mismatch 로 인한 spurious energy bug — UK Met Office 발견 (`ukmo-rwdavies`, 2026-05-20 issue 등록, fix PR 예정). GitHub Issues API 직접 fetch (2026-05-28).

**Bug 메커니즘** (issue body verbatim):

> "Wave energy has been seen to be added along all coastlines of a nested SMC grid model. This has occurred in cases where a boundary point at which lateral boundary conditions are supplied by an outer (e.g. Global) model is not matched with a sea-point within a nested grid."

**재현 절차**:

1. WW3 simulation with outer (e.g. Global) + nested SMC (e.g. regional) model
2. Outer 의 `ww3_grid.nml` 의 `&OUTBND_LINE_NML` namelist 에 boundary output points 지정
3. **그 중 최소 1개 point 가 nested model 의 sea (wet) cells 외 위치**
4. Nested model 을 **quiescent IC + no wind input** (lateral boundary forcing 만)
5. 시뮬레이션 진행 시 모든 coastline cells 에서 매 time-step spurious wave energy 누적

**증상**:

- 모든 coastline cell 에서 동일한 magnitude · direction 의 spurious wave energy
- Boundary 에서 domain interior 로 전파
- T+12h 시점 Hs 의 colorbar cap (≤ 1m) 적용해도 coast 인근 spurious signal 명확 (issue 첨부 screenshot)
- 비교: boundary point 모두 sea cell 매치 시 spurious signal 없음

**한국 적용 영향**:

- 한국은 WW3 글로벌 → SWAN nested 흐름 (§3.3 line 106) — SWAN nested 시 boundary points 모두 sea cell 매치 검증 필요
- NOAA WW3 글로벌 hindcast → 한국 SMC nested (또는 SWAN nested) 시점에 boundary mismatch 검증 권장

**Status (2026-05-28)**:

- Issue OPEN, mingchen-NOAA collaborator confirmed (2026-05-20)
- UK Met Office 의 fix PR 제출 예정 ("This issue will be addressed by the UK Met Office and a pull request will follow")
- Fix merge 후 본 §3.4 본문 갱신 + WW3 release note 추적

## 4. XBeach

### 4.1 인용

> Roelvink, D. et al. — Deltares.
>
> 공식 메뉴얼: [https://xbeach.readthedocs.io/](https://xbeach.readthedocs.io/)
> Manual (2015): [Deltares PDF](https://ftp.soest.hawaii.edu/coastal/Tiffany/Runup/manuals/XBeach_manual_11032015.pdf)
> Non-hydrostatic report: [oss.deltares.nl PDF](https://oss.deltares.nl/documents/4142077/4199062/non-hydrostatic_report_draft.pdf/...)

### 4.2 3 모드

1. **Stationary (hydrostatic)**: 단주기 파의 진폭 평균만 풀이. 단주기 위상 안 풂. **계산 시간 절약**
2. **Surfbeat (instationary, hydrostatic)**: 단주기 envelope + 장주기 (infragravity) wave. wave-group scale.
3. **Non-hydrostatic (wave-resolving)**: 단주기 위상까지 풀이. 비선형 천해 방정식 + 압력 보정. **계산 비용 큰 만큼 정밀**.

### 4.3 적용

- 폭풍 침식·범람 (storm impact)
- Surf zone hydrodynamics
- Avalanching of dune fronts
- 비점착성 sediment transport + 지형 변화 (morphological)

XBeach 상세: [`models/XBeach/`](../../models/XBeach/) (source-analysis 32 + manual-notes 4 verified).

## 5. 기타 도구

| 도구 | 종류 | 비고 |
|---|---|---|
| MIKE 21 SW | 상용 spectral | DHI |
| TOMAWAC | open spectral | TELEMAC 가족 (EDF) |
| **STWAVE** | spectral | US Army Corps |
| **WAM** | 1st gen → 3rd gen 효시 | WAMDI Group 1988 |
| Boussinesq (Funwave, MIKE Boussinesq) | phase-resolved 비선형 분산 | 항만 공명·조도 |
| pyHHO·Python 스펙트럼 분석 | post-processing | matplotlib + scipy.signal |

### 5.1 위상평균 vs 위상해상 모델 종합 리뷰 (Ferdaus et al. 2025) (source-needed)

- 출처: arxiv:2511.21856v1 (Ferdaus·Cooper·Schmidt·Pokhrel·Ioup·Abdelguerfi·Simeonov, 2025-11-26), <https://arxiv.org/abs/2511.21856>
- 요약: 연안공학·해양학 수치 파랑모델을 **위상평균(spectral) vs 위상해상** 축으로 종합 리뷰. 3세대 위상평균 5종 — **SWAN·WAVEWATCH III·MIKE 21 SW·TOMAWAC·WAM** (wave action 보존식) — 의 정식화·지배방정식·기법 평가, 그리고 위상해상 4종 — **FUNWAVE·SWASH·COULWAVE·NHWAVE** (Boussinesq-type + 비정수압) — 비교. 효율·천해 정확도·비선형 wave-wave 상호작용·쇄파·회절·wave-current 상호작용 해상능력을 대비. 운영예보·극한사상·구조물 설계·기후영향 적용과 검증 metric·intercomparison 연구를 정리하고, computational scalability·물리 parameterization·model coupling 한계 + 고해상도/hybrid 신흥 트렌드를 논의.
- 본 위키 접점: §2(SWAN)·§3(WW3)·§5(MIKE21/TOMAWAC/WAM/Boussinesq) 모델 카탈로그를 횡단하는 1차 리뷰 출처. §6 도구 선택 가이드 및 위상해상 모델 선택근거의 학술적 뒷받침.
- citation_status: source-needed (abstract 기반 — 본문 모델별 정량 intercomparison 표·검증 metric 수치 미확인)
- 인용 검증 TODO: full PDF read 시 모델별 정량 비교표·검증 metric·지배방정식 발췌 보강

## 6. 도구 선택 가이드

| 상황 | 권장 |
|---|---|
| 글로벌 대양 hindcast | **WW3** |
| 한국 연안 spectral, 외해 forcing 받아 nested | **SWAN** + WINK 패턴 (`swan-library-firesinger`) |
| 폭풍 침식·범람 시뮬 | **XBeach** (surfbeat 또는 non-hydrostatic) |
| 항만 내부 공명·다중 반사 | Boussinesq (Funwave) |
| 설계파 산출 (재현기간 50/100년) | WW3 글로벌 + POT/Gumbel ([03 §5.3](03-analysis-methods.md)) |
| 한국 spectrum archive (재사용) | 사용자 `swan-library-firesinger/spectrum_archive/` |

## 7. SWAN library 통합 워크플로 (사용자 예시)

```bash
cd /mnt/d/Numerical_models/01_Models/swan/Fin/07_SWAN_LIBRARY

# 1) 수심 생성 (대표수심_MSL.parquet → SWAN 격자)
/mnt/d/Projects/축산항/SWAN/.venv/bin/python3 \
  tools/build_swan_depth_from_parquet.py \
  --area CUSTOM_CHUKSAN \
  --areas-csv metadata/custom_detail_areas.csv \
  --points-csv metadata/check_points.csv \
  --out-dir generated

# 2) JMA-MSM 바람 입력
/mnt/d/Projects/축산항/SWAN/.venv/bin/python3 \
  tools/build_jma_uv_monthly.py \
  --year 2025

# 3) SWAN 실행 (외부)
# 4) NESTOUT → 다음 nesting level
```

상세는 [`swan-library-firesinger` README](../../textbook/sources.yml) 참조.

## 8. 보강

- **각 모델의 라이선스 확인** (LICENSE 파일 직접 읽기)
- WW3 한국 적용 사례 (Pacific basin nesting 등) 추가 인용
- XBeach 천해 검증 한국 사례
- 사용자 spectrum_archive 3-layer 비전 별도 노트 (`experience/swan-spectrum-archive-vision.md` 작성 검토)
- 상용 도구 (MIKE 21 SW) 비교 — 한국 항만 설계에서 사용 빈도

### 8.1 연구 문헌 (research/inbox promote, source-needed)

- **PIML wave runup — XBeach (Saviz Naeini·Snaiki 2024)** — arxiv:[2401.08684](https://arxiv.org/abs/2401.08684). 시간의존 wave runup 을 physics-informed ML 로 예측 — XBeach **Surfbeat(XBSB) 효율 + Nonhydrostatic(XBNH) 정확도** 결합. cGAN 으로 XBSB→XBNH scalogram image-to-image 매핑, 역 wavelet 변환으로 시계열 복원. runup risk 평가. cf. [`05-examples.md`](05-examples.md) · swash-zone runup.
- **식생 drag 계수 보정 — XBeach NH (Amini·Marsooli·Neshat 2024)** — arxiv:[2401.09687](https://arxiv.org/abs/2401.09687). 식생 wave height 감쇠 예측의 핵심 = drag 계수 추정. 수동보정 vs **메타휴리스틱 최적화**(최초적용) vs Tanino-Nepf(2008) 경험식의 XBeach NH 통합 — 3 방법 비교. nature-based flood mitigation 설계.
- citation_status: 위 2건 source-needed (abstract 기반)

## 9. 연결

- `02-theory.md` — action balance, source terms, 분산 관계
- `03-analysis-methods.md` — 스펙트럼 분석 (post-processing)
- `05-examples.md` — MPT 정점 실측 스펙트럼
- `06-model-application.md` — SWAN canonical
- [`models/SWAN/`](../../models/SWAN/) — SWAN 모델 자체 (canonical, 작성 진행)
- 소스 노트:
  - [`textbook/notes/waves-holthuijsen-toc.md`](../../textbook/notes/waves-holthuijsen-toc.md) §Ch.9 — SWAN 알고리즘 1차 reference
- 외부 인용:
  - **Holthuijsen (2007)** Ch.9 — SWAN canonical educational source
  - **Booij, Ris, Holthuijsen (1999)** — SWAN seminal paper
  - **WAVEWATCH III** — [github.com/NOAA-EMC/WW3](https://github.com/NOAA-EMC/WW3)
  - **XBeach** — [xbeach.readthedocs.io](https://xbeach.readthedocs.io/)
  - JMA-MSM — Japan Meteorological Agency Meso-Scale Model
