---
title: "adcirc"
topic: general
canonical_source: self
citation_status: verified
verification_method: "ADCIRC source code 직접 분석 (models/ADCIRC/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/adcirc.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

# ADCIRC

## Status

foundation phase

## Why ADCIRC First

ADCIRC is the first active model for this wiki. The goal is to build a clean foundation before regular trial-and-error accumulation begins.

## Current Scope

- solver orientation
- file and workflow vocabulary
- governing assumptions
- numerical formulation basics
- validation references
- example setup artifacts
- baseline case selection
- first-pass parameter glossary

## What This Note Should Eventually Hold

- solver identity and scope
- major input and output artifacts
- important numerical choices
- common setup traps
- links to validation examples
- links to failure patterns, heuristics, and playbooks

## Foundation References Collected On 2026-04-12

- official docs hub
- getting started guide
- theory and formulation docs
- theory PDF for numerical formulation
- input files reference
- parameter definitions reference
- examples index
- official example problems page
- official support page
- official FAQ
- GitHub model repository
- GitHub release history
- GitHub test suite
- tooling ecosystem page
- ADCIRCpy
- ASGS operator material

## Not Filled Yet

- baseline example set selection
- first experiment links
- first narrow theme decision

## First Narrow Theme Candidates

- mesh and boundary-condition vocabulary
- fort.14 and fort.15 baseline anatomy
- timestep / CFL / stability setup discipline
- official example case selection for first baseline

## Foundation Outputs Now Present

- source catalog
- source note set
- baseline selection note
- parameter glossary v1
- fort.15 checklist v1
- first controlled DT-sensitivity experiment draft
