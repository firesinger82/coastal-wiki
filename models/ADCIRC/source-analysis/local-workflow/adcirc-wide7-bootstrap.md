---
title: "adcirc wide7 bootstrap"
topic: general
canonical_source: self
citation_status: source-needed
classification: local-workflow-notes
verification_method: "ADCIRC source code 직접 분석 (models/ADCIRC/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/adcirc-wide7-bootstrap.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

# ADCIRC wide7 Bootstrap

Date: 2026-04-13

Purpose:
- mark `wide7` as the clean working branch after `wide6`
- keep `wide6` as reference/evidence only

Working directory:
- `E:\numerical_models\adcirc\projects\korea_wide\mesh_dev\wide7`

Initial structure:
- `docs/`
- `input/DEM/`
- `input/domain/`
- `mesh/candidates/`
- `mesh/accepted/`
- `reviews/`
- `runs/`
- `scripts/`
- `artifacts/`

Initial files:
- `README.md`
- `docs/domain-decision-record.md`
- `docs/mesh-candidate-log.md`
- `docs/manual-intervention-log.md`
- `docs/TODO.md`

Working rule:
- all new domain work starts in `wide7`
- all new decisions are recorded before mesh generation
- all mesh candidates are preserved rather than overwritten
- all manual interventions are logged explicitly

Reference rule:
- `wide6` remains a reference and evidence source
- `wide7` is the clean branch for formalized process-driven work
