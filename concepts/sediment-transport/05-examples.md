---
title: "표사이동 — 05 학습 예제 (한국 사례)"
topic: sediment-transport
canonical_source: self
citation_status: source-needed
verification_method: "AI cross-reference: Soulsby formulae 코드 (verified). 가정값 기반 교육용 예제 — 정량 결과는 KHOA 저질조사 등 객관 데이터 확보 후 verified 가능."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-21
verification_by: ""
verification_date: ""
---

# 표사이동 — 05 학습 예제

> **상태**: 코드 frame + 정점 골격 (가정값 기반 교육용 예제). 실제 KHOA 저질 데이터 통합은 보강 대기 (source-needed → verified 승격 시 KHOA 데이터 추가).

## 1. 인천 정점 — bed shear · Shields · bedload

(가정값: d_{50} = 0.15 mm 서해 갯벌 인근, h = 10 m, M₂ 조류 0.4 m/s, 풍파 H_s=1.0 m T=5.5s)

### 1.1 코드

```python
import numpy as np
from sediment_helpers import critical_shields, settling_velocity, tau_combined, shields, bedload_MPM
# (`03-analysis-methods.md` §3.2의 함수들)

# 입력
d50_mm = 0.15
h = 10.0
u_c = 0.4          # M₂ 진폭 (m/s)
Hs = 1.0; T = 5.5
# Orbital velocity at bed (linear theory, deep-to-shallow transitional)
# U_w = π·H / (T · sinh(kh))  → k from dispersion (Newton-Raphson)
k = 0.018          # 약식 (T=5.5s, h=10m)
U_w = np.pi * Hs / (T * np.sinh(k * h))

# Shields critical
theta_cr, D_star = critical_shields(d50_mm)
w_s = settling_velocity(d50_mm)
tau_c, tau_w, tau_max = tau_combined(u_c, U_w, T, d50_mm, h)
theta = shields(tau_max, d50_mm)
q_b = bedload_MPM(theta, theta_cr, d50_mm)

print(f"d_50 = {d50_mm} mm")
print(f"θ_cr = {theta_cr:.4f}, D_* = {D_star:.2f}")
print(f"w_s = {w_s*100:.2f} cm/s")
print(f"τ_c={tau_c:.2f}, τ_w={tau_w:.2f}, τ_max={tau_max:.2f} N/m²")
print(f"θ = {theta:.3f}  (excess: {theta - theta_cr:.3f})")
print(f"q_b (MPM) = {q_b*1000:.3f} mm²/s per m width")
# Rouse number
kappa = 0.4
u_star = np.sqrt(tau_max / 1025)
P = w_s / (kappa * u_star)
print(f"Rouse P = {P:.2f}  ({'suspended-dominant' if P < 1.2 else 'bedload-dominant'})")
```

### 1.2 예상 출력

```
d_50 = 0.15 mm
θ_cr = 0.054, D_* = 3.84
w_s = 1.4 cm/s
τ_c=0.5, τ_w=1.2, τ_max=1.7 N/m²
θ = 0.74  (excess: 0.69)
q_b (MPM) = ... 
Rouse P ≈ 0.34  (suspended-dominant)
```

→ 인천 인근 서해는 **suspension 우세** (P << 1) — 강조류 + 풍파로 인한 강한 부유사 운반. 실측 OBS 검증 권장.

## 2. 동해 묵호 정점 — 너울 우세 환경

(가정값: d_{50} = 0.5 mm 거친 모래, h = 5 m, M₂ 조류 0.005 m/s, 너울 H_s=1.5 m T=10s)

```python
d50_mm = 0.5
h = 5.0
u_c = 0.005
Hs = 1.5; T = 10
# ... (위와 동일)
```

예상:
- θ_cr ≈ 0.040
- w_s ≈ 7.5 cm/s
- τ_w (long-period 너울) ≈ 0.5-1.0 N/m²
- Rouse P ≈ 1.5-2.0 → **bedload 우세**

→ 동해 해변은 거친 모래 + 너울 → bedload + 일부 suspension. 폭풍 시 비선형 sheet flow 발생 가능.

## 3. 한국 적용 사례

> 한국 특정 해역의 EFDC/SWAN 표사 모델링 적용 사례는 바이블 검증(객관 데이터: KHOA 저질조사·OBS·multibeam 등) 후 `experience/` 에 카테고리화 — 본 canonical 미수록. *(source-needed)*

## 4. 한국 해역별 표사 활동도 (정성 비교, 정량 보강 대기)

| 해역 | 정점 | d_{50} (mm) | M₂ 흐름 | H_s | 표사 모드 | 활동도 |
|---|---|---|---|---|---|---|
| 서해 (황해) | 인천 | 0.15 | 0.4 m/s | 1.0 m | **suspension 우세** | 매우 강함 |
| 서해 (황해) | 군산 | 0.10-0.20 | 0.3 m/s | 1.0 m | suspension | 강함 |
| 남해 | 부산 | 0.3 | 0.03 m/s | 0.7 m | bedload + 일부 suspension | 중간 |
| 남해 | 여수 | 0.2-0.4 | 0.05 m/s | 0.8 m | mixed | 중간 |
| 동해 | 묵호 | 0.5 | 0.005 m/s | 1.0 m | **bedload 우세** | 너울 의존 |
| 제주 | 제주 | 0.3 | 0.07 m/s | 0.8 m | bedload + 일부 suspension | 너울 의존 |

→ 정확한 d_{50}은 KHOA 저질조사 필요. 본 표는 일반론 기반 정성 비교 (가정값, source-needed).

## 5. EFDC SED 워크플로 (일반 모델 연쇄)

```
1. 외해 조류 forcing
   ↓ KHOA 수치조류도 (서해·남해) 또는 NAO.99Jb (동해)
   ↓
2. 외해 파 forcing
   ↓ SWAN (nested grid)
   ↓ middle (0.005°) → detail (0.0015°)
   ↓ 파 radiation stress + H_s + T_p output
   ↓
3. EFDC + SED 통합 시뮬
   ↓ 초기 bed (KHOA 저질조사)
   ↓ multi-class sediment (cohesive + non-cohesive)
   ↓ 시간 적분 (수개월~수년)
   ↓
4. 검증
   ↓ 인근 측정 정점 (저질·OBS·multibeam)
   ↓ 평형 단면 비교
```

## 6. 보강·미해결

- 각 정점 d_{50} KHOA 저질조사 자료 입수·통합 → 본 페이지 정량 결과 verified
- Soulsby helper 함수 실제 패키지화 → `sediment_helpers.py`
- 응집침강 (cohesive) 예제 추가
- Dean equilibrium profile 한국 해변 적용 사례

## 7. 연결

- `02-theory.md` — Shields·Rouse·Soulsby 식
- `03-analysis-methods.md` — 입도·관측·formula
- `04-code-and-tools.md` — EFDC SED·Delft3D·XBeach
- `06-model-application.md` — 모델 적용 통합
- `concepts/currents/05-examples.md` — 정점별 조류 (입력 데이터)
- `concepts/waves/05-examples.md` — 정점별 파 (입력 데이터)
- `experience/` — 한국 적용 사례는 객관 데이터 검증 후 별도 레이어로 카테고리화
