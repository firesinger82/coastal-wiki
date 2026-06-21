---
title: "조류 — 03 분석 방법 (UTide 2D·ADCP·KHOA protocol)"
topic: currents
canonical_source: self
citation_status: verified
has_source_needed: false
verification_method: "AI cross-reference: KHOA glossary (조류관측·라그랑주식해류측정·오일러식해류측정 등) + UTide _solve.py 2D mode 변수 + Foreman 1977 algorithm 매핑 (조위와 동일)."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-21
verification_by: "Claude Opus 4.7 (1M context) — cross-ref"
verification_date: 2026-05-21
---

# 조류 — 03 분석 방법

## 1. 조류관측 — KHOA protocol

> **조류관측 (*tidal current observation*)**: 조석에 의한 해수의 주기적 수평흐름인 조류의 유향·유속을 연속하여 관측. **수심 3~10 m 층**에서 관측 (파랑 영향 제외). 필요에 따라 층별 관측도. ([KHOA] 조류관측)

### 1.1 관측 기간

| 기간 | 분조 분리 가능 범위 |
|---|---|
| **1주야 (25시간)** | M₂·창낙조류 1주기. 분조 분리 거의 불가 |
| **15주야** | M₂·S₂ 분리 가능 (Rayleigh 14.77일 ≈ 충족) — 대조·소조 포함 |
| **30주야** | 4대분조 정밀, K₁·O₁ 분리 마진 |
| **6개월** | 다수 분조 분리, satellite·nodal 일부 |

> Rayleigh criterion 상세는 [`concepts/tides/03-analysis-methods.md` §1.5](../tides/03-analysis-methods.md).

### 1.2 관측 장비 (KHOA 사용)

| 장비 | 종류 | 비고 |
|---|---|---|
| 기계식 유속계 | 프로펠러식 | 초기 표준, 단층 |
| **ADCP** | Acoustic Doppler Current Profiler | 음파 도플러, **층별 동시 측정** |
| RCM-9 | 음파 유속계 | KHOA 사용 |
| RDCP-600 | 음파 유속계 | KHOA 사용 |
| **HF-Radar** | High Frequency Radar 해수유동관측소 | **광역 표층 흐름** 관측 (km 단위 격자). KHOA Annual Report 2025 `khoa-annual-reports` §1.4에 정점 list |

### 1.3 KHOA 연간백서 공식 분석 절차 (조류조화분해·창낙조·항류)

KHOA 국가해양관측망 연간백서의 해수유동 분석은 §3의 UTide 기반 일반 절차와 별개로 **공식 표준 절차**를 따른다 (출처: `khoa-annual-reports`, Annual Report 2025 제3장 §1(5)·(1)).

- **조류조화분해 SW — TASK-2000**: 영국 Proudman 해양연구소(POL/PSMSL) P.L. Woodworth 등이 개발한 TASK-2000(Tidal Analysis Software Kit 2000)으로 정점별 주요 4대분조(M₂·S₂·K₁·O₁)의 조류타원 요소·조류조화상수를 산출 (Annual Report 2025 L2487). 조위 조화분해와 동일 SW.
  - **지각 g 기준**: 조류조화분해로 산출한 지각(g)은 **한국표준시(KST) 기준자오선 = 동경 135°** 기준 (Annual Report 2025 L2491; 조위도 동일, L2420). → `05-examples.md` 수치조류도 위상 기준 해소.
  - **SW 연혁**: 2018년 백서까지는 캐나다 M.G.G. Foreman(1977)이 개발한 **IOS Package(2004)**를 사용했으나(Year_report 2018 L1499–1501), 2025년 백서는 조위·조류 모두 TASK-2000으로 통일.
- **창·낙조 구분 — 주성분분석(PCA)**: 주성분 분석(Principal Component Analysis)으로 창조·낙조를 구분하고, 각 조시별 가장 빠른 유속을 최강 창·낙조류로, 동일시각의 유향을 최강유향으로 선정 (Annual Report 2025 L2483).
  - 단, **해류가 조류보다 강한 동해안 관측소**(해양관측부이 7개소: 울릉도북서·북동·고래불·망상·경포대·낙산·속초 / 해수유동관측소 3개 해역: 울산항·포항항·동해남부)는 조시 구분 없이 **최강류만** 제시하고, 주유향도 빈도 최다 방향으로만 제시 (L2483–2491).
  - **변형**: 2018 백서는 PCA 미사용 — 인근 조위관측소 조위 시계열을 참조해 대조시 최강 창·낙조류를 제시(Year_report 2018 L1495). PCA 도입은 방법론 갱신.
- **항류(Permanent Current)·평균류**: 항류는 관측기간 중 흐름의 평균치로 조류조화분해를 통해 산출. 평균류는 동방성분(U)·북방성분(V)의 평균으로 합성한 유속·유향 (Annual Report 2025 L2493–2495).
- **HF-Radar 합성**: 해수유동관측소 표층 자료는 각 관측영역 정점(Radial site)의 단일벡터(Radial vector)를 합성한 **Total vector 1시간 자료**를 분석하며, 해역별 대표정점(9개)에 대해 수행 (L2481). 원리는 특정 주파수 전파의 **도플러 효과**로 광역 표층 유향·유속을 관측 (Annual Report 2025 제1장, L1722–1726).

> **UTide(§3) vs TASK-2000(KHOA 공식)**: 둘 다 Foreman 1977 계열 최소자승 조화분해. UTide는 본 위키의 재현·분석 도구, TASK-2000은 KHOA 연간백서 공식 산출 SW. 분조·조류타원 요소는 호환되나, 창낙조 구분(PCA)·항류 정의는 KHOA 공식 절차 고유.

## 2. 두 관측 방식 (KHOA glossary)

| 방식 | 한국어 | 영문 | 정의 |
|---|---|---|---|
| **Lagrangian** | 라그랑주식해류측정 | Lagrangian current measurement | 부유체(부표 등)를 따라가며 측정 |
| **Eulerian** | 오일러식해류측정 | Eulerian current measurement | 고정 지점에서 시간 따라 측정 (ADCP·정박 유속계 표준) |

조류 분석의 대부분은 Eulerian. Lagrangian은 표층 유적·확산 연구에 활용.

## 3. UTide 2D 모드 — 조화분해

조위의 1D 분석 ([`concepts/tides/03-analysis-methods.md` §1.3](../tides/03-analysis-methods.md))을 2D 벡터로 확장.

### 3.1 입력

```python
from utide import solve

coef = solve(
    t,                      # 시각 array (datetime64 또는 days since epoch)
    time_series_u,          # 동-서 성분 (m/s, cm/s, knots 등 일관)
    time_series_v,          # 북-남 성분
    lat=37.5,               # 위도
    nodal=True,
    trend=True,
    method="ols",           # 또는 'robust' (IRLS, 천해 강함)
    conf_int="linear",
    Rayleigh_min=1.0,
)
```

(`khoa-tide-model` skill.md 인용 + UTide README sample 확장)

### 3.2 출력 (utide/_solve.py 2D mode)

```python
coef["name"]    # 분조 이름 array
coef["Lsmaj"]   # 반장축 (semi-major) array
coef["Lsmin"]   # 반단축 (semi-minor) — 부호 = 회전 방향
coef["theta"]   # 장축 inclination ° (0-180, 동쪽 기준 CCW)
coef["g"]       # phase ° (Greenwich 기준, lat·nodal 보정 적용)
coef["umean"]   # u 평균
coef["vmean"]   # v 평균
coef["uslope"]  # u trend (trend=True 시)
coef["vslope"]  # v trend
```

(utide/_solve.py `solve()` returns block 직접 인용)

### 3.3 분조별 (Lsmaj, Lsmin, θ, g) 사용

각 분조의 4개 parameter로 [`02-theory.md` §3](02-theory.md) 조류타원 완전 표현. 시간 t에서 조류 벡터 재구성:

```
u(t) = Σ_n [Lsmaj_n cos(σ_n t - g_n) cos(θ_n) - Lsmin_n sin(σ_n t - g_n) sin(θ_n)]
v(t) = Σ_n [Lsmaj_n cos(σ_n t - g_n) sin(θ_n) + Lsmin_n sin(σ_n t - g_n) cos(θ_n)]
```

UTide `reconstruct(t_pred, coef)` 함수가 위 합성을 자동 처리.

## 4. 회전 분해 (Rotary Decomposition) — 보조 방법

조류 벡터를 두 회전 성분으로 분해:
- W⁺ (CCW 회전) — 진폭, 위상
- W⁻ (CW 회전) — 진폭, 위상

관계 (Lsmaj/Lsmin과 매핑):
```
Lsmaj = |W⁺| + |W⁻|
Lsmin = |W⁺| - |W⁻|   (부호 따라 CCW/CW)
```

→ 회전 성분이 직관적 (회전 방향 부호 명확) — `04-code-and-tools.md` §2 UTide 회전 분해 옵션.

## 5. 천해 비선형 분조 (서해 적용)

[`concepts/tides/03-analysis-methods.md` §3](../tides/03-analysis-methods.md) 천해 분조 발생 원리와 동일. 조류에서는 **창·낙조류 비대칭** 명시화:

- M₂ 단독 → 대칭적 sinusoidal 진동
- M₂ + M₄ → 비대칭 (한쪽 더 가파르거나 강함)
- MS₄: M₂·S₂ 상호작용
- M₆: M₂의 3차 고조파

UTide는 `constit='auto'`로 시계열 길이에 맞게 자동 선택. 천해 케이스는 분조 list 명시 권장:

```python
coef = solve(
    t, u, v, lat=37.5,
    constit=['M2','S2','K1','O1','N2','K2','M4','MS4','M6'],
    method='robust',                    # 천해 비선형엔 robust 유리
    Rayleigh_min=0.95,
)
```

## 6. 검증 방법

UTide 결과 vs 다른 source 비교:

| 비교 대상 | 정합 기준 |
|---|---|
| 인근 KHOA 정점 분조 | M₂ 진폭 ±10% 이내 (지형 차이 고려) |
| 수치조류도 격자 (`khoa-tide-model`) | 같은 위치에서 ±20% 이내 (모델 격자 해상도 한계) |
| ADCP 동일 정점 다른 기간 | 같은 위치 ±5% (계절 변동 ε) |
| 시간 영역 재구성 vs 원본 시계열 | RMS 잔차 < 분조 외 잡음 진폭 |

## 7. KHOA 조류관측 자료 활용 흐름

1. **관측**: ADCP 1~30주야 (목적별)
2. **품질관리 (QC)**: spike·결측 제거, 보간 (UTide는 NaN 허용)
3. **조화분해**: UTide 2D, lat 입력
4. **조류타원 산출**: (Lsmaj, Lsmin, θ, g) per 분조
5. **검증**: 인근 정점·수치조류도와 비교
6. **예측**: `reconstruct()` 임의 시간 array
7. **시각화**: 조류 벡터 hodograph, 조류 곡선, 등조류선

## 8. 보강·미해결

- KHOA OpenAPI에서 조류 관측 직접 다운로드 endpoint — `04-code-and-tools.md` §3에서 명시
- ADCP 다층 데이터의 수직 평균 vs 층별 분석 best practice
- 명량·진도해협 등 강조류 해역 특이 사례
- Foreman 1977 본문 OCR 후 nodal correction 정밀화 (조류도 동일 적용)

## 9. 연결

- `01-concept.md` — 관측 방식·분류
- `02-theory.md` — 조류타원·분조 이론
- `04-code-and-tools.md` — UTide 2D 사용·수치조류도 격자
- `05-examples.md` — 수치조류도 정점 추출 예제
- `concepts/tides/03-analysis-methods.md` — 동일 조화분해 알고리즘 (1D 조위)
- 외부 인용:
  - UTide 2D `coef[]` 구조: utide/_solve.py
  - [KHOA] 조류관측·라그랑주식·오일러식해류측정
