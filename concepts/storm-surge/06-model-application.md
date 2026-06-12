---
title: "폭풍해일 — 06 모델 적용 (ADCIRC · Delft3D · ROMS · EFDC)"
topic: storm-surge
canonical_source: link-hub
citation_status: verified
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-12
---

# 폭풍해일 — 06 모델 적용

> **Canonical source**: 모델 메커닉(구현·서브루틴·알고리즘)은 `models/<model>/`이 진실의 원천. 이 페이지는 **요약 + 링크만** ([CONVENTIONS.md](../../CONVENTIONS.md) §3, drift 방지). 구현 디테일은 복제하지 않고 source-analysis 노트로 링크.

폭풍해일은 **저기압·바람에 의한 이상고조**로, 수치적으로는 **천수방정식(depth-integrated SWE)** 을 바람응력·기압·조석·마찰·범람과 함께 푸는 문제. 이론은 [`02-theory.md`](02-theory.md)(Pugh §6 + GWCE), 인자는 [`01-concept.md`](01-concept.md) 참조.

## 1. 모델 선택 (도메인별)

| 모델 | 적합 도메인 | surge 위상 |
|---|---|---|
| **ADCIRC** | open-coast·대영역·비정형 메시 (de facto 표준) | barotropic 2DDI GWCE — **한반도 광역 surge 1순위** |
| **Delft3D-FLOW / D-Flow FM** | 하구·연안 structured(FLOW) / 비정형(FM) | ADI(structured) / Stelling-Kernkamp(FM) SWE |
| **ROMS (+COAWST)** | 해양순환 결합 surge·baroclinic | barotropic mode + wave/sediment 결합 |
| **EFDC** | 만·하구 천해 surge·범람 | external mode(수위) + 천해 |

## 2. 한국 적용 표준 흐름

ADCIRC barotropic + 태풍 parametric/재분석 바람 + (선택) SWAN 결합 wave setup. KHOA 정점 검증. 자세한 입출력·NWS 모드는 [`04-code-and-tools.md`](04-code-and-tools.md), 검증 사례는 [`05-examples.md`](05-examples.md).

## 3. ADCIRC — canonical (주 surge 모델)

지배방정식과 surge 구성요소 (전부 `models/ADCIRC/source-analysis/` verified 링크):

- **수위(연속)**: [GWCE](../../models/ADCIRC/source-analysis/adcirc-gwce-implementation.md) — generalized wave-continuity로 ζ 산출 (surge 본체). 선형solver는 [ITPACKV JCG](../../models/ADCIRC/source-analysis/adcirc-itpack-solver.md), 실행순서는 [timestep orchestration](../../models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md).
- **유속(운동량)**: [momentum](../../models/ADCIRC/source-analysis/adcirc-momentum-implementation.md) — U,V 2D 운동량(GWCE companion).
- **기상 강제력(surge 구동)**: [met-forcing](../../models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md) — 바람응력 + 기압. NWS 모드 카탈로그는 [storm-surge/ NWS families](../../models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge-nws-families.md) + [foundation](../../models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge-foundation.md).
- **조석–해일 상호작용**: [tidal-forcing](../../models/ADCIRC/source-analysis/adcirc-tidal-forcing.md) — 조석 body-force + SAL. 천해 비선형 결합은 [`03-analysis-methods.md`](03-analysis-methods.md)(Pugh tide-surge separation).
- **바닥마찰**: [nodal-attributes](../../models/ADCIRC/source-analysis/adcirc-nodal-attributes.md) — Manning→Cd 등 공간변화 마찰(surge 진폭 지배 인자).
- **범람(wet/dry)**: [wetting-drying](../../models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md) — NOLIFA/H0/NODECODE 침수.
- **경계·구조물**: [boundary-conditions](../../models/ADCIRC/source-analysis/adcirc-boundary-conditions.md)(radiation/flux/sponge) + [weir-boundary](../../models/ADCIRC/source-analysis/adcirc-weir-boundary.md)(제방·월류).
- **wave setup(해일 가산)**: [SWAN coupling](../../models/ADCIRC/source-analysis/adcirc-swan-coupling.md) — radiation stress가 surge에 추가. wave 측은 [`../waves/06-model-application.md`](../waves/06-model-application.md).
- **경압(보통 surge엔 2D barotropic)**: [3D mode](../../models/ADCIRC/source-analysis/adcirc-3d-mode.md) · [baroclinic coupling](../../models/ADCIRC/source-analysis/adcirc-baroclinic-coupling.md).
- 메시 구축(개인 wide6/wide7 프로젝트)은 canonical 아님 → [`source-analysis/local-workflow/`](../../models/ADCIRC/source-analysis/local-workflow/) (source-needed).

## 4. Delft3D-FLOW / D-Flow FM

- **structured FLOW**: [ADI solver](../../models/Delft3D/source-analysis/delft3d_adi_solver.md)(SUD/UZD double-sweep) — 수위·운동량 implicit. 바람·기압 강제력으로 surge.
- **unstructured FM**: [kernel scheme](../../models/Delft3D/source-analysis/delft3d_dflowfm_kernel_scheme.md)(furu/s1nod Guus-NestedNewton) + [overview](../../models/Delft3D/source-analysis/delft3d_dflowfm_overview.md) · 입력 [mdu](../../models/Delft3D/source-analysis/delft3d_dflowfm_mdu_input.md). 비정형 연안 surge·범람.

## 5. ROMS (+COAWST)

- **barotropic mode**: [2D barotropic](../../models/ROMS/source-analysis/roms_barotropic_2d.md) — fast-mode 수위(surge 성분). 조석 강제는 [tidal forcing](../../models/ROMS/source-analysis/roms_tidal_forcing.md).
- ROMS 단독 surge는 드물고, **COAWST 결합**(wave·sediment·atm)로 활용 — [`models/ROMS/web-refs/roms-official-resources.md`](../../models/ROMS/web-refs/roms-official-resources.md) §3.6.

## 6. EFDC

- **external mode**: [external mode solver](../../models/EFDC/source-analysis/efdc_external_mode_solver.md)(congrad 5-point Jacobi-CG 수위) + [hydro core](../../models/EFDC/source-analysis/efdc_hydro_core.md). 만·하구 천해 surge·범람. 내부 wind-wave는 [waves](../../models/EFDC/source-analysis/efdc_waves.md).

## 7. 검증 (한국 사례)

[`05-examples.md`](05-examples.md)의 관측 검증 case와 대응:
- **Maemi 2003**(마산 최악, source-needed) · **Hinnamnor 2022**(포항 +36cm spike, verified) · **Bolaven 2012**(군산외해 ADCP 잔차, verified)
- 독립 설계모델 검증: 서승원·이화영(2012) pADCIRC+unSWAN 목포 100년 191cm — [[khoa-design-surge-eva-2026]] §4 3중일치.

## 8. 다른 토픽과의 교차

- [`../tides/06-model-application.md`](../tides/06-model-application.md) — 조석 강제(같은 ADCIRC/Delft3D, surge와 동일 SWE에 중첩).
- [`../waves/06-model-application.md`](../waves/06-model-application.md) — wave setup이 surge에 가산(ADCIRC+SWAN / Delft3D-WAVE).
- [`02-theory.md`](02-theory.md) — GWCE 유도 + Pugh §6-7.

## 9. ML 우회 (surrogate)

위 full-physics 모델을 **ML emulator가 대체/보정** — [`07-ml-emulators.md`](07-ml-emulators.md): direct emulator(PACT·Global LI·DeepSurge), bias-corrector(StormNet·HURRI-GAN), 학습전략(Regional surrogate). ADCIRC 출력이 대부분 surrogate의 학습 target.

## 10. 보강 — `verified` 승격·미커버

- **SCHISM** 미커버(본 위키 미수록 모델) — 한반도 surge 연구 다수 사용, 향후 후보.
- Delft3D/ROMS/EFDC surge **한국 적용 사례** 정량 검증은 미보강(현재 ADCIRC 중심).
- 각 모델 surge 입력카드(바람·기압 강제력 포맷) 요약은 source-analysis 본문 참조.

## 11. 연결

- [`01-concept.md`](01-concept.md) · [`02-theory.md`](02-theory.md) · [`03-analysis-methods.md`](03-analysis-methods.md) · [`04-code-and-tools.md`](04-code-and-tools.md) · [`05-examples.md`](05-examples.md) · [`07-ml-emulators.md`](07-ml-emulators.md)
- 모델: [`models/ADCIRC/`](../../models/ADCIRC/) · [`models/Delft3D/`](../../models/Delft3D/) · [`models/ROMS/`](../../models/ROMS/) · [`models/EFDC/`](../../models/EFDC/)
