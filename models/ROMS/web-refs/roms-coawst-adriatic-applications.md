---
title: "ROMS·COAWST 운영적용 리뷰 — Adriatic Sea (Carniel et al. 2013)"
topic: roms-web-refs
canonical_source: self
citation_status: source-needed
verification_method: "arxiv:1309.7600v4 (Carniel·Russo·Benetazzo 2013) abstract 직접 인용 — Adriatic ROMS/COAWST 운영·연구 적용 범위 요약. COAWST 시스템 구성(ROMS+SWAN+WW3+CSTMS)은 publicly-known canonical (Warner et al. 2010, [[roms-official-resources]] §3 인용). 정량 격자·검증 수치·운영 forecast 상세는 full PDF read 후 보강 가능 — 현재 abstract-level."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-15
related:
  - models/ROMS/README.md
  - models/ROMS/web-refs/roms-official-resources.md
  - models/ROMS/source-analysis/roms_wec.md
  - models/SWAN/web-refs/swan-official-resources.md
---

# ROMS·COAWST 운영적용 리뷰 — Adriatic Sea

> [`roms-official-resources.md`](roms-official-resources.md) 의 공식 큐레이션 보완 — ROMS/COAWST 가 실제 반폐쇄해(Adriatic)에서 **순수 hydrodynamic → 완전 결합(COAWST)** 으로 발전한 운영·연구 적용 사례 리뷰. 모델 메커닉 자체는 [`source-analysis/`](../source-analysis/) 가 canonical, 본 노트는 적용 맥락(application context) 참조.

## 1. 출처

| 항목 | 값 |
|---|---|
| 제목 | "A review of modeling applications using ROMS model and COAWST system in the Adriatic sea region" |
| 저자 | Sandro Carniel, Aniello Russo, Alvise Benetazzo |
| arxiv ID | **1309.7600v4** (2013-09-29) |
| URL | <https://arxiv.org/abs/1309.7600> |
| citation_status | **source-needed** (abstract 기반 — 정량·검증 수치 미확인) |

## 2. COAWST 시스템 — 본 리뷰의 결합 축

COAWST (Coupled Ocean-Atmosphere-Wave-Sediment Transport, Warner et al. 2010) 은 ROMS 를 해양 코어로 atmosphere·wave·sediment 모듈을 MCT(Model Coupling Toolkit) 로 결합:

- **Ocean**: ROMS ([`source-analysis/roms_baroclinic_3d.md`](../source-analysis/roms_baroclinic_3d.md), [`roms_barotropic_2d.md`](../source-analysis/roms_barotropic_2d.md))
- **Wave**: SWAN ([[../../SWAN/web-refs/swan-official-resources]]) — 본 리뷰 Adriatic 구현은 ROMS↔SWAN **two-way coupling**
- **Sediment**: CSTMS (Community Sediment Transport Modeling System, Warner et al. 2008)
- ROMS 내 wave effect on current 연계는 [`source-analysis/roms_wec.md`](../source-analysis/roms_wec.md) (WEC, vortex-force) 참조

→ 본 리뷰는 이 결합 스택이 단일 해역에서 **다목적 운영체계**로 성숙한 사례를 정리한 1차 출처.

## 3. Adriatic 적용 범위 (abstract 직접 인용)

### 3.1 운영 구현 (operational)

abstract 명시 3 운영 구현:

1. **수력학 + 해수면 3일 예보** — 매일 hydrodynamic + sea level forecast 제공
2. **생지화학 (biogeochemistry)** — 주요 biogeochemical property 모델링 (ROMS biology, [`source-analysis/roms_biology.md`](../source-analysis/roms_biology.md))
3. **극한파 예보** — SWAN 과 **two-way coupled** 하여 extreme wave forecast

→ 시민·환경 보호 활동 지원: oil-spill 분산, **storm surge**, 폭풍 중 **연안 morphodynamic 변화**, Po River 염수쐐기(saline wedge) 침입 등 sub-model 구동.

### 3.2 연구 적용 (research)

- **sediment transport** 조사 (COAWST CSTMS 활용)
- eggs·larvae 분산
- 만내 hypoxic(저산소) event
- successive nesting 으로 이탈리아 연안 **초고해상** 도달 → 하구(river mouth) 환경 + 인공어초(artificial reef) 시뮬

### 3.3 데이터 배포

- 출력: **NetCDF CF-compliant** 포맷
- **THREDDS Data Server** 경유 전세계 사용자 배포

## 4. 본 위키 접점

| 본 위키 자료 | 접점 |
|---|---|
| [`source-analysis/roms_baroclinic_3d.md`](../source-analysis/roms_baroclinic_3d.md) | Adriatic 운영 코어 = ROMS 3D baroclinic |
| [`source-analysis/roms_wec.md`](../source-analysis/roms_wec.md) | ROMS↔SWAN two-way coupling 의 wave-current 연계 메커닉 |
| [`source-analysis/roms_biology.md`](../source-analysis/roms_biology.md) | 운영 구현 #2 biogeochemistry |
| [`source-analysis/roms_nesting.md`](../source-analysis/roms_nesting.md) | successive nesting → 연안 초고해상 (§3.2) |
| [[../../SWAN/web-refs/swan-official-resources]] | COAWST wave 컴포넌트 |

→ 한국 적용 함의: ROMS+SWAN 결합 운영체계의 reference architecture — 반폐쇄해(Adriatic ≈ 일부 한국 연안 만) 다목적 운영 사례로 참조 가능. 단 한국 직접 적용 사례 아님(미실증).

## 5. 인용 검증 TODO (verified 승격 조건)

- full PDF read → 격자 해상도·nesting 단계·검증 metric(관측 대비 skill) 정량 보강
- Warner et al. 2010 (COAWST 원논문) DOI 정확화 + [`roms-official-resources.md §3`](roms-official-resources.md) 와 교차
- THREDDS endpoint·운영 forecast 현행 여부 확인 (2013 논문 — 현재 운영 상태 별도 확인)
