---
title: "조석 — 04 코드와 도구 + 전 지구 조석 모델"
topic: tides
canonical_source: self
citation_status: verified
has_source_needed: true
verification_method: "AI programmatic cross-reference against textbook/md/stewart_textbook.md + textbook/md/Manual_for_Tidal_Heights_Analysis_and_Pr.md, plus WebSearch (2026-05-21) for external repos/papers/tide models — DOI, GitHub URL, official project pages, model documentation. 인용 URL은 acc. 2026-05-21."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-21
verification_by: "Claude Opus 4.7 (1M context) — cross-ref + WebSearch"
verification_date: 2026-05-21
---

# 조석 — 04 코드·도구 및 전 지구 조석 모델

두 카테고리:
- **분석 도구 (analysis tools)** — 시계열에서 조화상수 추출·예측 (§2-5)
- **전 지구 조석 모델 (global tide models)** — 위성고도계·hydrodynamic 기반 분조 데이터 제품 (§6)

사용 예제는 별도 (`05-examples.md`).

## 1. 도구 비교 요약

| 도구 | 언어 | 알고리즘 출처 | 라이선스 | 활성도 (2026-05) |
|---|---|---|---|---|
| **t_tide** | MATLAB | Foreman 1977 + 자체 error estimates | (개별 확인 필요) | maintained (UBC) |
| **UTide** | MATLAB / Python | 통합 admittance·IRLS robust fit | (개별 확인 필요) | maintained (URI / PyPI) |
| **pytides** | Python | Schureman 1958 (NOAA SP No. 98) | (개별 확인 필요) | 정체 (Python 2 origin), python3 fork 존재 |
| **pyTMD** | Python | Doodson & Lamb 1921 + TPXO/FES/GOT | (개별 확인 필요) | active (NASA GSFC/UW-APL) |

> 라이선스는 각 repo의 LICENSE 파일 직접 확인 권장 — 본 표는 공백으로 두고 사용자 검토 시 채움.

## 2. t_tide (MATLAB)

### 인용 정보

> Pawlowicz, R., Beardsley, B., & Lentz, S. (2002). **Classical tidal harmonic analysis including error estimates in MATLAB using T_TIDE.** *Computers & Geosciences*, **28**(8), 929–937. DOI: [10.1016/S0098-3004(02)00013-4](https://doi.org/10.1016/S0098-3004(02)00013-4)

- 저자: Rich Pawlowicz (UBC), Bob Beardsley (WHOI), Steve Lentz (WHOI)
- 홈페이지 (저자 직접 배포): [https://www.eoas.ubc.ca/~rich/](https://www.eoas.ubc.ca/~rich/)
- 사회과학·해양학 인용수 가장 높음 — 사실상 **MATLAB 조석 분석의 표준 (de facto)**

### 알고리즘 특성 (논문 abstract 발췌)

- 고전적(Foreman-식) **harmonic analysis with nodal corrections**
- **inference** 기능 — 약한 분조를 인접 강한 분조의 admittance로 추론
- **~1년 이하** 시계열 권장
- **confidence intervals** 자동 계산 (analyzed components의)
- 사용자 지정 옵션 다수

### 알고리즘 ↔ Foreman 1977 매핑

- 사용 분조 set: Foreman 1977 (146 분조, [tides-foreman1977-appendix.md](../../textbook/notes/tides-foreman1977-appendix.md))
- nodal correction satellite data: Foreman 1977 appendix p.59-62 (canonical)
- 즉 **t_tide = Foreman 1977 알고리즘 + MATLAB 구현 + error analysis** 보강

### 사용 사이클 (개념)

1. 시계열 + 위도·기준시각 입력
2. `t_tide(elevation, 'interval', dt, 'start time', t0, 'latitude', lat)` 호출
3. 출력: 분조별 (frequency, amplitude, phase, amp/phase error) 표
4. 예측: `t_predic(t, t_tide_output)` 사용

> 실제 예제 코드는 `05-examples.md` 작성 시 추가. 본 문서는 알고리즘·인용 정리에 한정.

## 3. UTide (MATLAB / Python)

### 인용 정보 (Technical Report — canonical)

> Codiga, D. L. (2011). **Unified Tidal Analysis and Prediction Using the UTide Matlab Functions.** Technical Report 2011-01, Graduate School of Oceanography, University of Rhode Island, Narragansett, RI. 59 pp.
>
> URL (full PDF): [https://www.po.gso.uri.edu/codiga/utide/2011Codiga-UTide-Report.pdf](https://www.po.gso.uri.edu/codiga/utide/2011Codiga-UTide-Report.pdf)
> Project page: [https://www.po.gso.uri.edu/~codiga/utide/utide.htm](https://www.po.gso.uri.edu/~codiga/utide/utide.htm)

저널 paper도 존재 (별도 ResearchGate 등재) — 정식 인용 시 technical report URL 권장.

### Python 포트

> Bowman, W. et al. **UTide (Python)** — Python re-implementation of the MATLAB UTide package.
>
> GitHub: [https://github.com/wesleybowman/UTide](https://github.com/wesleybowman/UTide)
> PyPI: [`utide`](https://pypi.org/project/utide/)

설치:
```bash
pip install utide
```

### 알고리즘 특성 (Codiga 2011, Bowman README 종합)

- **t_tide 후계**, 알고리즘 통합·확장
- **irregularly distributed times** 지원 — gap 있는 시계열, 비균일 sampling 처리 (t_tide는 균일 시간 가정)
- **2D 케이스** 지원 — 조류 (u, v) 입력 시 current ellipse parameter 출력
- 1D 케이스 (scalar 조위)는 2D 코드의 자연스러운 축소
- **IRLS (Iteratively Reweighted Least Squares) robust fitting** — outlier 자동 down-weight
- **자기-정합 방정식 집합 (self-consistent and complete)** — 통합 framework 강조

### 알고리즘 ↔ Foreman / t_tide

- 분조 set: Foreman 1977 기반 확장
- nodal correction: 자체 통합 처리 (irregular time 일관성)
- 한국 연안 적용 시: 서해 비선형 조석에서 IRLS robust 적합 유리

## 4. pytides (Python)

### Repo·문헌

> Cox, Sam. **pytides** — Tide prediction and analysis in Python.
>
> GitHub: [https://github.com/sam-cox/pytides](https://github.com/sam-cox/pytides)
> PyPI: [`pytides`](https://pypi.org/project/pytides/)
> Python 3 fork: [`pytides-py3`](https://pypi.org/project/pytides-py3/) (원본은 Python 2 기반)
> Wiki — Theory: [https://github.com/sam-cox/pytides/wiki/Theory-of-the-Harmonic-Model-of-Tides](https://github.com/sam-cox/pytides/wiki/Theory-of-the-Harmonic-Model-of-Tides)

### 알고리즘 출처

- 기초 이론: **Schureman, P. (1958). Manual of Harmonic Analysis and Prediction of Tides. U.S. Coast and Geodetic Survey, Special Publication No. 98.**
- 적합: SciPy `leastsq` 사용 (raw nonlinear least squares)
- 분조 set: **NOAA published harmonic constituents** 직접 사용 가능 — 별도 분석 없이 NOAA 진폭·위상으로 예측

### 시간 표기 주의 (Wiki 인용)

> "It is recommended that all interactions with pytides which require times to be specified are in the format of **naive UTC datetime** instances. pytides makes no adjustment for summertime or any other civil variations within timezones."

→ 한국 표준시(KST) 데이터 사용 시 UTC 변환 후 입력 필수.

### 위치

- **틈새**: NOAA 분조 데이터 직접 사용 + 짧은 코드 — 학습용·간단한 예측에 적합
- **한계**: t_tide / UTide 같은 정밀 error analysis·robust fitting 없음. 큰 분석 프로젝트는 UTide 권장

## 5. pyTMD (Python)

### 인용 정보

> Sutterley, T. C., et al. (2025). **pyTMD: Python-based tidal prediction software.** *Journal of Open Source Software*. paper id: joss.08566.
>
> Paper PDF: [https://www.theoj.org/joss-papers/joss.08566/10.21105.joss.08566.pdf](https://www.theoj.org/joss-papers/joss.08566/10.21105.joss.08566.pdf)
> GitHub: [https://github.com/pyTMD/pyTMD](https://github.com/pyTMD/pyTMD)
> PyPI: [`pyTMD`](https://pypi.org/project/pyTMD/)

소속: NASA Goddard Space Flight Center (GSFC) + University of Washington Applied Physics Laboratory (UW-APL).

### 알고리즘 출처

- 천체 인수 계산: **Doodson & Lamb (1921)** astronomical argument formalism
- 분조 보간: `pyTMD.io`가 모델 격자에서 임의 위치로 분조 interpolation
- 시간 처리: pyTMD 자체 시간 시스템 (Julian/seconds since epoch)

### 지원 모델 (Tide Model)

전 지구 위성 기반 조석 모델 직접 사용:

| 모델군 | 출처 | 특징 |
|---|---|---|
| TPXO | OSU / Egbert & Erofeeva | 위성고도계 + assimilation, 가장 널리 사용 |
| FES (2014/2022) | AVISO / FES Group | 유럽 표준, 진폭·위상 격자 |
| GOT | NASA GSFC | Topex/Poseidon 기반 |
| EOT | DGFI-TUM | European Tide |

### 위치

- **틈새**: 전 지구 위성고도계 데이터 분석, ICESat-2 등 (위성에서 임의 위치의 조석 보정 필요)
- 연안 분석에는 무거움 — 격자 해상도가 연안 sub-grid 미해상
- OTPS/OTIS (Fortran) / TMD (MATLAB)의 Python 대안

## 6. 전 지구 조석 모델 (Global Tide Models)

조석 모델 = **분조 데이터 제품**. 격자 위에서 각 분조의 진폭·위상을 제공. 해양·해안 모델(EFDC, ADCIRC 등)의 경계 조건 forcing, 위성고도계 보정, 항해·해석에 사용. 분석 도구(§2-5)의 입력 또는 비교 reference로도 활용.

### 6.1 모델 비교 요약

| 모델 | 개발 | 기법 | 격자 | 분조 수 | 인용 |
|---|---|---|---|---|---|
| **TPXO** | OSU (Egbert & Erofeeva) | inverse + altimeter assimilation (OTIS) | 1/30° (TPXO10 atlas) | 15+ | Egbert & Erofeeva 2002 |
| **FES** | LEGOS/CNES/AVISO | finite element T-UGOm + altimeter assim | 1/30°×1/30° (FES2022) | 34 (FES2014) | Lyard et al. 2021 (FES2014) |
| **NAO** | NAO Japan (Matsumoto et al.) | altimeter + tide gauge assim, hydrodynamic | 0.5° 글로벌 / 1/12° Japan | 16 | Matsumoto et al. 2000 |
| **GOT** | NASA GSFC (Ray) | empirical altimeter (no hydrodynamic) | varies | 10 (GOT4.10), more (GOT5) | Ray et al. — GOT5 NASA TM 2025 |
| **EOT** | DGFI-TUM Germany | empirical multi-mission altimeter | varies (EOT20) | 13 (EOT20) | 별도 확인 필요 |

### 6.2 TPXO (Egbert & Erofeeva, Oregon State)

> Egbert, G. D., & Erofeeva, S. Y. (2002). **Efficient Inverse Modeling of Barotropic Ocean Tides.** *Journal of Atmospheric and Oceanic Technology*, **19**(2), 183-204. [AMS link](https://journals.ametsoc.org/view/journals/atot/19/2/1520-0426_2002_019_0183_eimobo_2_0_co_2.xml)
>
> 공식 사이트: [https://www.tpxo.net/](https://www.tpxo.net/) — 등록 후 다운로드
> Earlier basis: Egbert, Bennett, Foreman (1994)

**알고리즘**:
- **OTIS** (OSU Tidal Inversion Software) 패키지로 구현
- Generalized inverse penalty functional 최소화 (representer method)
- Frequency-domain linearized shallow-water 방정식 (forward + adjoint) 반복 풀이
- **위성고도계(TOPEX/Poseidon, Jason 등) + 일부 tide gauge** assimilation

**버전 이력 (발견된 references)**:
- TPXO.2, TPXO.6, TPXO7.1, TPXO8, TPXO9, **TPXO10** (가장 최근)
- 글로벌 + 지역(regional) + 로컬(local) 변종 다수

**한국 적용 사례**:
- East-Asian Seas에서 OTIS를 활용해 개선된 tidal prediction 생성한 연구 존재 ([researchgate citation 발견](https://www.researchgate.net/publication/235016434_Use_of_the_Oregon_State_University_Tidal_Inversion_Software_OTIS_to_Generate_Improved_Tidal_Prediction_in_the_East-Asian_Seas))

**위치**:
- **사실상 표준** (de facto). 위성·해안 두 영역 모두에서 가장 많이 인용
- 한계: 격자 해상도가 한국 서해 sub-inlet 수준은 미해상

### 6.3 FES — Finite Element Solution (LEGOS/CNES/AVISO)

> **공식 사이트**: [https://www.aviso.altimetry.fr/en/data/products/auxiliary-products/global-tide-fes.html](https://www.aviso.altimetry.fr/en/data/products/auxiliary-products/global-tide-fes.html)
>
> FES2014 paper preprint: [https://os.copernicus.org/preprints/os-2020-96/os-2020-96-manuscript-version6.pdf](https://os.copernicus.org/preprints/os-2020-96/os-2020-96-manuscript-version6.pdf)
> FES2022 description: [https://www.aviso.altimetry.fr/en/data/products/auxiliary-products/global-tide-fes/release-fes22.html](https://www.aviso.altimetry.fr/en/data/products/auxiliary-products/global-tide-fes/release-fes22.html)
> Code: [https://github.com/CNES/aviso-fes](https://github.com/CNES/aviso-fes) (PyFES)

**기관 협력**: CNES (자금) + LEGOS + NOVELTIS + CLS

**알고리즘**:
- **T-UGOm** (T-UGO model) — 2D/3D **unstructured grid** hydrodynamic
  - finite element / finite volume (연속·불연속) 옵션
  - triangle / quadrangle elements
  - Boussinesq 근사 Navier-Stokes 기반
- spectral configuration으로 tidal barotropic 방정식 풀이
- 위성고도계 + tide gauge assimilation

**FES2022 vs FES2014 (개선점)**:
- 천해·연안 bathymetry 정밀화
- 전 지구 격자 refinement (고해상도)
- altimeter·tide gauge 데이터셋 확장
- T-UGO model 개선 (spectral + sequential 양 모드)

**격자**: FES2022 = **1/30°×1/30°** (약 3.7 km @ 적도)

**데이터 구성**:
- **Tide elevation**: 각 분조 진폭·위상
- **Tide loading**: 각 분조 진폭·위상 (지각 변형 효과)

**Python 인터페이스**: PyFES — [https://cnes.github.io/aviso-fes/](https://cnes.github.io/aviso-fes/)

**위치**:
- 유럽 표준, 위성 ESA·CNES 미션의 표준 조석 보정
- 연안에서 TPXO 대비 unstructured grid 장점

### 6.4 NAO — National Astronomical Observatory of Japan

> Matsumoto, K., Takanezawa, T., & Ooe, M. (2000). **Ocean Tide Models Developed by Assimilating TOPEX/POSEIDON Altimeter Data into Hydrodynamical Model: A Global Model and a Regional Model around Japan.** *Journal of Oceanography*, **56**(5), 567-581.
>
> DOI: [10.1023/A:1011157212596](https://doi.org/10.1023/A:1011157212596)
> 공식 사이트: [https://www.miz.nao.ac.jp/staffs/nao99](https://www.miz.nao.ac.jp/staffs/nao99)
> 영문 페이지: [https://www.miz.nao.ac.jp/rise/s/nao99/index_En.html](https://www.miz.nao.ac.jp/rise/s/nao99/index_En.html)

**기관**: National Astronomical Observatory of Japan (NAO), 후속 RISE 프로젝트

**모델 2종**:

| 모델 | 영역 | 격자 | 데이터 |
|---|---|---|---|
| **NAO.99b** | 글로벌 | 0.5° | TOPEX/POSEIDON 5년 altimeter |
| **NAO.99Jb** | 일본 주변 (지역) | **1/12°** | T/P + 219개 연안 tide gauge |

**분조 수**: 주요 16 분조

**알고리즘**: barotropic hydrodynamic + altimeter assimilation. CSR4.0·GOT99.2b 등 동시대 모델 대비 천해에서 오차 적음 (Matsumoto et al. 2000 비교).

**한국 적용 관점**:
- **NAO.99Jb (regional 1/12°)**는 일본 주변 + 동해·동중국해 부분에서 글로벌 TPXO보다 정확할 가능성
- 한국 서해 (황해)는 NAO.99Jb 영역 가장자리 — KHOA 자체 모델·tide gauge 조합 권장
- 동해 (조차 0.2-0.4 m, 일주조 우세)에서 NAO.99Jb 유용

**보강 필요**: 한국 서해·남해에서 NAO.99Jb vs TPXO9/10 vs FES2022 정확도 비교 자료

### 6.5 GOT — Goddard Ocean Tide (NASA GSFC)

> Ray, R. D. (2025). **Documentation for Goddard Ocean Tide Solution GOT5: Global Tides from Multi-mission Satellite Altimetry.** NASA Technical Memorandum NASA/TM-20250002085.
>
> Full PDF: [https://ntrs.nasa.gov/api/citations/20250002085/downloads/GOT5-TechMemo.pdf](https://ntrs.nasa.gov/api/citations/20250002085/downloads/GOT5-TechMemo.pdf)
> NASA Earth ocean tide models: [https://earth.gsfc.nasa.gov/geo/data/ocean-tide-models](https://earth.gsfc.nasa.gov/geo/data/ocean-tide-models)

**주저자**: Richard Ray (NASA GSFC)

**알고리즘**: **경험적 (empirical)** — hydrodynamic 모델 없이 위성고도계 데이터에서 직접 분조 진폭·위상 적합. 다른 모델(TPXO·FES)과 근본적으로 다른 접근.

**버전**:
- **GOT4.10**: Jason-1, Jason-2 데이터, 10 분조 (M₂·S₂·N₂·K₂·K₁·O₁·P₁·Q₁·Mf·Mm)
- **GOT5** (2025): TP + J1 + J2 + J3 + Sentinel-6 MF (5개 위성, 수십년 데이터). FES2014를 prior로 사용 (대부분 deep ocean)

**유효 영역**: 위도 ±66° 이내 deep ocean.

**위치**:
- 위성 altimetry 표준 보정으로 가장 많이 사용 (NASA·NOAA 미션 표준)
- 천해·연안에서는 FES/TPXO 권장 (GOT는 deep ocean 위주)

### 6.6 EOT — Empirical Ocean Tide (DGFI-TUM)

> 공식 출처는 별도 확인 필요. **EOT11a**, **EOT20** 버전 존재 (DGFI-TUM = Deutsches Geodätisches Forschungsinstitut, Technische Universität München).

**알고리즘**: empirical multi-mission altimeter. GOT 류 접근과 유사.

**위치**: 위성 측지 (geodesy) 응용. 표준 비교 모델 중 하나.

> 추가 인용 (Lyard FES2014, EOT 정식 paper, Egbert+Bennett+Foreman 1994 등)은 별도 WebSearch 또는 직접 인용 보강 후 추가.

### 6.7 한국·동아시아 적용 권장 흐름

| 영역 | 1차 권장 | 2차 보강 | 비고 |
|---|---|---|---|
| 한국 서해 (황해) | **FES2022** (1/30°, 천해 최적) | TPXO10 | KHOA tide gauge로 검증·보정 필수 |
| 한국 남해 | FES2022 또는 TPXO10 | NAO.99Jb (가장자리) | 부산·여수 정점 검증 |
| 한국 동해 | NAO.99Jb (regional 1/12°) | TPXO10 | 일주조 우세, K₁·O₁ 중요 |
| 동중국해 | NAO.99Jb 또는 FES2022 | TPXO10 | 양쯔강 영향 |
| 일본 주변 | **NAO.99Jb** | FES2022 | 원조 regional 모델 |
| 위성 altimetry 보정 | **GOT5** 또는 FES2022 | — | NASA·CNES 미션 표준 |

> 위 권장 표는 일반론·문헌 권장 — 특정 프로젝트 적용 시 **tide gauge 검증 필수**. 검증 결과는 `experience/`에 (3조건 통과 시).

### 6.8 모델 데이터 → 분석 도구 연결

| 분석 도구 | 직접 읽는 모델 |
|---|---|
| **pyTMD** | TPXO, FES, GOT, EOT 모두 |
| **PyFES** | FES만 (공식) |
| **OTIS** (Fortran) | TPXO만 (공식) |
| **TMD** (MATLAB) | TPXO 위주 |
| **eo-tides** | pyTMD wrapper로 모두 |
| t_tide / UTide / pytides | 모델 데이터 직접 사용 안 함 — 시계열 분석 도구 |

## 7. 관련 도구 (참고)

| 도구 | 언어 | 비고 |
|---|---|---|
| OTPS / OTIS | Fortran | OSU TPXO 원조 도구. pyTMD가 Python 대안 |
| TMD (Tide Model Driver) | MATLAB | OSU. pyTMD의 MATLAB 전임자 |
| TAPPY | Python | Tidal Analysis Program in Python — 활성 낮음 |
| t_tide-modified | MATLAB | GOFUVI fork — 일부 한국 사용 케이스 ([https://github.com/GOFUVI/t_tide-modified](https://github.com/GOFUVI/t_tide-modified)) |
| eo-tides | Python | Geoscience Australia, satellite EO + pyTMD wrapper ([https://github.com/GeoscienceAustralia/eo-tides](https://github.com/GeoscienceAustralia/eo-tides)) |

## 8. 도구·모델 선택 가이드

### 8.1 분석 도구

| 상황 | 권장 |
|---|---|
| 1년 이내 단일 정점 분석, MATLAB 환경 | **t_tide** |
| irregular time / gap 있는 시계열 / 정밀 분석 | **UTide** (Python) |
| Python 환경 + NOAA 분조로 빠른 예측 | **pytides** (또는 UTide) |
| 위성 데이터에서 임의 위치 조석 보정 | **pyTMD** |
| 한국 서해 비선형 조석 (M₄·MS₄ 강함) | **UTide** + 천해 분조 명시 추가 |
| 한국 항만 설계 — 4대분조 기반 | **UTide** 또는 **t_tide** (조화상수 산출 후 [`02-theory.md` §8](02-theory.md) 비조화상수 공식 적용) |

### 8.2 전 지구 조석 모델

| 상황 | 권장 |
|---|---|
| EFDC/ADCIRC 외해 경계 forcing (한국 서해) | **FES2022** (1/30° 천해 강함) → KHOA tide gauge로 보정 |
| EFDC/ADCIRC 외해 경계 forcing (동해·일본해) | **NAO.99Jb** (regional 1/12°) |
| 위성고도계 (Sentinel-3/6, Jason 등) 조석 보정 | **GOT5** 또는 **FES2022** |
| 글로벌 대규모 ocean modeling | **TPXO10** (de facto 표준) |
| ICESat-2 등 NASA 미션 데이터 처리 | **pyTMD** + GOT/FES |
| 모델 간 비교·검증 | TPXO + FES + GOT 다중 비교 후 tide gauge 대조 |

> **핵심 원칙**: 모든 글로벌 조석 모델은 연안 sub-grid에서 한계 — **반드시 현지 tide gauge 검증** 후 사용. KHOA 조위 관측망 활용 필수.

## 9. 보강 필요

**도구**:
- 각 도구의 **라이선스** 표 (LICENSE 파일 직접 읽고 명시)
- Schureman (1958) Special Publication 98 — pytides의 알고리즘 1차 출처, 추가 인용 보강
- 한국 KHOA 자체 조석 분석 소프트웨어 (KOHA·KMA 내부 도구) 존재 여부 — 별도 조사

**모델**:
- **FES2014 paper 정식 인용**: Lyard, F. H., et al. (2021). FES2014 global ocean tides atlas. 별도 *Ocean Science* 게재 paper 인용 — 현재 preprint URL만 확인
- **EOT 정식 출처**: Savcenko, R., Bosch, W., 등 DGFI-TUM EOT11a/EOT20 논문 추가 검색
- **Egbert, Bennett, Foreman (1994)** — TPXO 알고리즘 원조 논문 정식 인용
- **GOT4.10 paper**: Ray, R. D. 등 GOT4.10 별도 publication
- 한국 서해·남해·동해에서 **각 모델 정확도 비교 사례** — 학술 논문 검색
- KHOA 자체 조석 예측 시스템·자료 — 별도 조사

**적용 사례**:
- 실제 한국 연안 적용 사례 (서해 인천·서산, 남해 부산, 동해) — `05-examples.md` 또는 `06-model-application.md`

## 10. 연결

- `02-theory.md` — 분조 이론·평형 진폭 (Stewart Table 17.2와 본 도구들의 입력 분조 set 정합)
- `03-analysis-methods.md` — 조화분해 알고리즘 (본 도구들이 구현)
- `05-examples.md` (미작성) — 실제 사용 예제 + 코드
- `06-model-application.md` (미작성) — EFDC/ADCIRC tidal forcing 생성에 이들 도구 활용
- 소스 노트:
  - [`textbook/notes/tides-foreman1977-appendix.md`](../../textbook/notes/tides-foreman1977-appendix.md) — t_tide·UTide의 algorithmic ancestor
  - [`textbook/notes/tides-stewart-ch17.md`](../../textbook/notes/tides-stewart-ch17.md) — Stewart §17.5 Response method (UTide IRLS와 별개 방법론)
- 외부 인용 (분석 도구):
  - **Pawlowicz et al. (2002)** — t_tide paper, *Computers & Geosciences* 28:929-937
  - **Codiga (2011)** — UTide technical report, URI GSO 2011-01
  - **Sutterley et al. (2025)** — pyTMD paper, *JOSS* joss.08566
  - **Schureman (1958)** — Special Publication No. 98, U.S. Coast and Geodetic Survey (pytides 출처)
  - **Doodson & Lamb (1921)** — Astronomical argument formalism (pyTMD 출처)
- 외부 인용 (전 지구 조석 모델):
  - **Egbert & Erofeeva (2002)** — *J. Atmos. Ocean. Technol.* 19:183-204 — TPXO 알고리즘
  - **Egbert, Bennett, Foreman (1994)** — TPXO inverse method 원조 (보강 인용)
  - **Lyard et al. (2021)** — FES2014 (preprint, 정식 게재 보강)
  - **Matsumoto, Takanezawa, Ooe (2000)** — *J. Oceanogr.* 56:567-581 — NAO 모델 doi:10.1023/A:1011157212596
  - **Ray, R. D. (2025)** — GOT5 NASA Technical Memorandum NASA/TM-20250002085
