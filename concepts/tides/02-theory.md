---
title: "조석 — 02 일반론 (기조력·평형조석·조화상수)"
topic: tides
canonical_source: self
citation_status: verified
verification_method: "AI programmatic cross-reference against textbook/md/stewart_textbook.md (Stewart §17.4-17.5, pp.314-326) + khoa-portcals-glossary ([KHOA], [PORTCALS] 용어집). 페이지 번호 정정 적용 후 verified."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-21
verification_by: "Claude Opus 4.7 (1M context) — cross-ref"
verification_date: 2026-05-21
---

# 조석 — 02 일반론

## 1. 기조력 (Tide-Generating Force)

> **정의 (한국)**: 조석 현상을 일으키는 힘. 지구와 천체(주로 달·태양) 간의 만유인력과 공전으로 발생하는 원심력이 합쳐져서 생긴다. 크기는 천체의 질량에 비례하고, 지구와 천체 간 거리의 **세제곱에 반비례**한다. 태양은 달보다 질량이 크지만 거리가 멀어 태양 효과는 달보다 작다. ([KHOA] 기조력, [PORTCALS] 기조력)

영문 표기: *tide-generating force* (또는 *tide-producing force*).

### 1.1 기조 위치 에너지 (Tide-Generating Potential)

Stewart (2008)와 Pugh (1987)의 유도를 따른다 (stewart-physical-ocean, p.315-316).

좌표계 (Stewart figure 17.10):
- O = 지구 중심
- P = 지구 표면의 점 (관측점)
- A = 천체 (달 또는 태양) 위치
- r = OP (지구 반지름)
- R = OA (지구-천체 거리)
- ϕ = ∠POA
- r₁ = PA (관측점-천체 거리)

천체 M이 점 P에 미치는 중력 위치 에너지:

```
V_M = -γM / r₁        (Stewart eq. 17.5)
```

여기서 γ는 만유인력 상수, M은 천체 질량.

삼각형 OPA에서:

```
r₁² = r² + R² - 2rR cosϕ    (eq. 17.6)
```

이를 (17.5)에 대입한 뒤 r/R ≈ 1/60 (달의 경우)을 이용해 Legendre 다항식으로 전개 (eq. 17.7→17.8):

```
V_M = -(γM/R) [1 + (r/R) cosϕ + (1/2)(r/R)² (3 cos²ϕ - 1) + ···]   (eq. 17.8)
```

- **1차 항**: 힘이 발생하지 않음 (상수)
- **2차 항**: 일정한 힘 γM/R² (OA 방향) — 지구가 지구-달 공통 질량중심을 공전하게 만드는 힘
- **3차 항**: **조석을 일으키는 항**. 4차 이상 항은 무시 가능

따라서 기조 위치 에너지는:

```
V = -(γM r² / 2R³) (3 cos²ϕ - 1)    (eq. 17.9)
```

### 1.2 거리 3제곱 반비례의 기원

(17.9)에서 V ∝ 1/R³. 한국 해양용어집의 "거리 세제곱에 반비례" ([KHOA] 기조력)는 위 유도의 결과.

### 1.3 수평 성분 (실제 조석을 일으키는 성분)

조석 생성력은 해면에 수직·수평 두 성분으로 분해. 수직 성분은 해저 압력으로 균형, **수평 성분만이 실제로 조석을 일으킴** (Cartwright 1999, Stewart p.316 인용).

수평 성분 (Stewart eq. 17.10):

```
H = -(1/r) ∂V/∂ϕ = (3/2) (γM r/R³) sin(2ϕ)
```

최댓값 위치: sin(2ϕ) = 1 → ϕ = 45° 또는 135° (Lubbad slides p.25에도 동일 언급).
힘이 0인 위치: sin(2ϕ) = 0 → ϕ = 0° (sublunar point) 또는 ϕ = 90°.

### 1.4 달 vs 태양 비교

(Stewart eq. 17.12-17.14):

```
G_moon = (3/4) γM (r²/R_moon³)
G_sun  = (3/4) γS (r²/R_sun³)
G_sun / G_moon = 0.46051
```

태양은 달보다 훨씬 무겁지만 거리(R³)에 반비례하므로 태양의 조석 효과는 달의 약 **0.46배**. 따라서 달이 주효과, 태양이 부효과.

## 2. 평형조석 이론 (Equilibrium Theory of Tide)

> **정의 (한국)**: 지구가 똑같은 깊이의 균질 해수로 둘러싸여 있고, 해수의 마찰과 관성은 무시 가능하며, 기조력에 대응하는 해면은 순간적으로 자유로이 변형되어 **중력과 기조력의 합력에 수직인 해면**이 된다는 가정 아래 해면 현상을 표현한 이론 ([KHOA] 평형조석이론).
>
> [PORTCALS]는 동의어로 *평형조석론*. "어떤 순간의 해면은 해수에 작용하는 중력과 기조력이 언제나 서로 직각이 된다는 가정"으로 표현 ([PORTCALS] 평형조석론).

영문: *equilibrium theory of tide*.

### 2.1 핵심 가정

(KHOA·Stewart 종합):
1. 지구 전체가 균질 깊이의 해수로 덮인 "ocean planet"
2. 해수의 관성·마찰·해류 무시
3. 해면은 기조 위치 에너지에 즉시 평형 (compliance = 무한)
4. 대륙·해저 지형 없음

### 2.2 결과 — 두 개의 부풀음 (Bulges)

위 가정 하에서 기조력 분포는 천체-지구 축 양쪽에 **두 개의 해수 부풀음**을 만든다 — 천체 방향과 그 정반대 방향 모두에 (Stewart p.314).

지구가 자전하면 두 부풀음을 통과하면서 하루에 두 번 만조가 발생 (반일주조 origin).

### 2.3 평형조석의 한계

(Stewart p.321 "17.5 Tidal Prediction" 도입부)

> "If tides in the ocean were in equilibrium with the tidal potential, tidal prediction would be much easier. Unfortunately, tides are far from equilibrium. **The shallow-water wave which is the tide cannot move fast enough to keep up with sun and moon.** On the equator, the tide would need to propagate around the world in one day. This requires a wave speed of around 460 m/s, which is only possible in an ocean 22 km deep."

즉:
- 적도에서 조석파는 하루에 지구 한 바퀴를 돌아야 함 (속도 ≈ 460 m/s, Stewart p.321)
- 천해파 속도 c = √(gh)로부터 h ≈ 22 km 깊이가 필요하나 실제 해양은 평균 약 4 km (Stewart p.321)
- 대륙이 가로막아 자유 전파 불가
- 실제 조석은 평형조석이 아닌 **dynamic tide** — 해양 분지의 sloshing (almost-resonant), 자체 중력 효과 (Stewart p.322 "selfgravitational attraction"), 탄성 해저 변형 (Stewart p.323)

→ 평형조석은 이론 골격, 실제 조석 예측은 동력학적 접근 필요.

## 3. 천체 좌표계와 시간 척도

(Stewart p.317-318)

### 3.1 적도 좌표계 (Equatorial system)

- **적위 (declination, δ)**: 천구 적도면 기준의 남북 각도
- **시각 (hour angle, τ₁)**: 천체-지구 축이 적도와 교차하는 자오선의 경도
- **춘분점 (vernal equinox)**: 황도와 적도의 교차점. 천체 위치의 영점.

### 3.2 황도 좌표계 (Ecliptic system)

- 지구 공전 평면을 기준
- 황도 경위도 (ecliptic latitude/longitude)
- **황도 경사 (obliquity of the ecliptic) = 23.45°** — 지구 자전축이 공전면에 대해 기울어진 각도

### 3.3 핵심 주기

(Stewart p.318)

| 주기 | 값 | 의미 |
|---|---|---|
| Solar day | 24 h 0 m | 태양 시각 주기 |
| Lunar day | **24 h 50.47 m** | 달 시각 주기 |
| Tropical month | 27.32 solar days | 달의 적위 한 주기 |
| Lunar nodal cycle | 18.613 years | 달 궤도면의 지구 축 기준 회전 |
| Lunar perigee | 8.85 years | 달 근지점 회전 |
| Earth precession | 26 000 years | 자전축 세차 |
| Sun perigee | 20 942 years | 지구 근일점 회전 |

> **정밀도 비교**: Lubbad 슬라이드 p.19 = "Lunar day 24 h 50 min"; Stewart = 24 h 50.47 min. 일반론·실무에서는 24 h 50 m이 통용되나, 정밀 계산은 50.47 m.

### 3.4 메톤 주기 (Metonic cycle)

> 그리스 천문학자 메톤이 태음력을 태양력에 일치시키기 위해 만든 역법. 19년 주기. 19년 = 6939.6018일, 235 삭망월 = 6939.6882일로 태양(계절)과 달(삭망)의 관계가 거의 완전하게 순환. ([KHOA] 메톤주기)

조석 예측에서 19년 데이터 권장의 이론적 배경 (Stewart p.322 — Harmonic Method가 "more than 18.6 years of data needed to resolve the modulation of the lunar tides").

## 4. 분조 (Tidal Constituents)

> **정의**: 조석에 영향을 미치는 개개의 조석 성분. 조석은 달·태양을 포함한 다수 천체의 규칙적인 특성 성분이 합해져서 나타난다. **조석 특성 분석에 사용하는 분조는 약 64개**. 각 분조의 진폭(반조차)과 지각을 **조화상수**라 한다. ([KHOA] 분조)

영문: *tidal constituent* (또는 *partial tide*, *component tide*).

### 4.1 Doodson 전개

Stewart eq. 17.16에서 위 식을 더 정확하게 전개하면, 천체 위치 (δ, τ₁)에 따라 조석 위치 에너지가 **세 그룹의 주기**로 분해됨:
- **반일주조** (twice-daily, 약 12 h): cos2τ₁ 항
- **일주조** (daily, 약 24 h): cos τ₁ 항
- **장기조** (long period, 14일·180일 등): 비-τ 항

Doodson (1922)은 (17.16)을 6개 기본 주파수의 정수 조합으로 푸리에 전개:

```
f = n₁f₁ + n₂f₂ + n₃f₃ + n₄f₄ + n₅f₅ + n₆f₆    (eq. 17.17)
```

| 기본 주파수 | 주기 | 의미 |
|---|---|---|
| f₁ | 1 lunar day | 평균 태음시 |
| f₂ | 1 month | 달의 평균 황경 |
| f₃ | 1 year | 태양의 평균 황경 |
| f₄ | 8.847 years | 달 근지점 황경 |
| f₅ | 18.613 years | 달 승교점 황경 |
| f₆ | 20 940 years | 태양 근지점 황경 |

(Stewart Table 17.1, p.319)

각 분조는 Doodson 수 (n₁n₂n₃.n₄n₅n₆)로 식별. 예: M₂ = 255.555.

총 분조 수: Doodson 전개로 **399개** — 100 장기조, 160 일주조, 115 반일주조, 14 삼일주조 (Stewart p.321). 실무에서는 진폭 큰 약 60-100개만 사용 (한국 해양용어집의 "약 64개"와 정합).

### 4.2 주요 분조와 진폭 (평형조석 이론값)

(Stewart Table 17.2, p.319-320)

#### Semidiurnal (반일주조, n₁ = 2)

| 기호 | 이름 | 평형 진폭 (m) | 주기 (h) |
|---|---|---|---|
| **M₂** | Principal lunar | 0.242334 | **12.4206** |
| **S₂** | Principal solar | 0.112841 | **12.0000** |
| N₂ | Lunar elliptic | 0.046398 | 12.6584 |
| K₂ | Lunisolar | 0.030704 | 11.9673 |

#### Diurnal (일주조, n₁ = 1)

| 기호 | 이름 | 평형 진폭 (m) | 주기 (h) |
|---|---|---|---|
| **K₁** | Lunisolar | 0.141565 | **23.9344** |
| **O₁** | Principal lunar | 0.100514 | 25.8194 |
| P₁ | Principal solar | 0.046843 | 24.0659 |
| Q₁ | Elliptic lunar | 0.019256 | 26.8684 |

#### Long Period (장기조, n₁ = 0)

| 기호 | 이름 | 평형 진폭 (m) | 주기 (h) |
|---|---|---|---|
| Mf | Fortnightly | 0.041742 | 327.85 (≈13.66일) |
| Mm | Monthly | 0.022026 | 661.31 (≈27.55일) |
| Ssa | Semiannual | 0.019446 | 4383.05 (≈182.6일) |

> 진폭은 Apel (1987) 인용 (Stewart Table 17.2 footnote).

### 4.3 한국 해양용어집 — 주요 4대분조

> **주요 4대 분조 (major four tidal components)**: 분조 중에서 진폭이 큰 4개. **M₂ (주태음반일주조), S₂ (주태양반일주조), K₁ (일월합성일주조), O₁ (주태음일주조)**. ([PORTCALS] 주요 4대분조)

각 분조의 한국 명칭:

| 기호 | 한국 명칭 | 한자 | 영문 | 주기 |
|---|---|---|---|---|
| M₂ | 주태음반일주조 | 主太陰半日周潮 | principal lunar semidiurnal | 12 h 25 m (Stewart 정밀값 12.4206 h) |
| S₂ | 주태양반일주조 | 主太陽半日周潮 | principal solar semidiurnal | 12 h (정확) |
| K₁ | 일월합성일주조 | 日月合成日周潮 | luni-solar diurnal | 23.93 h ([KHOA] 일월합성일주조) |
| O₁ | 주태음일주조 | 主太陰日週潮 | principal lunar diurnal | 25.82 h (Stewart 25.8194) |

`textbook/sources.yml` 추가 source 후보: KHOA 용어집 — 별도 `khoa-glossary` source_id로 등록 권장 (별도 작업).

## 5. 조석 분류

### 5.1 일조부등에 따른 분류

| 분류 | 한국어 | 영문 | 정의 |
|---|---|---|---|
| 일주조 | 日週潮 | diurnal tide | 1조석일에 1회 고조·저조 ([KHOA] 일주조) |
| 반일주조 | 半日週潮 | semi-diurnal tide | 1조석일(약 24 h 50 m)에 2회 고조·저조 ([KHOA] 반일주조) |
| 혼합조 | 混合潮 | mixed tide | 일주조·반일주조 혼합. 일조부등이 클 때 1회만 ([KHOA] 혼합조) |

> [PORTCALS]: "모든 조석은 혼합조이지만 더 우세한 형태에 따라 일주조 또는 반일주조로 부른다" — 분류는 상대적, 우세 성분 기준.

### 5.2 천문조 vs 기상조

> **천문조 (astronomical tide)**: 달·태양 등 천체 영향에 의해 생기는 조석. 기상조에 대비. 실용적으로는 주요 4대 분조 (M₂, S₂, K₁, O₁)가 가장 크게 작용. ([KHOA] 천문조)

기상조는 폭풍해일 등 별도 토픽 — `concepts/storm-surge/` 참조 (작성 예정).

## 6. 동력학적 조석과 예측 (Dynamic Tide & Prediction)

(Stewart §17.5, p.321-326)

평형조석은 이론 골격이고, 실제 해양 조석은 **동력학적**.

### 6.1 천해파로서의 조석파

- 조석파는 천해파 (shallow-water wave) — 파장이 수심보다 훨씬 큼
- 적도 일주를 위한 속도 460 m/s 불가능 (Stewart p.321)
- 해양 분지의 **공명에 가까운 sloshing** — 분지 형상·수심이 진폭을 좌우
- **자체 중력** (selfgravitational attraction): 한 분지의 조석 부풀음이 다른 분지를 끌어당김 (Stewart p.322)
- **지각 변형**: 해수 무게로 해저가 탄성 변형, 변형은 수천 km 확장 (Stewart p.323)
- **마찰·에너지 소산**: 천해 저면 마찰, 해산·중앙해령 위 흐름, 내부파 생성으로 소산 (Stewart p.323)

### 6.2 예측 방법

**조화 방법 (Harmonic method)** — 전통적, 여전히 널리 사용:
- 19년치 데이터로 각 분조의 진폭·지각 계산 ([KHOA] 조화분해)
- 분조 주파수는 Table 17.1로부터 사전 지정
- 한계: 18.6년 이상 데이터 필요 (달의 nodal cycle, Stewart p.321), 약한 분조는 비조석 변동에 잡힘, 천해 비선형 조석에서 분조 수 폭증, 극단의 경우 tidal bore 형성 (Stewart p.321-322)

**응답 방법 (Response method)** — Munk & Cartwright (1966) 개발:
- 관측 조석과 기조 위치 에너지 간 spectral admittance 계산
- 수개월 데이터만으로 가능
- 선형파 가정 (천해 비선형 케이스에서 한계)

상세는 `03-analysis-methods.md` 참조 (작성 예정).

### 6.3 심해 조석

T/P (Topex/Poseidon) 위성 고도계 등장 이후 심해 조석 ±2 cm 정확도 측정 가능 (Stewart p.322-323). LeProvost et al. (1994)이 첫 정확한 전 지구 심해 조석도 발표 (Stewart p.314).

## 7. 비조화 상수 (Non-Harmonic Tidal Constant)

> 조위 관측 자료로부터 조화상수에 일정 공식을 적용해 산출. 항만 설계에 사용하는 조석 제원 — 약최고고조위, 대조평균고조위, 평균고조위, 소조평균고조위, **평균해면**, 소조평균저조위, 평균저조위 등. ([KHOA] 비조화상수, [PORTCALS] 비조화상수)

평균 고조 간격 (MHWI) = g_m / 28.98 (g_m은 M₂ 지각, [KHOA] 비조화상수)

이 값들은 한국 항만 설계 기준 — `concepts/coastal-structures/` 또는 `concepts/datum-and-water-levels/` (작성 예정) 토픽에서 상세.

## 8. 기준면 (Datum)

> **기본수준면 (Datum level, DL)**: 일정 기간 조석을 관측·분석한 결과 가장 낮은 해수면 (한국 = **약최저저조위, A.L.L.W**). 해도 수심·간출암 높이·조석표 조위의 기준. ([KHOA] 기본수준면)
>
> **약최저저조위**: 평균해면보다 **주요 4대분조 (M₂, S₂, K₁, O₁)의 반조차 합계**만큼 낮은 해수면. ([PORTCALS] 약최저저조위)

### 8.1 Z₀ — 4대분조 반조차합

한국 공식 정의 (국립해양조사원고시 **제2021-7호** 2021.3.31 전부개정 — [tides-khoa-nonharmonic-research.md](../../textbook/notes/tides-khoa-nonharmonic-research.md) §2):

```
Z₀ = H_M2 + H_S2 + H_K1 + H_O1
```

### 8.2 핵심 기준면 공식

```
약최고고조면 (Approx. HHWL) = MSL + Z₀
기본수준면     (DL, Chart Datum) = MSL - Z₀
A.L.L.W              ≡ DL (= 한국 해도 수심 기준)
```

→ Darwin의 *Indian Spring Low Water (ISLW)* 방식과 동일.

DL을 0으로 설정하면 MSL = Z₀ (DL 기준 표기).

### 8.3 한국 4대분조 각속도 (국립해양조사원고시 제2021-7호)

| 분조 | 각속도 (°/hr, **9자리 정밀**) | 주기 (h) | 9·a (KST offset) |
|---|---|---|---|
| **M₂** | 28.984104156 | 12.4206 | 260.857° |
| **S₂** | 30.000000000 | 12.0000 | 270.000° |
| **K₁** | 15.041068639 | 23.9344 | 135.370° |
| **O₁** | 13.943035584 | 25.8194 | 125.487° |

→ Stewart Table 17.2 (§4.2) 값과 정합. 9자리 정밀값은 `khoa-tide-model` skill.md 인용 ([tides-khoa-cross-verification.md](../../textbook/notes/tides-khoa-cross-verification.md) §2 검증).

### 8.3.1 위상 기준 (G / g / κ) — 변도성 2007

한국에서 사용되는 3가지 조석 지각 기준:

| 기준 | 정의 | 사용처 |
|---|---|---|
| **G (Greenwich)** | 그리니치 자오선 (경도 0°) 기준 지각 | 국제 표준, **FES2022·EFDC**, UTide UTC 출력 |
| **g (135°E / KST)** | 한국 표준시 자오선 (135°E) 기준 지각 | **KHOA 보고서·조석표**, UTide KST 출력 |
| **κ (kappa)** | 관측 지점 경도 기준 local 지각 | 한국 일부 오래된 연구 |

**변환 공식** (변도성 2007):
```
g = G + 9·a    (mod 360)
G = g - 9·a    (mod 360)
```
여기서 9는 9시간(KST = UTC+9), a는 분조 각속도 (°/hr).

> 통합 DB·자료원 사용 시 G/g 어느 기준인지 **반드시 확인**. tide_model 통합 DB의 g 컬럼에 일부 정점 변환 오차 발견 — 인용 시 DASHBOARD 조위관측소_조화상수.csv (검증된 정확값) 우선 ([tides-khoa-cross-verification.md](../../textbook/notes/tides-khoa-cross-verification.md) §3).

### 8.4 비조화상수 — 부산항 검증된 공식

비조화상수는 **모두 DL 기준** (`tides-khoa-nonharmonic-research.md` §3 — 사용자 연구가 **KHOA 부산항 조석표 공시값**과 정확히 일치 검증; H_M2=40 cm는 조석표 공시 정점값. DT_0005 부산 (38.23 cm)·다대포항 (42.6 cm) 등 sub-stations 별도, [tides-khoa-cross-verification.md](../../textbook/notes/tides-khoa-cross-verification.md) §4):

| 비조화상수 | 한국어 | 공식 | 부산항 (cm) |
|---|---|---|---|
| Z₀ | 4대분조 반조차합 | H_M2 + H_S2 + H_K1 + H_O1 | 64.9 |
| MSL | 평균해면 | Z₀ | 64.9 |
| Approx. HHWL | 약최고고조면 | 2 × Z₀ | 129.8 |
| **대조승** | Spring Rise | 2·H_M2 + 2·H_S2 + H_K1 + H_O1 | 123.8 |
| **소조승** | Neap Rise | 2·H_M2 + H_K1 + H_O1 | 86.0 |
| 평균조차 | Mean Range | 2 × H_M2 | 80.0 |
| 대조차 | Spring Range | 2 × (H_M2 + H_S2) | 117.8 |
| 소조차 | Neap Range | 2 × (H_M2 - H_S2) | 42.2 |
| HWI(g) | 평균고조간격(KST g) | g_M2 / 28.984104156 (시간) | 8h 07m |
| HWI(κ) | 평균고조간격(local κ) | κ_M2 / 28.984104156 (시간) | 8h 02m |

> **"조승" ≠ "조차" — 혼동 금지**
> 조승 = DL 기준 **높이** (m above DL).
> 조차 = 고조-저조 **차이** (m, range).

### 8.5 조석 형태 계수 (Form Factor)

```
F = (H_K1 + H_O1) / (H_M2 + H_S2)
```

**한국 KHOA 공식 분류** (`khoa-annual-reports` Annual Report 2025 인용):

| F 범위 | 한국 KHOA 명칭 | 영문 |
|---|---|---|
| **0 – 0.25** | **반일주조형** | semidiurnal |
| **0.25 – 1.50** | **반일주조가 우세한 혼합형** | mixed (mainly semidiurnal) |
| **1.50 – 3.00** | **일주조가 우세한 혼합형** | mixed (mainly diurnal) |
| **≥ 3.00** | **일주조형** | diurnal |

> KHOA 2025 Annual Report §3.1 인용. 본 분류는 NOAA 등 국제 통용 기준과 일치하나 **한국 공식 명칭 한국어 표기는 위와 같음**.

부산항: F = 0.102 → 반일주조형. 인천 (DT_0001): F = 0.169 → 반일주조형.

### 8.6 평균해면 장기 추세 — 한국 연안 SLR

MSL은 단기적으로 안정한 비조화상수이지만 **장기 추세**(decade scale)에서는 해수면 상승(Sea Level Rise) 신호. KHOA Annual Report 2007-2025 19년 데이터 13정점 선형회귀:

| 정점 그룹 | 평균 SLR (mm/yr) | 비고 |
|---|---:|---|
| 한국 전체 (13정점) | **3.94** | 글로벌 평균(3.4) 초과 |
| 남해 | 4.10 | Kuroshio 영향 |
| 서해 | 3.90 | |
| 동해 | 3.72 | |
| **서귀포** | **5.42** | 한국 최대 (동중국해/Kuroshio) |
| **울산** | **2.59** | 최소 (큰 단기 변동성) |

전체 분석: [`experience/khoa-annual-climate-trend.md`](../../experience/khoa-annual-climate-trend.md).

→ 설계 수명 30~50년 구조물은 MSL을 **고정값 아닌 trend 적용** 권장. 가속화(acceleration) 시그널 — 본 19년 평균 3.94 mm/yr는 KHOA 1989-2017 분석(2.97 mm/yr)보다 33% 높음.

## 9. 보강 필요·미해결

- Laplace 조석 방정식 (Laplace tidal equations) — Stewart는 명시 인용 없음, 별도 source 필요
- Amphidromic system 형성 메커니즘 — Stewart §17.5에 그림(17.13 M2 global map) 있으나 별도 보강 권장
- 한국 연안 조차 분포 (서해/남해/동해) — KHOA 별도 자료 필요
- 비조화 상수 산출 공식 전체 (MHWI·MLWI 외) — [KHOA] 비조화상수에 일부, 전체는 KHOA 매뉴얼 별도 인용
- 분조 nomenclature 상세 (Doodson number, Darwin name) — Stewart Table 17.2 footnote 외 별도 보강

## 10. 연결

- `01-concept.md` — 정의·용어 개관 (verified)
- `03-analysis-methods.md` (미작성) — 조화분해 구현, t_tide·UTide·pytides
- `04-code-and-tools.md` (미작성) — 조석 예측 코드
- `06-model-application.md` (미작성) — EFDC tidal forcing (M₂·S₂·K₁·O₁), ADCIRC tidal database
- 소스 노트:
  - [`textbook/notes/tides-lubbad2009-overview.md`](../../textbook/notes/tides-lubbad2009-overview.md) — Lubbad 슬라이드 개관 (verified)
  - `textbook/notes/tides-stewart-ch17.md` (생성 예정) — Stewart §17.4-17.5 전용 노트
- 외부 참조:
  - Pugh, D. T. (1987). *Tides, Surges and Mean Sea-Level*. Wiley. — Stewart가 위치 에너지 유도에서 인용 (Stewart p.315)
  - Cartwright, D. E. (1999). *Tides: A Scientific History*. Cambridge. — 수평/수직 성분 분리 인용 (Stewart p.316)
  - Doodson, A. T. (1922). 분조 주파수 전개 — Stewart p.319 인용
  - Munk, W., & Cartwright, D. E. (1966). Response method — Stewart p.322 인용
  - LeProvost, C. et al. (1994). 첫 전 지구 심해 조석도 — Stewart p.314 인용
  - Apel, J. R. (1987). 분조 평형 진폭 데이터 — Stewart Table 17.2 footnote

## 검증 이력

**2026-05-21 Claude Opus 4.7 cross-reference 검증**

소스 파일:
- `textbook/md/stewart_textbook.md` § "Coastal Processes and Tides" (Stewart §17.4-17.5, p.314-326)
- `khoa-portcals-glossary` source (3055 entries, KHOA + PORTCALS — [textbook/sources.yml](../../textbook/sources.yml))

검증 통과 항목 (페이지별 인덱싱 후 needle lookup, char/word 중복 정규화):

| § | 항목 | 출처 | 결과 |
|---|---|---|---|
| 1.1 | eq. 17.5 V_M = -γM/r₁ | Stewart p.315 | PASS |
| 1.1 | r/R ≈ 1/60 (달) | Stewart p.315 | PASS |
| 1.1 | eq. 17.9 (3 cos²ϕ - 1) | Stewart p.315 | PASS |
| 1.3 | eq. 17.10 H ∝ sin(2ϕ) | Stewart p.316 | PASS |
| 1.4 | G_sun/G_moon = 0.46051 | Stewart p.317 eq. 17.14 | PASS |
| 3.3 | Lunar day 24 h 50.47 m | Stewart p.318 | PASS |
| 3.3 | 황도 경사 23.45° | Stewart p.318 | PASS |
| 3.4 | 메톤주기 19년 | KHOA glossary | PASS |
| 4.1 | f₁ = 14.49205211°/hr | Stewart Table 17.1 p.319 | PASS |
| 4.1 | Doodson 399 constituents | Stewart p.321 | PASS |
| 4.1 | 분조 약 64개 | KHOA 분조 | PASS |
| 4.2 | M₂ 12.4206 h, K₁ 23.9344 h, Mf 327.85 h | Stewart Table 17.2 p.319 | PASS |
| 4.3 | 주요 4대분조 M₂ S₂ K₁ O₁ | PORTCALS 주요 4대분조 | PASS |
| 4.3 | K₁ 일월합성일주조 23.93h | KHOA 일월합성일주조 | PASS |
| 5.1 | 반일주조 12시간 25분 | KHOA 반일주조 | PASS |
| 5.2 | 천문조 (4대분조) | KHOA 천문조 | PASS |
| 6.1 | 460 m/s, 22 km deep | Stewart p.321 | PASS |
| 6.1 | selfgravitational | Stewart p.322 | PASS |
| 6.1 | elastic solid 변형 | Stewart p.323 | PASS |
| 6.2 | 18.6 years 데이터 필요 | Stewart p.321 | PASS |
| 8 | 약최저저조위 = MSL - (4대분조 반조차) | PORTCALS 약최저저조위 | PASS |

**페이지 번호 정정 적용**:
- 17.5 Tidal Prediction 도입부: p.322 → p.321
- 460 m/s, 22 km, 18.6 years: p.322 → p.321
- selfgravitational: p.323 → p.322
- (이 정정은 PDF의 페이지 break가 단원 헤더 직전에 위치한 데서 발생)

**보강 권장** (현재 verified 외 추가 인용 필요 항목):
- Laplace 조석 방정식 — Stewart에 명시 인용 없음, 별도 source
- Amphidromic system 형성 — Stewart figure 17.13 (M2 global map) 외 별도 보강
- 한국 연안 조차 분포 — KHOA 별도 자료
- 비조화상수 산출 공식 전체 — KHOA 매뉴얼 별도

**사용자 override**: 본 검증은 AI cross-reference. 의문 시 `citation_status: source-needed` 강등하고 재검토.
