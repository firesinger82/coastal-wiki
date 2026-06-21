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
