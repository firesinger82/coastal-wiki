---
title: "복합침수 모델 적용 — 침수 모델 스펙트럼 link-hub (full-physics → reduced-complexity → ML emulator)"
topic: compound-flooding
canonical_source: self
citation_status: verified
has_source_needed: true
verification_method: >
  본 노트는 link-hub. 인용한 모든 cross-link 대상 source-analysis 노트의 실재를
  ls 로 직접 확인(2026-06-18), 각 노트의 frontmatter(citation_status: verified)·
  도입부에서 물리수준·솔버 종류·결합 인자를 직접 읽어 표에 반영. 모델별 물리·솔버
  단언은 해당 검수완료 source-analysis 노트로 위임(cross-link). 한국 적용·정량
  벤치마크는 source-needed 로 명시.
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - concepts/compound-flooding/README.md
  - concepts/compound-flooding/01-concept.md
  - models/SFINCS/README.md
  - models/LISFLOOD-FP/README.md
---

# 복합침수 모델 적용 — 침수 모델 스펙트럼 (link-hub)

> 이 파일은 **링크 허브**다. 복합침수([[README]]·[[01-concept]])를 모의하는 모델들을
> **정확도↔계산비용** 축에서 배치하고, 각 모델의 물리·솔버 단언은 본 위키의
> **검수완료(verified) source-analysis 노트**로 위임한다. 여기서는 새 단언을 만들지 않고
> 분류·연결만 한다.

## 0. 스펙트럼 한눈

복합침수 침수 모델은 동일한 천수 흐름을 어느 수준까지 푸느냐로 정확도와 비용이 갈린다.

```
정확도 高 / 비용 高                                정확도 ~ / 비용 低
 full-physics  ───────  reduced-complexity  ───────  ML emulator
 (full SWE)              (단순화 SWE: LIE/ACC)        (학습된 surrogate)
 ADCIRC                  SFINCS                       PACT / StormNet
 Delft3D-FLOW            LISFLOOD-FP                  Global LI / CLDNet
 EFDC                    (LISFLOOD-FP는 full SWE      climate-adapt CNN
                          FV1/DG2 경로도 보유)
```

핵심 구분: **하나의 모델이 어느 침수 인자(coastal / pluvial / fluvial)를 다루는가**.
ADCIRC 류는 연안 해일(coastal surge) 특화이고, SFINCS·LISFLOOD-FP 는 설계상
세 인자를 한 격자에서 통합(compound)한다.

## 1. 비교표

| 모델 | 물리 수준 | 솔버 / 이산화 | 격자 | 다루는 침수 인자 | 비용 | 검수 source-analysis |
|---|---|---|---|---|---|---|
| **ADCIRC** | full-physics (2D-DI / 3D) | GWCE(일반화 파동연속식) + 운동량, 유한요소 | 비정형 삼각망 (unstructured FEM) | coastal surge·조석·(파 결합 시 WAVE) | 高 (수~십수 시간, MPI) | [[../../models/ADCIRC/source-analysis/adcirc-gwce-implementation]](GWCE/FEM) · [[../../models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge]](forcing) |
| **Delft3D-FLOW** | full-physics (2D/3D) | TRISULA SWE, ADI 유한차분 (structured) | 정형 curvilinear / σ·z layer | coastal·조석·(D-WAQ/morpho 결합) | 高 | [[../../models/Delft3D/source-analysis/delft3d_flow2d3d_dispatcher]] |
| **EFDC** | full-physics (3D, 정수압+준비정수압) | external/internal mode split, 3TL/2TL | 정형 curvilinear, σ layer | coastal·하구·하천·조석 | 高 | [[../../models/EFDC/source-analysis/efdc_hydro_core]] |
| **SFINCS** | reduced-complexity | 단순화 SWE (LIE / SSWE, Bates 류 explicit) | staggered + **subgrid + quadtree** 적응 | **compound: coastal + pluvial + fluvial** | 低 (full 대비 대폭↓) | [[../../models/SFINCS/source-analysis/sfincs_flow_solver]] · [[../../models/SFINCS/source-analysis/sfincs_subgrid_quadtree]] · [[../../models/SFINCS/README]] |
| **LISFLOOD-FP** | reduced↔full 스펙트럼 | **ACC**(local inertia, Bates 2010) / diffusive / Roe / **FV1·DG2**(full SWE) | structured raster + SGC 채널 | **compound: fluvial + pluvial + coastal** | 低(ACC)~中(FV1/DG2) | [[../../models/LISFLOOD-FP/source-analysis/lisflood-fp-classic-acc-flow]] · [[../../models/LISFLOOD-FP/source-analysis/lisflood-fp-swe-fv1-dg2]] |
| **ML emulator** | surrogate (학습) | 신경망(ST-GNN·GCN+GAT+LSTM·UNet·CNN) | 정점/메쉬/그리드 학습표현 | (학습 대상이 정한) coastal surge·compound flood | 極低 (초 단위 추론) | [[../storm-surge/07-ml-emulators]] |

> 표의 "물리 수준·솔버"는 각 cross-link 노트의 verified 본문 요약이며, 정확한 식·file:line 은
> 해당 노트를 따른다. SWE = Shallow Water Equations, LIE = Local Inertial Equations,
> ACC = ACCeleration(local inertia), GWCE = Generalized Wave Continuity Equation.

## 2. full-physics — 고정확·고비용

완전 천수방정식(혹은 3D)을 직접 푸는 계열. 정확도가 높지만 계산비용·전문성 요구가 크다.
복합침수 맥락에서는 주로 **연안 해일(coastal surge)** 성분의 reference 솔버로 쓰인다.

- **ADCIRC** — GWCE 기반 유한요소 해일 모델, 비정형 삼각망으로 연안 복잡지형·해상도 적응에 강함.
  태풍 바람장(NWS=19/20 parametric, 29/30 OWI hybrid) 으로 해일을 구동.
  → [[../../models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge]] (GAHM/AHM/OWI forcing, vortex)
- **Delft3D-FLOW** — TRISULA SWE 엔진(ADI, structured curvilinear), 8 Fortran package 구조.
  파(D-Waves)·수질·형태변화 결합 생태계.
  → [[../../models/Delft3D/source-analysis/delft3d_flow2d3d_dispatcher]]
- **EFDC** — external(2D 수심적분)/internal(3D shear) mode-split, 3TL↔2TL 전환. 하구·하천·연안 통합
  하이드로다이내믹스에 강함.
  → [[../../models/EFDC/source-analysis/efdc_hydro_core]]

이들은 full SWE 솔버로서 정확도 기준점(benchmark)을 제공하지만, ensemble·기후 시나리오·early
warning 처럼 **반복·실시간** 요구에는 비용이 병목 — 아래 reduced/ML 계열의 동기.

## 3. reduced-complexity — compound 통합·고속

침수 모의에 충분한 만큼만 물리를 남겨 대폭 가속한 계열. **이 두 모델이 복합침수의 정의적 도구**다
(coastal+pluvial+fluvial 을 한 격자에서 동시 처리).

### 3.1 SFINCS (Deltares)

- 단순화 SWE(LIE/SSWE) explicit 솔버 + **subgrid look-up table** + **quadtree 적응격자**로
  "거친 계산격자 + 정밀 지형 정확도"를 동시 달성.
- 설계 목적 자체가 **compound flooding**(연안 조석·해일·파 + 강우 + 하천)의 고속·ensemble·
  early-warning 모의.
- → 흐름 코어 [[../../models/SFINCS/source-analysis/sfincs_flow_solver]] ·
  고속화 [[../../models/SFINCS/source-analysis/sfincs_subgrid_quadtree]] ·
  정체·인자 [[../../models/SFINCS/README]]

### 3.2 LISFLOOD-FP (Bristol/Sheffield)

- **솔버 스펙트럼을 한 코드에 보유**: ACC(local inertia, Bates 2010) ↔ diffusive ↔ Roe 근사
  리만 ↔ **full SWE(FV1 1차 Godunov / DG2 2차 Discontinuous Galerkin)**. 따라서
  reduced↔full 경계를 모델 내부에서 넘나든다.
- 강점은 **fluvial + pluvial** 범람(raster + SGC subgrid 채널), 연안 forcing 결합 시 compound.
- → ACC/diffusive/Roe + time loop [[../../models/LISFLOOD-FP/source-analysis/lisflood-fp-classic-acc-flow]] ·
  full SWE FV1/DG2 [[../../models/LISFLOOD-FP/source-analysis/lisflood-fp-swe-fv1-dg2]]

> **결합 인자 관점 정리**: ADCIRC/Delft3D/EFDC 는 **coastal(해일·조석)** 솔버가 본체이고,
> SFINCS·LISFLOOD-FP 는 **세 인자(coastal·pluvial·fluvial) 통합**이 설계 의도라는 점이
> 복합침수 적용에서 핵심 차이다. (인자 정의는 [[01-concept]] 참조.)

## 4. ML emulator — 학습된 surrogate·극저비용

full hydrodynamic 모델의 비용을 신경망으로 우회. 추론이 초 단위라 대규모 ensemble·기후
시나리오·실시간 early warning 에 적합. 대신 학습 분포(태풍·지역) 밖 일반화·정량 신뢰도가
관건이며, 학습 reference(보통 ADCIRC/Delft3D)의 정확도 상한을 넘지 못한다.

- → [[../storm-surge/07-ml-emulators]] — PACT/ST-GNN(연안 해일), StormNet(GCN+GAT+LSTM bias-correction),
  Global LI surge(UNet), climate-adaptation flood CNN, CLDNet 류 SWE surrogate 정리.

복합침수 surrogate 는 본 위키의 우선 관심사다(storm↔wave coupled surrogate, climate-adaptation
flood) — 상세·정량은 위 노트로 위임.

## 5. 모델 선택 가이드 (정성)

| 상황 | 우선 계열 | 이유 |
|---|---|---|
| 단일 이벤트 고정밀 연안 해일 hindcast | full-physics (ADCIRC/Delft3D/EFDC) | 정확도·검증용 reference |
| coastal+pluvial+fluvial 통합 침수 매핑 | reduced-complexity (SFINCS / LISFLOOD-FP) | compound 설계·고속 |
| 100~1000 ensemble·기후 시나리오·return period | reduced-complexity 또는 ML emulator | 반복비용 |
| 초 단위 early-warning·실시간 다중 track | ML emulator | 추론 극저비용 |

> 위 가이드는 위 cross-link 노트들의 정성적 특성에서 도출한 분류이며, **정량 벤치마크
> (정확도·런타임 수치)·한국 연안도시 구체 적용 사례는 별도 확보 후 보강** (아래 §6).

## 6. 미해결 / source-needed

- **한국 연안도시 복합침수 모델 적용 사례·정량 비교** (KHOA·해안침수예상도·적응계획 등):
  `source-needed`. 확보 시 본 허브에 사례 표 추가 또는 `concepts/compound-flooding/05-*` 신설.
- **모델 간 정량 벤치마크**(동일 케이스 정확도/런타임): `source-needed`. SFINCS↔ADCIRC,
  LISFLOOD-FP ACC↔FV1 비교 문헌 확보 후.
- SCHISM·Delft3D-FM(D-Flow FM) 등 미보유 모델은 본 위키에 source-analysis 가 생기면 표에 추가.

## 관련

- [[README]] · [[01-concept]] (복합침수 정의·인자)
- 모델: [[../../models/SFINCS/README]] · [[../../models/LISFLOOD-FP/README]]
- 인접 개념: [`concepts/storm-surge`](../storm-surge/) (연안 해일 인자) · [[../storm-surge/07-ml-emulators]]
