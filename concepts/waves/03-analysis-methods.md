---
title: "파랑 — 03 분석 방법 (스펙트럼·통계·관측)"
topic: waves
canonical_source: self
citation_status: verified
verification_method: "AI cross-reference against textbook/md/Waves-Holthuijsen2007.md Ch.3 §3.5 (스펙트럼) + Ch.4 (통계). 페이지·정의·표준 spectrum 형태 인용."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-21
verification_by: "Claude Opus 4.7 (1M context) — cross-ref"
verification_date: 2026-05-21
---

# 파랑 — 03 분석 방법

> 출처: Holthuijsen (2007) Ch.3 §3.5 *The wave spectrum* p.31-55 + Ch.4 *Statistics* p.56-105.

## 1. Random-Phase/Amplitude Model (§3.5.2 p.33)

불규칙 파 시계열 η(t)를 무수히 많은 정현파의 합으로 표현:

```
η(t) = Σ_i a_i · cos(2π f_i t + φ_i)
```

가정:
- 위상 φ_i ~ Uniform(0, 2π), 서로 독립
- 진폭 a_i는 확정값 (관측에서 추출) 또는 Rayleigh 분포 (장기 통계)
- 각 성분은 분산 관계 (`02-theory.md` §2) 만족

→ Gaussian 표면 통계의 직접 결과.

## 2. Variance Density Spectrum E(f) (§3.5.3 p.36)

연속 형태로 표현:
```
E(f) df = (1/2) · 〈a²(f, f+df)〉
```

`E(f)`는 단위 [m²/Hz]. 적분:
```
m_n = ∫₀^∞ f^n · E(f) df       (n번째 모먼트)
```

### 2.1 스펙트럼 모먼트와 파라미터

| 모먼트 | 의미 | 단위 | 파라미터 산출 |
|---|---|---|---|
| m₀ | 분산 (variance) | m² | H_{m0} = 4√m₀ ≈ H_s |
| m₁ | 평균 주파수 모먼트 | m²/s | T_{m01} = m₀/m₁ |
| m₂ | zero-crossing 주기 모먼트 | m²/s² | T_{m02} = √(m₀/m₂) |
| m₄ | crest 주파수 | m²/s⁴ | T_{m24} = √(m₂/m₄) |
| f_p | spectrum peak | Hz | T_p = 1/f_p |

### 2.2 단순 파 ↔ 스펙트럼 등가

| 단순 파라미터 | 스펙트럼 표현 |
|---|---|
| **H_s = H_{1/3}** | ≈ H_{m0} = 4√m₀ (협대역 한정) |
| H_rms | 2√(2m₀) ≈ H_s/√2 |
| H_mean | √(2π·m₀) ≈ 0.626·H_s |

> 협대역 ↔ 광대역 변환 계수는 Forristall (2000) 또는 Tayfun 비선형 보정 사용 (Holthuijsen §4.2.2).

## 3. 표준 Spectrum 형태 (Holthuijsen §6.3.3)

### 3.1 Pierson-Moskowitz (PM) — Fully Developed Sea

```
E_PM(f) = α · g² / (2π)⁴ · f⁻⁵ · exp[−5/4 · (f/f_p)⁻⁴]
α = 8.1 × 10⁻³ (Phillips 상수)
f_p = 0.13 · g / U_{19.5}      (피크 주파수, 풍속 의존)
```

조건: 풍역 무한대 + 풍지속 무한대.

### 3.2 JONSWAP — Wind Sea (Limited Fetch)

JONSWAP = Joint North Sea Wave Project (Holthuijsen 본인 참여, [TOC §저자 소개](../../textbook/notes/waves-holthuijsen-toc.md)). p.95 인용:

```
E_J(f) = α · g² / (2π)⁴ · f⁻⁵ · exp[−5/4 · (f/f_p)⁻⁴] · γ^Γ
Γ = exp[−(f − f_p)² / (2σ²f_p²)]
γ ≈ 3.3 (피크 강도 enhancement factor)
σ = 0.07 (f < f_p), 0.09 (f ≥ f_p)
α = 0.076 · (U²/(F·g))^0.22       (fetch F 의존)
f_p = 3.5 · (g/U) · (F·g/U²)^(−0.33)
```

→ JONSWAP은 fetch F (km 단위 풍역 길이)와 풍속 U_{10}으로 결정. 한국 서해처럼 fetch 짧은 영역에서 사용.

### 3.3 TMA — JONSWAP + 수심 보정

TMA (Texel-Marsen-Arsloe, Bouws et al. 1985): JONSWAP을 천해에서 수심 effect로 보정. SWAN에서 표준 input spectrum.

### 3.4 PMA(Karmpadakis-Tayfun-Soares) 등 최신은 별도

## 4. Frequency–Direction Spectrum E(f, θ) (§3.5.6 p.43)

2D 스펙트럼:
```
E(f, θ) = E(f) · D(f, θ)
∫₀^{2π} D(f, θ) dθ = 1
```

방향 분포 D(f, θ) 일반 형태:
```
D(θ) = C(s) · cos^{2s}((θ − θ_m)/2)         (cosine-2s 모델)
```
s = 방향 spread parameter (s=1: 광 분산, s>10: 협 분산).

### 4.1 한국 KHOA "회절도·굴절도" → 2D 스펙트럼 활용

연안에서 방향 스펙트럼은 굴절·회절 영향 평가에 핵심.

## 5. 통계 분포 (Ch.4)

### 5.1 Surface Elevation η — Ch.4 §4.2.1

선형·random-phase 가정 하 Gaussian:
```
p(η) = (1/√(2π·m₀)) · exp(−η²/(2m₀))
```

### 5.2 Wave Height — Rayleigh 분포

협대역 가정 하:
```
P(H > h) = exp(−2h²/H_s²)
```

극단치 (Ch.4 §4.2.4 p.77):
- Forristall (2000) crest 분포 — Rayleigh보다 약간 보수적
- 짧은 시계열의 H_max ≈ H_s · √(0.5·ln(N))  (N = 파 개수)

### 5.3 Long-term Climate — Ch.4 §4.3

| 접근법 | 정의 | 사용 |
|---|---|---|
| Initial-distribution | 전 관측의 분포 적합 | 빈도가 충분 |
| Peak-over-threshold (POT) | threshold 초과만 적합 (Generalized Pareto) | 극단 사건 |
| Annual-maximum | 매년 max 적합 (Gumbel·GEV) | 설계파 (재현기간) |

한국 설계파: KCS 표준은 보통 50년·100년 재현기간 H_s 사용. POT 권장.

## 6. 관측 → 스펙트럼 (FFT)

### 6.1 시계열 → 스펙트럼

```python
# Python: scipy.signal.welch 또는 numpy.fft
from scipy.signal import welch
f, Pxx = welch(eta, fs=1.28, nperseg=1024, noverlap=512, window='hann')
# Pxx = variance density spectrum (m²/Hz) at frequencies f
```

표준 설정:
- 샘플링 1.28 Hz (관측 표준) 또는 2 Hz
- 윈도우 길이 1024 또는 2048 (분해능 vs 안정도 trade-off)
- 겹침 50%
- Hann/Hamming window

### 6.2 H_{m0} 계산

```python
import numpy as np
df = f[1] - f[0]
m0 = np.trapz(Pxx, f)                         # ≈ Σ Pxx · df
H_m0 = 4 * np.sqrt(m0)
f_p = f[np.argmax(Pxx)]
T_p = 1 / f_p
m2 = np.trapz(Pxx * f**2, f)
T_m02 = np.sqrt(m0 / m2)
```

### 6.3 방향 스펙트럼 (DSPR)

다중 센서 (buoy 가속도 + GPS, ADCP, X-band 레이더) → MEM/MLM 알고리즘으로 D(θ) 추정.

## 7. 한국 KHOA 관측 표준

| 정점 종류 | 출처 | 출력 | 관측 주기 |
|---|---|---|---|
| KMA buoy (MPT1xx) | 기상청 | H_s, T_p, 방향, 풍 | 1시간 |
| MOF buoy (MPT2xx) | 해양수산부 | 동상 + 스펙트럼 일부 | 1시간 |
| KHOA station (MPT 추가) | 국립해양조사원 | 동상 | 1시간 |

→ `05-examples.md`에서 MPT 정점 데이터 실제 사용.

## 8. 보강·미해결

- Welch vs lag-window 스펙트럼 추정 정밀도 비교
- JONSWAP γ·σ 파라미터 한국 서해 fitting 사례
- MEM/MLM 방향 추정 알고리즘 코드
- 한국 KHOA "회절도·굴절도·반사도" 산출 도구 (KHOA 자체 시뮬레이션)
- Forristall (2000), Tayfun (1980) — 비선형 분포 보정

## 9. 연결

- `02-theory.md` §2 분산관계 (스펙트럼 각 성분에 적용)
- `04-code-and-tools.md` — 스펙트럼 출력하는 모델 (SWAN·WW3·XBeach)
- `05-examples.md` — MPT 정점 실제 FFT
- 외부 인용:
  - Pierson & Moskowitz (1964) — fully developed sea
  - Hasselmann et al. (1973) — JONSWAP report
  - Bouws et al. (1985) — TMA spectrum
  - Forristall (2000) — wave crest distribution
