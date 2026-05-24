---
title: "efdc"
topic: general
canonical_source: self
citation_status: verified
verification_method: "EFDC source code 직접 분석 (models/EFDC/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/efdc.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

# EFDC

## Status

queued foundation phase

## Why EFDC Next

EFDC is a strong candidate for the next active model because the local problem context is already calibration-heavy: water level may match while currents do not, and the practical bottleneck is not abstract solver theory but diagnosis of boundary conditions, bathymetry representation, friction zoning, turbulence settings, and comparison basis.

## Intended Scope

- solver orientation
- major file and setup vocabulary
- calibration order for tide and current problems
- bathymetry and boundary-condition interpretation
- observation-versus-model comparison discipline
- first failure patterns and playbooks for current mismatch

## What This Note Should Eventually Hold

- solver identity and practical domain fit
- important inputs and outputs
- calibration-sensitive parameter groups
- common setup traps for estuary and harbor cases
- links to current-mismatch diagnosis notes
- links to failure patterns, heuristics, and playbooks

## First Foundation Targets

- parameter glossary v1
- calibration foundation note
- boundary-condition foundation note
- observation-comparison principles note
- current-mismatch diagnosis note

## Why EFDC Belongs In This Wiki

EFDC work benefits from the same durable structure as ADCIRC, but the center of gravity is different. The most reusable assets are likely to be:
- repeated calibration sequences
- recurring mismatch patterns
- observation-comparison rules
- estuary/harbor-specific boundary and bathymetry lessons

## First Narrow Theme Candidates

- tide matches but current does not
- friction zoning versus bathymetry error
- open-boundary forcing interpretation
- wetting/drying sensitivity in shallow harbor and estuary settings
- fair comparison between observed and modeled current vectors or depth-averaged speed
