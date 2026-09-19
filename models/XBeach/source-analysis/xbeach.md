---
title: "xbeach"
topic: general
canonical_source: self
citation_status: verified
verification_method: "XBeach source code 직접 분석 (models/XBeach/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/xbeach.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

# XBeach

## Status

queued foundation phase

## Why XBeach After EFDC

XBeach is a natural later lane for this wiki because it supports event-scale coastal response, erosion, and morphology questions that are not the center of the current ADCIRC foundation work. It should enter after ADCIRC and EFDC have cleaner baseline rules, because XBeach adds strong sensitivity to wave forcing, event definition, grid orientation, and morphology settings.

## Intended Scope

- solver orientation
- 1D versus 2D use cases
- wave and water-level boundary setup
- morphology-sensitive parameter vocabulary
- event-based validation strategy
- shoreline, profile, and erosion-response interpretation

## What This Note Should Eventually Hold

- model identity and domain fit
- major setup and output artifacts
- hydrodynamic versus morphology validation sequence
- common setup traps for erosion studies
- links to failure patterns, heuristics, and playbooks

## First Foundation Targets

- parameter glossary v1
- boundary and wave-setup note
- morphology foundation note
- first baseline case-selection note
- first erosion validation checklist

## Source Availability

Archived source root (vendor mirror):
- `models/XBeach/raw/source_code/trunk/`

High-value sources:
- `models/XBeach/raw/source_code/trunk/doc/manual/XBeach_manual_master.pdf`
- `models/XBeach/raw/source_code/trunk/doc/manual/XBeach_manual_kingsday.pdf`
- `XBEACH_MANUAL.md` (XBeach v1.24 practical manual note; not archived in this wiki)
- `models/XBeach/raw/source_code/trunk/doc/misc/DecisionTreeXBeach.docx`
- source trees under `models/XBeach/raw/source_code/trunk/src/xbeach/` and `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/`

## Why XBeach Belongs In This Wiki

XBeach will likely contribute a different class of durable knowledge than ADCIRC or EFDC. The most reusable assets are likely to be:
- event-definition rules
- wave-boundary interpretation habits
- morphology-before/after validation discipline
- grid-orientation and profile-definition checks
- recurring shoreline/erosion misfit patterns

## First Narrow Theme Candidates

- validate hydrodynamics before trusting morphology
- choose a first erosion baseline case with simple forcing and good observations
- boundary wave setup versus resulting shoreline response
- cross-shore profile interpretation and grid-orientation pitfalls
- event-window definition for storm erosion analysis
