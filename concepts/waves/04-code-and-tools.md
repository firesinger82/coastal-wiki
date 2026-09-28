---
title: "파랑 — 04 코드와 도구 (SWAN·WAVEWATCH III·XBeach)"
topic: waves
canonical_source: self
citation_status: verified
has_source_needed: true
verification_method: "AI cross-reference: textbook/md/Waves-Holthuijsen2007.md Ch.9 (SWAN canonical) + WebSearch acc. 2026-05-21 (WW3 NOAA, XBeach Deltares). §3.4 추가 (2026-05-28): NOAA-EMC/WW3 Issue #1600 (UK Met Office ukmo-rwdavies, OPEN 2026-05-20) GitHub Issues API 직접 fetch — bug body verbatim 인용 (SMC nested grid boundary point mismatch → coastline spurious wave energy), 재현 절차. Fix PR 제출 예정 (status tracking). **§5.1 full PDF 격상 (2026-09-28)**: arXiv:2511.21856v1 (Ferdaus et al., 2025-11-26) 전문을 curl+pdftotext 로 받아 §3.8.1 Decision Framework·§3.8.2 Application-Specific Recommendations·§3.9+Table 5 Computational Performance·§3.11.2 Statistical Validation Metrics·§3.11.3 Intercomparison 을 직접 인용. 확인 사항: 공간규모(<10 / 10-1,000 / 10^4-10^6 / >10^7 km^2)·수심(<10 / 10-200 / >200 m / 극지)·출력별 권장 모델, SWAN 의 회절이 'limited' 이고 항만 정온도는 위상해상 필요, Table 5 대표 소요(항만 1 km^2 1시간 = FUNWAVE-TVD 10-100 cores 2-10시간 > 전지구 7일 예보 0.5-2시간), GPU 10-50x(WW3·WAM·FUNWAVE-TVD). ★실측 판정: 리뷰는 검증 **지표 정의만** 주고 **수치 합격 임계는 제시하지 않는다** — 06-model-application 의 미출처 임계표는 이 리뷰로 닫히지 않으며, 대신 표준 소재(WISE Group·JCOMM Wave Forecast Verification Project·WMO 검증표준)를 §5.1.3 에 기록했다. ★한계: 리뷰가 다루는 9모델 중 본 위키 수록은 SWAN·WW3·FUNWAVE·SWASH 4종뿐이라 나머지(MIKE 21 SW·TOMAWAC·WAM·COULWAVE·NHWAVE) 서술은 소스 대조 없이 리뷰 인용에 머문다. Table 5 는 representative 추정이지 벤치마크 실측이 아니다(리뷰 자체 단서)."
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

→ 외해 풍파 forcing(예: NOAA/IOWAGA WW3 글로벌 hindcast) → SWAN nested run은 일반적 표준 흐름.

### 3.4 SMC nested grid boundary issue ([Issue #1600](https://github.com/NOAA-EMC/WW3/issues/1600), ✅**CLOSED 2026-06-15**)

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

- 한국은 WW3 글로벌 → SWAN nested 흐름 (§3.3) — SWAN nested 시 boundary points 모두 sea cell 매치 검증 필요
- NOAA WW3 글로벌 hindcast → 한국 SMC nested (또는 SWAN nested) 시점에 boundary mismatch 검증 권장

**Status (2026-07-19 갱신 — GitHub Issues API 재조회)**:

- ✅ **Issue CLOSED — `closed_at` 2026-06-15T17:00:21Z** (등록 2026-05-20, mingchen-NOAA collaborator 확인 후 UK Met Office 대응)
- ⚠ 종료 사유·merge 된 PR 번호·수정 반영 release 는 **미확인** `[source-needed]` — 실사용 전 해당 커밋과 사용 중 WW3 버전 포함 여부 대조 필요
- ★신선도 교훈: 2026-05-28 판이 "OPEN·fix PR 예정"으로 5주간 잔존했다. **외부 이슈 트래커 상태는 시점 종속** — 인용 시 조회일자 병기 + 사용 직전 재확인(프로젝트 freshness 규약)

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

### 5.1 위상평균 vs 위상해상 모델 종합 리뷰 — Ferdaus et al. (2025) ✅ verified (full PDF 판독 2026-09-28)

Ferdaus·Cooper·Schmidt·Pokhrel·Ioup·Abdelguerfi·Simeonov (2025),
"A Comprehensive Review of Phase-Averaged and Phase-Resolving Wave Models for Coastal Modeling
Applications", arXiv:[2511.21856](https://arxiv.org/abs/2511.21856)v1, 2025-11-26.

위상평균 5종(**SWAN · WAVEWATCH III · MIKE 21 SW · TOMAWAC · WAM**)과
위상해상 4종(**FUNWAVE · SWASH · COULWAVE · NHWAVE**)을 정식화·지배방정식·수치기법 축으로 비교한
1차 리뷰다. 본 §2(SWAN)·§3(WW3)·§5 카탈로그를 횡단하고, **§6 도구 선택 가이드의 학술적 뒷받침**이 된다.

#### 5.1.1 결정 프레임워크 — 세 축

| 축 | 구간 | 권장 |
|---|---|---|
| **공간규모** | 항만~국소 연안 **< 10 km²** | SWAN · TOMAWAC · **위상해상** |
| | 지역 연안 **10–1,000 km²** | SWAN · MIKE 21 SW · TOMAWAC |
| | 분지 **10⁴–10⁶ km²** | WAVEWATCH III · WAM |
| | 전지구 **> 10⁷ km²** | WAVEWATCH III · WAM |
| **수심** | **< 10 m**(쇄파) | SWAN 및 위상해상 |
| | 10–200 m | SWAN · MIKE 21 SW · TOMAWAC · WW3 |
| | **> 200 m** | WW3 · WAM |
| | **극지 해빙** | **WW3**(유일 지목) |
| **요구 출력** | bulk 파라미터·방향스펙트럼 | 위상평균 아무거나 |
| | **위상해상 수면·유속장** | 위상해상 **필수** |
| | wave–current 상호작용 | SWAN · MIKE 21 SW · TOMAWAC · 위상해상 |
| | **구조물 회절** | 위상해상 — **SWAN 은 "limited diffraction capability"** |
| | 쓰나미 전파·처오름 | FUNWAVE-TVD · COULWAVE · SWASH |

[^fe-frame]

★ **SWAN 의 회절이 제한적이라는 것이 항만 문제의 분기점이다.** 리뷰는 항만·항내 정온도를
따로 떼어 *"harbor resonance, wave agitation, and vessel motion studies require phase-resolving
models to capture diffraction, reflection, and resonance phenomena"* 라고 적고,
FUNWAVE-TVD·SWASH 를 쓰되 **SWAN 은 경계조건과 예비해석에 두라**고 권한다.
매우 복잡한 형상·파-구조물 상호작용이면 CFD 로 간다.[^fe-app]
[[harbor-tranquility-kds64]] 가 다루는 정온도 문제가 왜 위상평균만으로 닫히지 않는지의 근거다.

응용별 권고도 명시적이다 — 연안공학 설계는 **SWAN 우선**(포괄적 천해물리·정상상태 효율·광범위 검증),
구조물 회절이 필요하면 SWAN 안에 위상해상을 **nesting**. 전지구 운영예보는 **WW3 지배**,
지역은 SWAN 또는 MIKE 21 SW, WAM 은 *"historical continuity and recent GPU acceleration"* 으로 잔존.
기후·재해석은 전지구 WW3/WAM + 지역 SWAN. 쓰나미는 FUNWAVE-TVD 가 널리 쓰인다.[^fe-app]

#### 5.1.2 ★ 계산비용 — 항만 1 km² 가 전지구 7일보다 비싸다

Table 5 의 대표 소요(현대 HPC·효율적 병렬화 가정):[^fe-cost]

| 응용 | 권장 모델 | 자원 | 벽시계 |
|---|---|---|---|
| 전지구 예보 (0.5°, 7일) | WAVEWATCH III | 100–500 cores | **0.5–2 시간** |
| 지역 연안 (100 km², 500 m, 24시간) | SWAN | 1–10 cores | 0.5–2 시간 |
| **항만 (1 km², 10 m, 1시간)** | **FUNWAVE-TVD** | 10–100 cores | **2–10 시간** |
| 쓰나미 분지 전파 (10⁶ km², 1 km, 6시간) | WAVEWATCH III | 50–200 cores | 1–4 시간 |
| **쓰나미 침수 (10 km², 5 m, 1시간)** | **FUNWAVE-TVD** | 50–500 cores | **5–50 시간** |

**공간규모가 비용을 정하지 않는다 — 위상해상이냐 아니냐가 정한다.**
1 km² 항만 1시간 모의가 전지구 7일 예보보다 오래 걸리고, 10 km² 쓰나미 침수는
10⁶ km² 분지 전파보다 한 자릿수 이상 비싸다. 위상을 푸는 대가다.

**GPU 가속은 WAVEWATCH III·WAM·FUNWAVE-TVD 에서 10–50× 속도향상**을 준다고 리뷰가 적는다.[^fe-cost]
([[../../models/FUNWAVE/source-analysis/funwave-gpu-cuda-port]] 가 본 위키의 해당 구현 검수.)

#### 5.1.3 검증 지표 — 정의는 주고 합격선은 주지 않는다

리뷰는 지표를 정리한다 — bias, RMSE, **Scatter Index**(RMSE 를 평균 관측치로 정규화),
상관계수 R, 결정계수 R², symmetric slope(크기·위상 오차 동시 반영),
**Willmott 일치도**(0–1), **Brier Skill Score**(기준 예측 대비, 양수면 개선).
bulk 파라미터를 넘어서면 스펙트럼 거리(Earth Mover's/Wasserstein), wind sea–swell
**스펙트럼 분할**, 방향확산 비교까지 간다.[^fe-metric]

> [!source-needed]
> **그러나 수치 합격 임계는 주지 않는다.** [[06-model-application]] 이
> *"'일반 기준' 수치(RMSE·bias·상관계수·방향오차 임계)는 인용 근거 미확보"* 로 남긴 표는
> **이 리뷰로 닫히지 않는다.** 다만 리뷰가 표준의 소재를 가리킨다 —
> **WISE Group** 비교 연구, **JCOMM Wave Forecast Verification Project**(운영예보 기관 간 대조),
> 그리고 **WMO 의 파랑모델 검증 표준**(국제 일관성 목적).[^fe-metric]
> 그 세 곳이 다음 확보 대상이다.

#### 5.1.4 본 위키 접점·한계

- **§6 도구 선택 가이드**의 근거 — 공간규모·수심·출력 세 축과 응용별 권고가 §5.1.1.
- **[[harbor-tranquility-kds64]]** — SWAN 회절 제한이 정온도 해석의 분기점(§5.1.1).
- **[[../swash-zone/04-code-and-tools]]** — 위상해상 모델 계열 비교와 같은 대상을 다루되,
  그쪽은 swash 처리, 여기는 선택·비용 축.
- **한계** `source-needed`: 리뷰가 드는 **MIKE 21 SW·TOMAWAC·WAM·COULWAVE·NHWAVE 는 본 위키 미수록**이라
  대조 서술을 그대로 옮길 뿐 소스 대조를 하지 못한다. 수록 모델(SWAN·WW3·FUNWAVE·SWASH)에 대해서만
  source-analysis 와 교차 확인이 가능하다.
- **한계** `source-needed`: Table 5 는 *"representative"* 추정이며 리뷰가
  *"Actual performance depends on specific hardware, model configuration, and domain characteristics"*
  라고 단서를 단다 — 벤치마크 실측이 아니다.

## 6. 도구 선택 가이드

| 상황 | 권장 |
|---|---|
| 글로벌 대양 hindcast | **WW3** |
| 연안 spectral, 외해 forcing 받아 nested | **SWAN** (nested run) |
| 폭풍 침식·범람 시뮬 | **XBeach** (surfbeat 또는 non-hydrostatic) |
| 항만 내부 공명·다중 반사 | Boussinesq (Funwave) |
| 설계파 산출 (재현기간 50/100년) | WW3 글로벌 + POT/Gumbel ([03 §5.3](03-analysis-methods.md)) |

> 한국 적용 사례는 바이블 검증(객관 데이터) 후 `experience/` 에 카테고리화 — 본 canonical 미수록. (source-needed)

## 7. 보강

- **각 모델의 라이선스 확인** (LICENSE 파일 직접 읽기)
- WW3 한국 적용 사례 (Pacific basin nesting 등) 추가 인용
- XBeach 천해 검증 한국 사례
- 상용 도구 (MIKE 21 SW) 비교 — 한국 항만 설계에서 사용 빈도

### 7.1 연구 문헌 (research/inbox promote, source-needed)

- **PIML wave runup — XBeach (Saviz Naeini·Snaiki 2024)** — arxiv:[2401.08684](https://arxiv.org/abs/2401.08684). 시간의존 wave runup 을 physics-informed ML 로 예측 — XBeach **Surfbeat(XBSB) 효율 + Nonhydrostatic(XBNH) 정확도** 결합. cGAN 으로 XBSB→XBNH scalogram image-to-image 매핑, 역 wavelet 변환으로 시계열 복원. runup risk 평가. cf. [`05-examples.md`](05-examples.md) · swash-zone runup.
- **식생 drag 계수 보정 — XBeach NH (Amini·Marsooli·Neshat 2024)** — arxiv:[2401.09687](https://arxiv.org/abs/2401.09687). 식생 wave height 감쇠 예측의 핵심 = drag 계수 추정. 수동보정 vs **메타휴리스틱 최적화**(최초적용) vs Tanino-Nepf(2008) 경험식의 XBeach NH 통합 — 3 방법 비교. nature-based flood mitigation 설계.
- citation_status: 위 2건 source-needed (abstract 기반)

## 7.2 §5.1 출처

[^fe-frame]: Ferdaus et al. (2025) arXiv:2511.21856v1 §3.8.1 Decision Framework — 공간규모: *"For harbor to local coastal domains smaller than 10 km2, suitable options include SWAN, TOMAWAC, or phase-resolving models. For regional coastal areas ranging from 10 to 1,000 km2, SWAN, MIKE 21 SW, and TOMAWAC are recommended. At basin scales of approximately 10^4 to 10^6 km2, WAVEWATCH III and WAM are typically employed, while for global domains larger than 10^7 km2, WAVEWATCH III and WAM remain the preferred modeling tools."* 수심: *"in very shallow waters (less than 10 m) with breaking waves, SWAN and other phase-resolving models are recommended; in shallow to intermediate depths (10–200 m) … SWAN, MIKE 21 SW, TOMAWAC, and WAVEWATCH III; in deep ocean environments (greater than 200 m), WAVEWATCH III and WAM are preferred; and in polar regions with sea ice, WAVEWATCH III is the model of choice."* 출력: *"phase-resolved surface elevation and velocity fields require the use of phase-resolving models; wave–current interactions can be represented in SWAN, MIKE 21 SW, TOMAWAC, and in phase-resolving models; diffraction around coastal and offshore structures is captured by phase-resolving models, with SWAN offering only limited diffraction capability; and tsunami propagation and inundation analyses are typically conducted using models such as FUNWAVE-TVD, COULWAVE, or SWASH."*
[^fe-app]: 同 §3.8.2 Application-Specific Recommendations — 연안공학 *"SWAN is the preferred choice due to comprehensive shallow water physics, efficient steady-state computation, and extensive validation. For projects requiring diffraction analysis around structures, phase-resolving models (FUNWAVE-TVD, SWASH) should be used for detailed local analysis, potentially nested within SWAN for boundary conditions."* 운영예보 *"Global operational forecasting is dominated by WAVEWATCH III … WAM continues to be used at some centers due to historical continuity and recent GPU acceleration capabilities."* 항만 *"Harbor resonance, wave agitation, and vessel motion studies require phase-resolving models to capture diffraction, reflection, and resonance phenomena. FUNWAVE-TVD and SWASH are commonly used, with SWAN providing boundary conditions and preliminary analysis. For very complex harbor geometries or wave-structure interactions, CFD models may be necessary."* 쓰나미 *"FUNWAVE-TVD is widely used due to robust TVD numerics, multi-scale nesting capabilities, and extensive validation."*
[^fe-cost]: 同 §3.9 Computational Performance Considerations + Table 5 — 표 행(응용/권장모델/자원/벽시계): 전지구 예보 0.5° 7일 = WAVEWATCH III / 100–500 cores / 0.5–2 hours; 지역 연안 100 km² 500 m 24시간 = SWAN / 1–10 cores / 0.5–2 hours; 항만 1 km² 10 m 1시간 = FUNWAVE-TVD / 10–100 cores / 2–10 hours; 쓰나미 분지 전파 10⁶ km² 1 km 6시간 = WAVEWATCH III / 50–200 cores / 1–4 hours; 쓰나미 침수 10 km² 5 m 1시간 = FUNWAVE-TVD / 50–500 cores / 5–50 hours. 단서 *"These estimates assume modern HPC systems and efficient parallelization. Actual performance depends on specific hardware, model configuration, and domain characteristics."* GPU *"GPU acceleration can provide a 10–50× speedup for supported models (WAVEWATCH III, WAM, and FUNWAVE-TVD)."*
[^fe-metric]: 同 §3.11.2 Statistical Validation Metrics — bias(계통오차=모델−관측 평균차), RMSE, *"the Scatter Index (SI) normalizes RMSE by the mean observation to facilitate comparison across different conditions"*, R(−1~1), R². 특수 지표 *"The symmetric slope accounts for errors in both magnitude and phase, while Willmott's Index of Agreement ranges from 0 to 1, with 1 indicating perfect agreement. The Brier Skill Score (BSS) compares model performance against a baseline or reference prediction, with positive values indicating improvement over the baseline."* 스펙트럼 수준 *"spectral distance parameters like Earth Mover's Distance or Wasserstein distance. Spectral partitioning separates wind sea and swell components … Directional spread comparison validates the directional distribution of wave energy."* 본문 어디에도 **수치 합격 임계는 제시되지 않는다**(본 노트 실측). §3.11.3 이 표준의 소재를 지목 — *"The WISE Group (Wave Modelling Group) has conducted comprehensive reviews and comparisons of wave models"*, *"The JCOMM Wave Forecast Verification Project compares operational wave forecasts from different centers against observations"*, *"The World Meteorological Organization has established wave model verification standards to ensure consistency in validation practices across the international community."*

## 8. 연결

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
