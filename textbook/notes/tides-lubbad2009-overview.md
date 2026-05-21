---
title: "Tides — Lubbad 2009 NTNU 슬라이드 개관"
source_id: lubbad2009-tides-slides
chapter: "전체 슬라이드 (p.1-73)"
pages: "1-73"
page_offset_applied: false
topic: tides
canonical_source: self
citation_status: draft-unsourced
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-21
verification_by: ""
verification_date: ""
---

# Tides — Lubbad 2009 (NTNU TBA4265) 슬라이드 개관

> **출처 주의**: 정식 교과서가 아닌 **NTNU 강의 슬라이드**. 입문 개관 적합, 깊은 이론은 별도 보강 (stewart-physical-ocean, sea-level 등).

## 슬라이드 구조

| 페이지 | 주제 |
|---|---|
| p.1-3 | 표지·코스 정보 (TBA4265 Marine Physical Environment) |
| p.4-5 | 공학적 맥락 (해안구조물, 사빈) |
| p.6 | 수위 변동 분류 |
| p.7-13 | 조석 정의·용어·전형값 |
| p.14-25 | 조석 생성력 (천체역학, 뉴턴 중력) |
| p.30 | 평형조석 (Equilibrium tide) |
| p.40 | 조화 상수 (Harmonic constituents) |
| p.50 | 조석류 (Tidal currents in inlets/bays) |
| p.60 | 폭풍해일 (Storm surge) |
| p.70-73 | 쓰나미, 기후변화 |

## 핵심 발췌

### 1. 정의 (p.8)

> "Alternate and regular rise and fall of sea level in oceans and other large bodies of water. These changes are caused by the gravitational attraction of the moon and, to a lesser extent, of the sun on the earth."

조석 = 달의 만유인력(주효과) + 태양 인력(부효과)에 의한 해양 해수면의 규칙적·교대적 상승·하강.

### 2. 용어 (p.9-12)

| 용어 | 영문 | 정의 |
|---|---|---|
| 기준면 | Datum | 조위 측정의 기준 평면. 대체로 거의 모든 조위가 그 이상이 되도록 설정 |
| Rise | Rise | 채택 척도에서 만조의 높이 (기준면 기준) |
| Range | Range | 만조와 이어지는 (또는 직전) 간조 간의 수위 차 |
| 조류 | Tidal currents | 조석 효과에 의한 수평 흐름 |
| 창조류 | Flood current | 상승 수위에 동반되는 조류 |
| 낙조류 | Ebb current | 하강 수위에 동반되는 조류 (창조류 ≠ 낙조류) |
| 조석파 | Tidal waves | 가장 긴 해양파. 수시간 주기의 규칙적 수위 진동 |

### 3. 전형 조차 (p.13)

- 외해(open ocean): 약 0.6 m
- 연안: 2–3 m
- 최대: 12 m (Bay of Fundy, Canada)

### 4. 조석 생성력 개관 (p.14-25)

천체 운동 3가지가 조석 패턴을 결정:
1. 지구 자전 (24시간)
2. 달의 지구 공전 (타원궤도, 27.32일)
3. 지구의 태양 공전 (타원궤도, 365.24일)

**중요 시간 척도**:
- Solar day = 24 h (태양이 같은 자오선에 두 번 올 때까지)
- Lunar day = **24 h 50 min** (달이 같은 자오선에 두 번 올 때까지) — 매일 만조 시각이 약 50분씩 늦어지는 원인

달 궤도면이 지구 적도면에 기울어져 있어 달이 적도면과 정확히 일치하는 순간은 **음력 한 달에 두 번뿐**.

조석 생성력은 뉴턴 *Principia*의 만유인력 법칙을 기반. 최대 힘은 천체-관측점 각도 θ = 45°와 135°에서 발생, sublunar point(θ = 0°)에서는 0.

### 5. 평형조석 (p.30)

지구가 강체이고 해양이 빠르게 평형에 도달한다고 가정하면, 조석 생성력은 해수면 경사로 균형:

```
F_tan = ρ g s (× tan)
```

여기서 s = 해수면 경사. 즉 압력 경사(중력 × 수면 경사)와 조석 생성력의 접선 성분이 균형.

**현실에서의 한계**: 평형조석은 이상화. 실제 조석은 해저 지형, 해안선, 코리올리, 마찰 영향으로 복잡한 amphidromic system을 형성.

### 6. 조화 상수 (p.40)

조석 생성 위치 에너지는 시간의 복잡한 함수. 여러 조화 성분의 합으로 분해:

| Species | Constituent | Symbol | Period |
|---|---|---|---|
| Semidiurnal | Principal lunar | M₂ | 12.42 h |
| Semidiurnal | Principal solar | S₂ | 12.00 h |
| Semidiurnal | Large lunar elliptic | N₂ | 12.66 h |
| Semidiurnal | Luni-solar | K₂ | 11.97 h |
| Diurnal | Luni-solar | K₁ | (디아넨 미명시) |
| Diurnal | Principal lunar | O₁ | (디아넨 미명시) |
| Diurnal | Principal solar | P₁ | (디아넨 미명시) |
| Long period | Lunar fortnightly | Mf | 13.66 days |
| Long period | Lunar monthly | Mm | 27.55 days |
| Long period | Solar semiannual | Ssa | 182.70 days |

> **표기 주의**: 슬라이드의 K₁/O₁/P₁ 주기는 슬라이드에서 잘려 보임. 정확한 값은 별도 보강 필요(예: K₁ ≈ 23.93 h, O₁ ≈ 25.82 h, P₁ ≈ 24.07 h).

### 7. 조석류 (p.50)

조석 inlet과 bay에서의 조류 특성:
- 큰 bay + 큰 입구 → 조류 약함
- 좁고 긴 bay 또는 좁은 inlet → 조류 강함 (단면 수축 → 가속)

### 8. 기타 수위 변동 (p.60+)

조석 외 수위 변동:
- 단기: 기압, 폭풍해일, seiche
- 계절: 기후 변동
- 장기: isostatic, 해수면 상승, 빙하 후퇴

폭풍해일은 폐쇄성 수역에서 **음의 storm surge**(수위 하강)도 발생 가능.

기후 변화에 의한 해수면 상승: 최후 빙기 이래 100–150 m (극빙 융해 + 수온 상승).

## 한계와 보강 필요

- 슬라이드라 깊이 부족 — 평형조석 수식 전체 유도, amphidromic system 형성 메커니즘, Laplace 조석 방정식 등은 정식 교과서 필요
- K₁/O₁/P₁ 주기 표 슬라이드에서 잘려 있음 — 보강
- 천체역학 그림이 슬라이드 형태라 본 노트에 옮기지 못함
- 조석 예측·조화 분해의 실제 알고리즘은 별도 자료 (`Manual_for_Tidal_Heights_Analysis_and_Pr.pdf` 등)

## 연결

- `concepts/tides/01-concept.md` — 정의·용어 (이 노트 §1, §2)
- 후속 (작성 예정):
  - `concepts/tides/02-theory.md` — 생성력·평형조석 (§4, §5 확장)
  - `concepts/tides/03-analysis-methods.md` — 조화 분해 (§6 확장)
