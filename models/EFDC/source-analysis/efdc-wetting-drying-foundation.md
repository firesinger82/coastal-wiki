---
title: "efdc wetting drying foundation"
topic: general
canonical_source: self
citation_status: verified
verification_method: "EFDC source code 직접 분석 (models/EFDC/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/efdc-wetting-drying-foundation.md (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

# EFDC Wetting-Drying Foundation

Date: 2026-04-30

This note captures the current wetting/drying foundation for EFDC coastal and estuarine setup in this wiki.

Important scope note:
- unlike some earlier EFDC notes, the local EFDC+ manual RAG did return concrete wetting/drying control names and behavior
- therefore this note contains both manual-backed control details and practical synthesis for calibration use

## Manual-Backed Controls

The local EFDC+ manual RAG explicitly returned the following wetting/drying controls.

### 1. ISDRY Options

The retrieved EFDC+ KB guidance indicates simplified wetting/drying options after older versions.

Returned options:
- `ISDRY = 0`
  - do not allow cells to wet and dry
- `ISDRY = 11`
  - use non-linear iterations for wetting/drying without face masking
  - when a cell is dry, all four faces are blocked, preventing inflow from neighboring cells
- `ISDRY = 99`
  - use non-linear iterations with face masking
  - if a neighboring cell is wet, the shared face does not have to remain blocked, allowing rewetting flow into the dry cell

### 2. Dry Depth

Returned meaning:
- defines the depth below which a cell is considered dry
- when cell-center depth falls below this threshold, faces are blocked and flow is forced to zero through the dry logic

### 3. Minimum Height

Returned meaning:
- the minimum initial-condition height should be smaller than `Dry Depth`
- otherwise the initialization can incorrectly force cells to start wet that should be dry-capable

### 4. Number Of Time Steps Before Water In Cell Goes Dry

Returned meaning:
- used to drain isolated or shallow wet cells when they have no inflow for a specified number of model time steps
- removed water volume is tracked for mass-balance accounting

## What These Controls Mean Practically

### A. Wetting/Drying Changes Effective Connectivity

This is not just a local shallow-water detail.
It changes which pathways are hydraulically open or closed during the tide cycle.

In practical terms, wet/dry settings can alter:
- shallow exchange between channels and flats
- marginal harbor connectivity
- estuarine shoal bypass pathways
- current concentration through the remaining wet cross section

### B. ISDRY = 11 Versus ISDRY = 99 Is Physically Important

The key difference is not cosmetic.

Working interpretation from the retrieved manual behavior:
- `ISDRY = 11` is more blocking-oriented once a cell is dry
- `ISDRY = 99` allows a more realistic rewetting pathway through face masking logic when neighboring wet cells can reconnect flow

For shallow tidal flats, marsh-like edges, harbor margins, and narrow secondary pathways, this distinction may materially change circulation realism.

### C. Initialization Can Corrupt Later Wet/Dry Behavior

If `Minimum Height` is inconsistent with `Dry Depth`, the model can begin from an unrealistically wet state.
That can contaminate early-stage interpretation and make later calibration look like a friction or forcing problem instead of an initialization problem.

## Calibration Implications

Wetting/drying should be checked early when:
- current mismatch is concentrated near shoals, flats, or channel margins
- the model gets stage broadly right but velocity pathways still look wrong
- flood/ebb asymmetry appears distorted in shallow regions
- isolated shallow cells appear to trap water or dry unrealistically

## Working Rule For This Wiki

Treat wetting/drying as a connectivity-control problem, not just as a shallow-cell numerical option.

## What To Log In Future EFDC Experiments

Each EFDC experiment card should record:
- `ISDRY` selection
- `Dry Depth`
- `Minimum Height`
- draining / dry-step behavior if used
- which shallow zones are most sensitive to the setting
- whether stage fit changed less than current fit after wet/dry changes

## Common Failure Interpretations

Wet/dry issues can masquerade as:
- friction problems
- bathymetry problems
- boundary-condition problems

That is why wetting/drying belongs before aggressive friction tuning in the calibration order for shallow coastal and estuarine cases.

## Manual-Backed Versus Practical Synthesis

### Clearly manual-backed from current retrieval
- the meaning of `ISDRY = 0`, `11`, and `99`
- the roles of `Dry Depth`, `Minimum Height`, and the dry-step draining control
- the use of cell skipping to improve computational efficiency

### Practical synthesis built on that manual behavior
- treating wet/dry as a connectivity-control issue in tidal calibration
- expecting strongest impact in shallow flats, harbor margins, and estuarine channels
- checking wet/dry before major friction retuning when currents remain wrong

## Next Expansion Candidates

- future `knowledge/failure-patterns/efdc-wetdry-connectivity-bias.md`
- future `knowledge/playbooks/efdc-shallow-zone-wetdry-checklist.md`
- targeted source-note extraction for the exact UI/control mapping in the EFDC+ version currently used
