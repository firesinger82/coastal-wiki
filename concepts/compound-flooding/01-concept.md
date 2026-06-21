---
title: "복합침수 (Compound Flooding) — 정의·인자·메커니즘·위험"
topic: compound-flooding
canonical_source: self
citation_status: verified
has_source_needed: true
verification_method: "정의·5 forcing = SFINCS 공식 docs overview.rst (models/SFINCS/raw/source_code/sfincs/docs/overview.rst) 직접 read, line 35-36·44·127-128 인용 (readthedocs overview.html 동일 본문). 인자 분류·hazard = textbook page 본문 grep+Read 후 인용: [coastal-eng-intro-wijetunge] PAGE-7·22·23·24 (Wijetunge §1·§5 coastal hazards: cyclone surge·tsunami·SLR·erosion), [sea-level] PAGE-24·25·26·198·200·270 (Pugh Ch1/6/7: surge-tide 동시발생 → exceptional high total level, §7:8 tide-surge interaction 본문), [coastal-structures-design] PAGE-16·17·24 (wave run-up·overtopping 설계 프로세스). 복합 메커니즘(surge+tide 비선형 상호작용) = [sea-level] PAGE-270 본문 (TS interaction term·bottom friction) 직접 인용. 모델 cross-link = models/SFINCS/source-analysis/sfincs_boundaries_forcing.md 실재·forcing 커버리지 확인 후 link. 한국 연안도시 정량은 미확보 → source-needed 명시."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - concepts/compound-flooding/README.md
  - concepts/storm-surge/01-concept.md
  - concepts/compound-flooding/06-model-application.md
---

# 복합침수 (Compound Flooding) — 정의·인자·메커니즘·위험

## 1. 정의

**복합침수(compound flooding)**는 연안역에서 **여러 침수 인자가 동시에 발생하거나 상호작용하여 (극한) 침수를 일으키는 사건**으로 정의된다. SFINCS 공식 문서는 이를 Wahl et al. (2015)을 인용하며 "the interaction of high sea levels, large river discharges and local precipitation causes (extreme) flooding"으로 기술한다(고조위·하천유량·국지강우의 상호작용).[^sfincs-def]

핵심은 **개별 인자의 단순 합산을 초과하는 위험 증폭**이다. 즉 여러 driver가 같은 시점·같은 장소에 겹칠 때, 또는 한 인자가 다른 인자의 배수를 막아 침수가 가중될 때 복합침수가 성립한다(§3). 따라서 복합침수를 모의하려면 모델이 모든 관련 외력을 동시에 다룰 수 있어야 하며, SFINCS는 이 목적에서 **fluvial(하천)·pluvial(강우)·tidal(조석)·wind(바람)·wave(파) 5종 forcing**을 포함한다.[^sfincs-forcing]

## 2. 침수 인자 분류

복합침수의 driver는 발생 출처에 따라 세 계열로 분류된다.

| 계열 | 인자 | 구성 process | 근거 |
|---|---|---|---|
| **연안(coastal)** | 조석(tidal) + 폭풍해일(surge) + 파(wave) | 천문조 + 기상해일(wind setup·기압) + 파 setup/runup/overtopping | [^wij-hazard][^sea-surge][^design-overtop] |
| **강우(pluvial)** | 국지강우 내수 | 직접 강우 유출·배수 한계 초과 | [^sfincs-forcing] |
| **하천(fluvial)** | 하천유량 | 상류 유출 → 하구 수위 상승 | [^sfincs-forcing] |

### 2.1 연안 인자

Wijetunge는 연안 재해를 tsunami·storm surge·sea level rise·coastal erosion으로 분류하고, 그중 **cyclone-induced sea surge**와 **지진성 tsunami**가 연안 침수(coastal flooding)를 일으키는 극한 사건임을 명시한다.[^wij-hazard] 실제로 연안 공학 개입의 목적에는 "to protect onshore developments against coastal flooding due to tsunami and storm surges"가 포함된다.[^wij-hazard2] 폭풍해일은 강풍이 얕은 바다 위로 장시간 불 때 가장 크게 발달한다(Pugh).[^sea-surge2]

파 성분은 정적 수위가 아니라 **구조물·사면에서의 동적 처오름**으로 침수에 기여한다. 설계 관점에서 파는 wave run-up($R_{u2\%}$), wave overtopping($q$ 평균월류량, $V_{max}$ 개별 월류 체적)으로 정량화되며, 처오르는 파가 마루(crest)에 도달하면 구조물을 월류한다.[^design-overtop] (개념 상세는 [[../waves/01-concept]]·[[../swash-zone/01-concept]] 참조.)

### 2.2 강우·하천 인자

SFINCS 문서는 도시(urban)·하천(riverine) 모델 맥락에서 강우와 하천유량의 역할을 구분한다. urban 모델에서는 강우의 일부가 침투/유출로 나뉘며(curve number 방식), riverine 모델에서는 상류 discharge에 더해 하천에 떨어지는 국지강우가 매우 중요할 수 있다고 기술한다.[^sfincs-urban] 본 위키 모델 분석에서 이들 forcing의 코드 구현(조석 성분·discharge·meteo·강우)은 [[../../models/SFINCS/source-analysis/sfincs_boundaries_forcing]]에 정리되어 있다.

## 3. 복합 메커니즘 — 왜 합산을 초과하는가

복합침수가 단순 합산보다 위험한 핵심 메커니즘은 **인자 간 상호작용(interaction)**이다.

### 3.1 동시발생(co-occurrence)에 의한 총수위 극대화

해일과 고조위가 시간적으로 겹치면 총수위가 비정상적으로 높아진다. Pugh는 1982년 1월 Cromer에서 spring tide와 기상기인 수위 상승이 겹쳐 "exceptionally high total level"이 발생한 사례를 든다.[^sea-coincide] 역사적으로도 대형 기상해일과 큰(혹은 중간 이상의) 조석의 동시발생이 재난적 연안 침수를 반복적으로 야기했으며, 1953년 북해 surge는 spring tide보다 약간 낮은 조석과 겹쳤음에도 영국·네덜란드 해안에서 catastrophic flooding을 일으켰다(완전한 spring tide와 겹쳤다면 피해가 더 컸을 것).[^sea-coincide2]

### 3.2 비선형 tide-surge interaction

조석과 해일의 합은 단순 선형 합이 아니다. Pugh는 총수위 분해에서 **TS 항(tide-surge interaction)**이 조석과 해일의 상호작용을 나타내며, 이는 해석모델로 기술하기 어렵고 수치모델로 계산하는 것이 최선이라고 기술한다.[^sea-ts] 천해역에서 가장 뚜렷하며(남부 북해·템스강), 주된 인자는 **유속의 제곱에 비례하는 바닥마찰**이다.[^sea-ts] 이 상호작용 때문에 큰 양(+)의 surge peak는 조석 만조 시점을 회피하여(만조 직전 상승조에 발생하기 쉬움), joint-probability 통계에서 100년 빈도 수위가 (독립 가정 대비) 조정된다.[^sea-ts2]

개념도식으로 총수위를 다음과 같이 표현할 수 있다(선형 분해 + 상호작용항):

$$
\eta_{\text{total}}(t) = \eta_{\text{tide}}(t) + \eta_{\text{surge}}(t) + \underbrace{TS(t)}_{\text{interaction}}
$$

여기서 $TS$ 항이 0이 아니라는 점이 복합침수의 비선형성 근거다.[^sea-ts]

### 3.3 배수 차단(drainage blocking)

해일·고조위가 하천 하구·배수구 수위를 끌어올리면 내륙의 배수·하천 유출이 막혀(아류계 sub-critical 흐름에서 하류 수위가 상류에 영향), 강우 내수와 하천유량이 갈 곳을 잃고 내수 범람이 가중된다. SFINCS 문서는 riverine 모델에서 하류단 수위 시계열이 sub-critical 조건일 때 상류 흐름에 영향을 준다고 명시하며, compound flooding 모델에서는 "joint effect of multiple flood drivers that can enhance flooding"을 함께 고려할 수 있다고 기술한다.[^sfincs-river][^sfincs-compound]

> 메커니즘 요약: (a) 동시발생으로 총수위 극대화, (b) tide-surge 비선형 상호작용($TS$ 항), (c) 해일이 하천/배수 하구 수위를 높여 내수·하천 배수를 차단 → 세 경로가 결합해 단일 인자 합산을 초과하는 침수를 만든다.

## 4. 위험·연계

- **인명·재산 피해**: 열대저기압 등 극한 사건에서의 복합침수는 막대한 재산 피해와 인명 손실을 야기한다(SFINCS 문서).[^sfincs-why] Pugh는 저지대·고밀도 지역(예: 벵골만 북부 Ganges 삼각주)에서 해일 침수가 최대 규모의 인적 재난으로 이어질 수 있음을 지적한다.[^sea-disaster]
- **인자별 개념 연결**:
  - 해일 driver → [[../storm-surge/01-concept]] (정의·결정 인자·한국 영향)
  - 파 overtopping/setup → [[../waves/01-concept]]
  - 처오름(runup) 범람 → [[../swash-zone/01-concept]]
- **모델 적용**: full-physics → reduced-complexity(SFINCS·LISFLOOD-FP) → ML emulator 스펙트럼은 [[06-model-application]](작성 예정) 허브 참조. SFINCS forcing 구현은 [[../../models/SFINCS/source-analysis/sfincs_boundaries_forcing]].

### 4.1 한국 연안도시 — source-needed

한국 연안도시(부산·인천 등)의 복합침수 정량(빈도·피해액·SLR 시나리오별 침수 면적)은 **현재 본 위키에 검수된 출처가 없다**. KHOA 이상조위 분석·지자체 침수 적응계획·해당 지역 침수 모델링 결과를 확보한 뒤 별도 노트(예: `05-examples.md` 또는 `experience/`)로 보강한다. 그 전까지 한국 정량 단언은 추가하지 않는다(citation_status: source-needed 대상).

---

## 출처

[^sfincs-def]: SFINCS 공식 docs, `overview.rst` line 35: "Compound flooding is described as events occurring in coastal areas where the interaction of high sea levels, large river discharges and local precipitation causes (extreme) flooding (Wahl et al., 2015)." — `models/SFINCS/raw/source_code/sfincs/docs/overview.rst` (readthedocs `overview.html` 동일 본문).
[^sfincs-forcing]: 同 line 36: "SFINCS includes fluvial, pluvial, tidal, wind- and wave-driven processes!" — `models/SFINCS/raw/source_code/sfincs/docs/overview.rst`.
[^wij-hazard]: Wijetunge, *An Introduction to Coastal Engineering*, [coastal-eng-intro-wijetunge] PAGE-23: 연안 재해 분류(tsunami·storm surges·sea level rise·coastal erosion); PAGE-7: "extreme events capable of causing coastal flooding such as cyclone-induced sea surges and seismically-generated tsunami pose a threat...".
[^sea-surge]: Pugh, *Sea Level* (Tides, Surges and Mean Sea-Level), [sea-level] PAGE-198(§6 Storm Surges): "The total level can give rise to serious coastal flooding when severe storms acting on an area of shallow water produce high levels which coincide with high water on spring tides."
[^design-overtop]: *Design of Coastal Structures and Sea Defenses*, [coastal-structures-design] PAGE-16~17: wave impact·run-up·overtopping process(Figure 1) + 설계 파라미터 $R_{u2\%}$, $q$, $V_{max}$; PAGE-24(§2.4): mean wave overtopping은 governing 설계 파라미터, 개별 월류 체적은 2-parameter Weibull 분포.
[^wij-hazard2]: (병합) [coastal-eng-intro-wijetunge] PAGE-22: 연안 공학 개입 목적에 "to protect onshore developments against coastal flooding due to tsunami and storm surges" 포함.
[^sea-surge2]: [sea-level] PAGE-25: "The largest surges occur when hurricane winds blow for a long time over large expanses of shallow water."
[^sfincs-urban]: SFINCS docs, `overview.rst` line 98-104(Urban model): curve number 침투/유출 분리; line 90(Riverine model): "besides the general river discharge, local rainfall adding water to the river can be very relevant too." — `models/SFINCS/raw/source_code/sfincs/docs/overview.rst`.
[^sea-coincide]: [sea-level] PAGE-24: "On 29 January the coincidence of a spring tide and a large increase in the levels due to the weather has caused an exceptionally high total level."
[^sea-coincide2]: [sea-level] PAGE-25: "In January 1953 catastrophic flooding on both the English and Dutch coasts of the North Sea occurred... This surge, which exceeded 2.6 m at Southend, coincided with slightly less than average spring tides, otherwise even more damage would have occurred."; PAGE-24: "Historically there have been many disastrous coastal floodings caused by the coincidence of large meteorologically induced surges and large or even moderately high tides."
[^sea-ts]: [sea-level] PAGE-270(§7:8 Tide-surge interaction): "The TS term represents the interaction between tides and surges. In practice the interactions are difficult to describe in terms of analytical models, and the full details are best calculated by numerical models." / "Tide-surge interaction is very important because it is most apparent in shallow-water areas where large surges may be generated... the primary factor is the bottom friction, which increases as the square of the current speed."
[^sea-ts2]: [sea-level] PAGE-270: "tide-surge interaction causes large surges to avoid the times of tidal high water. Positive surges are most likely to occur on the rising tide." + joint-probability(독립 vs 조석 의존 통계)로 100년 빈도 수위 조정.
[^sfincs-river]: SFINCS docs, `overview.rst` line 89(Riverine model): "At the downstream end of rivers, water level time-series need to be specified, which in case of sub-critical flow conditions will influence the flow upstream." — `models/SFINCS/raw/source_code/sfincs/docs/overview.rst`.
[^sfincs-compound]: 同 line 127-128(Compound flooding model): "all relevant types of forcing... can be combined into 1 domain. Hereby the joint effect of multiple flood drivers that can enhance flooding can be taken into account."
[^sfincs-why]: 同 line 19(Why SFINCS?): "Compound flooding during tropical cyclones and other extreme events result in tremendous amounts of property damage and loss of life."
[^sea-disaster]: [sea-level] PAGE-198(§6): "Where the surrounding land is both low-lying and densely populated the inundations can result in human disasters of the greatest magnitude" (northern Bay of Bengal / Ganges 삼각주 예시).
