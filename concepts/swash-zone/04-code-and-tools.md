---
title: "처오름대 수치모델 — NLSW·Boussinesq/Green-Naghdi·SWASH·XBeach·VOF 점검"
topic: swash-zone
canonical_source: self
citation_status: verified
verification_method: "swash 수치모델 점검표. **모델 swash-handling(wetting-drying·breaking·runup·비정수압)은 본 위키 검수 완료 source-analysis 노트로 verified** (2026-06-18 승격): SWASH=[[swash-wetting-drying-runup]](SwashDryWet/SwashRunupHeight/SwashBreakPoint bore-front, file:line)·[[swash-nonhydrostatic-pressure-solver]] / XBeach=[[xbeach_nonh]]·[[xbeach_wave_action_balance]](surfbeat)·[[xbeach_flow_solver]] / FUNWAVE=[[funwave-flux-tvd]](TVD wetting-drying MASK)·[[funwave-physics-sources]]. 모델 정체 bibliographic: SWASH=Zijlema·Stelling·Smit 2011 Coastal Eng 58:992-1012 doi:10.1016/j.coastaleng.2011.05.015 / XBeach=Roelvink 2009 Coastal Eng 56:1133-1152 / Green-Naghdi DG=Kazhyken·Videman·Dawson 2020 arxiv:2005.00920·2010.06167 / NLSW swash 해=Shen-Meyer 1963·Antuono 2010 JFM. VOF/SPH(§1 마지막 행)·한국 검증은 미수록=source-needed 잔존."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-15
verification_date: 2026-06-18
related:
  - concepts/swash-zone/01-concept.md
  - concepts/waves/04-code-and-tools.md
  - models/SWASH/source-analysis/swash-wetting-drying-runup.md
  - models/XBeach/source-analysis/xbeach_nonh.md
  - models/FUNWAVE/source-analysis/funwave-flux-tvd.md
---

# 처오름대 수치모델 점검

> swash 는 **위상해상(phase-resolving)** 모델이 필수 — 위상평균(SWAN/WW3 등 spectral)은 개별 bore·shoreline 운동을 해상 못함. wetting-drying(이동경계) 처리가 swash 모델의 핵심 요건. ✅ 본 위키 수록 3 위상해상 모델(SWASH·XBeach·FUNWAVE)의 swash-handling 커널이 source-analysis 로 검수됨(§2-4 각 절 cross-link).

## 1. 모델 계열 비교

| 계열 | 대표 모델 | swash 처리 | 비고 |
|---|---|---|---|
| **NLSW (비선형 천수)** | 해석해 + FV solver | bore collapse·dam-break 유사, 이동 shoreline | 분산 무시 → surf/swash 직접. [`01 §4.2`](01-concept.md) Antuono 2010 해 |
| **Boussinesq / Green-Naghdi** | **FUNWAVE-TVD** · COULWAVE · Celeris | 약분산 + 비선형, surf~swash. wetting-drying | [[../../models/FUNWAVE/README]] 기수록. Green-Naghdi DG = Kazhyken 2020 |
| **비정수압 (non-hydrostatic)** | **SWASH** · XBeach-NH | 다층 비정수압, 분산·쇄파·swash | SWASH = SWAN 그룹(Zijlema·Stelling·Smit 2011), 본 위키 미수록 모델 |
| **Surfbeat (IG-resolving)** | **XBeach surfbeat (XBSB)** | 단파포락+IG 해상(개별 bore 평균), runup | 효율적, storm impact 표준. [`waves/04 §4`](../waves/04-code-and-tools.md) |
| **VOF / Navier-Stokes** | OpenFOAM(interFoam) · SPH | sheet flow·turbulence·airflow 직접 | 고비용, lab-scale swash 정밀연구 |

## 2. Boussinesq / Green-Naghdi — 본 위키 기수록

- **FUNWAVE-TVD** — [[../../models/FUNWAVE/README]]. 완전비선형 Boussinesq, TVD shock-capturing, wetting-drying 로 surf~swash 처오름. ✅ swash-handling 검수: [[../../models/FUNWAVE/source-analysis/funwave-flux-tvd]](TVD flux + **wetting-drying MASK** 처리)·[[../../models/FUNWAVE/source-analysis/funwave-physics-sources]](breaking·bottom friction). GPU(Blackwell, cuSPARSE v2) 빌드 검증됨([[../../models/FUNWAVE/source-analysis/funwave-gpu-cuda-port]]). 위상해상 정온/처오름 정밀 티어.
- **Green-Naghdi DG (Kazhyken·Videman·Dawson 2020)** — arxiv:[2005.00920](https://arxiv.org/abs/2005.00920)(morphodynamic) · [2010.06167](https://arxiv.org/abs/2010.06167)(sediment-morpho). Strang splitting 으로 surf zone 등에서 분산항 끄기 → **swash zone 까지 hydrodynamic 해상**. bed morphodynamic 결합. [`sediment-transport/04 §10.1`](../sediment-transport/04-code-and-tools.md) 중복 등재.
- **Celeris** — [[../../models/Celeris/README]] (source-analysis 9 verified: boussinesq-solver·breaking·fv-reconstruction·webgpu-infra). WebGPU 실시간 interactive Boussinesq.

## 3. 비정수압 — SWASH ✅ ([[../../models/SWASH/README]] 수록)

**SWASH** (Simulating WAves till SHore, Zijlema·Stelling·Smit 2011 *Coastal Engineering* 58:992-1012 doi:10.1016/j.coastaleng.2011.05.015) — SWAN 과 같은 TU Delft 그룹의 **비정수압 다층** 위상해상 모델. Boussinesq 고차 분산항 대신 **연직 층분할 + 비정수압 압력**(Poisson)으로 분산 표현(층↑→깊은물 정확). 분산·비선형·쇄파·runup·wave-current. SWAN(위상평균 광역) → SWASH(위상해상 항내·swash) nesting 자연 — SWAN OCP 인프라 공유. ✅ **소스 전수 검수(2026-06-16, 19 source-analysis)**: [[../../models/SWASH/README]] (v12.01 GitLab clone) + 아키텍처([`swash-architecture-source-map`](../../models/SWASH/source-analysis/swash-architecture-source-map.md), Exp/Imp×Dep/Lay).
  - **swash 핵심 메커닉 검수**: [[../../models/SWASH/source-analysis/swash-wetting-drying-runup]] — 침수-건조 마스크(`SwashDryWet`), **bore-front wave breaking 판정**(`SwashBreakPoint`), runup 높이(`SwashRunupHeight`, 1D), 총수심 갱신. + [[../../models/SWASH/source-analysis/swash-nonhydrostatic-pressure-solver]](비정수압 압력 projection = SWASH 분산의 정의적 메커닉).

## 4. XBeach — surfbeat + non-hydrostatic

- **XBeach** (Roelvink et al. 2009 *Coastal Engineering* 56:1133-1152) 2 모드가 swash 관련:
  - **Surfbeat(XBSB)**: short-wave envelope + IG wave 해상 → swash·runup·storm erosion(dune overwash). 효율적. ✅ [[../../models/XBeach/source-analysis/xbeach_wave_action_balance]](파작용 균형 envelope)·[[../../models/XBeach/source-analysis/xbeach_single_dir]].
  - **Non-hydrostatic(XBNH)**: 개별 파 위상해상 → swash 정밀(느림). ✅ [[../../models/XBeach/source-analysis/xbeach_nonh]](비정수압 압력 보정). flow solver 의 wetting-drying = [[../../models/XBeach/source-analysis/xbeach_flow_solver]].
- [`waves/04 §4`](../waves/04-code-and-tools.md) 기존 XBeach 절 + [`01 §4.1`](01-concept.md) PIML runup(2401.08684, XBSB↔XBNH cGAN 매핑).

## 5. 모델 선택 가이드

| 목적 | 권장 |
|---|---|
| 광역→해빈 runup·storm erosion | **XBeach surfbeat** (효율) |
| 항내/구조물 정밀 처오름·정온 | **FUNWAVE / SWASH** (위상해상) |
| swash sheet-flow·표사 미시 | OpenFOAM VOF / SPH (lab-scale) |
| swash + morphodynamic 결합 | Green-Naghdi DG(Kazhyken) / XBeach-NH |
| alongshore swash transport | NLSW(Antuono/Ryrie 해, [`01 §4.2`](01-concept.md)) |

## 6. 보강 현황

- ✅ **SWASH** 신설 + 소스 전수 검수 완료 (19 source-analysis, swash-handling 커널 §3). swashuse/swashtech 매뉴얼도 검수([[../../models/SWASH/manual-notes/swash-user-manual]]·[[../../models/SWASH/manual-notes/swash-tech-documentation-overview]]).
- ✅ **FUNWAVE** swash/wetting-drying source-analysis cross-link 완료 (§2).
- ✅ **XBeach** surfbeat vs NH source-analysis cross-link 완료 (§4).
- ⬜ XBeach surfbeat vs NH swash 검증 **한국 사례** (source-needed 잔존).
- ⬜ VOF(interFoam) swash boundary 설정 + SPH 인용 (본 위키 미수록 외부모델, source-needed).

## 7. 연결

- [`01-concept.md`](01-concept.md) — swash process·전이 연구 3건
- [`concepts/waves/04-code-and-tools.md`](../waves/04-code-and-tools.md) — 위상해상 모델 + §5.1 위상평균/위상해상 종합리뷰(FUNWAVE·SWASH·COULWAVE·NHWAVE 포함)
- [[../../models/FUNWAVE/README]] · [[../../models/Celeris/README]]
