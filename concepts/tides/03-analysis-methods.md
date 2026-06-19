---
title: "조석 — 03 분석 방법 (조화분해·예측)"
topic: tides
canonical_source: self
citation_status: verified
verification_method: "AI programmatic cross-reference. Stewart §17.5 (textbook/md/stewart_textbook.md p.321-326) + Foreman 1977 appendix (textbook/md/Manual_for_Tidal_Heights_Analysis_and_Pr.md p.48-66) + KHOA/PORTCALS glossary. Foreman 본문(p.1-47)은 스캔 PDF로 미추출 — 본 문서의 알고리즘 구현 상세는 Stewart 인용으로 한정, 추가 상세는 [tides-foreman1977-appendix.md](../../textbook/notes/tides-foreman1977-appendix.md)의 보강 작업 후 갱신."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-21
verification_by: "Claude Opus 4.7 (1M context) — cross-ref"
verification_date: 2026-05-21
---

# 조석 — 03 분석 방법

조석 시계열에서 분조 진폭·지각을 추출하고 임의 시점의 조위를 예측하는 방법.

## 1. 조화분해 (Harmonic Analysis)

> **정의 (한국)**: 조석 관측 자료를 토대로 조석을 **다수의 규칙적인 조석 성분으로 분리**하고, 각 성분의 **진폭·지각**을 구하는 것. 개개 성분은 분조(分潮), 각 분조의 진폭(반조차)과 지각이 **조화상수**. 그 지점의 조석 특성 분석과 예측에 사용. ([KHOA] 조화분해)
>
> [PORTCALS]: "관측된 조석 데이터로부터 조석을 구성하는 다수의 성분(분조)을 수학 계산을 이용하여 분해하고 그들의 조화상수를 구하는 것." 조석·조류 장기 관측 자료를 조화분해하여 각 분조의 조화상수를 구하면 **그 지역에서 임의 시간의 조석·조류 예측 가능**. ([PORTCALS] 조화분해)

영문: *harmonic analysis*, *harmonic analysis of tides*.

### 1.1 기본 모델

조위 시계열 η(t)를 분조의 정현파 합으로 분해 (Stewart §17.5, p.321-322 — Harmonic Method 설명을 따름):

```
η(t) = Z₀ + Σ_n H_n cos(σ_n t - g_n)
```

여기서:
- Z₀ = 평균 해면 (mean sea level, datum 위)
- H_n = n번째 분조 진폭 (m)
- σ_n = n번째 분조 각주파수 (rad/h 또는 °/h)
- g_n = n번째 분조 지각 (phase lag, °)
- (H_n, g_n) 쌍 = **조화상수** ([KHOA] 분조)

분조 주파수 σ_n은 사전 지정 — Stewart Table 17.1의 6개 기본 주파수의 정수 조합으로 결정 (Doodson 1922 expansion).

### 1.2 분조 선택

Stewart Table 17.2 (p.319-320)는 평형조석 기준 11개 주요 분조 — 실무에서는 더 많음:

- **Foreman 1977 매뉴얼**: 146개 분조 다룸 (`textbook/notes/tides-foreman1977-appendix.md` 참조)
- **KHOA 권고**: 조석 특성 분석에 사용하는 분조는 약 64개 ([KHOA] 분조)
- **주요 4대분조**: M₂, S₂, K₁, O₁만으로도 한국 연안의 약최저저조위 산정 가능 ([PORTCALS] 약최저저조위, `02-theory.md` §8)

### 1.3 알고리즘 (개관)

> Foreman 1977 본문(p.1-47)이 알고리즘의 canonical 출처이나 현재 추출본은 스캔 미해독 상태. 본 §1.3은 Stewart §17.5 + 통용 지식 기반 개관. 정밀 알고리즘 상세는 Foreman OCR 후 보강 예정.

**최소자승 적합 (least-squares fit)** — 주된 접근:

관측 η_obs(t_k) (k = 1...N) 에 대해 잔차 제곱합을 최소화:

```
χ² = Σ_k [η_obs(t_k) - Z₀ - Σ_n H_n cos(σ_n t_k - g_n)]²
```

각 분조의 (H_n cos g_n, H_n sin g_n)을 미지수로 두면 σ_n이 고정이므로 **선형 최소자승** 문제 → 정규방정식으로 직접 해 (구현은 t_tide·UTide의 핵심).

각 분조에 대해:
- H_n = √(a_n² + b_n²), where (a_n, b_n) = (H_n cos g_n, H_n sin g_n)
- g_n = atan2(b_n, a_n)

### 1.4 시계열 길이 요건

> Stewart p.321: "More than 18.6 years of data are needed to resolve the modulation of the lunar tides."

- **18.6년**: 달의 nodal cycle (lunar nodal regression). 이 보다 짧으면 K₁·K₂의 진폭이 nodal 변동에 흔들림
- **19년**: 실무 권고 (KHOA 등) — 18.6년 nodal + 안전 margin
- **메톤주기 19년**: 태양-달 위상이 거의 완전히 일주 ([KHOA] 메톤주기, `02-theory.md` §3.4)

짧은 시계열의 경우:
- **1년**: 주요 일주·반일주 분조 (M₂, S₂, K₁, O₁) 분해 가능, 단 satellite·nodal correction 필요
- **29일**: 최소 — 일주·반일주 핵심만 분리 가능, 약한 분조는 결정 불가
- **2주 미만**: 분리 불가, 평균 조차·고저조 통계만 의미 있음

### 1.5 Rayleigh Criterion

두 분조 σ_n, σ_m을 분리하려면 시계열 길이 T가 만족:

```
T ≥ 1 / |σ_n - σ_m|        (Rayleigh criterion)
```

예: M₂ (12.4206 h) vs S₂ (12.0000 h) → Δf = 0.00284 cph, T_min = 14.77 일.
예: K₁ (23.9344 h) vs K₂ (11.9673 h) → 서로 다른 species라 분리 자명.
예: K₂ (11.9673 h) vs S₂ (12.0000 h) → Δf = 0.000229 cph, T_min ≈ 6 개월.

> 이 식의 Foreman 1977 원본 인용은 OCR 보강 후 추가. 현재는 일반 신호처리 결과로 표시.

### 1.6 Nodal Correction

달의 nodal cycle (18.613년) 동안 각 분조의 진폭이 변동. 18.6년 미만 분석 시 nodal factor f_n과 nodal phase u_n으로 보정:

```
η(t) = Z₀ + Σ_n f_n(t) H_n cos(σ_n t + (V_n + u_n(t)) - g_n)
```

V_n, u_n은 Doodson-Cartwright 결과 — Foreman appendix (p.59-62)에 satellite constituent 데이터로 제공. 실무는 보통 1년 단위 cohort로 묶어 분석 (cohort마다 f, u 적용).

> 상세 수식·테이블은 Foreman 1977 본문 OCR 후 추가.

## 2. 응답 방법 (Response Method)

(Stewart §17.5 p.322 — Munk & Cartwright 1966)

> Response method: 관측 조석과 **기조 위치 에너지(tide-generating potential)** 간 spectral admittance를 계산.

### 2.1 핵심 아이디어

조위는 천체에서 유도된 위치 에너지 V(t)에 대한 시스템 응답:

```
η(f) = Z(f) · V(f)
```

여기서:
- η(f) = 관측 조위 푸리에 변환
- V(f) = 기조 위치 에너지 푸리에 변환 (천체 운동에서 계산 가능, `02-theory.md` §1.1 eq. 17.9)
- Z(f) = G(f) / H(f) = spectral admittance (Stewart p.322)

미래 조위는 V(f) × Z(f) 역변환.

### 2.2 장점 (Stewart p.322 인용)

- 수개월 데이터만으로 가능 (Harmonic method의 18.6년 대비 짧음)
- 기조 위치 에너지는 천체 위치만으로 즉시 계산 — 분조 주파수 사전 지정 불필요
- admittance Z(f)는 천천히 변하는 함수로 가정 → 약한 분조는 인접 분조의 admittance로 보간

### 2.3 한계 (Stewart p.322)

- **선형파 가정** — 천해·하구 비선형 조석에서 한계
- 진폭 변조 모델링 부족
- 한국 연안 (서해 비선형 조석)에서 harmonic method가 더 일반적

## 3. 천해 비선형 조석

(Stewart p.321-322)

천해에서 조석은 비선형 — 큰 분조의 고조파가 생성:
- M₄ = 2 × M₂
- M₆ = 3 × M₂
- MS₄, MN₄, MK₃ 등 cross-term

극단 케이스: **tidal bore** (조석 단파). 강 하구에서 입사파의 leading edge가 거의 수직으로 가팔라지고 solitary wave로 전파.

Foreman 1977 appendix는 천해 비선형 분조 (M3, M4, MK3, MN4, M6, M8, M10, M12 등)를 다수 포함 — 한국 서해 분석에 필요.

> 한국 서해의 비선형 조석 분석 사례·매뉴얼은 KHOA 별도 자료 필요. 보강 항목.

## 4. 비조화 상수 산출

> **정의 (한국)**: 조위 관측 자료를 조화분해하여 산출한 조화상수로부터 **일정 공식**에 따라 계산한 조석 상수. 항만 설계에 사용하는 조석 제원 (조차·조위·조시 간격 등). ([PORTCALS] 비조화상수)

### 4.1 한국 공식 — 국립해양조사원고시 제2021-7호 (검증된 공식 전체)

상세 유도·부산항 검증은 [tides-khoa-nonharmonic-research.md](../../textbook/notes/tides-khoa-nonharmonic-research.md) (`khoa-notice-2021-7` source·국립해양조사원고시 제2021-7호). 결과 공식 요약:

```
Z₀         = H_M2 + H_S2 + H_K1 + H_O1     # 4대분조 반조차합

MSL        = DL + Z₀ = Z₀  (DL 기준)
HHWL       = MSL + Z₀ = 2·Z₀  (DL 기준)
DL (A.L.L.W) = 0  (해도 datum 기준점)

대조승      = 2·H_M2 + 2·H_S2 + H_K1 + H_O1   = Z₀ + H_M2 + H_S2
소조승      = 2·H_M2 + H_K1 + H_O1            = Z₀ + H_M2 - H_S2
평균조차    = 2·H_M2
대조차      = 2·(H_M2 + H_S2)
소조차      = 2·(H_M2 - H_S2)

HWI(g)     = g_M2 / 28.984104156  (KST 135°E 지각, 시간)
HWI(κ)     = κ_M2 / 28.984104156  (local 경도 지각, 시간)

F (Form)   = (H_K1 + H_O1) / (H_M2 + H_S2)
```

> **"조승" vs "조차" 혼동 금지**:
> - 조승 = DL 기준 **높이** (m above DL)
> - 조차 = 고저조 **차이** (m, range)
> KHOA "대조승" 공시값은 DL 기준 높이임 (range 아님).

> **분 계산**: KHOA는 HWI 분 계산 시 **floor (내림)** 적용으로 관측됨 — 0~1분 오차 가능.

### 4.2 주요 비조화 상수 — KHOA 표기 ([KHOA] 비조화상수)

조화상수 → 비조화상수 변환으로 얻는 항만 설계 제원:

- 약최고고조위 (A.H.H.W) = HHWL = 2·Z₀
- 대조 평균 고조위 (HWOST) = 대조승
- 평균 고조위 (MHW)
- 소조 평균 고조위 = 소조승
- **평균 해면 (MSL)** = Z₀ (DL 기준)
- 소조 평균 저조위
- 평균 저조위 (MLW)
- 대조 평균 저조위
- **약최저저조위 (A.L.L.W) = DL** — 한국 해도 datum

### 4.3 부산항 검증 (대시보드 연구 §3, KHOA 부산항 조석표 공시값)

> **출처 명시**: H_M2=40 cm는 **KHOA 부산항 조석표 공시값** (단일 정점, 정확 obs_code 미확인). DT_0005 (부산, 38.23 cm), 다대포항/가덕도 등 sub-stations와는 정점 정의 차이 — `tides-khoa-cross-verification.md` §4 참조.

조화상수: H_M2=40.0 cm, H_S2=18.9 cm, H_K1=4.4 cm, H_O1=1.6 cm, g_M2=235.6°, κ_M2=232.8°.

공식 적용 → 동일 출처 (KHOA 부산항 조석표) 비조화 공시값과 **모두 일치** (HWI(κ)만 floor 반올림 차이 0.86분):
- Z₀ = 64.9 cm, MSL = 64.9, 약최고고조면 = 129.8
- 대조승 = 123.8, 소조승 = 86.0, 대조차 = 117.8, 소조차 = 42.2
- HWI(g) = 8h 07m, HWI(κ) = 8h 01m (KHOA 8h 02m)
- F = 0.102 → 반일주조형

상세 표는 [tides-khoa-nonharmonic-research.md](../../textbook/notes/tides-khoa-nonharmonic-research.md) §4.

### 4.4 KHOA OpenAPI

| API | 엔드포인트 |
|---|---|
| 조화상수 | `/api/oceangrid/tideObsHarmo/search.do` |
| 실측조위 | `/api/oceangrid/tideObsReal/search.do` |
| 예측조위 | `/api/oceangrid/tideObsPre/search.do` |
| 조석예보 | `/api/oceangrid/tideObsPreTab/search.do` |

**중요**: KHOA OpenAPI는 **조화상수만 제공**. **비조화상수는 §4.1 공식으로 계산 필요**.

API 키 체계: `khoa.go.kr` (바다누리 전용) vs `data.go.kr` (공공데이터포털) — 두 키는 비호환.

### 4.5 KHOA 표준 — 62개 조화상수

KHOA 각 정점은 **62개 조화상수**를 표준으로 산출 (Annual Report 2025 `<표 3-31>` 등 인용, `khoa-annual-reports`). 주요 4대분조 (M₂·S₂·K₁·O₁) + 다양한 satellite·천해 비선형 분조 포함. Foreman 1977 appendix의 146개 분조 ([tides-foreman1977-appendix.md](../../textbook/notes/tides-foreman1977-appendix.md))의 부분집합.

## 5. 분석 출력

조화분해 결과 일반 형식:

| 분조 | 진폭 H (m) | 지각 g (°) | 표준 오차 |
|---|---|---|---|
| Z₀ | mean | — | — |
| M₂ | ... | ... | ± |
| S₂ | ... | ... | ± |
| ... | | | |

**Foreman 1977 출력 예제** (p.55, Tuktoyaktuk NWT 1976):

```
6 1.0 0.0
K1 0.0417807462 P1 0.0415525871 0.33093 -7.07
S2 0.0833333333 K2 0.0835614924 0.27215 -22.40
```

- K1 진폭 0.33093 m, 지각 -7.07°
- S2 진폭 0.27215 m, 지각 -22.40°
- 인접 컬럼 P1·K2: satellite 분조 (위상 lock)

## 6. 소프트웨어 구현 (개관)

> 상세 사용법·설치는 `04-code-and-tools.md` (작성 예정). 본 §은 알고리즘 매핑만.

| 도구 | 언어 | 알고리즘 |
|---|---|---|
| t_tide | MATLAB | Foreman 1977 직접 이식 (Pawlowicz, Beardsley, Lentz 2002) |
| UTide | Python/MATLAB | t_tide 확장, IRLS robust fitting (Codiga 2011) |
| pytides | Python | Doodson-Cartwright 분조 기반 |
| pyTMD | Python | 위성고도계 기반 전 지구 모델 (GOT, FES, TPXO) |

> 위 4 도구의 정식 인용은 04-code-and-tools.md 작성 시 공식 GitHub repo·논문 추가 인용 후 verify.

## 7. KHOA 한국 용어 정리

| 용어 | 한자 | 영문 | 정의 ([KHOA]/[PORTCALS]) |
|---|---|---|---|
| 조화분해 | 調和分解 | harmonic analysis | 분조 분리 + 진폭·지각 계산 |
| 분조 | 分潮 | tidal constituent | 조석을 구성하는 개개 성분 |
| 조화상수 | 調和常數 | harmonic constants | 분조의 (진폭, 지각) 쌍 |
| 비조화상수 | 非調和常數 | non-harmonic tidal constant | 조화상수에서 공식으로 산출한 조석 제원 |
| 평균해면 | — | mean sea level (MSL) | 1년 이상 장기 평균 해수면 ([PORTCALS] 평균해면) |
| 산술평균해면 | — | A0 | 임의 기준면에서 천문조+기상조 포함 장기 평균 ([KHOA] 산술평균해면) |
| 기본수준면 | 基本水準面 | datum level (DL) / A.L.L.W | 한국 해도 datum, 약최저저조위 ([KHOA] 기본수준면) |

## 8. 보강 필요·미해결

- Foreman 1977 본문 (p.1-47) — OCR 후 알고리즘 상세, Rayleigh criterion 유도, nodal correction 수식 전체
- KHOA 비조화상수 산출 공식 전체 (MHWI 외)
- Pawlowicz et al. (2002) t_tide 논문 인용 (UTide·t_tide 알고리즘 보강)
- Codiga (2011) UTide technical report
- 한국 서해 비선형 조석 분석 사례 (M4·MS4 진폭 분포)
- Response method 실제 사용 사례 (Munk & Cartwright 1966 후 발전)

## 9. 연결

- `01-concept.md` — 정의·용어 개관 (verified)
- `02-theory.md` — 기조력·평형조석·분조 이론 (verified)
- `04-code-and-tools.md` (미작성) — t_tide / UTide / pytides 사용법
- `06-model-application.md` (미작성) — EFDC `tidal_open_boundary.inp` 등에서 조화상수 forcing
- 소스 노트:
  - [`textbook/notes/tides-stewart-ch17.md`](../../textbook/notes/tides-stewart-ch17.md) — Stewart §17.4-17.5 (verified)
  - [`textbook/notes/tides-foreman1977-appendix.md`](../../textbook/notes/tides-foreman1977-appendix.md) — Foreman appendix (verified, 본문 OCR 보강 대기)
- 외부 인용 라이브러리:
  - Foreman, M.G.G. (1977). Pacific Marine Science Report 77-10. — 본 토픽의 algorithmic canonical
  - Munk, W., & Cartwright, D. E. (1966). Response method (Stewart §17.5 인용)
  - Doodson, A. T. (1922). 분조 주파수 전개 (Stewart §17.4)
  - Pawlowicz, R., Beardsley, B., & Lentz, S. (2002). t_tide. *Computers & Geosciences*. — 04에서 정식 인용
  - Codiga, D. L. (2011). UTide. — 04에서 정식 인용
