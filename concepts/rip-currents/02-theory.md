---
title: "이안류 형성 mechanism·유형 taxonomy — 물리 형성론"
topic: rip-currents
canonical_source: self
citation_status: verified
verification_method: "교과서 page 직접 확인 인용: (mechanics-of-sediment-transport, p.764·766 §16.2.5.2-16.2.5.3) 이안류 정의·setup 구배 형성 mechanism·Bowen-Inman·wave refraction별 nearshore circulation 3유형(Fig 16.24)·800m 규모; (stewart-physical-ocean, p.309-310 §17.4·p.325 §17.6) narrow swift seaward rip·수백 m 간격·feeder longshore channel·유속 의존(파고/빈도/onshore wind)·edge wave; (coastal-eng-guidelines, p.91 glossary) radiation stress가 longshore current·rip current 구동 + rip current 정의(surf-zone seaward). 미보유 정량(edge wave 공명파장·shear instability 분산식·flash rip)은 source-needed 명시."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - concepts/rip-currents/01-concept.md
  - concepts/rip-currents/README.md
  - concepts/waves/02-theory.md
  - concepts/littoral-drift/02-theory.md
---

# 이안류 형성 mechanism·유형 taxonomy (물리 형성론)

> [[01-concept]] 가 정의·위험·CV 자동탐지를 다룬다면, 본 노트는 **왜·어떻게 이안류가 생기는가**(형성 동역학)와 **유형 분류**를 교과서 인용으로 정리한다. 핵심 사슬: 쇄파의 **alongshore 변동 → wave setup 구배 → 보상류(return flow)가 한 곳으로 수렴 → seaward rip**.

## 1. 구동력: radiation stress → setup → 보상류

쇄파대(surf zone)의 흐름은 **radiation stress(파동 운동량 flux)** 가 구동한다. radiation stress 는 wave setdown·setup, surf-beat, longshore current, 그리고 **rip current** 를 모두 구동한다 (coastal-eng-guidelines, p.91 §glossary "RADIATION STRESS"). 이안류 자체는 글로서리에서 "**파에 의해 구동되는 surf-zone 의 바다 방향 흐름**(Seaward directed surf-zone currents driven by waves)"으로 정의된다 (coastal-eng-guidelines, p.91 §glossary "RIP CURRENTS").

쇄파로 인해 **해안 부근 평균수면이 외해 평균수면보다 상승(superelevation, wave setup)** 한다. 이 상승량은 파고에 비례 — **파고가 클수록 수위 상승이 크다** (mechanics-of-sediment-transport, p.766 §16.2.5.3). 핵심은 이 setup 이 해안선을 따라 균일하지 않다는 점이다:

> 외해 지형(offshore relief)이 복잡하면 수면 상승량이 해안선을 따라 일정하지 않다. 따라서 **파고가 큰 쇄파대 → 파고가 작은 쇄파대 방향으로** 흐름이 형성되고, 이 흐름이 한 곳으로 **수렴(concentrate)** 하여 **seaward flow** 를 만든다 (mechanics-of-sediment-transport, p.766 §16.2.5.3).

즉 형성 사슬은 다음과 같다 (mechanics-of-sediment-transport, p.766 §16.2.5.3):

```
alongshore 파고 변동  →  alongshore setup 구배(높은 setup ↔ 낮은 setup)
                     →  setup 높은 곳 → 낮은 곳 alongshore feeder 흐름
                     →  한 지점으로 수렴
                     →  좁고 강한 seaward rip current
```

Bowen, A. J. 와 Bowen & Inman 이 이 형성 mechanism 을 이론·실험 양면에서 상세히 설명했다 (mechanics-of-sediment-transport, p.766 §16.2.5.3; 원문 인용 ref [34] Bowen 1969 *J. Geophys. Res.* 74:5467-5478, ref [35] Bowen & Inman 1969 *J. Geophys. Res.* 74:5479-5490).

> ⚠ longshore current 와 rip current 는 **생성 mechanism 이 다르다**. 과거에는 longshore current 가 운반한 물이 rip 으로 되돌아간다고 연속(continuity) 관점에서 묶어 다뤘으나, 최근 연구는 **rip current 의 생성은 해안선을 따른 파고 변동(variation of wave height along the coastline)에 의존**함을 보였다 (mechanics-of-sediment-transport, p.764 §16.2.5.2). radiation stress 유도 longshore current 의 momentum 관점 유도는 [[../littoral-drift/02-theory]] 참조.

## 2. 셀 순환(cell circulation)과 feeder channel

Stewart 는 동일 사슬을 nearshore cell circulation 으로 기술한다. 쇄파대 안으로 들어온 물은 반드시 외해로 되돌아가야 하며, 그 경로는 (stewart-physical-ocean, p.309 §17.4):

1. 먼저 해안과 평행하게 **alongshore current(feeder)** 로 이동,
2. 이어 방향을 틀어 **해안과 직각으로 좁고 빠른(narrow, swift) rip current** 로 외해로 빠져나간다.

- rip 들은 보통 **수백 m 간격(hundreds of meters apart)** 으로 배치된다 (stewart-physical-ocean, p.309 §17.4, Fig 17.5).
- 보통 쇄파대와 해변 사이에 **더 깊은 물의 띠(band of deeper water)** 가 있고, longshore current(feeder)는 이 **channel** 을 따라 흐른다 (stewart-physical-ocean, p.309 §17.4) — 이것이 아래 3절의 **channel rip / bathymetric rip** 의 지형적 기반이다.

## 3. 유형 taxonomy — wave refraction 에 따른 nearshore circulation

Mechanics 는 nearshore current 패턴이 입사파 특성에 따라 변하며, 이는 **wave refraction(굴절)** 과 밀접함을 Fig 16.24 의 3 case 로 정리한다 (mechanics-of-sediment-transport, p.766 §16.2.5.3):

| case | 입사파 | refraction | 결과 흐름 패턴 |
|---|---|---|---|
| (a) | **단주기파 + 해안에 직각 입사** | 거의 굴절 안 됨 | rip 이 **다수이나 각각 작다**(more numerous but smaller) |
| (b) | **단주기파 + 큰 사각 입사** | — | **연속적 longshore current** 형성(rip 미발달) |
| (c) | **장주기파 + 사각 입사** | 에너지 집중 영역 소수 | 집중도 높은 소수 영역 → **더 강한 rip current**(stronger rips) |

이 패턴들은 wave refraction·reflection·diffraction 이 함께 결정하는 **nearshore 에너지 spectrum** 에 의해 좌우된다 (mechanics-of-sediment-transport, p.766 §16.2.5.3, ref [25][37]).

위 분류는 "구동 메커니즘(파고 변동의 원인)" 축의 분류이며, 실무에서 흔히 쓰는 유형명과 대응시키면:

- **bathymetric rip / channel rip** — 해저 channel·sandbar gap 등 **지형이 alongshore 파고 변동을 고정**시켜 setup 구배를 만드는 경우. Stewart 의 deeper-water channel feeder 구조(2절)·Mechanics case (a) 의 "지형 기인 setup 불균일"(p.766)이 이에 해당. 위치가 지형에 묶여 비교적 **고정·persistent**.
- **structure / boundary rip** — 방파제·groin 등 구조물 또는 headland 경계에서 흐름이 차단·집중되어 발생. radiation stress glossary 의 "파 구동 surf-zone seaward 흐름" 일반 정의에 포함되나, 본 위키 보유 교과서에 **구조물 rip 의 독립 정량 유도는 없음 → source-needed**.
- **flash rip(transient rip)** — 고정 지형 없이 surf zone 의 일시적 alongshore 변동(파군·shear)으로 단발적으로 나타나는 rip. 본 위키 보유 교과서 page 에 정식 정의/정량 **없음 → source-needed** (MacMahan-Reniers-Thornton 2006 review·Dalrymple et al. 2011 Annu. Rev. Fluid Mech. 격상 시 보강).

## 4. 유속 scale·규모

- **유속 의존성**: rip current 의 강도(strength)는 **쇄파의 파고·빈도(height and frequency of breaking waves)** 와 **onshore wind 의 세기**에 의존한다 (stewart-physical-ocean, p.310 §17.4). 즉 큰 파·강한 onshore wind 일수록 강한 rip → [[01-concept]] §2 의 "8.7 km/h 초과(올림픽 수영선수보다 빠름)" 위험 수치와 정합.
- **공간 규모**: rip 은 쇄파선(breaker line)을 통과한 뒤 **부채꼴(fan shape)** 로 퍼지며 점차 소멸하고, 길이는 **800 m 를 넘을 수 있다** (mechanics-of-sediment-transport, p.766 §16.2.5.3). 간격은 **수백 m**(stewart-physical-ocean, p.309 §17.4).
- **탈출 전략(역동학적 함의)**: feeder longshore current 에 실린 수영자가 rip 으로 외해로 끌려가므로, **rip 을 거슬러 헤엄치지 말고 해안과 평행하게 헤엄쳐 빠져나가라** — narrow 한 rip 폭 때문에 가능 (stewart-physical-ocean, p.310 §17.4).

## 5. edge wave·shear instability (관련 — 정량 source-needed)

쇄파대 흐름의 alongshore 주기성을 설명하는 두 메커니즘이 문헌에서 거론된다:

- **edge wave**: 해안에 trap 된 파로, 쇄파 구동 nearshore 흐름과 함께 거론된다. Stewart 는 chapter 요약에서 "쇄파가 longshore current·**rip current**·**edge wave** 를 포함한 nearshore current 를 구동한다"고 명시 (stewart-physical-ocean, p.325 §17.6). edge wave 의 **공명 파장이 rip 간격을 설정**한다는 Bowen-Inman 류의 정량 메커니즘은 본 위키 보유 교과서에 유도가 없음 → **source-needed**.
- **shear (longshore current) instability**: longshore current 의 전단 불안정으로 alongshore 변동·vortex 가 생겨 transient rip 으로 이어진다는 메커니즘 — 본 위키 보유 교과서 page 에 **정량 분산식 없음 → source-needed**.

## 6. 연결

- [[01-concept]] — 정의·위험·CV 자동탐지(RipVIS·RipSeg·RipDetSeg) (본 노트의 형성론과 상보)
- [[../waves/02-theory]] — radiation stress(이안류의 1차 구동력)·wave setup·쇄파 이론
- [[../littoral-drift/02-theory]] — radiation stress → longshore current 유도(feeder current 의 근간)
- 후속 격상 대상: MacMahan, Reniers & Thornton (2006) *Coast. Eng.* rip review / Dalrymple, MacMahan, Reniers & Nelko (2011) *Annu. Rev. Fluid Mech.* 43:551-581 / Bowen (1969)·Bowen & Inman (1969) 원논문 — edge wave 공명·flash rip·shear instability 정량 보강 시 §3·§5 source-needed 해소
