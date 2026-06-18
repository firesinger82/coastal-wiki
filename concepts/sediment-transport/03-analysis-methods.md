---
title: "표사이동 — 03 분석 방법 (입도·관측·formula)"
topic: sediment-transport
canonical_source: self
citation_status: verified
verification_method: "AI cross-reference: Soulsby (1997) Marine Sands + KHOA 표사 용어 + 일반 sediment analysis 표준."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-21
verification_by: "Claude Opus 4.7 (1M context) — cross-ref"
verification_date: 2026-05-21
---

# 표사이동 — 03 분석 방법

## 1. 입도 분석 (KHOA 표준)

> [KHOA] **입도분석 (grain size analysis)**: 저질의 입자 크기 분포를 결정하는 분석. 시브 분석 + 침강 분석 + 레이저 회절 등 방법별 적용 범위 차이.

### 1.1 방법

| 방법 | 적용 입경 | 특징 |
|---|---|---|
| **시브 분석 (sieve)** | > 0.0625 mm (모래·자갈) | 표준, 한국 KCS 권장 |
| **침강 분석** | 0.0039-0.0625 mm (실트) | Stokes 침강 시간 측정 |
| **레이저 회절 (LD)** | 전 범위 (자동) | 빠름, 표준화 (Mastersizer) |
| **밀도 (hydrometer)** | 실트·점토 | 전통 방법 |

### 1.2 통계 파라미터

```
d_n : n% 누적 통과 입경 (예: d_{50} = 중앙값)
M_z = (d_{16} + d_{50} + d_{84}) / 3       (mean)
σ_1 = (d_{84} − d_{16})/2 (대수 단위)      (sorting)
Sk = ((d_{84} + d_{16} − 2d_{50}) / (d_{84} − d_{16}))   (skewness)
```

(Folk & Ward 1957)

### 1.3 KHOA 용어

| 한국어 | 의미 |
|---|---|
| 입도 | d (입경, 일반) |
| 입도분포 | grain size distribution |
| 입도곡선 | cumulative grain size curve |
| 입도분석 | grain size analysis |
| 저질 | sea-bed substrate |
| 저질조사 | sea-bed sediment survey |

## 2. 현장 관측

### 2.1 흐름·파 관측

`concepts/currents/03-analysis-methods.md` (ADCP·RCM 등) + `concepts/waves/03-analysis-methods.md` (buoy·pressure).

### 2.2 표사 관측

| 항목 | 측정 |
|---|---|
| 저질 채취 | grab sampler, box corer |
| 부유사 농도 | OBS (Optical Backscatter), ABS, water sampling |
| Bedload | bedload trap, dune migration survey |
| Sandwave migration | repeat side-scan sonar, multibeam |

### 2.3 한국 KHOA 표준

- 저질조사: 정점별 grab 표본 + 시브 분석
- 부유사: OBS 정점 부유 농도 시계열 (Soulsby + Rouse profile validation)
- 사주 이동: 연안 line survey (multibeam) + GPS

## 3. Formula 적용 워크플로

### 3.1 입력 데이터

1. 저질 d_{50} (시브 분석 → median 산출)
2. 흐름 시계열 u(t) (`concepts/currents/`)
3. 파 시계열 H_s, T_p, 방향 (`concepts/waves/`)
4. 수심 h (BADA + parquet)
5. 좌표·격자

### 3.2 단계별 계산

```python
import numpy as np

# 1) Critical Shields θ_cr
def critical_shields(d_mm, rho_s=2650, rho=1025, g=9.81, nu=1.4e-6):
    s = rho_s / rho
    d = d_mm / 1000
    D_star = ((g * (s - 1) / nu**2) ** (1/3)) * d
    theta_cr = 0.30 / (1 + 1.2 * D_star) + 0.055 * (1 - np.exp(-0.020 * D_star))
    return theta_cr, D_star

# 2) Settling velocity (Soulsby 1997)
def settling_velocity(d_mm, rho_s=2650, rho=1025, g=9.81, nu=1.4e-6):
    s = rho_s / rho
    d = d_mm / 1000
    D_star = ((g * (s - 1) / nu**2) ** (1/3)) * d
    w_s = (nu / d) * (np.sqrt(10.36**2 + 1.049 * D_star**3) - 10.36)
    return w_s

# 3) Bed shear stress (current + wave Soulsby 1995)
def tau_combined(u_c, U_w, T, d_mm, h, rho=1025):
    # current
    z0 = (d_mm / 1000) / 30
    Cd = (0.4 / np.log(h / z0))**2
    tau_c = rho * Cd * u_c**2
    # wave (Swart 1974 rough)
    A = U_w * T / (2 * np.pi)
    k_s = 2.5 * d_mm / 1000      # grain roughness
    f_w = 0.237 * (k_s / A)**0.52
    tau_w = 0.5 * rho * f_w * U_w**2
    # combined (Soulsby 1995, simplified linear)
    tau_max = tau_c + tau_w      # ignoring angle for simplicity
    return tau_c, tau_w, tau_max

# 4) Shields parameter
def shields(tau, d_mm, rho_s=2650, rho=1025, g=9.81):
    return tau / ((rho_s - rho) * g * d_mm / 1000)

# 5) Bedload (Meyer-Peter Müller 1948)
def bedload_MPM(theta, theta_cr, d_mm, rho_s=2650, rho=1025, g=9.81):
    s = rho_s / rho
    d = d_mm / 1000
    factor = ((s - 1) * g * d**3)**0.5
    q_b = 8 * factor * max(0, theta - theta_cr)**1.5
    return q_b   # m²/s per unit width
```

### 3.3 적용 사례 (Korean 정점)

| 정점 | 흐름 (`currents/05`) | 파 (`waves/05`) | d_{50} (typical) | 활동도 |
|---|---|---|---|---|
| 인천 (서해) | M₂ 40 cm/s | H_s 1.0 m | 0.15 mm | **매우 강함** (강조류+파) |
| 부산 (남해) | M₂ 3 cm/s | H_s 0.7 m | 0.3 mm | 중간 (파 우세) |
| 묵호 (동해) | M₂ 0.06 m/s | H_s 1.0 m | 0.5 mm | 파 우세, 너울 침식 |

→ 정확한 d_{50}과 활동도는 정점별 저질조사 + 모델링 필요.

→ 한국 특정 항만 적용 사례(개인 모델링 영역)는 바이블 검증(객관 데이터) 후 `experience/` 에 카테고리화 — 본 canonical 미수록. <!-- citation_status: source-needed -->

## 4. Bed Form 분석 — Soulsby Ch.7

### 4.1 Wave ripples 예측 (Soulsby SC §7.3)

입력: H, T, h, d_{50} (Soulsby 1997 예제 7.3).

단계:
1. Orbital velocity U_w (Figure 14 in Soulsby) → A = U_w T/(2π)
2. Skin-friction Shields θ_ws
3. Mobility ψ = U_w²/((s−1) g d)
4. Grant-Madsen (1982) 또는 Nielsen (1992) 적용 → λ_r, Δ_r

### 4.2 Sandwave migration 분석 (Soulsby Ex.7.2)

```
q_b (volumetric) ≈ α_m · Δ · F_mig
```
- Δ: trough-to-crest height
- F_mig: migration speed (m/day)
- α_m ≈ 0.32 (Soulsby)

예제: Δ=0.8 m, F_mig=1.0 m/day → q_b ≈ 0.26 m²/day.

## 5. 장기 morphodynamic (지형 변화)

### 5.1 한계수심 ([KHOA])

| 한국어 | 영문 | 의미 |
|---|---|---|
| **이동한계수심** | limit depth of motion | θ = θ_cr 되는 수심 |
| **모래이동 한계수심** | limit depth of sand motion | 동상, 모래 한정 |
| **수심변화 한계수심** | limit depth of bathymetric change | morphodynamic depth, 장기 |

연안 morphodynamic 모델링 시 위 한계 이하만 활성.

### 5.2 평형 단면 (Dean equilibrium profile)

```
h(x) = A · x^(2/3)
A = scale parameter (입경 의존, 통상 0.04-0.15)
```

해변 단면이 장기 평형으로 수렴 — Dean 1991. Soulsby Ch.10에서 다룸.

## 6. 보강·미해결

- Van Rijn (1993) 본문 OCR 후 정밀 formula 추가
- Mechanics of Sediment Transport 본문 발췌
- 한국 정점 d_{50} 통계 (KHOA 저질조사 자료)
- 점착성 (응집침강) 분석 별도

## 7. 연결

- `02-theory.md` — Shields, Rouse, Soulsby (이 §의 식 출처)
- `04-code-and-tools.md` — EFDC SED 등 자동화
- `05-examples.md` — 실제 정점 적용
- `concepts/waves/03-analysis-methods.md`, `concepts/currents/03-analysis-methods.md` — 입력 데이터
- 외부:
  - Folk & Ward (1957) — 입도 통계
  - Soulsby (1997) Ch.7-10
  - Dean (1991) — equilibrium beach profile
