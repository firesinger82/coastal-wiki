---
title: "파랑 — 02 일반론 (linear theory · 분산관계 · energy · 천해변형)"
topic: waves
canonical_source: self
citation_status: verified
verification_method: "AI cross-reference against textbook/md/Waves-Holthuijsen2007.md Ch.5 (oceanic linear theory) + Ch.7 (coastal linear theory). 페이지·식 인용은 직접 lookup."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-21
verification_by: "Claude Opus 4.7 (1M context) — cross-ref"
verification_date: 2026-05-21
---

# 파랑 — 02 일반론

> 출처: Holthuijsen (2007) Ch.5 *Linear wave theory (oceanic waters)* p.106-144 + Ch.7 *Linear wave theory (coastal waters)* p.197-243. 자세한 TOC는 [`textbook/notes/waves-holthuijsen-toc.md`](../../textbook/notes/waves-holthuijsen-toc.md).

## 1. 가정 (Holthuijsen §5.3.1)

선형 파랑 이론 (linear wave theory)의 4가지 이상화:
1. 비압축성·균질 유체 (incompressible, homogeneous)
2. 점성·표면장력 무시 (gravity-only)
3. 비회전 흐름 (irrotational) → velocity potential φ 존재
4. **미소 진폭** (H/L << 1, H/h << 1) → 자유표면·운동 방정식 선형화

위 4 가정 하에서 Airy 1845의 정현파 해석 유효. **유한 진폭(Stokes 2~5차)·천해 비선형(cnoidal·solitary)** 시 §5.6 별도.

## 2. 분산 관계 (Dispersion Relation) — Holthuijsen §5.4.3 p.123

진행파 η = a·cos(kx − ωt)의 자유표면·바닥 경계조건에서 유도:

```
ω² = g k tanh(k h)        (5.18 in Holthuijsen Ch.5)
```

| 영역 | 조건 | 간소화 | 위상 속도 c |
|---|---|---|---|
| **심해 (deep water)** | kh > π (h/L > 1/2) | ω² = gk → L = gT²/2π | c = gT/2π |
| **천이 (transitional)** | π/10 < kh < π | full ω² = gk·tanh(kh) | iter 풀이 |
| **천해 (shallow water)** | kh < π/10 (h/L < 1/20) | ω² = ghk² | **c = √(gh)** |

### 2.1 수치 풀이 (Newton-Raphson)

주어진 (ω, h) → k 풀이:
```
f(k) = ω² − gk·tanh(kh) = 0
df/dk = −g·tanh(kh) − gkh·sech²(kh)
```

초기값 k₀ = ω²/g (심해 근사). 수렴 빠름 (3-5회 iter).

### 2.2 위상속도 vs 군속도 (Holthuijsen §5.4.3 p.125)

```
c   = ω/k                        (위상속도)
c_g = ∂ω/∂k = (c/2) · [1 + 2kh/sinh(2kh)]   (군속도)
```

| 영역 | c_g / c | 의미 |
|---|---|---|
| 심해 | 1/2 | 군이 위상의 절반 속도로 진행 |
| 천이 | 0.5 ~ 1 | 점진 증가 |
| 천해 | 1 | 군과 위상이 같이 (분산 없음) |

→ **에너지는 c_g로 전파** (§5.5).

## 3. 입자 운동 (Holthuijsen §5.4.2 p.119-122)

심해: 원형 궤도 (반지름 a·exp(kz), z<0 깊이).
천해: 타원 궤도 (장축 수평 → 천해에서 강한 수평 운동, 표사이동 유발).
천이: 타원 (수심에 따라 형상 변화).

## 4. 파압·압력 (Holthuijsen §5.4.3 p.128)

표면 아래 압력 변동:
```
p(z, t) − p_atm − ρgz = ρg · a · [cosh(k(h+z)) / cosh(kh)] · cos(kx − ωt)
```

→ **수압식 파고계** ([`01-concept.md` §7.1](01-concept.md))는 위 식 역연산으로 z에서 측정한 p 변동을 표면 η로 환산.

## 5. 파 에너지 (Wave Energy) — Holthuijsen §5.5 p.131-136

### 5.1 에너지 밀도 (단위 면적당)

```
E = (1/2) ρ g a²  = (1/8) ρ g H²        (5.32)
```

운동 에너지 + 위치 에너지 정확히 같이 = 각각 E/2.

### 5.2 에너지 전송

```
P = E · c_g       (energy flux, W/m, per crest-length)
```

→ **천수(shoaling)에서 진폭 증가** 원리: c_g가 천해에서 감소 → E가 증가 (= H 증가) → §7.

## 6. 천해 변형 (Coastal Transformation) — Holthuijsen Ch.7

### 6.1 Shoaling (천수) — §7.3.1 p.199

E·c_g가 보존 (정상상태, 손실 없음):
```
E₁·c_{g1} = E₂·c_{g2}
H₂/H₁ = √(c_{g1}/c_{g2}) = K_s   (shoaling coefficient)
```

심해 → 천해 천이에서 K_s는 일반적으로 1 → 0.91 → 1.0+ 변화 (deep≈1, breaking 직전 ≈ 1.5).

### 6.2 Refraction (굴절) — §7.3.2 p.202

Snel's Law (Holthuijsen p.222 — Snel의 Latin name은 Snellius. **Snel's Law (Snell이 아님)**으로 정확):
```
sin(θ)/c = const            ← 등심선을 따라
```

수심 감소 → c 감소 → θ 감소 → 등심선에 직각으로 들어옴.

### 6.3 Diffraction (회절) — §7.3.3 p.210

장애물 (방파제 끝, 갭) 우회. KHOA "회절·회절계수·회절도" 용어. wave-induced 진폭 분포는 Sommerfeld 해석해 또는 수치 (BEM, mild-slope) 풀이.

### 6.4 Reflection (반사) — §7.3.6 p.221

구조물·해벽에서 반사. 반사계수 K_r = H_r/H_i (0-1). KHOA "반사·반사파·반사율" 용어.

### 6.5 깊이 유도 쇄파 (Depth-Induced Surf-Breaking) — Holthuijsen Ch.8 §8.4.5

쇄파 한계 (Miche·McCowan):
```
H_max ≈ 0.78 · h        (단순 기준, 천해)
```

Holthuijsen Ch.9 §9.3.4의 SWAN 구현: Battjes & Janssen (1978) statistical breaker model — 스펙트럼 적분에 의한 평균 dissipation.

### 6.6 Wave-Induced Set-Up — §7.4 p.225

Radiation stress (Longuet-Higgins & Stewart 1962-64):
```
S_xx = E [n(2cos²θ + 1) − 1/2]   (방향 평균 시)
S_xy = E n cos θ sin θ
```
여기서 n = c_g/c.

쇄파 영역에서 dS_xx/dx → 평균 해면 set-up (조위 외 추가 해면 상승):
```
d(η̄)/dx = − (1/ρgh) · dS_xx/dx
```

해안 충돌 시 약 0.2 H_b (쇄파 진폭의 20%) set-up 발생. 폭풍 시 storm surge와 결합 → 침수 위험 증폭.

## 7. 비선형 정상 파 (Holthuijsen §5.6 p.137-144)

| 이론 | 적용 영역 | 특징 |
|---|---|---|
| Stokes 2-5차 | 심해 ~ 천이 | crest 가팔라짐, trough 평탄화 |
| **Dean's stream-function** | 깊이 한정 (천이) | 수치적 정상해, 비선형 정밀 |
| **Cnoidal** | 천해, kh<π/10 | 긴 trough + 좁은 crest. Jacobi cnoidal 함수 |
| **Solitary** | 천해 한계 (kh→0) | 단일 hump, 비분산 |

상세 식·계수는 Holthuijsen p.139-143.

## 8. 불규칙 파 (Irregular Waves) — Holthuijsen Ch.6 + Ch.8

선형 가정 하에서 불규칙 파 = **random-phase/amplitude model** (Ch.3 §3.5.2 p.33):
```
η(x, t) = Σ_i a_i · cos(k_i x − ω_i t + φ_i),   φ_i ~ Uniform(0, 2π)
```

각 성분은 분산 관계 만족. **스펙트럼 표현**은 `03-analysis-methods.md`로.

## 9. 에너지 균형 방정식 — Holthuijsen §6.4.1 (오션) + §8.4.1 (천해 + 흐름)

### 9.1 오션 (energy balance)

```
∂E/∂t + c_g · ∇E = S_in + S_nl4 + S_ds     (Ch.6 §6.4.1)
```

S_in: 바람 생성. S_nl4: quadruplet 비선형. S_ds: dissipation (white-capping).

### 9.2 천해 + 흐름 (action balance) — Ch.8 §8.4.1

action density N = E/σ (σ = intrinsic frequency, 흐름 있을 때 ω = σ + k·U). 흐름이 있을 때 E는 보존 안 되지만 N은 보존:
```
∂N/∂t + ∇_x · (c_x · N) + ∂(c_θ · N)/∂θ + ∂(c_σ · N)/∂σ = (S_in + S_nl4 + S_nl3 + S_ds) / σ
```

여기서 (c_x, c_θ, c_σ)는 N의 4D phase space (x, y, θ, σ) propagation velocity.

→ **SWAN의 핵심** ([04-code-and-tools.md](04-code-and-tools.md) §SWAN, Holthuijsen Ch.9).

## 10. 보강·미해결

- Boussinesq 모델 (Ch.7 §7.5) — 천해 비선형 + 분산 동시 처리
- Mild-slope equation — refraction-diffraction 결합
- Pierson-Moskowitz·JONSWAP 스펙트럼 형태 → `03-analysis-methods.md`로
- Wave breaking 정밀 조건 (Battjes-Janssen statistical)
- 한국 KHOA glossary 파랑 용어와 본 이론 항목 cross-check (별도 노트)

## 11. 연결

- `01-concept.md` — 개념·파라미터
- `03-analysis-methods.md` — 스펙트럼·통계 분석
- `04-code-and-tools.md` — SWAN·Boussinesq 모델
- `06-model-application.md` — [models/SWAN/](../../models/SWAN/) canonical
- 소스 노트:
  - [`textbook/notes/waves-holthuijsen-toc.md`](../../textbook/notes/waves-holthuijsen-toc.md) — Ch.5, Ch.7 페이지·식 매핑
- 외부 인용:
  - Holthuijsen, L. H. (2007). Ch.5, Ch.7. Cambridge UP
  - Longuet-Higgins & Stewart (1962, 1964) — radiation stress
  - Battjes & Janssen (1978) — statistical breaker model
  - Snel (1621) — Snel's Law (refraction)
