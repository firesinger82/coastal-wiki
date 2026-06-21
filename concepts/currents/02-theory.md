---
title: "조류 — 02 일반론 (분조 분해·조류타원)"
topic: currents
canonical_source: self
citation_status: verified
has_source_needed: true
verification_method: "AI cross-reference: KHOA glossary 조류타원 정의 + UTide 2D output (utide/_solve.py 'Lsmaj','Lsmin','theta','g','umean','vmean','uslope','vslope' 변수명 직접 인용) + Stewart §17 tidal currents intro (p.313-314)."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-21
verification_by: "Claude Opus 4.7 (1M context) — cross-ref"
verification_date: 2026-05-21
---

# 조류 — 02 일반론

## 1. 조류의 분조 분해 (Harmonic Decomposition of Tidal Currents)

조류는 조위와 동일한 천체 인력에 의해 발생 → **동일 분조 set**으로 분해 가능 (`concepts/tides/02-theory.md` §4 참조). 차이점:

| 항목 | 조위 (scalar η) | 조류 (vector U=(u,v)) |
|---|---|---|
| 미지수 per 분조 | 2 (진폭, 위상) | 4 (u 진폭, u 위상, v 진폭, v 위상) |
| 표현 | 단일 정현파 | **타원** (회전 벡터) |
| 출력 | (H, g) | (Lsmaj, Lsmin, θ, g) — `02-theory` §3 |

분조 분리 가능 시계열 길이는 조위와 동일 (Rayleigh criterion, [`concepts/tides/03-analysis-methods.md` §1.5](../tides/03-analysis-methods.md)).

## 2. 평형 조류 (Equilibrium Currents)

이상화된 ocean planet 가정 ([`concepts/tides/02-theory.md` §2](../tides/02-theory.md)) 하에서:
- 조위의 동·서 경사 → 동·서 압력 경사 → 조류 동·서 성분
- 남·북 경사 → 남·북 압력 경사 → 조류 남·북 성분
- 두 성분은 시간 위상 차로 결합 → 조류 벡터가 시간에 따라 회전

평형조류는 **이론 골격**이고 실제 조류는 동력학적 (§5).

## 3. 조류타원 (Tidal Current Ellipse)

### 3.1 정의 ([KHOA] 조류타원)

> 조석 주기(12시간 25분) 동안 조류의 유향·유속을 벡터로 나타내고, 그 끝을 연결하여 만든 **타원**. 타원의 **회전방향, 반장축·반단축의 크기, 장축의 기울기, 위상**에 의하여 표현한다. 이를 통해 **최강창조류와 최강낙조류의 크기, 방향, 시각** 정보를 구할 수 있다.

### 3.2 4개 parameter (UTide 2D 출력)

분조 n에 대한 조류 타원 표현 (`khoa-tide-model` UTide _solve.py 2D mode `coef["Lsmaj"]`, `coef["Lsmin"]`, `coef["theta"]`, `coef["g"]` 인용):

| 기호 | UTide 변수 | 의미 | 단위 |
|---|---|---|---|
| **L_smaj** | `Lsmaj` | 반장축 (semi-major) — 타원의 가장 긴 반축, 최강 조류 속도 | m/s, cm/s |
| **L_smin** | `Lsmin` | 반단축 (semi-minor) — 타원의 짧은 반축. **부호**가 회전 방향을 표시 (+ = CCW / − = CW, UTide 규약) | m/s |
| **θ (theta)** | `theta` | inclination — 장축이 양의 x축(동쪽)으로부터 반시계 방향으로 이루는 각도 | ° (0-180) |
| **g** | `g` | phase — Greenwich (또는 사용자 설정 기준) 시각에 분조 인수가 0일 때부터 조류 벡터가 장축의 한쪽 끝에 도달할 때까지의 시간을 위상으로 표현 | ° |

### 3.3 회전 방향

| 부호 of L_smin | 회전 | 의미 |
|---|---|---|
| L_smin > 0 | **반시계 (counter-clockwise, CCW)** | 북반구 외해에서 흔함 (Coriolis right-deflection 결과의 자연 회전) |
| L_smin < 0 | **시계 (clockwise, CW)** | 남반구 외해 또는 북반구 일부 만 |
| L_smin ≈ 0 | **왕복성 (reversing)** | 좁은 수로·연안에서 — 한국 서해 다수 |

### 3.4 최강 창조류 / 낙조류 추출

조류타원에서 ([KHOA] 조류타원):
- **최강 창조류** = 타원 장축 양 끝점 중 한쪽 도달 시
- **최강 낙조류** = 반대 끝점 도달 시
- 두 최강 사이 시간 ≈ 6.21 h (M₂ 분조 기준 = 12.42 h / 2)

왕복성 (L_smin ≈ 0)에서는 두 끝점이 정확히 반대 방향. 회전성 (L_smin > 0)에서는 두 끝점도 반대 방향이지만 사이에 게류가 명확하지 않거나 유속만 최소.

### 3.5 다중 분조 합성

실제 조류는 여러 분조의 합 — 각 분조 타원이 시간에 따라 회전·중첩하여 복잡한 패턴 생성. 시각화는:
- 매 분조별 타원 4 parameter 표
- 시간 적분 → vector hodograph (등조류선)
- 또는 `03-analysis-methods.md` §1.5 등조류선 (co-current line)

## 4. Coriolis 효과

> 본 §은 일반론·source-needed로 표시 (Stewart §17.4에 명시 인용 없음, 별도 source 보강 필요).

회전 조류 패턴의 1차 원인:
- 북반구: 흐름의 방향이 오른쪽으로 편향 → 시간에 따라 자연스러운 CCW 회전 (대규모 해역)
- 좁은 수로에서는 지형 제약이 Coriolis를 압도 → 왕복성

Stewart §9 (Geostrophic Currents)·§11 (Vorticity)에서 Coriolis 일반 다루지만 조류 ellipse 형성에는 별도 텍스트 필요 (Pugh 1987, Cartwright 1999 등).

## 5. 동력학적 조류 — 평형조석 한계 (Stewart §17.5 p.321)

조위와 동일한 한계 ([`concepts/tides/02-theory.md` §6.1](../tides/02-theory.md)):
- 조류파는 천해파 (shallow water wave)
- 적도 일주에 460 m/s 필요 → 22 km 깊이 평형 조건 미달
- 실제 해양 = sloshing in basin, self-gravitation, 탄성 변형, 마찰 소산

**조류 dynamic 효과 추가**:
- **연속방정식**: 단면 수축에서 가속 (Lubbad p.50, [01-concept.md §6](01-concept.md))
- **저면 마찰**: 천해에서 조류 진폭 감쇠 + 위상 지연
- **Kelvin wave 패턴**: 분지 경계를 따라 진행하는 조류파 (Stewart Kelvin wave 19회 인용, 주로 §10-13)
- **Amphidromic 시스템**: 조위 진폭 0이 되는 회전 중심 — 조류는 그 주변을 회전

## 6. 한국 해역 조류 특성 (typical)

> 본 §은 일반론 기반. 정량 검증은 [`05-examples.md`](05-examples.md) 수치조류도 데이터 분석으로 보강.

| 해역 | 조류 패턴 | M₂ 최강 typical | 주조 |
|---|---|---|---|
| 서해 (황해) | 강한 왕복성 | 1-3 m/s (수로 5 m/s+) | 반일주조 |
| 남해 | 중간, 일부 회전성 | 0.5-1 m/s | 반일주조 |
| 동해 | 약함, 회전성 | < 0.3 m/s | 일주조 우세 |
| 명량해협 (전남) | 강한 왕복성 | 5+ m/s | 반일주조 |
| 진도해협 | 강한 왕복성 | 3-5 m/s | 반일주조 |

→ 정량 검증은 [`05-examples.md`](05-examples.md)에서 수치조류도 CSV 격자에서 직접 추출.

## 7. 분조 set (조류 적용)

조위와 동일 ([`concepts/tides/02-theory.md` §4](../tides/02-theory.md)):

| 분조 | 우선순위 | 메모 |
|---|---|---|
| **M₂** | 1 | 한국 서해 우세 |
| **S₂** | 2 | 대조·소조 변동 |
| **K₁** | 3 | 동해 일주조 핵심 |
| **O₁** | 4 | 동해 일주조 |
| N₂, K₂, P₁ | 보조 | 정밀 분석용 |
| **M₄, MS₄, M₆** | 천해 비선형 | 서해 강함 |

수치조류도 CSV는 14 분조 제공 (`khoa-tide-model`/수치조류도 헤더):
j1, k1, k2, l2, m1, m2, mu2, n2, nu2, o1, oo1, p1, q1, s2

## 8. 보강·미해결

- Coriolis ↔ 조류타원 회전 방향 정량 (§4)
- Pugh (1987) tidal current chapter 인용 추가
- 한국 동해 회전성 조류 사례·자료
- 명량·진도해협 조류 극값 정량 source

## 9. 연결

- `01-concept.md` — 정의·분류·KHOA 표준
- `03-analysis-methods.md` — UTide 2D·ADCP 분석
- `04-code-and-tools.md` — UTide 2D 출력 sample
- `05-examples.md` — 수치조류도에서 정점 추출
- `concepts/tides/02-theory.md` — 분조 이론 (조류와 공유)
- `concepts/tides/02-theory.md` §8.3 4대분조 각속도 9자리 정밀
- 외부 인용:
  - UTide 2D 출력 변수: `wesleybowman/UTide/utide/_solve.py` (Lsmaj, Lsmin, theta, g)
  - [KHOA] 조류타원 정의
  - Stewart §17.4 (p.313-314) tidal currents intro
