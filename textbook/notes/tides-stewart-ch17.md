---
title: "Tides — Stewart, Introduction to Physical Oceanography, Ch.17"
source_id: stewart-physical-ocean
chapter: "17 Coastal Processes and Tides (§17.4 Theory + §17.5 Tidal Prediction)"
pages: "314-326"
page_offset_applied: false
topic: tides
canonical_source: self
citation_status: verified
verification_method: "AI programmatic cross-reference against textbook/md/stewart_textbook.md"
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-21
verification_by: "Claude Opus 4.7 (1M context) — cross-ref"
verification_date: 2026-05-21
---

# Stewart §17.4 Theory of Ocean Tides + §17.5 Tidal Prediction

> Stewart, R. H. *Introduction to Physical Oceanography*. ch.17 "Coastal Processes and Tides" pages 314-326.

## §17.4 Theory of Ocean Tides 핵심

### 조석의 중요성 (p.313-314)

Stewart는 §17.4 도입부에서 조석의 8가지 중요성을 나열:
1. 강한 조류 (연안에서 최대 5 m/s), 항해·혼합에 영향
2. 해산·대륙사면·중앙해령 위에서 내부파 생성 → 해양 혼합 주요 동력
3. 조석 혼합이 심층 순환과 기후 영향
4. 심해 저서 퇴적물 부유 가능
5. 지각 탄성 변형 — 조석 위치 에너지와 해양 조석 무게로 해저·대륙이 약 10 cm 상하 운동, 정밀 측지에 영향
6. 해양 조석이 기조 위치 에너지에 비해 lag → 지구-달 각운동량 전달 → 지구 자전 감속, 달 멀어짐
7. 위성 궤도에 영향 (altimetry 보정 필수)
8. 다른 행성·항성에도 적용 — 수성·금성·Io 자전 속도 결정

### 기조 위치 에너지 유도 (p.315-316)

Pugh (1987 §3.2) 유도 채택. 좌표계 (Figure 17.10):
- O = 지구 중심
- P = 지구 표면 점
- A = 천체
- r = OP, R = OA, ϕ = ∠POA, r₁ = PA

```
V_M = -γM / r₁                              (17.5)
r₁² = r² + R² - 2rR cosϕ                    (17.6)
V_M = -(γM/R) [1 - 2(r/R)cosϕ + (r/R)²]^(-1/2)    (17.7)
```

r/R ≈ 1/60 (달), Legendre 다항식 전개:

```
V_M ≈ -(γM/R) [1 + (r/R)cosϕ + (1/2)(r/R)²(3 cos²ϕ - 1) + ···]    (17.8)
```

- 1차 항: 힘 0 (상수)
- 2차 항: 일정 힘 γM/R² (OA 방향) — 지구가 지구-달 공통 질량중심 공전
- 3차 항: **조석 항**. 4차+ 무시

```
V = -(γM r² / 2R³) (3 cos²ϕ - 1)            (17.9)  ← tide-generating potential
```

> Stewart는 명시적으로 비판: "많은 해양학 책이 조석을 (i) 지구-달 공전의 구심 가속도 + (ii) 만유인력의 두 과정으로 설명하지만, 기조 위치 에너지 유도에는 구심 가속도가 사용되지 않으며 천문학·측지학 공동체에서 이 개념을 쓰지 않는다." (p.315)

### 수평·수직 성분 분리 (p.316)

Cartwright (1999, p.39, 45) 인용:
> "The vertical component is balanced by pressure on the sea bed, but the ratio of the horizontal force per unit mass to vertical gravity has to be balanced by an opposing slope of the sea surface, as well as by possible changes in current momentum"

수평 성분:
```
H = -(1/r) ∂V/∂ϕ = (3G/r) sin(2ϕ)           (17.10)
G = (3/4) γM (r²/R³)                         (17.11)
```

최댓값 ϕ = 45°, 135°. 0 at ϕ = 0° (sublunar), 90°. Figure 17.11에 도식.

### 달 vs 태양 (p.317)

```
G_sun  = (3/4) γS (r²/R_sun³)                (17.12)
G_moon = (3/4) γM (r²/R_moon³)               (17.13)
G_sun / G_moon = 0.46051                      (17.14)
```

태양은 더 무거우나 거리 R³에 반비례하여 효과는 달의 약 46%.

### 좌표·시간 척도 (p.317-318)

적도 좌표계 (Pugh 1987:72 인용):
- 적위 (declination) δ
- 시각 (hour angle) τ₁
- 춘분점 (vernal equinox, "First Point of Aries")
- 황도 (ecliptic), 황도 경사 23.45°

핵심 주기:
- Solar day = 24 h 0 m
- **Lunar day = 24 h 50.47 m**
- 황도 경사 ±23.45° (1년 주기)
- Earth precession: 26 000년
- Sun perigee: 20 942년
- Moon orbit plane 5.15° tilt to ecliptic
- Tropical month: 27.32 solar days (lunar declination 주기)
- Moon perigee rotation: 8.85년
- Moon orbit plane rotation around Earth axis: 18.613년 (lunar nodal cycle)

### 조석 주파수 (p.318-319)

eq. 17.15-17.16 전개 후 세 그룹 주파수:
- twice-daily (cos2τ₁ 항)
- daily (cos τ₁)
- long period (비-τ)

Doodson (1922) 푸리에 전개 (Table 17.1):

| 기본 주파수 | °/hour | 주기 | 의미 |
|---|---|---|---|
| f₁ | 14.49205211 | 1 lunar day | 평균 태음시 |
| f₂ | 0.54901653 | 1 month | 달 평균 황경 |
| f₃ | 0.04106864 | 1 year | 태양 평균 황경 |
| f₄ | 0.00464184 | 8.847 year | 달 근지점 황경 |
| f₅ | -0.00220641 | 18.613 year | 달 승교점 황경 |
| f₆ | 0.00000196 | 20 940 year | 태양 근지점 황경 |

각 분조 주파수: f = n₁f₁ + n₂f₂ + ... + n₆f₆. Doodson 수 (n₁n₂n₃.n₄n₅n₆). M₂ = 255.555. n₆은 보통 무시.

### Table 17.2 주요 분조 (p.319-320)

(평형조석 진폭 = Apel 1987 인용)

| Species | Constituent | Symbol | n₁ n₂ n₃ n₄ n₅ | Amplitude (m) | Period (h) |
|---|---|---|---|---|---|
| Semidiurnal | Principal lunar | M₂ | 2 0 0 0 0 | 0.242334 | 12.4206 |
| Semidiurnal | Principal solar | S₂ | 2 2 -2 0 0 | 0.112841 | 12.0000 |
| Semidiurnal | Lunar elliptic | N₂ | 2 -1 0 1 0 | 0.046398 | 12.6584 |
| Semidiurnal | Lunisolar | K₂ | 2 2 0 0 0 | 0.030704 | 11.9673 |
| Diurnal | Lunisolar | K₁ | 1 1 0 0 0 | 0.141565 | 23.9344 |
| Diurnal | Principal lunar | O₁ | 1 -1 0 0 0 | 0.100514 | 25.8194 |
| Diurnal | Principal solar | P₁ | 1 1 -2 0 0 | 0.046843 | 24.0659 |
| Diurnal | Elliptic lunar | Q₁ | 1 -2 0 1 0 | 0.019256 | 26.8684 |
| Long Period | Fortnightly | Mf | 0 2 0 0 0 | 0.041742 | 327.85 |
| Long Period | Monthly | Mm | 0 1 0 -1 0 | 0.022026 | 661.31 |
| Long Period | Semiannual | Ssa | 0 0 2 0 0 | 0.019446 | 4383.05 |

### 총 분조 수 (p.321)

Doodson 전개 = 399 분조 (장기 100, 일주 160, 반일 115, 삼일 14). 대부분 진폭 매우 작음. 큰 것만 Table 17.2.

이름: Sir George Darwin (1911).

## §17.5 Tidal Prediction 핵심

### 평형조석의 한계 (p.321)

> "If tides in the ocean were in equilibrium with the tidal potential, tidal prediction would be much easier. Unfortunately, tides are far from equilibrium. The shallow-water wave which is the tide cannot move fast enough to keep up with sun and moon."

- 적도 일주: 460 m/s 필요 → c = √(gh)에서 h ≈ 22 km, 실제 평균 4 km
- 대륙이 자유 전파 방해

### 조화 방법 (Harmonic Method, p.321-322)

19년 데이터로 각 분조 진폭·지각 계산. 사전 지정 주파수 (Table 17.1 기반).

단점:
1. **18.6년 이상 데이터 필요** (lunar nodal cycle)
2. 1e-3 정확도 39개 주파수, 1e-4 정확도 400개 필요
3. 비조석 변동이 약한 분조를 묻음
4. 천해 비선형 (특히 강 하구) — 분조 수 폭증, 극단 시 tidal bore

### 응답 방법 (Response Method, p.322)

Munk & Cartwright (1966) 개발. 관측 조석과 기조 위치 에너지 간 spectral admittance:
```
Z(f) = G(f) / H(f)
```
G, H는 위치 에너지·관측의 푸리에 변환.

- 수개월 데이터로 가능
- 분조 주파수 사전 지정 불필요
- 선형파 가정 — 천해 비선형에서 한계

### 심해 조석 (p.322-326)

T/P (Topex/Poseidon) 이후 ±2 cm 정확도. Parke et al. (1987) 궤도 설계. LeProvost et al. (1994) 첫 정확한 전 지구 심해 조석도 (p.314 인용).

심해 조석 모델링에 포함해야 할 요소 (p.322-323):
1. **selfgravitational attraction**: 한 분지 조석 부풀음이 다른 분지 끌어당김
2. **탄성 해저 변형**: 해수 무게로 해저가 변형, 수천 km 영향
3. **공명**: 해양 분지가 조석 주파수 근처 자연 공명. tidal bulge = 회전 분지 가장자리를 따라 도는 천해파. 실제 심해 조차가 Table 17.2 평형값보다 큼
4. **소산**: 천해 저면 마찰, 해산·해령 위 흐름, 내부파 생성

## 인용 라이브러리 (Stewart §17.4-17.5에서 언급된 외부 문헌)

| 인용 | Stewart 페이지 | 맥락 |
|---|---|---|
| Pugh, D. T. (1987) *Tides, Surges and Mean Sea-Level* | p.315 | 위치 에너지 유도 |
| Cartwright (1999) *Tides: A Scientific History* | p.316, 319 | 수평/수직 성분, equilibrium 정의 |
| Dietrich, Kalle, Krauss, Siedler (1980) | p.315, 316 | 유도 + Figure 17.11 |
| Doodson (1922) | p.318-319 | 분조 주파수 전개 |
| Darwin, G. (1911) | p.321 | 분조 명명 |
| Apel (1987) | p.319 (Table 17.2 footnote) | 분조 평형 진폭 |
| Lang (1980 §5.1.2) | p.318 | 천체 위치 정밀 정의 |
| Whittaker & Watson (1963 §15.1) | p.315 | Legendre 다항식 전개 |
| Ferrel (1880) | p.314 | 첫 조석 예측 기계 |
| Harris (1901) | p.314 | 37 분조 확장 |
| Munk & Cartwright (1966) | p.322 | Response method |
| LeProvost et al. (1994) | p.314 | 첫 전 지구 심해 조석도 |
| Parke et al. (1987) | p.322 | T/P 궤도 설계 |

## 연결

- `concepts/tides/02-theory.md` — 이 노트를 1차 소스로 사용
- `concepts/tides/03-analysis-methods.md` (미작성) — Harmonic/Response method 구현 상세
