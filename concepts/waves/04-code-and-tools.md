---
title: "파랑 — 04 코드와 도구 (SWAN·WAVEWATCH III·XBeach)"
topic: waves
canonical_source: self
citation_status: verified
has_source_needed: true
verification_method: "AI cross-reference: textbook/md/Waves-Holthuijsen2007.md Ch.9 (SWAN canonical) + WebSearch acc. 2026-05-21 (WW3 NOAA, XBeach Deltares). §3.4 추가 (2026-05-28): NOAA-EMC/WW3 Issue #1600 (UK Met Office ukmo-rwdavies, OPEN 2026-05-20) GitHub Issues API 직접 fetch — bug body verbatim 인용 (SMC nested grid boundary point mismatch → coastline spurious wave energy), 재현 절차. Fix PR 제출 예정 (status tracking). **§5.1 full PDF 격상 (2026-09-28)**: arXiv:2511.21856v1 (Ferdaus et al., 2025-11-26) 전문을 curl+pdftotext 로 받아 §3.8.1 Decision Framework·§3.8.2 Application-Specific Recommendations·§3.9+Table 5 Computational Performance·§3.11.2 Statistical Validation Metrics·§3.11.3 Intercomparison 을 직접 인용. 확인 사항: 공간규모(<10 / 10-1,000 / 10^4-10^6 / >10^7 km^2)·수심(<10 / 10-200 / >200 m / 극지)·출력별 권장 모델, SWAN 의 회절이 'limited' 이고 항만 정온도는 위상해상 필요, Table 5 대표 소요(항만 1 km^2 1시간 = FUNWAVE-TVD 10-100 cores 2-10시간 > 전지구 7일 예보 0.5-2시간), GPU 10-50x(WW3·WAM·FUNWAVE-TVD). ★실측 판정: 리뷰는 검증 **지표 정의만** 주고 **수치 합격 임계는 제시하지 않는다** — 06-model-application 의 미출처 임계표는 이 리뷰로 닫히지 않으며, 대신 표준 소재(WISE Group·JCOMM Wave Forecast Verification Project·WMO 검증표준)를 §5.1.3 에 기록했다. ★한계: 리뷰가 다루는 9모델 중 본 위키 수록은 SWAN·WW3·FUNWAVE·SWASH 4종뿐이라 나머지(MIKE 21 SW·TOMAWAC·WAM·COULWAVE·NHWAVE) 서술은 소스 대조 없이 리뷰 인용에 머문다. Table 5 는 representative 추정이지 벤치마크 실측이 아니다(리뷰 자체 단서). **§7.1 full PDF 격상 (2026-09-28)**: arXiv:2401.08684v1 (Saviz Naeini·Snaiki, 28p) · arXiv:2401.09687v1 (Amini·Marsooli·Neshat, 26p) 전문을 curl+pdftotext 로 받아 방법·설정·Table 2 를 직접 인용. ★실측 판정: (1) PIML runup 의 scalogram MSE 18–22배 개선이 시계열 MSE 에서는 1.3–2.0배로 줄고, 시나리오 1·2 는 cGAN 시계열 MSE 가 XBNH σ² 를 넘는다(위상 skill 없음, 분포 일치만 확인) — 본 노트 재계산. (2) 식생 Cd 최적화 이득은 수동 대비 ≤0.19%p, T&N 계수는 저자 재회귀, 식생 치수(9.5 vs 3.2 mm, λ 19.1 cm vs 3182/m²) 본문 내 모순으로 φ 재현 불가. (3) XBeach 소스 직독: vegetation.F90:327-329 Cdveg<0 자동값은 첫 호출에 s%Cdveg 로 덮어써져 고정 — 저자의 'Cd 시간 불변' 진술과 부합; NH 에서 bulkdragcoeff 입력(H·sigm·k, :731·:742·:745) 내용은 미추적(params.F90:1560-1563 swave 강제 0)."
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

### 7.1 XBeach 연구 문헌 2편 ✅ verified (full PDF 판독 2026-09-28)

#### 7.1.1 PIML wave runup — Saviz Naeini·Snaiki (2024), arXiv:[2401.08684](https://arxiv.org/abs/2401.08684)v1

XBeach **Surfbeat(XBSB)** runup 시계열을 Morlet 웨이블릿 scalogram → RGB 이미지로 바꾸고,
pix2pix 계열 cGAN(U-Net 생성기 + PatchGAN 판별기, λ_L1=100)으로 **Nonhydrostatic(XBNH)** scalogram 을
예측한 뒤 역변환으로 시계열을 복원한다.[^px-method] 원 cGAN 은 [`storm-surge/07-ml-emulators`](../storm-surge/07-ml-emulators.md) 계열과 같은
"저충실도 → 고충실도" 매핑이되, 입력이 **물리모델(XBSB) 출력**이라는 점이 "physics-informed" 의 실체다
(손실함수에 물리 제약은 없다 — 식 11–13 은 표준 cGAN+L1).

| 항목 | 논문 값 |
|---|---|
| 영역 | **1D 실험수조 단면** ~30 m, 수심 −0.5→+0.4 m, SWL 0.05 m (Demirbilek et al. 2007 fringing reef 수조 재현) |
| 격자 | XBNH 2.5 cm 균일 / XBSB 5→2.5 cm, Manning 0.01 |
| 강제 | JONSWAP, Hm0 0.05–0.085 m · fp 0.55–1 Hz · γ 1–3.3 변화, mainang 270° · dsc 1000 · fnyq 1 Hz 고정 |
| 데이터 | 모드별 100 run × 1800 s (spin-up 150 s 제외), 무작위 90/10 분할 → **본문 보고 시나리오 3건** |
| 비용 | XBNH ≈ 5 분 / XBSB < 2.5 분 → cGAN 파이프라인 ≈ XBSB 시간 = **약 2배 단축** |

★ **scalogram 공간의 개선이 시간영역에서 크게 줄어든다** (Table 2·§4.3 수치로 재계산).[^px-t2]

| 시나리오 | scalogram MSE 비 (XBSB/cGAN) | 시계열 MSE 비 (XBSB/cGAN) | cGAN 시계열 MSE ÷ XBNH σ² |
|---|---|---|---|
| 1 | 18.0 | 1.29 | **1.87** (σ 반올림 범위 1.6–2.2) |
| 2 | 20.2 | 1.40 | **1.75** (1.55–2.0) |
| 3 | 22.0 | 1.97 | 0.97 (0.90–1.05) |

- 마지막 열이 1 을 넘으면 **"XBNH 평균값 하나를 예측"하는 것보다 시계열 MSE 가 크다** — 즉 1·2 시나리오에서
  위상 일치 기술(skill)은 없고, 논문이 확인한 것은 **평균·σ 의 분포 일치**(Table 2)다.
  "good agreement" 는 Fig. 9 육안 판정이다. XBSB 역시 시계열 MSE 가 σ² 의 1.9–2.5배라, 두 모드 모두 XBNH 와
  개별 파 위상을 맞추지 못한다는 점은 XBSB 가 입사대역을 풀지 않는다는 구조(§4.2)와 부합한다.
- 시나리오 1 cGAN **MAE 0.0001 m** 는 같은 행 RMSE(√9.16e-5 ≈ 0.0096 m)와 두 자릿수 차이이고
  다른 행(MAE ≈ 0.8×RMSE)과 어긋난다 — **표기 오류 의심**(원문 그대로 둔다).
- **runup 추출 정의가 본문에 없다** — gauge 위치·`rugdepth` 미기재. XBeach 기본 설정에서는 처오름 임계가
  침수-건조 임계 `eps` 로 승격되므로([`xbeach_output.md §C.2`](../../models/XBeach/source-analysis/xbeach_output.md)),
  이 논문의 "runup 시계열"은 설정 의존량이다.
- 적용 한계(저자 명시): **단일 단면에서만 유효, 새 지형은 재학습**, 계산시간 하한이 XBSB 실행시간에 묶인다.[^px-lim]
- 부수: 식 (3) 의 $D_w$ 를 "dispersion due to wave breaking" 이라 부르나 문맥상 **쇄파 소산(dissipation)** 이다.

#### 7.1.2 식생 drag 계수 보정 — Amini·Marsooli·Neshat (2024), arXiv:[2401.09687](https://arxiv.org/abs/2401.09687)v1

XBNH 로 Wu et al. (2011) 1:21 경사 식생 수조(강체 원기둥, JONSWAP Hs 3.7–7.9 cm · Tp 1.2–1.8 s, 4 case)를
재현하며 $C_D$ 결정법 셋을 비교: **수동 보정**($C_D$ 1.8–2.8 탐색) · **메타휴리스틱**(GWO·MFO, 에이전트 10 × 400 반복,
탐색 범위 1.8–10) · **Tanino-Nepf(2008) 벌크식을 XBNH 에 이식**($C_D = 2(\alpha_0/R_p + \alpha_1)$).[^am-method]
XBNH 설정 `maxbrsteep`=0.65 · `breakviscfac`=1.5 (Amini & Marsooli 2023 선행 보정값).

| Case | 수동 | T&N 식 | GWO | MFO |
|---|---|---|---|---|
| I | 3.49 % | **5.91 %** | 3.56 % | 3.47 % |
| II | 2.81 % | 2.86 % | 2.69 % | 2.66 % |
| III | 4.87 % | 5.45 % | 4.68 % | 4.81 % |
| IV | 4.17 % | 4.16 % | 4.08 % | 4.09 % |

(파고 정규화 RMSE, Table 2)[^am-t2]

- ★ **최적화의 이득은 수동 대비 최대 0.19 %p**(Case III) — 결론부의 *"major advance"* 는 정확도가 아니라
  **자동화**에 대한 주장으로 읽어야 한다. 비용은 case 당 XBNH 최대 ~4000 회 평가(10 × 400).
  최적 $C_D$ 값 자체는 표로 주지 않는다(Fig. 8·9 그림만).
- ★ **"T&N 식"은 원식 계수가 아니다** — $\alpha_1 = 0.56 + 4.08\varphi$ ($R^2$ 0.94), $\alpha_0 = 5.26 + 318.1\varphi$ ($R^2$ 0.83)
  를 저자들이 문헌 자료로 **재회귀**했다. 또 T&N 은 **emergent** 원기둥 배열 · $R_p$ 40–685 에서 유도됐는데,
  여기서는 submerged 식생($h_v$ 20 cm)에 Stone & Shen (2002) 식생층 평균유속 보정을 얹어 쓴다. T&N 오차가
  소파고 Case I 에서 가장 크고 Case IV 에서 사라지는 것을 저자는 $R_p$ 유효범위 이탈로 설명한다(검증은 안 함).
- ★ **재현 불가 지점 — 식생 치수가 본문 안에서 모순된다.** 줄기 지름이 "9.5 mm birch dowels" 와 $b_v$ = 3.2 mm 로
  두 번 나오고, 간격 λ = 19.1 cm 는 $N_v$ = 3182 stems/m² 와 맞지 않는다(엇갈림 배열 $2/(\sqrt3\lambda^2)$ 로
  λ = 1.91 cm → 3165/m², 19.1 cm → 32/m²).[^am-dim] 두 지름 비(2.97)와 밀도 비 3182/350 = 9.09 ≈ 3² 는
  **1:3 모형/원형 척도 혼용**을 시사하나 어느 쪽이 수조값인지는 이 논문만으로 판정 불가(`source-needed`: Wu et al. 2011 원전).
  영향이 크다 — $\varphi = N_v\pi b_v^2/4$ 가 0.026(3.2 mm) 대 0.226(9.5 mm)이 되어 $\alpha_0$ 가 13.4 대 77.0 으로 갈린다.
  논문은 사용한 $\varphi$ 를 밝히지 않는다.
- **XBeach 소스 대조** — 저자의 *"the drag coefficient in the model is a predefined temporally constant value"* 는
  기본 제공 자동 옵션까지 포함해도 성립한다. `Cdveg < 0` 이면 `bulkdragcoeff`(Mendez & Losada 2004 eq. 40,
  소스 주석 *"Only applicable for Laminaria Hyperborea (kelp)???"*)가 호출되지만 결과를 **`s%Cdveg` 에 덮어써**
  다음 호출부터 조건이 거짓이 된다 — 첫 `vegatt` 호출에서 한 번 계산되고 고정된다
  (`vegetation.F90:327-329`, `:763`). 또 그 식은 단파 작용량 필드 `s%H`·`s%sigm`·`s%k` 로 KC 를 만드는데
  (`:731`, `:742`, `:745`) NH 모드는 `swave` 를 강제로 0 으로 둔다(`params.F90:1560-1563`).
  NH 에서 그 필드가 무엇을 담는지는 여기서 추적하지 않았다 → 모델 메커닉은
  [`xbeach_vegetation.md`](../../models/XBeach/source-analysis/xbeach_vegetation.md) 후속 대상.

[^px-method]: Saviz Naeini & Snaiki (2024) arXiv:2401.08684v1 §3.1–3.2, §4.2 — *"a Conditional Generative Adversarial Network (cGAN) is employed to establish a mapping between the image representations of the XBSB-based scalograms and the XBNH-based scalograms"*; 생성기 C64-C128-C128-C256-C256-C512×5 / CD512×4-CD256×2-CD128×2-CD64, 4×4 stride 2; *"The weighting parameter λ of Eq. (13) was set to a large value of 100"*; *"The implementation of the entire framework is based on pix2pixGAN project (Isola et al., 2017)"*. 설정 §4.1 — *"The domain size extends approximately 30 m in the cross-shore direction. The depth of the 1D profile ranges from -0.5 m offshore to 0.4 m nearshore. The still water level (SWL) is set at 0.05 m"*; *"A uniform grid size of 2.5 cm is utilized for XBNH, whereas for XBSB, the grid spacing varies from 5 cm offshore to 2.5 cm closer to the shoreline"*; *"a total of 100 experiments were conducted for each mode … 0.05 ≤ Hm0 (m) ≤ 0.085, 0.55 ≤ fp (Hz) ≤ 1, and 1 ≤ γ ≤ 3.3"*; *"On average, each simulation using the XBNH mode lasted approximately 5 minutes, whereas the simulations using the XBSB mode required less than 2 minutes and a half"*.
[^px-t2]: 同 §4.3 — scalogram MSE *"between the cGAN-based and the XBNH-based scalograms are 1.06e-06, 1.26e-06, and 2.37e-06 … between the XBSB-based and the XBNH-based scalograms are 1.91e-05, 2.54e-05, and 5.21e-05"*. Table 2 (XBNH mean/σ; cGAN mean/σ/MSE/MAE; XBSB mean/σ/MSE/MAE, m·m²): 1st 0.055/0.007; 0.056/0.007/9.16e-5/0.0001; 0.053/0.008/1.18e-4/0.008 · 2nd 0.055/0.008; 0.053/0.008/1.12e-4/0.008; 0.056/0.010/1.57e-4/0.010 · 3rd 0.061/0.013; 0.058/0.012/1.64e-4/0.010; 0.059/0.014/3.23e-4/0.015. 비율·σ² 비교는 본 노트 계산이며 σ 가 1 mm 단위로 반올림돼 있어 범위로 적었다.
[^px-lim]: 同 §5 — *"its applicability is restricted to a single coastal profile (Fig. 3). With a new basin configuration, it's necessary to retrain the model"*; *"the cGAN model necessitates the use of low-fidelity simulations from XBSB mode as input … leading to a total simulation time comparable to XBSB"*; *"the proposed model reduces the time required for high-fidelity simulation by almost half"*.
[^am-method]: Amini, Marsooli & Neshat (2024) arXiv:2401.09687v1 §2.1–2.3 — T&N *"C_D = 2(α0/Rp + α1)"*, *"we applied a linear relationship between α1 and φ, expressed as α1 = 0.56 + 4.08 φ with the R² value of 0.94 … α0 = 5.26 + 318.1 φ, displaying an R² value of 0.83"*; *"maxbrsteep was set to 0.65 and breakviscfac was set to 1.5"*; *"The values of Cd range from 1.8 to 10 … the constraint for the decision variable is considered as 1.8 ≤ Cd ≤ 10"*; Appendix Algorithm 1·2 *"N=10, Max_iter=400"*. §1 *"This represents an improvement to the XBNH model, given that the drag coefficient in the model is a predefined temporally constant value."* §3 *"T&N formula being developed and validated for a limited range of plant Reynolds numbers between 40-685"*.
[^am-t2]: 同 Table 2 *"Root-mean-square-error (RMSE) of the different approaches across four cases"*; 수동 탐색 §3 *"For each case, we manually tested different drag coefficient (Cd) values between 1.8 and 2.8 … Cd values above 2.8 are not simulated as the errors increased for all cases"*. 결론 §4 *"This represents a major advance by harnessing optimization techniques to improve the accuracy, efficiency, and consistency of Cd calibration."*
[^am-dim]: 同 §2.2 — *"The rigid model vegetation consisted of uniform cylindrical birch dowels with a diameter of 9.5 mm"* 와 *"scaled rigid vegetation with a density of Nv=3182 stems/m2, stem diameter of bv=3.2 mm, and height of hv=20 cm were installed along the sloping beach profile with the spacing of λ=19.1 cm to represent a full-scale density of 350 stems/m2"*. 밀도·φ·α 역산은 본 노트 계산.

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
