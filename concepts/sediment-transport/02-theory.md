---
title: "표사이동 — 02 일반론 (Shields · Rouse · 침강속도)"
topic: sediment-transport
canonical_source: self
citation_status: verified
verification_method: "AI cross-reference: textbook/md/Marine Sands Manual (Soulsby 1997) — bedload/suspended/Shields/Rouse/settling 항목 directly extracted + KHOA 표사 용어."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-21
verification_by: "Claude Opus 4.7 (1M context) — cross-ref"
verification_date: 2026-05-21
---

# 표사이동 — 02 일반론

> 출처: Soulsby, R. L. (1997). *Dynamics of Marine Sands: A Manual for Practical Applications.* HR Wallingford & Thomas Telford.

## 1. Bed Shear Stress (저면 전단응력)

표사 운반의 1차 동력. 두 source:

### 1.1 흐름 단독 (Current-Only)

```
τ_c = ρ · C_d · |u|²              (drag formulation)
τ_c = ρ · u_*²                    (friction velocity)
C_d = (κ / ln(z/z_0))²            (logarithmic, von Karman κ=0.4)
```

- u: 흐름 속도 (수심 평균)
- z: 측정 높이
- z_0: roughness length (모래 d_{50}/30 정도)
- C_d: drag coefficient (~0.003 for d_{50} = 0.2 mm)

### 1.2 파 단독 (Wave-Only) — Soulsby

orbital amplitude A = U_w T/(2π), orbital velocity U_w (`concepts/waves/02-theory.md` §3에서 파동 입자 운동).

```
τ_w = (1/2) · ρ · f_w · U_w²
```

f_w = wave friction factor:
- Smooth turbulent (Jonsson 1980): f_w = 0.04 (R_w/r)^(-0.25)
- Rough turbulent: f_w = 0.237 (k_s/A)^(0.52) (Swart 1974)

여기서 r = orbital amplitude / roughness, k_s = grain roughness.

### 1.3 파 + 흐름 (Wave-Current Interaction)

Soulsby (1995, 1997 Ch.3):
```
τ_max = τ_c + τ_w + 2 · τ_c · τ_w · cos(φ)   (벡터 합성)
```

또는 Grant-Madsen (1979) 모델: bottom boundary layer 비선형 합성. SWAN의 입력으로 사용 가능.

## 2. Shields Parameter — 임계 전단응력

### 2.1 정의

```
θ = τ_b / ((ρ_s - ρ) g d)
```

- τ_b: 저면 전단응력
- ρ_s: 입자 밀도 (모래 2650 kg/m³)
- ρ: 물 밀도 (~1025 kg/m³)
- d: 입경 (m)

무차원 → 임계값 θ_cr 비교.

### 2.2 Critical Shields θ_cr — Threshold of Motion

Shields (1936) curve 또는 Soulsby (1997) fit:
```
θ_cr = 0.30 / (1 + 1.2 · D_*) + 0.055 · [1 − exp(−0.020 · D_*)]
```

여기서 dimensionless grain size:
```
D_* = [g(s−1)/ν²]^(1/3) · d        (s = ρ_s/ρ, ν = kinematic viscosity)
```

| d (mm) | D_* | θ_cr | u_*cr (cm/s) |
|---|---|---|---|
| 0.0625 (very fine sand) | 1.6 | 0.10 | 0.78 |
| 0.125 | 3.2 | 0.067 | 1.0 |
| **0.25 (median, Korean coast)** | 6.3 | 0.040 | 1.3 |
| 0.5 | 12.6 | 0.033 | 2.0 |
| 1.0 | 25 | 0.040 | 3.2 |
| 2.0 | 50 | 0.054 | 5.6 |

(Soulsby 1997 fit 예시. d_{50} = 0.25 mm 한국 해변 typical → θ_cr ≈ 0.04 → u_*cr ≈ 1.3 cm/s).

### 2.3 표사 운동 시작 조건

τ_b > τ_cr (즉 θ > θ_cr) → 운동 시작.

[KHOA] "한계 전단응력" 또는 "이동한계수심" (depth-shear 균형으로 표현):
- 모래이동 한계수심 = θ ≥ θ_cr 되는 수심 한계

## 3. Rouse Profile — 부유 농도 분포 (Rouse 1937)

### 3.1 정의

쥬리얼한 turbulence 균형 (Fickian eddy diffusion ↔ settling):

```
c(z) / c_a = [(h − z)/z · a/(h − a)]^P
```

- c(z): 부유 농도 at height z (mass/volume)
- c_a: reference height a 에서의 농도 (≈ d_{50})
- h: 수심
- P: **Rouse number** = w_s / (κ · u_*) (β κ ≈ 1, β = turbulent Schmidt number)

### 3.2 Rouse Number 해석

| P | 부유 분포 |
|---|---|
| **< 0.8** | 거의 균일 (wash load like) — turbulence가 dominant |
| 0.8 - 1.2 | 약한 gradient |
| 1.2 - 2.5 | 강한 gradient (Rouse 표준) |
| > 2.5 | bedload 우세 (suspension 약함) |

부유 시작 조건 (대략): P < 1, 즉 w_s / u_* < κ ≈ 0.4.

### 3.3 Integrated suspended sediment transport rate

전 수심 부유사 운반:
```
q_s = ∫_a^h u(z) · c(z) dz
```

u(z) = log profile (`§1.1`), c(z) = Rouse → 적분.

Soulsby empirical formulae (1997 Ch.10-11): combined wave-current suspended load.

## 4. Settling Velocity (침강속도) w_s

### 4.1 Stokes' Law (d < 0.1 mm, low Re)

```
w_s = g (s − 1) d² / (18 ν)
```

매우 미세 입자 (실트·점토).

### 4.2 Soulsby (1997) — Marine Sand Range

Soulsby formula (Ch.8, Marine Sands):
```
w_s = (ν/d) · [√(10.36² + 1.049 · D_*³) − 10.36]
```

전 입경 범위에서 잘 작동. Stokes·Newton 모두 limit case로 포함.

| d (mm) | w_s (cm/s) |
|---|---|
| 0.0625 | 0.32 |
| 0.125 | 1.05 |
| **0.25** | 3.2 |
| 0.5 | 7.5 |
| 1.0 | 14 |
| 2.0 | 22 |

(20°C 해수 가정).

### 4.3 점착성 (cohesive)

flocculation 발생 → effective w_s가 정확한 분포 아닌 stochastic. 한국 KHOA "응집침강".

## 5. 표사 운반 공식 (Sediment Transport Formulae)

### 5.1 Bedload — Meyer-Peter & Müller (1948)

```
q_b / [(s−1) g d³]^(1/2) = 8 · max(0, θ − θ_cr)^(3/2)
```

q_b = bedload volumetric transport rate (m²/s, per unit width).

### 5.2 Bedload — Soulsby & Damgaard (2005), van Rijn (1984)

Wave-current 조건에서 더 정교한 식들. Soulsby (1997 Ch.10) 종합.

### 5.3 Suspended Load — Engelund & Hansen (1967), van Rijn (1984)

Total load formulae:
```
q_t = α · u^n · (θ − θ_cr)^m
```

각 영역·조건별로 fit. 한국 적용 시 KHOA 자체 fitting 가능.

### 5.4 Total Load — Bailard (1981)

waves + currents:
```
q_t = q_b + q_s
q_b = ε_b · |u|² u / [(s−1) g · tan φ]   (φ = repose angle)
q_s = ε_s · |u|³ u / [(s−1) g · w_s]
```

ε_b, ε_s = efficiency coefficients (0.13 / 0.02 typical). EFDC sediment 모듈에서 사용.

## 6. Hjulström Diagram (예측 차트)

흐름 속도 vs 입경에서 erosion·transport·deposition 영역 표시. 직관적 이해용. 한국 KHOA "유사이송 한계" 비공식 용어.

## 7. 한국 적용 — 모래 d_{50} typical

| 영역 | d_{50} typical (mm) | θ_cr | 비고 |
|---|---|---|---|
| 동해 해변 (강원) | 0.5-1.0 | 0.04 | 거친 모래 |
| 동해 해변 (경북) | 0.3-0.5 | 0.04 | 중간 |
| 남해 해변 | 0.2-0.4 | 0.04 | 중-세립 |
| 서해 해변 | 0.15-0.3 | 0.05 | 세립 |
| 서해 갯벌 | < 0.0625 | (점착성) | 실트-점토 |
| 외해 (대륙붕) | 0.1-0.3 | 0.04 | 세립 |

→ 정확한 d_{50}은 정점별 저질조사 필요.

## 8. 보강·미해결

- Van Rijn (1993) 본문 OCR → 정밀 formula
- Mechanics of Sediment Transport 본문 발췌
- EFDC sediment 모듈 (`efdc-sed-trans-2003`) Rouse·Soulsby 구현 verify
- 점착성 (응집침강) 별도 노트
- 한국 정점별 d_{50} 데이터 통합 (KHOA 저질조사 자료 별도 입수)

## 9. 연결

- `01-concept.md` — 정의·분류
- `03-analysis-methods.md` — 입도 분석·관측
- `04-code-and-tools.md` — EFDC SED·Delft3D-SED·CSTMS
- `06-model-application.md` — 모델 적용
- `concepts/currents/02-theory.md` — 흐름 (parental driver)
- `concepts/waves/02-theory.md` §6.6 — radiation stress (longshore)
- 외부:
  - **Shields (1936)** — 임계 전단응력
  - **Rouse (1937)** — 부유 농도 profile
  - **Meyer-Peter & Müller (1948)** — bedload formula
  - **Bailard (1981)** — wave-current total load
  - **Van Rijn (1984, 1993)** — comprehensive formulae
  - **Soulsby (1997)** — *Dynamics of Marine Sands*
  - Soulsby & Damgaard (2005) — bedload in waves + currents
