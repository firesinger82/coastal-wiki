---
title: "ADCIRC NWS=13 + JMA-MSM 로컬 워크플로 서술 (canonical 추출분)"
extracted_from: models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge-nws-families.md
extracted_date: 2026-07-10
extracted_reason: "L4 감사 2026-07-10 INTEGRITY-VIOLATION — 개인 워크플로 서술('the user' 화법)이 canonical(models/)에 존재, 절대규칙 #2(개인 경험은 experience/에만)·#8(운영 지침 canonical 금지) 레이어 위반. experience/ promote 는 3조건 게이트(반복 관찰·객관 데이터·재현 가능) 통과 후 사람이 결정."
status: pending-user-gate
---

# 추출된 개인 워크플로 서술 (원문 보존)

아래는 2026-04 modeling-wiki 작성분에서 마이그레이션된 개인 워크플로 서술 원문.
객관 사실(NWS=13 = OWI NetCDF 포맷 등)은 canonical 노트에 잔존하며
[[adcirc-met-forcing-implementation]] 이 file:line 인용으로 커버.

## Why `NWS=13` Fits The Current Workflow (개인 부분)

Current local workflow fact from the user:
- you mainly experiment with `JMA-MSM` data using `NWS=13`

Inference:
- the working path is not "ADCIRC reads raw JMA-MSM by name"
- the working path is "JMA-MSM is converted into an OWI-NWS13-compatible NetCDF product that ADCIRC can read through `NWS=13`"

That inference is consistent with the official docs and with the fact that the docs describe the expected `NWS=13` file convention, not a JMA-MSM-native reader.

## Local Workflow Statement

This wiki should treat:
- `JMA-MSM -> OWI-NWS13 NetCDF -> ADCIRC NWS=13`

as the default storm-surge forcing pathway unless a project explicitly says otherwise.

## 처리 방향 (사람 결정 대기)

1. **experience/ promote**: 반복 run 으로 검증되면 `experience/heuristics/` 또는 [[khoa-adcirc-typhoon-forcing-design-2026]] 계열로 편입
2. **프로젝트 repo 이동**: 워크플로 선언은 위키가 아닌 개별 프로젝트/coastal-runs 문서가 맞을 수 있음 (절대규칙 #8)
3. **폐기**: JMA-MSM 경로가 더 이상 기본이 아니면 삭제
