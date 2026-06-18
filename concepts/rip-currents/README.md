# concepts/rip-currents — 이안류 (Rip Currents)

> 쇄파대에서 해안선과 직각으로 **바다 쪽으로 강하게 빠져나가는 좁은 표층 흐름**. surf beach 익사사고의 최대 원인이며, 최근 컴퓨터비전 기반 자동 탐지·세그멘테이션 연구가 활발.

## 정체

- **1차 축**: 도메인 개념(이안류 동역학·위험·탐지). nearshore circulation 의 seaward 분기.
- 인접: [`concepts/waves`](../waves/)(쇄파·radiation stress) · [`concepts/currents`](../currents/)(연안류) · [`concepts/littoral-drift`](../littoral-drift/)(longshore current) · [`concepts/swash-zone`](../swash-zone/).
- 형성: 쇄파의 alongshore 변동(bathymetric channel·structure·wave-wave) → 보상류로 이안류 발생.

## 상태

| 파일 | 상태 | 비고 |
|---|---|---|
| `README.md` | self (governance) | 이 파일 |
| `01-concept.md` | **source-needed** (탐지 §4 full-PDF verified) | 정의·위험·유형·시각signature + ML 탐지 벤치마크(RipVIS·RipSeg·RipDetSeg·YOLOv8). 형성 mechanism taxonomy 는 교과서(MacMahan 2006·Dalrymple 2011) page 미보유 source-needed |

## 출처 원칙

신규(2026-06-18) — research/inbox promote 4건(CV 탐지 벤치마크 arxiv full-PDF read) + 이안류 정의·위험은 해당 논문 intro 인용. 형성 mechanism·유형 taxonomy 정량은 교과서(MacMahan-Reniers 2006 review·Dalrymple 2011 Annu. Rev.) page 인용 후 verified 승격.

## 생성 경위

inbox 의 rip current 4편 클러스터(RipVIS·RipSeg·RipDetSeg·YOLOv8 benchmark) promote 로 신설. 이안류는 한국 연안 안전(해수욕장 이안류 사고)에서도 중요 — KHOA 이안류 예측 연계 후속 후보.
