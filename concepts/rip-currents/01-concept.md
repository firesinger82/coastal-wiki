---
title: "이안류 (Rip Currents) — 정의·위험·유형 + CV 자동 탐지 벤치마크"
topic: rip-currents
canonical_source: self
citation_status: verified
verification_method: "신규 토픽 (2026-06-18). §1-3 정의·위험·유형/시각signature **textbook page 직접 read·인용 verified** (2026-06-18 보강): mechanics-of-sediment-transport p.766 §16.2.5.3(정의=concentrated offshore current·800m·fan shape, superelevation 구배 구동, Bowen·Inman, Fig.16.24 파 특성별 rip 패턴 변이) + stewart-physical-ocean p.309(rip=narrow swift seaward flow·수백m 간격·channel·세기 지배요인) + p.310(수영자 위험·해안평행 탈출법·edge wave 주기/파장/감쇠). 해당 page 본문 실제 확인 후 인용. §4 CV 탐지 벤치마크 4편 = arxiv full PDF 직접 read(pdftotext) verified: RipVIS(2504.01128,18p)·YOLOv8 baseline(2504.02558,11p)·RipSeg AIM2025(2508.13401,10p)·RipDetSeg NTIRE2026(2604.17070,12p). **잔존 source-needed**: 정량 유속 임계값(m/s), 정식 유형 taxonomy(MacMahan-Reniers 2006·Dalrymple 2011 Annu.Rev.) page 미보유, edge wave↔rip 간격 정량 연계, 한국 KHOA 운영(§5). radiation stress 형성 정량 유도는 02-theory 위임."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - concepts/rip-currents/README.md
  - concepts/waves/01-concept.md
  - concepts/currents/01-concept.md
  - concepts/littoral-drift/02-theory.md
---

# 이안류 (Rip Currents)

> 쇄파대에서 해안선과 거의 직각으로 **바다 쪽으로 빠져나가는 강하고 좁은 표층 흐름**. nearshore circulation 의 seaward return flow.

## 1. 정의

- **이안류 = 집중된 외해 방향 흐름(concentrated offshore current)**: "A rip current is a concentrated offshore current … After a rip current passes the line of breakers, it spreads out in a fan shape and gradually loses its identity. It can be more than 800 m long." (mechanics-of-sediment-transport p.766 §16.2.5.3, Fig.16.23). → 쇄파선을 지나면 부채꼴(fan shape)로 퍼지며 소멸, 길이 **800 m 초과 가능**.
- **쇄파대 물의 외해 귀환 경로**: 쇄파된 물(bore)이 해안에 쌓인 뒤 먼저 해안 평행(longshore current)으로 흐르다 직각으로 방향을 틀어 "a narrow, swift rip current"로 외해로 빠져나감 (stewart-physical-ocean p.309). 즉 nearshore circulation 의 seaward return flow.
- **구동 메커니즘 = 평균수위 superelevation 의 alongshore 불균일**: 쇄파로 해안 평균수위가 외해보다 상승하며, 이 superelevation 은 파고에 비례("the higher the waves, the greater the increase in water level"). 해저지형(offshore relief)이 복잡해 superelevation 이 해안선을 따라 불균일 → **고파(高波) breaker zone → 저파 breaker zone 으로 흐름이 형성·집중되어 seaward flow** 가 됨 (mechanics-of-sediment-transport p.766; Bowen·Inman 이론·실험 인용). → 발생 지배요인은 nearshore hydrodynamics(파고 변동) + underwater morphology(해저지형).
- **현대 정의 보강**: "strong, localized, narrow" 바다 방향 흐름 — 쇄파로 해안에 쌓인 물의 보상류 (RipVIS abstract, [2504.01128](https://arxiv.org/abs/2504.01128); NTIRE RipDetSeg intro, [2604.17070](https://arxiv.org/abs/2604.17070): "strong, narrow seaward flows that transport water away from the shoreline"; YOLOv8 baseline, [2504.02558](https://arxiv.org/abs/2504.02558): "governed by local hydrodynamics, seabed morphology").
- ocean·sea·large lake 연안 모두 발생 (2504.02558·2604.17070 intro).
- 형성 메커니즘 정량 유도(radiation stress 구배 → longshore 수렴 → seaward rip)는 [[02-theory]] 참조.

## 2. 위험성

- **수영자에게 직접적 위험** — "Rips are a danger to unwary swimmers, especially poor swimmers bobbing along in the waves inside the breaker zone. They are carried along by the along-shore current until they are suddenly carried out to sea by the rip." (stewart-physical-ocean p.310). 즉 longshore current 에 실려 가다 갑자기 rip 으로 외해로 끌려나감.
- **탈출법 = 해안 평행 수영**: "Swimming against the rip is futile, but swimmers can escape by swimming parallel to the beach." (stewart-physical-ocean p.310) — rip 에 맞서 헤엄치지 말고 해안과 평행하게 빠져나올 것.
- **세기 지배요인**: rip current 의 세기는 "the height and frequency of breaking waves and the strength of the onshore wind"에 의존 (stewart-physical-ocean p.309-310) → 고파·고풍 시 강화.
- **surf beach 사망사고의 최대 원인** — "Rip currents are the leading cause of fatal accidents" (YOLOv8 baseline, 2504.02558 intro).
- 속도 **8.7 km/h 초과 가능 — Olympic 수영선수보다 빠름** (RipDetSeg, 2604.17070:33-34) → 수영자를 빠르게 외해로 이송. ⚠ 정량 유속 임계값(예: 1–2 m/s)은 textbook page 미보유 source-needed.
- 위험의 핵심 = 단순 유속만이 아니라 visual 식별 곤란성(RipVIS §intro) → 조기 경보·자동 탐지 필요.

## 3. 유형·시각 signature

- **공간 간격(spacing)**: rip 은 보통 **수백 m 간격으로 배열**("usually spaced hundreds of meters apart", stewart-physical-ocean p.309). breaker zone 과 해안 사이에 깊은 수로(channel)가 있고 longshore current 가 이 channel 을 따라 흐름.
- **파 특성에 따른 패턴 변이** (mechanics-of-sediment-transport p.766, Fig.16.24 — Bowen·Inman):
  - 단주기파 + 해안 직각 입사 → 굴절 거의 없음 → **rip 이 다수이나 작음**(numerous but smaller).
  - 단주기파 + 큰 사각 입사 → **연속 longshore current** 형성.
  - 장주기파 + 사각 입사 → wave energy 집중부가 적게 형성 → **더 강한 rip**(stronger rip).
  - → rip 의 수·세기·배열은 wave refraction(+reflection·diffraction)으로 결정되는 nearshore energy spectrum 에 좌우됨 (p.766).
- **시각 식별**: 교란된 wave-breaking 패턴, sediment transport(탁한 물기둥), deflection rip, 물색 변화 (RipVIS, 2504.01128 Fig.1 캡션·본문). + 쇄파선 통과 후 부채꼴 확산(fan shape, mechanics-of-sediment-transport p.766).
- **edge wave 연계**: 도래파 wave energy 변동(원거리 storm 의 wave group)이 breaker 높이의 minute-단위 변동을 만들고, 이것이 longshore current 의 저주파 변동을 구동 → 해안에 갇힌 저주파 파인 **edge wave**(주기 수 분, alongshore 파장 ~1 km, 외해로 지수 감쇠 진폭)를 발생시킴 (stewart-physical-ocean p.310). edge wave 의 alongshore 정상파 구조는 rip 간격의 규칙성과 관련됨(정량 연계는 source-needed).
- 유형: bathymetric(channel)·deflection·structure-controlled 등 — ⚠ 정식 taxonomy(MacMahan-Reniers-Thornton 2006 review·Dalrymple-MacMahan-Reniers-Nelko 2011 Annu. Rev.) **source-needed**(교과서 page 미보유).
- 형성 mechanism(쇄파의 alongshore 변동 → 보상류): superelevation 구배 → 흐름 수렴 → seaward rip — 정량 유도(radiation stress)는 [[02-theory]] · [[../littoral-drift/02-theory]] longshore current 유도 참조.

## 4. CV 자동 탐지·세그멘테이션 벤치마크 (full PDF verified, 2026-06-18)

이안류는 visual 외형이 beach·viewpoint·sea state 별로 크게 변해 자동 탐지가 어려움 → 최근 딥러닝 benchmark 경쟁이 형성됨.

### 4.1 RipVIS — Video Instance Segmentation 벤치마크 (Dumitriu et al. 2025)

arxiv:[2504.01128](https://arxiv.org/abs/2504.01128) (18p, CVPR 2025 계열). **현존 최대 규모** rip current 데이터셋:
- **184 videos (212,328 frames)** — 그 중 **150 videos (163,528 frames)에 이안류 annotation** + 34 videos (48,800 frames) 이안류 없음 (2504.01128 본문 :36-46).
- 위치·유형·고도·viewpoint 다양성. YOLO11 fine-tuning + 신규 post-processing step. <https://ripvis.ai>.
- Video instance segmentation(시간축 instance 추적)로 still-image 한계 극복.

### 4.2 YOLOv8 instance segmentation baseline (2025)

arxiv:[2504.02558](https://arxiv.org/abs/2504.02558) (11p). bounding box(YOLO-Rip)를 넘어 **instance segmentation** 과제 정식화:
- 신규 데이터셋 **2,466 images** (기존 de Silva et al. 1,740 images 대비 확장, :49).
- bounding box 가 이안류 일부를 누락하거나 주변 noise 포함하는 한계 → segmentation mask 로 개선 (Fig.1).

### 4.3 RipSeg — AIM 2025 Challenge (2508.13401)

arxiv:[2508.13401](https://arxiv.org/abs/2508.13401) (10p). RipVIS 기반 **still-image 세그멘테이션 챌린지**. 평가 = **F1·F2·AP50 합성 score**. 다양 조건 하 성능 비교.

### 4.4 RipDetSeg — NTIRE 2026 Challenge (2604.17070)

arxiv:[2604.17070](https://arxiv.org/abs/2604.17070) (12p). RipVIS 기반 **detection + segmentation 동시** 챌린지(NTIRE 2026 워크숍). 탐지·세그 양쪽 평가.

> 계보: **RipVIS(데이터셋·VIS)** → **RipSeg(AIM2025 still-image)** → **RipDetSeg(NTIRE2026 det+seg)** — 동일 RipVIS 벤치마크 위 challenge 진화. + YOLOv8 baseline 이 instance-seg 정식화.

## 5. 한국 적용 (탐색)

- 한국 해수욕장 이안류 사고 빈발(해운대·대천 등) — KHOA 이안류 지수·CCTV 기반 탐지 운영 중(공식 발표). 위 CV 벤치마크는 한국 CCTV 이안류 자동탐지에 직접 전이가치. ⚠ 한국 데이터·운영 연계는 source-needed.

## 6. 연결

- [[../waves/01-concept]] — 쇄파·radiation stress(이안류 구동)
- [[../currents/01-concept]] — nearshore 흐름
- [[../littoral-drift/02-theory]] — radiation stress → longshore current(이안류 형성 관련)
- 후속: 형성 mechanism deep(02-theory, MacMahan 2006 textbook 인용 시) · 한국 KHOA 이안류 운영(05-examples)
