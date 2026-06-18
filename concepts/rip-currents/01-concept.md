---
title: "이안류 (Rip Currents) — 정의·위험·유형 + CV 자동 탐지 벤치마크"
topic: rip-currents
canonical_source: self
citation_status: source-needed
verification_method: "신규 토픽 (2026-06-18). §4 CV 탐지 벤치마크 4편 = **arxiv full PDF 직접 read(pdftotext) verified**: RipVIS(2504.01128, 18p)·YOLOv8 baseline(2504.02558, 11p)·RipSeg AIM2025(2508.13401, 10p)·RipDetSeg NTIRE2026(2604.17070, 12p) — 데이터셋 규모·방법·지표 본문 인용. §1-3 정의·위험·시각signature 는 해당 논문 intro 인용(verified-from-paper); **형성 mechanism·유형 taxonomy 정량은 교과서(MacMahan-Reniers 2006·Dalrymple 2011 Annu. Rev. Fluid Mech.) page 미보유 source-needed**. 실제 읽은 abstract/intro/dataset 절만 인용."
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

- **강하고 국소적이며 좁은(strong, localized, narrow) 바다 방향 흐름** — 쇄파로 해안에 쌓인 물의 보상류(return flow) (RipVIS abstract, [2504.01128](https://arxiv.org/abs/2504.01128); NTIRE RipDetSeg intro, [2604.17070](https://arxiv.org/abs/2604.17070): "strong, narrow seaward flows that transport water away from the shoreline").
- 발생 지배요인 = **nearshore hydrodynamics + underwater morphology(해저지형)** (YOLOv8 baseline intro, [2504.02558](https://arxiv.org/abs/2504.02558); RipDetSeg: "behavior governed by local hydrodynamics, seabed morphology").
- ocean·sea·large lake 연안 모두 발생 (2504.02558·2604.17070 intro).

## 2. 위험성

- **surf beach 사망사고의 최대 원인** — "Rip currents are the leading cause of fatal accidents" (YOLOv8 baseline, 2504.02558 intro). 흔한 life-threatening 위험.
- 속도 **8.7 km/h 초과 가능 — Olympic 수영선수보다 빠름** (RipDetSeg, 2604.17070:33-34) → 수영자를 빠르게 외해로 이송.
- 위험의 핵심 = 단순 유속만이 아니라 visual 식별 곤란성(RipVIS §intro) → 조기 경보·자동 탐지 필요.

## 3. 유형·시각 signature

- **시각 식별**: 교란된 wave-breaking 패턴, sediment transport(탁한 물기둥), deflection rip, 물색 변화 (RipVIS, 2504.01128 Fig.1 캡션·본문).
- 유형: bathymetric(channel)·deflection·structure-controlled 등 — ⚠ 정식 taxonomy(MacMahan-Reniers-Thornton 2006 review·Dalrymple-MacMahan-Reniers-Nelko 2011 Annu. Rev.) **source-needed**(교과서 page 미보유).
- 형성 mechanism(쇄파의 alongshore 변동 → 보상류): radiation stress 구배 → longshore current 수렴 → seaward rip ([[littoral-drift/02-theory]] longshore current 유도와 연계) — 정량 유도 source-needed.

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
