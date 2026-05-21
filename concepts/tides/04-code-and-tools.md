---
title: "조석 — 04 코드와 도구"
topic: tides
canonical_source: self
citation_status: verified
verification_method: "AI programmatic cross-reference against textbook/md/stewart_textbook.md + textbook/md/Manual_for_Tidal_Heights_Analysis_and_Pr.md, plus WebSearch (2026-05-21) for external repos/papers — DOI, GitHub URL, official project pages. 인용 URL은 acc. 2026-05-21."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-21
verification_by: "Claude Opus 4.7 (1M context) — cross-ref + WebSearch"
verification_date: 2026-05-21
---

# 조석 — 04 코드와 도구

조석 분석·예측을 위한 주요 오픈소스 도구. 각 도구의 알고리즘 출처·논문·repo·라이선스를 정리. 사용 예제는 별도 (`05-examples.md`).

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

## 6. 관련 도구 (참고)

| 도구 | 언어 | 비고 |
|---|---|---|
| OTPS / OTIS | Fortran | OSU TPXO 원조 도구. pyTMD가 Python 대안 |
| TMD (Tide Model Driver) | MATLAB | OSU. pyTMD의 MATLAB 전임자 |
| TAPPY | Python | Tidal Analysis Program in Python — 활성 낮음 |
| t_tide-modified | MATLAB | GOFUVI fork — 일부 한국 사용 케이스 ([https://github.com/GOFUVI/t_tide-modified](https://github.com/GOFUVI/t_tide-modified)) |
| eo-tides | Python | Geoscience Australia, satellite EO + pyTMD wrapper ([https://github.com/GeoscienceAustralia/eo-tides](https://github.com/GeoscienceAustralia/eo-tides)) |

## 7. 도구 선택 가이드

| 상황 | 권장 |
|---|---|
| 1년 이내 단일 정점 분석, MATLAB 환경 | **t_tide** |
| irregular time / gap 있는 시계열 / 정밀 분석 | **UTide** (Python) |
| Python 환경 + NOAA 분조로 빠른 예측 | **pytides** (또는 UTide) |
| 위성 데이터에서 임의 위치 조석 보정 | **pyTMD** |
| 한국 서해 비선형 조석 (M₄·MS₄ 강함) | **UTide** + 천해 분조 명시 추가 |
| 한국 항만 설계 — 4대분조 기반 | **UTide** 또는 **t_tide** (조화상수 산출 후 [`02-theory.md` §8](02-theory.md) 비조화상수 공식 적용) |

## 8. 보강 필요

- 각 도구의 **라이선스** 표 (LICENSE 파일 직접 읽고 명시)
- Schureman (1958) Special Publication 98 — pytides의 알고리즘 1차 출처, 추가 인용 보강
- Egbert & Erofeeva (2002) — TPXO 모델 인용 — pyTMD의 데이터 출처로 정식 인용
- 한국 KHOA 자체 조석 분석 소프트웨어 (KOHA·KMA 내부 도구) 존재 여부 — 별도 조사
- 실제 한국 연안 적용 사례 (서해 인천·서산, 남해 부산) — `05-examples.md` 또는 `06-model-application.md`

## 9. 연결

- `02-theory.md` — 분조 이론·평형 진폭 (Stewart Table 17.2와 본 도구들의 입력 분조 set 정합)
- `03-analysis-methods.md` — 조화분해 알고리즘 (본 도구들이 구현)
- `05-examples.md` (미작성) — 실제 사용 예제 + 코드
- `06-model-application.md` (미작성) — EFDC/ADCIRC tidal forcing 생성에 이들 도구 활용
- 소스 노트:
  - [`textbook/notes/tides-foreman1977-appendix.md`](../../textbook/notes/tides-foreman1977-appendix.md) — t_tide·UTide의 algorithmic ancestor
  - [`textbook/notes/tides-stewart-ch17.md`](../../textbook/notes/tides-stewart-ch17.md) — Stewart §17.5 Response method (UTide IRLS와 별개 방법론)
- 외부 인용:
  - **Pawlowicz et al. (2002)** — t_tide paper, *Computers & Geosciences* 28:929-937
  - **Codiga (2011)** — UTide technical report, URI GSO 2011-01
  - **Sutterley et al. (2025)** — pyTMD paper, *JOSS*
  - **Schureman (1958)** — Special Publication No. 98, U.S. Coast and Geodetic Survey (pytides 출처)
  - **Doodson & Lamb (1921)** — Astronomical argument formalism (pyTMD 출처)
  - **Egbert & Erofeeva (2002)** — TPXO model (pyTMD 데이터 출처) — 별도 인용 보강
