---
title: "EFDC Sediment & Contaminant Transport Theory (Tetra Tech 2002 / 2003) — 9 sections deep summary"
topic: efdc-sediment-theory-2003
canonical_source: self
citation_status: verified
verification_method: "textbook/md/86899804-EFDC-Theory-Tech-Aspects-of-Sed-Trans-2003-05.md (source_id: efdc-sed-trans-2003, 8543 줄 markdown 추출본) 직접 인용 — Tetra Tech, Inc. prepared for US EPA Office of Science and Technology, May 2002 (3rd DRAFT), final revision 05/21/2003. 본 markdown 의 §1-9 챕터 직접 인용 (lines 48-8543) + EFDC+ Theory v12 Ch 6 와의 매핑 cross-walk."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-24
verification_by: "Claude Opus 4.7 (1M context) — 추출 markdown 본문 직접 인용 + DSI v12 Theory §6 cross-ref"
verification_date: 2026-05-24
related:
  - models/EFDC/manual-notes/efdc-manuals-overview.md
  - models/EFDC/manual-notes/efdc-theory-doc-v12.md
  - concepts/sediment-transport/02-theory.md
  - concepts/sediment-transport/06-model-application.md
---

# EFDC Sediment Theory (Tetra Tech 2002/2003) — Hamrick legacy reference

> 출처: source_id `efdc-sed-trans-2003` = [`textbook/md/86899804-EFDC-Theory-Tech-Aspects-of-Sed-Trans-2003-05.md`](../../../textbook/md/86899804-EFDC-Theory-Tech-Aspects-of-Sed-Trans-2003-05.md) (8543 줄, raw PDF [`models/EFDC/raw/manuals/pdfs/86899804-EFDC-Theory-Tech-Aspects-of-Sed-Trans-2003-05.pdf`](../raw/manuals/pdfs/) 추출본). **DSI v12 §6.3 SedTran Module 의 legacy reference**.

## 1. 자료 식별

| 항목 | 값 |
|---|---|
| 제목 | EFDC Technical Memorandum — Theoretical and Computational Aspects of Sediment and Contaminant Transport in the EFDC Model |
| 발주처 | US Environmental Protection Agency, Office of Science and Technology (401 M Street SW, Washington DC 20460) |
| 작성처 | Tetra Tech, Inc. (10306 Eaton Place Suite 340, Fairfax VA 22030) |
| 1차 draft | May 2002 (3rd DRAFT) |
| Final revision | 05/21/2003 (§5 expanded) |
| 본 위키 markdown | 8543 줄 (textbook/md/86899804-...md) |

## 2. Contents (markdown line 29-39 직접 인용)

```
- 1. Introduction                                                  3
- 2. Summary of Hydrodynamic and Generic Transport Formulations    4
- 3. Solution of the Sediment Transport Equation                   9
- 4. Hydrodynamic and Sediment Boundary Layers                    11
- 5. Sediment Bed Mass Conservation and Geomechanics              14
- 6. Noncohesive Sediment Settling, Deposition and Resuspension   26
- 7. Cohesive Sediment Settling, Deposition and Resuspension      34
- 8. Sorptive Contaminant Transport                               47
- 9. References                                                   53
```

(markdown 추출본 line 711+ 에서 §5 가 별도 final revision 05/21/2003 으로 expanded — "5. Sediment Bed Mass Conservation, Armoring and Consolidation" 으로 확장됨.)

## 3. 챕터별 핵심 (markdown line cited)

### 3.1 §1 Introduction (markdown line 48~)

> "This report summarizes theoretical and computational aspects of the sediment and sorptive contaminant transport formulations used in the EFDC model. Theoretical and computational aspects for the basic EFDC hydrodynamic and generic transport model components are presented in Hamrick (1992). Theoretical and computational aspects of the EFDC water quality-eutrophication model component are presented in Park et al." (markdown line 50-55)

→ 본 문서는 **EFDC sediment 모듈 전담** reference. hydro core 는 Hamrick (1992), water quality 는 Park et al. 별도.

### 3.2 §2 Summary of Hydrodynamic and Generic Transport (line 64~)

EFDC 의 3D shallow-water + sigma 좌표 정형:

- $\partial \eta / \partial t + \nabla \cdot (Hu) = 0$ — continuity (markdown line ~156)
- $\partial (Hu)/\partial t + \nabla \cdot \dots = -gH\nabla\eta - \nabla(Hp) + \dots$ — momentum
- sigma 좌표 $\sigma = (z-\eta)/H$ + curvilinear orthogonal

**transport 일반 form**:

$$\partial (HC)/\partial t + \nabla \cdot (Hu C) = \nabla \cdot (HA_v \nabla C) + \text{sources}$$

→ Sediment / contaminant 가 이 $C$ 에 대입 + bed exchange BC.

### 3.3 §3 Solution of Sediment Transport Equation (line 476~)

수치 해법:
- **External + internal mode split** (Hamrick split-explicit)
- Sediment $C_n$ (n 번째 size class) 에 대한 별도 advection-diffusion
- **bed exchange source term** — 다음 §4 boundary layer 에서 정의

### 3.4 §4 Hydrodynamic and Sediment Boundary Layers (line 660~) — 가장 상세

3 sub-section:
- **§4.1 Background** (line ~675) — bottom layer theory 기초
- **§4.2 Neutral Current and Sediment Boundary Layers** (line 1145) — 무중력 안정성 가정
- **§4.3 Stratified Current and Sediment Boundary Layers** (line 1677) — 안정도 효과 포함

**핵심 식**:

bottom shear velocity $u_*$ + reference height $z_r$ (markdown line ~983):

$$u(z) = \frac{u_*}{\kappa} \ln(z/z_0)$$

wave-current 결합 (markdown line ~1099, eq 4.33):

$$z_{uc}^2 + z_{uw}^2 + 2 z_{uc} z_{uw} \cos(\phi_c - \phi_w)$$

→ wave + current 의 combined boundary layer (Grant-Madsen 1979 류).

### 3.5 §5 Sediment Bed Mass Conservation, Armoring and Consolidation (line 3110~) — final revision 05/21/2003

bed 의 시간 발전:
- mass conservation per size class
- consolidation (deeper layer compaction)
- armoring (surface coarsening)

→ DSI v12 SEDZLJ §6.4.6 의 armoring concept 의 legacy.

### 3.6 §6 Noncohesive Sediment Settling, Deposition, Resuspension (line 4545~)

**Noncohesive (모래·gravel) — size-class based**:
- settling: Stokes 또는 Rouse-derived $w_s(d_{50}, \nu)$
- deposition: shear < critical → settle
- resuspension: shear > critical → entrainment (van Rijn 식 유사)

→ DSI v12 §6.3.1 Non-Cohesive Sediment 의 source.

### 3.7 §7 Cohesive Sediment Settling, Deposition, Resuspension (line 5298~)

**Cohesive (실트·점토) — Partheniades-Krone formulation**:
- settling: floc 형성 + concentration-dependent $w_s$
- deposition: Krone (1962) — shear < $\tau_d$ → settle prob
- erosion: Partheniades (1965) — shear > $\tau_c$ → linear erosion

> "5298:## 7. Cohesive Sediment Settling, Deposition and Resuspension" — markdown line 5298

→ DSI v12 §6.3.2 Cohesive Sediments 의 source.

추가 sub-section markdown line 5711: "## 7. Sediment Bed Geomechanical Processes" (번호 중복 표기, 실질 §7 sub) — consolidation·gas exchange·bioturbation 모델.

### 3.8 §8 Sorptive Contaminant Transport (line 6630~)

**Toxics (Hg·PCB·HAP) — Partitioning + bed exchange**:
- water column: $C_{\text{aq}} + C_{\text{sed-sorbed}}$
- equilibrium partitioning $K_d$ 또는 kinetic
- bed exchange: 표사 deposition/resuspension 과 결합

→ DSI v12 Ch 7 Chemical Fate and Transport 의 source.

### 3.9 §9 References (line 6464 + 8374)

핵심 외부 paper (markdown line 6464~):
- Hamrick (1992) — EFDC original
- Hamrick (1996) — EFDC user manual
- van Rijn (1984) — noncohesive sediment transport
- Krone (1962), Partheniades (1965) — cohesive
- Mehta & Partheniades (1975) — flocculation
- Grant & Madsen (1979) — wave-current boundary layer
- Smith & McLean (1977) — bottom roughness

## 4. DSI v12 와의 cross-walk

| 본 doc (2003) | DSI v12 Theory (2024) | 비고 |
|---|---|---|
| §2 hydro+transport | Ch 2 + Ch 3 | hydro 확장 (SGZ·propwash·hydraulic structures 추가) |
| §3 sediment eq solution | §6.2 Suspended Sediment + Numerical | 매핑 직접 |
| §4 boundary layer | §2.2.1 Bottom Friction + §6 sediment | DSI v12 에서 hydro 와 sed 분리 |
| §5 bed mass + armoring | §6.4.6 Bed Armoring | DSI 가 SEDZLJ 에 흡수 |
| §6 noncohesive | §6.3.1 Non-Cohesive Sediment | direct continuation |
| §7 cohesive | §6.3.2 Cohesive Sediments | direct continuation |
| §7 geomechanics (sub) | §6.3.3 Consolidation | 매핑 직접 |
| §8 sorptive | Ch 7 Chemical Fate and Transport | 확장 |

→ DSI v12 § 6.3 SedTran Module = 본 2003 doc 의 **modernized rewrite**. 2003 doc 의 식·notation 이 DSI v12 의 source 로 살아있음.

## 5. 활용 시나리오

| 활용 | 본 doc 인용 위치 |
|---|---|
| **이론 cite (논문·보고서)** | §6 noncohesive 또는 §7 cohesive (markdown line 4545~ 또는 5298~) |
| **wave-current boundary layer 수식** | §4.2-4.3 (markdown line 1145~, 1677~) — Grant-Madsen 류 |
| **bed armoring legacy** | §5 (markdown line 3110~) — DSI SEDZLJ 와 비교 |
| **Krone-Partheniades cohesive 정의** | §7 (line 5298~) — Krone 1962·Partheniades 1965 인용 source |
| **EFDC vs Delft3D-SED·CSTMS 알고리즘 비교** | §6+§7 (foundation 동일, dispatcher 다름) |

## 6. 작성 우선순위 (남은 작업)

- `efdc-sedtran-vs-sedzlj-walkthrough.md` — 본 doc §5-7 ↔ DSI v12 §6.3 vs §6.4 algorithm-level 매핑
- `efdc-boundary-layer-grant-madsen.md` — §4.2-4.3 의 wave-current combined boundary layer 식 정형 + Grant-Madsen 1979 cross-cite

## 7. 관련 자료

- [[efdc-manuals-overview]] — 6 manuals 인덱스
- [[efdc-theory-doc-v12]] — DSI 2024 modernized theory
- [`concepts/sediment-transport/02-theory.md`](../../../concepts/sediment-transport/02-theory.md) — 일반 표사 이론 (cross-reference, 본 doc 식의 도메인 컨텍스트)
- [`concepts/sediment-transport/06-model-application.md`](../../../concepts/sediment-transport/06-model-application.md) — EFDC SedTran/SEDZLJ dispatch (ssedtox.f90:868-880)
- [`models/EFDC/source-analysis/efdc_sediment.md`](../source-analysis/efdc_sediment.md) — codex source-code 직접 분석
- `textbook/sources.yml` 의 `efdc-sed-trans-2003` source_id
- 외부: Krone (1962), Partheniades (1965) — 본 doc §7 의 cohesive sediment legacy paper
