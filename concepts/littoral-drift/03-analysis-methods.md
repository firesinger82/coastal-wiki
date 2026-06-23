---
title: "연안표사 분석·산정 방법 — CERC 공식·Kamphuis/Damgaard-Soulsby·sediment budget·one-line shoreline 변화 (Soulsby §10.5, Dean-Dalrymple §10.5)"
topic: littoral-drift
canonical_source: self
citation_status: verified
has_source_needed: true
verification_method: "Soulsby 'Dynamics of Marine Sands' (marine-sands-manual) §10.5 Longshore transport — CERC 공식 Eq(138) 본문·계수 0.023 (p.198) + 계수 calibration/적용 한계 (p.199) + Damgaard-Soulsby Eq(139a-e) (p.199-200) + Example 10.3 longshore transport 수치 (p.201-203, shingle Q_LS=36,700 m3/yr vs CERC 819,410 m3/yr) + beach planshape(one-line)·coastal profile 모델 분류·sediment budget 셀 (p.207-208) 직접 인용. Dean-Dalrymple 'Water Wave Mechanics' (water-wave-mechanics) §10.5 Example 10.2 longshore wave thrust Eq(10.37) F_y=-dS_xy/dx (p.309) 인용. 모든 page 는 textbook/md ---PAGE-NN--- 구분자로 직접 확인."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - concepts/littoral-drift/01-concept.md
  - concepts/littoral-drift/02-theory.md
  - concepts/littoral-drift/04-code-and-tools.md
  - concepts/sediment-transport/01-concept.md
---

# 연안표사 분석·산정 방법

> [`01-concept.md`](01-concept.md) 의 정의·CERC·Komar-Inman 정형과 [`02-theory.md`](02-theory.md) 의 radiation stress → longshore current 유도를 받아, **실무 산정 절차**로 연결한다. 흐름: (1) 단면 적분 transport rate 공식(CERC·Kamphuis·Damgaard-Soulsby) → (2) 공간적 표사수지(sediment budget) → (3) one-line shoreline 변화식.
>
> 공식·계수의 출처는 본 위키 보유 교과서 중 longshore transport 를 **정량 수식·계수·검증 예제**까지 담은 Soulsby *Dynamics of Marine Sands* §10.5 (`marine-sands-manual`) 를 주 reference 로 한다. driver(longshore wave thrust) 의 momentum 수식은 Dean-Dalrymple §10.5 (`water-wave-mechanics`).

## 1. driver — longshore wave thrust (Dean-Dalrymple §10.5)

surf zone 에서 oblique wave 가 breaking → wave energy 감소 → radiation stress shear component $S_{xy}$ 감소 → 그 cross-shore gradient 가 alongshore force(longshore wave thrust)를 만든다. straight & parallel bottom contour 가정에서 단위면적당 thrust (`water-wave-mechanics`, p.309 §10.5 Eq (10.37)):

$$F_y = -\frac{\partial S_{xy}}{\partial x}$$

이 thrust 가 bottom·lateral shear stress 와 균형을 이루며(Longuet-Higgins 1970), longshore current 와 그에 따른 littoral drift 의 직접 driver 이다 (`water-wave-mechanics`, p.309). $S_{xy}$ 자체의 정의·유도는 [`02-theory.md §2`](02-theory.md) 참조.

→ 즉 longshore transport 산정은 원리적으로 surf zone 전 폭에 걸친 $F_y$ 적분 문제이지만, 실무에서는 아래 §2 의 단면 적분 empirical 공식으로 우회한다.

## 2. 단면 적분 transport rate 공식

연안표사 산정의 1차 대상은 surf zone 전 폭에 걸쳐 적분한 **총 longshore sediment transport rate $Q_{LS}$** (단위: m³/s, pore space 제외 순 sediment 부피; `marine-sands-manual`, p.198 §10.5).

### 2.1 CERC 공식 (Shore Protection Manual 1984)

가장 널리 쓰이는 방법. 원식은 SPM(CERC, 1984)에 US 단위로 주어졌고, group velocity 를 $c_g = (gh)^{1/2}$, breaking 기준을 $H_{bk}=0.8h$, $H_s=\sqrt{2}H_{rms}$ 로 두어 dimensionally-consistent 단순형으로 변환하면 (`marine-sands-manual`, p.198 §10.5 Eq (138)):

$$Q_{LS} = 0.023\, g^{1/2}\, H_{sb}^{5/2}\, \sin(2\alpha_b)$$

- $Q_{LS}$ = surf zone 적분 transport rate (m³/s, pore space 제외)
- $H_{sb}$ = breaker line 의 significant wave height
- $\alpha_b$ = breaker line 에서 wave crest 와 shoreline 사이 각
- $s$ = sediment relative density (입력 인자로 명시되나, 위 단순형은 $s$ 가 흡수된 형태로 leading 계수 0.023 에 포함됨; 원 full 식과의 관계는 `marine-sands-manual` p.198)

(*주의*: 위 식은 OCR 본문에서 수식 본체가 깨져 있어, Soulsby 가 명시한 입력 변수 $g, H_{sb}, \alpha_b, s$ + leading 계수 0.023 + shallow-water linear theory 가정으로부터 재구성한 표준형이다. 본문은 "coefficient 0.023" 과 입력 변수 목록을 직접 진술 (`marine-sands-manual`, p.198). 정확한 지수·계수 대조가 필요하면 SPM 1984 원문 또는 Fredsøe & Deigaard 1992 와 재대조 권장 — 이 부분만 `source-needed` 강등 가능.)

핵심 특성 (`marine-sands-manual`, p.198 §10.5):

- shallow-water linear wave theory 를 full 식에 적용한 **가장 단순한** 형태
- **입경(grain size)·해빈경사(beach slope) 에 독립** — 이것이 한계이자 단순함의 원천

### 2.2 CERC 계수 calibration·적용 한계

leading 계수 0.023 은 입경 약 0.6 mm 미만 sandy beach 의 longshore transport 자료로 보정된 것으로, 이 영역 transport 의 상당 부분이 **suspended load** 다 (`marine-sands-manual`, p.199 §10.5). 따라서:

- 굵은 입자(shingle 등, 주로 bedload) 에 표준 CERC 를 그대로 쓰면 관측 대비 **약 20배 과대평가** (Brampton & Motyka 1984; `marine-sands-manual`, p.199)
- 대응: (a) CERC 재보정, (b) 수정판 사용, (c) 굵은 입자 전용 공식 사용

→ CERC 의 장점은 **suspended load 포함 + 단순함**, 단점은 **입경·경사·주기 미반영** (`marine-sands-manual`, p.199-200).

### 2.3 수정·확장 — 입경·경사·주기 의존 (Kamphuis 1991 외)

Soulsby 는 Eq (138) 에 다음을 반영하기 위한 수정판들을 인용한다 (`marine-sands-manual`, p.198 §10.5):

- **입경 의존**: 계수 0.023 이 grain size 의 감소함수가 됨
- **해빈경사 의존**: 계수가 beach slope 증가에 따라 증가
- 고차 wave theory 반영
- alongshore wave-height 변동 (큰 파고 → 작은 파고 영역으로 표사 driving)

이 수정 계열의 대표가 **Kamphuis (1991)** "Alongshore sediment transport rate", *J. Waterway Port Coastal & Ocean Eng.* 117(6):624-640 (`marine-sands-manual`, p.198 인용; reference p.207 region) 으로, **입경 $D_{50}$·해빈경사 $\tan\beta$·파주기 $T_p$** 의존성을 명시적으로 도입한다. (Ozasa & Brampton 1980 은 alongshore wave-height gradient 항 추가; `marine-sands-manual`, p.198.)

> Kamphuis(1991) 공식 본체(지수·계수)는 본 위키 보유 교과서가 식 전체를 싣지 않으므로 본 노트는 **의존 변수까지만 verified**(Soulsby 인용 기준), 식 본체는 원논문 인용 필요 → `source-needed`. [`04-code-and-tools.md`](04-code-and-tools.md) 의 모델(예: GENESIS) 계열이 Kamphuis 옵션을 제공하면 그 구현으로 cross-check.

### 2.4 Damgaard & Soulsby (1997) — bedload(shingle) 물리 기반 공식

CERC 의 굵은입자 과대평가를 보완하기 위한 **physics-based bedload** longshore 공식. surf zone radiation stress gradient 로부터 mean bed shear-stress 를, wave orbital velocity 로부터 oscillatory bed shear-stress 를 계산해 Soulsby 의 combined wave+current bedload 식에 직접 대입하는 방식이며, longshore current 분포를 따로 계산하지 않는다 (`marine-sands-manual`, p.199 §10.5). 식은 두 후보의 최댓값으로 주어진다 (`marine-sands-manual`, p.199-200 Eq (139a)-(139e)):

$$Q_{LS} = \max(Q_{LS1},\, Q_{LS2})$$

각 항은 threshold Shields parameter $\theta_{cr}$, breaker height $H_b$, wave period $T$, 중앙입경 $D_{50}$, 해빈경사 $\tan\beta$, breaker angle $\alpha_b$ 에 의존하며, $\theta_{cr}$ 초과 여부로 분기한다 ($\theta_{cr}<1$ 일 때만 활성; `marine-sands-manual`, p.199-200 Eq (139a),(139c) 및 부속 정의). 함수형 보조항 예:

$$f(\alpha_b) = (0.95 - 0.19\cos 2\alpha_b)\,\sin 2\alpha_b$$

(`marine-sands-manual`, p.200·p.202 Example). 이 공식은 입경·경사·주기 의존성을 가져 CERC 보다 적용 범위가 넓지만, CERC 와 달리 **suspended load 를 포함하지 않는다** (`marine-sands-manual`, p.200).

### 2.5 공식 선택 가이드 (Soulsby 권고)

(`marine-sands-manual`, p.201 §10.5):

| 입경 | 권장 공식 | 대표 wave 입력 |
|---|---|---|
| 세립 (< ~0.5 mm, suspended+bedload) | **CERC** Eq (138) | significant wave height $H_s$ |
| 조립 (> ~0.5 mm, 주로 bedload) | **Damgaard & Soulsby** Eq (139) | $H_b=H_{rms}=H_s/\sqrt2$, $T=T_p$ |

적용 제한 (둘 다): longshore current 의 20% 초과 tidal current 가 있거나, 해빈이 뚜렷이 비평면이거나, 입경이 zone 별로 다르면(예: 상부 shingle + 하부 sand) 위 단면 적분식 대신 cross-shore 분포를 푸는 **coastal profile numerical model** 사용 권장 (`marine-sands-manual`, p.203 §10.5).

### 2.6 검증 예제 (Example 10.3) — 두 공식 정량 비교

Soulsby Example 10.3 (shingle beach, `marine-sands-manual`, p.201-203):

- 입력: $D_{50}=0.5$ mm 부근, 수온 15 °C, breaker angle $\alpha_b=20°$($\beta=2.86°$), $T_p=6$ s, $\tan\beta=1/10$
- 중간값: $H_b=H_{rms}=0.707$ m, mean Shields $\theta_m=0.153$, wave Shields $\theta_w=0.169$, $f(\alpha_b)=0.264$
- Damgaard-Soulsby 결과: $Q_{LS2}=6.98\times10^{-4}$ m³/s → pore space 포함 부피로 환산 (porosity 0.40):

$$\frac{0.00698 \times 3600\times24\times365}{1-0.40} \approx 36{,}700\ \text{m}^3/\text{yr}$$

- **동일 입력에 CERC** Eq (138) 적용 시: $Q_{LS}=0.0156$ m³/s ≈ **819,410 m³/yr**

→ shingle 조건에서 CERC 가 Damgaard-Soulsby 대비 **약 22배 과대평가** (`marine-sands-manual`, p.203 §10.5). §2.2 의 "굵은입자 ~20배 과대" 진술의 정량 확인이며, 공식 선택의 실무적 중요성을 보여준다.

## 3. Sediment budget — 표사수지 (control volume)

공간적으로 변하는 $Q_{LS}$ 가 해안선 전·후퇴를 만든다. shoreline 을 따라 격자 셀을 두고 각 셀에서 **transport in − transport out** 의 표사수지를 계산하는 것이 budget 분석의 핵심 (`marine-sands-manual`, p.207-208 §11.1).

$$\frac{\partial V_{\text{cell}}}{\partial t} = Q_{LS,\text{in}} - Q_{LS,\text{out}} + \sum(\text{sources} - \text{sinks})$$

- 좌변: 셀 내 sediment 부피 변화율 → 해안선 advance/recession 으로 환산
- $Q_{LS}$ 항: §2 공식으로 격자점마다 산정 (`marine-sands-manual`, p.207)
- sources/sinks: 하천 공급, cliff erosion, 양빈(nourishment) = source; dune 퇴적, headland·harbor trap = sink ([`01-concept.md §7`](01-concept.md) 참조)

특히 groyne·harbor entrance·river training wall 같은 cross-shore 구조물이 longshore transport 를 가로막으면 **updrift 측 퇴적 / downdrift 측 침식** 이 발생한다 (`marine-sands-manual`, p.197 §10.5). 이 비대칭이 sediment budget 의 가장 흔한 실무 진단 대상이다.

## 4. One-line shoreline 변화식 (beach planshape model)

§3 의 cell 단위 budget 을 연속 해안선에 시계열로 적용한 것이 **beach planshape model = one-line model** 이다. Soulsby 의 분류 (`marine-sands-manual`, p.207 §11.1):

> Beach planshape models — 수년~수십 년 규모로 해안선(예: 평균 정수면선)의 위치·형상 변화를 계산. 장기 파고·파향 시계열을 입력해 deep water 에서 breaker line 까지 굴절시키고, 격자점마다 **CERC 같은 longshore transport 공식**을 구동.

절차 (`marine-sands-manual`, p.207-208 §11.1):

1. 장기 wave 시계열(파고·파향)을 deep water → breaker line 으로 굴절
2. 격자점마다 §2 공식으로 $Q_{LS}$ 산정
3. 각 time step 에서 격자 셀 사이의 sediment budget(in − out)으로 해안선 recession/advance 계산
4. 갱신된 planshape 로 반복 (전 시계열 동안)

→ 즉 one-line 모델은 **"longshore transport 공식 + cell budget(연속식)"의 시간 적분**이다. 개념적으로 sediment 연속식:

$$\frac{\partial y_s}{\partial t} = -\frac{1}{d_c}\frac{\partial Q_{LS}}{\partial x} + (\text{source/sink})$$

($y_s$ = 해안선 위치, $d_c$ = active profile 의 닫힘수심 region; 위 budget 형의 미분 표현. Soulsby 는 cell 차분 narrative 로 기술; `marine-sands-manual`, p.207-208).

확장(`marine-sands-manual`, p.208 §11.1): 더 정교한 transport 공식, surf zone 전폭 분포, 단일선 대신 multi-line 사용. 더 강한 cross-shore 거동(breaker bar 등)이 필요하면 **coastal profile model**(cross-shore 단면 budget) 로, 더 일반적이면 coastal area model 로 단계 상승 (`marine-sands-manual`, p.208).

## 5. 산정 chain 요약

$$\underbrace{F_y=-\partial S_{xy}/\partial x}_{\text{driver, Dean-Dalrymple §10.5}} \;\Rightarrow\; \underbrace{Q_{LS}=0.023\,g^{1/2}H_{sb}^{5/2}\sin 2\alpha_b}_{\text{CERC §10.5 / Kamphuis·Damgaard-Soulsby 수정}} \;\Rightarrow\; \underbrace{\partial V_{\text{cell}}/\partial t = Q_{in}-Q_{out}+\text{src/sink}}_{\text{sediment budget §11.1}} \;\Rightarrow\; \underbrace{\partial y_s/\partial t}_{\text{one-line shoreline §11.1}}$$

## 6. 인용 정형

핵심 인용 (page 는 textbook/md `---PAGE-NN---` 직접 확인):

- Longshore wave thrust $F_y=-\partial S_{xy}/\partial x$ — `water-wave-mechanics`, p.309 §10.5 Eq (10.37) (Example 10.2)
- CERC 공식 $Q_{LS}=0.023\,g^{1/2}H_{sb}^{5/2}\sin 2\alpha_b$, 계수 0.023, 입력 $H_{sb}·\alpha_b·s$ — `marine-sands-manual`, p.198 §10.5 Eq (138)
- CERC 입경/경사 독립·계수 0.023 의 grain-size 감소함수화·경사 의존 수정 (Kamphuis 1991, Ozasa-Brampton 1980) — `marine-sands-manual`, p.198 §10.5
- CERC 계수 보정(<0.6 mm, suspended)·shingle 20배 과대 — `marine-sands-manual`, p.199 §10.5
- Damgaard & Soulsby (1997) bedload 공식 $Q_{LS}=\max(Q_{LS1},Q_{LS2})$, $f(\alpha_b)=(0.95-0.19\cos2\alpha_b)\sin2\alpha_b$ — `marine-sands-manual`, p.199-200 §10.5 Eq (139a)-(139e)
- 공식 선택 가이드 (세립 CERC / 조립 Damgaard-Soulsby) + tidal current·비평면 제한 — `marine-sands-manual`, p.201·203 §10.5
- Example 10.3: shingle $Q_{LS}=36{,}700$ m³/yr vs CERC $819{,}410$ m³/yr (~22배) — `marine-sands-manual`, p.201-203 §10.5
- sediment budget cell(in−out) + groyne updrift 퇴적/downdrift 침식 — `marine-sands-manual`, p.197·207-208 §10.5·§11.1
- beach planshape(one-line) 모델 절차 + coastal profile/area 모델 위계 — `marine-sands-manual`, p.207-208 §11.1

## 7. 관련 문헌

### Textbook (PDF 보유)
- **Soulsby, R.L.** *Dynamics of Marine Sands — a Manual for Practical Applications*, §10.5 Longshore transport (p.193-204) + §11.1 Coastal sediment transport models (p.205-208) (`marine-sands-manual`)
- **Dean, R.G. & Dalrymple, R.A.** *Water Wave Mechanics for Engineers and Scientists*, §10.5 (p.309, longshore wave thrust) (`water-wave-mechanics`)

### 외부 paper (PDF 미보유 — 식 본체는 원논문 인용 필요)
- **CERC** (1984) *Shore Protection Manual*, U.S. Army Corps of Engineers (Soulsby 가 CERC 공식 원전으로 인용)
- **Kamphuis, J.W.** (1991) "Alongshore sediment transport rate" *J. Waterway Port Coastal & Ocean Eng.* 117(6):624-640 (입경·경사·주기 의존; `source-needed` — 식 본체)
- **Ozasa, H. & Brampton, A.H.** (1980) — alongshore wave-height gradient 항
- **Damgaard, J.S. & Soulsby, R.L.** (1997) "Longshore bed-load transport" *Proc. 25th ICCE* 3:3614-3627
- **Fredsøe, J. & Deigaard, R.** (1992) *Mechanics of Coastal Sediment Transport* (CERC dimensionally-consistent 변환 reference)

## 8. 연결

- [`01-concept.md`](01-concept.md) — 정의·CERC/Komar-Inman 정형·sediment budget 개요·한국 사례
- [`02-theory.md`](02-theory.md) — radiation stress $S_{xy}$ 유도 + longshore current(Bowen 1969/Battjes 1974)
- [`04-code-and-tools.md`](04-code-and-tools.md) — GENESIS/UNIBEST-LT one-line·XBeach process-based 구현 (위 공식의 코드화)
- [`concepts/sediment-transport/01-concept.md`](../sediment-transport/01-concept.md) — bedload/suspended 일반 + Shields parameter $\theta_{cr}$ (Damgaard-Soulsby 입력)
