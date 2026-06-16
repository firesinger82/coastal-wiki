---
title: "처오름대 수치모델 — NLSW·Boussinesq/Green-Naghdi·SWASH·XBeach·VOF 점검"
topic: swash-zone
canonical_source: self
citation_status: source-needed
verification_method: "신규 (2026-06-15) — swash-capable 수치모델 점검표. 모델명·계열·대표 인용은 publicly-known canonical (SWASH=Zijlema·Stelling·Smit 2011 Coastal Eng / XBeach=Roelvink 2009 Coastal Eng / Green-Naghdi DG=Kazhyken·Videman·Dawson 2020 arxiv:2005.00920·2010.06167 / NLSW swash 해=Shen-Meyer 1963·Antuono 2010 JFM). 각 모델 swash 처리 디테일·정량 검증은 해당 모델 매뉴얼/소스 직접 인용 후 verified 승격 TODO. 본 위키 기수록 모델 cross-link: [[FUNWAVE]]·waves/04 XBeach."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-15
related:
  - concepts/swash-zone/01-concept.md
  - concepts/waves/04-code-and-tools.md
  - models/FUNWAVE/README.md
---

# 처오름대 수치모델 점검

> ⚠ source-needed. swash 는 **위상해상(phase-resolving)** 모델이 필수 — 위상평균(SWAN/WW3 등 spectral)은 개별 bore·shoreline 운동을 해상 못함. wetting-drying(이동경계) 처리가 swash 모델의 핵심 요건.

## 1. 모델 계열 비교

| 계열 | 대표 모델 | swash 처리 | 비고 |
|---|---|---|---|
| **NLSW (비선형 천수)** | 해석해 + FV solver | bore collapse·dam-break 유사, 이동 shoreline | 분산 무시 → surf/swash 직접. [`01 §4.2`](01-concept.md) Antuono 2010 해 |
| **Boussinesq / Green-Naghdi** | **FUNWAVE-TVD** · COULWAVE · Celeris | 약분산 + 비선형, surf~swash. wetting-drying | [[../../models/FUNWAVE/README]] 기수록. Green-Naghdi DG = Kazhyken 2020 |
| **비정수압 (non-hydrostatic)** | **SWASH** · XBeach-NH | 다층 비정수압, 분산·쇄파·swash | SWASH = SWAN 그룹(Zijlema·Stelling·Smit 2011), 본 위키 미수록 모델 |
| **Surfbeat (IG-resolving)** | **XBeach surfbeat (XBSB)** | 단파포락+IG 해상(개별 bore 평균), runup | 효율적, storm impact 표준. [`waves/04 §4`](../waves/04-code-and-tools.md) |
| **VOF / Navier-Stokes** | OpenFOAM(interFoam) · SPH | sheet flow·turbulence·airflow 직접 | 고비용, lab-scale swash 정밀연구 |

## 2. Boussinesq / Green-Naghdi — 본 위키 기수록

- **FUNWAVE-TVD** — [[../../models/FUNWAVE/README]]. 완전비선형 Boussinesq, TVD shock-capturing, wetting-drying 로 surf~swash 처오름. GPU(Blackwell) 빌드 검증됨(메모리). 위상해상 정온/처오름 정밀 티어.
- **Green-Naghdi DG (Kazhyken·Videman·Dawson 2020)** — arxiv:[2005.00920](https://arxiv.org/abs/2005.00920)(morphodynamic) · [2010.06167](https://arxiv.org/abs/2010.06167)(sediment-morpho). Strang splitting 으로 surf zone 등에서 분산항 끄기 → **swash zone 까지 hydrodynamic 해상**. bed morphodynamic 결합. [`sediment-transport/04 §10.1`](../sediment-transport/04-code-and-tools.md) 중복 등재.
- **Celeris** — [[../../models/Celeris/README]](STUB). WebGPU 실시간 interactive Boussinesq.

## 3. 비정수압 — SWASH ✅ ([[../../models/SWASH/README]] 수록)

**SWASH** (Simulating WAves till SHore, Zijlema·Stelling·Smit 2011 *Coastal Engineering* 58:992-1012 doi:10.1016/j.coastaleng.2011.05.015) — SWAN 과 같은 TU Delft 그룹의 **비정수압 다층** 위상해상 모델. Boussinesq 고차 분산항 대신 **연직 층분할 + 비정수압 압력**(Poisson)으로 분산 표현(층↑→깊은물 정확). 분산·비선형·쇄파·runup·wave-current. SWAN(위상평균 광역) → SWASH(위상해상 항내·swash) nesting 자연 — SWAN OCP 인프라 공유. ✅ **2026-06-15 신설**: [[../../models/SWASH/README]] (v12.01 GitLab clone) + [`source-analysis`](../../models/SWASH/source-analysis/swash-architecture-source-map.md)(명명규칙 Exp/Imp×Dep/Lay + compute dispatch) + [`web-refs`](../../models/SWASH/web-refs/swash-official-resources.md).

## 4. XBeach — surfbeat + non-hydrostatic

- **XBeach** (Roelvink et al. 2009 *Coastal Engineering* 56:1133-1152) 2 모드가 swash 관련:
  - **Surfbeat(XBSB)**: short-wave envelope + IG wave 해상 → swash·runup·storm erosion(dune overwash). 효율적.
  - **Non-hydrostatic(XBNH)**: 개별 파 위상해상 → swash 정밀(느림).
- [`waves/04 §4`](../waves/04-code-and-tools.md) 기존 XBeach 절 + [`01 §4.1`](01-concept.md) PIML runup(2401.08684, XBSB↔XBNH cGAN 매핑).

## 5. 모델 선택 가이드

| 목적 | 권장 |
|---|---|
| 광역→해빈 runup·storm erosion | **XBeach surfbeat** (효율) |
| 항내/구조물 정밀 처오름·정온 | **FUNWAVE / SWASH** (위상해상) |
| swash sheet-flow·표사 미시 | OpenFOAM VOF / SPH (lab-scale) |
| swash + morphodynamic 결합 | Green-Naghdi DG(Kazhyken) / XBeach-NH |
| alongshore swash transport | NLSW(Antuono/Ryrie 해, [`01 §4.2`](01-concept.md)) |

## 6. 보강 (verified 승격 TODO)

- SWASH 매뉴얼 직접 인용 → `models/SWASH/` 신설 검토 (Zijlema 2011 Coastal Eng full)
- FUNWAVE swash/wetting-drying source-analysis cross-link 정밀화
- XBeach surfbeat vs NH swash 검증 한국 사례
- VOF(interFoam) swash boundary 설정 + SPH 인용

## 7. 연결

- [`01-concept.md`](01-concept.md) — swash process·전이 연구 3건
- [`concepts/waves/04-code-and-tools.md`](../waves/04-code-and-tools.md) — 위상해상 모델 + §5.1 위상평균/위상해상 종합리뷰(FUNWAVE·SWASH·COULWAVE·NHWAVE 포함)
- [[../../models/FUNWAVE/README]] · [[../../models/Celeris/README]]
